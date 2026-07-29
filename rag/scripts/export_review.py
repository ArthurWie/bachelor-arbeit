"""Markdown-Export für die Sichtprüfung (Schritt 2).

    python -m scripts.export_review                    # exportiert alles
    python -m scripts.export_review --mark-ok ABCD1234 # parse_ok=1 setzen

Schreibt pro Dokument review/<zotero_key>.md und einen Sammelreport
review/_report.md mit Auffälligkeiten. Ab der Sichtprüfung gilt: indexiert
wird ausschließlich, was parse_ok = 1 hat.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from library_core import config, db

_PAGE_SPLIT = re.compile(r"\[S\. (\d+)\]")


def _page_chars(full_text: str) -> dict[int, int]:
    """Zeichen pro Seite aus den [S. N]-Markern rekonstruieren."""
    parts = _PAGE_SPLIT.split(full_text or "")
    chars: dict[int, int] = {}
    # parts = [präambel, page1, text1, page2, text2, ...]
    for i in range(1, len(parts) - 1, 2):
        page = int(parts[i])
        chars[page] = chars.get(page, 0) + len(parts[i + 1].strip())
    return chars


def _findings(full_text: str, num_pages: int | None = None) -> list[str]:
    findings = []
    if not (full_text or "").strip():
        return ["VOLLTEXT LEER"]
    chars = _page_chars(full_text)
    if not chars:
        return ["keine Seitenmarker im Volltext"]
    # Echte Seitenzahl (aus dem Parser) schlägt den letzten Marker – sonst
    # bleiben fehlende Schlussseiten (z. B. verworfenes Material) unsichtbar.
    max_page = max(num_pages or 0, max(chars))
    missing = [p for p in range(1, max_page + 1) if p not in chars]
    thin = [p for p, c in chars.items() if c < config.SCAN_CHAR_THRESH]
    if missing:
        findings.append(f"keine Inhalte auf Seite(n) {missing}")
    if thin:
        findings.append(f"< {config.SCAN_CHAR_THRESH} Zeichen auf Seite(n) {sorted(thin)}")
    if "## " not in full_text:
        findings.append("keine Sektionsstruktur erkannt")
    return findings


def _scopus_first_pages() -> dict[str, int | None]:
    """study_id → erste gedruckte Seite laut Scopus (Prüfwert, optional)."""
    try:
        from library_core import corpus
        return {d.study_id: d.printed_first for d in corpus.documents()}
    except Exception:
        return {}


def _pages_note(conn, doc_id: int, printed_first: int | None) -> str:
    """Zustand der Druckseiten-Kalibrierung für den Report."""
    raw = db.get_meta(conn, f"page_offset:{doc_id}")
    if raw is None:
        return "keine → PDF-Seiten"
    offset = int(raw)
    labels = db.get_meta(conn, f"page_labels:{doc_id}")
    n_obs = len(json.loads(labels)) if labels else 0
    if printed_first is None:
        return f"Offset {offset} ({n_obs} Fußzeilen)"
    if offset == printed_first - 1:
        return f"Offset {offset} ✓"
    return f"Offset {offset} ≠ Scopus {printed_first - 1} – PRÜFEN"


def export(conn, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = conn.execute(
        "SELECT id, zotero_key, title, authors, year, doi, full_text, is_scan, "
        "parse_ok FROM documents ORDER BY year, title"
    ).fetchall()
    if not rows:
        print("Keine Dokumente in der DB. Erst `python -m scripts.ingest "
              "--parse-only` laufen lassen.")
        return

    report = [
        "# Sichtprüfungs-Report",
        "",
        "Prüfen pro Dokument: Lesereihenfolge bei zweispaltigem Layout, "
        "Tabellen erhalten, keine fehlenden Abschnitte. Danach freigeben mit "
        "`python -m scripts.export_review --mark-ok <zotero_key>`.",
        "",
        "| Dokument | Key | Seiten | Ø Zeichen/Seite | Druckseiten | Scan | "
        "parse_ok | Auffälligkeiten |",
        "|---|---|---|---|---|---|---|---|",
    ]
    scopus_first = _scopus_first_pages()

    for r in rows:
        authors = ", ".join(json.loads(r["authors"] or "[]")) or "o. A."
        chars = _page_chars(r["full_text"] or "")
        num_pages_meta = db.get_meta(conn, f"num_pages:{r['id']}")
        num_pages = int(num_pages_meta) if num_pages_meta else None
        pages = num_pages or (max(chars) if chars else 0)
        avg = int(sum(chars.values()) / len(chars)) if chars else 0
        findings = _findings(r["full_text"] or "", num_pages)

        pages_note = _pages_note(conn, r["id"], scopus_first.get(r["zotero_key"]))

        doc_md = out_dir / f"{r['zotero_key']}.md"
        doc_md.write_text(
            f"# {r['title']}\n\n"
            f"- **Autoren:** {authors}\n"
            f"- **Jahr:** {r['year'] or '?'}  **DOI:** {r['doi'] or '–'}\n"
            f"- **Scan/OCR:** {'ja' if r['is_scan'] else 'nein'}  "
            f"**parse_ok:** {r['parse_ok']}\n"
            f"- **Druckseiten:** {pages_note}\n"
            f"- **Auffälligkeiten:** {'; '.join(findings) or 'keine'}\n\n"
            "---\n\n"
            f"{r['full_text'] or '(kein Volltext)'}\n",
            encoding="utf-8",
        )

        report.append(
            f"| {r['title'][:50]} | `{r['zotero_key']}` | {pages} | {avg} | "
            f"{pages_note} | {'ja' if r['is_scan'] else ''} | "
            f"{'✓' if r['parse_ok'] else ''} | {'; '.join(findings) or ''} |"
        )

    (out_dir / "_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"{len(rows)} Dokumente nach {out_dir}/ exportiert, "
          f"Report: {out_dir / '_report.md'}")


def mark_ok(conn, keys: list[str]) -> None:
    for key in keys:
        cur = conn.execute(
            "UPDATE documents SET parse_ok = 1 WHERE zotero_key = ?", (key,)
        )
        if cur.rowcount == 0:
            print(f"UNBEKANNTER Key: {key}")
        else:
            print(f"parse_ok=1 gesetzt: {key}")
    conn.commit()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mark-ok", nargs="+", metavar="ZOTERO_KEY",
                    help="Dokument(e) nach Sichtprüfung freigeben")
    ap.add_argument("--out", default="review", help="Zielverzeichnis")
    ap.add_argument("--db", default=None)
    args = ap.parse_args()

    conn = db.connect(args.db)
    db.init_db(conn)

    if args.mark_ok:
        mark_ok(conn, args.mark_ok)
    else:
        export(conn, Path(args.out))


if __name__ == "__main__":
    main()
