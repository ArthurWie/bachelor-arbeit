"""Druckseiten-Kalibrierung und Zitier-Formatierung.

Der teuerste Fehler dieses Werkzeugs wäre eine PDF-Seite, die als gedruckte
Seitenzahl in eine Fußnote wandert. Deshalb hier festgenagelt.
"""

from library_core.parse import page_offset
from retrieval_mcp.__main__ import _pages, _surname


# ------------------------------------------------------------- page_offset

def test_konstanter_offset_wird_erkannt():
    # Chatterjee 2021 (IMM), gedruckt S. 205–219 auf 15 PDF-Seiten.
    assert page_offset({2: 206, 3: 207, 4: 208}) == 204


def test_offset_null_bei_artikelnummerierung():
    # Babina 2024 (JFE): Fußzeile zählt 1..26, entspricht der PDF-Seite.
    assert page_offset({2: 2, 3: 3, 4: 4}) == 0


def test_einzelbeobachtung_reicht_nicht():
    assert page_offset({7: 512}) is None


def test_ohne_fusszeilen_kein_offset():
    # Emerald-PDFs tragen statt Seitenzahl einen Download-Vermerk.
    assert page_offset({}) is None


def test_modus_schlaegt_ausreisser():
    # Vorgebundenes Deckblatt + eine falsch gelesene Zeile: der Modus gewinnt.
    assert page_offset({2: 3333, 3: 3334, 4: 3335, 9: 42}) == 3331


def test_min_obs_konfigurierbar():
    assert page_offset({5: 100}, min_obs=1) == 95


# ------------------------------------------------------------------ _pages

def test_gedruckte_seite_mit_pdf_seite_in_klammern():
    assert _pages(3, 3, 207, 207) == "S. 207 (PDF-S. 3)"


def test_spanne_ueber_zwei_seiten():
    assert _pages(3, 4, 207, 208) == "S. 207–208 (PDF-S. 3–4)"


def test_kein_klammerzusatz_wenn_identisch():
    assert _pages(5, 5, 5, 5) == "S. 5"


def test_ohne_druckseite_wird_gewarnt():
    out = _pages(3, 3)
    assert "PDF-S. 3" in out
    assert "nicht als Druckseite zitieren" in out
    assert not out.startswith("S. ")


# ---------------------------------------------------------------- _surname

def test_scopus_reihenfolge_nachname_vorne():
    assert _surname("Wamba-Taguimdje S.L.") == "Wamba-Taguimdje"
    assert _surname("Fosso Wamba S.") == "Fosso Wamba"
    assert _surname("Babina T.") == "Babina"


def test_fallback_vorname_nachname():
    assert _surname("Tanja Babina") == "Babina"


def test_einzelnamen_bleiben():
    assert _surname("Krakowski") == "Krakowski"
    assert _surname("") == ""
