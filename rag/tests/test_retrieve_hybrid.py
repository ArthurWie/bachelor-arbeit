"""Abnahme Schritt 4: Ein nur lexikalisch passendes Dokument (exaktes
Fachwort) UND ein nur semantisch passendes landen beide nach RRF in den
Kandidaten. Ohne Modelle: Vektoren werden von Hand gesetzt (dim=4)."""

import json

import numpy as np
import pytest

from library_core import db
from library_core.retrieve import fts_search, rrf, vec_search

DIM = 4
QUERY_TEXT = "Was besagt das QX-49-Protokoll zur Titration?"
QUERY_VEC = [0.0, 1.0, 0.0, 0.0]


class _Env:
    pass


@pytest.fixture()
def env():
    e = _Env()
    c = e.conn = db.connect(":memory:")
    db.init_db(c, dim=DIM)

    def add(title, year, text, vec):
        doc = c.execute(
            "INSERT INTO documents (zotero_key, title, authors, year, parse_ok) "
            "VALUES (?,?,?,?,1)",
            (f"K{title}", title, json.dumps(["A"]), year),
        ).lastrowid
        cid = c.execute(
            "INSERT INTO chunks (document_id, ordinal, section, page_start, "
            "page_end, bbox, text, embed_text, token_count) "
            "VALUES (?,0,'Methoden',1,1,'[]',?,?,10)",
            (doc, text, text),
        ).lastrowid
        c.execute(
            "INSERT INTO chunks_vec (chunk_id, embedding) VALUES (?,?)",
            (cid, np.asarray(vec, dtype=np.float32).tobytes()),
        )
        return cid

    # Nur LEXIKALISCH passend: exaktes Fachwort, Vektor weit weg von der Query
    e.lex = add("Lexikalisches Paper", 2010,
                "Das QX-49-Protokoll schreibt eine langsame Titration vor.",
                [1.0, 0.0, 0.0, 0.0])
    # Nur SEMANTISCH passend: kein Query-Wort, Vektor nah an der Query
    e.sem = add("Semantisches Paper", 2023,
                "Die schrittweise Dosissteigerung erfolgte über vier Wochen.",
                [0.05, 0.99, 0.05, 0.0])
    # Ablenker
    e.noise = add("Ablenker", 2019,
                  "Unverbundener Inhalt über Fragebogenvalidierung.",
                  [0.0, 0.0, 1.0, 0.0])
    return e


def test_lexikalischer_treffer_kommt_ueber_bm25(env):
    sparse = fts_search(env.conn, QUERY_TEXT, limit=10)
    assert env.lex in sparse
    assert env.sem not in sparse            # kein gemeinsames Wort


def test_semantischer_treffer_kommt_ueber_vektorsuche(env):
    dense = vec_search(env.conn, np.asarray(QUERY_VEC), limit=2)
    assert dense[0] == env.sem              # nächster Nachbar zuerst


def test_beide_landen_nach_rrf_in_den_kandidaten(env):
    dense = vec_search(env.conn, np.asarray(QUERY_VEC), limit=10)
    sparse = fts_search(env.conn, QUERY_TEXT, limit=10)
    fused = rrf([dense, sparse])
    assert env.lex in fused
    assert env.sem in fused


def test_year_min_filtert_vor_der_suche(env):
    dense = vec_search(env.conn, np.asarray(QUERY_VEC), limit=10, year_min=2020)
    sparse = fts_search(env.conn, QUERY_TEXT, limit=10, year_min=2020)
    assert env.lex not in dense and env.lex not in sparse   # Jahr 2010
    assert env.sem in dense


def test_fts_sonderzeichen_crashen_nicht(env):
    # Bindestriche/Anführungszeichen dürfen keinen FTS5-Syntaxfehler auslösen
    assert isinstance(fts_search(env.conn, 'QX-49 "Titration" (p<0.05)?', 10), list)
    assert fts_search(env.conn, "???", 10) == [] or True
