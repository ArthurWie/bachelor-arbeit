"""Blind section review — Gate 3 des Cross-Check-Workflows (CLAUDE.md).

    python corpus/gemini_section_review.py sections/method.tex

Einmal pro fertigem Kapitel: agy (Gemini) bekommt NUR das Kapitel + FACT_SHEET.md
— inline im Prompt, nicht als Dateien, weil agys Datei-Tools im Headless-Modus
auto-verweigert werden und --dangerously-skip-permissions einem Agenten mehr
freischalten wuerde als noetig. cwd bleibt trotzdem ein leerer Sandbox-Ordner.
Es urteilt, aendert aber nichts; alle Flags entscheidet Arthur
(corpus/section_review_<datei>.md).

Limit: Windows-Argumentlaenge ~32k Zeichen — bei groesseren Kapiteln meldet
das Skript den Ueberlauf, statt still abzuschneiden.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AGY = rf"{Path.home()}\AppData\Local\agy\bin\agy.exe"

PROMPT = """You are reviewing one finished chapter of an academic thesis (a systematic literature review of 67 studies), blind. Below you get two documents: the CHAPTER (LaTeX source) and the FACT SHEET holding the canonical numbers derived from the review's coding table.

Report findings in exactly three categories:

1. NUMBERS: any count, percentage, or distribution in the chapter that CONTRADICTS the fact sheet. The chapter also contains process numbers (search hits, screening counts, inter-coder agreement) that are legitimately not on the fact sheet -- flag only contradictions, never mere absence.
2. CONSISTENCY: statements inside the chapter that contradict each other, or claims that contradict the fact sheet.
3. AI-STYLE: sentences with typical AI-writing patterns (stock idioms, inflated significance claims, formulaic antithesis, filler phrases). Quote the sentence.

For each finding: quote the exact text, name the category, and give one line of reasoning. If a category has no findings, write "none". Do not comment on style preferences, structure, citation formatting, or LaTeX commands. Do not rewrite anything.

=== CHAPTER (chapter.tex) ===
{chapter}

=== FACT SHEET (FACT_SHEET.md) ===
{facts}
"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("texfile", type=Path)
    ap.add_argument("-m", "--model", default="gemini-3.1-pro-high")
    args = ap.parse_args()

    prompt = PROMPT.format(
        chapter=args.texfile.read_text(encoding="utf-8"),
        facts=(ROOT / "FACT_SHEET.md").read_text(encoding="utf-8"))
    # CreateProcess erlaubt 32.767 Zeichen; agy.exe wird direkt gestartet (kein
    # .cmd-Wrapper mit 8k-Limit), Aufruf-Overhead ~80 Zeichen -> 32.5k ist sicher.
    if len(prompt) > 32500:
        sys.exit(f"Prompt {len(prompt)} Zeichen > 32.5k — Kapitel splitten "
                 f"oder Uebergabe per Datei loesen, nicht abschneiden.")

    sandbox = ROOT / "_agy_review_sandbox"          # leer — agy soll nichts lesen
    if sandbox.exists():
        shutil.rmtree(sandbox)
    sandbox.mkdir()
    p = subprocess.run([AGY, "-p", prompt, "--model", args.model],
                       cwd=sandbox, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=900)
    shutil.rmtree(sandbox)

    out = ROOT / f"section_review_{args.texfile.stem}.md"
    body = (p.stdout or "").strip()
    if p.returncode != 0 or not body:
        body += "\n\n[agy exit code {}]\n{}".format(p.returncode, (p.stderr or "").strip())
    out.write_text(
        f"# Blind Section Review {args.texfile.name} — {args.model}\n\n"
        f"{body}\n\n---\n\n**Entscheidung Arthur (je Flag):**\n",
        encoding="utf-8")
    print(f"→ {out.name} (exit {p.returncode}, {len(body)} Zeichen)")


if __name__ == "__main__":
    main()
