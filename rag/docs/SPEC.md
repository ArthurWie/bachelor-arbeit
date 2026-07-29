# Implementierungsauftrag: lokales Recherche- und Zitations-Tool
Diese Datei ist die vollständige Vorgabe. **Alle technischen Entscheidungen sind getroffen.** Weiche nicht ab und schlage keine Alternativen vor. Wenn etwas unmöglich erscheint, melde es und halte an, statt zu improvisieren.
---
## 0. Auftrag
Baue ein lokales RAG-System über eine Zotero-Literaturbibliothek (~70 wissenschaftliche PDFs). Es wird über einen MCP-Server von Claude Code genutzt und später über eine React-Oberfläche gelesen. Kernanforderung ist **prüfbare Zitierbarkeit**: jede Aussage muss mit wörtlichem Zitat und Seitenzahl belegt und programmatisch verifiziert sein.
### Harte Randbedingungen
| | |
|---|---|
| GPU | RTX 4060, **8 GB VRAM** – niemals überschreiten |
| Netz | **Keine Cloud-APIs für Embedding oder Reranking.** Alles lokal |
| Korpusgröße | ~70 Dokumente, ~5.000 Chunks. Optimiere dafür, nicht für Skalierung |
| Laufzeit | Unkritisch. Qualität hat immer Vorrang vor Geschwindigkeit |
| Sprachen | Deutsch und Englisch gemischt |
### Festgelegte Modelle – nicht ersetzen
```
Embedding : Qwen/Qwen3-Embedding-4B   fp8, 2560 Dim, keine MRL-Truncation
Reranking : BAAI/bge-reranker-v2-m3   fp16
Parsing   : Docling, do_ocr = False
OCR       : EasyOCR (Docling-Default), nur für erkannte Scans, lang=["en","de"]
Synthese  : Claude via Claude Code (kein API-Client im Code!)
```
VRAM-Budget: 4,0 GB (Embedder) + 1,2 GB (Reranker) = **5,2 GB**, beide dauerhaft geladen.
---
## 1. Projektstruktur
Erzeuge genau diese Struktur:
```
library-rag/
├── pyproject.toml
├── CLAUDE.md                  # Nutzungsregeln für Claude Code, siehe §8
├── .env.example               # ZOTERO_BASE_URL, DB_PATH, MODEL_CACHE
├── library_core/
│   ├── __init__.py
│   ├── config.py              # zentrale Konstanten, siehe §2
│   ├── db.py                  # Schema, Trigger, Verbindung
│   ├── zotero.py              # Client für die lokale Zotero-API
│   ├── parse.py               # Docling-Wrapper
│   ├── chunk.py               # strukturbewusstes Chunking
│   ├── embed.py               # Qwen3-Embedding, Laden + Encode
│   ├── retrieve.py            # hybrid + RRF + Rerank
│   └── cite.py                # Zitat-Verifikation
├── retrieval_mcp/
│   ├── __init__.py
│   └── __main__.py            # MCP-Server, siehe §7
├── api/
│   └── main.py                # FastAPI für das Frontend
├── scripts/
│   ├── ingest.py              # Volldurchlauf Zotero → DB
│   ├── export_review.py       # Markdown-Export für die Sichtprüfung
│   └── run_eval.py            # Eval-Harness
├── eval/
│   └── questions.yaml
└── frontend/                  # erst in Schritt 8
```
**`library_core` ist die einzige Implementierung der Suchlogik.** `retrieval_mcp` und `api` importieren sie. Dupliziere niemals Retrieval-Code.
### Dependencies
```toml
[project]
requires-python = ">=3.11"
dependencies = [
  "docling",
  "sentence-transformers",
  "torch",
  "sqlite-vec",
  "mcp>=1.0,<2.0",        # v2 benennt FastMCP um -> würde brechen
  "fastapi",
  "uvicorn",
  "httpx",
  "pyyaml",
  "numpy",
]
```
---
## 2. `config.py` – alle Konstanten an einem Ort
```python
EMBED_MODEL      = "Qwen/Qwen3-Embedding-4B"
EMBED_PRECISION  = "fp8"
EMBED_DIM        = 2560          # nativ, keine Truncation
RERANK_MODEL     = "BAAI/bge-reranker-v2-m3"
RERANK_MAX_LEN   = 1024
CHUNK_TOKENS     = 600
CHUNK_OVERLAP    = 0.15
SCAN_CHAR_THRESH = 100           # < 100 Zeichen/Seite => Scan-Verdacht
CAND_PER_METHOD  = 200           # dense und BM25 je 200
RRF_K            = 60
FINAL_K          = 12
QUERY_INSTRUCTION = (
    "Given a research question, retrieve passages from scientific "
    "papers that directly answer it."
)
ZOTERO_BASE = "http://localhost:23119"
```
Diese Werte sind bewusst gesetzt. Ändere sie nicht eigenmächtig.
---
## 3. Datenbank (`db.py`)
SQLite, eine Datei. Lege Schema **und** Trigger in einer idempotenten `init_db()` an.
```sql
CREATE TABLE IF NOT EXISTS documents (
  id            INTEGER PRIMARY KEY,
  zotero_key    TEXT UNIQUE,
  title         TEXT,
  authors       TEXT,              -- JSON-Array
  year          INTEGER,
  doi           TEXT,
  file_path     TEXT,
  full_text     TEXT,              -- kompletter Text mit [S. N]-Markern
  content_hash  TEXT,
  is_scan       INTEGER DEFAULT 0,
  parse_ok      INTEGER DEFAULT 0, -- wird in Schritt 2 manuell gesetzt
  parsed_at     TEXT
);
CREATE TABLE IF NOT EXISTS chunks (
  id            INTEGER PRIMARY KEY,
  document_id   INTEGER REFERENCES documents(id) ON DELETE CASCADE,
  ordinal       INTEGER,
  section       TEXT,
  page_start    INTEGER,
  page_end      INTEGER,
  bbox          TEXT,              -- JSON [{page,x0,y0,x1,y1,coord_origin}]
  text          TEXT,              -- Original. Wird zitiert.
  embed_text    TEXT,              -- mit Kontextpräfix. Wird embedded.
  token_count   INTEGER
);
CREATE TABLE IF NOT EXISTS index_meta (
  key TEXT PRIMARY KEY, value TEXT
);
-- Pflicht beim Ingest: embed_model, embed_precision, embed_dim
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
  text, section, content='chunks', content_rowid='id',
  tokenize='unicode61 remove_diacritics 2'
);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_vec USING vec0(
  chunk_id INTEGER PRIMARY KEY, embedding FLOAT[2560]
);
CREATE TABLE IF NOT EXISTS eval_questions (
  id INTEGER PRIMARY KEY,
  question TEXT,
  gold_chunk_ids TEXT,             -- JSON-Array
  kind TEXT                        -- fact | concept | cross | negative
);
```
**Trigger sind Pflicht.** FTS5-External-Content-Tabellen pflegen sich nicht selbst; ohne sie liefert die Keyword-Suche stillschweigend keine Treffer:
```sql
CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
  INSERT INTO chunks_fts(rowid, text, section) VALUES (new.id, new.text, new.section);
END;
CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
  INSERT INTO chunks_fts(chunks_fts, rowid, text, section)
    VALUES('delete', old.id, old.text, old.section);
END;
CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
  INSERT INTO chunks_fts(chunks_fts, rowid, text, section)
    VALUES('delete', old.id, old.text, old.section);
  INSERT INTO chunks_fts(rowid, text, section) VALUES (new.id, new.text, new.section);
END;
```
`sqlite-vec` muss per `conn.enable_load_extension(True)` und `sqlite_vec.load(conn)` geladen werden, **bevor** die vec0-Tabelle angesprochen wird.
**Abnahme:** `init_db()` zweimal hintereinander ausführbar ohne Fehler. Ein Test fügt einen Chunk ein und findet ihn über `chunks_fts` per MATCH wieder.
---
## 4. Schritte
Arbeite in dieser Reihenfolge. Jeder Schritt hat Abnahmekriterien; erfülle sie, bevor du weitergehst.
### Schritt 1 — Zotero-Ingest und Parsing
**`zotero.py`**
- Basis: `http://localhost:23119/api/users/0/items`
- PDF-Pfad über `GET /api/users/0/items/<itemKey>/file` → folgt einem **302-Redirect auf eine `file://`-URL**. Pfad daraus extrahieren. Rate niemals Pfade im Zotero-Storage-Verzeichnis.
- API ist **read-only**, nur GET.
- Bei `403`: klare Fehlermeldung ausgeben, dass in Zotero *Settings → Advanced → „Allow other applications on this computer to communicate with Zotero"* aktiviert werden muss.
- Metadaten (Titel, Autoren, Jahr, DOI) kommen **immer aus Zotero**, niemals aus dem PDF-Text.
**`parse.py`**
```python
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions, EasyOcrOptions
from docling.datamodel.base_models import InputFormat
def build_converter(ocr: bool = False) -> DocumentConverter:
    opts = PdfPipelineOptions()
    opts.do_ocr = ocr
    opts.do_table_structure = True
    if ocr:
        opts.ocr_options = EasyOcrOptions(lang=["en", "de"])
    return DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )
```
Zwei Durchläufe: erst alles mit `ocr=False`. Dokumente, bei denen eine Seite unter `SCAN_CHAR_THRESH` Zeichen liefert, mit `is_scan=1` markieren und in einem zweiten Lauf mit `ocr=True` neu parsen.
Beim Iterieren über die Blöcke:
```python
for item, _level in doc.iterate_items():
    prov = item.prov[0]
    page = prov.page_no
    bb   = prov.bbox      # .l .t .r .b  und  .coord_origin
```
**`bbox.coord_origin` muss mit in die DB.** Docling liefert beim PDF-Backend `BOTTOMLEFT`; ohne dieses Feld ist die Koordinaten-Umrechnung im Frontend unmöglich.
Verwerfen: Referenzverzeichnis, Header, Footer, reine Seitenzahlen.
Behalten: Abstract, alle Fließtextsektionen, Tabellen als Markdown, Bildunterschriften.
Zusätzlich: kompletten Text mit `[S. N]`-Markern in `documents.full_text` schreiben.
**Abnahme:**
- Alle Dokumente aus Zotero sind in `documents` mit `file_path`, `full_text` und `content_hash`.
- Für mindestens ein Dokument ist per Stichprobe belegt, dass `bbox` und `coord_origin` gefüllt sind.
- Verifiziere an einem Dokument explizit, dass **OCR wirklich aus ist** (Laufzeit und Log prüfen). In Docling gibt es einen gemeldeten Fall, in dem `do_ocr=False` nicht greift.
### Schritt 2 — Export für die Sichtprüfung
**`scripts/export_review.py`**: schreibt pro Dokument eine Markdown-Datei nach `review/<zotero_key>.md` mit Sektionsüberschriften, Seitenmarkern und Tabellen.
Zusätzlich `review/_report.md` mit einer Tabelle: Dokument, Seitenzahl, Zeichen pro Seite, `is_scan`, Auffälligkeiten (leere Seiten, Seiten mit < 100 Zeichen, fehlende Sektionsstruktur).
Dann folgt ein **manueller Schritt des Nutzers** (Prüfung aller 70 Dokumente, `parse_ok` setzen). Baue dafür ein kleines CLI: `python -m scripts.export_review --mark-ok <zotero_key>`.
**Abnahme:** Report existiert, listet alle Dokumente, markiert Auffälligkeiten. `--mark-ok` setzt `parse_ok=1`.
**Ab hier gilt: indexiere ausschließlich Dokumente mit `parse_ok = 1`.**
### Schritt 3 — Chunking und Embedding
**`chunk.py`** – Regeln, keine Heuristik-Freiheit:
1. Zielgröße `CHUNK_TOKENS` (600), Überlappung `CHUNK_OVERLAP` (15 %).
2. **Niemals über Sektionsgrenzen hinweg.** Ein Chunk gehört zu genau einer Sektion.
3. Nur an Absatzgrenzen schneiden, nie mitten im Satz.
4. Tabellen bleiben ein Chunk, auch wenn größer als 600 Tokens.
5. Jeder Chunk erbt `section`, `page_start`, `page_end` und die Vereinigung der bboxes seiner Blöcke.
6. Kontextpräfix: `embed_text = f"Aus '{title}' ({year}), Abschnitt {section}: {text}"`
**`embed.py`**
```python
model = SentenceTransformer(
    EMBED_MODEL,
    model_kwargs={"device_map": "cuda"},     # fp8 aktivieren, siehe unten
    tokenizer_kwargs={"padding_side": "left"},
    truncate_dim=None,
)
# Dokumente: OHNE Instruction
model.encode(texts, batch_size=8, normalize_embeddings=True)
# Queries: MIT Instruction
model.encode([q], prompt_name="query", normalize_embeddings=True)
```
Vier Pflichtregeln:
1. **`normalize_embeddings=True` immer.** Ohne Normalisierung sind Cosine-Distanzen verzerrt.
2. **Asymmetrie einhalten:** Queries mit Instruction (`QUERY_INSTRUCTION`), Dokumente ohne. Verstoß erzeugt keinen Fehler, nur schlechtere Treffer.
3. **2560 Dimensionen, keine Truncation.**
4. **fp8 verifizieren:** Lade das Modell und prüfe die belegte VRAM-Menge. Erwartung ~4 GB, nicht ~8 GB. Die Flags unterscheiden sich je Toolchain (`transformers` `FinegrainedFP8Config`, vorquantisiertes FP8-Repo, oder vLLM). Wenn fp8 nicht erreichbar ist: **anhalten und melden**, nicht auf int8 oder fp16 ausweichen.
Schreibe `embed_model`, `embed_precision`, `embed_dim` in `index_meta`. Prüfe bei jedem Lauf, dass diese Werte zur Config passen – sonst abbrechen mit dem Hinweis, dass ein Neu-Indexieren nötig ist.
Ingest muss **nach jedem Dokument committen** (Wiederaufnahme nach Abbruch) und über `content_hash` unveränderte Dokumente überspringen.
**Abnahme:**
- `chunks`, `chunks_fts` und `chunks_vec` sind konsistent gefüllt (gleiche Anzahl).
- Ein Testlauf zeigt VRAM ≈ 4 GB für das Embedding-Modell.
- Ein zweiter Ingest-Lauf ohne Änderungen erzeugt keine neuen Chunks.
### Schritt 4 — Retrieval
**`retrieve.py`**
```python
def search(query: str, year_min: int | None = None, k: int = FINAL_K) -> list[Chunk]:
    qv     = embed_query(query)
    dense  = vec_search(qv, limit=CAND_PER_METHOD)      # exakt, brute force
    sparse = fts_search(query, limit=CAND_PER_METHOD)   # BM25
    fused  = rrf([dense, sparse], k=RRF_K)              # ALLE behalten
    return rerank(query, fused)[:k]
```
- **RRF**, nicht Score-Mittelung: `score(d) = Σ 1/(RRF_K + rank(d))`. BM25 ist unbegrenzt positiv, Cosine liegt in [−1,1]; deren Summe ist bedeutungslos.
- **Exakte Vektorsuche, kein ANN.** Bei ~5.000 Vektoren alle Distanzen rechnen. Keine Approximation, kein Recall-Verlust.
- **Alle fusionierten Kandidaten in den Reranker**, nicht vorher kürzen.
- Reranker über `CrossEncoder(RERANK_MODEL, max_length=RERANK_MAX_LEN)`, einmal global laden, nie pro Query.
- Optionaler Metadatenfilter `year_min` **vor** der Suche anwenden.
**Abnahme:** Ein Unit-Test mit einer Handvoll Chunks belegt, dass ein Dokument, das nur lexikalisch (exaktes Fachwort) passt, gefunden wird, und eines, das nur semantisch passt, ebenfalls. Beide landen nach RRF in den Kandidaten.
### Schritt 5 — Eval-Harness
**`eval/questions.yaml`**
```yaml
- question: "Welche Stichprobengröße hatte Studie X?"
  gold_chunk_ids: [142, 143]
  kind: fact
```
Verteilung: 10 `fact`, 8 `concept`, 8 `cross`, 4 `negative` (Themen, die **nicht** in der Bibliothek vorkommen).
**`scripts/run_eval.py`** berechnet und gibt aus:
```
recall_at_12  = Anteil Fragen mit mindestens einem Gold-Chunk in Top-12
mrr           = mean(1 / Rang des ersten Gold-Chunks)
abstain_rate  = Anteil der negative-Fragen ohne plausiblen Treffer
```
Ausgabe als Tabelle plus JSON nach `eval/results/<timestamp>.json`, damit Läufe vergleichbar sind.
**Schwellen zur Beurteilung:** `recall_at_12 < 0.70` → Retrieval ist nicht belastbar. `> 0.85` → gut. `abstain_rate < 0.75` → Prompting nachschärfen.
**Abnahme:** Harness läuft, schreibt JSON, Ergebnisse zweier Läufe sind diffbar.
### Schritt 6 — MCP-Server
**`retrieval_mcp/__main__.py`**
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("library")
@mcp.tool()
def search_library(query: str, year_min: int | None = None, k: int = 12) -> str:
    """Hybride Suche über die Literaturbibliothek (semantisch + lexikalisch).
    Gibt Auszüge mit Titel, Autor, Jahr, Seitenzahl und chunk_id zurück."""
@mcp.tool()
def find_relevant_documents(query: str, k: int = 5) -> str:
    """Wählt ganze relevante Dokumente aus. Gibt document_id, Titel, Jahr
    und eine kurze Begründung. Für Synthese- und Vergleichsfragen."""
@mcp.tool()
def read_full_document(document_id: int) -> str:
    """Vollständiger Text eines Papers inklusive [S. N]-Seitenmarkern."""
@mcp.tool()
def get_chunk_context(chunk_id: int, window: int = 1) -> str:
    """Angrenzende Chunks laden, wenn ein Auszug abgeschnitten wirkt."""
@mcp.tool()
def list_documents(query: str | None = None) -> str:
    """Bibliothek überblicken und prüfen, was indexiert ist."""
```
Regeln:
- **Jede Rückgabe enthält `chunk_id` und Seitenzahl.** Ohne diese kann nicht korrekt zitiert werden.
- Rückgaben als lesbarer, kompakter Text, nicht als rohes JSON.
- Kein Anthropic-API-Client im Code. Die Synthese macht Claude Code.
- `mcp>=1.0,<2.0` pinnen.
**`cite.py` – Zitatverifikation, Pflicht:**
```python
def verify_quote(quote: str, chunk_text: str) -> bool:
    """True, wenn quote nach Whitespace-Normalisierung Substring von
    chunk_text ist. Groß/Kleinschreibung ignorieren."""
```
Nicht verifizierte Zitate werden in der Ausgabe **explizit als unbestätigt markiert**, nicht stillschweigend durchgelassen.
**Abnahme:** `claude mcp add library -- python -m retrieval_mcp` registriert erfolgreich; alle fünf Werkzeuge antworten; `verify_quote` hat Tests für Treffer, Nicht-Treffer und abweichende Whitespaces.
### Schritt 7 — Query-Expansion
Führe im MCP-Server ein zusätzliches Werkzeug ein, das mehrere Queries entgegennimmt und fusioniert:
```python
@mcp.tool()
def search_library_multi(queries: list[str], k: int = 12) -> str:
    """Mehrere Query-Varianten suchen und per RRF fusionieren.
    Claude erzeugt die Varianten (Umformulierungen + hypothetische Antwort)."""
```
Die Varianten erzeugt **Claude Code**, nicht der Server. Dokumentiere in `CLAUDE.md`, dass Claude vor komplexen Suchen 3 Umformulierungen plus eine hypothetische Antwort (HyDE) bilden und alle fünf über dieses Werkzeug schicken soll.
**Abnahme:** Fünf Queries werden korrekt per RRF fusioniert; das Ergebnis ist nachweislich nicht identisch mit dem der Einzelquery.
### Schritt 8 — FastAPI und Reader
**`api/main.py`**
```
GET  /api/documents                → Liste
GET  /api/documents/{id}/file      → PDF-Bytes
POST /api/search  {query, filters} → library_core.search()
GET  /api/chunks/{id}              → Text + bbox
```
**Frontend:** React + Vite + `pdfjs-dist`. Highlights als absolut positionierte Overlays über dem Canvas.
**Koordinaten nicht selbst umrechnen:**
```js
const viewport = page.getViewport({ scale, rotation });
const [x, y] = viewport.convertToViewportPoint(bb.l, bb.t);
```
Das erledigt Y-Spiegelung (PDF-Ursprung unten links vs. Canvas oben links), Zoom und Rotation.
**Abnahme:** Ein Zitat aus der Suche führt per Klick zur richtigen Seite mit korrekt sitzendem Highlight, auch nach Zoomänderung.
---
## 5. Harte Regeln
Verstöße erzeugen meist **keinen Fehler**, sondern still schlechtere Ergebnisse. Deshalb explizit:
1. `normalize_embeddings=True` bei jedem Encode.
2. Query mit Instruction, Dokument ohne. Nie beides gleich.
3. Index und Query mit identischem Modell **und** identischer Präzision.
4. FTS5-Trigger existieren, sonst findet BM25 nichts.
5. `bbox.coord_origin` wird gespeichert.
6. Nur `parse_ok = 1` wird indexiert.
7. RRF statt Score-Addition.
8. Kein ANN, exakte Suche.
9. Reranker-Modell global laden, nie pro Query.
10. Kein Anthropic-API-Client. Kein Cloud-Embedding. Kein Cloud-Reranking.
11. VRAM nie über 8 GB. Bei OOM `batch_size` senken, nicht das Modell tauschen.
12. `mcp>=1.0,<2.0`.
---
## 6. Definition of Done
- `python -m scripts.ingest` läuft von leerer DB bis vollständigem Index durch, wiederaufnehmbar.
- `python -m scripts.run_eval` liefert `recall_at_12 ≥ 0.85` auf dem 30-Fragen-Set.
- `abstain_rate ≥ 0.75` auf den negative-Fragen.
- MCP-Server in Claude Code registriert, alle Werkzeuge funktionsfähig.
- Zitatverifikation aktiv, unbestätigte Zitate werden markiert.
- Reader zeigt Highlights an der korrekten Stelle.
- VRAM im Betrieb ≤ 6 GB.
---
## 7. Vorgehen
- Arbeite die Schritte 1–8 der Reihe nach ab. Erfülle die Abnahmekriterien, bevor du weitergehst.
- **Schritt 5 (Eval) vor Schritt 7 und 8.** Erst messen, dann optimieren.
- Schreibe Tests für: DB-Trigger, RRF, Zitatverifikation, Chunking-Grenzen.
- Bei Blockern anhalten und melden. Improvisiere nicht mit anderen Modellen oder Cloud-Diensten.
---
## 8. Inhalt für `CLAUDE.md`
Lege diese Datei im Projekt an, damit Claude Code das Tool später richtig nutzt:
```markdown
# Nutzung der Literaturbibliothek
## Werkzeugwahl
- Eng umgrenzte Faktenfrage → `search_library`
- Vergleich, Synthese, „wie verhält sich X zu Y" → `find_relevant_documents`,
  danach `read_full_document` für die 3–5 ausgewählten Papers.
  Die Bibliothek ist klein genug, um ganze Papers zu lesen. Nutze das.
- Auszug wirkt abgeschnitten → `get_chunk_context`
- Vor komplexen Suchen: 3 Umformulierungen plus eine hypothetische
  Antwort bilden und alle über `search_library_multi` schicken.
## Antwortregeln
Antworte ausschließlich auf Basis der bereitgestellten Auszüge.
- Belege jede inhaltliche Aussage mit wörtlichem Zitat plus [Autor Jahr, S. X].
- Zitiere wortgetreu. Erfinde keine Seitenzahlen.
- Wenn die Auszüge die Frage nicht beantworten, sage genau das.
  Rate nicht und ergänze nichts aus Allgemeinwissen.
- Widersprechen sich Quellen, benenne den Widerspruch statt ihn zu glätten.
```

---

*Hinweis (nachträglich, siehe docs/ABWEICHUNGEN.md): Umgesetzt mit dokumentierten,
gemeldeten Abweichungen – u. a. korrigierte Schreibweise `FineGrainedFP8Config`
(transformers-API), zusätzliches MCP-Werkzeug `verify_citations`, `accelerate`
als Dependency.*
