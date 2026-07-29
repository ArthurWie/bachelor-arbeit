# library-rag in der Bachelorarbeit: Analyse und Integrationsplan

Stand 27. Juli 2026. Analysiert: `C:\Users\arthu\Downloads\library-rag-windows\library-rag`
(~2.400 LOC Python + React). Grundlage der Analyse unten: statisches Codelesen.

---

## Umsetzungsstand (P0 gebaut, 27. Juli 2026)

Der Plan unten ist der Stand *vor* der Umsetzung und bleibt als Entscheidungsprotokoll
stehen. Was beim Bauen tatsächlich herauskam:

**Läuft, unter `rag/`:** Setup mit CUDA (RTX 4060), 62 Tests grün, alle 67 PDFs geparst
und indexiert, MCP-Server `library` registriert und verbunden. Nutzungsregeln im
Abschnitt „Library Tools" der `CLAUDE.md`; Offenlegung in `ai-usage-log.md` und der
List of Aids in `main.tex`. Alle Abweichungen in `rag/docs/ABWEICHUNGEN.md` Nr. 10–16.

**fp8 war erreichbar — Abschnitt 3.3 unten ist überholt.** Nicht die Hardware war das
Problem (Ada/sm89 kann fp8, `torch._scaled_mm` rechnet), sondern zwei fehlende Pakete:
transformers 5.14 holt den fp8-Matmul aus dem Kernel-Hub (`kernels==0.15.2`), und dieser
Kernel ist Triton-basiert (`triton-windows`). Verifiziert: 4,1 GB VRAM statt 8. WSL2 nicht
nötig, Präzision musste nicht freigegeben werden, das Modell bleibt wie spezifiziert.

**Die Seitenzahl-Lösung wurde zweimal korrigiert.** Erster Entwurf (Fußzeilen im
Item-Loop abfangen) griff nie: `iterate_items()` läuft nur über die BODY-Ebene, Kopf- und
Fußzeilen liegen in FURNITURE. Gelesen wird jetzt `doc.texts`. Bei Elsevier-PDFs
klassifiziert Docling die Fußzeilenzahl gar nicht als solche — dafür gibt es eine
Rückfallebene über den Scopus-Seitenbereich, aber nur wenn dessen Spanne exakt der
PDF-Seitenzahl entspricht und er nicht bei 1 beginnt. Ergebnis: **60 von 67 zitierfähig
mit Druckseite**, 7 melden ausdrücklich „PDF-Seite, nicht als Druckseite zitieren".

**Der Abgleich hat Scopus in allen drei Streitfällen widerlegt** (am PDF geprüft):
S18 trägt gedruckt 3334 wo Scopus 3333 rechnet (vorgebundenes Deckblatt), S43 beginnt
auf S. 44 statt 1, S61 auf S. 1954. Scopus' `pages` ist bei Emerald artikelrelativ und
fürs Zitieren unbrauchbar. Die Entscheidung „Fußzeile ist Primärquelle, Scopus nur
Prüfsumme" war damit richtig — die umgekehrte Reihenfolge hätte drei Papers falsch
paginiert.

**Zwei latente Fehler im Original gefunden, die erst der Volllauf auslöste.** Die
Scan-Erkennung zählte nur Body-Text und hielt vier Papers für Scans (S32 S.12: Body 0
Zeichen, PDF-Textebene 1.412) — ein OCR-Durchlauf hätte sauberen Verlagstext dieser vier
durch OCR-Text ersetzt, bei wortgetreuen Fußnoten ein Rückschritt. Und `easyocr` war nie
installiert (fehlte im `pyproject.toml`, Docling bündelt es nicht), was den OCR-Pfad
hart abbrechen ließ. Nach dem Fix: 0 Scan-Verdacht, kein OCR nötig, `easyocr` bewusst
nicht nachgezogen.

**Abschnitt 3.4 unten ist ebenfalls überholt — die Annahme war falsch.** Dort stand,
pdfplumber liefere den verlässlicheren Wortlaut. Gemessen ist das Gegenteil: Auf
zweispaltigen Verlags-PDFs linearisiert pdfplumber anders als Docling und setzt
Leerzeichen mitten in Wörter, sodass nur ~25 % echter 20-Wort-Zitate als Substring
wiederzufinden sind. Docling ist die bessere Textquelle. Statt einer manuellen
pdfplumber-Runde prüft `verify_citations` die Seite jetzt selbst über die Wortfolge,
Schwelle 0,60 — kalibriert an 40 echten und 60 erfundenen Zitaten (echte Median 1,00,
erfundene **maximal 0,18**; bei 0,60 werden 36/40 echte bestätigt und 0/60 erfundene).
Der Test fängt zusätzlich ein echtes Zitat mit falscher `chunk_id` ab.

**Die Seitenzuordnung ist belastbar.** Für 24 Chunks wurde die bestpassende Seite im
PDF gesucht: in keinem Fall lag sie anders als in der Datenbank (0 Abweichungen).

**Abnahme bestanden:** 62 Tests grün, Suche 12 s bei warmen Modellen (33 s beim ersten
Aufruf mit Modell-Laden), Zitatprüfung trennt echt/erfunden/falsch zugeordnet.

**Vor dem ersten Schreiben noch zu tun:** nichts Blockierendes. Wer will, prüft die
7 Papers ohne Druckseitenzahl (Liste im `rag/review/_report.md`, Spalte „Druckseiten")
und entscheidet je Fall, ob über Abschnitt oder Artikelnummer zitiert wird.

---

## P1 erledigt (28. Juli 2026): erster echter Einsatz

Gebaut an Abschnitt 2.1 der Arbeit („Competitive advantage and firm performance", die
Konstrukttrennung aus Feedback #1). Vier Zitate, alle zweistufig geprüft, Druckseiten
215/247/550 am PDF bestätigt, kompiliert. Neu dabei: `corpus/make_bib.py` erzeugt
BibTeX-Einträge aus dem eingefrorenen Scopus-Export (keine neue Abfrage, kein Scholar).

**Das Werkzeug taugt für die Aufgabe.** Die Suche nach „competitive advantage als
eigenes Konstrukt" fand auf Anhieb die Messmodell-Abschnitte: Chatterjees Items COA1–COA3
mit Wortlaut und Druckseite 215, Hossains SCA-Items nach Cao et al. (S. 247), Mehtas
Hypothesen H8/H9 (S. 550). Genau die Stellen, die man sonst durch 15 PDFs sucht.

**Zwei Befunde:**

1. **Getrennte Ligaturen** (siehe `rag/docs/ABWEICHUNGEN.md` Nr. 17): 16 Studien liefern
   „fi rm" statt „firm". Auffällig nur beim echten Zitieren. Gelöst durch Warnung plus
   leerzeichenfreien Zweitvergleich in `verify_quote`.
2. **Der erste Aufruf nach Sitzungsstart ist teuer, danach nicht mehr.** Die erste
   Suche über den MCP-Server lief in einen Timeout (30 Minuten Serverstille). Aufgeklärt:
   Es ist das erstmalige Laden der beiden Modelle im Serverprozess (Embedder 4,1 GB +
   Reranker) bei belegter GPU — auf Windows fällt PyTorch dann in geteilten
   Systemspeicher statt mit OOM abzubrechen, und alles wird um Größenordnungen langsamer.
   Belegt: `list_documents` (braucht kein Modell) antwortete sofort, und **nach** dem
   Ladevorgang liefen sowohl Einzel- als auch Mehrfachsuche normal, auch bei nur 784 MiB
   freiem VRAM. Die Funktion selbst ist in Ordnung (Direktaufruf: Einzelsuche 5,4 s,
   Mehrfachsuche 14 s bei 903 statt 371 Kandidaten).

   Praktisch: nach dem Start der Sitzung eine beliebige kleine Suche als Aufwärmrunde
   abschicken und den ersten Timeout einkalkulieren, oder vorher GPU-hungrige Programme
   schließen. Kein Codefehler, keine Änderung an der Werkzeugwahl nötig.

**Merken für den Alltag:** Codeänderungen an `rag/` greifen erst nach Neustart der
Claude-Code-Sitzung — der MCP-Server lädt das Modul beim Start. Sichtbar daran, dass
die Ligatur-Warnung in der Werkzeugausgabe fehlt.

## Konsistenz-Audit (28. Juli 2026)

Gesucht wurde nach doppelten Versionen für dieselbe Aufgabe. Drei Funde, zwei behoben:

1. **Zwei pdfplumber-Versionen.** System-Python 3.13.3 mit 0.11.9, `rag/.venv` 3.12.9 mit
   0.11.10 — beide lasen PDF-Seiten für die Zitatprüfung, und die Schwelle 0,60 ist gegen
   0.11.10 kalibriert. Behoben: Die `CLAUDE.md` schickt das PDF-Lesen jetzt an den
   venv-Interpreter. Ein Extraktionspfad für einen Zweck.
2. **`library_core/zotero.py` gelöscht.** Zwei Module, die beide die Dokumentquelle sein
   wollen, sind eine Falle. `tests/test_imports.py` hielt das toter Modul am Leben und
   prüft jetzt `corpus.py`.
3. **Zwei `CLAUDE.md` mit denselben Regeln.** `rag/CLAUDE.md` enthielt Werkzeugwahl und
   Zitatprüfung doppelt. Gekürzt auf die Antwortregeln, mit Verweis auf die verbindliche
   Fassung in der Arbeit.

**Offen, bewusst nicht angefasst:** Die Originalkopie liegt weiter in
`C:\Users\arthu\Downloads\library-rag-windows\library-rag` und weicht in 14 Dateien ab
(dort existiert `zotero.py` noch). Zwei Kopien derselben Codebasis sind die letzte
Doppelung — Empfehlung: den Download löschen, sobald du `rag/` als gesetzt ansiehst.
Löschen ist deine Entscheidung, nicht meine.

**Gut gelöst und nicht anzufassen:** Die Bindung Index ↔ Modell ↔ Präzision prüft
`db.check_index_meta()` bei jedem Lauf gegen `index_meta` und bricht bei Abweichung ab.
Das ist die einzige Versionsfrage im System, die nicht von Disziplin abhängt.

---

## 1. Was das Projekt ist

Ein lokales RAG-System über eine PDF-Bibliothek mit einem einzigen echten
Verkaufsargument: **prüfbare Zitierbarkeit**. Kein Chatbot, kein Anara-Klon im
Sinne von „schöne Oberfläche", sondern eine Suchmaschine, die Claude Code als
Werkzeug bekommt.

Die Architektur ist sauberer als bei den meisten Hobbyprojekten:

| Teil | LOC | Was |
|---|---|---|
| `library_core/` | ~1.000 | Einzige Implementierung der Suchlogik |
| `retrieval_mcp/` | 225 | 7 MCP-Werkzeuge für Claude Code, nur Formatierung |
| `api/` + `frontend/` | ~850 | FastAPI + React-Reader mit PDF-Highlights |
| `scripts/` | ~540 | ingest, export_review, run_eval, Windows-Setup |
| `tests/` | ~420 | 36 Tests, laufen ohne GPU |

Die Suchpipeline: Docling parst PDFs strukturbewusst (Sektionen, Tabellen,
bbox-Koordinaten) → Chunking an Absatzgrenzen, nie über Sektionsgrenzen →
Qwen3-Embedding-4B (fp8, 2560 Dim) → **hybride Suche**: exakte Vektorsuche +
BM25 parallel, Fusion per Reciprocal Rank Fusion, dann Cross-Encoder-Reranking
über alle Kandidaten. Das ist die richtige Reihenfolge und die richtige
Fusionsmethode (RRF statt Score-Addition — BM25 und Cosine haben
unvergleichbare Skalen). Kein ANN, exakte Suche, bei ~5.000 Vektoren korrekt.

Der ökonomische Trick: Es gibt **keinen Anthropic-API-Client im Code**. Der
Server wird von Claude Code aufgerufen, nicht umgekehrt. Damit ist die Synthese
vom Max-Abo gedeckt und die Gesamtkosten sind null.

Der Kern für uns ist `cite.py` (41 LOC): `verify_quote()` prüft
whitespace-normalisiert und case-insensitiv, ob ein angeblich wörtliches Zitat
tatsächlich im Quelltext vorkommt. Über das MCP-Werkzeug `verify_citations`
aufrufbar. Das ist die deterministische Halluzinationsschranke.

Qualität des Codes: hoch. Die harten Regeln der Spec sind im Code verankert und
scheitern laut statt still (`check_index_meta` bei jeder Query,
fp8-VRAM-Verifikation, Konsistenzprüfung chunks/chunks_vec/chunks_fts, OOM-Backoff
statt Modelltausch). Abweichungen von der Spec sind in `docs/ABWEICHUNGEN.md`
dokumentiert. Das ist Arbeit, die man nicht wegwerfen sollte.

---

## 2. Passt das zur Arbeit?

**Ja, aber schmaler als „Anara-Klon" suggeriert.** Der ehrliche Wertnachweis:

Was das Tool **nicht** löst: Die deskriptiven Fragen der Arbeit (Verteilungen,
Methoden, Länder, outcome_construct) sind bereits in `corpus/coding_table.csv`
und `corpus/FACT_SHEET.md` beantwortet. Dafür ist `grep` schneller als jede
Vektorsuche, und der Fact Sheet ist per Regel die einzige Zahlenquelle. RAG
bringt hier nichts.

Was es löst, und zwar teuer eingespart: **die Fußnoten-Konvention.** Jede
Zitation in dieser Arbeit braucht `\footnote{[Autor (Jahr), p.X] "wörtliche
Passage"}`. Über sechs Kapitel sind das mehrere Hundert Fußnoten. Der aktuelle
Weg ist: PDF mit pdfplumber aufmachen, Seite für Seite nach der Passage suchen,
Text herauskopieren. Bei 67 Papers × ~25 Seiten ≈ 1.700 Seiten ist das der
mechanisch aufwendigste Rest der Arbeit. Genau das automatisiert `search_library`
(Passage + Seite + chunk_id) plus `verify_citations` (Zitat wirklich vorhanden).

Zweiter echter Nutzen: das Synthese-Kapitel und die Theorie. Fragen wie „welche
Studien nennen absorptive capacity als Moderator?" oder „wer widerspricht Kemps
Situated-AI-Argument?" sind über 67 Volltexte nicht grep-bar (Flexion, Synonyme,
deutsche/englische Varianten). `find_relevant_documents` + `read_full_document`
adressiert genau die Vergleichsfragen, die im Discussion-Kapitel anfallen.

Timing ist gut: `sections/` ist bis auf `results.tex` (748 Wörter) und die
Appendix-Tabelle leer. Das Tool käme vor der Schreibphase, nicht mitten hinein.

---

## 3. Blocker und Anpassungen

### 3.1 Zotero ist nicht installiert (Blocker, aber klein)

Geprüft: kein `%APPDATA%\Zotero`, kein `%LOCALAPPDATA%\Zotero`, API auf Port
23119 antwortet nicht. Der komplette Ingest-Pfad hängt an Zotero.

**Zotero nicht installieren.** Die Metadaten liegen längst besser vor:
`corpus/coding_table.csv` hat für alle 67 Studien `authors`, `year`, `journal`,
`doi`, `pdf` — adjudiziert, gegen Scopus geprüft, eingefroren. Alle 67 PDFs sind
in `literature/` vorhanden und 67/67 korrekt gemappt (verifiziert).

Die Kopplung ist erfreulich lokal: `zotero.py` (176 LOC) plus **ein** Import in
`scripts/ingest.py`. Ersatz ist ein `library_core/corpus.py` von ~40 Zeilen, das
dieselbe `ZoteroDocument`-Form aus der CSV liefert. In `documents.zotero_key`
kommt die `study_id` (S01–S67) — Spalte bleibt, Semantik ändert sich, kein
Schema-Eingriff. Nebeneffekt: Die Bibliothek ist damit deckungsgleich mit dem
eingefrorenen Korpus, nicht mit „was gerade in Zotero liegt".

### 3.2 Seitenzahlen sind PDF-Seiten, nicht Druckseiten (der wichtigste Punkt)

Docling liefert `page_no` = physische PDF-Seite. Die Arbeit zitiert Druckseiten.
An drei echten Korpus-PDFs verifiziert:

| Paper | PDF-Seite 2 trägt gedruckt | Offset |
|---|---|---|
| Babina 2024 (JFE) | „2" | 0 |
| Chatterjee 2021 (IMM) | „206" | **+204** |
| Banna 2025 (IJEBR) | keine Druckseitenzahl (Emerald, DOI-paginiert) | — |

Eine Fußnote „p. 3" statt „p. 207" ist ein Zitierfehler, den der Betreuer sofort
findet. Verschärfend: `parse.py` wirft `page_header`/`page_footer` weg
(`_SKIP_LABELS`) — die gedruckte Seitenzahl steht genau dort.

Fix, ~20 Zeilen: Footer/Header-Text pro Seite nicht verwerfen, sondern als
`page_labels`-Map mitschreiben, und die Ausgabe des MCP-Servers gibt das Label
aus, wenn vorhanden, sonst die PDF-Seite mit ausdrücklicher Kennzeichnung. Bei
Emerald-Artikeln ohne Druckpaginierung bleibt PDF-Seite plus Abschnitt — das ist
dann auch die zitierfähige Angabe.

### 3.3 fp8 auf nativem Windows (offenes Risiko)

Der Code hält bewusst an, wenn fp8 nicht erreichbar ist (`_HALT_NO_FP8`), statt
auf fp16 auszuweichen. Ob `FineGrainedFP8Config` mit der Toolchain auf nativem
Windows durchläuft, kann ich ohne Ausführung nicht sagen — die RTX 4060 (Ada,
sm89) kann fp8 grundsätzlich, aber der transformers-Pfad braucht je nach Version
Triton-Kernels, die unter nativem Windows fehlen können. Konfidenz: ~50/50.

**Empfehlung, falls es scheitert: Präzision freigeben, nicht WSL2 aufsetzen.**
Begründung: Das RAG ist **kein Teil der SLR-Methode**. Korpus, Screening und
Coding sind eingefroren und dokumentiert; das Tool findet Passagen zum Zitieren.
Welches Embedding-Modell in welcher Präzision das tut, hat null methodische
Konsequenz — die einzige Regel, die zählt, ist Index/Query mit identischem
Modell, und die erzwingt `check_index_meta` automatisch. Der Korpus ist außerdem
komplett englisch, das mehrsprachige 4B-Modell also überspezifiziert. `bge-m3`
oder `Qwen3-Embedding-0.6B` in fp16 (~1,2 GB VRAM) würde für 67 Papers reichen.
Kosten des Wechsels: Neu-Indexieren, ~20 Minuten. Kosten von WSL2: ein Tag.

Nebenbei: Auf der GPU liegen bereits ~1,6 GB (Discord, EA, Browser). Das
Budget 5,2 GB + 1,6 GB = 6,8 GB von 8 GB ist knapp, aber der OOM-Backoff greift.

### 3.4 Docling-Text ≠ PDF-Glyphen (Integritätsrisiko)

`verify_quote` prüft gegen den **Docling-geparsten** Text. Wenn Docling
Ligaturen, Trennstriche oder Spaltenreihenfolge verstümmelt, bestätigt die
Prüfung ein Zitat, das im PDF so nicht steht. Das ist genau die Fehlerklasse, die
in einer Bachelorarbeit teuer wird.

Daraus die zentrale Arbeitsregel der Integration:

> **Das RAG findet die Stelle. pdfplumber liefert den Wortlaut der Fußnote.**

Also: `search_library` gibt Paper + Seite + Passage → pdfplumber liest genau
diese Seite → der Fußnotentext wird aus dem pdfplumber-Output kopiert. Das ist
ein zusätzlicher Schritt pro Fußnote, kostet Sekunden, und macht den teuren Teil
(Finden über 1.700 Seiten) trotzdem geschenkt. Nebenwirkung: Der bestehende
`pdfplumber`-Workflow aus `CLAUDE.md` bleibt unangetastet gültig.

### 3.5 Überlappung mit dem geplanten Cross-Check-Workflow

`CLAUDE.md` plant `corpus/gemini_verify_citations.py`: Gemini prüft blind
Zitat-wörtlich + Seitenzahl + Paraphrase-Treue. Das MCP-Werkzeug
`verify_citations` erledigt den ersten Teil **deterministisch** — was Arthurs
eigener Regel entspricht („Numbers → script, never an LLM"). Sinnvolle
Aufteilung, die den Plan sogar vereinfacht:

- Zitat wörtlich vorhanden → `verify_citations` (Substring, exakt, kein LLM)
- Seitenzahl korrekt → pdfplumber auf die genannte Seite (Skript, kein LLM)
- Paraphrase treu, kein Source-Echo → Gemini, weil nur das Urteilsvermögen braucht

Damit fällt ein zu bauendes Skript weg statt eines dazuzukommen.

---

## 4. Was mitkommt, was nicht

| Teil | Entscheidung | Warum |
|---|---|---|
| `library_core/` (chunk, embed, retrieve, cite, db, parse) | **übernehmen, unverändert** | Der eigentliche Wert. Getestet, regelkonform. |
| `library_core/zotero.py` | **ersetzen** durch `corpus.py` (~40 LOC) | Kein Zotero; CSV ist die bessere Quelle. |
| `parse.py` Header/Footer-Handling | **patchen** (~20 LOC) | Druckseitenzahlen, siehe 3.2. |
| `retrieval_mcp/` (7 Werkzeuge) | **übernehmen** | Das ist die Schnittstelle. |
| `scripts/ingest.py`, `export_review.py` | übernehmen, ~10 Zeilen anpassen | Zotero-Import raus. |
| Sichtprüfung aller 67 Papers (`--mark-ok`) | **reduzieren** | Nur `_report.md`-Auffälligkeiten prüfen, Rest en bloc freigeben. Arthur hat alle 67 Volltexte im Coding gelesen; die 3.4-Regel fängt Parse-Fehler an der Fußnote ab. ~45 min statt 2–4 h. |
| `eval/` + `run_eval.py` (30 Fragen) | **verkleinern, später** | 30 Fragen mit Gold-Chunks = halber Tag. Die Coding-Tabelle **ist** ein Gold-Fragenkatalog (z. B. „welche Studie nennt USD 11,3 Mio. als Wendepunkt?" → S26). 10–12 Fragen daraus generieren, wenn Zweifel an der Trefferqualität auftauchen. |
| `api/` + `frontend/` (Reader mit Highlights) | **weglassen** | 850 LOC + 2–3 Tage für etwas, das die Fußnotenarbeit nicht schneller macht. Claude Code + MCP reicht. Nachrüstbar, weil bbox und coord_origin ohnehin in der DB landen. |
| `docs/SPEC.md` als bindende Vorgabe | **entbinden** | Die Spec war eine Bauanweisung, kein Methodenteil. Siehe 3.3. |

---

## 5. Reihenfolge

**P0 — bis das Werkzeug nutzbar ist (realistisch ein halber bis ein Tag)**

1. Ordner nach `C:\Users\arthu\Desktop\College Bachelor Arbeit\rag\` kopieren.
   `MODEL_CACHE` und `DB_PATH` auf einen Pfad außerhalb des Arbeitsordners
   setzen (~15 GB torch + Modelle gehören nicht in die Abgabe-Struktur).
2. `scripts\setup_windows.ps1` laufen lassen. Erwartung: `CUDA verfuegbar: True`
   und `36 passed`. Ab hier ist zum ersten Mal etwas verifiziert.
   (Stand heute: `62 passed` — die Testsuite ist seit P0/P1 gewachsen.)
3. `library_core/corpus.py` schreiben (CSV → Dokumente), Import in `ingest.py`
   tauschen. Ein Test: 67 Dokumente, 67 existierende Pfade.
4. Header/Footer-Patch in `parse.py` (Druckseiten-Labels).
5. `ingest --parse-only`, dann `export_review`, Auffälligkeiten prüfen,
   en bloc freigeben, `ingest --index-only`.
6. MCP registrieren, `CLAUDE.md` der Arbeit um einen kurzen Abschnitt
   „Bibliotheks-Werkzeuge" ergänzen (Werkzeugwahl + die Regel aus 3.4).
   Nicht die ganze library-rag-`CLAUDE.md` kopieren.
7. **`ai-usage-log.md` + List-of-Aids-Tabelle in `main.tex` ergänzen.** Nicht
   optional: Das Tool wird beim Schreiben verwendet, also gehört es offengelegt —
   inklusive Modellnamen und Zweck („Auffinden zitierfähiger Passagen im
   eingefrorenen Korpus, lokal, keine Synthese").

**P1 — wenn P0 läuft**

8. Erste echte Nutzung an einem Abschnitt von `background.tex`, um die Regel aus
   3.4 im Alltag zu prüfen. Falls die Trefferquote enttäuscht: Mini-Eval (P2).

**P2 — nur bei Bedarf**

9. 10–12 Eval-Fragen aus der Coding-Tabelle generieren, `run_eval` laufen lassen.
10. Reader-Frontend. Ehrlich: wahrscheinlich nie.

---

## 6. Pro und Contra, kompakt

**Dafür**

- Trifft die teuerste verbleibende Aufgabe der Arbeit (Fußnoten mit wörtlicher
  Passage und Seitenzahl) mitten ins Zentrum.
- Deterministische Zitatprüfung statt „Claude verspricht, korrekt zu zitieren" —
  passt exakt zur Cross-Check-Philosophie, die schon in der Coding-Phase getragen hat.
- Korpus ist eingefroren und klein: 67 Papers ist genau die Größe, für die
  `read_full_document` (ganze Paper lesen statt Schnipsel) funktioniert.
- Die Anpassung ist überschaubar: eine Datei ersetzen, eine patchen.
- Läuft lokal, kostet nichts, keine Daten verlassen den Rechner.
- Der aufwendige Teil (hybride Suche, RRF, Reranking, DB-Konsistenz) ist fertig
  und getestet.

**Dagegen**

- fp8-Risiko auf nativem Windows, 50/50, mit klarem Ausweg (3.3), der aber eine
  bewusste Abweichung von der eigenen Spec bedeutet.
- Docling-Text ≠ PDF-Wortlaut: Die Zitatprüfung ist eine Schranke gegen
  *erfundene* Zitate, keine Garantie für *wortgetreue*. Erfordert Disziplin
  (Regel 3.4), sonst ist das Sicherheitsversprechen zu groß.
- Seitenzahl-Mapping muss stimmen, sonst produziert das Tool schnell und
  zuverlässig falsche Fußnoten. Vor dem ersten Einsatz an 3–4 Papers gegenprüfen.
- Zeit, die nicht ins Schreiben geht. Die Arbeit hat sechs praktisch leere
  Kapitel. Ein halber Tag Werkzeugbau ist vertretbar, zwei Tage nicht.
- Offenlegungspflicht: Das Tool muss in die List of Aids. Wer es dort nicht
  nennt, hat ein Problem, das größer ist als jeder Zeitgewinn.
- Wartung: Modelle, Docling, transformers — nichts davon ist stabil. Für die
  Dauer dieser Arbeit irrelevant, danach Datenmüll auf der Platte.

**Nicht mitbauen:** Reader-Frontend, 30-Fragen-Eval, vollständige Sichtprüfung
aller 67 Papers, Zotero-Installation. Zusammen sind das drei bis vier Tage für
Funktionen, die keine einzige Fußnote schneller machen.
