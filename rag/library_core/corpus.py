"""Korpus-Adapter: die eingefrorene SLR-Bibliothek als Dokumentquelle.

Ersetzt `library_core/zotero.py` (Zotero ist auf diesem Rechner nicht
installiert und wäre hier auch die schlechtere Quelle). Gelesen wird, was die
Arbeit ohnehin als System of Record führt:

- `corpus/coding_table.csv`  – die 67 finalen Studien: study_id, DOI, PDF-Name
- `corpus/corpus_2026-07-17.csv` – der eingefrorene Scopus-Export: Titel,
  Autoren, Seitenbereich

Beide Dateien sind eingefroren (siehe CLAUDE.md der Arbeit). Titel und Autoren
kommen aus dem Scopus-Export, niemals aus dem PDF-Text – dieselbe Regel wie
vorher gegenüber Zotero, nur mit der besseren Quelle.

`printed_first`/`printed_last` sind reine PRÜFWERTE für die Seitenzahl-
Kalibrierung (siehe scripts/ingest.py); zitiert wird nie daraus gerechnet.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

from library_core import config


class CorpusError(RuntimeError):
    pass


@dataclass
class CorpusDocument:
    study_id: str            # S01…S67 – landet in documents.zotero_key
    path: str                # absoluter Pfad zum PDF in literature/
    title: str
    authors: list[str]       # Scopus-Reihenfolge: "Nachname I.I."
    year: int | None
    doi: str | None
    printed_first: int | None
    printed_last: int | None


def _read_csv(path: Path, delimiter: str) -> list[dict]:
    if not path.is_file():
        raise CorpusError(
            f"Korpusdatei fehlt: {path}\nDer Adapter erwartet die eingefrorenen "
            "Dateien der Arbeit. Pfade notfalls über die Umgebungsvariablen "
            "CORPUS_DIR / LITERATURE_DIR setzen."
        )
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=delimiter))


def _authors(raw: str) -> list[str]:
    return [a.strip() for a in (raw or "").split(";") if a.strip()]


def _int_or_none(raw: str | None) -> int | None:
    m = re.search(r"\d+", raw or "")
    return int(m.group()) if m else None


def _printed_range(pages: str | None) -> tuple[int | None, int | None]:
    """Scopus-Seitenbereich '205-219' → (205, 219). Artikelnummern und leere
    Felder → (None, None); 39 der 67 Studien haben keinen Bereich."""
    m = re.fullmatch(r"\s*(\d+)\s*[-–]\s*(\d+)\s*", pages or "")
    if not m:
        return None, None
    return int(m.group(1)), int(m.group(2))


def documents() -> list[CorpusDocument]:
    """Die 67 finalen Studien mit Metadaten und PDF-Pfad.

    Scheitert laut, wenn ein PDF fehlt oder ein EID nicht im Scopus-Export
    steht – stillschweigend ein Dokument zu überspringen wäre der schlimmere
    Fehler (die Bibliothek wäre dann nicht deckungsgleich mit dem Korpus).
    """
    coding = _read_csv(config.CODING_TABLE, ";")
    scopus = {r["eid"]: r for r in _read_csv(config.SCOPUS_EXPORT, ",")}

    docs: list[CorpusDocument] = []
    missing_pdf: list[str] = []
    missing_meta: list[str] = []

    for row in coding:
        eid = (row.get("eid") or "").strip()
        study_id = (row.get("study_id") or "").strip()
        meta = scopus.get(eid)
        if meta is None:
            missing_meta.append(f"{study_id} ({eid})")
            continue
        pdf_path = Path(config.LITERATURE_DIR) / (row.get("pdf") or "").strip()
        if not pdf_path.is_file():
            missing_pdf.append(f"{study_id}: {pdf_path.name}")
            continue
        first, last = _printed_range(meta.get("pages"))
        docs.append(
            CorpusDocument(
                study_id=study_id,
                path=str(pdf_path.resolve()),
                title=(meta.get("title") or "(ohne Titel)").strip(),
                authors=_authors(meta.get("authors", "")),
                year=_int_or_none(row.get("year") or meta.get("year")),
                doi=((row.get("doi") or meta.get("doi") or "").strip() or None),
                printed_first=first,
                printed_last=last,
            )
        )

    if missing_meta:
        raise CorpusError(
            "EIDs der Coding-Tabelle fehlen im Scopus-Export "
            f"({config.SCOPUS_EXPORT.name}): {', '.join(missing_meta)}"
        )
    if missing_pdf:
        raise CorpusError(
            f"PDFs fehlen in {config.LITERATURE_DIR}: {'; '.join(missing_pdf)}"
        )
    if not docs:
        raise CorpusError(f"Keine Studien in {config.CODING_TABLE} gefunden.")
    return docs
