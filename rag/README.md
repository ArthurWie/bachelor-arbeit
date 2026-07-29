# library-rag

Lokales Recherche- und Zitations-Tool über eine Zotero-Bibliothek (~70 PDFs).
Hybride Suche (semantisch + BM25 + Reranking) läuft komplett lokal auf der
GPU; die Synthese macht Claude Code über einen MCP-Server. Jede Aussage ist
mit wörtlichem Zitat und Seitenzahl belegt und programmatisch verifizierbar.

**Zielrechner: Windows-PC mit RTX 4060 (8 GB VRAM).** Auf anderen Rechnern
laufen nur die Tests – Embedding/Reranking halten ohne CUDA absichtlich an.

---

## 1. Voraussetzungen (einmalig)

| Was | Wozu | Woher |
|---|---|---|
| NVIDIA-Treiber (aktuell) | CUDA für fp8-Embedding | GeForce Experience / nvidia.com |
| Claude Code | Synthese über MCP | claude.com/claude-code |

**Quelle ist der eingefrorene Korpus der Arbeit, nicht Zotero** (siehe
`docs/ABWEICHUNGEN.md` Nr. 10): `corpus/coding_table.csv`,
`corpus/corpus_2026-07-17.csv` und die 67 PDFs in `literature/`. Erwartet werden
sie im übergeordneten Projektordner; andere Orte über die Umgebungsvariablen
`CORPUS_DIR` / `LITERATURE_DIR`. Node.js braucht nur, wer den Reader nachrüstet.

## 2. Setup (automatisch)

Projektordner auf den PC kopieren – **ohne** `.venv/` und
`frontend/node_modules/` (falls vom Mac mitkopiert: löschen, die sind
plattformspezifisch). Dann im Projektordner:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1
```

Das Script installiert `uv`, erstellt `.venv` mit Python 3.12, installiert
**zuerst das CUDA-Build von PyTorch** (wichtig – das normale PyPI-Wheel ist
auf Windows CPU-only), dann alle übrigen Abhängigkeiten, lässt die Testsuite
laufen und prüft, ob CUDA die 4060 sieht. Am Ende muss dastehen:
`CUDA verfuegbar: True | GPU: … 4060 …` und `62 passed`.
Das Frontend wird bewusst übersprungen (nicht im Umfang).

## 3. Ablauf (in dieser Reihenfolge)

Alle Kommandos im Projektordner, mit `.venv\Scripts\python.exe` (oder venv
aktivieren: `.venv\Scripts\activate`).

**Schritt A – Einlesen:**

```powershell
.venv\Scripts\python.exe -m scripts.ingest --parse-only
```

Parst die 67 PDFs des Korpus mit Docling (OCR aus; erkannte Scans bekommen
automatisch einen zweiten Durchlauf mit EasyOCR). Wiederaufnehmbar: bei Abbruch
einfach neu starten, Unverändertes wird über den `content_hash` übersprungen.
Nebenbei wird pro Dokument die **Druckseiten-Kalibrierung** gemeldet
(`Seitenzahlen: Offset 204 …`); Zeilen mit `ABWEICHUNG` vor dem Zitieren an
einer Seite prüfen. Dauer: rund 40 Minuten für 67 Papers.

Hinweis zur Fortschrittsanzeige: Bei Umleitung in eine Datei puffert Python die
Ausgabe. Den echten Stand liefert die DB:
`SELECT COUNT(*) FROM documents WHERE full_text IS NOT NULL`.

**Schritt B – Sichtprüfung** (der wichtigste manuelle Schritt):

```powershell
.venv\Scripts\python.exe -m scripts.export_review
```

Erzeugt `review\_report.md` (Übersicht + Auffälligkeiten) und pro Paper eine
Markdown-Datei. **Reduzierter Umfang** (siehe `RAG_INTEGRATION_PLAN.md`): nicht
alle 67 Papers einzeln durchsehen, sondern die Auffälligkeiten-Spalte des
Reports abarbeiten und den Rest gesammelt freigeben. Die wortgetreue
Absicherung der Fußnoten passiert ohnehin später gegen das PDF selbst.
Freigeben (Key ist die `study_id`, z. B. `S03`):

```powershell
.venv\Scripts\python.exe -m scripts.export_review --mark-ok S03 S04 S05
```

(Mehrere Keys auf einmal möglich. Nur freigegebene Papers werden indexiert.)

**Schritt C – Indexieren** (~1 Stunde GPU-Zeit, einmalig):

```powershell
.venv\Scripts\python.exe -m scripts.ingest --index-only
```

Beim ersten Lauf werden die Modelle von HuggingFace geladen (~10 GB, einmalig;
Cache-Ort optional per `MODEL_CACHE`-Umgebungsvariable). Das Skript
verifiziert automatisch, dass fp8 aktiv ist (~4 GB VRAM statt ~8) und bricht
mit klarer Meldung ab, wenn nicht – dann NICHT auf andere Präzision
ausweichen, sondern melden (siehe Troubleshooting).

**Schritt D – Testfragen & Messung:**

30 Fragen in `eval\questions.yaml` eintragen (Anleitung steht in der Datei,
Verteilung: 10 fact / 8 concept / 8 cross / 4 negative), dann:

```powershell
.venv\Scripts\python.exe -m scripts.run_eval
```

Ziel: `recall_at_12 ≥ 0.85`, `abstain_rate ≥ 0.75`. Ergebnisse landen
versioniert in `eval\results\`.

**Schritt E – An Claude Code anbinden:**

```powershell
claude mcp add library --env DB_PATH=<ABSOLUTER\PFAD>\library.db -- <ABSOLUTER\PFAD>\.venv\Scripts\python.exe -m retrieval_mcp
```

Beide Pfade absolut angeben (die DB liegt nach dem Ingest als `library.db`
im Projektordner). Danach in Claude Code testen: *„Nutze list_documents und
zeig mir die Bibliothek."* Die Nutzungsregeln für Claude stehen in
`CLAUDE.md` und werden automatisch gelesen, wenn Claude Code im
Projektordner gestartet wird.

**Schritt F – Reader-Oberfläche (optional):**

```powershell
.venv\Scripts\python.exe -m uvicorn api.main:app --port 8000
```

und in einem zweiten Terminal:

```powershell
cd frontend; npm run dev
```

Dann http://localhost:5173 öffnen. Klick auf einen Suchtreffer öffnet das
PDF an der zitierten Stelle mit Highlight. Deep-Link: `?chunk=<id>`.

## 4. Troubleshooting

- **„Korpusdatei fehlt" / „PDFs fehlen":** Der Adapter sucht die eingefrorenen
  Dateien im übergeordneten Projektordner. Andere Ablage → `CORPUS_DIR` und
  `LITERATURE_DIR` setzen. Fehlt ein einzelnes PDF, bricht der Ingest bewusst ab,
  statt die Bibliothek stillschweigend unvollständig zu lassen.
- **„finegrained-fp8 kernel requires the `kernels` package" / `No module named
  'triton'`:** fp8 braucht in transformers 5.x einen Kernel aus dem Kernel-Hub,
  und der ist Triton-basiert. Fix: `uv pip install --python .venv\Scripts\python.exe
  "kernels==0.15.2" triton-windows` (steht seit dem 27.07.2026 in `pyproject.toml`;
  siehe `docs/ABWEICHUNGEN.md` Nr. 12). **Nicht** auf fp16/int8 ausweichen.
- **„CUDA nicht verfügbar … Anhalten":** Es ist das CPU-Wheel von torch
  installiert. Fix: `uv pip install --python .venv\Scripts\python.exe torch --index-url https://download.pytorch.org/whl/cu128 --reinstall`
- **„fp8 ist mit dieser Toolchain nicht erreichbar":** Erst
  `transformers`/`accelerate` aktualisieren. Hilft das nicht (fp8-Kernel
  unter nativem Windows), ist der saubere Weg WSL2 (Ubuntu) oder ein
  vorquantisiertes FP8-Repo des Modells – **nicht** auf fp16/int8 ausweichen,
  die DB wäre sonst inkonsistent zur Konfiguration.
- **CUDA-OOM beim Indexieren:** passiert automatisch nichts Schlimmes – die
  Batchgröße wird schrittweise gesenkt. VRAM-Budget: 4 GB Embedder + 1,2 GB
  Reranker.
- **„index_meta passt nicht zur Config":** Die DB wurde mit anderen
  Einstellungen gebaut. `library.db` löschen und neu indexieren.
- **Erste Suche nach Sitzungsstart hängt minutenlang:** Der Serverprozess lädt beide
  Modelle (Embedder 4,1 GB + Reranker). Ist die GPU von anderen Programmen belegt, fällt
  PyTorch unter Windows in geteilten Systemspeicher statt mit OOM abzubrechen, und der
  Ladevorgang dauert ein Vielfaches – im Extremfall über 30 Minuten (einmal beobachtet).
  Danach sind Einzel- und Mehrfachsuche normal schnell, auch bei knappem VRAM. Abhilfe:
  GPU-hungrige Programme schließen oder eine kleine Suche als Aufwärmrunde absetzen.
  `list_documents` braucht kein Modell und antwortet immer sofort.
- **Suche findet nichts:** Wurden Papers freigegeben (`--mark-ok`)? Nur
  `parse_ok=1` wird indexiert – `list_documents` (MCP) zeigt den Status.
- **Seitenzahl sieht falsch aus:** `S. 207 (PDF-S. 3)` heißt: 207 gehört in die
  Fußnote, 3 blättert man zum Nachprüfen auf. Steht dort
  `PDF-S. 3 (keine gedruckte Seitenzahl erkannt)`, hat das PDF keine
  Druckpaginierung (z. B. Emerald) – dann nicht die PDF-Seite als Druckseite
  ausgeben, sondern über Abschnitt oder Artikelnummer zitieren.

## 5. Tests

```powershell
.venv\Scripts\python.exe -m pytest tests -q
```

62 Tests, laufen ohne GPU (DB-Trigger, RRF, Chunking, Zitatverifikation,
Hybrid-Suche mit synthetischen Vektoren, Korpus-Adapter gegen die echten
Korpusdateien, Druckseiten-Kalibrierung, Zitier-Formatierung, Seitenbeleg
über die Wortfolge und Erkennung getrennter Ligaturen).

## 6. Was wo liegt

```
library_core/     Suchlogik (einzige Implementierung – MCP und API importieren nur)
  corpus.py       Korpusquelle: coding_table.csv + Scopus-Export + literature/
                  (ersetzt zotero.py, das gelöscht wurde – siehe ABWEICHUNGEN Nr. 10)
retrieval_mcp/    MCP-Server für Claude Code (7 Werkzeuge)
api/ + frontend/  FastAPI + React-Reader (nicht installiert, nachrüstbar)
scripts/          ingest / export_review / run_eval / setup_windows.ps1
eval/             Testfragen (questions.yaml) + Messergebnisse (leer, siehe Plan)
docs/             SPEC.md (Original-Vorgabe), KONZEPT.md, ABWEICHUNGEN.md
CLAUDE.md         Nutzungs- und Zitierregeln (gilt auch in der Arbeit selbst)
library.db        SQLite-Datenbank (entsteht beim Ingest)
```

Die Einbau-Entscheidungen und was bewusst weggelassen wurde, stehen in
`../RAG_INTEGRATION_PLAN.md`; die Nutzungsregeln für die Arbeit im Abschnitt
„Library Tools" der `../CLAUDE.md`.
