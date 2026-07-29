"""Zitat-Verifikation.

Kernstück der prüfbaren Zitierbarkeit: ein angeblich wörtliches Zitat muss
nach Whitespace-Normalisierung als Substring im Quelltext vorkommen.
Nicht verifizierte Zitate werden vom Aufrufer explizit als unbestätigt
markiert, nie stillschweigend durchgelassen.
"""

from __future__ import annotations

import re
import sqlite3
import unicodedata

_WORD = re.compile(r"[^\W_]+", re.UNICODE)

# Ab diesem Anteil übereinstimmender Wortfolge gilt ein Zitat als auf der
# Seite belegt. Empirisch bestimmt an 40 echten Zitaten aus dem Korpus und 60
# erfundenen gegen dieselben Seiten (x_tolerance=1):
#   echte      Median 1.00, Minimum 0.35
#   erfundene  Median 0.08, MAXIMUM 0.18
# Bei 0.60 werden 36/40 echte bestätigt und 0/60 erfundene – Faktor 3 Abstand
# zum höchsten erfundenen Wert. Höhere Schwellen kosten nur echte Treffer
# (0.90: 31/40), ohne einen einzigen Fehlalarm zusätzlich zu verhindern.
PAGE_MATCH_MIN = 0.60

# pdfplumber-Extraktion: gemessen 17/24 statt 13/24 Treffern gegenüber der
# Voreinstellung (x_tolerance=3). Blocksatz-PDFs setzen Leerzeichen mitten in
# Wörter; die engere Toleranz trennt weniger falsch.
PAGE_X_TOLERANCE = 1


# Manche Verlags-PDFs (Emerald, einige Wiley) geben die Ligaturen fi/fl/ff als
# eigenen Textabschnitt aus, mit Leerzeichen davor UND danach: „fi rm“,
# „signi fi cant“, „in fl uence“, „di ff erent“. Betroffen: 16 der 67 Studien,
# 1.307 Vorkommen, der Großteil in drei Papers (S17, S38, S34).
#
# Automatisch reparieren lässt sich das NICHT sicher: „signi fi cant“ muss nach
# vorn UND hinten verbunden werden, „the fi rm“ aber nur nach hinten – und ohne
# Wörterbuch ist „signi“ nicht von „the“ zu unterscheiden („the fi rm“ würde zu
# „thefirm“). Deshalb wird nur erkannt und gewarnt; der Wortlaut für die
# Fußnote kommt in diesen Fällen von der PDF-Seite.
_LIGATURE_SPLIT = re.compile(r"(?:^|\s)(ffi|ffl|ff|fi|fl)\s+[a-zäöüß]{2,}")


def has_split_ligatures(s: str) -> bool:
    """Enthält der Text getrennte Ligaturen und ist damit nicht direkt
    zitierfähig?"""
    return _LIGATURE_SPLIT.search(s) is not None


def _normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().casefold()


def _tight(s: str) -> str:
    """Alle Leerzeichen weg. Fängt getrennte Ligaturen und Blocksatz-Artefakte
    ab: „signi fi cant“ und „significant“ werden identisch."""
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", s)).casefold()


def _words(s: str) -> list[str]:
    return _WORD.findall(unicodedata.normalize("NFKC", s).casefold())


def page_sequence_match(quote: str, page_text: str) -> float:
    """Anteil der Zitatwörter, die im Seitentext in derselben Reihenfolge
    vorkommen (Lücken erlaubt). 1.0 = alle, in Reihenfolge.

    Warum keine Substring-Prüfung wie in verify_quote: Der Seitentext kommt
    aus pdfplumber und linearisiert zweispaltige Verlags-PDFs anders als
    Docling. Dazu setzen diese PDFs Leerzeichen mitten in Wörter
    (Kerning/Blocksatz) – „critically“ und „organizations,“ fehlen dort als
    Token. Ein 20-Wort-Substring trifft deshalb nur in ~25 % der Fälle,
    obwohl der Text auf der Seite steht. Die Wortfolge ist robust dagegen und
    trennt echte von erfundenen Zitaten trotzdem sauber.
    """
    qw = _words(quote)
    if not qw:
        return 0.0
    i = 0
    for w in _words(page_text):
        if i < len(qw) and w == qw[i]:
            i += 1
    return i / len(qw)


def verify_quote_on_page(quote: str, page_text: str) -> bool:
    return page_sequence_match(quote, page_text) >= PAGE_MATCH_MIN


def verify_quote(quote: str, chunk_text: str) -> bool:
    """True, wenn quote nach Whitespace-Normalisierung Substring von
    chunk_text ist. Groß/Kleinschreibung ignorieren.

    Zweiter Versuch ohne jedes Leerzeichen: Sonst scheitert ein korrekt
    geschriebenes Zitat an den getrennten Ligaturen der Quelle („signi fi cant“
    im Chunk vs. „significant“ in der Fußnote). Aufgegeben wird dabei nur die
    Wortgrenze; welche Zeichen in welcher Reihenfolge stehen, wird weiter
    geprüft, und Stufe 2 (page_sequence_match) prüft ohnehin gegen die Seite.
    """
    q = _normalize(quote)
    if not q:
        return False
    if q in _normalize(chunk_text):
        return True
    return _tight(quote) in _tight(chunk_text)


def verify_quote_in_chunk(conn: sqlite3.Connection, quote: str, chunk_id: int) -> bool:
    row = conn.execute("SELECT text FROM chunks WHERE id = ?", (chunk_id,)).fetchone()
    if row is None:
        return False
    return verify_quote(quote, row["text"])


def verify_quote_in_document(conn: sqlite3.Connection, quote: str, document_id: int) -> bool:
    row = conn.execute(
        "SELECT full_text FROM documents WHERE id = ?", (document_id,)
    ).fetchone()
    if row is None or row["full_text"] is None:
        return False
    return verify_quote(quote, row["full_text"])


def check_quote_against_pdf(
    conn: sqlite3.Connection, quote: str, chunk_id: int
) -> tuple[float | None, str]:
    """Zitat gegen die ECHTE PDF-Seite prüfen, nicht nur gegen den Chunk.

    Zweite, unabhängige Stufe: fängt sowohl erfundene Zitate als auch eine
    falsche Seitenzuordnung ab, weil die Wörter dann auf der genannten Seite
    nicht stehen. Gibt (Trefferquote, Klartext) zurück; (None, Grund), wenn
    die Seite nicht lesbar ist.
    """
    row = conn.execute(
        """SELECT c.page_start, c.page_end, d.file_path
           FROM chunks c JOIN documents d ON d.id = c.document_id
           WHERE c.id = ?""",
        (chunk_id,),
    ).fetchone()
    if row is None:
        return None, "Chunk unbekannt"
    try:
        import pdfplumber
    except ImportError:
        return None, "pdfplumber nicht installiert"
    try:
        with pdfplumber.open(row["file_path"]) as pdf:
            pages = [
                pdf.pages[p - 1].extract_text(x_tolerance=PAGE_X_TOLERANCE) or ""
                for p in range(row["page_start"],
                               min(row["page_end"], len(pdf.pages)) + 1)
            ]
    except (OSError, IndexError, ValueError) as exc:
        return None, f"PDF-Seite nicht lesbar ({type(exc).__name__})"
    page_text = "\n".join(pages)
    score = page_sequence_match(quote, page_text)
    pages_label = (
        f"S. {row['page_start']}" if row["page_start"] == row["page_end"]
        else f"S. {row['page_start']}–{row['page_end']}"
    )
    if verify_quote_on_page(quote, page_text):
        return score, f"auch auf PDF-{pages_label} belegt, {score:.0%} Wortfolge"
    return score, (
        f"auf PDF-{pages_label} maschinell nicht bestätigt ({score:.0%} "
        "Wortfolge) – meist ein Extraktionsproblem der Seite, nicht des Zitats; "
        "die Seite vor der Fußnote kurz ansehen"
    )
