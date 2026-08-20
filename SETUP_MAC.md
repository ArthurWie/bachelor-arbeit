# Setup auf dem MacBook (Urlaubs-Arbeitsumgebung)

Stand 29. Juli 2026. Das Repo enthält alles Eingefrorene (Korpus, Coding-Tabelle,
`rag/library.db`, alle 76 Literatur-PDFs) — auf dem Mac wird nur Werkzeug neu
installiert, keine Daten neu erzeugt.

## 1. LaTeX

```bash
brew install --cask mactex-no-gui
```

Kompilieren (auf dem Mac funktioniert `latexmk`, Perl ist vorinstalliert):

```bash
latexmk -pdf main.tex
```

Oder die Handkette wie unter Windows: `pdflatex` → `biber main` → 2× `pdflatex`.
Gleiches gilt für `BA_Zwischenstand_2026-07-29.tex`.

## 2. Python-venv für die Library-Tools (optional, ~15 Min)

Das Windows-venv ist ausgeschlossen (`.gitignore`); auf dem Mac neu bauen:

```bash
cd rag
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

`triton-windows` überspringt sich auf macOS von selbst (Plattform-Marker),
torch kommt als CPU-Wheel. Danach den MCP-Server registrieren:

```bash
claude mcp add library --env DB_PATH="$(pwd)/library.db" -- "$(pwd)/.venv/bin/python" -m retrieval_mcp
```

### Was auf dem Air läuft — und was nicht

| Tool | Läuft? | Warum |
|---|---|---|
| `list_documents`, `get_chunk_context`, `read_full_document` | ja | reine DB-Lesezugriffe |
| `verify_citations` | ja | String-Abgleich (sqlite + pdfplumber), **keine Modelle** |
| `search_library`, `search_library_multi`, `find_relevant_documents` | **nein** | laden ~6 GB Embedding-/Reranker-Modelle — zu groß für das Air |

## 2b. Zellen-Audit-Tool (Stand 20. Aug 2026)

Das Audit läuft im Browser (React-Frontend + FastAPI). Einmalig nach dem Klonen:

```bash
# Schritt 2 oben (venv) muss erledigt sein — fastapi/uvicorn kommen mit `pip install -e .`
brew install node        # falls Node noch fehlt
cd rag/frontend && npm install
```

Danach bei jeder Sitzung nur noch:

```bash
rag/start_audit.sh       # startet API + Frontend, öffnet localhost:5173/?view=audit
```

Urteile landen append-only in `corpus/author_audit.csv` — nach der Sitzung
committen/pushen, dann sind sie auf dem Hauptrechner. Die 28 Zellen der
Flag-Aufarbeitung vom 20. Aug tragen ein „2. Pass: geändert"-Badge; die Taste
G springt von Zelle zu Zelle (Begründungen: `corpus/audit_flag_resolutions.md`).

## 3. Arbeits-Regeln unterwegs (Kurzfassung der CLAUDE.md-Regeln)

- **Passagen finden ohne Suche:** PDFs in `literature/` direkt lesen; die
  `conditions`-/`key_finding`-Spalten in `corpus/coding_table.csv` sagen pro
  Studie, wonach zu suchen ist.
- **Zitate:** am Seitenbild prüfen (Goldstandard). `verify_citations` braucht
  eine `chunk_id` aus der Suche — für unterwegs neu gefundene Zitate stattdessen
  `[unbestätigt]` markieren und daheim nachziehen.
- **Zahlen** kommen weiterhin nur aus der Coding-Tabelle bzw. dem Fact Sheet,
  nie aus Erinnerung.
- **Kapitel-Reihenfolge für den Urlaub:** Methode (Vollfassung), Einleitung,
  Limitations/Conclusion brauchen den RAG-Server nicht. 4.2 (Synthese) ist der
  RAG-hungrige Block — Passagen dafür idealerweise vor Abreise sammeln.
- **Scopus/VPN wird nicht gebraucht** — der Korpus ist eingefroren. Der API-Key
  (`.scopus_api_key`) bleibt bewusst außerhalb des Repos.

## 4. pdfplumber-Einzeiler (Mac-Variante)

```bash
rag/.venv/bin/python -c "
import pdfplumber, sys
with pdfplumber.open('literature/DATEI.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        t = page.extract_text()
        if t: print(f'--- PAGE {i+1} ---\n{t}')
"
```

Zweispaltige Verlags-PDFs wie unter Windows spaltenweise mit
`page.crop((0, 0, w/2, h))` und `extract_text(x_tolerance=1.4)` extrahieren
(siehe CLAUDE.md, „Reading PDFs").
