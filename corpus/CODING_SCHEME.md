# Coding Scheme — State-of-the-Art Table (frozen 18 July 2026)

One row per included study (n = 67) in `coding_table.csv`. Bibliographic columns
(`study_id`…`pdf`) are auto-filled from the frozen corpus — never edit by hand.
Coding columns below. Rules: code only what the study explicitly reports; when a
value doesn't fit the categories, write it out verbatim rather than forcing a
category; every non-obvious judgment gets a note in `quality_notes`.

| Column | Allowed values / format | Notes |
|---|---|---|
| `theoretical_lens` | RBV, dynamic capabilities, GPT, TOE, KBV, institutional, agency, contingency, none, other (name it); combinations with `+` | The lens the study *uses*, not what it cites in passing |
| `method` | `survey-SEM`, `panel econometrics`, `event study`, `case study`, `experiment`, `fsQCA`, `DEA`, `mixed` | Primary identification strategy; add IV/DiD/GMM detail in `quality_notes` |
| `sample` | free text: n, unit, period, design | e.g. "1,479 firms, EU-26, panel 2012–2023" |
| `country_region` | country name(s), `multi-country`, or region | As reported |
| `industry` | sector or `cross-industry` | As reported |
| `ai_measure` | free text, but name the *type*: survey construct, resume-based, patents, announcements, earnings-call/10-K text, procurement index, robot penetration, adoption dummy, case observation | This column feeds a key results figure — keep the type words consistent |
| `outcome_construct` | `performance` \| `competitive_advantage` \| `both` | **Supervisor feedback #1.** `competitive_advantage` only if the study measures a distinct CA construct (sustained advantage, positional advantage, perceived CA scale) — a performance gain alone is `performance` |
| `performance_measure` | free text (ROA, TFP, Tobin's q, firm value/CAR, revenue growth, operational efficiency, …) | Empty if not measured |
| `ca_measure` | free text | Empty if not measured — expect this column to be mostly empty; that emptiness is itself a finding |
| `effect_direction` | `positive` \| `negative` \| `mixed` \| `null` \| `conditional` | `conditional` = the sign/size depends on identified conditions (most interesting case for the RQ) |
| `conditions` | free text; separate multiple with `;` — name each condition + its role (moderator/mediator/complement/threshold) | **The core column of the thesis.** e.g. "complementary tech investments (complement); AI intensity threshold; internal R&D strategy (moderator)" |
| `key_finding` | one sentence | In your own words, not the abstract's |
| `quality_notes` | free text | Perceptual self-report? Vendor data? IV/quasi-experiment? Pre-registered? Small n? |
| `coding_status` | `` (empty) → `draft` → `final` | `final` only after the full text was read (this doubles as the full-text eligibility check for never-flagged includes; if a study fails eligibility here, it goes back to the screening CSV with an E-code) |

Workflow: Claude drafts codes from the PDF (→ `draft`), Arthur verifies against
the paper and sets `final`. Any eligibility failure discovered during coding is
documented in `screening_2026-07-17.csv`, and the PRISMA count is updated.
