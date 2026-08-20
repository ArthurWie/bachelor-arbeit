# -*- coding: utf-8 -*-
"""Generate the appendix coding table (sections/appendix_coding_table.tex).

Two landscape longtables from corpus/coding_table.csv (n = 67, frozen):
  A.1 study characteristics (design side)
  A.2 findings (outcome side)
Re-runnable; the .tex file is fully derived — edit the CSV or this script, never the .tex.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
with open(ROOT / "corpus" / "coding_table.csv", encoding="utf-8-sig") as f:
    ROWS = list(csv.DictReader(f, delimiter=";"))
assert len(ROWS) == 67 and all(r["coding_status"] == "final" for r in ROWS)
ALL_ROWS = list(ROWS)  # pre-excerpt copy for validating the condensed layer

# --excerpt: 25 studies for the supervisor's interim draft, best-ranked journals
# first (AJG 4*, 4, then 3; within a rating by year/author as in the full table);
# separate output file, captions marked as excerpt. The full table is untouched.
EXCERPT = "--excerpt" in sys.argv
if EXCERPT:
    RANK = {"4*": 0, "4": 1, "3": 2, "2": 3}
    ROWS.sort(key=lambda r: RANK[r["ajg2024"]])  # stable: keeps year order within a rating
    ROWS = ROWS[:25] + [r for r in ROWS if r["ajg2024"] == "2"][:3]  # + AJG-2 examples
    ids = {r["study_id"] for r in ROWS}
    assert {"S08", "S14", "S17"} <= ids, "benchmark studies missing from excerpt"
    assert sum(r["ajg2024"] == "2" for r in ROWS) == 3, "AJG-2 examples missing"
    N_NOTE = ("excerpt: 28 of 67 studies --- the 25 in the highest-ranked journals "
              "(AJG 4*, 4, 3) plus the first three AJG 2 studies; within a rating by year")
    OUTFILE = "appendix_coding_table_excerpt.tex"
else:
    N_NOTE = "n = 67"
    OUTFILE = "appendix_coding_table.tex"

# --- reader-facing layer -----------------------------------------------------
# The CSV is the audit trail and stays as coded: path coefficients, hypothesis
# labels, coder shorthand. None of that belongs in a table a reader reads, so the
# cells are cleaned mechanically here (stats, labels, shouting caps) and the ~20
# cells whose internal path arrows cannot be resolved by rule are replaced from
# appendix_overrides.tsv. Rendering only — the coded values never change.

OVERRIDES = {}
_ov = ROOT / "corpus" / "appendix_overrides.tsv"
if _ov.exists():
    with open(_ov, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if not row["study_id"].startswith("#"):
                OVERRIDES[(row["study_id"], row["column"])] = row["text"].strip()

# emphasis words the coder shouted; acronyms (AI, ROA, SOE, TFP, …) stay as they are
SHOUT = {"FULL", "NO", "NOT", "ONLY", "BOTH", "AND", "BY", "NULL", "FAIL", "RELATIVE",
         "LARGER", "WEAKER", "SLOWS", "LOWERS", "AMPLIFIES", "ATTENUATES", "INVERTED",
         "SUBSTITUTES", "SUBSTANCE", "RELATIONAL", "REVENUE", "PROFIT", "MARKET",
         "QUANTIFIED", "CONFIGURATIONAL", "CONTROLS", "SUSTAINABILITY", "VOLATILITY",
         "DEPTH", "BREADTH", "BUYERS", "DEVELOPERS", "NEGATIVELY", "U-SHAPE"}

DROP = [
    r"[-–]?\s*boundary case[^;]*",                 # coder note
    r",?\s*discuss in thesis",                     # coder note
    r"\(abstract:[^)]*\)",                         # coder note
    r"\(Leoni/Wang pattern:[^)]*\)",               # coder cross-reference
    r"^BENCHMARK:\s*",                             # coder tag
    r"\bR2\s*=\s*\.?\d*\.?\d+",                    # model fit
    r"\bModel \d+:\s*",                            # model number
    r"\bH\d+[a-z]?(?:\s*[-/]\s*H?\d+[a-z]?)?\b(?:\s+rejected)?",  # H4, H3a-c, H5/H6
    r"(?<![\d.%])[-+]?\b0\.\d+(?![\d.])\*{0,3}(?!\s*%)",  # path coefficients (0.48***, -0.23*)
    r"\*{1,3}",                                    # orphaned significance stars
]

TIDY = [
    (r"\bn\.s\.", "not significant"),
    (r"\(\s*[^()A-Za-z0-9]*\s*\)", ""),            # parens the drops emptied out
    (r"\(\s+", "("),
    (r"\(\s*[,;:]\s*", "("),
    (r"\s*,\s*\)", ")"),
    (r"\s{2,}", " "),
    (r"\s+([,;:.)])", r"\1"),
    (r"[,;:]\s*([;)])", r"\1"),
    (r"^[\s,;:-]+", ""),
    (r"[\s,;:-]+$", ""),
]


def readable(s):
    for pat in DROP:
        s = re.sub(pat, "", s)
    s = re.sub(r"\b[A-Z][A-Z0-9-]+\b", lambda m: m.group(0).lower() if m.group(0) in SHOUT else m.group(0), s)
    for pat, rep in TIDY:
        s = re.sub(pat, rep, s)
    return s


def cell(r, col):
    return readable(OVERRIDES.get((r["study_id"], col), r[col]))


# --- condensed layer (19 Aug 2026, author's request) --------------------------
# appendix_condensed.tsv holds hand-written, reader-facing short versions of
# selected cells (plus "notes": short evidence tags for the Notes column in
# A.2, derived from quality_notes). Condensed text wins over overrides/readable;
# no entry = unchanged. Rendering only — the coded values never change.

CONDENSED, NOTES = {}, {}
_cd = ROOT / "corpus" / "appendix_condensed.tsv"
if _cd.exists():
    with open(_cd, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["study_id"].startswith("#"):
                continue
            if row["column"] == "notes":
                NOTES[row["study_id"]] = row["text"].strip()
            else:
                CONDENSED[(row["study_id"], row["column"])] = row["text"].strip()

_ALL_IDS = {r["study_id"] for r in ALL_ROWS}
_COLS = {"sample", "ai_measure", "performance_measure", "ca_measure",
         "conditions", "key_finding"}
bad_keys = ([k for k in CONDENSED if k[0] not in _ALL_IDS or k[1] not in _COLS]
            + [s for s in NOTES if s not in _ALL_IDS])
assert not bad_keys, f"invalid condensed keys: {bad_keys[:5]}"

# a condensed cell may not contain a number that is absent from the coded row
_NUM = re.compile(r"\d+(?:[.,]\d+)*")
_BY_ID = {r["study_id"]: r for r in ALL_ROWS}
_SRC = {"notes": "quality_notes"}
bad_nums = []
for (sid, col), text in (list(CONDENSED.items())
                         + [((s, "notes"), t) for s, t in NOTES.items()]):
    row = _BY_ID[sid]
    for n in _NUM.findall(text):
        if n not in row[_SRC.get(col, col)] and not any(n in v for v in row.values()):
            bad_nums.append((sid, col, n))
assert not bad_nums, f"numbers not in coded source: {bad_nums[:8]}"


def cond(r, col, default):
    return CONDENSED.get((r["study_id"], col), default)


def esc(s):
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s


def study_label(r):
    surnames = [a.strip().split(" ")[0].rstrip(",") for a in r["authors"].split(";") if a.strip()]
    if len(surnames) == 1:
        who = esc(surnames[0])
    elif len(surnames) == 2:
        who = f"{esc(surnames[0])} \\& {esc(surnames[1])}"  # escape parts first, \& is LaTeX
    else:
        who = f"{esc(surnames[0])} et al."
    return f"{who} ({r['year']})"


def outcome_measures(r):
    parts = []
    if r["performance_measure"].strip():
        parts.append("Perf: " + cond(r, "performance_measure",
                                      cell(r, "performance_measure")).strip())
    if r["ca_measure"].strip():
        parts.append("CA: " + cond(r, "ca_measure", cell(r, "ca_measure")).strip())
    return esc("; ".join(parts))


OC_SHORT = {"performance": "Perf.", "competitive_advantage": "CA", "both": "Both"}

HEAD = r"""% AUTO-GENERATED by corpus/make_appendix_table.py — do not edit by hand.
\begingroup
\renewcommand{\thetable}{A.\arabic{table}}
\setcounter{table}{0}
\begin{landscape}
\scriptsize
"""

FOOT = r"""\end{landscape}
\endgroup
"""


def longtable(caption, label, colspec, header, rowfn):
    lines = [r"\begin{longtable}{" + colspec + "}",
             r"\caption{" + caption + r"}\label{" + label + r"}\\",
             r"\toprule", header + r" \\", r"\midrule", r"\endfirsthead",
             r"\multicolumn{%d}{@{}l}{\tablename~\thetable{} (continued)}\\" % (header.count("&") + 1),
             r"\toprule", header + r" \\", r"\midrule", r"\endhead",
             r"\bottomrule", r"\endfoot"]
    for r in ROWS:
        lines.append(rowfn(r) + r" \\")
        lines.append(r"\addlinespace[2pt]")
    lines.append(r"\end{longtable}")
    return "\n".join(lines)


t1 = longtable(
    caption=f"Included studies: characteristics and design ({N_NOTE}). Source: author's compilation.",
    label="tab:coding-a1",
    colspec=r"@{}l p{2.6cm} p{3.4cm} p{1.8cm} p{5.0cm} p{2.1cm} p{6.2cm}@{}",
    header=r"ID & Study & Journal (AJG) & Country & Sample & Method & AI investment measure",
    rowfn=lambda r: " & ".join([
        r["study_id"], study_label(r),
        f"{esc(r['journal'])} ({r['ajg2024']})",
        esc(r["country_region"].split(" (")[0]),
        esc(cond(r, "sample", r["sample"])), esc(r["method"]),
        esc(cond(r, "ai_measure", r["ai_measure"]))]),
)

t2 = longtable(
    caption=f"Included studies: outcomes, effect directions, and conditions ({N_NOTE}). Source: author's compilation.",
    label="tab:coding-a2",
    colspec=r"@{}l p{2.4cm} l p{4.2cm} l p{6.2cm} p{6.2cm}@{}",
    header=r"ID & Study & Outcome & Outcome measure(s) & Direction & Conditions & Key finding",
    rowfn=lambda r: " & ".join([
        r["study_id"], study_label(r), OC_SHORT[r["outcome_construct"]],
        outcome_measures(r), esc(r["effect_direction"]),
        esc(cond(r, "conditions", cell(r, "conditions"))),
        esc(cond(r, "key_finding", cell(r, "key_finding")))]),
)
# Notes column trialled and removed again (author's decision, 19 Aug 2026);
# the notes entries stay in appendix_condensed.tsv but are not printed.

# nothing coder-facing may survive into the rendered table
LEFTOVERS = [("->", "path arrow"), ("*", "significance star"), ("n.s.", "shorthand"),
             ("discuss in thesis", "coder note"), ("boundary case", "coder note"),
             ("BENCHMARK", "coder tag"), ("R2", "model fit")]
dirty = [(r["study_id"], col, what) for r in ROWS
         for col in ("conditions", "performance_measure", "ca_measure", "key_finding")
         for tok, what in LEFTOVERS if tok in cond(r, col, cell(r, col))]
dirty += [(sid, "notes", what) for sid, t in NOTES.items()
          for tok, what in LEFTOVERS if tok in t]
assert not dirty, f"coder shorthand left in {len(dirty)} cells: {dirty[:8]}"

out = HEAD + t1 + "\n\n\\clearpage\n" + t2 + "\n" + FOOT
(ROOT / "sections" / OUTFILE).write_text(out, encoding="utf-8")
print("wrote sections/" + OUTFILE + ",", len(ROWS), "rows x 2 tables,",
      len(OVERRIDES), "overrides applied,", len(CONDENSED) + len(NOTES),
      "condensed cells")

# side-by-side review of every condensed cell (author's approval record)
if not EXCERPT and (CONDENSED or NOTES):
    rev = ["# Appendix condensed cells — before/after review",
           "",
           "Derived by corpus/make_appendix_table.py. 'Before' is what the "
           "printed table showed previously (override-cleaned where an "
           "override exists); 'after' is the condensed cell now printed. "
           "The coded values in coding_table.csv are unchanged.", ""]
    for r in ALL_ROWS:
        sid = r["study_id"]
        ent = [(c, CONDENSED[(sid, c)]) for c in
               ("sample", "ai_measure", "performance_measure", "ca_measure",
                "conditions", "key_finding") if (sid, c) in CONDENSED]
        if not ent and sid not in NOTES:
            continue
        rev.append(f"## {sid} — {r['authors'].split(';')[0].strip()} ({r['year']})")
        for c, after in ent:
            before = r[c] if c in ("sample", "ai_measure") else \
                readable(OVERRIDES.get((sid, c), r[c]))
            rev += [f"- **{c}**", f"  - before: {before}", f"  - after: {after}"]
        if sid in NOTES:
            rev += ["- **notes (NOT printed — Notes column removed by the "
                    "author; tags kept in the layer file)**",
                    f"  - before: {r['quality_notes']}",
                    f"  - after: {NOTES[sid]}"]
        rev.append("")
    (ROOT / "corpus" / "appendix_condense_review.md").write_text(
        "\n".join(rev), encoding="utf-8")
    print("wrote corpus/appendix_condense_review.md")
