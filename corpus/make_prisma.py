# -*- coding: utf-8 -*-
"""PRISMA-style flow diagram for the Method chapter.

All counts are frozen method documentation (CLAUDE.md, screening CSV) — hard-coded
on purpose, with a checksum so the chain cannot drift silently. Style matches
corpus/make_figures.py (Okabe-Ito, serif). Output: figures/fig_prisma.pdf.

Canonical 4-box chain; each main box carries the count ENTERING that stage:
identified 432 -> screened 174 -> full text 81 -> included 67.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent.parent
BLUE = "#0072B2"

# frozen PRISMA chain (17-18 July 2026)
IDENTIFIED = 432
AFTER_AJG, EXCL_AJG1, EXCL_UNLISTED = 174, 109, 149
AFTER_TA, E1, E2, E3, E4 = 81, 20, 7, 39, 27
INCLUDED, FT_CONTENT, FT_NR = 67, 12, 2
assert IDENTIFIED - (EXCL_AJG1 + EXCL_UNLISTED) == AFTER_AJG
assert AFTER_AJG - (E1 + E2 + E3 + E4) == AFTER_TA
assert AFTER_TA - (FT_CONTENT + FT_NR) == INCLUDED

plt.rcParams.update({"font.family": "serif", "font.size": 9, "figure.dpi": 150})

MAIN = [
    f"Records identified through Scopus\n(search of 17 July 2026)\nn = {IDENTIFIED}",
    f"Records screened on\ntitle and abstract\nn = {AFTER_AJG}",
    f"Full texts assessed\nfor eligibility\nn = {AFTER_TA}",
    f"Studies included\nin the review\nn = {INCLUDED}",
]
SIDE = [  # side box i hangs on the arrow leaving main box i
    f"Removed by journal-quality filter\n(AJG 2024 rating $\\geq$ 2 required)\nn = {EXCL_AJG1 + EXCL_UNLISTED}\nrated AJG 1: {EXCL_AJG1}\nnot listed in the AJG: {EXCL_UNLISTED}",
    f"Excluded: n = {E1 + E2 + E3 + E4}\nnot empirical (E1): {E1}\nnot firm-level (E2): {E2}\nAI not the investment object (E3): {E3}\nno performance/CA outcome (E4): {E4}",
    f"Excluded: n = {FT_CONTENT + FT_NR}\ncontent-based, E2–E4: {FT_CONTENT}\nfull text not retrievable: {FT_NR}",
]

fig, ax = plt.subplots(figsize=(5.8, 5.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

MX, MW = 0.2, 4.2          # main column x/width
SX, SW = 5.3, 4.5          # side column x/width
YS = [8.5, 5.8, 3.1, 0.4]  # bottom y of each main box
BH = 1.3


def box(x, y, w, h, text, fs):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                facecolor="white", edgecolor=BLUE, linewidth=1.0))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)


for y, text in zip(YS, MAIN):
    box(MX, y, MW, BH, text, 8.4)
for y0, y1 in zip(YS, YS[1:]):  # arrows down the main column
    ax.annotate("", xy=(MX + MW / 2, y1 + BH), xytext=(MX + MW / 2, y0),
                arrowprops=dict(arrowstyle="->", color="black", linewidth=0.9))
for i, text in enumerate(SIDE):
    ymid = (YS[i] + YS[i + 1] + BH) / 2          # midpoint of the connecting arrow
    h = 0.28 * (text.count("\n") + 1) + 0.3
    box(SX, ymid - h / 2, SW, h, text, 7.8)
    ax.annotate("", xy=(SX, ymid), xytext=(MX + MW / 2, ymid),
                arrowprops=dict(arrowstyle="->", color="black", linewidth=0.9))

fig.savefig(ROOT / "figures" / "fig_prisma.pdf", bbox_inches="tight")
print("wrote figures/fig_prisma.pdf")
