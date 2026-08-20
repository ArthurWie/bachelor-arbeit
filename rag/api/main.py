"""FastAPI-Schicht für das Frontend (Schritt 8).

Importiert die Suchlogik ausschließlich aus library_core – kein dupliziertes
Retrieval. Start:  uvicorn api.main:app --port 8000
"""

from __future__ import annotations

import csv
import json
import sqlite3
from datetime import date
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from library_core import config, db, retrieve

app = FastAPI(title="library-rag")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _conn() -> sqlite3.Connection:
    return db.connect()


class SearchFilters(BaseModel):
    year_min: int | None = None


class SearchRequest(BaseModel):
    query: str
    filters: SearchFilters | None = None
    k: int | None = None


@app.get("/api/documents")
def list_documents() -> list[dict]:
    rows = _conn().execute(
        "SELECT d.id, d.zotero_key, d.title, d.authors, d.year, d.doi, "
        "       d.is_scan, d.parse_ok, COUNT(c.id) AS n_chunks "
        "FROM documents d LEFT JOIN chunks c ON c.document_id = d.id "
        "GROUP BY d.id ORDER BY d.year, d.title"
    ).fetchall()
    return [
        {**dict(r), "authors": json.loads(r["authors"] or "[]")} for r in rows
    ]


@app.get("/api/documents/{document_id}/file")
def document_file(document_id: int) -> FileResponse:
    row = _conn().execute(
        "SELECT file_path, title FROM documents WHERE id = ?", (document_id,)
    ).fetchone()
    if row is None:
        raise HTTPException(404, "Unbekanntes Dokument")
    path = Path(row["file_path"] or "")
    if not path.is_file():
        raise HTTPException(410, f"PDF nicht (mehr) am erwarteten Ort: {path}")
    return FileResponse(path, media_type="application/pdf", filename=path.name)


@app.post("/api/search")
def search(req: SearchRequest) -> list[dict]:
    year_min = req.filters.year_min if req.filters else None
    try:
        results = retrieve.search(
            req.query, year_min=year_min, k=req.k or config.FINAL_K, conn=_conn()
        )
    except (RuntimeError, ImportError, sqlite3.OperationalError) as exc:
        # z. B. "CUDA nicht verfügbar … Anhalten" oder fehlende/leere DB –
        # Meldung sichtbar machen, statt sie hinter einem nackten 500 zu
        # verstecken.
        raise HTTPException(503, str(exc)) from exc
    return [
        {
            "chunk_id": r.chunk_id,
            "document_id": r.document_id,
            "title": r.title,
            "authors": r.authors,
            "year": r.year,
            "section": r.section,
            "page_start": r.page_start,
            "page_end": r.page_end,
            "printed_start": r.printed_start,   # gedruckte Seite, zum Zitieren
            "printed_end": r.printed_end,       # None = keine erkannt
            "text": r.text,
            "score": r.score,
        }
        for r in results
    ]


# --- Zellen-Audit der Kodiertabelle (19. Aug 2026) ---------------------------
# Ein Schritt = eine Zelle der Anhangstabelle; Belege kommen aus den Evidenz-
# JSONs des Dossiers (corpus/evidence/Sxx.json). Urteile landen append-only in
# corpus/author_audit.csv (letzte Zeile pro Zelle gilt; "clear" hebt auf).
# coding_table.csv bleibt unberührt.

THESIS_ROOT = Path(__file__).resolve().parents[2]
AUDIT_CSV = THESIS_ROOT / "corpus" / "author_audit.csv"
EVIDENCE_DIR = THESIS_ROOT / "corpus" / "evidence"
# Zellen, die bei der Flag-Aufarbeitung (20. Aug 2026) geändert oder neu belegt
# wurden — im Viewer als "2. Pass" markiert, damit nur sie nachgeprüft werden.
SECOND_PASS_CSV = THESIS_ROOT / "corpus" / "audit_second_pass.csv"


def _read_second_pass() -> set[tuple[str, str]]:
    if not SECOND_PASS_CSV.exists():
        return set()
    with open(SECOND_PASS_CSV, encoding="utf-8", newline="") as f:
        return {(r["study_id"], r["column"]) for r in csv.DictReader(f)}

# Reihenfolge der gedruckten Anhangstabellen (A.1, A.2, dann ungedruckte Felder)
AUDIT_COLS = [
    "country_region", "sample", "method", "ai_measure",
    "outcome_construct", "performance_measure", "ca_measure",
    "effect_direction", "conditions", "key_finding",
    "theoretical_lens", "industry", "quality_notes",
]


class AuditVerdict(BaseModel):
    study_id: str
    column: str
    verdict: str  # ok | flag | clear
    note: str = ""


def _read_verdicts() -> dict[str, dict]:
    if not AUDIT_CSV.exists():
        return {}
    out: dict[str, dict] = {}
    with open(AUDIT_CSV, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            key = f"{row['study_id']}|{row['column']}"
            if row["verdict"] == "clear":
                out.pop(key, None)
            else:
                out[key] = {"verdict": row["verdict"], "note": row["note"],
                            "date": row["date"]}
    return out


def _load_render_tsv(path: Path) -> dict[tuple[str, str], str]:
    """appendix_condensed.tsv / appendix_overrides.tsv: die Wortlaute, die in
    der gedruckten Anhangstabelle stehen (Rendering-Schicht, "notes" ungedruckt)."""
    out: dict[tuple[str, str], str] = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if row["study_id"].startswith("#") or row["column"] == "notes":
                    continue
                out[(row["study_id"], row["column"])] = row["text"].strip()
    return out


@app.get("/api/audit/queue")
def audit_queue() -> dict:
    with open(THESIS_ROOT / "corpus" / "coding_table.csv",
              encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    condensed = _load_render_tsv(THESIS_ROOT / "corpus" / "appendix_condensed.tsv")
    overrides = _load_render_tsv(THESIS_ROOT / "corpus" / "appendix_overrides.tsv")
    second_pass = _read_second_pass()
    steps = []
    for r in rows:
        sid = r["study_id"]
        ev_path = EVIDENCE_DIR / f"{sid}.json"
        ev = (json.loads(ev_path.read_text(encoding="utf-8"))
              if ev_path.exists() else {"quotes": []})
        label = f"{r['authors'].split(';')[0].strip()} ({r['year']}) · {r['journal']}"
        row_note = (ev.get("row_check") or {}).get("notes")
        for col in AUDIT_COLS:
            quotes = [q for q in ev.get("quotes", [])
                      if col in q.get("fields", [])]
            if not r[col].strip() and not quotes:
                continue  # leere Zelle ohne Belegstelle: nichts zu prüfen
            steps.append({
                "study_id": sid,
                "document_id": int(sid[1:]),
                "label": label,
                "column": col,
                "coded": r[col],
                "printed": condensed.get((sid, col)) or overrides.get((sid, col)),
                "quotes": [{
                    "quote": q["quote"],
                    "ctrl_f": q.get("ctrl_f"),
                    "pdf_page": (q.get("located_pdf_pages")
                                 or [q.get("pdf_page") or 1])[0],
                    "printed_pages": q.get("printed_pages"),
                    "verdict": q.get("verdict"),
                    "supports": q.get("supports"),
                    "tension": q.get("tension"),
                } for q in quotes],
                "flagged": any(q.get("tension") for q in quotes),
                "recheck": (sid, col) in second_pass,
                "row_note": row_note,
            })
    return {"steps": steps, "verdicts": _read_verdicts()}


@app.post("/api/audit/verdict")
def audit_verdict(v: AuditVerdict) -> dict:
    if v.verdict not in ("ok", "flag", "clear"):
        raise HTTPException(422, "verdict muss ok, flag oder clear sein")
    if v.column not in AUDIT_COLS:
        raise HTTPException(422, f"unbekannte Spalte {v.column!r}")
    is_new = not AUDIT_CSV.exists()
    with open(AUDIT_CSV, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["study_id", "column", "verdict", "note", "date"])
        w.writerow([v.study_id, v.column, v.verdict,
                    v.note.replace("\n", " "), date.today().isoformat()])
    return {"ok": True}


@app.get("/api/chunks/{chunk_id}")
def chunk(chunk_id: int) -> dict:
    row = _conn().execute(
        "SELECT c.id, c.document_id, c.section, c.page_start, c.page_end, "
        "       c.bbox, c.text, d.title, d.authors, d.year "
        "FROM chunks c JOIN documents d ON d.id = c.document_id "
        "WHERE c.id = ?",
        (chunk_id,),
    ).fetchone()
    if row is None:
        raise HTTPException(404, "Unbekannter Chunk")
    return {
        "chunk_id": row["id"],
        "document_id": row["document_id"],
        "section": row["section"],
        "page_start": row["page_start"],
        "page_end": row["page_end"],
        "bbox": json.loads(row["bbox"] or "[]"),
        "text": row["text"],
        "title": row["title"],
        "authors": json.loads(row["authors"] or "[]"),
        "year": row["year"],
    }
