"""Hybrides Retrieval: exakte Vektorsuche + BM25, RRF-Fusion, Cross-Encoder-
Reranking.

Harte Regeln (§5):
- RRF statt Score-Addition: BM25 ist unbegrenzt positiv, Cosine liegt in
  [-1,1]; deren Summe ist bedeutungslos. score(d) = Σ 1/(RRF_K + rank(d)).
- Exakte Vektorsuche, kein ANN – bei ~5.000 Vektoren alle Distanzen rechnen.
- ALLE fusionierten Kandidaten gehen in den Reranker, kein Kürzen davor.
- Reranker einmal global laden, nie pro Query.
- Metadatenfilter (year_min) wird VOR der Suche angewandt.
"""

from __future__ import annotations

import json
import re
import sqlite3
import threading
from collections import defaultdict
from dataclasses import dataclass

import numpy as np

from library_core import config, db
from library_core import embed as embed_mod

_reranker = None
_rr_lock = threading.Lock()

_HALT_NO_CUDA_RERANK = (
    "CUDA ist nicht verfügbar. Der Reranker ist auf fp16 auf der GPU "
    "festgelegt; kein stiller Präzisions-Fallback. Bitte auf dem "
    "Zielrechner ausführen. Anhalten."
)


@dataclass
class SearchResult:
    chunk_id: int
    document_id: int
    title: str
    authors: list[str]
    year: int | None
    section: str
    page_start: int          # PDF-Seite (zum Aufblättern/Nachprüfen)
    page_end: int
    text: str
    score: float             # Sigmoid über Reranker-Logit, [0,1]
    printed_start: int | None = None   # gedruckte Seitenzahl (zum Zitieren)
    printed_end: int | None = None     # None = keine erkannt


# --------------------------------------------------------------------- RRF

def rrf(rank_lists: list[list[int]], k: int = config.RRF_K) -> list[int]:
    """Reciprocal Rank Fusion über beliebig viele Ranglisten.
    Behalten wird ALLES, es wird nur neu geordnet."""
    scores: dict[int, float] = defaultdict(float)
    for lst in rank_lists:
        for rank, cid in enumerate(lst, start=1):
            scores[cid] += 1.0 / (k + rank)
    return sorted(scores, key=lambda cid: (-scores[cid], cid))


# ------------------------------------------------------------ Kandidatensuche

def _fts_match_expr(query: str) -> str:
    """Query in einen sicheren FTS5-MATCH-Ausdruck übersetzen (OR-verknüpfte
    Phrasenterme; die Präzision stellt der Reranker her, BM25 sorgt für
    lexikalischen Recall)."""
    tokens = re.findall(r"[^\W_]+", query, re.UNICODE)
    return " OR ".join(f'"{t}"' for t in tokens)


def fts_search(
    conn: sqlite3.Connection,
    query: str,
    limit: int = config.CAND_PER_METHOD,
    year_min: int | None = None,
) -> list[int]:
    match = _fts_match_expr(query)
    if not match:
        return []
    if year_min is None:
        rows = conn.execute(
            "SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH ? "
            "ORDER BY rank LIMIT ?",
            (match, limit),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT f.rowid FROM chunks_fts f "
            "JOIN chunks c ON c.id = f.rowid "
            "JOIN documents d ON d.id = c.document_id "
            "WHERE chunks_fts MATCH ? AND d.year >= ? "
            "ORDER BY rank LIMIT ?",
            (match, year_min, limit),
        ).fetchall()
    return [r[0] for r in rows]


def _allowed_chunk_ids(conn: sqlite3.Connection, year_min: int) -> list[int]:
    rows = conn.execute(
        "SELECT c.id FROM chunks c JOIN documents d ON d.id = c.document_id "
        "WHERE d.year >= ?",
        (year_min,),
    ).fetchall()
    return [r[0] for r in rows]


def vec_search(
    conn: sqlite3.Connection,
    query_vec: np.ndarray,
    limit: int = config.CAND_PER_METHOD,
    year_min: int | None = None,
) -> list[int]:
    """Exakte KNN-Suche über sqlite-vec (brute force, kein ANN)."""
    blob = np.asarray(query_vec, dtype=np.float32).tobytes()
    sql = "SELECT chunk_id FROM chunks_vec WHERE embedding MATCH ? AND k = ?"
    if year_min is not None:
        allowed = _allowed_chunk_ids(conn, year_min)
        if not allowed:
            return []
        # Filter VOR der Suche: IN-Constraint auf den Primärschlüssel
        # schränkt den KNN-Scan ein (sqlite-vec Pre-Filtering).
        sql += f" AND chunk_id IN ({','.join(str(int(i)) for i in allowed)})"
    sql += " ORDER BY distance"
    rows = conn.execute(sql, (blob, limit)).fetchall()
    return [r[0] for r in rows]


def _hybrid_lists(
    conn: sqlite3.Connection, query: str, year_min: int | None
) -> list[list[int]]:
    qv = embed_mod.encode_query(query)
    dense = vec_search(conn, qv, limit=config.CAND_PER_METHOD, year_min=year_min)
    sparse = fts_search(conn, query, limit=config.CAND_PER_METHOD, year_min=year_min)
    return [dense, sparse]


# ---------------------------------------------------------------- Reranking

def get_reranker():
    """bge-reranker-v2-m3 in fp16, einmal global laden (Harte Regel 9)."""
    global _reranker
    if _reranker is not None:
        return _reranker
    with _rr_lock:
        if _reranker is not None:
            return _reranker
        import torch
        from sentence_transformers import CrossEncoder

        if not torch.cuda.is_available():
            raise RuntimeError(_HALT_NO_CUDA_RERANK)
        _reranker = CrossEncoder(
            config.RERANK_MODEL,
            max_length=config.RERANK_MAX_LEN,
            device="cuda",
            model_kwargs={"torch_dtype": torch.float16},
        )
    return _reranker


def _rerank_scores(query: str, texts: list[str]) -> np.ndarray:
    """Reranker-Scores als Sigmoid-Wahrscheinlichkeiten in [0,1].
    Harte Regel 11: bei CUDA-OOM Batchgröße senken, nie das Modell tauschen."""
    import torch

    ce = get_reranker()
    pairs = [(query, t) for t in texts]
    batch_size = 32
    while True:
        try:
            scores = np.asarray(
                ce.predict(pairs, batch_size=batch_size), dtype=np.float64
            )
            break
        except torch.cuda.OutOfMemoryError:
            if batch_size <= 1:
                raise
            batch_size = max(1, batch_size // 2)
            torch.cuda.empty_cache()
            print(f"[rerank] CUDA-OOM – batch_size gesenkt auf {batch_size}")
    if scores.size and (scores.min() < 0.0 or scores.max() > 1.0):
        scores = 1.0 / (1.0 + np.exp(-scores))   # rohe Logits -> Sigmoid
    return scores


def _fetch_rows(conn: sqlite3.Connection, chunk_ids: list[int]) -> list[sqlite3.Row]:
    if not chunk_ids:
        return []
    placeholder = ",".join("?" for _ in chunk_ids)
    rows = conn.execute(
        f"""SELECT c.id AS chunk_id, c.document_id, c.section, c.page_start,
                   c.page_end, c.text, d.title, d.authors, d.year
            FROM chunks c JOIN documents d ON d.id = c.document_id
            WHERE c.id IN ({placeholder})""",
        chunk_ids,
    ).fetchall()
    by_id = {r["chunk_id"]: r for r in rows}
    return [by_id[cid] for cid in chunk_ids if cid in by_id]


def _to_result(
    row: sqlite3.Row, score: float, offsets: dict[int, int] | None = None
) -> SearchResult:
    offset = (offsets or {}).get(row["document_id"])
    return SearchResult(
        chunk_id=row["chunk_id"],
        document_id=row["document_id"],
        title=row["title"],
        authors=json.loads(row["authors"] or "[]"),
        year=row["year"],
        section=row["section"],
        page_start=row["page_start"],
        page_end=row["page_end"],
        text=row["text"],
        score=float(score),
        printed_start=None if offset is None else row["page_start"] + offset,
        printed_end=None if offset is None else row["page_end"] + offset,
    )


def _rerank_rows(
    query: str, rows: list[sqlite3.Row], offsets: dict[int, int] | None = None
) -> list[SearchResult]:
    if not rows:
        return []
    scores = _rerank_scores(query, [r["text"] for r in rows])
    ranked = sorted(zip(rows, scores), key=lambda p: -p[1])
    return [_to_result(r, s, offsets) for r, s in ranked]


# -------------------------------------------------------------------- Suche

def search(
    query: str,
    year_min: int | None = None,
    k: int = config.FINAL_K,
    conn: sqlite3.Connection | None = None,
) -> list[SearchResult]:
    conn = conn or db.connect()
    db.check_index_meta(conn)                    # Harte Regel 3, Query-Seite
    fused = rrf(_hybrid_lists(conn, query, year_min), k=config.RRF_K)
    rows = _fetch_rows(conn, fused)              # ALLE Kandidaten
    return _rerank_rows(query, rows, db.page_offsets(conn))[:k]


def search_multi(
    queries: list[str],
    k: int = config.FINAL_K,
    conn: sqlite3.Connection | None = None,
) -> list[SearchResult]:
    """Mehrere Query-Varianten (Umformulierungen + HyDE) per RRF fusionieren.
    Gerankt wird gegen die erste Query (die Originalfrage)."""
    if not queries:
        return []
    conn = conn or db.connect()
    db.check_index_meta(conn)                    # Harte Regel 3, Query-Seite
    lists: list[list[int]] = []
    for q in queries:
        lists.extend(_hybrid_lists(conn, q, None))
    fused = rrf(lists, k=config.RRF_K)
    rows = _fetch_rows(conn, fused)
    return _rerank_rows(queries[0], rows, db.page_offsets(conn))[:k]


def find_documents(
    query: str,
    k: int = 5,
    conn: sqlite3.Connection | None = None,
) -> list[dict]:
    """Ganze Dokumente auswählen: Chunk-Treffer pro Dokument aggregieren
    (Summe der Top-3-Chunk-Scores), mit Belegstellen als Begründung."""
    conn = conn or db.connect()
    results = search(query, k=40, conn=conn)
    per_doc: dict[int, list[SearchResult]] = defaultdict(list)
    for r in results:
        per_doc[r.document_id].append(r)
    scored = []
    for doc_id, hits in per_doc.items():
        hits.sort(key=lambda r: -r.score)
        scored.append({
            "document_id": doc_id,
            "title": hits[0].title,
            "authors": hits[0].authors,
            "year": hits[0].year,
            "score": sum(h.score for h in hits[:3]),
            "evidence": [
                {"chunk_id": h.chunk_id, "section": h.section,
                 "page_start": h.page_start, "page_end": h.page_end,
                 "printed_start": h.printed_start, "printed_end": h.printed_end,
                 "score": h.score}
                for h in hits[:2]
            ],
        })
    scored.sort(key=lambda d: -d["score"])
    return scored[:k]


def chunk_context(
    conn: sqlite3.Connection, chunk_id: int, window: int = 1
) -> list[sqlite3.Row]:
    """Angrenzende Chunks (per ordinal) desselben Dokuments, inkl. des
    angefragten Chunks, in Lesereihenfolge."""
    base = conn.execute(
        "SELECT document_id, ordinal FROM chunks WHERE id = ?", (chunk_id,)
    ).fetchone()
    if base is None:
        return []
    return conn.execute(
        """SELECT c.id AS chunk_id, c.document_id, c.ordinal, c.section,
                  c.page_start, c.page_end, c.text, d.title, d.authors, d.year
           FROM chunks c JOIN documents d ON d.id = c.document_id
           WHERE c.document_id = ? AND c.ordinal BETWEEN ? AND ?
           ORDER BY c.ordinal""",
        (base["document_id"], base["ordinal"] - window, base["ordinal"] + window),
    ).fetchall()
