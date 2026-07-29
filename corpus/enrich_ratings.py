"""Enrich the frozen corpus with AJG 2024 journal ratings.

Matches primarily on ISSN (print + electronic), falls back to normalized
journal title. Writes corpus_<date>_rated.csv and prints the rating
distribution used to set the inclusion threshold.
"""
import csv
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "corpus_2026-07-17.csv"
AJG = ROOT / "ratings" / "ajg2024.xlsx"
OUT = ROOT / "corpus_2026-07-17_rated.csv"


def norm_issn(s):
    s = re.sub(r"[^0-9X]", "", (s or "").upper())
    return s if len(s) == 8 else ""


def norm_title(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


rows = list(open(AJG, "rb") and openpyxl.load_workbook(AJG, read_only=True).active.iter_rows(values_only=True))
header, rows = rows[0], rows[1:]

by_issn, by_title = {}, {}
for r in rows:
    field, title, rating = r[0], r[1], str(r[3]).strip()
    rec = {"ajg2024": rating, "ajg_field": field, "ajg_title": title}
    for issn in (norm_issn(str(r[16])), norm_issn(str(r[17]))):
        if issn:
            by_issn[issn] = rec
    by_title[norm_title(title)] = rec

corpus = list(csv.DictReader(open(CORPUS, encoding="utf-8-sig")))
matched_issn = matched_title = 0
for c in corpus:
    rec = by_issn.get(norm_issn(c["issn"])) or by_issn.get(norm_issn(c["eissn"]))
    if rec:
        matched_issn += 1
    else:
        rec = by_title.get(norm_title(c["journal"]))
        if rec:
            matched_title += 1
    c["ajg2024"] = rec["ajg2024"] if rec else ""
    c["ajg_field"] = rec["ajg_field"] if rec else ""

cols = list(corpus[0].keys())
with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(corpus)

sys.stdout.reconfigure(encoding="utf-8")
n = len(corpus)
print(f"matched via ISSN : {matched_issn}")
print(f"matched via title: {matched_title}")
print(f"unmatched        : {n - matched_issn - matched_title}")
print("\nAJG 2024 distribution (n=432):")
from collections import Counter
dist = Counter(c["ajg2024"] or "not in AJG" for c in corpus)
order = ["4*", "4", "3", "2", "1", "not in AJG"]
cum = 0
for k in order:
    v = dist.pop(k, 0)
    cum += v
    print(f"  {k:>10}: {v:4d}   (cumulative: {cum})")
for k, v in dist.items():
    print(f"  {k:>10}: {v:4d}")
print(f"\nwrote {OUT.name}")
