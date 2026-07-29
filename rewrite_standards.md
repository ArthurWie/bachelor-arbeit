# Rewrite Standards — Human-Voice Pass

Ported from the Seminar Arbeit project; rules unchanged, examples updated to this thesis's domain.

## Purpose

This document governs a paragraph-by-paragraph rewrite of the thesis to eliminate AI-typical phrasing and restore a natural, direct academic voice. Apply every rule in this file to every paragraph in sequence. Do not batch-rewrite; process one paragraph at a time and confirm before moving to the next.

---

## How to Use the Vocabulary Files

Two CSV files live in `vocabulary/`:

- `vocabulary/high_relevance.csv` — preferred words directly relevant to the thesis topic. Use these as first-choice substitutes when replacing banned words.
- `vocabulary/medium_relevance.csv` — general connective and functional words (e.g., *because, although, yet, however, while, different, various*). Use these when you need transitional language that doesn't trigger the banned-opener list.

> **NOTE (port):** The CSVs must be REGENERATED from this thesis's literature corpus once `literature/` is populated — the seminar-era CSVs were harvested from KM/PE sources and do not carry over. Run `vocabulary/pipeline.py` (see that folder's scripts). Until then, apply the fallback rule: choose the plainest English word that carries the meaning.

**How to apply them:** When a banned word appears, look for the most accurate substitute in `high_relevance.csv` first. If no match fits, check `medium_relevance.csv`. If neither list contains a precise fit, choose the plainest English word that carries the meaning without flair. Do not use a longer or rarer word just because it avoids the ban — simplicity is the goal.

---

## Academic Register Caveat

This thesis is a formal academic literature review. The rules below are applied to produce natural, readable prose, not conversational copy. Specifically:

- **Contractions**: Apply sparingly and only where they sound genuinely neutral rather than casual. In a scientific paper, `it's` and `don't` are acceptable in parenthetical or qualifying clauses; they are not appropriate inside a formal claim or a definition sentence. Use judgment.
- Third-person voice and passive constructions remain acceptable where they are standard academic usage.
- The goal is to remove AI-generated stiffness, not to introduce informality that would read as unprofessional in a WU thesis.

---

## 1. Vocabulary and Lexical Guardrails

### 1.1 Banned Verbs

Remove every instance of these verbs entirely. Replace with a plain alternative from the vocabulary files or the simplest accurate English verb:

> delve, embark, navigate, foster, garner, showcase, utilize, underscore, enhance, spearhead, leverage

**Common replacements:** *use* (for utilize), *show* (for showcase/underscore), *find/gain* (for garner), *support/build* (for foster), *lead* (for spearhead), *improve* (for enhance), *highlight/point to* (for underscore).

### 1.2 Banned Abstract Nouns

Remove these nouns and rewrite the surrounding phrase with concrete language:

> tapestry, landscape, realm, sphere, ecosystem, intersection, intricacies

**Approach:** Replace with a specific noun that names the actual thing. "The AI investment landscape" → "research on AI investments." "The intersection of AI and strategy" → "where AI and strategy research meet" or simply name what overlaps.

### 1.3 Banned Scale Modifiers

Strip these adjectives and adverbs entirely. Either drop them or replace with a specific, measurable claim:

> crucial, pivotal, robust, dynamic, multifaceted, intricate, vibrant, overarching, seamless, unparalleled, unprecedented, enduring

**Rule:** If the sentence relies on one of these words to convey importance, the sentence is not doing enough work on its own. Make the importance explicit through specifics, not adjectives.

---

## 2. Banned Connective Openers

Do not open a sentence with these formal linkers. Ideas must connect through logic and sentence construction, not stock transitions:

> Moreover, Furthermore, Consequently, Additionally, Therefore, Thus, Hence

**Replacement approach:** Restructure the sentence so the logical relationship is carried by the clause itself. If a causal link must be signalled, use *because*, *since*, *so*, or *which means* (mid-sentence, not as openers). *However* and *yet* are acceptable as non-opening connectives.

---

## 3. Banned Filler Phrases

Delete these phrases wherever they appear — they add length without meaning:

> "it is worth noting," "it is important to note," "due to the fact that," "in order to," "at this point in time," "in today's fast-paced world"

**Replacement approach:** Drop the phrase entirely and start with the actual claim. "It is worth noting that AI investments improve firm growth" → "AI investments improve firm growth."

---

## 4. Banned Vague Attributions

Do not use unattributed authority claims. Every claim must trace to a named source or be presented as the author's own synthesis:

> "experts believe," "studies show," "industry reports suggest," "critics argue," "research indicates" (when no citation follows)

**Rule:** State the fact or finding directly, with a citation, or flag it as the author's own reading of the literature (e.g., "Across the reviewed studies, a pattern emerges…").

---

## 5. Banned Hedging Clusters

Strip stacked hedges. A single hedge is acceptable where genuine uncertainty exists; never combine two or more:

> "could potentially possibly," "might arguably perhaps," "may arguably suggest"

**Rule:** Choose one hedge if uncertainty is real. Drop all of them if the claim is well-supported by a citation.

---

## 6. Syntactic and Structural Rules

### 6.1 Sentence Rhythm

Vary sentence length within every paragraph. After a sentence longer than 25 words, write at least one sentence under 12 words before the next long one. Monotonous clause length is a primary AI-prose signal.

### 6.2 No Rule of Three

Do not list exactly three adjectives, three examples, or three outcomes in a row. Use two, four, or a prose description instead.

*Flagging pattern:* Any "X, Y, and Z" list of qualities or examples within a single sentence is a candidate for this check.

### 6.3 No Parallel Negation or Antithesis

Do not write "It is not just X, but rather Y" or "This isn't merely X — it is Y." State the positive claim directly.

### 6.4 Use the Copula Directly

Use *is* and *are*. Never substitute them with:

> "serves as," "acts as," "operates as," "functions as"

*AI serves as a general-purpose technology* → *AI is a general-purpose technology.*

### 6.5 Punctuation Budget

- Em-dashes: maximum one per 500 words. Use a comma, semicolon, or a new sentence instead.
- Parenthetical asides: use sparingly. If a parenthetical can be a separate sentence, make it one.

### 6.6 No Rhetorical Q&A

Do not pose a question only to answer it immediately in the next sentence. State the point directly.

### 6.7 No Anaphora

Do not start two consecutive sentences with the same word or phrase. Restructure one of them.

### 6.8 No Runway Sentences

Do not chain multiple independent clauses into a single breathless sentence with *and*, *while*, *as*, or *which* stacked more than twice. Break it at the natural clause boundary.

### 6.9 No Elegant Variation (Synonym Cycling)

If a specific noun is the most accurate term, repeat it. Do not substitute synonyms to avoid repetition. Consistency of terminology is a requirement of `WRITING_STANDARDS.md §5` and reinforces academic precision.

---

## 7. Voice, Tone, and Rhetorical Framing

### 7.1 No Puffery

Do not describe any concept, method, or finding as:

> "groundbreaking," "milestone," "pivotal turning point," "transformative," "breathtaking," "game-changing"

Drop the evaluative claim and let the evidence carry the weight.

### 7.2 No Sycophantic Phrases

Remove any instance of:

> "Great question!", "You're absolutely right!", "That's a fascinating perspective."

These have no place in academic writing and should not appear in the rewritten text.

### 7.3 No Dramatic Reframe or Manufactured Punchline

Do not end paragraphs with an artificially profound or witty closing line inserted to create rhetorical impact. End when the point is made.

### 7.4 No Performative Directness

Remove phrases inserted to simulate authority:

> "Let's be clear," "Here's the truth," "To be honest," "Simply put," "Make no mistake"

### 7.5 No Forced Optimism

If discussing a gap, failure, or limitation, do not append a hopeful qualifier. Leave the limitation stated plainly.

### 7.6 Allow Unresolved Arguments

Not every paragraph needs a tidy conclusion. If the evidence is ambiguous or incomplete, say so and move on. Do not force resolution.

---

## 8. Formatting Rules

### 8.1 No Metronomic Paragraph Structure

Do not structure every paragraph as Claim → Evidence → Significance. Vary the internal logic: start with the evidence, or with a qualification, or mid-thought.

### 8.2 No Generic Openings or Closings

Do not begin a section with scene-setting preamble ("Artificial intelligence is a field that…"). Start with the first substantive claim. End when the final point is made — no summary sentence that repeats what the paragraph just said.

### 8.3 No Outline-Style Conclusions

Do not include a paragraph or subheading titled:

> "Challenges and Future Prospects," "Looking Ahead," "In Summary," "To Conclude"

The Conclusion chapter has its own heading via LaTeX sectioning. Within-paragraph summary closings are banned.

### 8.4 No Inline Bold Headers

Do not bold the first few words of a sentence to simulate a bullet point:

> **Cost efficiency:** The system reduces costs… ← banned

Use proper LaTeX `\subsection{}` or plain prose instead.

### 8.5 Sentence Case for Subheadings

All subheadings use sentence case, not Title Case.

---

## 9. Paraphrase Authenticity

Every indirect citation in the thesis has a `\footnote{}` containing the verbatim source passage used to verify the claim (see CLAUDE.md citation footnote convention). During the rewrite, read that footnote passage before touching the running text.

**The rule:** The rewritten sentence must not echo the source's word order, clause structure, or phrasing. If someone removed the footnote and placed the running text next to the source, they should not read as near-identical.

**How to check:** After drafting the rewrite, compare it word-by-word against the footnote passage. If three or more consecutive words from the running text also appear consecutively in the source, restructure until they don't.

**What counts as a genuine paraphrase:**
- The subject of the sentence changes, or the grammatical construction changes (source uses a noun clause → running text uses an active verb construction, or vice versa)
- Only the core finding is preserved — the framing, emphasis, and sentence architecture are the author's own

**What this is not:**
- This rule does not require distorting the source's meaning. The finding must still be accurately represented.
- This rule does not apply to direct quotes (text inside `"..."` in the running text). Direct quotes reproduce the source verbatim by definition.
- This rule does not apply to defined technical terms (AI, RBV, SLR, GPT as general-purpose technology, etc.) — those must be consistent per `WRITING_STANDARDS.md §5`.

---

## 10. Rewrite Process — Paragraph-by-Paragraph Protocol

1. **Read the paragraph** as written.
2. **Read all footnotes** in the paragraph to see the source passages being cited.
3. **Flag all violations** against §1–§8 above before writing a single word of the rewrite.
4. **Check substitutes** in `vocabulary/high_relevance.csv` for any banned word being replaced.
5. **Rewrite** the paragraph, applying all flagged corrections simultaneously.
6. **Paraphrase check:** compare each rewritten indirect-citation sentence against its footnote source passage. Restructure any sentence that shares three or more consecutive words with the source.
7. **Self-check** the rewrite: scan for any new instances of banned patterns introduced during rewriting.
8. **Present the rewrite** and wait for confirmation before moving to the next paragraph.

Do not rewrite the next paragraph until the current one is confirmed.

---

## 11. Simplicity Override (added 4 July 2026, from author feedback)

The strongest rule in this file. When any rule here conflicts with plainness, plainness wins.

**Minimal-edit principle:** Rewrite a sentence ONLY if it violates §1–§8, exceeds the
§6.1 length rhythm, or is genuinely hard to follow. "I can phrase this better" is not
a reason. The original sentence is the default; every edit must be justifiable as a
simplification, not a stylistic improvement.

**Banned rhetorical structures** (beyond §6):

- Cleft and pseudo-cleft sentences: "What these investments return is…", "It is the
  conditions that…" — write subject-verb-object instead.
- Emphasis adverbs used for stress: *actually, truly, genuinely, indeed, in fact*
  (acceptable only for genuine contrast with a previous claim).
- Evaluative comparatives replacing plain description: "far less clear" → "unclear";
  "much more compelling" → state the finding.
- Added colons, dashes, or inversions that the original sentence did not need.

**Hard checks for every rewrite:**

- If the rewrite is LONGER than the original, it is suspect — revert or shorten.
- If the rewrite uses RARER vocabulary than the original, it is wrong — revert.
- If the subject appears later in the rewrite than in the original, revert.
- A voice trait (VOICE_PROFILE.md) never justifies adding rhetorical structure to a
  sentence that was already plain.

## 12. What This Pass Does Not Change

- Citation formatting (`\parencite{}`, `\footnote{}`, page numbers) — do not alter.
- LaTeX commands, environments, or structure — do not alter.
- Factual claims or the attribution of findings to sources — do not alter.
- Chapter-level organisation — do not alter.
- Terminology that is defined on first use and used consistently — keep as-is per `WRITING_STANDARDS.md §5`.
