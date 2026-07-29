"""BibTeX-Einträge für Korpusstudien aus dem eingefrorenen Scopus-Export.

    python corpus/make_bib.py S03 S05 S10        # Einträge ausgeben
    python corpus/make_bib.py --append S03 S05   # an bib.bib anhängen

Quelle ist `corpus/corpus_2026-07-17.csv`, also derselbe Scopus-Export, der den
Korpus definiert – keine neue Abfrage, kein Google Scholar (siehe CLAUDE.md).
Vorhandene Schlüssel in bib.bib werden nicht doppelt geschrieben.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODING = ROOT / "corpus" / "coding_table.csv"
SCOPUS = ROOT / "corpus" / "corpus_2026-07-17.csv"
BIB = ROOT / "bib.bib"

_STOP = {"a", "an", "the", "on", "in", "of", "for", "and", "when", "does", "do",
         "how", "what", "from", "to", "is", "are", "with", "at", "by"}


def _authors_bibtex(raw: str) -> str:
    """Scopus „Nachname I.I.; Nachname I.I."“ → BibTeX „Nachname, I.I. and …“."""
    out = []
    for a in (x.strip() for x in (raw or "").split(";")):
        if not a:
            continue
        parts = a.split()
        # Initialen stehen hinten: alles davor ist der Nachname.
        init = [p for p in parts if re.fullmatch(r"(?:[A-Z]\.?){1,4}", p)]
        if init:
            surname = " ".join(parts[: len(parts) - len(init)])
            out.append(f"{surname}, {' '.join(init)}")
        else:
            out.append(a)
    return " and ".join(out)


def _title_field(raw: str) -> str:
    """Scopus-Titel → BibTeX-Titel.

    Zwei Eingriffe, beide zwingend: `&` muss escaped werden (sonst bricht LaTeX
    beim ersten Zitat ab), und Akronyme müssen in Klammern stehen, weil
    biblatex-apa den Titel auf Satzschreibung setzt und „AI" sonst als „ai" im
    Literaturverzeichnis landet. Eigennamen mitten im Titel (French, European)
    erkennt keine Regel – die meldet main() zur Prüfung.
    """
    def protect(m: re.Match) -> str:
        word = m.group(0)
        # Zwei Großbuchstaben im Wort = Akronym (AI, SME, B2B, R&D, AI-based).
        return "{" + word + "}" if len(re.findall("[A-Z]", word)) >= 2 else word

    out = re.sub(r"[A-Za-z0-9&'’-]+", protect, (raw or "").strip())
    return out.replace("&", r"\&")


def _suspect_propernouns(raw: str) -> list[str]:
    """Wörter mit einzelnem Großbuchstaben mitten im Titel (Eigenname?)."""
    words = re.findall(r"[A-Za-z'’-]+", raw or "")
    return [w for i, w in enumerate(words)
            if i > 0 and w[:1].isupper() and not w.isupper()
            and len(re.findall("[A-Z]", w)) == 1]


def _key(first_author: str, year: str, title: str) -> str:
    surname = re.sub(r"[^a-z]", "", (first_author or "anon").split()[0].lower())
    word = next((w for w in re.findall(r"[a-z]+", (title or "").lower())
                 if w not in _STOP and len(w) > 3), "study")
    return f"{surname}{year}{word}"


# Selbsttest der Namens- und Schlüssellogik (Konvention wie corpus/fact_sheet.py:
# Prüfung beim Import, kein Framework). Scopus schreibt „Nachname I.I.“, BibTeX
# braucht „Nachname, I.I.“ – dreht man das, stehen im Literaturverzeichnis die
# Initialen als Nachname.
assert _authors_bibtex("Chatterjee S.; Rana N.P.") == "Chatterjee, S. and Rana, N.P."
assert _authors_bibtex("Fosso Wamba S.") == "Fosso Wamba, S."     # zweiteiliger Name
assert _authors_bibtex("") == ""
assert _key("Chatterjee S.", "2021",
            "The effect of AI-based CRM on organization performance") == \
    "chatterjee2021effect"                                        # „The“, „of“ raus
assert _key("Lee Y.S.", "2022",
            "When does AI pay off? AI-adoption intensity") == "lee2022adoption"
# Akronyme geschützt, & escaped – ohne beides steht „ai" im Verzeichnis bzw.
# bricht der Lauf ab. Kleingeschriebenes bleibt unangetastet.
assert _title_field("Harnessing AI capabilities for SME performance") == \
    "Harnessing {AI} capabilities for {SME} performance"
assert _title_field("AI-based CRM in the B2B context") == \
    "{AI-based} {CRM} in the {B2B} context"   # Bindestrichwort bleibt ein Token
assert _title_field("complementary investments, and R&D strategy") == \
    r"complementary investments, and {R\&D} strategy"
assert _title_field("Artificial intelligence and firm-level productivity") == \
    "Artificial intelligence and firm-level productivity"
assert _suspect_propernouns("Evidence from French firms") == ["French"]
assert _suspect_propernouns("Harnessing AI capabilities") == []


def _entry(row: dict) -> tuple[str, str]:
    key = _key(row.get("first_author", ""), row.get("year", ""), row.get("title", ""))
    fields = [
        ("author", _authors_bibtex(row.get("authors", ""))),
        ("title", f"{{{_title_field(row.get('title', ''))}}}"),
        ("journal", (row.get("journal") or "").strip()),
        ("year", (row.get("year") or "").strip()),
        ("volume", (row.get("volume") or "").strip()),
        ("pages", (row.get("pages") or "").strip().replace("-", "--")),
        ("doi", (row.get("doi") or "").strip()),
    ]
    body = ",\n".join(f"  {k:8}= {{{v}}}" if k != "title" else f"  {k:8}= {v}"
                      for k, v in fields if v)
    return key, f"@article{{{key},\n{body}\n}}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("study_ids", nargs="+", metavar="SXX")
    ap.add_argument("--append", action="store_true", help="an bib.bib anhängen")
    args = ap.parse_args()

    coding = {r["study_id"]: r for r in
              csv.DictReader(CODING.open(encoding="utf-8-sig"), delimiter=";")}
    scopus = {r["eid"]: r for r in
              csv.DictReader(SCOPUS.open(encoding="utf-8-sig"))}
    existing = set(re.findall(r"@\w+\{([^,]+),", BIB.read_text(encoding="utf-8")))

    new, skipped = [], []
    for sid in args.study_ids:
        if sid not in coding:
            sys.exit(f"unbekannte study_id: {sid}")
        row = scopus[coding[sid]["eid"]]
        key, entry = _entry(row)
        (skipped if key in existing else new).append((sid, key, entry))

    for sid, key, _ in skipped:
        print(f"[bib] {sid}: {key} steht schon in bib.bib", file=sys.stderr)

    for sid, key, _ in new:
        suspects = _suspect_propernouns(scopus[coding[sid]["eid"]].get("title", ""))
        if suspects:
            print(f"[bib] {sid}: Großschreibung im Titel prüfen (Eigenname in "
                  f"Klammern schützen, sonst setzt APA es klein): "
                  f"{', '.join(suspects)}", file=sys.stderr)

    if args.append and new:
        with BIB.open("a", encoding="utf-8") as fh:
            for sid, key, entry in new:
                fh.write(f"\n% {sid} – SLR-Korpus, Scopus-Export 17.07.2026\n{entry}\n")
        print(f"[bib] {len(new)} Einträge angehängt: "
              f"{', '.join(k for _, k, _ in new)}", file=sys.stderr)
    else:
        for _, _, entry in new:
            print(entry + "\n")


if __name__ == "__main__":
    main()
