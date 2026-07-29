# Abweichungen von der Spec (docs/SPEC.md)

Die Spec verlangt: nicht abweichen, Blocker melden. Folgende Punkte wurden
während der Umsetzung gemeldet und bewusst abweichend gelöst. Alles andere
ist exakt wie spezifiziert.

## 1. `FineGrainedFP8Config` statt `FinegrainedFP8Config`
Die Spec (§4 Schritt 3) nennt `FinegrainedFP8Config`. Die transformers-Klasse
heißt tatsächlich `FineGrainedFP8Config` (großes G) – verifiziert gegen die
PyPI-Wheels 4.49/4.55/5.x; die Kleinschreibung existierte nie. Mit der
Spec-Schreibweise wäre jedes Embedding dauerhaft mit irreführender Meldung
gescheitert. Korrigiert in `library_core/embed.py`.

## 2. `accelerate` als zusätzliche Dependency
`device_map` beim Modell-Laden (von der Spec vorgegeben) setzt das Paket
`accelerate` voraus. Ohne es bricht das fp8-Laden ab. Ergänzt in
`pyproject.toml`.

## 3. Siebtes MCP-Werkzeug: `verify_citations`
Die Spec definiert `cite.verify_quote()` als Pflicht und fordert in der
Definition of Done „Zitatverifikation aktiv, unbestätigte Zitate werden
markiert" – listet aber nur sechs Werkzeuge. Ohne aufrufbaren Weg wäre die
Verifikation toter Code. Deshalb gibt es `verify_citations` als zusätzliches
MCP-Werkzeug; `CLAUDE.md` enthält dazu einen Zusatzabschnitt (Pflichtprüfung
vor jeder Antwort mit Zitaten). Rückbau: Werkzeug in
`retrieval_mcp/__main__.py` und Abschnitt in `CLAUDE.md` löschen.

## 4. Härtung von Harter Regel 3 (Query-Seite)
Die Spec verlangt die index_meta-Prüfung „bei jedem Lauf". Umgesetzt als
`db.check_index_meta()` (rein lesend, schreibt nie) an den Query-Einstiegen
`retrieve.search()`/`search_multi()` – zusätzlich zur Ingest-seitigen
`ensure_index_meta()`.

## 5. Zusätzliche `index_meta`-Schlüssel
Das Tabellenschema ist unverändert; der Key-Value-Store enthält zusätzlich:
- `blocks:<doc_id>` – geparste Blöcke, damit Indexieren ohne Neu-Parsen geht
  (und exakt das indexiert wird, was gesichtet wurde)
- `num_pages:<doc_id>` – echte Seitenzahl für den Sichtprüfungs-Report
- `ocr_pending:<doc_id>` – Wiederaufnahme-Marker zwischen Parse-Durchlauf 1
  und OCR-Durchlauf 2

## 6. `ABSTAIN_SCORE = 0.5` in config.py
Die Spec definiert „plausibler Treffer" für die abstain_rate nicht numerisch.
Festgelegt als Sigmoid über den Reranker-Logit ≥ 0.5.

## 7. Struktur-Ergänzungen
- `tests/` (von Spec §7 gefordert, fehlt im Strukturbaum von §1)
- `docs/` (SPEC.md, KONZEPT.md, diese Datei), `README.md`,
  `scripts/setup_windows.ps1` – auf Wunsch ergänzt
- Frontend: Deep-Link `?chunk=<id>` (für Verifikation nötig, praktisch als
  teilbarer Zitat-Link)

## 8. Robustheits-Fixes aus der adversarialen Review
Kein Spec-Widerspruch, aber über den Wortlaut hinaus:
- Tabelleninhalte zählen in die Scan-Erkennung (Docling-`TableItem` hat kein
  `.text`; sonst gälten Tabellenseiten als Scan)
- OOM-Backoff auch im Reranker-Pfad (Harte Regel 11 sinngemäß)
- API meldet Modell-/DB-Fehler als 503 mit Detail statt nacktem 500
- pdfjs: `destroy()`-Cleanup, CropBox-Offset, Seitenzahl-Reset

## 9. Gestaltung des Readers
Die Spec macht keine visuellen Vorgaben. Umgesetzt im Stil Anara × Adobe
Acrobat (Inter, weiße Flächen, Spectrum-Blau als Akzent, graue
Dokument-Wanne, schwebende Seitensteuerung).

## 10. Korpus statt Zotero (Integration in die Bachelorarbeit)
Ab dem Einbau in die Arbeit (27. Juli 2026) ist Zotero nicht mehr die Quelle –
es ist auf dem Zielrechner nicht installiert und wäre hier die schlechtere
Quelle. `library_core/corpus.py` liest stattdessen den eingefrorenen SLR-Korpus:
`corpus/coding_table.csv` (67 Studien, study_id, DOI, PDF-Name) plus den
Scopus-Export `corpus/corpus_2026-07-17.csv` (Titel, Autoren, Seitenbereich).
`documents.zotero_key` trägt jetzt die `study_id` (S01–S67); das Schema ist
unverändert. `library_core/zotero.py` wurde **gelöscht** (28.07.2026): Zwei Module,
die beide die Dokumentquelle sein wollen, sind eine Falle – nur `corpus.py` ist es.
Der Spaltenname `zotero_key` bleibt, um das Schema nicht anzufassen. Die Spec-Regel „Metadaten immer aus der Referenzverwaltung, nie aus
dem PDF-Text“ gilt unverändert, nur mit der besseren Quelle.

## 11. Gedruckte Seitenzahlen (neu, nicht in der Spec)
Die Spec kennt nur `page_start`/`page_end` = Docling-Seiten, also PDF-Seiten.
Für Fußnoten der Arbeit ist das falsch: Chatterjee 2021 (IMM) hat auf PDF-Seite 2
die gedruckte Seite 206 (Offset 204). Neu:
- `parse.py` sammelt gedruckte Seitenzahlen aus Kopf-/Fußzeilen
  (`_collect_page_labels`) und `page_offset()` bildet den modalen Offset.
- **Befund, der eine naive Umsetzung scheitern lässt:** `doc.iterate_items()`
  läuft nur über die BODY-Ebene. Kopf-/Fußzeilen liegen in der FURNITURE-Ebene
  und tauchen dort nie auf – geprüft an Chatterjee 2021: 15 `page_header` +
  17 `page_footer` in `doc.texts`, null davon in `iterate_items()`. Gelesen wird
  deshalb direkt `doc.texts`. Das `page_header`/`page_footer` in `_SKIP_LABELS`
  war entsprechend immer toter Code.
- Der Offset landet als `page_offset:<doc_id>` in `index_meta` (Schema
  unverändert), `SearchResult` trägt `printed_start`/`printed_end`.
- Nur die Fußzeile ist Primärquelle. Der Scopus-Seitenbereich dient als
  Prüfsumme und wird beim Ingest gemeldet, nicht angewandt: Bei S18 (29 PDF-
  Seiten, Scopus 3333–3360) ergibt die Fußzeile 3331, die Scopus-Arithmetik
  3332 – vorgebundenes Deckblatt. Die Fußzeile hat recht.
- Wo keine gedruckte Seitenzahl erkennbar ist (Emerald-PDFs tragen einen
  Download-Vermerk statt Seitenzahl), sagt die MCP-Ausgabe ausdrücklich
  „PDF-S. N (nicht als Druckseite zitieren)“ statt eine Zahl zu erfinden.

## 12. fp8 auf nativem Windows: erreichbar, aber mit zwei Paketen
Die Spec verlangt bei fehlendem fp8 „anhalten und melden“. Angehalten hat es –
mit `ImportError` im ersten Forward-Pass, nicht beim Laden. Ursache: transformers
5.14 holt den fp8-Matmul aus dem Kernel-Hub (`kernels`), und dieser Kernel ist
Triton-basiert. Kein Ausweichen auf fp16/int8 nötig, es fehlten nur:
`kernels==0.15.2` und `triton-windows` (liefert `import triton` unter Windows).
Danach verifiziert: **4,1 GB VRAM**, 2560 Dimensionen, normalisiert. In
`pyproject.toml` ergänzt. WSL2 ist nicht erforderlich.

## 13. Scan-Erkennung zählt die ganze Seite, nicht den Body-Anteil
Die Spec setzt „eine Seite unter `SCAN_CHAR_THRESH` Zeichen ⇒ Scan-Verdacht“.
Umgesetzt war das über `iterate_items()`, also nur über die BODY-Ebene. Der erste
Volllauf über den Korpus hat vier Fehlalarme erzeugt (S20, S27, S32, S47) –
jeweils ausgelöst von einer Abbildungs- oder Tabellenseite, auf der der Body fast
nichts liefert. Belegt mit der PDF-Textebene als Grundwahrheit:

| | Body (`iterate_items`) | ganze Seite (`doc.texts`) | PDF-Textebene |
|---|---|---|---|
| S20 S.14 | 65 | 113 | 149 |
| S27 S.12 | 22 | 101 | 136 |
| S32 S.12 | 0 | 1.241 | 1.412 |
| S47 S.7 | 55 | 426 | 488 |

Alles born-digital, kein einziger Scan. Die Zeichenstatistik läuft deshalb jetzt
über `doc.texts` (beide Content-Layer) plus Tabelleninhalt; über der Schwelle
liegen damit alle vier. **Das war nicht kosmetisch:** ein OCR-Durchlauf hätte
sauberen Verlagstext dieser vier Papers durch OCR-Text ersetzt – bei wortgetreuen
Fußnoten ein Rückschritt. Nach dem Fix: 67/67 geparst, 0 Scan-Verdacht.

## 14. EasyOCR ist nicht installiert
Die Spec nennt EasyOCR als OCR-Engine, aber `easyocr` fehlte im `pyproject.toml`
und Docling bündelt es nicht – der OCR-Durchlauf brach deshalb mit
`ModuleNotFoundError: No module named 'easyocr'` ab (latenter Fehler, der vorher
nie auslösen konnte). Bewusst **nicht** nachinstalliert: Nach Nr. 13 gibt es im
eingefrorenen Korpus keinen einzigen Scan, und ~100 MB OCR-Stack für einen Fall,
der bei 67 Verlags-PDFs nicht vorkommt, wäre toter Ballast. Docling meldet den
Fehlfall selbst verständlich („Please install it via `pip install easyocr`“).
Sollte je ein Scan dazukommen: `uv pip install --python .venv\Scripts\python.exe easyocr`.

## 15. `pdfplumber` als Dependency
Neu, weil die Arbeitsregel lautet: Das RAG findet die Stelle, den Wortlaut der
Fußnote liefert die PDF-Seite selbst (Docling-Text kann bei Ligaturen, Trennung
und Spaltenreihenfolge abweichen). Damit die Prüfung aus derselben Umgebung
läuft, liegt `pdfplumber` jetzt im venv.

## 16. Zitatprüfung zweistufig, gegen die echte PDF-Seite
Die Spec verlangt nur `verify_quote()` gegen den Chunk. Der Abnahmetest zeigte, dass
das die halbe Prüfung ist: Ein Zitat kann korrekt im Chunk stehen und trotzdem der
falschen Seite oder dem falschen Chunk zugeordnet sein. `verify_citations` prüft
deshalb zusätzlich, ob die Wörter des Zitats **in derselben Reihenfolge auf der
genannten PDF-Seite** stehen (`cite.page_sequence_match`).

Warum keine Substring-Prüfung auf der Seite: gemessen an 40 echten Zitaten aus dem
Korpus treffen nur ~25 %. Ursache ist nicht der Docling-Text, sondern pdfplumber —
zweispaltige Verlags-PDFs werden anders linearisiert, und Blocksatz/Kerning setzt
Leerzeichen mitten in Wörter (`critically`, `organizations,` fehlen dort als Token).
**Docling ist hier die bessere Quelle, nicht die schlechtere** – die ursprüngliche
Arbeitsannahme („Wortlaut aus pdfplumber kopieren“) war damit falsch und wurde in der
`CLAUDE.md` der Arbeit korrigiert.

Kalibrierung (`x_tolerance=1`, 40 echte vs. 60 erfundene Zitate gegen dieselben Seiten):

| | Median | Extremwert |
|---|---|---|
| echte Zitate | 1.00 | Minimum 0.35 |
| erfundene Zitate | 0.08 | **Maximum 0.18** |

Schwelle `PAGE_MATCH_MIN = 0.60`: 36/40 echte bestätigt, 0/60 erfundene. Höhere
Schwellen kosten nur echte Treffer (0.90: 31/40) und verhindern keinen zusätzlichen
Fehlalarm.

Nebenbefund, der Vertrauen schafft: Eine Stichprobe von 24 Chunks hat für jeden die
bestpassende Seite im PDF gesucht. In **keinem** Fall lag sie anders als in der DB
(13 mit Score 1.00, 11 unterhalb der Aussagekraft, 0 Abweichungen). Die
Seitenzuordnung des Parsers ist also belastbar; die niedrigen Scores sind
Extraktionsqualität, keine falschen Seitenzahlen.

## 17. Getrennte Ligaturen werden gemeldet, nicht repariert
Beim ersten echten Einsatz (Abschnitt 2.1 der Arbeit) fiel auf: Manche Verlags-PDFs
geben fi/fl/ff als eigenen Textabschnitt mit Leerzeichen aus – „fi rm“, „signi fi cant“,
„in fl uence“. Betroffen sind 16 der 67 Studien mit 1.307 Vorkommen, geballt in drei
Papers (S17: 721, S38: 322, S34: 246). So darf kein Wortlaut in eine Fußnote.

Automatisch zusammenziehen lässt sich das nicht sicher: „signi fi cant“ muss nach vorn
und hinten verbunden werden, „the fi rm“ nur nach hinten – ohne Wörterbuch ist „signi“
nicht von „the“ zu unterscheiden, und eine Vorwärtsregel allein macht aus „the fi rm“
entweder „thefirm“ oder lässt „signi ficant“ stehen. Zwei Tests halten das fest.
Deshalb:
- `cite.has_split_ligatures()` erkennt den Fall, und die MCP-Ausgabe hängt einen
  Hinweis an den Auszug („Wortlaut von der PDF-Seite nehmen“).
- `verify_quote()` versucht nach dem normalisierten Substring-Vergleich einen zweiten
  ohne jedes Leerzeichen. Damit verifiziert die KORREKTE Schreibweise („significant“)
  gegen den kaputten Chunk („signi fi cant“). Aufgegeben wird nur die Wortgrenze.

Praktisch bestätigt an Mehta et al. (S38): Alle drei Zitate mit korrigierten Ligaturen
sind Stufe 1 bestätigt und erreichen auf der PDF-Seite 100 % Wortfolge. Die richtige
Schreibweise steht also auf der gedruckten Seite; das Trennen ist ein Artefakt der
Extraktion.

## 18. Frontend nicht installiert
Der Reader (`api/` + `frontend/`) ist nicht Teil des Integrationsumfangs;
`scripts/setup_windows.ps1` überspringt `npm install`. `bbox` und
`coord_origin` werden weiter gespeichert, das Nachrüsten bleibt möglich
(`cd frontend; npm install; npm run dev`).
