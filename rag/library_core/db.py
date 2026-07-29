"""SQLite-Schema, Trigger und Verbindungsaufbau.

Eine Datei, sqlite-vec als Extension. `init_db()` ist idempotent und legt
Schema UND Trigger an. Die FTS5-Trigger sind Pflicht: External-Content-
Tabellen pflegen sich nicht selbst, ohne Trigger findet BM25 stillschweigend
nichts (Harte Regel 4).
"""

from __future__ import annotations

import sqlite3

import sqlite_vec

from library_core import config

_SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
  id            INTEGER PRIMARY KEY,
  zotero_key    TEXT UNIQUE,
  title         TEXT,
  authors       TEXT,              -- JSON-Array
  year          INTEGER,
  doi           TEXT,
  file_path     TEXT,
  full_text     TEXT,              -- kompletter Text mit [S. N]-Markern
  content_hash  TEXT,
  is_scan       INTEGER DEFAULT 0,
  parse_ok      INTEGER DEFAULT 0, -- wird in Schritt 2 manuell gesetzt
  parsed_at     TEXT
);

CREATE TABLE IF NOT EXISTS chunks (
  id            INTEGER PRIMARY KEY,
  document_id   INTEGER REFERENCES documents(id) ON DELETE CASCADE,
  ordinal       INTEGER,
  section       TEXT,
  page_start    INTEGER,
  page_end      INTEGER,
  bbox          TEXT,              -- JSON [{page,x0,y0,x1,y1,coord_origin}]
  text          TEXT,              -- Original. Wird zitiert.
  embed_text    TEXT,              -- mit Kontextpräfix. Wird embedded.
  token_count   INTEGER
);

CREATE TABLE IF NOT EXISTS index_meta (
  key TEXT PRIMARY KEY, value TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
  text, section, content='chunks', content_rowid='id',
  tokenize='unicode61 remove_diacritics 2'
);

CREATE TABLE IF NOT EXISTS eval_questions (
  id INTEGER PRIMARY KEY,
  question TEXT,
  gold_chunk_ids TEXT,             -- JSON-Array
  kind TEXT                        -- fact | concept | cross | negative
);
"""

_TRIGGERS = """
CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
  INSERT INTO chunks_fts(rowid, text, section) VALUES (new.id, new.text, new.section);
END;

CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
  INSERT INTO chunks_fts(chunks_fts, rowid, text, section)
    VALUES('delete', old.id, old.text, old.section);
END;

CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
  INSERT INTO chunks_fts(chunks_fts, rowid, text, section)
    VALUES('delete', old.id, old.text, old.section);
  INSERT INTO chunks_fts(rowid, text, section) VALUES (new.id, new.text, new.section);
END;
"""


def connect(db_path: str | None = None) -> sqlite3.Connection:
    """Verbindung mit geladener sqlite-vec-Extension und aktiven Foreign Keys."""
    conn = sqlite3.connect(db_path or config.DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    # sqlite-vec MUSS geladen sein, bevor chunks_vec angesprochen wird.
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    return conn


def init_db(conn: sqlite3.Connection, dim: int = config.EMBED_DIM) -> None:
    """Idempotent: beliebig oft ausführbar. `dim` ist nur für Tests variabel."""
    conn.executescript(_SCHEMA)
    conn.executescript(
        "CREATE VIRTUAL TABLE IF NOT EXISTS chunks_vec USING vec0(\n"
        f"  chunk_id INTEGER PRIMARY KEY, embedding FLOAT[{dim}]\n"
        ");"
    )
    conn.executescript(_TRIGGERS)
    conn.commit()


# ---------------------------------------------------------------- index_meta

def get_meta(conn: sqlite3.Connection, key: str) -> str | None:
    row = conn.execute("SELECT value FROM index_meta WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else None


def set_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute(
        "INSERT INTO index_meta(key, value) VALUES(?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (key, str(value)),
    )


def delete_meta(conn: sqlite3.Connection, key: str) -> None:
    conn.execute("DELETE FROM index_meta WHERE key = ?", (key,))


def page_offsets(conn: sqlite3.Connection) -> dict[int, int]:
    """document_id → Offset, mit `gedruckte Seite = PDF-Seite + Offset`.

    Dokumente ohne erkannte Druckseitenzahl fehlen in der Map; für die wird
    die PDF-Seite zitiert und als solche gekennzeichnet. Gefüllt beim Ingest
    (scripts/ingest.py), siehe library_core.parse.page_offset.
    """
    rows = conn.execute(
        "SELECT key, value FROM index_meta WHERE key LIKE 'page_offset:%'"
    ).fetchall()
    offsets: dict[int, int] = {}
    for r in rows:
        try:
            offsets[int(r["key"].split(":", 1)[1])] = int(r["value"])
        except (ValueError, IndexError):
            continue
    return offsets


_META_EXPECTED = lambda: {  # noqa: E731 – Config erst bei Aufruf lesen
    "embed_model": config.EMBED_MODEL,
    "embed_precision": config.EMBED_PRECISION,
    "embed_dim": str(config.EMBED_DIM),
}


def _meta_mismatches(conn: sqlite3.Connection) -> tuple[dict, dict]:
    expected = _META_EXPECTED()
    stored = {k: get_meta(conn, k) for k in expected}
    mismatches = {
        k: (stored[k], expected[k]) for k in expected if stored[k] != expected[k]
    }
    return stored, mismatches


def _raise_meta_mismatch(mismatches: dict) -> None:
    detail = ", ".join(
        f"{k}: DB={s!r} vs. Config={e!r}" for k, (s, e) in mismatches.items()
    )
    raise RuntimeError(
        "index_meta passt nicht zur Config – der bestehende Index wurde mit "
        f"anderen Einstellungen gebaut ({detail}). Neu-Indexieren nötig: "
        "DB-Datei löschen oder verschieben und `python -m scripts.ingest` neu laufen lassen."
    )


def ensure_index_meta(conn: sqlite3.Connection) -> None:
    """Harte Regel 3 (Ingest-Seite): Beim ersten Ingest werden die Werte
    geschrieben, danach wird jede Abweichung zur Config mit Abbruch quittiert
    (Neu-Indexieren nötig)."""
    stored, mismatches = _meta_mismatches(conn)
    if all(v is None for v in stored.values()):
        for k, v in _META_EXPECTED().items():
            set_meta(conn, k, v)
        conn.commit()
        return
    if mismatches:
        _raise_meta_mismatch(mismatches)


def check_index_meta(conn: sqlite3.Connection) -> None:
    """Harte Regel 3 (Query-Seite): rein lesende Prüfung bei JEDEM Lauf.
    Schreibt nie – eine fremde DB bekommt keine Meta-Werte untergeschoben.
    Leere Meta ist nur zulässig, solange noch nichts indexiert wurde."""
    stored, mismatches = _meta_mismatches(conn)
    if all(v is None for v in stored.values()):
        n_chunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        if n_chunks:
            raise RuntimeError(
                f"Diese DB enthält {n_chunks} Chunks, aber keine index_meta-"
                "Angaben zu Modell/Präzision. Herkunft unklar – nicht gegen "
                "sie suchen. Neu-Indexieren nötig."
            )
        return
    if mismatches:
        _raise_meta_mismatch(mismatches)


# ------------------------------------------------------------------- Löschen

def delete_document_chunks(conn: sqlite3.Connection, document_id: int) -> None:
    """Chunks eines Dokuments inkl. Vektoren entfernen.

    chunks_fts wird über den DELETE-Trigger mitgepflegt; chunks_vec ist eine
    vec0-Tabelle ohne Trigger-/FK-Anbindung und muss explizit geleert werden.
    """
    ids = [r[0] for r in conn.execute(
        "SELECT id FROM chunks WHERE document_id = ?", (document_id,)
    )]
    if ids:
        conn.executemany("DELETE FROM chunks_vec WHERE chunk_id = ?", [(i,) for i in ids])
        conn.execute("DELETE FROM chunks WHERE document_id = ?", (document_id,))
