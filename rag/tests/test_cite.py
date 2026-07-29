"""Zitatverifikation: Treffer, Nicht-Treffer, abweichende Whitespaces."""

from library_core.cite import (
    PAGE_MATCH_MIN,
    page_sequence_match,
    has_split_ligatures,
    verify_quote,
    verify_quote_on_page,
)


# --- Seitenprüfung: robust gegen pdfplumber-Eigenheiten, hart gegen Erfundenes

# So kommt eine Verlagsseite bei pdfplumber an: Leerzeichen mitten in Wörtern
# (Blocksatz/Kerning) und Spalten in anderer Reihenfolge als im Lesefluss.
_SEITE = (
    "S. Chatterjee et al. I n d u s t r i a l M a r k e t i n g\n"
    "Moreover, it is essential to collect the data (resources) by the\n"
    "organi zations, which are valuable, rare, and inimitable.\n"
    "206"
)


def test_echtes_zitat_trotz_zerschossener_woerter_belegt():
    quote = "Moreover, it is essential to collect the data (resources) by the"
    assert verify_quote_on_page(quote, _SEITE)
    assert page_sequence_match(quote, _SEITE) == 1.0


def test_erfundenes_zitat_faellt_durch():
    quote = "AI investments always guarantee a sustained competitive advantage."
    assert not verify_quote_on_page(quote, _SEITE)
    assert page_sequence_match(quote, _SEITE) < PAGE_MATCH_MIN


def test_umgestellte_wortfolge_faellt_durch():
    # Dieselben Wörter, andere Reihenfolge – ein Zitat ist es damit nicht.
    quote = "the data essential collect to is it Moreover"
    assert not verify_quote_on_page(quote, _SEITE)


def test_leeres_zitat_ist_kein_beleg():
    assert page_sequence_match("", _SEITE) == 0.0
    assert not verify_quote_on_page("   ", _SEITE)


# --- Ligatur-Trennung der Emerald-/Wiley-PDFs („fi rm“ statt „firm“)

def test_repariertes_zitat_verifiziert_gegen_kaputten_chunk():
    chunk = ("Adoption of AI gives distinct competitive advantage to the fi rm "
             "which ultimately translates into fi rm ' s overall performance.")
    # So wird zitiert – mit heilen Wörtern.
    assert verify_quote(
        "AI gives distinct competitive advantage to the firm", chunk)


def test_getrennte_ligaturen_werden_erkannt():
    assert has_split_ligatures("a signi fi cant in fl uence on fi rms")
    assert has_split_ligatures("di ff erent results")


def test_erkennung_greift_nicht_zu_weit():
    assert not has_split_ligatures("Wi-Fi network performance")
    assert not has_split_ligatures("significant influence on firms")
    assert not has_split_ligatures("")


def test_korrigierte_schreibweise_verifiziert_auch_mittendrin():
    # Der harte Fall: Ligatur mitten im Wort, nicht am Wortanfang.
    chunk = "This has a signi fi cant in fl uence on fi rm value."
    assert verify_quote("a significant influence on firm value", chunk)

CHUNK = (
    "Die Interventionsgruppe zeigte eine Reduktion der Symptomlast um zwölf\n"
    "Prozent   (p < 0.05), während die Kontrollgruppe unverändert blieb.\n"
    "Die Stichprobe umfasste N = 128 Teilnehmerinnen und Teilnehmer."
)


def test_exakter_treffer():
    assert verify_quote("Reduktion der Symptomlast um zwölf", CHUNK)


def test_whitespace_abweichung_zeilenumbruch():
    # Zitat einzeilig, Quelle mit Zeilenumbruch und Mehrfach-Spaces
    assert verify_quote(
        "eine Reduktion der Symptomlast um zwölf Prozent (p < 0.05)", CHUNK
    )


def test_whitespace_abweichung_im_zitat():
    assert verify_quote("N   =\n128", CHUNK)


def test_case_insensitiv():
    assert verify_quote("die interventionsgruppe ZEIGTE", CHUNK)


def test_nicht_treffer():
    assert not verify_quote(
        "eine Reduktion der Symptomlast um zwanzig Prozent", CHUNK
    )


def test_erfundenes_zitat():
    assert not verify_quote("Die Effektstärke lag bei d = 0.8", CHUNK)


def test_leeres_zitat_ist_nie_bestaetigt():
    assert not verify_quote("", CHUNK)
    assert not verify_quote("   \n ", CHUNK)
