"""Blind second-coder run: Gemini codes every included study independently.

Independence design: Gemini receives ONLY the frozen coding scheme and the
paper's PDF text - never Claude's drafts. Output: one JSON per study in
corpus/gemini_coding/. Resume-safe (skips studies already coded).
Compare afterwards with compare_coders.py (to be run when this finishes).
"""
import csv
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "gemini_coding"
OUT.mkdir(exist_ok=True)

PROMPT = """You are an independent coder in a systematic literature review on the question: under what conditions do firm-level AI investments translate into competitive advantage and superior firm performance?

Read the paper text below and code it. Reply with ONLY a JSON object (no markdown fence, no commentary) with exactly these keys:

- "method": one of "survey-SEM", "panel econometrics", "event study", "case study", "experiment", "fsQCA", "DEA", "mixed"
- "ai_measure": short phrase - how the firms' AI investment/adoption is operationalized (e.g. survey construct, patents, announcements, 10-K text, resume-based, adoption dummy, case observation)
- "outcome_construct": "performance" if the study measures firm performance outcomes (productivity, profit, firm value, growth, efficiency); "competitive_advantage" ONLY if it measures a distinct competitive-advantage construct (sustained/positional advantage, perceived CA scale); "both" if both are measured separately
- "effect_direction": "positive", "negative", "mixed", "null", or "conditional" (use "conditional" only if the effect exists or flips ONLY under certain conditions; if there is a clear average main effect, use its sign)
- "conditions": short list (as one string, ';'-separated) of the moderators/mediators/complements/thresholds the study identifies for the AI-outcome link; "" if none
- "key_finding": one sentence in your own words

PAPER TEXT:
"""


def pdf_text(path, limit=45000):
    with pdfplumber.open(path) as pdf:
        t = " ".join((p.extract_text() or "") for p in pdf.pages)
    t = re.sub(r"\s+", " ", t)
    if len(t) <= limit:
        return t
    # keep front (title/abstract/method) and back (results/discussion)
    return t[: int(limit * 0.7)] + " [...] " + t[-int(limit * 0.3):]


rows = list(csv.DictReader(open(ROOT / "coding_table.csv", encoding="utf-8-sig"), delimiter=";"))
todo = [r for r in rows if not (OUT / f"{r['study_id']}.json").exists()]
print(f"{len(todo)} studies to code (of {len(rows)})", flush=True)

for r in todo:
    sid = r["study_id"]
    pdf = ROOT.parent / "literature" / r["pdf"]
    try:
        text = pdf_text(pdf)
    except Exception as e:
        print(f"{sid} PDF ERROR: {e}", flush=True)
        continue
    prompt = PROMPT + text
    ok = False
    for attempt in range(3):
        try:
            # prompt via stdin - Windows command lines are capped at ~32k chars
            p = subprocess.run(
                [r"C:\Users\arthu\AppData\Roaming\npm\gemini.cmd", "-m", "gemini-2.5-pro"],
                input=prompt, capture_output=True, text=True,
                encoding="utf-8", errors="replace", timeout=300)
            raw = (p.stdout or "").strip()
            m = re.search(r"\{.*\}", raw, re.S)
            data = json.loads(m.group(0))
            need = {"method", "ai_measure", "outcome_construct", "effect_direction", "conditions", "key_finding"}
            if not need.issubset(data):
                raise ValueError(f"missing keys: {need - set(data)}")
            (OUT / f"{sid}.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
            print(f"{sid} OK ({data['outcome_construct']}, {data['effect_direction']})", flush=True)
            ok = True
            break
        except Exception as e:
            print(f"{sid} attempt {attempt+1} failed: {str(e)[:120]}", flush=True)
            time.sleep(20 * (attempt + 1))
    if not ok:
        print(f"{sid} GIVING UP for now (re-run script to retry)", flush=True)
    time.sleep(5)  # stay under free-tier rate limits

done = len(list(OUT.glob("S*.json")))
print(f"\nfinished: {done}/{len(rows)} coded", flush=True)
