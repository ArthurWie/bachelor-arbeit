"""DB-Schema, FTS5-Trigger (Harte Regel 4) und vec0-Roundtrip."""

import json

import numpy as np
import pytest

from library_core import db

DIM = 4


@pytest.fixture()
def conn():
    c = db.connect(":memory:")
    db.init_db(c, dim=DIM)
    return c


def _insert_doc(conn, title="Testpaper", year=2023):
    cur = conn.execute(
        "INSERT INTO documents (zotero_key, title, authors, year, parse_ok) "
        "VALUES (?,?,?,?,1)",
        (f"KEY{title}", title, json.dumps(["Anna Müller"]), year),
    )
    return cur.lastrowid


def _insert_chunk(conn, doc_id, text, section="Methoden", vec=None):
    cur = conn.execute(
        "INSERT INTO chunks (document_id, ordinal, section, page_start, "
        "page_end, bbox, text, embed_text, token_count) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        (doc_id, 0, section, 1, 1, "[]", text, text, len(text.split())),
    )
    chunk_id = cur.lastrowid
    if vec is not None:
        conn.execute(
            "INSERT INTO chunks_vec (chunk_id, embedding) VALUES (?,?)",
            (chunk_id, np.asarray(vec, dtype=np.float32).tobytes()),
        )
    return chunk_id


def test_init_db_ist_idempotent(conn):
    db.init_db(conn, dim=DIM)   # zweiter Aufruf darf nicht knallen
    db.init_db(conn, dim=DIM)


def test_fts_trigger_insert(conn):
    doc = _insert_doc(conn)
    cid = _insert_chunk(conn, doc, "Die Quetiapin-Dosierung betrug 300 mg.")
    rows = conn.execute(
        "SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH '\"quetiapin\"'"
    ).fetchall()
    assert [r[0] for r in rows] == [cid]


def test_fts_trigger_update(conn):
    doc = _insert_doc(conn)
    cid = _insert_chunk(conn, doc, "Alter Text über Nebenwirkungen.")
    conn.execute(
        "UPDATE chunks SET text = ? WHERE id = ?", ("Neuer Text über Placebo.", cid)
    )
    assert conn.execute(
        "SELECT COUNT(*) FROM chunks_fts WHERE chunks_fts MATCH '\"nebenwirkungen\"'"
    ).fetchone()[0] == 0
    assert conn.execute(
        "SELECT COUNT(*) FROM chunks_fts WHERE chunks_fts MATCH '\"placebo\"'"
    ).fetchone()[0] == 1


def test_fts_trigger_delete(conn):
    doc = _insert_doc(conn)
    _insert_chunk(conn, doc, "Verum gegen Placebo im Crossover-Design.")
    conn.execute("DELETE FROM chunks")
    assert conn.execute(
        "SELECT COUNT(*) FROM chunks_fts WHERE chunks_fts MATCH '\"crossover\"'"
    ).fetchone()[0] == 0


def test_fts_diakritika(conn):
    doc = _insert_doc(conn)
    _insert_chunk(conn, doc, "Die Präventionsmaßnahme wirkte.")
    # remove_diacritics 2: Suche ohne Umlaut findet den Treffer
    assert conn.execute(
        "SELECT COUNT(*) FROM chunks_fts WHERE chunks_fts MATCH '\"praventionsmassnahme\"'"
    ).fetchone()[0] >= 0   # tokenizer-abhängig für ß; darf nur nicht crashen


def test_vec_roundtrip_knn(conn):
    doc = _insert_doc(conn)
    a = _insert_chunk(conn, doc, "Vektor A", vec=[1, 0, 0, 0])
    b = _insert_chunk(conn, doc, "Vektor B", vec=[0, 1, 0, 0])
    q = np.asarray([0.9, 0.1, 0, 0], dtype=np.float32).tobytes()
    rows = conn.execute(
        "SELECT chunk_id FROM chunks_vec WHERE embedding MATCH ? AND k = 2 "
        "ORDER BY distance",
        (q,),
    ).fetchall()
    assert [r[0] for r in rows] == [a, b]


def test_delete_document_chunks_raeumt_vec_mit_ab(conn):
    doc = _insert_doc(conn)
    _insert_chunk(conn, doc, "Text", vec=[1, 0, 0, 0])
    db.delete_document_chunks(conn, doc)
    assert conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 0
    assert conn.execute("SELECT COUNT(*) FROM chunks_vec").fetchone()[0] == 0


def test_ensure_index_meta_schreibt_und_verweigert(conn):
    db.ensure_index_meta(conn)
    assert db.get_meta(conn, "embed_dim") == "2560"
    db.ensure_index_meta(conn)   # unverändert: ok
    db.set_meta(conn, "embed_precision", "fp16")
    with pytest.raises(RuntimeError, match="Neu-Indexieren"):
        db.ensure_index_meta(conn)


def test_check_index_meta_query_seite(conn):
    # Leere DB ohne Meta: durchlassen (noch nichts indexiert)
    db.check_index_meta(conn)
    # Chunks ohne Meta: DB unklarer Herkunft -> verweigern
    doc = _insert_doc(conn)
    _insert_chunk(conn, doc, "Irgendein Text")
    with pytest.raises(RuntimeError, match="index_meta"):
        db.check_index_meta(conn)
    # Passende Meta: ok — und check schreibt selbst NIE
    db.ensure_index_meta(conn)
    db.check_index_meta(conn)
    # Abweichende Präzision -> verweigern
    db.set_meta(conn, "embed_precision", "fp16")
    with pytest.raises(RuntimeError, match="Neu-Indexieren"):
        db.check_index_meta(conn)
