"""Chunking-Grenzen: Sektionen, Absätze, Tabellen, Überlappung, bbox-Erbe."""

from library_core import config
from library_core.chunk import chunk_blocks
from library_core.parse import Block

WORDS = lambda t: len(t.split())          # Token ~ Wörter für Tests


def para(n_words: int, section="Methoden", page=1, word="wort", bbox=None):
    return Block(
        text=" ".join(f"{word}{i}" for i in range(n_words)),
        section=section,
        page=page,
        bbox=bbox or {"l": 50.0, "t": 700.0, "r": 500.0, "b": 650.0,
                      "coord_origin": "BOTTOMLEFT"},
    )


def test_niemals_ueber_sektionsgrenzen():
    blocks = [para(100, section="Einleitung"), para(100, section="Methoden")]
    chunks = chunk_blocks(blocks, "T", 2023, count_tokens=WORDS)
    assert len(chunks) == 2
    assert chunks[0].section == "Einleitung"
    assert chunks[1].section == "Methoden"


def test_absaetze_sind_atomar_kein_schnitt_im_satz():
    # Ein Absatz über Zielgröße bleibt EIN Chunk (nur an Absatzgrenzen schneiden)
    blocks = [para(900)]
    chunks = chunk_blocks(blocks, "T", 2023, count_tokens=WORDS)
    assert len(chunks) == 1
    assert chunks[0].token_count == 900


def test_zielgroesse_wird_an_absatzgrenze_umgesetzt():
    blocks = [para(400, word="a"), para(400, word="b")]
    chunks = chunk_blocks(blocks, "T", 2023, count_tokens=WORDS)
    assert len(chunks) == 2                   # 800 > 600 -> Schnitt dazwischen
    assert "a0" in chunks[0].text and "b0" in chunks[1].text


def test_tabelle_bleibt_ein_chunk_auch_wenn_gross():
    table = Block(text="| a | b |\n" * 700, section="Ergebnisse", page=3,
                  bbox=None, kind="table")
    blocks = [para(100, section="Ergebnisse"), table,
              para(100, section="Ergebnisse", word="nach")]
    chunks = chunk_blocks(blocks, "T", 2023, count_tokens=WORDS)
    table_chunks = [c for c in chunks if "| a | b |" in c.text]
    assert len(table_chunks) == 1
    assert table_chunks[0].text == table.text     # ungeteilt, pur


def test_ueberlappung_traegt_letzte_absaetze_weiter():
    # 7 Absätze à 100 Wörter, Ziel 600, Overlap-Budget 90 -> Absatz passt
    # nicht ins Budget? Doch: 100 > 90 -> kein Overlap. Nimm 50er-Absätze.
    blocks = [para(50, word=f"p{i}x") for i in range(20)]
    chunks = chunk_blocks(blocks, "T", 2023, count_tokens=WORDS)
    assert len(chunks) >= 2
    # letzter Absatz von Chunk 0 muss Chunk 1 eröffnen (15 % von 600 = 90 >= 50)
    tail_word = chunks[0].text.split()[-1]
    assert tail_word in chunks[1].text.split()


def test_erbt_seiten_und_bbox_vereinigung():
    b1 = para(50, page=2, bbox={"l": 50.0, "t": 700.0, "r": 300.0, "b": 650.0,
                                "coord_origin": "BOTTOMLEFT"})
    b2 = para(50, page=2, bbox={"l": 60.0, "t": 400.0, "r": 500.0, "b": 350.0,
                                "coord_origin": "BOTTOMLEFT"})
    b3 = para(50, page=3)
    chunks = chunk_blocks([b1, b2, b3], "T", 2023, count_tokens=WORDS)
    c = chunks[0]
    assert (c.page_start, c.page_end) == (2, 3)
    page2 = next(bb for bb in c.bbox if bb["page"] == 2)
    assert page2["x0"] == 50.0 and page2["x1"] == 500.0
    assert page2["y0"] == 350.0 and page2["y1"] == 700.0
    assert page2["coord_origin"] == "BOTTOMLEFT"
    assert any(bb["page"] == 3 for bb in c.bbox)


def test_embed_text_hat_kontextpraefix_text_bleibt_original():
    blocks = [para(50, section="Diskussion")]
    c = chunk_blocks(blocks, "Mein Paper", 2021, count_tokens=WORDS)[0]
    assert c.embed_text.startswith("Aus 'Mein Paper' (2021), Abschnitt Diskussion: ")
    assert not c.text.startswith("Aus '")
    assert c.embed_text.endswith(c.text)


def test_konstanten_unveraendert():
    assert config.CHUNK_TOKENS == 600
    assert config.CHUNK_OVERLAP == 0.15
