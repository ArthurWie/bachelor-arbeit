"""Coding-evidence dossier for Arthur's final audit pass over coding_table.csv.

Three subcommands (run with the rag venv python — pdfplumber is calibrated there):

  rows    coding_table.csv  -> corpus/evidence/rows/Sxx.json   (one per study)
  verify  corpus/evidence/Sxx.json quotes get machine-verified in place:
          stage 1 locate the quote in the Docling full text (page segments),
          stage 2 word-sequence check against the real PDF page
          (same cite.py thresholds as the MCP tool: 0.60, x_tolerance=1)
  build   rows + verified quotes -> corpus/coding_evidence.md

Numbers/values in the document come verbatim from coding_table.csv — no LLM
output is trusted for coded values, only for quote selection.
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
EVID = CORPUS / "evidence"
ROWS = EVID / "rows"
DB = ROOT / "rag" / "library.db"
OUT_MD = CORPUS / "coding_evidence.md"

sys.path.insert(0, str(ROOT / "rag"))
from library_core import cite  # noqa: E402

CODING_COLS = [
    "theoretical_lens", "method", "sample", "country_region", "industry",
    "ai_measure", "outcome_construct", "performance_measure", "ca_measure",
    "effect_direction", "conditions", "key_finding", "quality_notes",
    "coding_status",
]

_MARK = re.compile(r"\[S\. (\d+)\]")


def read_table() -> list[dict]:
    with open(CORPUS / "coding_table.csv", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def cmd_rows() -> None:
    ROWS.mkdir(parents=True, exist_ok=True)
    rows = read_table()
    for r in rows:
        p = ROWS / f"{r['study_id']}.json"
        p.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} row files -> {ROWS}")


# --- verify ---

def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def page_segments(full_text: str) -> list[tuple[int, str]]:
    parts = _MARK.split(full_text)
    return [(int(parts[i]), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def locate(quote: str, segs: list[tuple[int, str]]) -> list[int]:
    """PDF pages the quote sits on, [] if not in the full text."""
    for page, text in segs:
        if cite.verify_quote(quote, text):
            return [page]
    for (p1, t1), (p2, t2) in zip(segs, segs[1:]):  # quote spans a page break
        if cite.verify_quote(quote, t1 + " " + t2):
            return [p1] if p1 == p2 else [p1, p2]
    return []


_LIG = re.compile(r"ffi|ffl|ff|fi|fl")


def _norm_word(w: str) -> str:
    return re.sub(r"[^0-9a-zà-ÿ]", "", w.casefold())


def ctrl_f_string(quote: str, page_text: str, penalize_lig: bool) -> str | None:
    """A short substring of the PDF's own text layer (what Ctrl+F searches)
    that also occurs, word for word, inside the quote. Single-line runs are
    preferred (Ctrl+F is most reliable there); two adjacent lines joined as a
    fallback. In split-ligature PDFs, words containing fi/fl/ff are penalized
    because the viewer's find may not match them either."""
    qw = [w for w in (_norm_word(t) for t in quote.split()) if w]
    if len(qw) < 4:
        return None
    lines = page_text.splitlines()
    candidates = lines + [a + " " + b for a, b in zip(lines, lines[1:])]
    best_score, best_raw = 0, None
    for li, line in enumerate(candidates):
        toks = [(m.group(0), m.start(), m.end())
                for m in re.finditer(r"\S+", line)]
        toks = [(t, s, e) for (t, s, e) in toks if _norm_word(t)]
        lw = [_norm_word(t) for t, _, _ in toks]
        i = 0
        while i < len(lw):
            starts = [k for k, w in enumerate(qw) if w == lw[i]]
            run_len = 0
            for k in starts:
                n = 0
                while (i + n < len(lw) and k + n < len(qw)
                       and lw[i + n] == qw[k + n]):
                    n += 1
                run_len = max(run_len, n)
            if run_len >= 4:
                # pick the 4..8-token window inside the run with least penalty
                for wlen in range(min(8, run_len), 3, -1):
                    for off in range(run_len - wlen + 1):
                        window = toks[i + off:i + off + wlen]
                        pen = sum(2 for t, _, _ in window
                                  if penalize_lig and _LIG.search(t.casefold()))
                        # single-line candidates rank above joined pairs
                        score = wlen - pen + (1 if li < len(lines) else 0)
                        if score > best_score:
                            best_score = score
                            best_raw = line[window[0][1]:window[-1][2]]
                i += max(run_len, 1)
            else:
                i += 1
    return best_raw


class PdfCache:
    def __init__(self) -> None:
        self._texts: dict[tuple[str, int], str] = {}

    def page_text(self, file_path: str, page: int) -> str:
        key = (file_path, page)
        if key not in self._texts:
            import pdfplumber
            with pdfplumber.open(file_path) as pdf:
                try:
                    t = pdf.pages[page - 1].extract_text(
                        x_tolerance=cite.PAGE_X_TOLERANCE) or ""
                except IndexError:
                    t = ""
            self._texts[key] = t
        return self._texts[key]


def cmd_verify() -> None:
    conn = _conn()
    offsets = {
        int(r["key"].split(":", 1)[1]): int(r["value"])
        for r in conn.execute(
            "SELECT key, value FROM index_meta WHERE key LIKE 'page_offset:%'")
    }
    cache = PdfCache()
    totals = {"verified": 0, "page-unconfirmed": 0, "not-in-text": 0}
    for jf in sorted(EVID.glob("S*.json")):
        data = json.loads(jf.read_text(encoding="utf-8"))
        doc_id = int(data["study_id"][1:])
        doc = conn.execute(
            "SELECT full_text, file_path FROM documents WHERE id = ?",
            (doc_id,)).fetchone()
        if doc is None or not doc["full_text"]:
            print(f"{jf.name}: document {doc_id} missing in library — skipped")
            continue
        segs = page_segments(doc["full_text"])
        off = offsets.get(doc_id)
        lig_doc = cite.has_split_ligatures(doc["full_text"])
        for q in data.get("quotes", []):
            pages = locate(q["quote"], segs)
            if not pages:
                q["verdict"] = "not-in-text"
                q["located_pdf_pages"] = []
                q["printed_pages"] = None
                q["pdf_seq_score"] = None
            else:
                # Docling sometimes attributes a paragraph to the neighboring
                # page (the MCP tool absorbs this via chunk page RANGES), so on
                # a miss retry single pages in a ±1 window, then the joined
                # window, and cite the best-scoring location.
                def _score(ps: list[int]) -> float:
                    txt = "\n".join(
                        cache.page_text(doc["file_path"], p) for p in ps)
                    return cite.page_sequence_match(q["quote"], txt)

                score = _score(pages)
                if score < cite.PAGE_MATCH_MIN:
                    window = [p for p in range(max(1, pages[0] - 1),
                                               pages[-1] + 2)]
                    cands = [[p] for p in window if [p] != pages]
                    cands.append(window)
                    for cand in cands:
                        s = _score(cand)
                        if s >= cite.PAGE_MATCH_MIN and s > score:
                            pages, score = cand, s
                            if len(cand) == 1:
                                break
                q["located_pdf_pages"] = pages
                q["pdf_seq_score"] = round(score, 2)
                q["verdict"] = ("verified" if score >= cite.PAGE_MATCH_MIN
                                else "page-unconfirmed")
                q["ctrl_f"] = None
                for p in pages:
                    q["ctrl_f"] = ctrl_f_string(
                        q["quote"], cache.page_text(doc["file_path"], p),
                        lig_doc)
                    if q["ctrl_f"]:
                        break
                if off is not None:
                    pp = [p + off for p in pages]
                    q["printed_pages"] = (str(pp[0]) if len(pp) == 1
                                          else f"{pp[0]}\u2013{pp[-1]}")
                else:
                    q["printed_pages"] = None
            totals[q["verdict"]] += 1
        data["has_printed_pagination"] = off is not None
        jf.write_text(json.dumps(data, ensure_ascii=False, indent=1),
                      encoding="utf-8")
    print(f"verify: {totals}")


# --- repair ---

def _windows(segs: list[tuple[int, str]], n_words: int):
    """Candidate windows: per page, sliding word windows sized like the quote."""
    for page, text in segs:
        words = text.split()
        span = max(4, n_words)
        step = max(1, span // 3)
        for i in range(0, max(1, len(words) - span // 2), step):
            yield page, " ".join(words[i:i + span + 8])


def cmd_repair() -> None:
    """Replace not-in-text quotes with the source's exact wording when a
    fuzzy match in the full text is unambiguous (ratio >= 0.85); print the
    rest for manual review."""
    from difflib import SequenceMatcher
    conn = _conn()
    fixed = manual = 0
    for jf in sorted(EVID.glob("S*.json")):
        data = json.loads(jf.read_text(encoding="utf-8"))
        todo = [q for q in data.get("quotes", [])
                if q.get("verdict") == "not-in-text"]
        if not todo:
            continue
        doc_id = int(data["study_id"][1:])
        doc = conn.execute(
            "SELECT full_text FROM documents WHERE id = ?", (doc_id,)).fetchone()
        segs = page_segments(doc["full_text"])
        for q in todo:
            target = re.sub(r"\s+", " ", q["quote"]).strip()
            best, best_page, best_ratio = None, None, 0.0
            for page, w in _windows(segs, len(target.split())):
                r = SequenceMatcher(None, target.casefold(),
                                    w.casefold(), autojunk=False).ratio()
                if r > best_ratio:
                    best, best_page, best_ratio = w, page, r
            if best_ratio >= 0.85:
                # trim window to quote-sized slice with max ratio
                bw = best.split()
                n = len(target.split())
                slice_best, slice_ratio = best, 0.0
                for i in range(0, max(1, len(bw) - n + 3)):
                    for extra in (-2, -1, 0, 1, 2):
                        cand = " ".join(bw[i:i + n + extra])
                        r = SequenceMatcher(None, target.casefold(),
                                            cand.casefold(),
                                            autojunk=False).ratio()
                        if r > slice_ratio:
                            slice_best, slice_ratio = cand, r
                q["quote_original"] = q["quote"]
                q["quote"] = slice_best
                q["repair_note"] = (f"auto-corrected to source wording "
                                    f"(match {slice_ratio:.0%}, PDF p. {best_page})")
                fixed += 1
            else:
                manual += 1
                print(f"MANUAL {data['study_id']} [{','.join(q['fields'])}] "
                      f"best {best_ratio:.0%} on PDF p. {best_page}:\n"
                      f"  quote: {q['quote'][:150]}\n  best : {best[:150]}\n")
        jf.write_text(json.dumps(data, ensure_ascii=False, indent=1),
                      encoding="utf-8")
    print(f"repair: {fixed} auto-corrected, {manual} need manual review "
          f"(re-run verify afterwards)")


# --- build ---

VERDICT_MARK = {
    "verified": "\u2713 verified",
    "page-unconfirmed": "\u26a0 not machine-confirmed on page \u2014 open the page",
    "not-in-text": "\u2717 NOT FOUND in document text \u2014 quote must be fixed",
}


def _cell(v: str) -> str:
    return (v or "\u2014").replace("|", "\\|").replace("\n", " ")


# order of the printed appendix tables, so the author can walk the dossier
# column by column alongside Tables A.1 and A.2
COL_ORDER = [
    "country_region", "sample", "method", "ai_measure",              # A.1
    "outcome_construct", "performance_measure", "ca_measure",
    "effect_direction", "conditions", "key_finding",                 # A.2
    "theoretical_lens", "industry", "quality_notes", "coding_status",  # not printed
]
_POS = {c: i for i, c in enumerate(COL_ORDER)}
_GROUP = {"country_region": "*Table A.1 columns*",
          "outcome_construct": "*Table A.2 columns*",
          "theoretical_lens": "*not printed (coding data only)*"}


def _quote_pos(q: dict) -> int:
    return min((_POS.get(f, len(COL_ORDER)) for f in q.get("fields", [])),
               default=len(COL_ORDER))


def cmd_build() -> None:
    rows = {r["study_id"]: r for r in read_table()}
    sections: list[str] = []
    flagged: list[str] = []
    n_quotes = 0
    n_by_verdict: dict[str, int] = {}
    for sid in sorted(rows):
        r = rows[sid]
        jf = EVID / f"{sid}.json"
        ev = json.loads(jf.read_text(encoding="utf-8")) if jf.exists() else None
        first_author = r["authors"].split(";")[0].strip()
        et_al = " et al." if ";" in r["authors"] else ""
        head = (f"## {sid} \u2014 {first_author}{et_al} "
                f"({r['year']}) \u2014 {r['journal']} (AJG {r['ajg2024']})")
        lines = [head, "",
                 f"DOI: {r['doi'] or '\u2014'} \u00b7 status: {r['coding_status']}"
                 f" \u00b7 PDF: `{r['pdf']}`", ""]
        lines += ["| Column | Coded value |", "|---|---|"]
        for c in COL_ORDER:
            if c in _GROUP:
                lines.append(f"| {_GROUP[c]} | |")
            lines.append(f"| {c} | {_cell(r[c])} |")
        lines.append("")
        study_flags: list[str] = []
        if ev is None:
            study_flags.append("no evidence file")
            lines += ["**\u2717 No evidence file — extraction missing.**", ""]
        else:
            if not ev.get("has_printed_pagination", True):
                lines += ["*No printed pagination in this PDF \u2014 pages below "
                          "are PDF pages; cite by section/article page per the "
                          "frozen rule.*", ""]
            lines.append("### Evidence")
            lines.append("")
            for i, q in enumerate(
                    sorted(ev.get("quotes", []), key=_quote_pos), 1):
                n_quotes += 1
                v = q.get("verdict", "not-in-text")
                n_by_verdict[v] = n_by_verdict.get(v, 0) + 1
                if v == "not-in-text":
                    study_flags.append(f"quote {i} not found in text")
                if q.get("printed_pages"):
                    where = f"p. {q['printed_pages']}"
                    if q.get("located_pdf_pages"):
                        where += (" (PDF p. "
                                  f"{q['located_pdf_pages'][0]})")
                elif q.get("located_pdf_pages"):
                    where = f"PDF p. {q['located_pdf_pages'][0]}"
                    if q.get("section"):
                        where += f", {q['section']}"
                else:
                    where = "page unresolved"
                score = q.get("pdf_seq_score")
                score_s = f", {score:.0%} word sequence" if score is not None else ""
                fields = ", ".join(sorted(
                    q.get("fields", []),
                    key=lambda f: _POS.get(f, len(COL_ORDER))))
                lines.append(f"{i}. **{fields}** \u2014 {where} \u2014 "
                             f"{VERDICT_MARK[v]}{score_s}")
                lines.append(f"   > {q['quote']}")
                if q.get("ctrl_f"):
                    lines.append(f"   Ctrl+F: „{q['ctrl_f']}“")
                elif q.get("located_pdf_pages"):
                    lines.append(
                        "   Ctrl+F: no reliable search string in the PDF text "
                        f"layer — open PDF p. {q['located_pdf_pages'][0]} "
                        "and check visually")
                if q.get("supports"):
                    lines.append(f"   \u2192 {q['supports']}")
                if q.get("tension"):
                    study_flags.append(f"tension on {fields}: {q['tension']}")
                    lines.append(f"   **\u26a0 TENSION:** {q['tension']}")
                lines.append("")
            rc = ev.get("row_check") or {}
            if rc.get("verdict") == "CHECK":
                study_flags.append(f"row check: {rc.get('notes')}")
                lines += [f"**\u26a0 ROW CHECK:** {rc.get('notes')}", ""]
            elif rc.get("notes"):
                lines += [f"*Row check OK: {rc['notes']}*", ""]
        if study_flags:
            flagged.append(f"- **{sid}** \u2014 " + "; ".join(study_flags))
        sections.append("\n".join(lines))

    header = [
        "# Coding Evidence Dossier \u2014 final audit pass",
        "",
        "One section per included study (n = 67): the coding-table row verbatim "
        "from `corpus/coding_table.csv`, then the verbatim source passages that "
        "back each coded value. Every quote was machine-checked in two stages "
        "(verbatim in the extracted full text; word-sequence \u2265 60% on the real "
        "PDF page, pdfplumber x_tolerance=1 \u2014 the same calibration as "
        "`verify_citations`).",
        "",
        "Symbols: \u2713 machine-verified \u00b7 \u26a0 on-page check failed (usually a page "
        "extraction problem, not a wrong quote \u2014 open the page) \u00b7 \u2717 not in "
        "document text (must be fixed). Pages are printed journal pages unless "
        "marked as PDF pages.",
        "",
        "**Order:** columns and evidence follow the printed appendix tables — "
        "first Table A.1 (Country, Sample, Method, AI measure), then Table A.2 "
        "(Outcome, measures, Direction, Conditions, Key finding), then the "
        "coding fields that are not printed (lens, industry, quality notes) — "
        "so you can walk the tables column by column.",
        "",
        "**Manual checking:** every quote carries a `Ctrl+F:` line \u2014 a short "
        "string copied from the PDF's own text layer (what Ctrl+F actually "
        "searches), so it hits even where the readable quote differs from the "
        "PDF internals (ligature splits, lost hyphens). Open the PDF, search "
        "the Ctrl+F string, and read the passage on the stated page. Where no "
        "reliable string exists in the text layer (tables, broken extraction), "
        "the line says so instead of offering a string that might miss.",
        "",
        f"Quotes: {n_quotes} \u00b7 " + " \u00b7 ".join(
            f"{VERDICT_MARK[k].split(' ')[0]} {n_by_verdict.get(k, 0)}"
            for k in ("verified", "page-unconfirmed", "not-in-text")),
        "",
        "## Start here \u2014 flagged studies" if flagged else
        "## No flags \u2014 no study has open issues",
        "",
    ]
    if flagged:
        header += flagged + [""]
    OUT_MD.write_text("\n".join(header) + "\n" + "\n---\n\n".join(sections) + "\n",
                      encoding="utf-8")
    print(f"built {OUT_MD} \u2014 {len(sections)} studies, {n_quotes} quotes, "
          f"{len(flagged)} flagged")


if __name__ == "__main__":
    {"rows": cmd_rows, "verify": cmd_verify, "repair": cmd_repair,
     "build": cmd_build}[sys.argv[1]]()
