"""Apply the journal-quality inclusion rule (AJG 2024 >= 2) to the rated corpus.

Rule set 17 July 2026 (supervisor mandate: broad, transparent, non-selective).
Writes screening_2026-07-17.csv: qualifying studies with empty screening
columns for the title/abstract pass. Excluded records stay documented in
corpus_2026-07-17_rated.csv (their ajg2024 column is the exclusion reason).
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RATED = ROOT / "corpus_2026-07-17_rated.csv"
OUT = ROOT / "screening_2026-07-17.csv"

INCLUDE = {"4*", "4", "3", "2"}

rows = list(csv.DictReader(open(RATED, encoding="utf-8-sig")))
kept = [r for r in rows if r["ajg2024"] in INCLUDE]

for r in kept:
    r["screen_decision"] = ""   # include / exclude
    r["screen_reason"] = ""     # reason code if excluded
    r["screen_notes"] = ""

cols = list(kept[0].keys())
with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(sorted(kept, key=lambda r: (r["year"], r["first_author"])))

sys.stdout.reconfigure(encoding="utf-8")
print(f"corpus            : {len(rows)}")
print(f"AJG >= 2 (kept)   : {len(kept)}")
print(f"excluded by rule  : {len(rows) - len(kept)} "
      f"(AJG 1: {sum(1 for r in rows if r['ajg2024'] == '1')}, "
      f"not in AJG: {sum(1 for r in rows if not r['ajg2024'])})")
benchmarks = [r["first_author"] for r in kept
              if any(n in r["authors"] for n in ("Babina", "Lui A", "Krakowski"))]
print(f"benchmarks kept   : {benchmarks}")
print(f"wrote {OUT.name}")
