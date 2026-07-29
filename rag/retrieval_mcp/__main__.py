"""MCP-Server für Claude Code. Registrierung:

    claude mcp add library -- python -m retrieval_mcp

Regeln (§4 Schritt 6):
- Jede Rückgabe enthält chunk_id und Seitenzahl – ohne sie kann nicht
  korrekt zitiert werden.
- Rückgaben als lesbarer, kompakter Text, nicht als rohes JSON.
- Kein Anthropic-API-Client: Die Synthese macht Claude Code selbst.
- Die gesamte Suchlogik lebt in library_core; hier wird nur formatiert.
"""

from __future__ import annotations

import json
import re

from mcp.server.fastmcp import FastMCP

from library_core import cite, db, retrieve

mcp = FastMCP("library")


def _conn():
    return db.connect()


_INITIALS_RE = re.compile(r"^(?:[A-Z]\.?){1,4}$")


def _surname(name: str) -> str:
    """Nachname aus einem Autorennamen.

    Der Korpus liefert Scopus-Reihenfolge („Wamba-Taguimdje S.L.“), also steht
    der Nachname VORNE. Ein einfaches „letztes Wort“ würde daraus „S.L.“
    machen. Fällt auf das letzte Wort zurück, wenn keine Initialen am Ende
    stehen (Reihenfolge „Vorname Nachname“).
    """
    parts = name.split()
    if not parts:
        return name
    head = [p for p in parts if not _INITIALS_RE.match(p)]
    return " ".join(head) if head and len(head) < len(parts) else parts[-1]


def _authors_short(authors_json: str | list) -> str:
    authors = (
        json.loads(authors_json or "[]")
        if isinstance(authors_json, str)
        else authors_json
    )
    if not authors:
        return "o. A."
    first = _surname(authors[0])
    return first if len(authors) == 1 else f"{first} et al."


def _span(a: int, b: int) -> str:
    return f"{a}" if a == b else f"{a}–{b}"


def _ligature_warning(text: str) -> str:
    """Hinweis, wenn der Auszug getrennte Ligaturen trägt („fi rm“).

    Betrifft 16 der 67 Studien. Der Auszug bleibt unverändert – automatisch
    zusammenzuziehen wäre nicht sicher (siehe cite.has_split_ligatures). Für
    ein wörtliches Zitat daraus gilt: Wortlaut von der PDF-Seite nehmen.
    verify_citations akzeptiert die korrigierte Schreibweise.
    """
    if not cite.has_split_ligatures(text):
        return ""
    return ("\n  [!] Getrennte Ligaturen im Quelltext („fi rm“ statt „firm“). "
            "Für ein wörtliches Zitat den Wortlaut von der PDF-Seite nehmen; "
            "die korrigierte Schreibweise wird von verify_citations akzeptiert.")


def _pages(
    page_start: int,
    page_end: int,
    printed_start: int | None = None,
    printed_end: int | None = None,
) -> str:
    """Seitenangabe für die Fußnote.

    Gedruckte Seitenzahl zum Zitieren, PDF-Seite in Klammern – zum Nachprüfen
    blättert man die PDF-Seite auf, zitiert wird aber die gedruckte. Wo keine
    gedruckte Seitenzahl erkannt wurde, sagt die Ausgabe das ausdrücklich,
    damit keine PDF-Seite als Druckseite in eine Fußnote wandert.
    """
    pdf = _span(page_start, page_end)
    if printed_start is None:
        return (f"PDF-S. {pdf} (keine gedruckte Seitenzahl erkannt – "
                "nicht als Druckseite zitieren)")
    printed = _span(printed_start, printed_end if printed_end is not None
                    else printed_start)
    return f"S. {printed}" if printed == pdf else f"S. {printed} (PDF-S. {pdf})"


def _format_results(results: list[retrieve.SearchResult]) -> str:
    if not results:
        return ("Keine Treffer. Die Bibliothek enthält dazu offenbar nichts – "
                "das ist eine gültige Antwort, bitte nicht raten.")
    parts = []
    for r in results:
        head = (
            f"[chunk_id {r.chunk_id}] {_authors_short(r.authors)} "
            f"({r.year or 'o. J.'}): {r.title} — "
            f"{_pages(r.page_start, r.page_end, r.printed_start, r.printed_end)}, "
            f"Abschnitt „{r.section}“ (Relevanz {r.score:.2f})"
        )
        parts.append(f"{head}{_ligature_warning(r.text)}\n{r.text}")
    return "\n\n---\n\n".join(parts)


@mcp.tool()
def search_library(query: str, year_min: int | None = None, k: int = 12) -> str:
    """Hybride Suche über die Literaturbibliothek (semantisch + lexikalisch).
    Gibt Auszüge mit Titel, Autor, Jahr, Seitenzahl und chunk_id zurück."""
    results = retrieve.search(query, year_min=year_min, k=k, conn=_conn())
    return _format_results(results)


@mcp.tool()
def search_library_multi(queries: list[str], k: int = 12) -> str:
    """Mehrere Query-Varianten suchen und per RRF fusionieren.
    Claude erzeugt die Varianten (Umformulierungen + hypothetische Antwort).
    Die erste Query der Liste muss die Originalfrage sein."""
    results = retrieve.search_multi(queries, k=k, conn=_conn())
    return _format_results(results)


@mcp.tool()
def find_relevant_documents(query: str, k: int = 5) -> str:
    """Wählt ganze relevante Dokumente aus. Gibt document_id, Titel, Jahr
    und eine kurze Begründung. Für Synthese- und Vergleichsfragen."""
    docs = retrieve.find_documents(query, k=k, conn=_conn())
    if not docs:
        return ("Kein Dokument der Bibliothek passt erkennbar zu dieser Frage – "
                "das ist eine gültige Antwort, bitte nicht raten.")
    parts = []
    for d in docs:
        evidence = "; ".join(
            f"Abschnitt „{e['section']}“ ("
            f"{_pages(e['page_start'], e['page_end'], e.get('printed_start'), e.get('printed_end'))}, "
            f"chunk_id {e['chunk_id']}, Relevanz {e['score']:.2f})"
            for e in d["evidence"]
        )
        parts.append(
            f"[document_id {d['document_id']}] {_authors_short(d['authors'])} "
            f"({d['year'] or 'o. J.'}): {d['title']}\n"
            f"  Begründung: Treffer in {evidence}"
        )
    return "\n\n".join(parts)


@mcp.tool()
def read_full_document(document_id: int) -> str:
    """Vollständiger Text eines Papers inklusive [S. N]-Seitenmarkern."""
    conn = _conn()
    row = conn.execute(
        "SELECT id, title, authors, year, full_text FROM documents WHERE id = ?",
        (document_id,),
    ).fetchone()
    if row is None:
        return f"Kein Dokument mit document_id {document_id}."
    if not row["full_text"]:
        return (f"Dokument {document_id} ({row['title']}) hat keinen "
                "geparsten Volltext.")
    head = (
        f"[document_id {row['id']}] {_authors_short(row['authors'])} "
        f"({row['year'] or 'o. J.'}): {row['title']}\n"
        "Seitenzahlen stehen als [S. N]-Marker im Text.\n"
    )
    return head + _ligature_warning(row["full_text"]) + "\n" + row["full_text"]


@mcp.tool()
def get_chunk_context(chunk_id: int, window: int = 1) -> str:
    """Angrenzende Chunks laden, wenn ein Auszug abgeschnitten wirkt."""
    conn = _conn()
    rows = retrieve.chunk_context(conn, chunk_id, window=window)
    if not rows:
        return f"Kein Chunk mit chunk_id {chunk_id}."
    offsets = db.page_offsets(conn)
    parts = []
    for r in rows:
        marker = " (angefragter Chunk)" if r["chunk_id"] == chunk_id else ""
        off = offsets.get(r["document_id"])
        pages = _pages(
            r["page_start"], r["page_end"],
            None if off is None else r["page_start"] + off,
            None if off is None else r["page_end"] + off,
        )
        parts.append(
            f"[chunk_id {r['chunk_id']}]{marker} "
            f"{_authors_short(r['authors'])} ({r['year'] or 'o. J.'}): "
            f"{r['title']} — {pages}, "
            f"Abschnitt „{r['section']}“{_ligature_warning(r['text'])}"
            f"\n{r['text']}"
        )
    return "\n\n---\n\n".join(parts)


@mcp.tool()
def list_documents(query: str | None = None) -> str:
    """Bibliothek überblicken und prüfen, was indexiert ist."""
    conn = _conn()
    sql = (
        "SELECT d.id, d.title, d.authors, d.year, d.parse_ok, d.is_scan, "
        "       COUNT(c.id) AS n_chunks "
        "FROM documents d LEFT JOIN chunks c ON c.document_id = d.id "
    )
    params: tuple = ()
    if query:
        sql += "WHERE d.title LIKE ? OR d.authors LIKE ? "
        params = (f"%{query}%", f"%{query}%")
    sql += "GROUP BY d.id ORDER BY d.year, d.title"
    rows = conn.execute(sql, params).fetchall()
    if not rows:
        return "Keine passenden Dokumente in der Bibliothek."
    lines = []
    for r in rows:
        status = "indexiert" if r["n_chunks"] else (
            "geprüft, noch nicht indexiert" if r["parse_ok"] else "NICHT geprüft (parse_ok=0)"
        )
        scan = ", Scan/OCR" if r["is_scan"] else ""
        lines.append(
            f"[document_id {r['id']}] {_authors_short(r['authors'])} "
            f"({r['year'] or 'o. J.'}): {r['title']} — {status}, "
            f"{r['n_chunks']} Chunks{scan}"
        )
    return "\n".join(lines)


@mcp.tool()
def verify_citations(citations: list[dict]) -> str:
    """Wörtliche Zitate programmatisch prüfen, BEVOR sie in der Antwort landen.
    Erwartet [{"quote": "...", "chunk_id": 123}, ...].

    Zwei Stufen: (1) Kommt das Zitat wörtlich im Chunk vor (whitespace-
    normalisiert, case-insensitiv), ersatzweise im Volltext des Dokuments?
    (2) Stehen seine Wörter in derselben Reihenfolge auf der echten PDF-Seite?
    Stufe 2 fängt zusätzlich eine falsche Seitenzuordnung ab.
    Nicht bestätigte Zitate MÜSSEN in der Antwort als [unbestätigt] markiert
    werden."""
    conn = _conn()

    def short(q: str) -> str:
        return q if len(q) <= 80 else q[:80] + "…"

    lines = []
    for i, c in enumerate(citations, start=1):
        quote = str(c.get("quote", ""))
        chunk_id = c.get("chunk_id")
        if not quote or chunk_id is None:
            lines.append(f"{i}. FEHLER: quote und chunk_id sind Pflicht.")
            continue
        try:
            cid = int(str(chunk_id).strip())
        except ValueError:
            lines.append(
                f"{i}. FEHLER: chunk_id {chunk_id!r} ist keine Zahl – "
                "die numerische chunk_id aus dem Suchergebnis übergeben."
            )
            continue
        row = conn.execute(
            "SELECT document_id, text FROM chunks WHERE id = ?", (cid,)
        ).fetchone()
        if row is None:
            lines.append(f"{i}. FEHLER: chunk_id {cid} existiert nicht.")
            continue
        if cite.verify_quote(quote, row["text"]):
            _, pdf_note = cite.check_quote_against_pdf(conn, quote, cid)
            lines.append(f"{i}. BESTÄTIGT ({pdf_note}): „{short(quote)}“")
        elif cite.verify_quote_in_document(conn, quote, row["document_id"]):
            lines.append(
                f"{i}. BESTÄTIGT (im Dokument, aber nicht in Chunk {cid} – "
                f"Seitenzahl gegen den Volltext prüfen): „{short(quote)}“"
            )
        else:
            lines.append(
                f"{i}. NICHT BESTÄTIGT – dieses Zitat kommt so nicht im "
                f"Quelltext vor. In der Antwort als [unbestätigt] markieren "
                f"oder korrigieren: „{short(quote)}“"
            )
    return "\n".join(lines)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
