#!/usr/bin/env python3
"""Pipeline orchestrator: runs Agent 1 then Agent 2 in sequence."""

import subprocess
import sys
from pathlib import Path


def run(script: str) -> None:
    print(f"\n{'='*60}\nRunning {script}\n{'='*60}")
    result = subprocess.run(
        [sys.executable, script],
        capture_output=False,
    )
    if result.returncode != 0:
        print(f"\nERROR: {script} exited with code {result.returncode}. Aborting.")
        sys.exit(result.returncode)
    print(f"\n{script} completed successfully.\n")


def main() -> None:
    master = Path("vocabulary/master_vocabulary.csv")
    if master.exists():
        answer = input("master_vocabulary.csv already exists. Re-run Agent 1? [y/N] ").strip().lower()
        if answer != "y":
            print("Skipping Agent 1 — using existing master_vocabulary.csv")
        else:
            run("vocabulary/agent1_harvester.py")
    else:
        run("vocabulary/agent1_harvester.py")

    run("vocabulary/agent2_matcher.py")
    print("\nPipeline complete.")
    print("  Final output:  vocabulary/project_vocabulary.csv")
    print("  Report:        vocabulary/vocabulary_report.md")


if __name__ == "__main__":
    main()
