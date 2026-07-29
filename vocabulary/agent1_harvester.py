#!/usr/bin/env python3
"""Agent 1 – CEFR Vocabulary Harvester.

Downloads CEFR-tagged word lists from authoritative sources, applies wordfreq
frequency filtering (top 15 000 English lemmas), and writes:
  vocabulary/raw/{a1,a2,b1,b2,c1}.txt   — one lemma per line
  vocabulary/master_vocabulary.csv       — word, cefr_level, frequency_rank
"""

import csv
import logging
import sys
import time
from pathlib import Path

import requests
from wordfreq import top_n_list

# ── Config ────────────────────────────────────────────────────────────────────
RAW_DIR   = Path("vocabulary/raw")
LOG_DIR   = Path("vocabulary/logs")
MASTER    = Path("vocabulary/master_vocabulary.csv")
FREQ_CAP  = 15_000

SOURCES = [
    ("https://raw.githubusercontent.com/winterdl/oxford-5000-vocabulary-audio-definition/main/data/oxford_5000.csv", "csv_level_col"),
    ("https://raw.githubusercontent.com/openlanguageprofiles/olp-en-cefrj/master/cefrj-vocabulary-profile-1.5.csv", "csv_level_col"),
]

VALID_LEVELS = {"A1", "A2", "B1", "B2", "C1"}
# ─────────────────────────────────────────────────────────────────────────────

log = logging.getLogger(__name__)


def _fetch(url: str, retries: int = 1) -> str | None:
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            log.info("Downloaded %s (%d bytes)", url, len(r.content))
            return r.text
        except requests.RequestException as exc:
            log.warning("Attempt %d failed for %s: %s", attempt + 1, url, exc)
            if attempt < retries:
                time.sleep(2)
    log.error("FAILED to download %s after %d attempts", url, retries + 1)
    return None


def _parse_csv_level_col(text: str) -> list[tuple[str, str]]:
    """Parse CSV that has separate word and cefr/level columns."""
    reader = csv.DictReader(text.splitlines())
    fields = [f.lower() for f in (reader.fieldnames or [])]
    word_col  = next((f for f in fields if "word" in f or "lemma" in f or "headword" in f), None)
    level_col = next((f for f in fields if "cefr" in f or "level" in f), None)
    if not word_col or not level_col:
        log.error("CSV missing word/level column; fields=%s", reader.fieldnames)
        return []
    orig_fields = reader.fieldnames or []
    orig_word  = next(c for c in orig_fields if c.lower() == word_col)
    orig_level = next(c for c in orig_fields if c.lower() == level_col)
    reader = csv.DictReader(text.splitlines())
    return [
        (row[orig_word].strip().lower(), row[orig_level].strip().upper())
        for row in reader
        if row.get(orig_word) and row.get(orig_level, "").strip().upper() in VALID_LEVELS
    ]


def _parse_plain(text: str, level: str) -> list[tuple[str, str]]:
    """Parse plain text with one word per line; level supplied externally."""
    return [
        (line.strip().lower(), level.upper())
        for line in text.splitlines()
        if line.strip() and not line.startswith("#")
    ]


def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_DIR / "agent1.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    log.info("=== Agent 1 starting ===")

    log.info("Building frequency whitelist: top %d English lemmas", FREQ_CAP)
    freq_list = top_n_list("en", FREQ_CAP)
    freq_set  = set(freq_list)
    freq_rank = {w: i + 1 for i, w in enumerate(freq_list)}
    log.info("Frequency whitelist ready (%d words)", len(freq_set))

    collected: dict[str, tuple[str, int]] = {}

    for url, fmt in SOURCES:
        text = _fetch(url)
        if text is None:
            continue

        if fmt == "csv_level_col":
            entries = _parse_csv_level_col(text)
        elif fmt.startswith("plain_"):
            level = fmt.split("_", 1)[1].upper()
            entries = _parse_plain(text, level)
        else:
            log.error("Unknown format %r for %s; skipping", fmt, url)
            continue

        kept = 0
        for word, level in entries:
            if word in freq_set and word not in collected:
                collected[word] = (level, freq_rank[word])
                kept += 1
        log.info("Source %s: parsed %d entries, kept %d after freq filter", url, len(entries), kept)

    if not collected:
        log.error("No words collected from any source — aborting")
        sys.exit(1)

    by_level: dict[str, list[str]] = {lvl: [] for lvl in ("A1", "A2", "B1", "B2", "C1")}
    for word, (level, _) in collected.items():
        by_level[level].append(word)

    for level, words in by_level.items():
        out = RAW_DIR / f"{level.lower()}.txt"
        out.write_text("\n".join(sorted(set(words))), encoding="utf-8")
        log.info("Wrote %d words to %s", len(words), out)

    with MASTER.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["word", "cefr_level", "frequency_rank"])
        for word, (level, rank) in sorted(collected.items(), key=lambda x: x[1][1]):
            writer.writerow([word, level, rank])

    total = len(collected)
    log.info("master_vocabulary.csv written: %d entries", total)
    print(f"Agent 1 complete — {total} words written to {MASTER}")


if __name__ == "__main__":
    main()
