# Writing Standards — Bachelor's Thesis

Ported from the Seminar Arbeit project (SS26); seminar-specific parameters removed.
Thesis-specific numbers (word count, chapter distribution) are TBD until PD Dr. Fredrich
confirms them — do not invent targets.

## 1. Citation Rules (Non-Negotiable)

- **Every single citation** — direct quote OR paraphrase — must include the **exact page number**. No exceptions.
- Format for **indirect citation** (paraphrase): `(Author, Year, p. X)` or `Author (Year, p. X)`
- Format for **direct quote**: `"exact text" (Author, Year, p. X)` — also requires quotation marks
- If a finding spans multiple pages: `(Author, Year, pp. X–Y)`
- **Never cite a paper without having verified the page number from the actual PDF.** No guessing.
- Secondary sources (citing X as cited in Y): avoid where possible. Always try to obtain the primary source.
- Every source cited in text must appear in the References section, and vice versa.
- **Citation style: APA 7th edition (author-date).** BibTeX entries must include DOI where available.
- **Default to paraphrase.** Use direct quotes only when the exact wording matters (definitions, terminology being introduced, distinctive phrasing). A literature review should contain very few direct quotes.

## 2. Source Fidelity

- Every claim that is not common knowledge must trace back to a source in the SLR corpus or the theory anchors in `bib.bib`.
- Do not fabricate findings, page numbers, or quotes. If a source does not say something, do not attribute it.
- If two sources make similar claims, cite both; do not collapse them into one citation.
- Paraphrases must accurately reflect the source's meaning — do not distort through summarization.
- **Mark own claims as such.** Any synthesizing claim, cross-source comparison, or assessment that is not directly attributable to a single source must be flagged as the author's own analysis (e.g., "This review finds that…", "Across the reviewed studies, a pattern emerges…"). Never present own synthesis as if it were sourced.
- **SLR-specific:** the corpus is defined by the documented Scopus query (see CLAUDE.md). Sources outside the corpus may only appear as theory/method anchors, and the Method chapter must make that distinction explicit.

## 3. Method Honesty (SLR)

- Describe the actual search process performed. Do not invent databases that weren't searched, search strings that weren't used, or inclusion/exclusion criteria that weren't applied.
- The reported query, run date, hit count, and screening numbers must match what actually happened (the run log / exports are the ground truth).
- Every screening decision must be reproducible from the stated criteria — that is the grading standard ("maximale Transparenz für eine kritische Reproduzierbarkeit").

## 4. Chapter Rules (genre standards — carry over from seminar structure)

### Abstract & Keywords
- Abstract must stand alone — no citations, no abbreviations not defined within it.
- Keywords listed below the abstract, separated by semicolons.

### Introduction
- Must address all four points in order: (1) topic/context + why relevant, (2) summary of prior research, (3) research question stated explicitly, (4) outlook on how the thesis answers it.
- No interpretation or conclusions here.

### Method
- Which database, what search string, what inclusion/exclusion criteria, how many studies at each screening stage (PRISMA-style flow).

### Results
- Present findings — do not interpret them.
- The state-of-the-art table is the core; every table/figure numbered, captioned, referenced in the running text before it appears.
- Own synthesis tables: caption `Source: own representation` or `Source: author's compilation based on [sources]`. Tables adapted from a single source cite it with page number.

### Discussion
- Must explicitly restate the research question at the start.
- Interpret what the Results mean — connect findings to each other and to the broader debate.
- Identify what the literature does NOT yet answer (gaps → future research).
- Lean into "conditions/configurations" framing (see supervisor profile in CLAUDE.md).

## 5. Academic Register and Language

- Language: **English** throughout (scientific register).
- Third person or passive voice where appropriate (no "I think", "I found").
- No colloquial expressions, contractions in formal claims, or informal phrasing.
- Be precise — no vague hedging ("kind of", "sort of", "maybe").
- Use hedging language correctly where genuine uncertainty exists ("suggests", "indicates", "may").
- **Terminology consistency:** once a term is chosen, use it throughout (e.g., do not alternate between "AI investment" and "AI adoption" when meaning the same construct — pick per construct and define on first use). Define abbreviations on first use (e.g., "artificial intelligence (AI)") and use the short form consistently thereafter.

## 6. LaTeX / Formatting

- Section headings via `\chapter{}`/`\section{}`/`\subsection{}` — never manually bolded headings.
- Tables in `table` environments with `\caption{}` + `\label{}`; figures likewise.
- All cross-references via `\ref{}`; all citations via `\parencite{}`/`\textcite{}` against `bib.bib`.
- Subheadings in sentence case, not Title Case.

## 7. What NOT to Include

- No empirical methods of our own (this is a literature review).
- No interpretation in the Results chapter.
- No unsourced claims (other than clearly-marked own synthesis — see §2).
- No corpus-external sources without explicit justification in the Method chapter.
- No padding, repetition, or filler sentences to hit word count.

## 8. AI Usage Protocol / List of Aids

Maintained in `ai-usage-log.md`, rendered as the List of Aids appendix in `main.tex` — sync immediately on every change (see CLAUDE.md). Entries in first-person, casually descriptive student-protocol tone: AI tools framed as checking, polishing, and lookup aids; substantive thinking, literature analysis, and synthesis done manually by the author. Per-section rows as chapters get drafted; a "no AI used" row where true.

## 9. Companion File

`rewrite_standards.md` governs the human-voice rewrite pass (banned words, syntax rules, paraphrase authenticity). Apply it to every drafted paragraph before considering a chapter done.
