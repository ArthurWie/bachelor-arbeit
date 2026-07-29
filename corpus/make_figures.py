# -*- coding: utf-8 -*-
"""Descriptive figures for the results chapter (mapping of the corpus, n=67).

Reads corpus/coding_table.csv (frozen, all rows coding_status=final) and writes
PDF figures to figures/. Re-runnable: figures are fully derived from the CSV.

Colors: Okabe-Ito subset, validated colorblind-safe (dataviz six-checks, 18 Jul 2026).
"""
import csv
import collections
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

BLUE = "#0072B2"  # single-series color
DIRECTION_COLORS = {  # stack order = key order; validated as adjacent pairs
    "positive": "#0072B2",
    "conditional": "#E69F00",
    "mixed": "#CC79A7",
    "negative": "#D55E00",
}

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.axisbelow": True,
    "figure.dpi": 150,
})

with open(ROOT / "corpus" / "coding_table.csv", encoding="utf-8-sig") as f:
    ROWS = list(csv.DictReader(f, delimiter=";"))
assert len(ROWS) == 67, f"expected 67 rows, got {len(ROWS)}"
assert all(r["coding_status"] == "final" for r in ROWS), "non-final rows present"


def style_axis(ax, xgrid=False):
    ax.grid(axis="x" if xgrid else "y", color="#d9d9d9", linewidth=0.6)
    ax.tick_params(length=0)


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight")
    plt.close(fig)
    print("wrote", OUT / name)


# --- Fig 1: publications per year (full search window 2015-2026) ------------
years = collections.Counter(int(r["year"]) for r in ROWS)
xs = list(range(2015, 2027))
ys = [years.get(y, 0) for y in xs]
fig, ax = plt.subplots(figsize=(5.8, 2.6))
ax.bar(xs, ys, color=BLUE, width=0.7)
for x, y in zip(xs, ys):
    if y:
        ax.text(x, y + 0.3, str(y), ha="center", va="bottom", fontsize=8)
ax.set_xticks(xs)
ax.set_ylabel("Included studies")
ax.set_ylim(0, max(ys) + 3)
style_axis(ax)
save(fig, "fig_year.pdf")

# --- Fig 2: methods ----------------------------------------------------------
METHOD_LABELS = {
    "panel econometrics": "Panel econometrics",
    "survey-SEM": "Survey (SEM)",
    "mixed": "Mixed methods",
    "event study": "Event study",
    "case study": "Case study",
    "survey-based regression (two cross-sectional surveys)": "Survey (regression)",
    "fsQCA": "fsQCA",
    "DEA": "DEA",
}
methods = collections.Counter(METHOD_LABELS[r["method"]] for r in ROWS)
labels, counts = zip(*methods.most_common())
fig, ax = plt.subplots(figsize=(5.8, 2.6))
ax.barh(range(len(labels)), counts, color=BLUE, height=0.65)
ax.set_yticks(range(len(labels)), labels)
ax.invert_yaxis()
for i, c in enumerate(counts):
    ax.text(c + 0.3, i, str(c), va="center", fontsize=8)
ax.set_xlabel("Included studies")
ax.set_xlim(0, max(counts) + 3)
style_axis(ax, xgrid=True)
save(fig, "fig_method.pdf")

# --- Fig 3: geography of study samples --------------------------------------
def region(raw):
    r = raw.lower()
    if r.startswith("multi") or "asia-pacific" in r or "china + europe" in r:
        return "Multi-country"
    if r in ("eu", "europe") or r.startswith(("eu (", "europe (")):
        return "Europe (multi-country)"
    return raw.split(" (")[0]  # "India (South India)" -> "India"

geo = collections.Counter(region(r["country_region"]) for r in ROWS)
main = [(k, v) for k, v in geo.most_common() if v >= 2]
other = sum(v for _, v in geo.items() if v < 2)
labels = [k for k, _ in main] + [f"Other single-country ({other} × 1)"]
counts = [v for _, v in main] + [other]
fig, ax = plt.subplots(figsize=(5.8, 3.0))
ax.barh(range(len(labels)), counts, color=BLUE, height=0.65)
ax.set_yticks(range(len(labels)), labels)
ax.invert_yaxis()
for i, c in enumerate(counts):
    ax.text(c + 0.2, i, str(c), va="center", fontsize=8)
ax.set_xlabel("Included studies (sample location)")
ax.set_xlim(0, max(counts) + 2)
style_axis(ax, xgrid=True)
save(fig, "fig_geography.pdf")

# --- Fig 4: outcome construct x effect direction (feedback #1 visible) -------
OUTCOMES = [("performance", "Firm performance"),
            ("both", "Both constructs"),
            ("competitive_advantage", "Competitive advantage")]
cross = {ok: collections.Counter() for ok, _ in OUTCOMES}
for r in ROWS:
    cross[r["outcome_construct"]][r["effect_direction"]] += 1
fig, ax = plt.subplots(figsize=(5.8, 2.4))
left = [0.0] * len(OUTCOMES)
for direction, color in DIRECTION_COLORS.items():
    vals = [cross[ok][direction] for ok, _ in OUTCOMES]
    bars = ax.barh(range(len(OUTCOMES)), vals, left=left, color=color,
                   height=0.6, label=direction.capitalize(),
                   edgecolor="white", linewidth=1.5)
    for i, (b, v) in enumerate(zip(bars, vals)):
        if v:
            ax.text(b.get_x() + b.get_width() / 2, i, str(v), ha="center",
                    va="center", fontsize=8, color="white", fontweight="bold")
    left = [l + v for l, v in zip(left, vals)]
ax.set_yticks(range(len(OUTCOMES)), [lbl for _, lbl in OUTCOMES])
ax.invert_yaxis()
ax.set_xlabel("Included studies")
ax.legend(loc="lower right", frameon=False, ncols=4, bbox_to_anchor=(1, 1.02))
style_axis(ax, xgrid=True)
save(fig, "fig_outcome_direction.pdf")

# --- Fig 5: journal quality (AJG 2024) ---------------------------------------
order = ["2", "3", "4", "4*"]
ajg = collections.Counter(r["ajg2024"] for r in ROWS)
fig, ax = plt.subplots(figsize=(3.2, 2.4))
ax.bar(range(len(order)), [ajg[k] for k in order], color=BLUE, width=0.6)
ax.set_xticks(range(len(order)), order)
for i, k in enumerate(order):
    ax.text(i, ajg[k] + 0.5, str(ajg[k]), ha="center", fontsize=8)
ax.set_xlabel("AJG 2024 rating")
ax.set_ylabel("Included studies")
ax.set_ylim(0, max(ajg.values()) + 4)
style_axis(ax)
save(fig, "fig_ajg.pdf")

print("done: 5 figures, n =", len(ROWS))
