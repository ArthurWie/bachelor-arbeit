# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this thesis.

## Project Overview

Bachelor's thesis by Arthur Wienerroither (Student ID: h12322363). Written in **LaTeX**.

- **Topic:** Instructor's Topic 3 — *AI Investments and Firm Competitive Advantage* (anchor: Kemp, 2024, AMR).
- **Official title (set by supervisor, 14 July 2026, confirmed by Arthur 16 July):** *Organizational Conditions for AI-Driven Firm Performance: A Systematic Review of Empirical Evidence, 2015–2026*. Fredrich renamed it to avoid identical titles among his supervisees; thesis is formally registered under this title. The RQ below is unchanged.
- **Research question:** *Under what conditions do firm-level AI investments translate into competitive advantage and superior firm performance? — A systematic review of empirical evidence (2015–2026).*
- **Supervisor:** PD Dr. Viktor Fredrich (signs emails "vf"). Research profile (Scopus, checked 2 July 2026): coopetition, alliances, business model innovation; heavy user of configurational methods (fsQCA) — outcomes as *combinations of conditions*. NO AI publications — do not force a Fredrich citation. Do lean into "conditions/configurations" language; it matches his methodological school and the thesis RQ.
- **Institute:** Institute for International Business (IIB), WU Wien. Style model: JIBS/SMJ intros, JIBS style guide.
- **Method (mandated):** Systematic literature review, 50–500 empirical studies, Scopus (WU license), max transparency/reproducibility, core deliverable = state-of-the-art coding table.
- **Proposal deadline:** Mon 13 July 2026. Spec: 3–4 pages text + 1 page references, only the 10 most relevant top-ranked sources (AJG 4*/4 or VHB A+/A).
- **Proposal file:** `proposal.tex` — red `\src{...}` markers are slots for sources Arthur pulls from Scopus.
- **Instructor materials:** `C:\Users\arthu\Downloads\AW_ Anfrage Bachelorarbeit - Arthur Wienerroither\` (Kemp 2024; Raisch & Krakowski 2021 — NOTE: filename says SMJ but it is actually AMR 46(1), 192–210; plus SLR guideline papers: Rojon 2021, Harari 2020, Rousseau 2008). Verbatim excerpts of Fredrich's requirement emails (incl. the 50–500 corridor — it refers to the *query yield*, see reading note) are preserved in `instructor_emails.md`.

## Supervisor Feedback on Proposal (14 July 2026) — binding for the thesis

Overall verdict: very good proposal; search query, benchmark-study validation, and coding matrix explicitly praised — "unbedingt wie angekündigt umsetzen". Concrete requirements:

1. **Separate constructs:** *competitive advantage* and *superior firm performance* must be analytically distinct throughout (theory, coding table, results). Performance gains ≠ sustained competitive advantage.
2. **Ranking threshold:** AJG 4*/4 (VHB A+/A) was proposal-only. For the thesis, a strict threshold risks too small a corpus — use a broader, transparent inclusion rule; exceptions must be transparent and non-selective, never ad hoc.
3. **Results chapter:** split descriptive mapping of the literature clearly from the analytical synthesis of mechanisms.
4. **Theory chapter:** GPT (general-purpose technologies), RBV, Situated AI, Automation/Augmentation — keep condensed; theory serves to interpret the empirical evidence, not as a survey.
5. **Corpus presentation (425 hits = upper end of range):** full SLR table goes in the appendix; main text cites the most important individual studies in theory, method, and discussion. Aggregate the corpus with varied visualizations (pie/bar charts, geographic distribution of authors by country, etc.), modeled on highly cited SLRs.

## Literature Tooling: Scopus Is the System of Record

Scopus (WU license, www.scopus.com) is the sole instrument for everything that enters the thesis:
- **Corpus identification:** the documented Scopus query (run date stated) + CSV/RIS export IS the SLR method. The export skeleton feeds the state-of-the-art table.
- **Citation metadata:** export BibTeX from Scopus, not Google Scholar (Scholar's BibTeX lacks DOIs, abbreviates journal names, mangles capitalization).
- **Snowballing:** forward/backward via Scopus "cited by".
- Google Scholar is a scratchpad only ("does this paper exist?") — nothing from it enters `bib.bib` or the corpus directly.
- Known Scopus limits (acceptable here): no grey literature/preprints (excluded by the instructor anyway), indexing lag for articles-in-press, full texts still fetched via WU library.

### Scopus API access (works — set up 2 July 2026)

Claude can query Scopus directly. API key is in `.scopus_api_key` (do not commit if this ever becomes a git repo). Requires the WU VPN to be connected (entitlement is IP-based). Pattern:

```bash
KEY=$(cat .scopus_api_key)
curl -s --get "https://api.elsevier.com/content/search/scopus" \
  -H "X-ELS-APIKey: $KEY" -H "Accept: application/json" \
  --data-urlencode 'query=<SCOPUS QUERY>' --data-urlencode 'count=25'
```

**Validated pilot query (2 July 2026, 484 hits, retrieves all 3 benchmark studies — Babina 2024, Lui 2022, Krakowski 2023):**

```
TITLE(("artificial intelligence" OR "machine learning" OR "deep learning" OR "AI"))
AND TITLE-ABS-KEY((invest* OR adopt* OR implement*) AND ("competitive advantage"
OR "firm performance" OR "financial performance" OR "firm productivity" OR
"firm value" OR "market value" OR "firm growth")) AND SUBJAREA(BUSI OR ECON OR DECI)
AND PUBYEAR > 2014 AND PUBYEAR < 2027 AND DOCTYPE(ar) AND LANGUAGE(english) AND SRCTYPE(j)
```

Calibration lessons: outcome vocabulary must include "firm value"/"firm growth" (Lui, Babina use these, not "firm performance"); SUBJAREA needs DECI because Annals of Operations Research is not BUSI/ECON. When the corpus is pulled for real, page through results with `start=` (25/page) and record the run date.

**CORPUS PULLED — FROZEN (17 July 2026):** the query below was executed in full via `corpus/pull_corpus.py`. Result: **432 records** (425 on 6 July + 7 from indexing lag; still inside the 50–500 corridor). Frozen export: `corpus/corpus_2026-07-17.csv` (COMPLETE view: abstracts, all authors, keywords) + raw JSON in `corpus/raw/2026-07-17/`. Verified: all 3 benchmark studies retrieved, 432 unique EIDs, 432 abstracts, 425 DOIs. **This CSV is the corpus** — do not re-run the query; a re-run would yield different counts and invalidate the documented method. The thesis reports run date 17 July 2026 and n = 432.

**INCLUSION RULE — FROZEN (17 July 2026, Arthur's decision per supervisor feedback #2):** journal quality filter = **listed in AJG 2024 with rating ≥ 2** (single fixed ranking edition applied uniformly to all records regardless of publication year — standard SLR practice; note as one-line limitation in method). Result: 432 → **174 studies enter title/abstract screening** (excluded: 109 AJG 1, 149 not in AJG — mostly MDPI/OA megajournals). All 3 benchmarks survive (Babina 4*, Krakowski 4*, Lui 3). Ratings matched via ISSN in `corpus/enrich_ratings.py` (283/283 ISSN matches, 0 title fallbacks); AJG list from unofficial mirror `corpus/ratings/ajg2024.xlsx`, verified against 5 known ratings + journal count (1,823 ≈ official 1,822) — for citation in the thesis, register free at charteredabs.org and cite the official AJG 2024. Screening file: `corpus/screening_2026-07-17.csv` (columns `screen_decision`/`screen_reason`/`screen_notes` to fill). PRISMA chain so far: 432 identified → 174 after journal-quality filter.

**SCREENING CRITERIA — FROZEN (17 July 2026, approved by Arthur):** a study stays in if it is (1) empirical, (2) firm-level, (3) has firms' AI investment/adoption as its object, (4) measures a performance/competitive outcome. Exclusion codes, assigned in fixed order (first match wins, for unambiguous PRISMA counts): **E1** not empirical (conceptual, review, simulation without firm data) · **E2** not firm-level (individual/team/country; manager studies stay IF the outcome is at firm level) · **E3** AI is the study's analysis tool, not the firms' investment object (adoption/implementation DOES count as investment — deliberate query scope) · **E4** no performance/competitive-advantage outcome (adoption intention, satisfaction etc.; innovation outcomes stay if performance-near, borderline cases flagged) · **E5** wrong publication type. Case studies count as empirical. Title/abstract rule: when in doubt, include (full-text screening decides). Decisions live in `corpus/screening_2026-07-17.csv`; Claude pre-screens with proposed decisions, Arthur confirms in blocks.

**TITLE/ABSTRACT SCREENING CONFIRMED by Arthur (17 July 2026):** 174 screened → 81 include, 93 exclude (E1: 20, E2: 7, E3: 39, E4: 27, E5: 0). All 3 benchmarks included. Record 120 (Xiao/Bai pre-registered report) excluded as protocol duplicate of record 127 (executed study, included).

**FULL-TEXT SCREENING COMPLETE — FINAL CORPUS n = 67 (18 July 2026):** PRISMA chain: **432 identified → 174 (AJG ≥ 2) → 81 (title/abstract) → 67 final** (full-text stage removed 14: 12 content-based — Baffour E2, Jabbouri E2, Mehmood E3, Shore/Rennings/Nayal/D'Amico A./Vaillant/Steinhauser/Wu L./Zhao/Liu S. E4 — plus 2 not retrievable (NR): He X. 2024 (World Scientific) and Platania 2025 (IEEE), no WU license/OA, Arthur's decision 18 July). All 3 benchmarks in. All 67 full texts in `literature/`, schema-named. Borderline flags: all resolved. Includes by year: 2020:1, 2021:2, 2022:7, 2023:6, 2024:7, 2025:21, 2026:23. Caveat: the 55 never-flagged includes passed abstract screening only — their full-text eligibility check folds into the coding phase (each paper is read anyway); any coding-stage exclusion must be documented in the screening CSV. NOTE: Vaillant 2025 (excluded E4) builds directly on Kemp (2024) Situated AI — use as discussion-chapter source. **CODING TABLE SET UP (18 July 2026):** `corpus/coding_table.csv` — 67 rows (S01–S67, sorted year/author), bibliographic columns auto-filled + PDF links resolved 67/67; 14 coding columns per `corpus/CODING_SCHEME.md` (frozen; matches the proposal's announced fields + feedback #1: `outcome_construct` = performance | competitive_advantage | both, with separate `performance_measure`/`ca_measure`). Regenerate safely with `corpus/make_coding_table.py` (preserves coded values, merge on eid).

**CODING DRAFTS COMPLETE — ALL 67 (18 July 2026, Claude = coder 1):** every row coded as `draft`. Distribution: outcome_construct 53 performance / 8 both / 6 competitive_advantage; effect_direction 47 conditional / 14 positive / 3 negative / 3 mixed; 24 rows carry explicit VERIFY flags (unresolved detail like n or country — resolve during adjudication). **Verification workflow (agreed with Arthur due to time constraints): dual independent AI coding.** Coder 2 = Gemini CLI, blind run via `corpus/gemini_blind_coding.py` (gets only coding scheme + PDF text, never Claude's drafts; JSONs land in `corpus/gemini_coding/`; resume-safe, re-run to retry failures). Then compare coders on method/ai_measure/outcome_construct/effect_direction/conditions, Arthur adjudicates ALL disagreements + random sample of agreements + resolves VERIFY flags, sets `coding_status=final`. **ADJUDICATION CASE LAW — binding decision rules developed over 18 adjudicated cases (18 July 2026). Apply to ALL remaining coding decisions:**

1. **outcome_construct:** `competitive_advantage` ONLY if a distinct CA construct is measured — own scale + hypothesis + validation (S03 Chatterjee 2021: COA1-3, H4) — or, in qualitative work, genuine competitor-comparative evidence (S11 Ali Mohamad: patient choice over competitors, bargaining power, differentiation). CA as framing/rhetoric/theory-section RBV talk = `performance` (S01 Wamba, S04 Chatterjee 2022, S18 Cannas, S36 Huang). "Competitiveness" as KPI word in a list ≠ CA (S01 p.10). Relative-performance-vs-competitors scales are CA boundary cases — code CA but flag in ca_measure (S05 Hossain SCA). Perceived value from co-creation ≠ performance (S10 Sun: "economic value" is a mediator, Yim et al. items). Expert-rated competitiveness dimensions in inherently competitive settings (tendering) can count as CA (S19 Pesqueira).
2. **effect_direction:** clear average main effect → use its sign; moderators/dampeners go to conditions (S04: TT/LS moderate side paths; S41 Shi: direct effect 0.048*** + subgroup nulls = positive with boundary conditions). `conditional` when the effect exists ONLY via mechanism or under conditions: full mediation with n.s. direct path (S07 Leoni: AI→MFP 0.006 n.s.; S21 Sullivan: no direct paths modeled + 10/18 conditional effects; S28 Bin-Nashwan: no direct path modeled + one channel null), threshold/U-shape sign flip (S26 Banna: turning point USD 11.3M), or null baseline (S54 Kazakis). `mixed` = component split across outcomes/indicators (S31 Chiu: sustainability+market ✓ profit ✗; S36 Huang: financial+market ✓ productivity n.s.; S48 Arshad expected: revenue ✓ cost ✗). **For every mediation study: check the direct path in the full text before deciding.**
3. **method:** category = the strategy that generates the AI→outcome evidence. Interviews/Delphi only for problem verification/instrument development → not mixed (S05 Hossain, S37 Kumar → survey-SEM). Mixed ONLY when multiple strands carry outcome evidence (S19 Pesqueira: case comparison + evidential Delphi ratings). Two quantitative methods on same data ≠ mixed (S16 Wu: SEM primary + supplementary fsQCA → survey-SEM).
4. **conditions:** only identified moderators/mediators/complements/thresholds — NOT mechanisms-as-narrative, robustness checks, or alternative measures (S09 Mishra and S12 Czarnitzki emptied → "unconditional evidence" contrast group). Implementation barriers count as conditions (S18). Always record quantified thresholds (S26: USD 11.3M).
5. **Process per disputed row:** cover-to-cover full-text read; present BOTH coders' positions with verbatim page-cited quotes; check author affiliation ≠ sample country (S28: authors Oman/Malaysia, sample China; S36: authors Taiwan, sample S&P 500).

**ADJUDICATION STATUS (18 July 2026): 18/29 disagreements adjudicated by Arthur** (roughly balanced scorecard: ~10 Claude, ~9 Gemini — dual design pays). Finalized: S01,S03,S04,S05,S07,S09,S10,S11,S12,S16,S18,S19,S21,S26,S28,S31,S36,S37,S41. **BATCH RUN COMPLETE (18 July 2026, late):** all 11 remaining disputes decided as PROPOSED (briefs with quotes in `corpus/adjudication_briefs.md`); all 10 SAMPLE rows spot-checked (no joint coder errors; S43 flagged borderline positive-vs-conditional); all 15 VERIFY fact-gaps resolved (notable corrections: S13 = 109 announcements S&P 500 USA; S28 sample = China; S29 = US retail managers; S36 = S&P 500). **ONLY OPEN: (a) Arthur's single batch-review session over adjudication_briefs.md, (b) S56 Li/JBR re-download (`doi.org/10.1016/j.jbusres.2026.115974` — PDF lost to early dedupe bug, Gemini coded wrong file, its S56 coding invalid), then re-verify + single-study Gemini re-run.** **CODING COMPLETE — ALL 67 ROWS FINAL (18 July 2026, Arthur batch approval: all PROPOSED accepted, S43 stays positive).** Final distributions: outcome_construct 52 performance / 9 both / 6 competitive_advantage; effect_direction 38 positive / 20 conditional / 5 mixed / 4 negative; 63/67 rows carry identified conditions; methods: 27 panel econometrics, 24 survey-SEM, 6 mixed, 4 event study, 3 case study, 1 fsQCA, 1 DEA, 1 verbatim. Adjudication totals: 29 disputes (18 individual + 10 batch + 1 resolved via S56 re-run), 10 sample spot-checks (no joint errors), 15 fact-gaps closed. DATA COLLECTION PHASE OF THE THESIS IS COMPLETE. Next: descriptive charts from coding table (year/country/method/outcome distributions, per supervisor feedback #5), results chapter part 1 (descriptive mapping), then part 2 (synthesis of conditions). **WORKFLOW CHANGE (Arthur, 18 July): no more per-case approvals — Claude processes ALL remaining cases autonomously (full reads, case law above), writes evidence briefs to `corpus/adjudication_briefs.md`, applies PROPOSED values to coding_table (coding_status stays `draft`), marks adjudication_list resolutions as "PROPOSED: ...". Arthur then reviews everything in ONE final batch session; only after his batch approval do rows flip to `final`.**

**DUAL CODING COMPLETE (18 July 2026):** Gemini blind run finished 67/67 (gemini-2.5-pro; two Windows fixes: full .cmd path + prompt via stdin). Initial agreement: method 90%, outcome_construct 88%, effect_direction 51%. Root cause of low direction agreement = coder-1 inconsistency (early blocks over-used `conditional` for mediated-positive effects). Documented self-consistency pass applied (26 rows → positive, 2 → mixed; direction now 40 positive / 19 conditional / 5 mixed / 3 negative), post-harmonization agreement: direction 73%, full-row 38/67. **Adjudication file: `corpus/adjudication_list.csv` — 29 disagreements + 10 fixed-seed sample rows; Arthur fills `resolution`, then values get merged into coding_table and `coding_status=final`.** Note for methods chapter: report both agreement stats and the harmonization step honestly. VERIFY flags (24) still to resolve during adjudication. Arthur's personal minimum: read the 3 benchmarks + all key_finding entries.

**Full-text screening working log (17 July 2026):** PDF acquisition: Elsevier Article Retrieval API (same key, VPN) delivers full PDFs **only for open-access** articles — 13 fetched to `literature/` via `corpus/fetch_fulltexts.py`; paywalled/preview 1-page files parked in `literature/_previews_no_entitlement/`; Lui + Krakowski + Babina full texts were already present. **66 PDFs still to fetch manually** (list: `corpus/fulltext_missing.csv`, borderline cases marked). First 4 full-text verdicts on borderline cases: Baffour Gyau → E2 (country-level panel), Shore → E4 (DV = resilience capability), Rennings → E4 (DV = patent forward citations), Pesqueira → include (qualitative comparative 4-firm evidence). Nayal flagged for recheck (same capability-vs-performance issue as Shore). **Current count: 78 include, 96 exclude, 11 borderline open.** PRISMA chain: 432 → 174 (AJG ≥ 2) → 81 (title/abstract) → full-text stage running. Update 17 July evening: Arthur manually fetched 11 PDFs (renamed to schema). Wamba-Taguimdje → include (code as low-rigor vendor-case evidence), Chiu → include (AI = patent proxy, firm-level DEA/Tobit). Update 18 July: OneDrive sync had delayed ~50 more of Arthur's downloads — all matched, renamed, 13 duplicate copies deleted. **Full texts now 76/78 — only 2 missing** (`corpus/fulltext_missing.csv`): He X. 2024 (World Scientific, 10.1142/S1363919624500191) and Platania 2025 (IEEE, 10.1109/TEM.2025.3585975), both borderline. Wamba-Taguimdje PDF re-downloaded (the earlier dedupe-bug loss is fixed; script patched). Borderline cases with PDFs on disk, awaiting full-text verdicts: D'Amico A., Vaillant, Steinhauser, Mehmood, Wu L., Zhao, Liu S., Jabbouri, Renfei + Nayal recheck.

**Query refined 6 July 2026 (proposal.tex is now the system of record, 425 hits):** the verb clause replaced `invest*` with an explicit term list (`"invest" OR "invests" OR "invested" OR "investing" OR "investment" OR "investments" OR "investor" OR "investors"`) plus `adopt* OR implement*`. Reason: `invest*` also matches `investigat*` ("this study investigates…"), which silently inflated the corpus by 75 records — mostly relevant but a *broader* construct (AI adoption/use/capability→performance) than the RQ's "AI investment". Scope decision = investment-specific (not broad AI-uptake). All 3 benchmarks still retrieved. Do NOT revert to `invest*`. (`adopt*`/`implement*` keep their wildcards — no false-friend stems.)

Scaffold cloned from the `Seminar Arbeit` project (APA/biblatex, per-section files, citation-footnote convention, AI-usage log).

## Cross-Check Workflow — Writing Phase (agreed with Arthur, 18 July 2026)

Continuation of the dual-AI principle from the coding phase: checks run only where there is objective ground truth, at defined gates — never continuous mutual review, and never a second opinion on style (style is governed by the standards files + Arthur). Three checks:

1. **Numbers → script, never an LLM.** `corpus/fact_sheet.py` (to build) derives a canonical fact sheet (all distributions, cross-tabs, percentages) from `coding_table.csv`. Rule: prose may only cite numbers that appear on the fact sheet; verification = diff against the file, deterministic.
2. **Citation fidelity → `corpus/gemini_verify_citations.py`, per finished section** (gebaut 28. Juli 2026). Aufruf: `python corpus/gemini_verify_citations.py sections/<datei>.tex` (`--no-llm` = nur der mechanische Teil, `--limit N` = Rauchtest). Das Skript parst jede `\parencite…\footnote{}`-Stelle, prüft das Source-Echo aus `rewrite_standards.md` §9 **selbst** (3+ gemeinsame Wörter, wörtliche Zitate und die Konstruktbegriffe der Arbeit ausgenommen) und lässt nur die Paraphrasentreue von Gemini beurteilen — blind, es sieht ausschließlich Satz + Passage. Ergebnis: JSON je Stelle in `corpus/gemini_citations/` (inhaltsadressiert, ein umformulierter Satz wird automatisch neu geprüft) plus `corpus/citation_check_<datei>.md` mit Adjudikationszeilen. Zwei bewusste Abweichungen von der ursprünglichen Skizze: „Zitat wörtlich" und „Seitenzahl korrekt" macht das MCP-Werkzeug `verify_citations` deterministisch, und der Echo-Test ist Rechnen, kein Urteilen — beides gehört nicht an ein LLM (Plan §3.5). Der PDF-Volltext bleibt draußen, weil die Auflösung Druckseite→PDF-Seite in `rag/` liegt; die Verwechslung Hypothese/Befund fragt der Prompt direkt ab.
3. **Blind section review → Gemini, once at the "section done" gate.** Gemini reads the finished section + fact sheet, flags factual contradictions and AI-style patterns. Once per section, not per paragraph. Arthur decides on all flags (same adjudication roles as in coding).

Every run gets logged in `ai-usage-log.md` (+ `main.tex` List of Aids) — this continues the dual-AI verification story from the coding phase.

**GEMINI CLI IST TOT (seit 13. Aug 2026 festgestellt):** Google hat den OAuth-Weg für
Einzelkonten abgeschaltet — genaues Datum unbekannt: am 28. Juli 2026 lief er noch
(Theorie-Zitatcheck), am 13. Aug 2026 kam `IneligibleTierError: UNSUPPORTED_CLIENT`
(auch mit AI-Pro-Abo). Ersatz: **Antigravity CLI** (`%LOCALAPPDATA%\agy\bin\agy.exe`,
Auth läuft still über den Windows-Keyring mit Arthurs Google-Account). Headless-Aufruf:
`agy -p "<prompt>" --model gemini-3.1-pro-high` — Prompt als Argument, nicht stdin.
`gemini_verify_citations.py` ist umgestellt (Modell wird je Verdict-JSON mitprotokolliert;
agy läuft in leerem Sandbox-Ordner, weil es ein Agent mit Datei-Tools ist — Blindheit).
`gemini_blind_coding.py` bleibt absichtlich auf dem alten Pfad: Coding-Phase abgeschlossen,
das Skript ist historisches Protokoll. Künftige Gemini-Zweitmeinungen (Blind Section
Review) ebenfalls über agy.

## File Structure

- `main.tex` — master file (documentclass `report`, chapters via `\input{sections/*}`); authoritative source
- `sections/introduction.tex`, `background.tex`, `method.tex`, `results.tex`, `discussion.tex`, `conclusion.tex` — one file per chapter
- `bib.bib` — bibliography (BibTeX exported from Scopus)
- `ai-usage-log.md` — running log of AI tools; rendered as the List of Aids appendix
- `WRITING_STANDARDS.md` — citation rules, source fidelity, register, chapter rules (ALWAYS follow when drafting)
- `rewrite_standards.md` — human-voice pass: banned words/syntax, paraphrase authenticity (apply to every drafted paragraph)
- `VOICE_PROFILE.md` — Arthur's writing fingerprint (derived from `voice_samples/`); use during drafting and the rewrite pass; standards outrank voice on conflict
- `vocabulary/` — pipeline scripts to harvest preferred vocabulary from the literature corpus; regenerate the CSVs once `literature/` is populated (seminar-era CSVs deliberately not copied)
- `literature/` — source PDFs (create as needed)

Compile with Overleaf, or locally with MiKTeX: `pdflatex main.tex`, then `biber main`,
then `pdflatex` twice more. (`latexmk` is installed but unusable here — MiKTeX's
latexmk is a Perl script and Perl is not installed on this machine.)

## Reading PDFs

**A PDF with no text layer is not automatically unquotable — look for a `.txt` sidecar
next to it first.** `literature/barney1991firm.pdf` is a pure image scan (0 characters
over 22 pages), but `literature/barney1991firm.txt` holds the verified text: OCR base,
then checked against the scan page by page, with `--- PAGE N (PDF p.M) ---` markers and
the pagination rule in its header, and the original's printed typos preserved on purpose.
Sidecar text is OCR-derived, so never take a footnote from it blind: read the quoted
passage off the page image as well. The Read tool renders PDF pages as images via the
`pages` parameter, which works on scans too.

Two-column publisher PDFs need column-wise extraction with a tight `x_tolerance`
(`page.crop((0, 0, w/2, h))` per column, `extract_text(x_tolerance=1.4)`); the default
interleaves the columns and drops the spaces between words. Verify printed page numbers
against the running heads (e.g. Kemp: PDF page n = printed 617+n).

Use pdfplumber from the `rag/.venv` interpreter, not the system Python. Both have
pdfplumber installed, in different versions (system 0.11.9 on Python 3.13, venv 0.11.10
on 3.12), and the citation check in `rag/` is calibrated against the venv one. One
extraction path for one job:

```powershell
$env:PYTHONIOENCODING = "utf-8"
& "C:\Users\arthu\Desktop\College Bachelor Arbeit\rag\.venv\Scripts\python.exe" -c "
import pdfplumber, sys
sys.stdout.reconfigure(encoding='utf-8')
with pdfplumber.open(r'PATH_TO_PDF') as pdf:
    for i, page in enumerate(pdf.pages):
        t = page.extract_text()
        if t: print(f'--- PAGE {i+1} ---\n{t}')
"
```

## Library Tools (`rag/`, MCP server `library`)

Local retrieval over the 67 full texts of the frozen corpus. Built 27 July 2026, see
`RAG_INTEGRATION_PLAN.md` and `rag/docs/ABWEICHUNGEN.md`. Purpose: **find citable
passages fast** — it locates, it does not decide and does not write.

Tool choice: narrow factual question → `search_library`. Comparison or synthesis →
`find_relevant_documents`, then `read_full_document` for the 3–5 selected papers.
Excerpt looks cut off → `get_chunk_context`. Before a complex search, form three
rephrasings plus one hypothetical answer and send all of them through
`search_library_multi` (original question first).

The first search of a session loads ~6 GB of models into the server process and can take
minutes — over 30 in one observed case, because Windows spills to shared memory instead
of erroring when VRAM is occupied. Warm it with a small search first; afterwards both
search tools respond in seconds. `list_documents` needs no model and always answers
immediately. Code changes under `rag/` need a session restart to take effect.

Three rules, all of them non-negotiable:

1. **The chunk text is the citation source; `verify_citations` checks it against the
   real page.** Originally the rule here said to re-copy the wording from pdfplumber.
   That was wrong and was measured out: on two-column publisher PDFs a naive
   pdfplumber read is *worse* than Docling — it interleaves columns and drops spaces
   into the middle of words (`critically`, `organizations,` vanish as tokens), so only
   ~25% of genuine 20-word quotes match it as a substring. Docling's linearization is
   the better text. `verify_citations` therefore does the page check for you, tolerant
   of that extraction noise (word sequence, threshold 0.60 — calibrated so that 0 of 60
   fabricated quotes pass). When it reports "maschinell nicht bestätigt", open that page
   and look before the quote goes in a footnote — roughly 1 in 10 legitimate quotes
   lands there. One exception you must fix by hand: 16 of the 67 papers render `fi`,
   `fl`, `ff` as a separate run, so the extract reads `fi rm`, `signi fi cant`,
   `in fl uence` (worst: S17, S38, S34; the tool flags the extract). Write the word
   normally in the footnote — `verify_citations` accepts the corrected spelling, and
   that spelling is what the printed page actually shows.
2. **Cite the printed page, never the PDF page.** Output reads `S. 207 (PDF-S. 3)`:
   207 goes in the footnote, 3 is the page you open to check. Where it says
   `PDF-S. N (keine gedruckte Seitenzahl erkannt)` the document has no printed
   pagination — resolve it explicitly (section reference or article number), never
   pass the PDF page off as a printed one.
3. **Run `verify_citations` before every answer containing quotes.** Pass
   `[{quote, chunk_id}, …]`. It checks two things: the quote appears verbatim in that
   chunk, and its words appear in order on the cited PDF page. The second stage also
   catches a quote pinned to the wrong chunk (verified: a real quote with a wrong
   `chunk_id` comes back NICHT BESTÄTIGT). NOT BESTÄTIGT means correct the quote or
   mark it `[unbestätigt]` — never let it through silently.

What the tool is not: it is **not** a source of numbers. Every count, percentage, and
cross-tab still comes from `corpus/FACT_SHEET.md` only. And it played no part in
corpus identification, screening, or coding — those were frozen before it existed.

Start it: `claude mcp add library --env DB_PATH=<abs>\rag\library.db -- <abs>\rag\.venv\Scripts\python.exe -m retrieval_mcp`

## Citation Footnote Convention (ALWAYS follow)

Every citation — direct quote or paraphrase — gets a `\footnote{}` placed **immediately after** the `\parencite{}` or `\textcite{}` command (before any following punctuation). The footnote holds the verbatim passage so the citation can be verified in the compiled PDF.

```latex
\parencite[p.~X]{key}\footnote{[Author (year), p.X] ``Exact quoted passage from the source.''}
```

- Read the cited page from the PDF with pdfplumber before writing the footnote.
- Multi-key citations: one passage per source in the same footnote.
- Strip all `\footnote{[...]}` blocks when the user says "delete the citation footnotes".
- Every citation (direct or paraphrase) needs a page number — no exceptions.

### Seven papers have no printed page numbers (rule frozen 28 July 2026)

`rag/review/_report.md` marks them „keine → PDF-Seiten". Never pass a PDF page off as a
printed journal page; cite them like this instead:

| Studien | Verlagstyp | Zitierweise |
|---|---|---|
| S06 Lee, S17 Babina, S21 Sullivan | Elsevier, artikelnummeriert | Artikelnummer im `eid`-Feld der bib (APA rendert „Article 103745"); Seitenangabe = artikelinterne Seite, die bei Elsevier mit der PDF-Seite identisch ist → `\parencite[p.~5]{...}` ist korrekt |
| S26 Banna, S39 Tehrani | Emerald | PDF-Paginierung ist artikelrelativ und unbrauchbar (Scopus' `pages` = `1--28` gehört gelöscht) → `\parencite[sec.~5.1]{...}` |
| S32 D'Amico (Springer), S54 Kazakis (Wiley) | online first / early view | noch keine Paginierung → `\parencite[sec.~4.2]{...}` |

Das gehört als Ein-Satz-Transparenzhinweis in den Methodenteil (Formulierung liegt als
Kommentar in `sections/method.tex`).

**`corpus/make_bib.py` erledigt zwei Dinge, die von Hand schiefgehen:** `&` in Titeln wird
escaped (unescaped bricht LaTeX beim ersten Zitat ab) und Akronyme werden geklammert, weil
biblatex-apa den Titel auf Satzschreibung setzt und „AI" sonst als „ai" im
Literaturverzeichnis steht. Eigennamen mitten im Titel (French, European) erkennt keine
Regel — das Skript warnt, geschützt werden sie von Hand.

## List of Aids (Appendix)

The appendix table in `main.tex` must always reflect the current state of `ai-usage-log.md`. Update the LaTeX table **immediately** when a new tool or per-section entry is added — do not defer to final compile.
