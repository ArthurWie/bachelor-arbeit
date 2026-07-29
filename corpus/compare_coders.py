"""Compare Claude (coder 1, coding_table.csv) vs Gemini (coder 2, gemini_coding/*.json).

Compared categorically: method, outcome_construct, effect_direction.
Free-text columns (ai_measure, conditions) are attached for context, plus a flag
when one coder found conditions and the other found none.

Output: corpus/adjudication_list.csv
  - all disagreement rows (Arthur decides, fills `resolution`)
  - + a fixed random sample of 10 agreement rows (marked SAMPLE) as human spot-check
Prints per-column agreement rates for the methods chapter.
"""
import csv
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = list(csv.DictReader(open(ROOT / "coding_table.csv", encoding="utf-8-sig"), delimiter=";"))

CATS = ["method", "outcome_construct", "effect_direction"]
agree = {c: 0 for c in CATS}
full_agree, disagreements, agreements = [], [], []

for r in rows:
    g = json.loads((ROOT / "gemini_coding" / f"{r['study_id']}.json").read_text(encoding="utf-8"))
    diffs = [c for c in CATS if r[c].strip().lower() != str(g[c]).strip().lower()]
    cond_flag = (bool(r["conditions"].strip()) != bool(str(g["conditions"]).strip()))
    for c in CATS:
        if c not in diffs:
            agree[c] += 1
    rec = dict(study_id=r["study_id"], authors=r["authors"].split(";")[0], year=r["year"],
               differing_fields="; ".join(diffs) + ("; conditions-existence" if cond_flag else ""),
               claude_method=r["method"], gemini_method=g["method"],
               claude_outcome=r["outcome_construct"], gemini_outcome=g["outcome_construct"],
               claude_direction=r["effect_direction"], gemini_direction=g["effect_direction"],
               claude_conditions=r["conditions"], gemini_conditions=g["conditions"],
               gemini_key_finding=g["key_finding"], row_type="DISAGREEMENT", resolution="")
    if diffs or cond_flag:
        disagreements.append(rec)
    else:
        rec["row_type"] = "SAMPLE"
        agreements.append(rec)

random.seed(20260718)  # fixed seed = reproducible sample
sample = random.sample(agreements, min(10, len(agreements)))

out = ROOT / "adjudication_list.csv"
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(disagreements[0].keys()) if disagreements else list(sample[0].keys()), delimiter=";")
    w.writeheader()
    w.writerows(disagreements)
    w.writerows(sample)

n = len(rows)
print(f"studies compared : {n}")
for c in CATS:
    print(f"agreement {c:18s}: {agree[c]}/{n} ({agree[c]/n:.0%})")
print(f"rows fully agreeing  : {len(agreements)}/{n}")
print(f"adjudication needed  : {len(disagreements)} disagreements + {len(sample)} sample rows -> {out.name}")
