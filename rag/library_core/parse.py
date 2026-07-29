"""Docling-Wrapper: PDF → strukturierte Blöcke + Volltext mit [S. N]-Markern.

Docling wird lazy importiert, damit Module wie chunk.py/db.py auch ohne
installierte Docling-Toolchain importierbar bleiben (Tests, MCP-Server).

Behalten: Abstract, alle Fließtextsektionen, Tabellen als Markdown,
Bildunterschriften. Verworfen: Referenzverzeichnis, Header, Footer,
reine Seitenzahlen.

Für jeden Block wird die Position auf der Seite (bbox) inkl. coord_origin
gespeichert – Docling liefert beim PDF-Backend BOTTOMLEFT; ohne dieses Feld
ist die Koordinaten-Umrechnung im Frontend unmöglich (Harte Regel 5).
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field

from library_core import config

_REFERENCES_RE = re.compile(
    r"^\s*(?:[\divx]+\.?\s+)?"
    r"(references?|bibliograph\w*|literaturverzeichnis|literatur|"
    r"quellenverzeichnis|quellen|works\s+cited|schrifttum)\s*$",
    re.IGNORECASE,
)

_PAGE_NUMBER_RE = re.compile(r"^(?:\d{1,4}|[ivxlcdm]{1,7})$", re.IGNORECASE)

# Docling-Labels, die nie in den Index gehören.
_SKIP_LABELS = {"page_header", "page_footer", "picture"}


@dataclass
class Block:
    text: str
    section: str
    page: int
    bbox: dict | None        # {"l","t","r","b","coord_origin"}
    kind: str = "text"       # "text" | "table" | "caption"


@dataclass
class ParsedDocument:
    blocks: list[Block] = field(default_factory=list)
    full_text: str = ""
    page_chars: dict[int, int] = field(default_factory=dict)
    num_pages: int = 0
    # PDF-Seite -> gedruckte Seitenzahl, aus Kopf-/Fußzeilen gelesen.
    page_labels: dict[int, int] = field(default_factory=dict)

    @property
    def is_scan_suspect(self) -> bool:
        """True, wenn irgendeine Seite unter SCAN_CHAR_THRESH Zeichen liefert."""
        if self.num_pages == 0:
            return True
        return any(
            self.page_chars.get(p, 0) < config.SCAN_CHAR_THRESH
            for p in range(1, self.num_pages + 1)
        )


def build_converter(ocr: bool = False):
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.do_ocr = ocr
    opts.do_table_structure = True
    if ocr:
        opts.ocr_options = EasyOcrOptions(lang=["en", "de"])
    # Bekannter Docling-Fall, in dem do_ocr=False nicht greift – hier explizit
    # absichern; die Laufzeit-Verifikation (Dauer/Log) macht scripts/ingest.py.
    assert opts.do_ocr is ocr, "PdfPipelineOptions.do_ocr wurde nicht übernommen"
    return DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )


def _bbox_dict(prov) -> dict | None:
    bb = getattr(prov, "bbox", None)
    if bb is None:
        return None
    origin = getattr(bb, "coord_origin", None)
    return {
        "l": float(bb.l),
        "t": float(bb.t),
        "r": float(bb.r),
        "b": float(bb.b),
        "coord_origin": getattr(origin, "value", str(origin)),
    }


def _label_of(item) -> str:
    label = getattr(item, "label", "")
    return getattr(label, "value", str(label))


def _collect_texts(parsed: ParsedDocument, doc) -> None:
    """Über ALLE Textitems gehen: Zeichenstatistik je Seite + Seitenzahlen.

    Wichtig: `doc.iterate_items()` läuft nur über die BODY-Ebene. Kopf- und
    Fußzeilen liegen in der FURNITURE-Ebene und tauchen dort nie auf (geprüft
    an Chatterjee 2021: 15 page_header + 17 page_footer in `doc.texts`, null
    davon in `iterate_items()`). `doc.texts` enthält beide Ebenen.

    Die Zeichenstatistik ist die Grundlage der Scan-Erkennung und muss sich
    deshalb auf die ganze Seite beziehen, nicht auf den Body-Anteil: Auf
    Abbildungs- und Tabellenseiten liefert der Body fast nichts, obwohl die
    Seite Text trägt. Gemessen an den vier Fehlalarmen des ersten Volllaufs
    (S20 S.14, S27 S.12, S32 S.12, S47 S.7): Body 65/22/0/55 Zeichen, über
    `doc.texts` 113/101/1241/426 – alle vier über der Schwelle, und die
    PDF-Textebene bestätigt mit 149/136/1412/488, dass es keine Scans sind.
    Tabellen fehlen in `doc.texts` und werden in parse_pdf() dazugezählt.
    """
    for item in getattr(doc, "texts", []) or []:
        prov = item.prov[0] if getattr(item, "prov", None) else None
        if prov is None:
            continue
        text = getattr(item, "text", "") or ""
        parsed.page_chars[prov.page_no] = (
            parsed.page_chars.get(prov.page_no, 0) + len(text)
        )
        if _label_of(item) in ("page_header", "page_footer"):
            _note_page_label(parsed, prov.page_no, text)


def _note_page_label(parsed: ParsedDocument, page: int, text: str) -> None:
    """Gedruckte Seitenzahl aus einer Kopf-/Fußzeile übernehmen.

    Bewusst streng: NUR wenn die Zeile ausschließlich aus einer Zahl besteht.
    Laufende Kolumnentitel wie „S. Chatterjee et al. Industrial Marketing
    Management 97 (2021) 205–219“ enthalten Zahlen, aber keine Seitenzahl –
    eine tolerantere Regel würde daraus auf jeder Seite „219“ lesen.
    """
    t = text.strip()
    if t.isdigit() and len(t) <= 4:
        parsed.page_labels.setdefault(page, int(t))


def page_offset(
    page_labels: dict[int, int], min_obs: int = config.PAGE_OFFSET_MIN_OBS
) -> int | None:
    """Modaler Offset `gedruckte Seite − PDF-Seite` für ein Dokument.

    Ein Journal-Artikel ist durchgehend paginiert, der Offset also konstant.
    Der Modus statt des ersten Treffers, damit vorgebundene Deckblätter oder
    eine einzelne falsch gelesene Zeile das Ergebnis nicht verschieben.
    None, wenn weniger als `min_obs` Seiten denselben Offset zeigen – dann
    wird ehrlich die PDF-Seite zitiert statt eine geratene Druckseite.
    """
    counts = Counter(label - pdf_page for pdf_page, label in page_labels.items())
    if not counts:
        return None
    offset, seen = counts.most_common(1)[0]
    return offset if seen >= min_obs else None


def parse_pdf(path: str, converter) -> ParsedDocument:
    """Ein PDF in Blöcke + Volltext überführen. Converter wird injiziert,
    damit er über viele Dokumente wiederverwendet wird."""
    result = converter.convert(path)
    doc = result.document

    parsed = ParsedDocument(num_pages=len(getattr(doc, "pages", {}) or {}))
    _collect_texts(parsed, doc)
    section = "(Anfang)"
    in_references = False
    full_parts: list[str] = []
    last_page: int | None = None

    def emit_marker(page: int) -> None:
        nonlocal last_page
        if page != last_page:
            full_parts.append(f"[S. {page}]")
            last_page = page

    for item, _level in doc.iterate_items():
        label = _label_of(item)
        prov = item.prov[0] if getattr(item, "prov", None) else None
        page = prov.page_no if prov else (last_page or 1)

        # Tabellen tragen ihren Inhalt nicht in .text, sondern in .data –
        # einmal exportieren und unten wiederverwenden.
        table_md: str | None = None
        if label == "table":
            try:
                table_md = item.export_to_markdown(doc)
            except TypeError:
                table_md = item.export_to_markdown()
            table_md = (table_md or "").strip()

        raw_text = getattr(item, "text", "") or ""
        # Tabellen fehlen in doc.texts (TableItem hat kein .text) – ihren
        # Inhalt hier zur Zeichenstatistik dazu, alles andere kommt aus
        # _collect_texts(). Sonst gälten Tabellenseiten als Scan.
        if prov is not None and table_md is not None:
            parsed.page_chars[page] = parsed.page_chars.get(page, 0) + len(table_md)

        if label in ("section_header", "title"):
            heading = raw_text.strip()
            if not heading:
                continue
            section = heading
            in_references = bool(_REFERENCES_RE.match(heading))
            if not in_references:
                emit_marker(page)
                full_parts.append(f"## {heading}")
            continue

        if in_references or label in _SKIP_LABELS:
            continue

        if label == "table":
            if not table_md:
                continue
            emit_marker(page)
            full_parts.append(table_md)
            parsed.blocks.append(
                Block(text=table_md, section=section, page=page,
                      bbox=_bbox_dict(prov) if prov else None, kind="table")
            )
            continue

        text = raw_text.strip()
        if not text or _PAGE_NUMBER_RE.match(text):
            continue

        kind = "caption" if label == "caption" else "text"
        emit_marker(page)
        full_parts.append(text)
        parsed.blocks.append(
            Block(text=text, section=section, page=page,
                  bbox=_bbox_dict(prov) if prov else None, kind=kind)
        )

    parsed.full_text = "\n\n".join(full_parts)
    return parsed
