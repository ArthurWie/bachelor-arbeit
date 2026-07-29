"""Build the state-of-the-art coding table skeleton from the screening CSV.

Pre-fills bibliographic columns for all included studies (n = 67) and adds
empty coding columns as announced in the proposal + supervisor feedback #1
(performance vs. competitive advantage coded separately).
Output: corpus/coding_table.csv  (one row per study, UTF-8 BOM for Excel).
Re-running preserves already-coded values (merge on eid).
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "coding_table.csv"

CODING_COLS = [
    "theoretical_lens",        # e.g. RBV, dynamic capabilities, GPT, TOE, RBV+DC
    "method",                  # survey-SEM | panel econometrics | event study | case study | experiment | fsQCA | mixed
    "sample",                  # e.g. "392 B2B SMEs, Saudi Arabia, cross-section" / "panel 3235 firms 2007-2021"
    "country_region",
    "industry",
    "ai_measure",              # how AI investment/adoption is operationalized
    "outcome_construct",       # performance | competitive_advantage | both   (supervisor feedback #1)
    "performance_measure",     # ROA, TFP, firm value, revenue growth, ... ("" if not measured)
    "ca_measure",              # how CA is measured, if at all ("" if not measured)
    "effect_direction",        # positive | negative | mixed | null | conditional
    "conditions",              # identified moderators/mediators/complementarities (the core of the RQ)
    "key_finding",             # one sentence
    "quality_notes",           # e.g. perceptual self-report, vendor data, IV strategy, pre-registered
    "coding_status",           # empty | draft | final
]


def pdf_name(r):
    author = re.sub(r"[^A-Za-z]", "", r["first_author"].split()[0]) or "Unknown"
    suffix = re.sub(r"[^A-Za-z0-9]+", "-", r["doi"].split("/", 1)[-1])[:40] if r["doi"] else r["eid"][-10:]
    name = f"{author}_{r['year']}_{suffix}.pdf"
    if (ROOT.parent / "literature" / name).exists():
        return name
    # legacy names from the proposal phase
    for cand in (ROOT.parent / "literature").glob(f"{author.lower()}*{r['year']}*.pdf"):
        return cand.name
    for cand in (ROOT.parent / "literature").glob(f"{author.lower()}{r['year']}*.pdf"):
        return cand.name
    return "MISSING"


rows = [r for r in csv.DictReader(open(ROOT / "screening_2026-07-17.csv", encoding="utf-8-sig"))
        if r["screen_decision"] == "include"]
rows.sort(key=lambda r: (r["year"], r["first_author"]))

old = {}
if OUT.exists():
    old = {r["eid"]: r for r in csv.DictReader(open(OUT, encoding="utf-8-sig"), delimiter=";")}

header = ["study_id", "authors", "year", "journal", "ajg2024", "doi", "pdf"] + CODING_COLS
with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["eid"] + header)
    for i, r in enumerate(rows, 1):
        prev = old.get(r["eid"], {})
        w.writerow([r["eid"], f"S{i:02d}", r["authors"], r["year"], r["journal"],
                    r["ajg2024"], r["doi"], pdf_name(r)]
                   + [prev.get(c, "") for c in CODING_COLS])

missing = sum(1 for r in rows if pdf_name(r) == "MISSING")
print(f"coding table: {len(rows)} studies, {len(header)+1} columns -> {OUT.name}")
print(f"pdf links resolved: {len(rows)-missing}/{len(rows)}")
