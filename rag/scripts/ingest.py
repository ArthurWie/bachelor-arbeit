"""Volldurchlauf Korpus → DB.

    python -m scripts.ingest              # Parsen + Indexieren
    python -m scripts.ingest --parse-only # nur Korpus-Sync + Docling
    python -m scripts.ingest --index-only # nur Chunking + Embedding

Quelle ist der eingefrorene SLR-Korpus der Arbeit (library_core/corpus.py),
nicht Zotero: coding_table.csv + Scopus-Export + literature/*.pdf.

Eigenschaften:
- Wiederaufnehmbar: Commit nach JEDEM Dokument.
- Unveränderte Dokumente werden über content_hash übersprungen.
- Indexiert werden ausschließlich Dokumente mit parse_ok = 1 (Schritt 2!).
- Zwei Parse-Durchläufe: erst alle mit ocr=False; Dokumente mit einer Seite
  unter SCAN_CHAR_THRESH Zeichen werden mit is_scan=1 markiert und danach
  mit ocr=True (EasyOCR, en+de) neu geparst.
- Ein neu geparstes Dokument verliert parse_ok und seine Chunks: die
  Sichtprüfung muss wiederholt werden.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import time
from datetime import datetime, timezone

from library_core import chunk as chunk_mod
from library_core import config, corpus, db


def _hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


# ------------------------------------------------------------------ Phase A

def _store_page_offset(
    conn: sqlite3.Connection, doc_row_id: int, parsed, cdoc
) -> str:
    """Druckseiten-Kalibrierung: gedruckte Seite = PDF-Seite + Offset.

    Primärquelle sind die aus den Fußzeilen gelesenen Seitenzahlen. Wo Scopus
    einen Seitenbereich liefert, dient der als Prüfsumme – Abweichungen werden
    gemeldet, nicht stillschweigend übernommen (der Fußzeilen-Wert gewinnt, er
    steht tatsächlich auf der Seite).
    """
    from library_core.parse import page_offset

    db.set_meta(conn, f"page_labels:{doc_row_id}",
                json.dumps(parsed.page_labels, ensure_ascii=False))
    offset = page_offset(parsed.page_labels)

    if offset is None:
        # Rückfallebene: Wenn die Fußzeilen nichts hergeben, Scopus aber einen
        # Seitenbereich nennt, dessen Spanne exakt der PDF-Seitenzahl
        # entspricht, ist die Zuordnung eindeutig. Bereiche, die bei 1 beginnen,
        # sind bei Emerald & Co. artikelrelativ und werden verworfen – lieber
        # ehrlich die PDF-Seite als eine erfundene Druckseite.
        first, last = cdoc.printed_first, cdoc.printed_last
        if (
            first is not None
            and first > 1
            and last - first + 1 == parsed.num_pages
        ):
            db.set_meta(conn, f"page_offset:{doc_row_id}", str(first - 1))
            return (f"Offset {first - 1} aus dem Scopus-Bereich "
                    f"S. {first}–{last} (keine Fußzeilen erkannt; Spanne passt "
                    f"auf {parsed.num_pages} PDF-Seiten)")
        db.delete_meta(conn, f"page_offset:{doc_row_id}")
        return "keine Druckseitenzahlen erkannt → es wird die PDF-Seite zitiert"

    db.set_meta(conn, f"page_offset:{doc_row_id}", str(offset))
    n_obs = len(parsed.page_labels)
    if cdoc.printed_first is None:
        return f"Offset {offset} aus {n_obs} Fußzeilen (kein Scopus-Abgleich möglich)"
    expected = cdoc.printed_first - 1
    if expected == offset:
        return f"Offset {offset} aus {n_obs} Fußzeilen, deckt sich mit Scopus"
    return (
        f"ABWEICHUNG: Offset {offset} aus {n_obs} Fußzeilen, Scopus erwartet "
        f"{expected} (S. {cdoc.printed_first}–{cdoc.printed_last}) – "
        "vor dem Zitieren an einer Seite prüfen"
    )


def _store_parse(
    conn: sqlite3.Connection, doc_row_id: int, parsed, is_scan: bool, cdoc
) -> str:
    conn.execute(
        "UPDATE documents SET full_text = ?, is_scan = ?, parse_ok = 0, "
        "parsed_at = ? WHERE id = ?",
        (parsed.full_text, int(is_scan),
         datetime.now(timezone.utc).isoformat(), doc_row_id),
    )
    db.delete_document_chunks(conn, doc_row_id)
    blocks = [
        {"text": b.text, "section": b.section, "page": b.page,
         "bbox": b.bbox, "kind": b.kind}
        for b in parsed.blocks
    ]
    db.set_meta(conn, f"blocks:{doc_row_id}", json.dumps(blocks, ensure_ascii=False))
    db.set_meta(conn, f"num_pages:{doc_row_id}", str(parsed.num_pages))
    note = _store_page_offset(conn, doc_row_id, parsed, cdoc)
    conn.commit()
    return note


def phase_parse(conn: sqlite3.Connection) -> None:
    from library_core.parse import build_converter, parse_pdf

    docs = corpus.documents()
    print(f"[ingest] {len(docs)} Studien im eingefrorenen Korpus "
          f"({config.CODING_TABLE.name}).")

    converter = build_converter(ocr=False)
    print("[ingest] Durchlauf 1: Docling mit do_ocr=False "
          "(OCR-Verifikation: Zeit pro Dokument beobachten – OCR wäre "
          "um Größenordnungen langsamer).")

    scan_candidates: list[tuple[int, object]] = []

    for cdoc in docs:
        path = cdoc.path
        content_hash = _hash_file(path)
        label = f"{cdoc.study_id} {cdoc.title[:55]}"

        row = conn.execute(
            "SELECT id, content_hash FROM documents WHERE zotero_key = ?",
            (cdoc.study_id,),
        ).fetchone()

        if row is None:
            cur = conn.execute(
                "INSERT INTO documents (zotero_key, title, authors, year, doi, "
                "file_path, content_hash) VALUES (?,?,?,?,?,?,?)",
                (cdoc.study_id, cdoc.title,
                 json.dumps(cdoc.authors, ensure_ascii=False),
                 cdoc.year, cdoc.doi, path, content_hash),
            )
            doc_row_id = cur.lastrowid
        else:
            doc_row_id = row["id"]
            # Metadaten kommen immer aus dem Korpus – bei jedem Lauf auffrischen.
            conn.execute(
                "UPDATE documents SET title=?, authors=?, year=?, doi=?, "
                "file_path=?, content_hash=? WHERE id=?",
                (cdoc.title, json.dumps(cdoc.authors, ensure_ascii=False),
                 cdoc.year, cdoc.doi, path, content_hash, doc_row_id),
            )
            if row["content_hash"] == content_hash and conn.execute(
                "SELECT full_text IS NOT NULL FROM documents WHERE id=?",
                (doc_row_id,),
            ).fetchone()[0]:
                conn.commit()
                # Wiederaufnahme: OCR-Durchlauf ausstehend? Dann nicht skippen.
                if db.get_meta(conn, f"ocr_pending:{doc_row_id}") == "1":
                    scan_candidates.append((doc_row_id, cdoc))
                    print(f"[ingest]   OCR-Durchlauf ausstehend: {label}")
                else:
                    print(f"[ingest]   unverändert, übersprungen: {label}")
                continue

        t0 = time.monotonic()
        parsed = parse_pdf(path, converter)
        dt = time.monotonic() - t0
        is_scan = parsed.is_scan_suspect
        note = _store_parse(conn, doc_row_id, parsed, is_scan, cdoc)
        flag = "  → Scan-Verdacht" if is_scan else ""
        print(f"[ingest]   geparst in {dt:5.1f}s (ocr=False): {label}{flag}")
        print(f"[ingest]     Seitenzahlen: {note}")
        if is_scan:
            # Persistenter Marker: übersteht Abbruch zwischen Pass 1 und 2.
            db.set_meta(conn, f"ocr_pending:{doc_row_id}", "1")
            conn.commit()
            scan_candidates.append((doc_row_id, cdoc))

    if scan_candidates:
        print(f"[ingest] Durchlauf 2: {len(scan_candidates)} Scan-Kandidaten "
              "mit do_ocr=True (EasyOCR, en+de).")
        ocr_converter = build_converter(ocr=True)
        for doc_row_id, cdoc in scan_candidates:
            t0 = time.monotonic()
            parsed = parse_pdf(cdoc.path, ocr_converter)
            dt = time.monotonic() - t0
            note = _store_parse(conn, doc_row_id, parsed, True, cdoc)
            db.delete_meta(conn, f"ocr_pending:{doc_row_id}")
            conn.commit()
            print(f"[ingest]   OCR-geparst in {dt:5.1f}s: {cdoc.study_id} "
                  f"{cdoc.title[:55]}")
            print(f"[ingest]     Seitenzahlen: {note}")

    print("[ingest] Parsen abgeschlossen. Nächster Schritt: Sichtprüfung "
          "(python -m scripts.export_review), dann parse_ok setzen.")


# ------------------------------------------------------------------ Phase B

def phase_index(conn: sqlite3.Connection) -> None:
    from library_core import embed

    db.ensure_index_meta(conn)

    rows = conn.execute(
        "SELECT d.id, d.title, d.year FROM documents d "
        "WHERE d.parse_ok = 1 "
        "AND NOT EXISTS (SELECT 1 FROM chunks c WHERE c.document_id = d.id) "
        "ORDER BY d.id"
    ).fetchall()
    skipped = conn.execute(
        "SELECT COUNT(*) FROM documents WHERE parse_ok = 0"
    ).fetchone()[0]
    if skipped:
        print(f"[ingest] {skipped} Dokument(e) ohne parse_ok=1 – werden NICHT "
              "indexiert (Sichtprüfung ausstehend).")
    if not rows:
        print("[ingest] Nichts zu indexieren.")
        return

    embed.get_model()  # lädt + verifiziert fp8, schlägt sonst hart fehl

    for row in rows:
        blocks_json = db.get_meta(conn, f"blocks:{row['id']}")
        if not blocks_json:
            print(f"[ingest]   KEINE Blockdaten für Dokument {row['id']} "
                  f"({row['title'][:50]}) – erst neu parsen.")
            continue
        from library_core.parse import Block
        blocks = [Block(**b) for b in json.loads(blocks_json)]
        chunks = chunk_mod.chunk_blocks(
            blocks, title=row["title"], year=row["year"],
            count_tokens=embed.count_tokens,
        )
        if not chunks:
            print(f"[ingest]   0 Chunks für Dokument {row['id']} – prüfen!")
            continue

        vectors = embed.encode_documents([c.embed_text for c in chunks])

        for c, vec in zip(chunks, vectors):
            cur = conn.execute(
                "INSERT INTO chunks (document_id, ordinal, section, page_start, "
                "page_end, bbox, text, embed_text, token_count) "
                "VALUES (?,?,?,?,?,?,?,?,?)",
                (row["id"], c.ordinal, c.section, c.page_start, c.page_end,
                 json.dumps(c.bbox, ensure_ascii=False), c.text, c.embed_text,
                 c.token_count),
            )
            conn.execute(
                "INSERT INTO chunks_vec (chunk_id, embedding) VALUES (?, ?)",
                (cur.lastrowid, vec.astype("float32").tobytes()),
            )
        conn.commit()   # Wiederaufnahme: nach jedem Dokument
        print(f"[ingest]   indexiert: {row['title'][:60]} "
              f"({len(chunks)} Chunks)")

    n_chunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    n_vec = conn.execute("SELECT COUNT(*) FROM chunks_vec").fetchone()[0]
    n_fts = conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0]
    print(f"[ingest] Fertig. chunks={n_chunks}, chunks_vec={n_vec}, "
          f"chunks_fts={n_fts} (alle drei müssen gleich sein).")
    if not (n_chunks == n_vec == n_fts):
        raise RuntimeError(
            f"Inkonsistenz: chunks={n_chunks}, chunks_vec={n_vec}, "
            f"chunks_fts={n_fts}."
        )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parse-only", action="store_true")
    ap.add_argument("--index-only", action="store_true")
    ap.add_argument("--db", default=None, help="Pfad zur SQLite-Datei")
    args = ap.parse_args()

    conn = db.connect(args.db)
    db.init_db(conn)

    if not args.index_only:
        phase_parse(conn)
    if not args.parse_only:
        phase_index(conn)


if __name__ == "__main__":
    main()
