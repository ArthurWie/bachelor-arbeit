"""FastAPI-Schicht für das Frontend (Schritt 8).

Importiert die Suchlogik ausschließlich aus library_core – kein dupliziertes
Retrieval. Start:  uvicorn api.main:app --port 8000
"""

from __future__ import annotations

import json
import sqlite3
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
