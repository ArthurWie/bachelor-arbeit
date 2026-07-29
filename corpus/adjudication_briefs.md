# Adjudication Briefs — Dual-Coding Review

**Purpose:** Evidence briefs for Arthur's final batch review. Cases S01–S41 (18 disputes)
were adjudicated one-by-one on 18 July 2026 (decisions recorded in `adjudication_list.csv`
and finalized in `coding_table.csv`). All cases below carry **PROPOSED** decisions from
Claude's full-text reads, applied to the coding table with `coding_status = draft`.
Nothing below is final until Arthur approves it in the batch session.

**How to review each case:** read the brief, check the quoted evidence against the PDF
(page refs given), then either accept (→ Claude flips row to `final`) or override
(state the correct value).

**Decision rules:** see "ADJUDICATION CASE LAW" section in CLAUDE.md — developed and
approved during the first 18 cases.

---

## Already adjudicated (for reference, no action needed)

| Case | Dispute | Decision | One-line rationale |
|---|---|---|---|
| S01 Wamba 2020 | outcome | performance | model P1–P6 contains no CA construct; "competitiveness" only a KPI word (p.10) |
| S03 Chatterjee 2021 | outcome+VERIFY | both | own COA scale, H4 (0.59***, R²=.76), discriminant-valid; moderators were actually controls |
| S04 Chatterjee 2022 | outcome, direction | performance, positive | 5 constructs no CA; ACRM→FP 0.53*** unconditional |
| S05 Hossain 2022 | method | survey-SEM | hypotheses tested only via PLS-SEM n=257; interviews developmental |
| S07 Leoni 2022 | direction | conditional | direct AI→MFP 0.006 n.s. (H2 rejected) — full mediation via KMPs |
| S09 Mishra 2022 | conditions | empty | no moderators tested (explicitly deferred to future research) |
| S10 Sun Y. 2022 | outcome | competitive_advantage | "economic value" = co-creation mediator, not performance |
| S11 Ali Mohamad 2023 | outcome, conditions | both, filled | 4 outcome categories + genuine competitor-comparative CA evidence |
| S12 Czarnitzki 2023 | conditions | empty | intensity = alternative treatment measure, not condition |
| S16 Wu 2023 | method | survey-SEM | SEM tests hypotheses; fsQCA supplementary |
| S18 Cannas 2024 | outcome, direction | performance, positive | competitiveness = operational improvements; barriers → conditions |
| S19 Pesqueira 2024 | all three | mixed, both, conditional | dual-method evidential; CA expert-rated in tender context; "contingent upon" as finding |
| S21 Sullivan 2024 | direction | conditional | no direct AI→perf paths; relational n.s.; 10/18 conditional effects |
| S26 Banna 2025 | direction | conditional | U-shape sign flip, turning point USD 11.3M |
| S28 Bin-Nashwan 2025 | direction | conditional | no direct path; GRC channel null; sample = 433 China (not Oman/Malaysia!) |
| S31 Chiu 2025 | direction | mixed | AI ✓ sustainability+market stages, ✗ profit stage |
| S36 Huang 2025 | outcome, direction | performance, mixed | no CA construct; productivity n.s., first movers partly negative; sample = S&P 500 |
| S37 Kumar 2025 | method | survey-SEM | AI→performance tested only in Study 2 SEM |
| S41 Shi 2025 | direction | positive | direct effect 0.048*** (z=10.3); subgroup nulls = boundary conditions |

---

## PROPOSED — awaiting Arthur's batch review

### S47 Alnofeli 2026 — method: PROPOSED `survey-SEM` (Gemini)
Claude said mixed. Full text: three-stage design, but "a systematic scoping review and in-depth
interviews with industry experts **identify the core dimensions and subdimensions** of AI-powered
CRM capability" (Stage 1, n=24 interviews) — pure construct/instrument development. "Third, a
**survey of 205 banking employees in Australia tests** the influence…" → the AI→outcome evidence
is solely SEM. Kumar/Hossain precedent.

### S48 Arshad 2026 — method: PROPOSED verbatim `survey-based regression (two cross-sectional surveys)`; direction: PROPOSED `mixed` (Claude)
Neither coder's method fits: not SEM (Gemini), not panel (Claude) — two cross-sectional
international surveys (Study 1: 2018 Deloitte survey, n=1219 large firms) analyzed with regression
models; scheme rule: write verbatim. Direction: "joint implementation is positively associated with
additional **revenue growth** … but is **not associated with additional cost reduction**" ("the
joint term is not significantly associated with cost reduction") → component split = mixed
(S31/S36 precedent).

### S52 Filieri 2026 — direction: PROPOSED `conditional` (Claude)
Gemini said positive. Full text: "performance benefits follow an **inverted U-shape**: extreme
tariff exposure diminishes AI's compensatory effects … revealing an **optimal investment
threshold**" — sign/size flip along the adversity dimension = conditional (S26 Banna precedent).

### S53 Giordino 2026 — conditions: PROPOSED empty (Gemini)
Claude had filled it. Full text: plain association study, no moderators/heterogeneity tested; the
E/S pillar gains and the governance-null (b=0.030, p=.166) are outcome descriptions →
performance_measure/key_finding, not conditions. S09/S12 precedent; joins the
unconditional-evidence contrast group.

### S55 Li (IJPE) 2026 — direction: PROPOSED `conditional` (Gemini)
Claude had positive (harmonization overshoot). Full text: "the initial **direct effect of
responsible AI on competitive advantages is … nonsignificant (β = 0.091, p > .05)**" — full
mediation via distributive + procedural justice; complexity weakens the distributive path
(−0.233***). Leoni class.

### S56 Li (JBR) 2026 — **BLOCKED, action needed**
The full text (1-s2.0-S0148296326000081-main.pdf) was **deleted by the early dedupe bug** (same
bug that hit Wamba, before the fix); the pdf column wrongly pointed to Lin M.'s file, so **Gemini
coded the wrong paper — its S56 coding is invalid.** Claude's draft is abstract-based.
→ **Arthur: re-download doi.org/10.1016/j.jbusres.2026.115974**; then Claude re-verifies and
Gemini re-runs this one study. Method+outcome dispute unresolvable until then.

### S60 Liu Z. 2026 — direction: PROPOSED `positive` (Claude)
Gemini said conditional. Full text: "AI-enabled innovation is associated with firm growth **both
directly and indirectly** through productivity gains, with the **strength** of the
innovation–productivity link contingent on the regional regulatory climate" — moderation of
strength, baseline effect present → positive per Shi rule; regulatory-climate moderated mediation
stays in conditions.

### S61 Mukherjee 2026 — direction: PROPOSED `positive` (Gemini); conditions: PROPOSED empty
Claude had conditional with TOE drivers as conditions. The drivers (ease of use, competitive
pressure, IT infrastructure, policy support) are **antecedents of adoption**, not conditions on
the AI→service-performance link; that link is a positive main effect.

### S63 Renfei 2026 — direction: PROPOSED `positive` (Gemini)
Claude had conditional. Full text: "AIC **significantly enhances CSP** through a tiered enabling
mechanism, but **prescriptive capabilities fail**…"; firm-type boundary: I4.0 firms 0.58*** vs
traditional **significantly weaker** — weaker, not null → positive per Shi rule; prescriptive-null
and firm-type boundary stay in conditions.

### S65 Song X. 2026 — direction: PROPOSED `negative` (Gemini)
Claude had conditional. The focal treatment is AI **overclaiming** (claims-vs-patents gap); its
net effect: "narratives **initially attract investors but ultimately yield negative market
reactions and sustained underperformance**" — short-lived pop, lasting punishment → net negative
per main-effect rule; time path documented in conditions.

### S67 Wang S. 2026 — direction: PROPOSED `conditional` (Claude)
Gemini said positive. Abstract: "The mediating effect of strategic resilience is robust and
**fully accounts for** the AI capability–success relationship" — full mediation, no independent
direct path → Leoni class; fsQCA equifinality noted.

---

## SAMPLE spot-checks (10 agreement rows) — all verified against full texts, 18 Jul 2026

| Row | Agreed coding | Check result |
|---|---|---|
| S03 Chatterjee 2021 | survey-SEM / both / positive | OK (fully verified in one-by-one adjudication) |
| S08 Lui 2022 | event study / performance / negative | OK (Factiva announcements, CAR −1.77%) |
| S13 Huang CKT 2023 | event study / performance / positive | OK — corrected detail: **109** announcements (not 97), 2014–2019, S&P 500/USA |
| S14 Krakowski 2023 | panel / both / conditional | OK (chess panel, verified in earlier full read) |
| S29 Cao 2025 | fsQCA / performance / conditional | OK — country resolved: 140 **U.S.** retail managers |
| S32 D'Amico E. 2025 | panel / performance / conditional | OK (R&D complementarity condition; AI measure = Beauhurst/BSD/UKIS) |
| S38 Mehta 2025 | mixed / both / positive | OK (CA = own mediator construct, H9) |
| S40 Sandeep 2025 | survey-SEM / CA / positive | OK (CA via established scales, Appendix 1) |
| S42 Song D. 2025 | event study / performance / negative | OK (120 events, NYSE/NASDAQ = USA) |
| S43 Tao 2025 | survey-SEM / performance / positive | **OK with caveat:** total effect 0.24***, indirect 0.15* — partial mediation; positive stands per main-effect rule, but direct-path row not explicit → borderline to conditional. Flagged for Arthur's judgment in batch review. |

**Conclusion:** no joint coder errors found; one borderline judgment (S43) surfaced for review.

## VERIFY fact-gaps (15 rows) — all resolved from full texts, 18 Jul 2026

S08 (lens: IT-business-value event-study tradition; announcements via Factiva 2015–2019, market
composition not explicit) · S13 (109 announcements, S&P 500, USA) · S15 (n=142, India) ·
S17 Babina (1,993 US Compustat firms, resume-based/Cognism) · S22 Sun Z. (annual-report AI term
frequency) · S26 Banna (AI_INV = log AI venture funding, OECD AI Policy Observatory) · S29 (140
US retail managers) · S30 Chakraborty (India, 1,487 invited → wave 1 n=437, wave 2 n=408) ·
S32 (Beauhurst + BSD + UKIS 2004–2020) · S42 (120 NYSE/NASDAQ events 2010–2024) · S54 Kazakis
(US Compustat, DEA efficiency, labor-based AI measure) · S57 Lin M. (annual-report text measure) ·
S58 Lin N. (tailored AI-keyword dictionary) · S59 Liu D. (CNINFO annual reports, jieba, ln(1+freq))
· S63 Renfei (292 valid responses, 120 Chinese manufacturers) · S64 Singh (AI patents p.a.,
PATENTSCOPE AI Index; 1 SD = 115.66 patents → Tobin's Q +3%)

---

## BATCH COMPLETE — what Arthur reviews in the final session
1. The 10 PROPOSED dispute decisions above (S47–S67 section)
2. The S43 borderline caveat (positive vs conditional)
3. S56: re-download `doi.org/10.1016/j.jbusres.2026.115974`, then Claude verifies + Gemini re-runs
4. On approval: all draft rows flip to `final` → coding table complete → descriptive charts + results chapter begin.
