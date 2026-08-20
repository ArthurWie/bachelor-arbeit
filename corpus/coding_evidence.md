# Coding Evidence Dossier — final audit pass

One section per included study (n = 67): the coding-table row verbatim from `corpus/coding_table.csv`, then the verbatim source passages that back each coded value. Every quote was machine-checked in two stages (verbatim in the extracted full text; word-sequence ≥ 60% on the real PDF page, pdfplumber x_tolerance=1 — the same calibration as `verify_citations`).

Symbols: ✓ machine-verified · ⚠ on-page check failed (usually a page extraction problem, not a wrong quote — open the page) · ✗ not in document text (must be fixed). Pages are printed journal pages unless marked as PDF pages.

**Order:** columns and evidence follow the printed appendix tables — first Table A.1 (Country, Sample, Method, AI measure), then Table A.2 (Outcome, measures, Direction, Conditions, Key finding), then the coding fields that are not printed (lens, industry, quality notes) — so you can walk the tables column by column.

**Manual checking:** every quote carries a `Ctrl+F:` line — a short string copied from the PDF's own text layer (what Ctrl+F actually searches), so it hits even where the readable quote differs from the PDF internals (ligature splits, lost hyphens). Open the PDF, search the Ctrl+F string, and read the passage on the stated page. Where no reliable string exists in the text layer (tables, broken extraction), the line says so instead of offering a string that might miss.

Quotes: 1019 · ✓ 894 · ⚠ 125 · ✗ 0

## Start here — flagged studies

- **S08** — tension on country_region: Coded country_region says 'multi-market (market composition not explicit)', but this limitation sentence explicitly states US publicly listed firms only (consistent with CRSP stock data and S&P domestic credit ratings). Consider recoding to USA.; row check: One tension: country_region coded 'multi-market (announcements via Factiva; market composition not explicit)', but the limitations section (p. 13) states 'the sample is limited to only U.S. publicly listed firms', and stock data come from CRSP with S&P domestic credit ratings - the paper is explicit after all; consider recoding to USA. Everything else verifies cleanly (S08 was a spot-check row: event study / performance / negative confirmed). ca_measure empty confirmed - only market value is measured; 'competitive edges' appears once as survey background rhetoric on p. 1.
- **S15** — tension on effect_direction, key_finding: The model contains no direct AIPRM->firm-performance path: AIPRM reaches FP only via the mediators partner engagement (H4/H6) and information processing (H5/H7), and SC only via FP (H8). Under the frozen 'no direct path modeled' precedent (S21, S28) this pattern could argue for conditional; unlike those cases, however, every path here is positive and significant, which supports the final coding of positive with the prerequisites recorded in conditions.; row check: All non-empty columns evidenced. Two points for the author: (1) tension flagged on the effect_direction quote — the structural model has no direct AIPRM->performance path (serial mediation via partner engagement and information processing, Table 6 p.12), which resembles the S21/S28 'no direct path modeled -> conditional' precedent, though here all eight paths are positive and significant; relatedly, the mediators FPE/FIP are not listed in conditions (only the three prerequisites are). (2) method = mixed rests on Section 3.1 (p.6): the interview stage 'critically examin[ed] the study's hypotheses' with 'widespread agreement', i.e., it carried some evidential weight beyond instrument piloting — consistent with the mixed coding under the case law, but worth a look since the pilot-phase wording also mentions questionnaire refinement. Cross-industry is additionally supported by Table 3 (p.10): IT services and consulting, logistics, finance and banking, manufacturing.
- **S16** — tension on performance_measure, ca_measure: Performance scale is anchored relative to competitors; under S05 case law relative-vs-competitor scales are CA boundary cases. Construct is named 'Performance' with no CA hypothesis, so performance/ca_measure-empty follows the frozen rule, but the author may want to see this anchor.; row check: (1) industry coded 'food manufacturing', but the sample is food franchises and chain stores (fast food, coffee shops, restaurants, beverages, food sales, Table 1) — food service rather than manufacturing; author should confirm the label. (2) Lens coded '(no grand theory)' although the paper explicitly invokes RBV in hypothesis development (pp. 2-3) and discussion (p. 9); lens content (marketing capabilities / market orientation) itself is well evidenced. (3) Performance scale is competitor-anchored (see tension quote); ca_measure = empty remains consistent with the frozen rules. (4) The 'Fredrich-relevant detail lives in conditions column' part of quality_notes is coder commentary, not source-based — no quote possible.
- **S21** — tension on country_region, sample: Coded country_region is 'USA' and sample says '107 US executives', but the paper's data come from firms in France (68.2%) and the UK (31.8%) via a European panel; only the first author's affiliation is US (Baylor). Coded value contradicts the full text.; row check: country_region ('USA') and the 'US executives' phrase in sample contradict the paper: data were collected from firms in France (68.2%) and the UK (31.8%) via a European market-research panel (population: AI-adopting firms in Europe); possibly confused with the authors' US affiliation or with S29. Everything else checks out. Minor: coded conditions report the automation x hostility interaction as -0.23*, Table 6 shows -0.23**. Note: footnote 5 reports supplementary direct AI->outcome effects (analytics 0.44*** on performance) outside the main model; the adjudicated 'no direct AI->performance paths modeled' refers to the hypothesized structural model and stands. Quality-note element 'effect highly environment-selective' is coder commentary summarizing the 10/18 result (quoted).
- **S26** — tension on ai_measure, quality_notes: Coded ai_measure reads 'venture-capital funding received', but the measure is COUNTRY-level VC investment matched to firms by country of incorporation, not funding the firm itself received.; tension on ai_measure: Coded ai_measure lists 'AI job intensity' as a robustness proxy; the paper's robustness proxies are AI_NUM, AI_INT (investment intensity) and patent filings — no job-based measure is used.; tension on conditions: The paper identifies firm size as an additional moderator (U-shape and AI x R&D significant only for small/medium firms, null for large firms) — not listed in the coded conditions.; tension on theoretical_lens: Coded theoretical_lens is 'none explicit (entrepreneurship/innovation economics)', but the paper states an explicit RBT + Dynamic Capabilities framework (Section 2.2) and claims contributions to both.; tension on theoretical_lens: Same as above: coded lens 'none explicit' conflicts with the paper's explicit RBT/DCT framing.; row check: Three points for the author: (1) theoretical_lens coded 'none explicit' although the paper has an explicit RBT + DCT framework (Section 2.2, Section 5.1); (2) ai_measure details: the VC funding proxy is country-level (matched by country of incorporation), not funding 'received' by the firm, and the robustness proxy is AI investment intensity/patents, not 'AI job intensity'; (3) coded conditions omit the firm-size moderator (effects significant only for small/medium firms). ca_measure emptiness confirmed — competitive advantage appears only as RBT framing/conclusion rhetoric, no CA construct is measured. quality_notes part 'investment timing as condition - direct RQ fit' is coder commentary, not source-based; 'IV + clustering robustness' is evidenced. Adjudicated direction=conditional (U-shape sign flip) left untouched per case law.
- **S30** — row check: All columns evidenced and the adjudication fact-gap resolution (India, 1,487 invited, waves 437/408) matches the text. One wording point for the author: the coded conditions clause 'narcissism moderates adoption-factor relationships and GAI effects on competitive positioning' mirrors the paper's abstract, but Table 5 locates the significant moderation on the firm-performance side - NIM x IAI -> FCE is significant in both waves (-0.178 t1, +0.152 t2) and NIM x CGE -> FCE in t2 only, while NIM x IAI -> CGE (competitive positioning) stays non-significant (p = .075) in both waves; no interactions with the TOE adoption factors themselves were tested. Consider tightening the clause to 'narcissism moderates how adoption translates into firm performance'. Direction 'positive' is unaffected (H4/H5 positive and significant in both waves; moderators belong in conditions).
- **S36** — row check: (1) ca_measure empty is correct: competitive advantage appears only as framing (p.14 'This survey confirms that AI is beneficial and provides a competitive advantage to companies') with no measured CA construct — adjudicated as performance, no tension. (2) quality_notes 'small adopter sample (n=50)' is coder commentary; n=50 itself is documented (p.5 quote). (3) Author may want to look at method label 'panel econometrics': the paper runs OLS on a single 2017 baseline cross-section of Compustat data (p.5: 'the baseline for performance analysis is only available in 2017'), not a panel estimation — the archival-econometrics bucket fits, the literal 'panel' does not.
- **S39** — tension on effect_direction, conditions: The model contains no direct AI-to-performance path (only H1 AI->agility and H3 agility->performance): the performance effect exists only via the mediator, the pattern that S21/S28 precedent coded 'conditional'. Coded 'positive' follows the documented mediated-positive harmonization (every link positive, no null channel) - author should confirm.; row check: (1) effect_direction tension flagged: no direct AI->performance path is modeled; the effect runs entirely through marketing agility (all links positive, bivariate AI-FP correlation 0.326**, Table 4). Structurally this mirrors S21/S28 (coded conditional), while the mediated-positive harmonization rule supports 'positive' - author's call. (2) theoretical_lens: paper self-declares stakeholder theory + knowledge-based theory (sec. 2.4); the coded 'dynamic capabilities / marketing agility' captures the capability framing but not the paper's named theories. (3) ca_measure empty is correct: the competitor-relative item is part of the Jaworski/Kohli firm-performance scale, no distinct CA construct or hypothesis. (4) H2 (turbulence moderating AI->agility) is only 'partially supported' (CI includes zero, Table 6); coded conditions summarize amplification across both links - fine but worth knowing.
- **S42** — row check: Three items for the author: (1) theoretical_lens - the paper's self-declared primary framework is signaling theory (own section 2.3, 'initial effort to apply signaling theory'); the coded 'expectation (dis)confirmation / IS failure literature' is supportable from the failure definition and hypothesis grounding but omits signaling theory. (2) conditions - the paper also identifies an industry-type moderator (technology firms hit harder, H2 partially supported at the [0,1] window) which is not in the coded conditions. (3) ca_measure empty is correct ('loss of competitive advantage' appears only as an unmeasured intangible-cost example); the 'SAMPLE-CHECK OK' part of quality_notes is process commentary, not source-based.
- **S43** — tension on conditions: The paper is internally inconsistent: this Figure 2 caption calls ESCC compensatory (stronger BDAI effect at LOW ESCC), while the abstract and Table 5 (conditional indirect effects rising 0.06 -> 0.10 -> 0.13 with higher ESCC) say strengthening - the coded 'strengthens the indirect effect' follows the abstract/Table 5, but the author should see this contradiction.; row check: Two items: (1) The quality_notes caveat says the direct-path row is 'not explicit in text' - but Table 4 (PDF p. 8) does list row 5 'The direct effect of BDAI assimilation on NPP' = 0.16, p < 0.05, 95% CI [0.01, 0.31], i.e. a significant direct path; this strengthens the adjudicated 'positive' (partial, not full, mediation) and the caveat could be updated. (2) Figure 2 caption contradiction on the ESCC moderation direction (see tension on the Figure 2 quote). ca_measure empty is correct: 'competitive advantage' appears only in DCT framing, no CA construct is measured.
- **S44** — tension on effect_direction, conditions, quality_notes: effect_direction is coded 'conditional', but the paper reports a clear, significant average positive main effect that is robust across endogeneity tests, alternative measures and subsamples (conclusion: 'strong evidence that AI investment positively impacts firm growth'). Under the frozen main-effect rule this reads as 'positive' with labour-market moderators in conditions; the row was not among the adjudicated disputes, so the author should re-check.; tension on theoretical_lens: theoretical_lens is coded 'none explicit (labour economics framing)', but the paper explicitly develops a resource-based (RBV) framework - see also section 2.1. The 'none explicit' label looks factually wrong; author should re-check.; row check: Three items: (1) theoretical_lens 'none explicit' conflicts with the paper's explicit RBV framework (tensions on quotes 2-3). (2) effect_direction 'conditional' vs the paper's robust significant positive average main effect (tension on the baseline-result quote); this row was not in adjudication_briefs.md, so it never went through individual adjudication. (3) The paper is internally muddled on moderation direction: H2/H3 predict labour share/cost weaken the AI-growth link (as coded), but Table 5 reports significantly POSITIVE interaction terms for all three labour conditions and still claims support for H2-H4 - the coded 'weaken' follows the abstract and the Table 4 direct effects, not Table 5. ca_measure empty is correct: competitive-advantage/VRIN talk is theory framing only, no CA construct is measured.
- **S49** — row check: One sample detail could not be evidenced from this document: 'A-share listed firms' is never stated verbatim in the executed paper - the data section defers to the pre-registered report (Bai and Zhao, 2025) for full sample details; the loaded text gives 25,746 firm-year observations, 2011-2024, Chinese firms in/outside AI pilot zones. Also, industry = 'cross-industry (listed firms)' is supported only indirectly (industry fixed effects over the full firm panel). The '(highest identification quality in corpus)' part of quality_notes is coder commentary; the source-based parts (pre-registered, quasi-experiment) are quoted. ca_measure empty confirmed - no CA construct anywhere in the paper.
- **S56** — row check: Coded effect_direction = positive is supported by the full text (total effect 0.588***, direct path with mediators still 0.314*** - partial mediation, positive per the main-effect rule), BUT the row's own quality_notes cell says 'Gemini re-run: FULL AGREEMENT survey-SEM/competitive_advantage/conditional', which contradicts the final 'positive' on its face - likely a stale process note from before the mediated-positive harmonization; author should reword it. Rest of quality_notes is process commentary (PDF re-download); 'perceptual cross-section' is backed by the 7-point-Likert survey design. performance_measure empty confirmed: the financial indicators (EBIT, ROI, ROS vs. industry averages) are items INSIDE the CA construct, no standalone performance outcome.
- **S60** — tension on outcome_construct, performance_measure, ca_measure: Growth scale is anchored 'relative to key competitors' - a competitor-comparative wording that is a boundary case under the S05 relative-performance rule. The construct itself is firm economic growth (no distinct CA construct, scale, or CA hypothesis), so outcome_construct = performance and empty ca_measure follow the frozen rule; flagged only so the author sees the anchor.; row check: Two things to look at, neither a rule violation: (1) the firm-growth scale is anchored 'relative to key competitors' (p.4) - see the tension note; performance coding follows the frozen rule because the construct is growth, not a distinct CA construct. (2) Direction adjudication confirmed in the full text: direct effect on growth γ=.15* and the AI->productivity slope stays significant even at low regulatory support (.18*, Table 4 Panel B), so moderation of strength, not existence. The second half of quality_notes ('PROPOSED(batch)...') is adjudication commentary, not source-based, and is deliberately not quote-evidenced.
- **S61** — tension on key_finding: The coded key_finding lists infrastructure among the positive drivers, following this abstract claim - but the paper's own Table 1 (p.10) reports the ITI -> adoption-intention estimate as negative (-0.142, p = 0.020, still labeled 'Supported'), and the discussion admits 'the undesirable correlation between ITI and adoption intention' (p.13). Paper-internal inconsistency the author should see before citing infrastructure as a positive driver.; row check: Three notes: (1) key_finding tension - the abstract (and conclusion) claim IT infrastructure as a positive adoption driver, but Table 1's ITI estimate is negative (-0.142, p=0.020) and the discussion calls it an 'undesirable correlation' (p.13); PU and TMS paths are not supported either. The coded sentence mirrors the abstract, but the author should know the paper is internally inconsistent on the infrastructure driver. (2) ai_measure nuance: the measured construct is intention for the adoption of AI (IAAI, survey scale after Chatterjee et al. 2021), i.e. adoption intention rather than realized adoption; SP is likewise expectation-worded. (3) Emptiness confirmed: conditions correctly empty (TAM/TOE factors are adoption antecedents per the adjudicated decision, no moderators/mediators on IAAI->SP); ca_measure correctly empty ('competitive advantage' appears only as implications rhetoric, e.g. 'competitive advantage entrenchment' p.1, no CA construct measured). The 'PROPOSED(batch)' half of quality_notes is adjudication commentary, not source-based, and is deliberately not quote-evidenced.
- **S66** — tension on sample: Methods report 419 valid questionnaires from 290 firms, while the abstract (and the coded sample '419 manufacturing firms') treats 419 as the number of firms - the paper is internally inconsistent; coded cell follows the abstract.; row check: One factual discrepancy for the author: the coded sample '419 manufacturing firms' follows the abstract, but the methods section states 419 valid questionnaires from 290 firms (38% response rate) - the paper is internally inconsistent; consider annotating the sample cell as '419 responses / 290 firms'. Everything else checks out. ca_measure empty is correct: 'sustainable competitive advantage' appears only as closing rhetoric, no CA construct measured. effect_direction = positive holds under the mediation rule: the model reports a strong positive AI-to-OP path (0.719) alongside significant indirect effects, so the mediators stay in conditions. 'LSTM validation gimmick' is coder phrasing, but the underlying concern is source-backed (RMSE degradation in testing).

## S01 — Wamba-Taguimdje S.L. et al. (2020) — Business Process Management Journal (AJG 2)

DOI: 10.1108/BPMJ-10-2019-0411 · status: final · PDF: `WambaTaguimdje_2020_BPMJ-10-2019-0411.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | multi-country |
| sample | ~500 vendor-published AI project mini-cases (IBM, AWS, Cloudera, Nvidia etc.), archival qualitative analysis |
| method | case study |
| ai_measure | case observation (AI-based transformation projects from vendor websites) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | organizational performance (financial, marketing, administrative) + process-level performance, qualitative |
| ca_measure | — |
| effect_direction | conditional |
| conditions | process reconfiguration required (mechanism: performance gains only when AI features are used to reconfigure processes); AI as configuration of complements (data, talent, domain knowledge, partnerships, infrastructure) |
| key_finding | AI transformation projects improve organizational and process performance, but only when firms use AI to reconfigure their processes rather than overlay it on existing ones. |
| *not printed (coding data only)* | |
| theoretical_lens | IT capabilities + process-oriented perspective (Mooney et al.) + RBV/dynamic capabilities |
| industry | cross-industry |
| quality_notes | Vendor success-story mini-cases; authors themselves note possible bias: "exaggerated claims" (p. 20). Code as low-rigor qualitative evidence |
| coding_status | final |

### Evidence

1. **country_region, industry** — p. 1906 (PDF p. 14) — ✓ verified, 100% word sequence
   > Abu Dhabi National Oil Company (ADNOC) is a major diversified group of energy and petrochemical companies in Abu Dhabi.
   Ctrl+F: „Abu Dhabi National Oil Company (ADNOC) is a“
   → Example case firm in the UAE oil/petrochemical sector, evidencing multi-country and cross-industry coverage.

2. **country_region, industry** — p. 1908 (PDF p. 16) — ✓ verified, 100% word sequence
   > United Healthcare Services (UHS), which operates in the healthcare industry sector, is a regional not-for-profit network of hospitals in the state of New York, USA
   Ctrl+F: „United Healthcare Services (UHS), which operates in the“
   → Second example case firm in US healthcare, evidencing multi-country and cross-industry coverage.

3. **sample, method** — p. 1914 (PDF p. 22) — ✓ verified, 100% word sequence
   > in this study, which focused on analyzing the influence of AI on organizational performance, we adopted a qualitative approach based on the analysis of 500 case studies
   Ctrl+F: „in this study, which focused on analyzing the“
   → States the qualitative case-study design and the 500-case sample, backing method = case study.

4. **sample, ai_measure** — p. 1904 (PDF p. 12) — ✓ verified, 100% word sequence
   > we collected five hundred (500) mini-case studies published by approved and world-renowned AI solution providers in their different websites
   Ctrl+F: „we collected five hundred (500) mini-case studies published“
   → Documents the ~500 vendor-published mini-cases from AI solution providers' websites, backing sample and the case-observation AI measure.

5. **sample, ai_measure** — p. 1893 (PDF p. 1) — ✓ verified, 100% word sequence
   > The research process (responding to the research question, making discussions, interpretations and comparisons, and formulating recommendations) was based on a review of 500 case studies from IBM, AWS, Cloudera, Nvidia, Conversica, Universal Robots websites, etc.
   Ctrl+F: „(responding to the research question, making discussions, interpretations“
   → Names the vendor sources (IBM, AWS, Cloudera, Nvidia etc.) listed in the coded sample and ai_measure.

6. **outcome_construct, performance_measure** — p. 1893 (PDF p. 1) — ✓ verified, 100% word sequence
   > the results of our study have highlighted such AI benefits in organizations, and more specifically, its ability to improve on performance at both the organizational (financial, marketing and administrative) and process levels.
   Ctrl+F: „highlighted such AI benefits in organizations, and more“
   → Outcome is organizational performance (financial, marketing, administrative) plus process-level performance — exactly the coded performance_measure; no CA construct measured.

7. **outcome_construct, ca_measure** — p. 1902 (PDF p. 10) — ✓ verified, 100% word sequence
   > In organizations, performance improvement at the process level is usually measured using key performance indicators concerned with efficiency, capacity, productivity, quality, profitability, competitiveness, effectiveness, and value
   Ctrl+F: „In organizations, performance improvement at the process level“
   → Shows 'competitiveness' appears only as one KPI word in a list — no distinct CA construct is measured, confirming the empty ca_measure and outcome_construct = performance (per adjudication brief).

8. **effect_direction, conditions, key_finding** — p. 1893 (PDF p. 1) — ✓ verified, 100% word sequence
   > The same results also showed that organizations achieve performance through AI capabilities only when they use their features/technologies to reconfigure their processes.
   Ctrl+F: „results also showed that organizations achieve performance through“
   → Central result: performance gains only under process reconfiguration — backs effect_direction = conditional, the coded condition, and the key_finding.

9. **conditions** — p. 1894 (PDF p. 2) — ✓ verified, 100% word sequence
   > multiple key elements must be brought together to ensure the success of AI: data, talent mix, domain knowledge, key decisions, external partnerships and scalable infrastructure.
   Ctrl+F: „must be brought together to ensure the success“
   → Names the configuration of complements coded under conditions (data, talent, domain knowledge, partnerships, infrastructure).

10. **theoretical_lens** — p. 1893 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study has called on the theory of IT capabilities to seize the influence of AI business value on firm performance (at the organizational and process levels).
   Ctrl+F: „This study has called on the theory of“
   → Names IT capabilities theory as the framework, matching the coded lens.

11. **theoretical_lens** — p. 1904 (PDF p. 12) — ⚠ not machine-confirmed on page — open the page, 59% word sequence
   > They included Paradox Productivity (Kijek and Kijek, 2019; Pol  ak, 2017; Triplett, 1999), Process-Oriented Perspective (Mooney et al. , 1996), ResourceBased View (Barney et al. , 2001; Grant, 1991), and Dynamics Capabilities (Kim et al.
   Ctrl+F: „2017; Triplett, 1999), Process-Oriented Perspective (Mooney et al.,“
   → Lists the paper's theoretical foundations: Mooney process-oriented perspective, RBV, and dynamic capabilities, as coded.

12. **industry** — p. 1913 (PDF p. 21) — ✓ verified, 100% word sequence
   > this study has met the challenge of investigating at the same time the use of several AI technologies in several sectors of activity
   Ctrl+F: „investigating at the same time the use of“
   → Authors' own statement that the study spans several sectors, backing industry = cross-industry.

13. **quality_notes** — p. 1912 (PDF p. 20) — ✓ verified, 100% word sequence
   > there may have been an element of bias in the data contained in the cases, such as exaggerated claims or even restrictions on published data.
   Ctrl+F: „there may have been an element of bias“
   → Authors' own limitation admission ('exaggerated claims') quoted in the coded quality_notes.

*Row check OK: All non-empty columns evidenced. The quality_notes clause 'Code as low-rigor qualitative evidence' is coder commentary (Arthur's screening decision), not source-based; the source-based part ('exaggerated claims', p. 20) is evidenced. ca_measure emptiness confirmed — 'competitiveness' occurs only as a KPI list word and in framing rhetoric, never as a measured construct.*

---

## S02 — Baabdullah A.M. et al. (2021) — Industrial Marketing Management (AJG 3)

DOI: 10.1016/j.indmarman.2021.09.003 · status: final · PDF: `Baabdullah_2021_j-indmarman-2021-09-003.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Saudi Arabia |
| sample | 392 B2B SMEs, cross-section, CB-SEM |
| method | survey-SEM |
| ai_measure | survey construct (acceptance of AI practices) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | perceived SME performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | technology roadmapping (enabler, sig.); attitude (sig.); infrastructure readiness (sig.); awareness (sig.); professional expertise and technicality NOT significant |
| key_finding | Acceptance of AI practices improves perceived SME performance; adoption is driven by roadmapping, attitude, infrastructure and awareness - not by professional expertise. |
| *not printed (coding data only)* | |
| theoretical_lens | TOE |
| industry | cross-industry (B2B SMEs) |
| quality_notes | Perceptual self-report, cross-sectional |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 262 (PDF p. 8) — ✓ verified, 100% word sequence
   > The target population was B2B SME CEOs, CIOs, general managers, senior managers, marketing managers, and owners in Saudi Arabia.
   Ctrl+F: „The target population was B2B SME CEOs, CIOs,“
   → Sample located in Saudi Arabia, backing country_region.

2. **sample, method** — p. 255 (PDF p. 1) — ✓ verified, 100% word sequence
   > The conceptual model was tested using structural equation modelling of survey data collected from B2B SMEs ( n = 392).
   Ctrl+F: „model was tested using structural equation modelling of“
   → States survey design, SEM analysis, and n = 392 B2B SMEs — backing method = survey-SEM and the coded sample.

3. **sample, method** — p. 262 (PDF p. 8) — ✓ verified, 100% word sequence
   > confirmatory factor analysis was conducted in AMOS using Maximum Likelihood Estimation, which was then followed by path analysis of the structural relationships.
   Ctrl+F: „conducted in AMOS using Maximum Likelihood Estimation, which“
   → AMOS with ML estimation evidences covariance-based SEM (CB-SEM) as noted in the sample column.

4. **ai_measure** — p. 260 (PDF p. 6) — ✓ verified, 100% word sequence
   > The extent of acceptance of AI applications by SMEs.
   Ctrl+F: „The extent of acceptance of AI“
   → Table 2 definition of the focal construct 'SMEs' AI practices', backing ai_measure = survey construct (acceptance of AI practices).

5. **outcome_construct, effect_direction, key_finding** — p. 264 (PDF p. 10) — ✓ verified, 100% word sequence
   > Both dimensions of business performance, financial ( γ = 0.709, p < 0.000) and non-financial ( γ = 0.681, p < 0.000) performance, were also found to be significantly predicted by the role of SMEs' AI practices.
   Ctrl+F: „predicted by the role of SMEs' AI“
   → Significant positive paths from AI practices to financial and non-financial performance — backs effect_direction = positive and outcome_construct = performance.

6. **performance_measure** — p. 260 (PDF p. 6) — ✓ verified, 100% word sequence
   > The financial results of AI integration that can be quantitatively measured such as profitability, sales volume, and return on investment.
   Ctrl+F: „integration that can be“
   → Definition of the financial-performance survey construct, backing the perceived SME performance (survey scale) measure.

7. **performance_measure, quality_notes** — p. 262 (PDF p. 8) — ✓ verified, 100% word sequence
   > Items were measured using a five-point Likert scale anchored 1 strongly disagree to 5 strongly agree
   Ctrl+F: „were measured using a five-point Likert scale anchored“
   → Performance measured by Likert self-report scales — backs 'perceived' performance_measure and the perceptual self-report quality note.

8. **ca_measure** — p. 260 (PDF p. 6) — ✓ verified, 100% word sequence
   > The non-financial results of AI integration in terms of customer satisfaction, loyalty, and competitive advantage.
   Ctrl+F: „integration in terms of customer“
   → 'Competitive advantage' appears only as one facet inside the non-financial performance scale definition — no distinct CA construct with its own hypothesis is measured, confirming the empty ca_measure under the frozen decision rule.

9. **conditions, key_finding** — p. 255 (PDF p. 1) — ✓ verified, 68% word sequence
   > The results showed that, of the AI enablers, acceptance of AI practices was significantly influenced by both technology roadmapping and attitude but not professional expertise.
   Ctrl+F: „results showed that, of the AI enablers, acceptance“
   → Backs the coded conditions: roadmapping and attitude significant, professional expertise not significant.

10. **conditions, key_finding** — p. 255 (PDF p. 1) — ✓ verified, 100% word sequence
   > Of the AI readiness variables, acceptance of AI practices was significantly influenced by infrastructure and awareness but not technicality.
   Ctrl+F: „Of the AI readiness variables, acceptance of AI“
   → Backs the coded conditions: infrastructure and awareness significant, technicality not significant.

11. **conditions** — p. 264 (PDF p. 10) — ✓ verified, 100% word sequence
   > As for the main P.AI antecedents, awareness was the most influential factor contributing to SMEs' AI practices ( γ = 0.452, p < 0.000), followed by technology roadmapping ( γ = 0.228, p < 0.000).
   Ctrl+F: „the main P.AI antecedents, awareness was the most“
   → Coefficient-level evidence for the significant enabler/readiness conditions in the coded row.

12. **key_finding** — p. 255 (PDF p. 1) — ✓ verified, 100% word sequence
   > The acceptance of AI practices was found to significantly affect AI-enabled relational governance and performance, and SME's business customer AI-based interaction.
   Ctrl+F: „AI-enabled relational governance and performance, and SME's business“
   → The paper's own summary of its central result: AI acceptance improves performance, matching the coded key_finding.

13. **theoretical_lens** — p. 255 (PDF p. 1) — ✓ verified, 100% word sequence
   > A conceptual model based on the technology-organisation-environment framework is developed which considers the impact of AI enablers and AI readiness on the acceptance of AI practices
   Ctrl+F: „A conceptual model based on the technology-organisation-environment framework“
   → Names the TOE framework as the study's theoretical basis, matching the coded lens.

14. **industry** — p. 262 (PDF p. 8) — ⚠ not machine-confirmed on page — open the page, 33% word sequence
   > The targeted participants worked in wholesaling, manufacturing, agriculture, information technology and social media, and construction industries that provide services and products to business customers.
   Ctrl+F: „that provide services and products to business customers.“
   → Multiple industries in the sample, backing industry = cross-industry (B2B SMEs).

15. **quality_notes** — p. 266 (PDF p. 12) — ✓ verified, 100% word sequence
   > First, this study is cross-sectional
   Ctrl+F: „this study is cross-sectional,“
   → Authors' own limitation statement backing the 'cross-sectional' quality note (sentence continues onto the next PDF page).

*Row check OK: All non-empty columns evidenced. ca_measure emptiness confirmed: competitive advantage occurs only as one item/facet of the non-financial performance scale (Table 2 and appendix item N.F1), not as a distinct validated CA construct with its own hypothesis — consistent with the frozen rule. Note: outcome variables are consequences 'of acceptance of AI practices' rated perceptually, matching 'perceived SME performance'.*

---

## S03 — Chatterjee S. et al. (2021) — Industrial Marketing Management (AJG 3)

DOI: 10.1016/j.indmarman.2021.07.013 · status: final · PDF: `Chatterjee_2021_j-indmarman-2021-07-013.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India |
| sample | 349 managers from 16 BSE-listed firms (11 manufacturing, 5 service), response rate 51.6%, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI-CRM implementation) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | perceived organizational performance (survey scale) |
| ca_measure | competitive advantage scale (COA1-3, Rogers-based; incl. market-share gain), discriminant-valid vs OP; predicted BY performance (H4: 0.59***, R2=.76) |
| effect_direction | positive |
| conditions | mediators: B2B engagement, employee experience, information processing capability (all sig.); moderator: leadership support (H5/H6 sig., MGA); firm size/age/industry only CONTROLS (not moderators) |
| key_finding | AI-CRM implementation improves perceived organizational performance and competitive advantage in B2B relationship management. |
| *not printed (coding data only)* | |
| theoretical_lens | institutional theory + RBV |
| industry | manufacturing + service (B2B) |
| quality_notes | Perceptual survey; 16-firm cluster behind 349 respondents; COA items partly adoption-flavored (COA1: edge over non-adopters) \| SAMPLE-CHECK OK: fully verified in one-by-one adjudication (full read) |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 210 (PDF p. 6) — ⚠ not machine-confirmed on page — open the page, 56% word sequence
   > This study randomly selected 39 manufacturing and service organizations from Bombay Stock Exchange (Mumbai, India) for data collection.
   Ctrl+F: „This study randomly selected 39 manufacturing and service“
   → BSE-listed manufacturing and service firms in India — backs country_region = India, industry, and the BSE-listed sample description.

2. **sample, method** — p. 210 (PDF p. 6) — ✓ verified, 100% word sequence
   > Partial least squares structural equation modelling (PLS-SEM) analysis was undertaken for 349 responses for a total of 36 questions.
   Ctrl+F: „least squares structural equation modelling (PLS-SEM) analysis was“
   → PLS-SEM on 349 usable responses — backs method = survey-SEM and the coded n and PLS-SEM note in sample.

3. **sample** — p. 210 (PDF p. 6) — ✓ verified, 100% word sequence
   > Eventually, 366 replies were obtained within the time with a response rate of 51.6%.
   Ctrl+F: „the time with a response rate of 51.6%.“
   → Backs the coded response rate of 51.6%.

4. **sample, quality_notes** — p. 210 (PDF p. 6) — ✓ verified, 100% word sequence
   > With such persuasion, eventually top executives of 16 organizations allowed their managers to participate in the survey.
   Ctrl+F: „persuasion, eventually top executives of 16 organizations allowed“
   → Backs the 16-firm cluster behind the 349 respondents (sample and quality note).

5. **ai_measure, conditions** — p. 208 (PDF p. 4) — ✓ verified, 100% word sequence
   > Implementation of AI-CRM for B2B relationship management significantly and positively impacts the B2B engagements.
   Ctrl+F: „Implementation of AI-CRM for B2B relationship management“
   → H2a: implementation of AI-CRM is the focal survey construct (ai_measure) and B2B engagement is a coded mediator path.

6. **outcome_construct, ca_measure, effect_direction** — p. 212 (PDF p. 8) — ✓ verified, 100% word sequence
   > The influence of OP on COA (H4) is significant as the concerned path coefficient is 0.59 with level of significance p < 0.001.
   Ctrl+F: „The influence of OP on COA (H4) is“
   → H4 result (0.59***): CA is measured as its own construct predicted by performance — backs ca_measure, outcome_construct = both, and positive direction.

7. **outcome_construct, key_finding** — p. 214 (PDF p. 10) — ✓ verified, 100% word sequence
   > This study integrated institutional theory and the RBV and developed a model showing how successful implementation of AI-CRM in B2B relationship management could impact organizations' performance and ultimately their competitive advantage.
   Ctrl+F: „This study integrated institutional theory and the RBV“
   → The paper's own conclusion of its central result — AI-CRM improves performance and competitive advantage, matching key_finding and outcome_construct = both.

8. **performance_measure, quality_notes** — p. 215 (PDF p. 11) — ✓ verified, 100% word sequence
   > I believe that successful implementation of AI-CRM will help the organization to improve its operational efficiency.
   Ctrl+F: „I believe that successful implementation of AI-CRM will“
   → OP1 item — performance is a perceptual survey scale ('I believe...'), backing performance_measure and the perceptual-survey quality note.

9. **ca_measure** — p. 209 (PDF p. 5) — ✓ verified, 100% word sequence
   > Competitive advantage is the degree to which the performance of an organization working in the B2B context could achieve greater benefits compared to other organizations functioning in similar conditions (Rogers, 1983, 1985).
   Ctrl+F: „the performance of an organization working in the“
   → Rogers-based definition of the distinct competitive-advantage construct, backing the coded 'Rogers-based' CA scale.

10. **ca_measure** — p. 212 (PDF p. 8) — ✓ verified, 100% word sequence
   > Moreover, the COA is explained by OP to the tune of 76%, which is the overall predictive power of the model.
   Ctrl+F: „Moreover, the COA is explained by OP to“
   → Backs the R2 = .76 recorded in the coded ca_measure.

11. **ca_measure, quality_notes** — p. 215 (PDF p. 11) — ✓ verified, 100% word sequence
   > I think that successful implementation of AI-CRM will help an organization to win over its competitor which has not yet implemented AI-CRM for B2B relationship management.
   Ctrl+F: „I think that successful implementation of AI-CRM will“
   → COA1 item text — evidences the COA1-3 scale and the quality note that COA1 is adoption-flavored (edge over non-adopters).

12. **ca_measure** — p. 215 (PDF p. 11) — ✓ verified, 100% word sequence
   > I believe that AI-CRM for B2B relationship management has helped our firm to increase market share.
   Ctrl+F: „I believe that AI-CRM for B2B relationship management“
   → COA3 item — backs 'incl. market-share gain' in the coded ca_measure.

13. **ca_measure** — p. 210 (PDF p. 6) — ✓ verified, 100% word sequence
   > Evaluation of discriminant validity as depicted in Table 3 reveals that square root of AVE shown in bold fonts across the diagonal is always greater than the correlation value
   Ctrl+F: „depicted in Table 3 reveals that square root“
   → Backs 'discriminant-valid vs OP' in the coded ca_measure (COA passes the Fornell-Larcker test against OP).

14. **effect_direction** — p. 216 (PDF p. 12) — ✓ verified, 100% word sequence
   > the path coefficient concerning the linkage IAB ➔ OP in the rival model appears to be 0.22 with level of significance * p < 0.05
   Ctrl+F: „rival model appears to be 0.22 with level“
   → Rival model shows a significant direct AI-CRM-to-performance effect — under the frozen rule a mediated-positive effect with significant direct effect codes as positive.

15. **conditions** — p. 212 (PDF p. 8) — ✓ verified, 100% word sequence
   > The mediating variables BE, EEB, and BIP have influence on OP (H3a, H3b, H3c) in conformity with RBV theory as presented in Table 4.
   Ctrl+F: „The mediating variables BE, EEB, and BIP have“
   → Backs the coded mediators: B2B engagement, employee experience, information processing capability (all significant).

16. **conditions** — p. 211 (PDF p. 7) — ✓ verified, 100% word sequence
   > This confirms that the effects of LS on H3a and on H3b are significant.
   Ctrl+F: „This confirms that the effects of LS on“
   → Backs the coded moderator: leadership support significant (H5/H6) via multi-group analysis.

17. **conditions** — p. 210 (PDF p. 6) — ✓ verified, 100% word sequence
   > In this study, we have considered organization size, organization age, and organization type as control variables for organization performance.
   Ctrl+F: „In this study, we have considered organization size,“
   → Backs the adjudicated note that firm size/age/industry are only controls, not moderators.

18. **theoretical_lens** — p. 205 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study combines institutional theory and the resource-based view (RBV) in B2B relationship management to understand how AI-CRM could impact the firm's performance with varied firm size, firm age, and industry type.
   Ctrl+F: „This study combines institutional theory and the resource-based“
   → Names institutional theory + RBV as the combined theoretical lens, matching the coded value.

*Row check OK: All non-empty columns evidenced. The '11 manufacturing, 5 service' split in the coded sample comes from Table 1 (p. 6, Industry Type rows: Manufacturing 11 / Service 5) — table cells, not quotable prose. Quality note 'SAMPLE-CHECK OK...' is coder commentary, not source-based. Minor discrepancy inside the paper itself: text says predictive power 76% in results but 78% in the limitations section — coded value follows the results section (R2=.76).*

---

## S04 — Chatterjee S. et al. (2022) — Journal of Business Research (AJG 3)

DOI: 10.1016/j.jbusres.2022.06.033 · status: final · PDF: `Chatterjee_2022_j-jbusres-2022-06-033.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India |
| sample | 312 usable manager responses from 14 BSE-listed firms (10 large/4 SME; telecom, IT, automobile, retail, pharma), Jan-Feb 2020, RR 47.3%, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (adoption of AI-embedded CRM system) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm performance scale (market+financial criteria, ROI/ROA, sales growth, market share, profitability) + B2B relationship satisfaction |
| ca_measure | — |
| effect_direction | positive |
| conditions | technology turbulence (negative moderator on ADM->BRS -0.23* and OPE->BRS -0.32***); leadership support (positive moderator on BRS->FP 0.29*); main effect ACRM->FP 0.53*** unconditional |
| key_finding | AI-embedded CRM improves relationship satisfaction and firm performance; gains shrink under technology turbulence and grow with leadership support. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + dynamic capability view + status-quo-bias theory |
| industry | cross-industry (B2B) |
| quality_notes | Perceptual survey; 14-firm cluster; same author group as S03 - here deliberately NO CA construct |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 441 (PDF p. 5) — ✓ verified, 100% word sequence
   > To target potential respondents from the different Indian firms, a list of the firms was procured from the Bombay Stock Exchange (Mumbai, India).
   Ctrl+F: „To target potential respondents from the different Indian“
   → Indian BSE-listed firms — backs country_region = India and the BSE-listed sample description.

2. **sample, method, quality_notes** — p. 437 (PDF p. 1) — ✓ verified, 100% word sequence
   > The model was validated using the PLS-SEM technique with 312 responses from 14 firms in the B2B context.
   Ctrl+F: „PLS-SEM technique with 312 responses from 14 firms“
   → PLS-SEM survey with 312 responses from 14 firms — backs method = survey-SEM, the coded n, and the 14-firm-cluster quality note.

3. **sample** — p. 441 (PDF p. 5) — ✓ verified, 100% word sequence
   > Out of 14 firms, 10 firms were large, whereas four were small and medium firms.
   Ctrl+F: „Out of 14 firms, 10 firms were large,“
   → Backs the coded 10 large / 4 SME split.

4. **sample, industry** — p. 441 (PDF p. 5) — ✓ verified, 100% word sequence
   > four firms were from the telecommunication sector, three from the IT sector, two from the retail sector, two from the pharmaceutical sector, and three from the automobile sector
   Ctrl+F: „the telecommunication sector, three from the IT sector,“
   → Backs the coded industry mix (telecom, IT, retail, pharma, automobile) and industry = cross-industry (B2B).

5. **sample** — p. 441 (PDF p. 5) — ✓ verified, 100% word sequence
   > Ultimately, by the first week of March 2020, only 326 responses from the managers of several ranks at those 14 firms were obtained, which is a response rate of 47.3%.
   Ctrl+F: „Ultimately, by the first week of March 2020,“
   → Backs the coded response rate of 47.3% (326 raw responses; 312 usable after screening).

6. **sample** — p. 441 (PDF p. 5) — ✓ verified, 100% word sequence
   > They were provided with the questionnaire along with the instructions, and were asked to respond within two months, that is, January and February 2020.
   Ctrl+F: „They were provided with the questionnaire along with“
   → Backs the coded survey window Jan-Feb 2020.

7. **ai_measure** — p. 437 (PDF p. 1) — ✓ verified, 100% word sequence
   > The purpose of this study is to determine the impact of adopting a artificial intelligence-embedded customer relationship management (CRM) system for business-to-business relationship management.
   Ctrl+F: „The purpose of this study is to determine“
   → Adoption of an AI-embedded CRM system is the focal survey construct, matching the coded ai_measure ('a artificial' typo is in the original).

8. **outcome_construct, effect_direction, key_finding** — p. 437 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study finds that an AI-embedded CRM system has a significant positive impact towards B2B relationship satisfaction and firm performance.
   Ctrl+F: „CRM system has a significant positive impact towards“
   → Paper's own statement of its central result: significant positive effect on relationship satisfaction and firm performance — backs outcome = performance, direction = positive, and key_finding.

9. **performance_measure** — p. 440 (PDF p. 4) — ✓ verified, 64% word sequence
   > Firm performance is measured by the net outcomes, including consideration of both market and financial criteria, return on investments and assets, sales growth, market share, and overall profitability
   Ctrl+F: „Firm performance is measured by the net outcomes,“
   → Backs the coded performance_measure content (market+financial criteria, ROI/ROA, sales growth, market share, profitability).

10. **performance_measure** — p. 440 (PDF p. 4) — ✓ verified, 100% word sequence
   > Level of satisfaction in the B2B relationship is also a measure of firm performance
   Ctrl+F: „relationship is also a measure of firm performance“
   → Backs the '+ B2B relationship satisfaction' component of the coded performance_measure.

11. **performance_measure, quality_notes** — p. 447 (PDF p. 11) — ✓ verified, 100% word sequence
   > I believe that our sales growth has improved post AI-CRM implementation.
   Ctrl+F: „I believe that our sales growth has improved“
   → FP1 item shows performance is measured by perceptual self-report ('I believe...'), backing the perceptual-survey quality note.

12. **ca_measure** — p. 447 (PDF p. 11) — ✓ verified, 100% word sequence
   > Using AI-CRM system for B2B relationship management can help improve competitiveness of the firms.
   Ctrl+F: „Using AI-CRM system for B2B relationship management can“
   → FP3 item: 'competitiveness' appears only as one item inside the firm-performance scale — the model's five constructs (ADM, OPE, ACRM, BRS, FP) contain no distinct CA construct, confirming the empty ca_measure per adjudication.

13. **effect_direction, conditions** — p. 443 (PDF p. 7) — ✓ verified, 100% word sequence
   > The ACRM significantly and positively impacts FP (H3), with the path coefficient being 0.53, having a level of significance of p < 0.001 (***).
   Ctrl+F: „The ACRM significantly and positively impacts FP (H3),“
   → The unconditional main effect ACRM->FP 0.53*** recorded in conditions — a clear positive average main effect, backing effect_direction = positive per the frozen rule.

14. **conditions** — p. 443 (PDF p. 7) — ✓ verified, 100% word sequence
   > the results show that the effects of TT on the linkages covered by H1 and H2 are both negative, since the concerned path coefficients are 0.23, with a level of significance of p < 0.05
   Ctrl+F: „show that the effects of TT on the“
   → Technology turbulence as negative moderator on ADM->BRS (-0.23*); the sentence continues with 0.32 (p < 0.001) on OPE->BRS, matching the coded -0.32***.

15. **conditions** — p. 443 (PDF p. 7) — ✓ verified, 100% word sequence
   > However, the effects of the other moderator LS on the linkage H4 are positive and significant, as the concerned path coefficient is 0.29, with a significance level of p < 0.05 (*).
   Ctrl+F: „However, the effects of the other moderator LS“
   → Leadership support as positive moderator on BRS->FP (0.29*), matching the coded condition.

16. **theoretical_lens** — p. 439 (PDF p. 3) — ✓ verified, 100% word sequence
   > Thus, RBV theory, DCV, and SQB theory could help to identify the antecedents that could eventually impact the firm performance.
   Ctrl+F: „Thus, RBV theory, DCV, and SQB theory could“
   → Names all three coded lenses: RBV, dynamic capability view, and status-quo-bias theory.

17. **quality_notes** — p. 446 (PDF p. 10) — ✓ verified, 100% word sequence
   > The present study is based on the findings from analyzing cross-sectional data, which creates problems in establishing accurate causality between the constructs.
   Ctrl+F: „the findings from analyzing cross-sectional data, which creates“
   → Authors' own limitation admission supporting the perceptual/cross-sectional quality note.

*Row check OK: All non-empty columns evidenced. ca_measure emptiness confirmed: RBV competitive-advantage language appears only as theory framing (p. 2) and 'competitiveness' only as FP scale item FP3 — no distinct measured CA construct, consistent with the adjudicated outcome = performance. The quality-note clause 'same author group as S03' is coder commentary, not source-based.*

---

## S05 — Hossain M.A. et al. (2022) — Industrial Marketing Management (AJG 3)

DOI: 10.1016/j.indmarman.2022.08.017 · status: final · PDF: `Hossain_2022_j-indmarman-2022-08-017.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Bangladesh |
| sample | 257 usable manager responses (1,953 approached, 278 qualified), RMG export manufacturers, research-firm panel/Qualtrics, random sampling; time-lagged robustness subsample n=93 |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption on top of marketing analytics platform) |
| *Table A.2 columns* | |
| outcome_construct | competitive_advantage |
| performance_measure | — |
| ca_measure | sustained competitive advantage = RELATIVE performance vs competitors over last 3 years (market share growth, sales growth, profitability, ROI) - boundary case performance-as-CA, discuss in thesis |
| effect_direction | conditional |
| conditions | mediators: market sensing/seizing/reconfiguring (carry MAC->SCA fully, H3a-c); moderator: AI adoption strengthens MAC->sensing (0.104*), ->seizing (0.131*), ->reconfiguring (0.128*) |
| key_finding | Marketing analytics capability drives sensing/seizing/reconfiguring toward sustained competitive advantage; AI adoption amplifies this only when built on an analytics foundation. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities (sensing/seizing/reconfiguring) |
| industry | readymade garment (manufacturing, B2B export) |
| quality_notes | Multi-phase design but interviews/Delphi only developmental; perceptual measures with objective-data correlation check (r=0.67); AI is moderator, not focal predictor - note for coding discussion |
| coding_status | final |

### Evidence

1. **country_region, industry** — p. 243 (PDF p. 4) — ✓ verified, 100% word sequence
   > To authenticate the problem more precisely, the study considered a country -Bangladesh, which heavily relies on RMG manufacturing and export.
   Ctrl+F: „To authenticate the problem more precisely, the study“
   → Backs country_region = Bangladesh and the readymade-garment export-manufacturing industry setting.

2. **sample, method** — p. 248 (PDF p. 9) — ✓ verified, 100% word sequence
   > Qualtrics version of the questionnaire link was distributed via the research firm's database using the random sampling technique.
   Ctrl+F: „Qualtrics version of the questionnaire link was distributed“
   → Backs the coded research-firm panel/Qualtrics survey with random sampling.

3. **sample** — p. 248 (PDF p. 9) — ✓ verified, 100% word sequence
   > In total, 1953 managers were approached.
   Ctrl+F: „1953 managers were approached.“
   → Backs the coded 1,953 approached.

4. **sample** — p. 248 (PDF p. 9) — ✓ verified, 100% word sequence
   > 1675 managers were screened out in this process, and 278 managers were qualified for the final steps.
   Ctrl+F: „1675 managers were screened out in this“
   → Backs the coded 278 qualified.

5. **sample** — p. 248 (PDF p. 9) — ✓ verified, 100% word sequence
   > After investigating the odd cases, the authors finally considered 257 responses for data analysis.
   Ctrl+F: „After investigating the odd cases, the authors“
   → Backs the coded 257 usable responses (the n behind the PLS-SEM test).

6. **sample** — p. 249 (PDF p. 10) — ✓ verified, 100% word sequence
   > In study 5a, we were able to obtain data from a subsample of 93 participants three months after study 4 (response rate 31.3%).
   Ctrl+F: „In study 5a, we were able to obtain“
   → Backs the coded time-lagged robustness subsample n = 93.

7. **sample, industry** — p. 247 (PDF p. 8) — ✓ verified, 100% word sequence
   > the authors recruited one of the top research firms to collect data from managers of export-oriented RMG manufacturing
   Ctrl+F: „the authors recruited one of the top research“
   → Main survey population = export-oriented RMG manufacturers via a research firm, backing sample and industry.

8. **method, quality_notes** — p. 243 (PDF p. 4) — ✓ verified, 100% word sequence
   > Further, as part of study 1, in study 1b, interviews were conducted on 25 managers of manufacturing firms based on a judgemental sampling technique to verify the problem.
   Ctrl+F: „Further, as part of study 1, in study“
   → Interviews served only problem verification, not outcome evidence — backs the adjudicated method = survey-SEM (not mixed) and the 'interviews developmental' quality note.

9. **method, quality_notes** — p. 246 (PDF p. 7) — ✓ verified, 100% word sequence
   > Further, two Delphi studies were conducted to conceptualize the research model.
   Ctrl+F: „Further, two Delphi studies were conducted to conceptualize“
   → Delphi rounds only for model conceptualization — developmental, so the study is not mixed-method per the frozen method rule.

10. **method** — p. 248 (PDF p. 9) — ✓ verified, 100% word sequence
   > The PLS algorithm verifies the reliability of the model construction.
   Ctrl+F: „The PLS algorithm verifies the reliability of the“
   → PLS(-SEM) is the analysis technique, backing method = survey-SEM.

11. **ai_measure, conditions, quality_notes** — p. 246 (PDF p. 7) — ✓ verified, 100% word sequence
   > The adoption of artificial intelligence moderates the relationship between marketing analytics capability and (a) market sensing (b) market seizing and (c) market reconfiguring.
   Ctrl+F: „relationship between marketing analytics capability and (a) market“
   → H4a-c: AI adoption is modeled as moderator on the analytics platform, not the focal predictor — backs ai_measure, the coded moderator condition, and the quality note.

12. **ai_measure, effect_direction, conditions** — p. 249 (PDF p. 10) — ✓ verified, 100% word sequence
   > moderator findings show AI adoption moderates the relationship of MAC-MSN ( β = 0.104, p < 0.05), MAC-MSI ( β = 0.131, p < 0.05), and MAC-MRN ( β = 0.128, p < 0.05).
   Ctrl+F: „adoption moderates the relationship of MAC-MSN (β = 0.104, p“
   → Exact moderation coefficients coded in conditions (0.104*/0.131*/0.128*); effects operate only through the capability paths, supporting effect_direction = conditional.

13. **ai_measure, conditions, key_finding** — p. 240 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 25% word sequence
   > The performance of sensing, seizing, and reconfiguring becomes higher for a firm when they adopt AI on the strength of the marketing analytics platform.
   Ctrl+F: „when they adopt AI on the strength of“
   → Backs the key_finding clause that AI adoption amplifies the effect only on top of the analytics foundation, and the coded AI-as-moderator condition.

14. **outcome_construct, performance_measure, ca_measure** — p. 248 (PDF p. 9) — ✓ verified, 100% word sequence
   > Using market-centric analytics capacity, how well has your firm performed its _____________ goals relative to competitors in the last three years?
   Ctrl+F: „Using market-centric analytics capacity, how well has your“
   → SCA scale stem (Table 2): outcome measured as performance RELATIVE to competitors over the last three years — backs outcome_construct = competitive_advantage, the coded boundary-case ca_measure, and confirms performance_measure is correctly empty (no separate performance construct).

15. **outcome_construct, key_finding, quality_notes** — p. 240 (PDF p. 1) — ✓ verified, 100% word sequence
   > Utilizing multi-phase research design, the study reveals that firms marketing analytics capability play a vital role in sensing, seizing, and reconfiguring the market, consequently leading to a sustained competitive advantage.
   Ctrl+F: „marketing analytics capability play a vital role in“
   → Paper's own central result: MAC drives sensing/seizing/reconfiguring toward sustained competitive advantage; also evidences the multi-phase design noted in quality_notes.

16. **ca_measure** — p. 251 (PDF p. 12) — ✓ verified, 100% word sequence
   > These initiatives will anticipate enhancing market share growth, sales growth, profitability, and good return on investment to attain a sustained competitive advantage.
   Ctrl+F: „return on investment to attain a sustained competitive“
   → Names the four SCA indicators coded in ca_measure (market share growth, sales growth, profitability, ROI; items SCA1-SCA4 in Table 2).

17. **effect_direction, conditions** — p. 248–250 (PDF p. 9) — ✓ verified, 89% word sequence
   > the mediator analysis of MAC-MSN-SCA ( β = 0.243, p < 0.001), MAC-MSI-SCA ( β = 0.160, p < 0.01), and MAC-MRN-SCA ( β = 0.150, p < 0.01) confirms the significant effect.
   Ctrl+F: „0.160, p < 0.01), and MAC-MRN-SCA (β = 0.150, p < 0.01)“
   → Sensing/seizing/reconfiguring carry the MAC->SCA relationship (H3a-c); no direct MAC->SCA path is modeled — effect exists only via mechanism, backing effect_direction = conditional per the frozen rule.

18. **theoretical_lens** — p. 242 (PDF p. 3) — ⚠ not machine-confirmed on page — open the page, 53% word sequence
   > Teece (2007) explained and distinguished dynamic capabilities into three specific dimensions to sustain competitive advantage: (a) market sensing capacity to identify opportunities and threats; (b) market seizing capacity to grab those opportunities
   Ctrl+F: „advantage: (a) market sensing capacity to identify opportunities“
   → Backs the coded lens: dynamic capabilities specified as sensing/seizing/reconfiguring (sentence continues with the reconfiguring dimension).

19. **quality_notes** — p. 249 (PDF p. 10) — ✓ verified, 100% word sequence
   > we co-related the items ' Using market-centric analytics capacity, how well has your firm performed its market share growth goals ' with ' the percentage of market share growth ' generates a strong positive correlation ( r = 0.67)
   Ctrl+F: „growth goals” with “the percentage of market share“
   → Backs the quality note: perceptual measures cross-checked against near-objective data with r = 0.67.

20. **quality_notes** — p. 252 (PDF p. 13) — ✓ verified, 100% word sequence
   > The study analyzed self-reported managers ' data and matched responses with some close to factual information in the robustness test.
   Ctrl+F: „study analyzed self-reported managers’ data and matched responses“
   → Authors' own limitation admission backing the perceptual-measures quality note.

*Row check OK: All non-empty columns evidenced; performance_measure emptiness confirmed (the only outcome construct is the SCA scale; its relative-performance items are recorded inside ca_measure as the flagged boundary case, per S05 case law). Minor observation for the author: the paper frames its lens as 'the overarching theoretical lens of RBV and dynamic capability' (p. 4) while the coded lens names only dynamic capabilities — DC (sensing/seizing/reconfiguring) is clearly the operative theory, but RBV is co-named in the paper. Not a contradiction under the frozen rules, just wording.*

---

## S06 — Lee Y.S. et al. (2022) — Technovation (AJG 3)

DOI: 10.1016/j.technovation.2022.102590 · status: final · PDF: `Lee_2022_j-technovation-2022-102590.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | South Korea |
| sample | 160 high-tech ventures (from 1,248 ministry list, 300 responses), survey + audited financials |
| method | panel econometrics |
| ai_measure | survey (AI-adoption intensity) linked to financial records |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | revenue growth |
| ca_measure | — |
| effect_direction | conditional |
| conditions | AI-intensity threshold (low-level adoption: no effect); complementary technology investments (cloud, database) amplify; internal/exclusive R&D strategy amplifies |
| key_finding | AI pays off only above an adoption-intensity threshold, and more so with complementary technology investments and venture-specific internal R&D. |
| *not printed (coding data only)* | |
| theoretical_lens | technology complementarity (no grand theory) |
| industry | high-tech ventures |
| quality_notes | n=160 cross-section; representativeness tested (K-S); objective revenue data |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, ai_measure, industry** — PDF p. 2, 1. Introduction — ⚠ not machine-confirmed on page — open the page, 43% word sequence
   > In this study, we use a novel survey and administrative data on hightech ventures in South Korea, where AI adoption has accelerated but with considerable variation across firms.
   Ctrl+F: „In this study, we use a novel survey“
   → Names the setting (South Korea), the population (high-tech ventures), and the survey-plus-administrative-data design behind the AI measure.

2. **sample** — PDF p. 4, 3.1. Data and sample — ✓ verified, 100% word sequence
   > We conducted a survey of high-tech ventures based on a list of 1248 companies that were randomly selected and given to us by the Ministry of SMEs and Startups.
   Ctrl+F: „We conducted a survey of high-tech ventures based“
   → Backs the coded sampling frame of 1,248 firms from the ministry list.

3. **sample** — PDF p. 4, 3.1. Data and sample — ✓ verified, 100% word sequence
   > We sent out surveys to all companies in the list and over three months in 2019, we collected 300 responses (i.e., a response rate of approximately 24%).
   Ctrl+F: „We sent out surveys to all companies in“
   → Backs the coded 300 survey responses.

4. **sample** — PDF p. 4, 3.1. Data and sample — ✓ verified, 100% word sequence
   > Based on these restrictions, our final sample includes 160 firms.
   Ctrl+F: „restrictions, our final sample includes 160 firms.“
   → Backs the coded final n = 160.

5. **sample, quality_notes** — PDF p. 4, 3.1. Data and sample — ⚠ not machine-confirmed on page — open the page, 11% word sequence
   > To ensure the representativeness of our final sample, we use the Kolmogorov-Smirnov (K -S) two-sample test to compare the sample of 160 and the full sample
   Ctrl+F: „of our final sample, we use the Kolmogorov-Smirnov“
   → Backs the quality note 'representativeness tested (K-S)' and the n = 160.

6. **sample, ai_measure, quality_notes** — PDF p. 4, 3.1. Data and sample — ⚠ not machine-confirmed on page — open the page, 30% word sequence
   > Thus, this data enables us to accurately measure financial performance and also cross-check the basic information with our survey.
   Ctrl+F: „measure financial performance and also cross-check the basic“
   → Government financial database (SMINFO) supplies objective revenue data linked to the survey - backs 'survey + audited financials', 'linked to financial records', and 'objective revenue data'.

7. **method** — PDF p. 6, 4. Empirical framework — ⚠ not machine-confirmed on page — open the page, 33% word sequence
   > To mitigate this concern, we control for unobserved firm-fixed effects by performing a first-differenced regression at the firm level
   Ctrl+F: „To mitigate this concern, we control for“
   → First-differenced growth regressions with firm fixed effects on 2015-2019 revenue - backs method = panel econometrics.

8. **ai_measure** — PDF p. 4, 3.2.1. Independent variable — ✓ verified, 100% word sequence
   > we asked respondents to rate their level of adoption in each of the three AI technologies (1 = no adoption, 2 = testing stage, 3
   Ctrl+F: „we asked respondents to rate their level of“
   → AI measured as survey-rated adoption intensity across NLP, CV, and ML - backs 'survey (AI-adoption intensity)'.

9. **outcome_construct, performance_measure** — PDF p. 5, 3.2.3. Dependent variables — ✓ verified, 100% word sequence
   > We used the average revenue growth rate as a measure of firm performance.
   Ctrl+F: „We used the average revenue growth rate as“
   → Dependent variable is revenue growth as firm performance; no competitive-advantage construct is measured - backs outcome_construct = performance and performance_measure = revenue growth.

10. **effect_direction, conditions, key_finding** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > We find that firm revenue increases only after sufficient investment in AI, and the benefits of AI adoption are greater at firms that also invest in complementary technologies and pursue internal R & D strategy.
   Ctrl+F: „revenue increases only after sufficient investment in AI,“
   → The paper's own summary of its central result: intensity threshold plus complementary-technology and internal-R&D amplification - backs key_finding, conditional direction, and all three coded conditions.

11. **effect_direction, conditions** — PDF p. 7, 5.2. AI-adoption intensity and firm performance — ✓ verified, 83% word sequence
   > However, low levels of AI adoption or the testing stages of AI technologies do not generate revenue growth.
   Ctrl+F: „However, low levels of AI adoption or the“
   → Null effect at low adoption intensity - the threshold pattern that grounds effect_direction = conditional and the 'AI-intensity threshold' condition.

12. **conditions** — PDF p. 7, 5.3. AI adoption and complementary investments — ✓ verified, 100% word sequence
   > As column (1) indicates, the interaction term is positive at 0.637 with a standard error of 0.175.
   Ctrl+F: „As column (1) indicates, the interaction term is“
   → Significant positive interaction of high AI adoption with database/cloud-computing adoption - backs the complementary-technology condition.

13. **conditions** — PDF p. 9, 5.3. AI adoption and complementary investments — ⚠ not machine-confirmed on page — open the page, 15% word sequence
   > we find a positive relationship between higher levels of AI adoption, and revenue growth is significant among firms that adopt more firm-specific internal R & D strategies
   Ctrl+F: „relationship between higher levels of AI adoption, and“
   → Subsample significance only under firm-specific internal R&D - backs the internal/exclusive R&D strategy condition.

14. **key_finding** — PDF p. 10, 6. Discussion and conclusion — ✓ verified, 100% word sequence
   > our findings show that firm performance increases with the level of AI adoption, but only after sufficient investment in AI technology has been made
   Ctrl+F: „our findings show that firm performance increases with“
   → Conclusion restates the threshold result - backs key_finding 'AI pays off only above an adoption-intensity threshold'.

15. **theoretical_lens** — PDF p. 3, 2.2. AI adoption and investment in complementary technologies — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > Hitt and Brynjolfsson (1997) emphasized the importance of complementary assets in explanation for substantial variations in returns when firms adopt new innovations.
   Ctrl+F: „Hitt and Brynjolfsson (1997) emphasized the importance of“
   → Hypotheses are built on the technology-complementarity literature (complementary assets), not a grand theory - matches lens 'technology complementarity (no grand theory)'.

*Row check OK: ca_measure empty confirmed: no CA construct is measured; 'enhance firm competitiveness' appears only as narrative mechanism talk in section 2.1. quality_notes' 'cross-section' is coder design description (not quotable); K-S test and objective revenue data are quoted. Note for the author: Table 4 shows a positive binary any-adoption effect (0.288**), but direction = conditional stands per the frozen threshold rule - the paper's own headline is 'only after sufficient investment' with null estimates at all low-intensity levels.*

---

## S07 — Leoni L. et al. (2022) — International Journal of Operations and Production Management (AJG 4)

DOI: 10.1108/IJOPM-05-2022-0282 · status: final · PDF: `Leoni_2022_IJOPM-05-2022-0282.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Italy |
| sample | 120 senior executives of manufacturing firms, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption/use) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | perceived manufacturing firm performance (survey scale) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | FULL mediation via knowledge management processes: direct AI->MFP 0.006 n.s. (H2 rejected), AI->KMPs 0.48***, KMPs->MFP 0.51***; also AI->SCR direct n.s.; firm size -> AI maturity (0.26**) |
| key_finding | AI alone does NOT improve manufacturing firm performance - the effect exists exclusively through knowledge management processes (full mediation). |
| *not printed (coding data only)* | |
| theoretical_lens | knowledge management / KBV |
| industry | manufacturing |
| quality_notes | Perceptual, n=120 cross-section, AJG 4 outlet; direct-path rejection makes this a strong conditional-evidence anchor |
| coding_status | final |

### Evidence

1. **country_region, sample, method, industry** — p. 411 (PDF p. 1) — ✓ verified, 100% word sequence
   > In the study, six hypotheses have been developed and tested through an empirical survey administered to 120 senior executives of Italian manufacturing firms.
   Ctrl+F: „In the study, six hypotheses have been developed“
   → One sentence names the survey design, the n = 120 senior executives, Italy, and manufacturing.

2. **sample** — p. 416 (PDF p. 6) — ✓ verified, 100% word sequence
   > Finally, after discarding incomplete questionnaires, we obtained 120 useful questionnaires, which yielded a response rate of 11%
   Ctrl+F: „questionnaires, we obtained 120 useful questionnaires, which yielded“
   → Confirms the final sample of 120 usable responses.

3. **method** — p. 418 (PDF p. 8) — ✓ verified, 100% word sequence
   > In this study, we adopt the PLS-SEM approach which constitutes an appropriate multivariate path modelling approach used to test predictive and causal research models
   Ctrl+F: „In this study, we adopt the PLS-SEM approach“
   → Analysis strategy is PLS structural equation modelling - backs method = survey-SEM.

4. **ai_measure** — p. 418 (PDF p. 8) — ✓ verified, 100% word sequence
   > participants were asked to choose the level of adoption from a list of specific AI tools derived from a review of previous literature on AI tools already used in KM, SC and manufacturing performance domains.
   Ctrl+F: „asked to choose the level of adoption from“
   → AI is a survey-measured adoption construct (level of adoption of specific AI tools) - backs 'survey construct (AI adoption/use)'.

5. **outcome_construct, performance_measure** — p. 417 (PDF p. 7) — ✓ verified, 100% word sequence
   > Regarding the other constructs (AI, SCR and MFP), they were considered reflective in the research model. For each item, we have used a 5-point Likert scale.
   Ctrl+F: „other constructs (AI, SCR and MFP), they were“
   → Manufacturing firm performance is a perceptual 5-point Likert survey scale - backs outcome_construct = performance and the perceived-performance measure; no CA construct appears in the model.

6. **effect_direction** — p. 422 (PDF p. 12) — ✓ verified, 100% word sequence
   > However, there was no significant impact on the part of AI on SCR and MFP; therefore, H2 and H3 were rejected.
   Ctrl+F: „However, there was no significant impact on the“
   → Direct AI-to-MFP path rejected (Table 8: 0.0063, n.s.) - the non-significant direct path that grounds effect_direction = conditional.

7. **effect_direction, conditions, key_finding** — p. 423 (PDF p. 13) — ✓ verified, 100% word sequence
   > Thus, although the impact of AI on MFP and SCR is not significant, the results show a significant effect stemming from the mediation of KMPs.
   Ctrl+F: „although the impact of AI on MFP and“
   → The paper's own statement that the effect exists only via KMPs - full mediation with n.s. direct path = conditional per the frozen rule, and the coded key_finding.

8. **conditions** — p. 422 (PDF p. 12) — ✓ verified, 100% word sequence
   > The results reveal positive and significant relationships between AI and KMPs, thus supporting H1.
   Ctrl+F: „The results reveal positive and significant relationships between“
   → First leg of the mediation chain (AI -> KMPs, 0.4812*** in Table 8) - backs the coded full-mediation condition.

9. **conditions** — p. 422 (PDF p. 12) — ✓ verified, 100% word sequence
   > the results indicate a difference regarding the maturity of AI adoption based on firm size ( β 5 0.26, p < 0.01)
   Ctrl+F: „the results indicate a difference regarding the maturity“
   → Backs the coded condition 'firm size -> AI maturity (0.26**)' (extraction renders '=' as '5').

10. **conditions** — p. 423 (PDF p. 13) — ✓ verified, 100% word sequence
   > we obtained a beta coefficient equal to 0.29 ( p <0.01) for the relationship AI- KMPs-MFP and a beta coefficient equal to 0.30 ( p < 0.01) for the relationship AI- KMPs-SCR
   Ctrl+F: „we obtained a beta coefficient equal to 0.29“
   → Significant indirect effects through KMPs quantify the mediation condition.

11. **key_finding** — p. 425 (PDF p. 15) — ✓ verified, 100% word sequence
   > AI has positive effects on MFP and SCR only when KMPs intervene in these relationships.
   Ctrl+F: „AI has positive effects on MFP and SCR“
   → Restates the central result: AI alone does not improve performance - backs key_finding.

12. **theoretical_lens** — p. 414 (PDF p. 4) — ✓ verified, 100% word sequence
   > According to the knowledge-based view (KBV) of the firm (Grant, 1996), knowledge can be considered the most valuable resource of a firm, the only enduring source of competitive advantage
   Ctrl+F: „According to the knowledge-based view (KBV) of the“
   → Hypotheses are grounded in the knowledge-based view - backs lens 'knowledge management / KBV'.

13. **quality_notes** — p. 418 (PDF p. 8) — ✓ verified, 100% word sequence
   > In survey-based studies, collecting perceptual data from a single source at a point in time generates common method bias (CMB) issues
   Ctrl+F: „In survey-based studies, collecting perceptual data from a“
   → Authors acknowledge the perceptual single-source cross-section design - backs the 'perceptual, n=120 cross-section' quality note.

14. **quality_notes** — p. 425 (PDF p. 15) — ✓ verified, 100% word sequence
   > therefore, the results reported in this paper potentially tend to be more positive than the actual situation
   Ctrl+F: „results reported in this paper potentially tend to“
   → Authors' own limitation (sample skews larger than the Italian national average) - source-based part of the quality note.

*Row check OK: ca_measure empty confirmed: competitive advantage appears only as KBV theory talk (p. 4) and discussion rhetoric (p. 14), never as a measured construct. quality_notes' 'AJG 4 outlet' and 'strong conditional-evidence anchor' are coder commentary, not quotable from the paper. Direction = conditional is the adjudicated decision (brief: direct AI->MFP 0.006 n.s., H2 rejected) and matches the full text exactly.*

---

## S08 — Lui A.K.H. et al. (2022) — Annals of Operations Research (AJG 3)

DOI: 10.1007/s10479-020-03862-8 · status: final · PDF: `lui2022impact.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 119 AI investment announcements by 62 listed firms, Factiva search Jan 2015 - Feb 2019 |
| method | event study |
| ai_measure | announcements (AI investment announcements) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm market value (CAR; -1.77% on event day) |
| ca_measure | — |
| effect_direction | negative |
| conditions | nonmanufacturing firms (more negative); weak IT capability (more negative); low credit rating (more negative) |
| key_finding | BENCHMARK: investors react negatively to AI investment announcements on average; the penalty concentrates in nonmanufacturing firms with weak IT capability and low credit ratings. |
| *not printed (coding data only)* | |
| theoretical_lens | IT business value / event-study tradition (investor expectations), no grand theory |
| industry | cross-industry |
| quality_notes | Short-window event study; market perception, not realized performance \| SAMPLE-CHECK OK: event study/negative confirmed in full-text probes |
| coding_status | final |

### Evidence

1. **country_region** — p. 379 (PDF p. 7) — ✓ verified, 100% word sequence
   > We collected stock price information from the Center for Research in Security Prices (CSRP) and financial data from COMPUSTAT.
   Ctrl+F: „We collected stock price information from the Center“
   → CRSP/COMPUSTAT are US-listing databases - relevant to the market composition of the sample.

2. **country_region** — p. 385 (PDF p. 13) — ✓ verified, 100% word sequence
   > First, the sample is limited to only U.S. publicly listed firms.
   Ctrl+F: „First, the sample is limited to only U.S.“
   → The authors' own limitation statement names the market composition.
   **⚠ TENSION:** Coded country_region says 'multi-market (market composition not explicit)', but this limitation sentence explicitly states US publicly listed firms only (consistent with CRSP stock data and S&P domestic credit ratings). Consider recoding to USA.

3. **sample, ai_measure** — p. 379 (PDF p. 7) — ✓ verified, 100% word sequence
   > We used Factiva to search for announcements containing pertinent keywords, such as 'AI' and 'Artificial Intelligence,' from January 2015 to February 2019
   Ctrl+F: „We used Factiva to search for announcements containing“
   → Backs the Factiva search window Jan 2015 - Feb 2019 and the AI measure = investment announcements.

4. **sample** — p. 379 (PDF p. 7) — ✓ verified, 100% word sequence
   > After a careful processing of the data, a total of 119 valid announcements representing 62 sample firms from 2015 to 2019 were maintained.
   Ctrl+F: „processing of the data, a total of 119“
   → Backs the coded 119 announcements by 62 listed firms.

5. **method, theoretical_lens** — p. 374 (PDF p. 2) — ✓ verified, 100% word sequence
   > Since a stock market response is instantaneous and can reflect investors' expectations of future firm performance (Bose and Pal 2012), an event study is an appropriate approach for this research.
   Ctrl+F: „Since a stock market response is instantaneous and“
   → Backs 'investor expectations' in the lens and the event-study method choice.

6. **method** — p. 374 (PDF p. 2) — ✓ verified, 100% word sequence
   > The event study methodology is employed to examine the effect of AI investment on market value.
   Ctrl+F: „study methodology is employed to examine the effect“
   → Directly states method = event study.

7. **outcome_construct, performance_measure, effect_direction, key_finding** — p. 373 (PDF p. 1) — ✓ verified, 100% word sequence
   > this study finds that AI investment has a negative impact on the firms' market value. The stock prices of the firms decrease by 1.77% on the day of the announcement.
   Ctrl+F: „this study finds that AI investment has a“
   → Backs outcome = performance measured as firm market value (CAR), the -1.77% event-day figure, negative direction, and the key finding.

8. **effect_direction** — p. 382 (PDF p. 10) — ✓ verified, 100% word sequence
   > Using both parametric and nonparametric tests, on day [0], the mean ( -1.77%) and median ( -0.10%) ARs are statistically significant and negative.
   Ctrl+F: „Using both parametric and nonparametric tests, on day“
   → Significant negative average main effect on the event day - backs effect_direction = negative.

9. **conditions** — p. 373 (PDF p. 1) — ✓ verified, 100% word sequence
   > Nonmanufacturing firms and firms with weak information technology capabilities or low credit ratings suffer a more negative impact compared with other firms.
   Ctrl+F: „firms and firms with weak information technology capabilities“
   → Backs all three coded conditions: nonmanufacturing, weak IT capability, low credit rating each amplify the negative reaction.

10. **conditions** — p. 384 (PDF p. 12) — ✓ verified, 100% word sequence
   > We found that IT capability, credit rating, and type of industry are strong moderating factors.
   Ctrl+F: „We found that IT capability, credit rating, and“
   → The paper itself labels the three coded conditions as moderating factors.

11. **key_finding** — p. 373 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 35% word sequence
   > The findings suggest that investors perceive AIinvestment announcements to be unwelcome news for the majority of firms.
   Ctrl+F: „announcements to be unwelcome news for the majority“
   → The paper's own summary of the central result - investors react negatively on average ('AIinvestment' is an extraction spacing artifact).

12. **theoretical_lens** — p. 376 (PDF p. 4) — ✓ verified, 100% word sequence
   > Previous studies have used the event study methodology to examine the impact of various types of IT investments on firm value (e.g., Dehning et al. 2003; Teo et al. 2016).
   Ctrl+F: „Previous studies have used the event study methodology“
   → The study is framed in the IT-business-value event-study tradition, not a grand theory - backs the coded lens.

13. **industry** — p. 379 (PDF p. 7) — ✓ verified, 100% word sequence
   > We used SIC codes to define whether the firms were part of the manufacturing sector. A firm was considered to be a manufacturing firm if its SIC code is from 20 to 39
   Ctrl+F: „to define whether the firms were part of“
   → Sample spans manufacturing and nonmanufacturing SIC codes (Table 3 Panel B lists 23 industries) - backs industry = cross-industry.

14. **quality_notes** — p. 385 (PDF p. 13) — ✓ verified, 100% word sequence
   > Although the results of event analysis cannot fully measure the actual performance of AI implementation, they can reflect the concerns of investors about the adoption of AI and the risks associated with the adoption.
   Ctrl+F: „event analysis cannot fully measure the actual performance“
   → Authors concede the method captures market perception, not realized performance - backs the quality note.

15. **quality_notes** — p. 385 (PDF p. 13) — ✓ verified, 100% word sequence
   > Finally, the research only examines the short-term impacts of AI investments.
   Ctrl+F: „examines the short-term impacts of AI investments.“
   → Authors' own limitation - backs 'short-window event study' in the quality note.

**⚠ ROW CHECK:** One tension: country_region coded 'multi-market (announcements via Factiva; market composition not explicit)', but the limitations section (p. 13) states 'the sample is limited to only U.S. publicly listed firms', and stock data come from CRSP with S&P domestic credit ratings - the paper is explicit after all; consider recoding to USA. Everything else verifies cleanly (S08 was a spot-check row: event study / performance / negative confirmed). ca_measure empty confirmed - only market value is measured; 'competitive edges' appears once as survey background rhetoric on p. 1.

---

## S09 — Mishra S. et al. (2022) — Journal of the Academy of Marketing Science (AJG 4*)

DOI: 10.1007/s11747-022-00876-5 · status: final · PDF: `Mishra_2022_s11747-022-00876-5.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 19,000 firm-year observations, US-listed firms (COMPUSTAT + EDGAR 10-Ks), simultaneous equations; PSM robustness (1,801 treatment / 2,251 control firms) |
| method | panel econometrics |
| ai_measure | 10-K text (share of AI keywords = AI focus) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | gross and net operating efficiency, net profitability, adspend, employment |
| ca_measure | — |
| effect_direction | mixed |
| conditions | — |
| key_finding | AI focus reduces gross operating efficiency but increases net operating efficiency and profitability - automation raises costs more slowly than revenues. |
| *not printed (coding data only)* | |
| theoretical_lens | economic + marketing theory (guiding framework, no single lens) |
| industry | cross-industry |
| quality_notes | Archival text measure (AI focus, not investment); endogeneity addressed via instruments (Cragg-Donald) + PSM; NO moderators tested (explicitly deferred) - rare unconditional-evidence case for synthesis contrast group |
| coding_status | final |

### Evidence

1. **country_region, sample, ai_measure** — p. 1179 (PDF p. 4) — ⚠ not machine-confirmed on page — open the page, 32% word sequence
   > we downloaded all the 10-K filings, excluding amended documents, from the SEC's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) website (www. sec. gov) filed for the period 2005-2019.
   Ctrl+F: „and Retrieval (EDGAR) website (www. sec. gov)“
   → EDGAR 10-K filings of US publicly traded firms 2005-2019 - backs the data source, USA, and the 10-K text basis of the AI measure.

2. **sample** — p. 1180 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 16% word sequence
   > We collected data on firm characteristics from COMPUSTAT. To measure AI, in accordance with Bodnaruk et al. (2015), we first cleaned the data to separate all the text from the annual reports.
   Ctrl+F: „separate all the text from the annual reports.“
   → Backs COMPUSTAT as the firm-data source in the coded sample.

3. **sample** — p. 1180 (PDF p. 5) — ✓ verified, 100% word sequence
   > The final sample comprised 19,000 firm-year observations.
   Ctrl+F: „The final sample comprised“
   → Backs the coded n of 19,000 firm-year observations.

4. **sample, quality_notes** — p. 1188 (PDF p. 13) — ✓ verified, 100% word sequence
   > There are 1801 firms in the treatment sample and 2251 firms in the control sample.
   Ctrl+F: „There are 1801 firms in the treatment sample“
   → Backs the coded PSM robustness detail (1,801 treatment / 2,251 control firms).

5. **method** — p. 1180 (PDF p. 5) — ✓ verified, 100% word sequence
   > Therefore, we employ a simultaneous equation framework for our empirical analysis.
   Ctrl+F: „Therefore, we employ a simultaneous equation framework“
   → System of ten simultaneous equations on the firm-year panel - backs method = panel econometrics (simultaneous equations).

6. **method, quality_notes** — p. 1181 (PDF p. 6) — ✓ verified, 100% word sequence
   > We estimate the system using three-stage least squares (3SLS) with instrumental variables to allow for the fact that regressors in one or more equation are correlated with the error terms.
   Ctrl+F: „squares (3SLS) with instrumental variables to allow for“
   → 3SLS with instruments backs the econometric method and the quality note 'endogeneity addressed via instruments'.

7. **ai_measure** — p. 1180 (PDF p. 5) — ✓ verified, 100% word sequence
   > We constructed the AI focus variable by searching for 122 AI-related words (reported in Internet Appendix III).
   Ctrl+F: „We constructed the AI focus variable by searching“
   → AI measured as 10-K keyword-based AI focus - backs ai_measure.

8. **ai_measure** — p. 1180 (PDF p. 5) — ✓ verified, 100% word sequence
   > We searched for the frequency of these terms in all the 10-Ks filed for the entire sample period and scaled it by the total number of words in the annual report.
   Ctrl+F: „scaled it by the total number of words“
   → AI focus = share of AI keywords in 10-K text - backs the 'share of AI keywords' formulation.

9. **outcome_construct, performance_measure** — p. 1176 (PDF p. 1) — ✓ verified, 100% word sequence
   > we examine the link between firms' focus on AI in their 10-K reports and their gross and net operating efficiency
   Ctrl+F: „on AI in their 10-K reports and their“
   → Outcomes are operating-efficiency performance measures; no competitive-advantage construct - backs outcome_construct = performance and the performance_measure list.

10. **performance_measure, effect_direction** — p. 1184 (PDF p. 9) — ✓ verified, 100% word sequence
   > Similarly, AI focus has a negative and significant relationship with Sales/Emp, a measure of gross efficiency. However, AI focus has a positive and significant relationship with NI/30% of SGA, return on marketing investment
   Ctrl+F: „AI focus has a negative and significant relationship“
   → Sign split across outcome components (gross efficiency negative, marketing return positive) - backs effect_direction = mixed.

11. **effect_direction** — p. 1184 (PDF p. 9) — ✓ verified, 100% word sequence
   > AI focus has a positive and significant relationship with both NI/Sales, NI/Emp.
   Ctrl+F: „has a positive and significant relationship with“
   → Positive components (return on sales, net profit per employee) of the mixed pattern.

12. **effect_direction, key_finding** — p. 1193 (PDF p. 18) — ✓ verified, 100% word sequence
   > We find a reduction in gross operating efficiency and an increase in net operating efficiency, suggesting that costs are increasing at a slower rate than revenue due to automation.
   Ctrl+F: „increasing at a slower rate than revenue due“
   → The paper's own statement of the central result - backs key_finding ('automation raises costs more slowly than revenues') and the mixed direction.

13. **conditions, quality_notes** — p. 1194 (PDF p. 19) — ✓ verified, 100% word sequence
   > Third, future research could test theoretically meaningful moderators.
   Ctrl+F: „Third, future research could test theoretically meaningful“
   → Moderator testing is explicitly deferred to future research - confirms conditions coded EMPTY (adjudicated: 'no moderators tested') and the quality note.

14. **key_finding** — p. 1176 (PDF p. 1) — ✓ verified, 100% word sequence
   > We show how AI focus is associated with improvements in net profitability, net operating efficiency and return on marketing-related investment while reducing adspend and creating jobs.
   Ctrl+F: „We show how AI focus is associated with“
   → Abstract summary of the result set - backs key_finding and the performance_measure list (adspend, employment).

15. **theoretical_lens** — p. 1177 (PDF p. 2) — ✓ verified, 100% word sequence
   > Our guiding framework draws on both economic and marketing theory.
   Ctrl+F: „Our guiding framework draws on both economic and“
   → Directly states the coded lens: economic + marketing theory as a guiding framework, no single grand lens.

16. **industry** — p. 1182 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > Having validated our AI focus variable, we consider the distribution of AI focus across twelve Fama French industries.
   Ctrl+F: „Having validated our AI focus variable, we consider“
   → Sample spans twelve Fama-French industries - backs industry = cross-industry.

17. **quality_notes** — p. 1193 (PDF p. 18) — ⚠ not machine-confirmed on page — open the page, 33% word sequence
   > Our results should be interpreted cautiously as our conclusions are based on firms' use of 122 AI related keywords in their 10-K reports.
   Ctrl+F: „Our results should be interpreted cautiously as our“
   → Authors' own caveat that the measure is archival 10-K text (AI focus), not investment - backs the quality note.

18. **quality_notes** — p. 1186 (PDF p. 11) — ✓ verified, 100% word sequence
   > The Cragg-Donald F-statistics are statistically significant, for all our simultaneous equations models, suggesting that the instruments are not weak.
   Ctrl+F: „models, suggesting that the instruments are not weak.“
   → Backs the quality note 'endogeneity addressed via instruments (Cragg-Donald)'.

*Row check OK: conditions EMPTY confirmed: no moderators/mediators are tested anywhere; moderator testing is explicitly deferred to future research (p. 19) - matches the adjudicated decision. ca_measure empty confirmed: 'competitiveness of firms' appears once as introduction rhetoric (p. 1), no CA construct measured. quality_notes' 'rare unconditional-evidence case for synthesis contrast group' is coder commentary, not quotable. Note: regression tables run on 15,553 observations after listwise deletion; the coded 19,000 is the paper's stated final sample size.*

---

## S10 — Sun Y. et al. (2022) — Systems Research and Behavioral Science (AJG 2)

DOI: 10.1002/sres.2860 · status: final · PDF: `Sun_2022_sres-2860.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 234 AI-related manufacturers (GM/CEO respondents), CB-SEM |
| method | survey-SEM |
| ai_measure | survey construct (value co-creation in AI innovation ecosystem) |
| *Table A.2 columns* | |
| outcome_construct | competitive_advantage |
| performance_measure | — |
| ca_measure | perceived competitive advantage scale (own construct, Table 3) + innovation intelligibility; NO performance construct in model |
| effect_direction | conditional |
| conditions | FULL mediation: direct paths VC->CA and EV/RV->CA not significant; dynamic capabilities + innovation capabilities carry the effect (Leoni/Wang pattern: effect only via mechanism) |
| key_finding | Value co-creation in AI ecosystems has NO direct effect on competitive advantage - effects run entirely through dynamic and innovation capabilities. |
| *not printed (coding data only)* | |
| theoretical_lens | value co-creation + dynamic capabilities |
| industry | manufacturing (AI-related) |
| quality_notes | Perceptual, cross-section, n=234 GM/CEO respondents; economic/relationship value are co-creation perceptions (Yim et al. 2012 items), easily mistaken for performance |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 478 (PDF p. 5) — ✓ verified, 100% word sequence
   > This study collected data from the general manager/CEO of the AI-related manufacturing companies in the Yangtze River Delta region.
   Ctrl+F: „This study collected data from the general manager/CEO“
   → Backs GM/CEO respondents, China (Yangtze River Delta), and the AI-related manufacturing industry.

2. **sample, method, industry** — p. 474 (PDF p. 1) — ✓ verified, 100% word sequence
   > We collected data from 234 AI-related manufacturers for the structural equation modelling analysis.
   Ctrl+F: „We collected data from 234 AI-related manufacturers“
   → One sentence names survey-SEM, n = 234, and AI-related manufacturing.

3. **sample** — p. 478 (PDF p. 5) — ✓ verified, 100% word sequence
   > We sent questionnaires to 400 companies in 2019 and received 234 valid responses, resulting in a 58% response rate.
   Ctrl+F: „400 companies in 2019 and received 234 valid“
   → Backs the coded n = 234 valid responses.

4. **method, quality_notes** — p. 478 (PDF p. 5) — ✓ verified, 100% word sequence
   > In this study, a 5-point Likert scale was used to measure the variables in the model.
   Ctrl+F: „In this study, a 5-point Likert scale was“
   → All constructs are perceptual survey scales - backs survey method and the 'perceptual' quality note.

5. **method** — p. 481 (PDF p. 8) — ⚠ not machine-confirmed on page — open the page, 28% word sequence
   > We reported the model fitting results, including χ 2 / df = 2.75, RMSEA = 0.048, CFI = 0.925, TLI = 0.905, and SRMR = 0.065.
   Ctrl+F: „We reported the model fitting results, including“
   → Covariance-based fit indices (chi-square/df, CFI, TLI) back the CB-SEM detail in the coded sample field.

6. **ai_measure** — p. 478 (PDF p. 5) — ✓ verified, 100% word sequence
   > Therefore, this study adopted Ranjan and Read (2016) co-productions 12 items to measure value co-creation.
   Ctrl+F: „Read (2016) co-productions 12 items to measure value“
   → The AI-side construct is a 12-item survey measure of value co-creation in the AI innovation ecosystem - backs ai_measure.

7. **outcome_construct, ca_measure** — p. 479 (PDF p. 6) — ✓ verified, 100% word sequence
   > We adapted six items to measure competitive advantage from several studies (Cao et al., 2019; Ferreira et al., 2020; Papadas et al., 2019).
   Ctrl+F: „(Cao et al., 2019; Ferreira et al., 2020;“
   → A distinct six-item CA scale (CA1-CA6, alpha = 0.927 in Table 3) is measured - backs outcome_construct = competitive_advantage and the coded ca_measure.

8. **outcome_construct** — p. 478 (PDF p. 5) — ✓ verified, 100% word sequence
   > Hypothesis 9. Value co-creation positively affects competitive advantage.
   Ctrl+F: „Hypothesis 9. Value co-creation positively“
   → CA is hypothesized as the model's outcome (scale + hypothesis, per the case-law requirement for coding competitive_advantage).

9. **performance_measure, quality_notes** — p. 476 (PDF p. 3) — ✓ verified, 100% word sequence
   > Economic value refers to the benefits and costs derived from better and customized products and services (Yim et al., 2012).
   Ctrl+F: „value refers to the benefits and costs derived“
   → 'Economic value' is a perceived co-creation value (Yim et al. items), not a firm-performance construct - confirms performance_measure EMPTY and the quality note that it is easily mistaken for performance.

10. **effect_direction, conditions, key_finding** — p. 474 (PDF p. 1) — ✓ verified, 100% word sequence
   > value co-creation does not have a significant impact on competitive advantage and innovation intelligibility, and dynamic capabilities and innovation capabilities play the mediating role
   Ctrl+F: „co-creation does not have a significant impact on“
   → The abstract's own statement: no direct effect, effect carried by DC and IC - backs conditional direction, the full-mediation condition, and key_finding.

11. **effect_direction** — p. 481 (PDF p. 8) — ⚠ not machine-confirmed on page — open the page, 58% word sequence
   > Considering that the significance level of the impact of value co-creation on competitive advantage and innovation intelligibility is greater than 0.1, both Hypotheses 9 and 10 are not supported.
   Ctrl+F: „Considering that the significance level of the impact“
   → Direct VC->CA path non-significant (0.240, p = .185 in Table 5) - the null direct path grounding effect_direction = conditional.

12. **conditions** — p. 481 (PDF p. 8) — ✓ verified, 100% word sequence
   > Given that the significance levels of the impact of economic value on the competitive advantage and innovation intelligibility are greater than 0.1
   Ctrl+F: „Given that the significance levels of the impact“
   → EV (and in the same sentence RV) direct paths to CA are non-significant - backs the coded condition 'direct paths EV/RV->CA not significant'.

13. **conditions** — p. 482 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 26% word sequence
   > As shown in Table 6, with path coefficients 95% confidence interval, dynamic capabilities and innovation capabilities have significant mediating effects between value co-creation and competitive advantage.
   Ctrl+F: „As shown in Table 6, with path“
   → Bootstrap mediation test: DC and IC carry the effect - backs the full-mediation condition.

14. **theoretical_lens** — p. 475 (PDF p. 2) — ✓ verified, 100% word sequence
   > Value co-creation has been extensively studied after a shift from sales to service dominance was proposed by Vargo and Lusch (2004).
   Ctrl+F: „been extensively studied after a shift from sales“
   → Backs the value co-creation half of the coded lens.

15. **theoretical_lens** — p. 477 (PDF p. 4) — ✓ verified, 100% word sequence
   > Dynamic capabilities are considered as a mechanism to produce competitive advantage and affect innovation intelligibility (Bitencourt et al., 2020).
   Ctrl+F: „Dynamic capabilities are considered as a mechanism“
   → Backs the dynamic-capabilities half of the coded lens.

16. **quality_notes** — p. 483 (PDF p. 10) — ✓ verified, 94% word sequence
   > Third, we collected the data from the Yangtze River Delta region, where SMEs are relatively concentrated.
   Ctrl+F: „Third, we collected the data from the Yangtze“
   → Authors' own limitation on the regional cross-sectional sample - source-based part of the quality note.

*Row check OK: performance_measure EMPTY confirmed: the model contains VC, EV, RV, DC, IC, CA, II - no performance construct; 'economic value' is a co-creation perception (adjudicated S10 decision). quality_notes' 'cross-section' is coder design description; perceptual scales and the regional sample are quoted. Direction = conditional matches the frozen rule (direct VC->CA 0.240 n.s., effect only via DC/IC mediation).*

---

## S11 — Ali Mohamad T. et al. (2023) — Journal of Organizational Change Management (AJG 2)

DOI: 10.1108/JOCM-03-2023-0057 · status: final · PDF: `Ali_2023_JOCM-03-2023-0057.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | UAE |
| sample | single case (CMC Dubai): 9 semi-structured interviews with robotic-surgery team + archival data, triangulated |
| method | case study |
| ai_measure | case observation (adoption of AI/robotic surgery) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | four qualitative outcome categories: clinical (errors/infections down, patient experience), financial (quantified: ~500K/month at 30 robotic cases), organizational (resource allocation), technological |
| ca_measure | competitive position with explicit competitor comparison: patient choice over competitors, bargaining power with third-party payers, differentiation, upper hand over competition (P1) |
| effect_direction | positive |
| conditions | qualified robotic team incl. revenue-cycle team (capability prerequisite); cultural shift in medical community; regulatory approval (DHA, case-by-case); high acquisition costs not covered by insurance (entry barrier) |
| key_finding | AI-enabled robotic surgery improves clinical, financial and technological outcomes and strengthens the competitive position of the healthcare organization. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV (substitution/complementation) |
| industry | healthcare |
| quality_notes | Single case (CMC Dubai), 9 interviews + archival triangulation; qualitative but with quantified financial claims and genuine competitor-comparative reasoning |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 49–51 (PDF p. 1) — ✓ verified, 100% word sequence
   > an exploratory analysis was conducted investigating the Clemenceau Medical Center in Dubai, one of the top private hospitals in the UAE(CMC)
   Ctrl+F: „an exploratory analysis was conducted“
   → Places the single case in the UAE (Dubai) in the healthcare (hospital) industry.

2. **country_region, quality_notes** — p. 63 (PDF p. 15) — ✓ verified, 100% word sequence
   > Our findings are context-specific in general, which may help explain the success of our findings in private healthcare institutions in the UAE and the conditions under which these insights might be generalized to public hospitals
   Ctrl+F: „Our findings are context-specific in general, which may“
   → Authors' own limitation (context-specific single case in UAE private healthcare) backing the source-based part of quality_notes and confirming country_region = UAE.

3. **sample** — p. 54 (PDF p. 6) — ✓ verified, 100% word sequence
   > We conducted nine semi-structured interviews with the head and the members of the robotic surgery team in CMC Dubai.
   Ctrl+F: „We conducted nine semi-structured interviews with the head“
   → Confirms 9 semi-structured interviews with the robotic-surgery team as coded in sample.

4. **sample** — p. 54 (PDF p. 6) — ✓ verified, 100% word sequence
   > we use multiple sources of evidence, such as semi-structured interviewees, archival data, including industry reports, newspaper and magazine articles and internal documents, to triangulate data
   Ctrl+F: „of evidence, such as semi-structured interviewees, archival data,“
   → Confirms the archival-data and triangulation component of the coded sample description.

5. **method** — p. 53 (PDF p. 5) — ✓ verified, 100% word sequence
   > To answer the research question in a qualitative approach we used the case study methodology (Yin, 1994) investigating the Clemenceau Medical Center in Dubai (CMC) case.
   Ctrl+F: „To answer the research question in a qualitative“
   → States the case study methodology on a single case (CMC Dubai), matching method = case study.

6. **method, quality_notes** — p. 53 (PDF p. 5) — ✓ verified, 100% word sequence
   > This in-depth, single case is designed to aid theory building through analytical generalization, not to generate statistical generalizability
   Ctrl+F: „This in-depth, single case is designed to aid“
   → Authors' own characterization of the single-case design, backing the 'single case' element of quality_notes.

7. **ai_measure** — p. 50 (PDF p. 2) — ✓ verified, 100% word sequence
   > the research question concerns how implementing digital solutions based on Artificial Intelligence enables healthcare facilities to maintain their competitive position and gain additional benefits compared to traditional surgical approaches
   Ctrl+F: „solutions based on Artificial Intelligence enables healthcare facilities“
   → AI is observed as the adoption/implementation of AI-based robotic surgery in the case firm, matching ai_measure = case observation of AI/robotic surgery adoption.

8. **outcome_construct, performance_measure** — p. 56 (PDF p. 8) — ✓ verified, 100% word sequence
   > distinguished in: (1) clinical outcome (i.e. minimization of surgical errors and infections; maximization of patients ' experience); (2) financial outcome; (3) organizational outcome (i.e. optimization resources ' allocation) and d) technological outcome (i.e. mechanical improvements)
   Ctrl+F: „distinguished in: (1) clinical outcome (i.e. minimization of“
   → Lists the four qualitative outcome categories coded in performance_measure (clinical, financial, organizational, technological) — the performance half of outcome_construct = both.

9. **outcome_construct, ca_measure** — p. 56 (PDF p. 8) — ✓ verified, 100% word sequence
   > when patients are choosing CMC Dubai over competitors this will reinforce and strengthen the company bargaining power with TPP and will lead to an increase in the base rate
   Ctrl+F: „competitors this will reinforce and strengthen the company“
   → Genuine competitor-comparative evidence (patient choice over competitors, bargaining power with third-party payers) backing the CA half of outcome_construct = both and the coded ca_measure.

10. **outcome_construct, effect_direction, key_finding** — p. 62 (PDF p. 14) — ✓ verified, 100% word sequence
   > implementing a robotic surgery program in a healthcare setting can easily represent a competitive advantage that will help position the organization in the market, as well as a source of increased income and revenue
   Ctrl+F: „program in a healthcare setting can easily represent“
   → The paper's own concluding statement of its central result: positive effect on both competitive advantage and financial outcomes, matching key_finding and effect_direction = positive.

11. **performance_measure** — p. 56 (PDF p. 8) — ✓ verified, 100% word sequence
   > Financially speaking, for a hospital averaging 30 robotic case a month, an amount of 500 K will financially improve our performance
   Ctrl+F: „“Financially speaking, for a hospital averaging 30 robotic“
   → The Finance Manager's quantified financial claim (~500K/month at 30 robotic cases) coded in performance_measure.

12. **ca_measure, conditions** — p. 62 (PDF p. 14) — ✓ verified, 100% word sequence
   > Developing a qualified robotic team, from nurses to technicians to surgeons, supported by a dynamic revenue cycle management team, will always give the organization the upper hand over the competition.
   Ctrl+F: „Developing a qualified robotic team, from nurses to“
   → Backs the coded 'upper hand over competition' element of ca_measure and the condition 'qualified robotic team incl. revenue-cycle team'.

13. **effect_direction, key_finding** — p. 61 (PDF p. 13) — ✓ verified, 100% word sequence
   > Our findings demonstrate the extent to which implementing Artificial Intelligence-based solutions inside healthcare ecosystems helps organisations gain a competitive advantage in the market
   Ctrl+F: „Our findings demonstrate the extent to which implementing“
   → Discussion's summary of the central result — an unambiguously positive effect on competitive position, backing key_finding and effect_direction = positive.

14. **conditions** — p. 53 (PDF p. 5) — ✓ verified, 100% word sequence
   > introducing breakthrough technology in the health sector, such as Artificial Intelligence, necessitates a cultural shift inside the medical community and new technologies that spur the process from the outside
   Ctrl+F: „introducing breakthrough technology in the health sector, such“
   → Backs the coded condition 'cultural shift in medical community'.

15. **conditions** — p. 61 (PDF p. 13) — ✓ verified, 100% word sequence
   > the numerous advantages and benefits generated by the adoption of a robotic approach led the DHA (Dubai Health Authority) to approve the treatment of automated surgery cases in Dubai on a case-by-case basis
   Ctrl+F: „the numerous advantages and benefits generated by the“
   → Backs the coded condition 'regulatory approval (DHA, case-by-case)'.

16. **conditions** — p. 61 (PDF p. 13) — ✓ verified, 100% word sequence
   > Despite the high cost of acquiring and developing such technologies, which is not fully covered by insurance
   Ctrl+F: „Despite the high cost of acquiring and developing“
   → Backs the coded condition 'high acquisition costs not covered by insurance (entry barrier)'.

17. **theoretical_lens** — p. 53 (PDF p. 5) — ✓ verified, 100% word sequence
   > Currently, substitution and augmentation of AI are challenging topics. The substitution construct is rooted in the Resource Based View (RBV), which argues that others replace resources with the same functionality
   Ctrl+F: „Currently, substitution and augmentation of AI are challenging“
   → Names RBV and the substitution/augmentation pairing as the study's theoretical anchor, matching the coded lens.

*Row check OK: All non-empty columns evidenced. Two author-side observations: (1) coded theoretical_lens says 'substitution/complementation' but the paper's own terms are 'substitution and augmentation' (p.5, following Raisch & Krakowski 2021) — label detail only, RBV anchor confirmed; (2) the evaluative tail of quality_notes ('qualitative but with quantified financial claims and genuine competitor-comparative reasoning') is coder commentary, not source text — the source-based parts (single case, 9 interviews, triangulation, context-specificity) are quoted. Abstract says 'three primary outcomes' but the findings section (p.8) lists the four categories as coded.*

---

## S12 — Czarnitzki D. et al. (2023) — Journal of Economic Behavior and Organization (AJG 3)

DOI: 10.1016/j.jebo.2023.05.008 · status: final · PDF: `Czarnitzki_2023_j-jebo-2023-05-008.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Germany |
| sample | 5,851 firms (409 AI users, ~7%), German CIS 2018 (ZEW); cross-section OLS/2SLS-IV + panel subset with IV-FE, entropy balancing |
| method | panel econometrics |
| ai_measure | survey (CIS AI adoption dummy + intensity of AI use in business processes) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm productivity (labor- and value-added-based) |
| ca_measure | — |
| effect_direction | positive |
| conditions | — |
| key_finding | AI adoption is robustly associated with higher firm productivity in representative German data; the effect grows with usage intensity. |
| *not printed (coding data only)* | |
| theoretical_lens | GPT (general-purpose technology) |
| industry | cross-industry |
| quality_notes | Representative innovation survey + IV strategy - one of the methodically strongest positive findings; robustness across adoption dummy AND intensity/breadth measure (2.5 of 20 method-area combos avg); no moderators tested -> unconditional-evidence contrast group (with S09) |
| coding_status | final |

### Evidence

1. **country_region, sample, ai_measure** — p. 193 (PDF p. 6) — ✓ verified, 100% word sequence
   > We use cross-section as well as panel data of firms taken from the German contribution to the Community Innovation Survey (CIS) of the European Commission.
   Ctrl+F: „We use cross-section as well as panel data“
   → Confirms the data source coded in sample and ai_measure: German CIS survey data (ZEW's Mannheim Innovation Panel).

2. **country_region, industry** — p. 193 (PDF p. 6) — ✓ verified, 100% word sequence
   > The information collected is representative of all firms in Germany with at least 5 employees in manufacturing, mining, utilities, and business-oriented service sectors
   Ctrl+F: „The information collected is representative of all firms“
   → Places the sample in Germany across manufacturing and service sectors, backing country_region = Germany and industry = cross-industry.

3. **sample, method** — p. 199 (PDF p. 12) — ✓ verified, 100% word sequence
   > we constructed a panel database to check the robustness of the results once we account for unobserved heterogeneity by including firm-fixed effects
   Ctrl+F: „we constructed a panel database to check the“
   → Backs the coded 'panel subset with IV-FE' element of sample/method.

4. **sample, method** — p. 192 (PDF p. 5) — ✓ verified, 95% word sequence
   > We implement an entropy balancing procedure as a further approach to address a likely bias due to unobserved heterogeneity.
   Ctrl+F: „We implement an entropy balancing procedure as a“
   → Backs the 'entropy balancing' element coded in sample.

5. **sample** — p. 194 (PDF p. 7) — ✓ verified, 100% word sequence
   > our cross-sectional sample contains 5851 firms out of which 409 can be classified as AI users (about 7%)
   Ctrl+F: „our cross-sectional sample contains 5851 firms out of“
   → Confirms the coded sample size of 5,851 firms with 409 AI users (~7%).

6. **sample, quality_notes** — p. 194 (PDF p. 7) — ✓ verified, 100% word sequence
   > the average value of our AI intensity variable amounts to 12.9%, i.e., the average firm used 2.5 out of the 20 possible combinations of AI methods and areas of application
   Ctrl+F: „the average value of our AI intensity variable“
   → Backs the '2.5 of 20 method-area combos avg' detail in quality_notes.

7. **method** — p. 188 (PDF p. 1) — ✓ verified, 100% word sequence
   > We employ both a cross-sectional dataset and a panel database. To address the potential endogeneity of AI adoption, we also implement IV estimators.
   Ctrl+F: „a panel database. To address the potential endogeneity“
   → Names the econometric strategy (cross-section, panel, IV) coded as method = panel econometrics with OLS/2SLS-IV.

8. **ai_measure** — p. 194 (PDF p. 7) — ✓ verified, 100% word sequence
   > Any firm that uses at least one AI method by 2018 is considered an AI user ( AI ), including all firms that adopted AI at any year before 2018.
   Ctrl+F: „Any firm that uses at least one AI“
   → Defines the survey-based AI adoption dummy coded in ai_measure.

9. **ai_measure** — p. 194 (PDF p. 7) — ✓ verified, 100% word sequence
   > AIint represents the sum of different AI methods and AI application areas that are used by a firm, divided by the maximum possible number, which is 20
   Ctrl+F: „AIint represents the sum of different AI methods“
   → Defines the AI-use intensity measure coded in ai_measure (intensity of AI use in business processes).

10. **outcome_construct, performance_measure** — p. 189 (PDF p. 2) — ✓ verified, 80% word sequence
   > The general positive relationship between AI and firm productivity also holds both for sales-based and valueadded-based productivity measures.
   Ctrl+F: „The general positive relationship between AI and firm“
   → Names firm productivity (sales- and value-added-based) as the outcome, backing performance_measure and outcome_construct = performance.

11. **effect_direction, key_finding** — p. 188 (PDF p. 1) — ✓ verified, 100% word sequence
   > We find positive and significant associations between the use of AI and firm productivity. This finding holds for different measures of AI usage
   Ctrl+F: „We find positive and significant associations between the“
   → Abstract states a clear positive average main effect across AI measures, matching effect_direction = positive and the key_finding.

12. **effect_direction, key_finding** — p. 201 (PDF p. 14) — ✓ verified, 100% word sequence
   > we showed that both the use of AI and the intensity with which firms exploit the potential of AI significantly increase both sales and value-added
   Ctrl+F: „showed that both the use of AI and“
   → Conclusion's own statement of the central result: positive productivity effect for both the adoption dummy and the intensity measure.

13. **conditions** — p. 202 (PDF p. 15) — ✓ verified, 65% word sequence
   > So far, little is known about how these complementary assets might affect the relationship between AI adoption and firm performance
   Ctrl+F: „So far, little is known about how these“
   → Confirms conditions = empty: complementarities/moderators are explicitly framed as future research, not tested — matching the adjudicated 'unconditional evidence' classification.

14. **key_finding** — p. 198 (PDF p. 11) — ✓ verified, 100% word sequence
   > increasing the fraction of AI methods or areas would have, on average, a significant and positive ceteris paribus impact on productivity
   Ctrl+F: „or areas would have, on average, a significant“
   → Backs the 'effect grows with usage intensity' element of the coded key_finding.

15. **theoretical_lens** — p. 188 (PDF p. 1) — ✓ verified, 65% word sequence
   > Artificial Intelligence (AI) is often regarded as a new general-purpose technology, with a rapid, penetrating, and farreaching use over a broad number of industrial sectors
   Ctrl+F: „a rapid, penetrating, and far-reaching use over a“
   → Opens with the general-purpose-technology framing, matching theoretical_lens = GPT.

16. **quality_notes** — p. 201 (PDF p. 14) — ✓ verified, 100% word sequence
   > Our empirical findings are subject to several limitations. First, we rely on data from one country and we can currently construct only a very short panel database.
   Ctrl+F: „Our empirical findings are subject to several limitations.“
   → Authors' own limitation statement, the source-based part of quality_notes.

*Row check OK: conditions and ca_measure correctly empty: no moderators are tested (complementary assets explicitly deferred to future research, p.15) and no CA construct appears anywhere — the study is pure productivity econometrics. Adjudication brief confirms AI intensity is an alternative treatment measure, not a condition. Two author-side observations: (1) coded performance_measure says 'labor- and value-added-based' but the paper's own wording is 'sales-based and valueadded-based productivity measures' (p.2) — the sales-based production-function measure, not labor productivity per se; (2) evaluative parts of quality_notes ('one of the methodically strongest positive findings') are coder commentary — source-based parts (representative survey, IV strategy, 2.5/20 average intensity, one-country/short-panel limits) are quoted.*

---

## S13 — Huang C.K.T. et al. (2023) — Data Base for Advances in Information Systems (AJG 2)

DOI: 10.1145/3595863.3595866 · status: final · PDF: `Huang_2023_3595863-3595866.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 109 AI implementation announcements 2014-2019, S&P 500 components (Compustat) + Google Search event collection |
| method | event study |
| ai_measure | announcements (AI implementation) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm market value (positive abnormal returns on event day) |
| ca_measure | — |
| effect_direction | positive |
| conditions | announcement detail (detailed > vague); IT vs non-IT firms (sig. difference); frequency of negative words in announcement (negative correlation) |
| key_finding | Markets reward AI implementation announcements on average - more so when announcements are detailed and come from IT firms. |
| *not printed (coding data only)* | |
| theoretical_lens | business value of IT (event-study framing) |
| industry | cross-industry |
| quality_notes | Short-window event study; counterpoint to Lui 2022 (S08) \| SAMPLE-CHECK OK: event study/positive confirmed (109 announcements, positive abnormal returns) |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 15 (PDF p. 7) — ✓ verified, 100% word sequence
   > we downloaded data related to the S&P 500 Index from Compustat, including the components list, tickers, and GISC sectors of the components.
   Ctrl+F: „list, tickers, and GISC sectors of the components.“
   → Confirms S&P 500 components via Compustat (US large-cap firms across GICS sectors), backing sample, country_region = USA, and industry = cross-industry.

2. **sample** — p. 15 (PDF p. 7) — ✓ verified, 100% word sequence
   > we collected events from Google Search with these keywords and the names of the component companies from January 1, 2014 to February 3, 2019 (about 5 years)
   Ctrl+F: „these keywords and the names of the component“
   → Confirms the Google Search event collection and the 2014-2019 window coded in sample.

3. **sample** — p. 15 (PDF p. 7) — ✓ verified, 100% word sequence
   > we acquired 109 news reports concerning 30 companies
   Ctrl+F: „we acquired 109 news“
   → Confirms the adjudication-corrected count of 109 announcements coded in sample.

4. **method, theoretical_lens** — p. 10 (PDF p. 2) — ✓ verified, 100% word sequence
   > in this study, we investigate the business value of AI from a market perspective by adopting an event study methodology
   Ctrl+F: „the business value of AI from a market“
   → Names the business-value-of-IT framing and the event study methodology, matching theoretical_lens and method.

5. **ai_measure** — p. 15 (PDF p. 7) — ✓ verified, 100% word sequence
   > we defined an event as an announcement of artificial intelligence (AI) implementation in public news media
   Ctrl+F: „we defined an event as an announcement of“
   → Defines the AI measure as AI implementation announcements, matching ai_measure.

6. **outcome_construct, performance_measure** — p. 12 (PDF p. 4) — ✓ verified, 100% word sequence
   > An abnormal stock return is the difference between the actual return and the expected return and is usually used as an indicator of the impact of an event
   Ctrl+F: „An abnormal stock return is the difference between“
   → Defines the market-value outcome (abnormal returns) coded in performance_measure; outcome_construct = performance.

7. **performance_measure, effect_direction, key_finding** — p. 9 (PDF p. 1) — ✓ verified, 100% word sequence
   > in response to the announcement of AI implementation, we find significant positive abnormal returns on the event day
   Ctrl+F: „in response to the announcement of AI“
   → Abstract states the positive average main effect on the event day, matching effect_direction = positive and the coded performance_measure.

8. **effect_direction, key_finding, quality_notes** — p. 24 (PDF p. 16) — ✓ verified, 100% word sequence
   > The results show that these announcements have a significantly positive impact on abnormal returns. However, these impacts only last for a short period.
   Ctrl+F: „show that these announcements have a significantly“
   → Conclusion's own statement of the central result: markets reward AI announcements on average (positive), and the effect is short-window — backing the 'short-window event study' quality note.

9. **conditions, industry** — p. 14–16 (PDF p. 6) — ✓ verified, 100% word sequence
   > the third classification uses the GICS sectors to determine whether the company making the announcement is an IT company
   Ctrl+F: „the third classification uses the“
   → Shows the sample spans IT and non-IT sectors (cross-industry) and defines the IT vs non-IT grouping coded in conditions.

10. **conditions** — p. 9 (PDF p. 1) — ✓ verified, 100% word sequence
   > the results show significant differences in average cumulative abnormal returns between announcements with detailed information and those without detailed information
   Ctrl+F: „the results show significant differences in average cumulative“
   → Backs the coded condition 'announcement detail (detailed > vague)'.

11. **conditions, key_finding** — p. 9 (PDF p. 1) — ✓ verified, 100% word sequence
   > our findings present significant differences in average cumulative abnormal returns between IT-companies and non-IT companies on the event day
   Ctrl+F: „significant differences in average cumulative abnormal returns between“
   → Backs the coded condition 'IT vs non-IT firms (sig. difference)' and the 'come from IT firms' clause of key_finding.

12. **conditions** — p. 9 (PDF p. 1) — ✓ verified, 100% word sequence
   > according to the content analysis, only one characteristic, the frequency of negative words, is modestly and negatively correlated with average cumulative abnormal returns
   Ctrl+F: „the content analysis, only one characteristic, the“
   → Backs the coded condition 'frequency of negative words in announcement (negative correlation)'.

13. **conditions, key_finding** — p. 23 (PDF p. 15) — ✓ verified, 100% word sequence
   > when investors receive information short on details, the reaction is short and immediate. In comparison, when they receive detailed information, they need more time to digest it, leading to a delayed positive reaction
   Ctrl+F: „reaction is short and immediate. In comparison, when“
   → Discussion's interpretation of the detailed-information condition, backing the 'detailed > vague' condition and the key_finding clause on detailed announcements.

14. **theoretical_lens** — p. 10 (PDF p. 2) — ✓ verified, 100% word sequence
   > In the previous studies of business value of information technology (IT), most findings showed that the investments of transformational ITs have a positive impact on firms' market value
   Ctrl+F: „In the previous studies of business value of“
   → Anchors the study in the business-value-of-IT literature coded as theoretical_lens.

15. **quality_notes** — p. 24 (PDF p. 16) — ✓ verified, 100% word sequence
   > the values of abnormal returns that we have captured are investor perceptions, and thus represent not the actual values but the expected values of investors
   Ctrl+F: „abnormal returns that we have captured are“
   → Authors' own limitation on what the short-window market measure captures, the source-based part of quality_notes.

*Row check OK: All non-empty columns evidenced. ca_measure correctly empty: 'competitive advantage' appears only as motivating rhetoric (abstract, H1's RBV passage) with no CA construct measured — under the frozen rule that stays performance. The 'counterpoint to Lui 2022 (S08)' part of quality_notes is coder commentary, not source text; the source-based parts (short-window effect, investor-perception limitation, 109-event sample size) are quoted. Country USA is evidenced indirectly via S&P 500 components — the paper never states 'USA' as a word.*

---

## S14 — Krakowski S. et al. (2023) — Strategic Management Journal (AJG 4*)

DOI: 10.1002/smj.3387 · status: final · PDF: `krakowski2023artificial.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | multi-country (tournament data) |
| sample | same chess players across conventional, centaur and engine tournaments (controlled competitive setting) |
| method | panel econometrics |
| ai_measure | AI (engine) adoption in competitive interaction |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | competitive performance (game outcomes/ratings) |
| ca_measure | sources of persistent performance heterogeneity (= sustained advantage) across settings |
| effect_direction | conditional |
| conditions | substitution: traditional human capabilities become obsolete; complementation: new human-machine capabilities emerge that are unrelated or negatively related to traditional ones |
| key_finding | BENCHMARK: AI adoption shifts the sources of competitive advantage - a new decision-making resource emerges at the human-AI intersection, unrelated to traditional capability. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV |
| industry | non-firm setting (chess as controlled competition) |
| quality_notes | Chess setting = high internal validity, limited external validity to firms; SMJ 4* \| SAMPLE-CHECK OK: chess panel design verified in prior full read (benchmark) |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 1431 (PDF p. 7) — ✓ verified, 100% word sequence
   > This sampling procedure yields a sample of 112 unique players from 39 chess federations participating in 3,281 tournaments.
   Ctrl+F: „112 unique players from 39 chess federations participating“
   → Gives the sample size and the 39 federations backing country_region = multi-country (tournament data).

2. **sample, method, ai_measure** — p. 1430 (PDF p. 6) — ✓ verified, 62% word sequence
   > We use the controlled chess context to compare the same players' capabilities and performance across conventional, centaur, and engine chess tournaments.
   Ctrl+F: „We use the controlled chess context to compare“
   → Confirms the coded sample design: same players observed across the three tournament formats in a controlled competitive setting.

3. **method** — p. 1433 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 52% word sequence
   > we apply a multinomial logistic model (Powers & Xie, 2008) to estimate the factors contributing to the likelihood of one of the three possible game results (i.e., win, draw, or loss)
   Ctrl+F: „multinomial logistic model (Powers & Xie, 2008) to estimate“
   → Names the econometric estimation strategy on the tournament data, backing method = panel econometrics.

4. **method** — p. 1436 (PDF p. 12) — ✓ verified, 100% word sequence
   > We explore this tendency toward convergence further by estimating two fixed-effects panel models with standard errors clustered at the player level
   Ctrl+F: „We explore this tendency toward convergence further by“
   → Explicit fixed-effects panel estimation, backing method = panel econometrics.

5. **ai_measure, theoretical_lens** — p. 1425 (PDF p. 1) — ✓ verified, 100% word sequence
   > We apply a resource-based view to investigate how the adoption of Artificial Intelligence (AI) affects competitive capabilities and performance.
   Ctrl+F: „to investigate how the adoption of Artificial Intelligence“
   → Abstract names the RBV lens and AI adoption as the treatment, matching theoretical_lens = RBV and ai_measure.

6. **outcome_construct, performance_measure** — p. 1431 (PDF p. 7) — ✓ verified, 100% word sequence
   > Our primary measure of chess performance is the game result , namely a win, loss, or draw from the focal player's perspective (with a draw as a baseline outcome).
   Ctrl+F: „Our primary measure of chess performance is the“
   → Defines the competitive-performance outcome (game outcomes) coded in performance_measure, the performance half of outcome_construct = both.

7. **outcome_construct, ca_measure, key_finding** — p. 1443 (PDF p. 19) — ✓ verified, 100% word sequence
   > we find that AI adoption has a dualistic effect that shifts the sources of competitive advantage
   Ctrl+F: „we find that AI adoption has a dualistic“
   → Discussion's summary: AI adoption shifts the sources of competitive advantage — the CA half of outcome_construct = both and the first clause of key_finding.

8. **ca_measure, conditions, key_finding** — p. 1425 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 41% word sequence
   > Our analysis shows that AI adoption triggers interrelated substitution and complementation dynamics, which make humans ' traditional competitive capabilities obsolete, while creating new sources of persistent heterogeneity when humans interact with chess engines.
   Ctrl+F: „analysis shows that AI adoption triggers interrelated“
   → States both coded conditions (substitution makes traditional capabilities obsolete; complementation creates new capabilities) and the persistent-heterogeneity construct coded as ca_measure.

9. **ca_measure, effect_direction, key_finding** — p. 1425–1427 (PDF p. 1) — ✓ verified, 92% word sequence
   > a new decision-making resource emerges at the human-AI intersection, which drives performance but is unrelated or even negatively related to humans ' original capability
   Ctrl+F: „but is unrelated or even negatively related to“
   → The paper's own statement of the central result, matching the coded key_finding almost verbatim; performance depends on the new capability, backing effect_direction = conditional.

10. **effect_direction, conditions** — p. 1434 (PDF p. 10) — ⚠ not machine-confirmed on page — open the page, 22% word sequence
   > The centaur and engine game results presented in Table 1 suggest that the player capability effects largely vanish after the adoption of AI
   Ctrl+F: no reliable search string in the PDF text layer — open PDF p. 10 and check visually
   → Empirical substitution result: traditional human capabilities lose their performance effect once AI enters — the substitution condition and the reason direction is conditional rather than a simple main effect.

11. **effect_direction, conditions** — p. 1439 (PDF p. 15) — ✓ verified, 100% word sequence
   > The results in Table 3 show that these human -machine capabilities have new, significant effects on game results.
   Ctrl+F: „The results in Table 3 show that these“
   → Empirical complementation result: performance effects emerge only through the new human-machine capabilities, backing the complementation condition and effect_direction = conditional.

12. **conditions, key_finding** — p. 1443 (PDF p. 19) — ✓ verified, 62% word sequence
   > These results indicate that the new human -machine capabilities are unrelated, or even negatively related, to humans' traditional chess playing capabilities
   Ctrl+F: „These results indicate that the new“
   → Backs the coded condition that the new capabilities are unrelated or negatively related to traditional ones, and the 'unrelated to traditional capability' clause of key_finding.

13. **industry, quality_notes** — p. 1430 (PDF p. 6) — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > The advantage of chess is that it provides a controlled context in which actors' capabilities, as well as the quality and sequence of their actions, are consistently identifiable and comparable
   Ctrl+F: „The advantage of chess is that it provides“
   → Confirms industry = non-firm setting (chess as controlled competition) and the high-internal-validity part of quality_notes.

14. **industry, quality_notes** — p. 1430 (PDF p. 6) — ✓ verified, 89% word sequence
   > Studying competitive strategy in a chess context has certain limitations. The most important of these is that chess is a well-defined game with a lower degree of uncertainty than most strategic actions in business settings
   Ctrl+F: „Studying competitive strategy in a chess context has“
   → Authors' own admission of limited external validity to business settings, the source-based part of quality_notes.

15. **quality_notes** — p. 1446 (PDF p. 22) — ✓ verified, 96% word sequence
   > Our research has a significant limitation in that we have provided empirical evidence from just one domain -chess competitions -in which complete substitution occurs.
   Ctrl+F: „Our research has a significant limitation in that“
   → Authors' explicit single-domain limitation, backing the limited-external-validity note in quality_notes.

*Row check OK: All non-empty columns evidenced. effect_direction = conditional is consistent with the frozen rules: there is no average main effect of AI on performance — traditional capability effects vanish (substitution) and performance differences exist only through the new human-machine capabilities (complementation). The 'SMJ 4*' and 'SAMPLE-CHECK OK' parts of quality_notes are coder metadata, not source text; the source-based limitation statements are quoted. country_region 'multi-country' rests on the 39-federations sample statement — the paper reports no country-level breakdown.*

---

## S15 — Samadhiya A. et al. (2023) — Industrial Marketing Management (AJG 3)

DOI: 10.1016/j.indmarman.2023.11.002 · status: final · PDF: `Samadhiya_2023_j-indmarman-2023-11-002.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India |
| sample | in-depth interviews with senior B2B managers + PLS-SEM on 142 responses |
| method | mixed |
| ai_measure | survey construct (AI-based partner relationship management implementation) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | perceived firm performance (survey scale) |
| ca_measure | perceived sustainable competitiveness (survey scale) |
| effect_direction | positive |
| conditions | ICT capability (prerequisite); technological readiness (prerequisite); firm fit |
| key_finding | AI-based partner relationship management improves firm performance and sustainable competitiveness, provided ICT capability and technological readiness are in place. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capability view + RBV |
| industry | cross-industry (B2B) |
| quality_notes | Perceptual, mixed methods |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 516 (PDF p. 7) — ✓ verified, 100% word sequence
   > The data were collected from January to March of 2023, focusing on Indian B2B firms that use information and communication technology capabilities for decision-making related to AIPRM.
   Ctrl+F: „The data were collected from January to March“
   → Confirms country_region = India and the survey population of the coded sample.

2. **sample, method, industry** — p. 510 (PDF p. 1) — ✓ verified, 100% word sequence
   > A mixed-methods approach was employed that involves in-depth interviews with senior managers from a diverse set of B2B firms
   Ctrl+F: „employed that involves in-depth interviews with senior managers“
   → Confirms method = mixed and the interview component of the coded sample; 'diverse set of B2B firms' backs industry = cross-industry (B2B).

3. **sample, method** — p. 510 (PDF p. 1) — ✓ verified, 100% word sequence
   > the proposed hypothesis model was evaluated by analysing the collected B2B data of 142 responses using partial least squares structural equation modelling
   Ctrl+F: „proposed hypothesis model was evaluated by analysing the“
   → Confirms the quantitative strand: PLS-SEM on 142 responses, as coded in sample.

4. **ai_measure, outcome_construct, theoretical_lens** — p. 510 (PDF p. 1) — ✓ verified, 74% word sequence
   > Drawing on the dynamic capability view and resource-based view, this study investigates the relationship among artificial intelligence (AI)-based partner relationship management, firm performance, and sustainable competitiveness concerning the climate management of business-to-business (B2B) firms.
   Ctrl+F: „Drawing on the dynamic capability view and resource-based“
   → Abstract names DCV + RBV (theoretical_lens), AIPRM as the AI construct, and the two outcomes (firm performance and sustainable competitiveness) coded as outcome_construct = both.

5. **ai_measure, industry** — p. 516 (PDF p. 7) — ✓ verified, 100% word sequence
   > The researchers used a structured study questionnaire to gather data from organisations that have implemented climate-focused initiatives, including the adoption of environmentally friendly technology and the integration of AI-enabled services into their B2B firms' operations.
   Ctrl+F: „questionnaire to gather data from organisations that have“
   → Backs the climate-management B2B context coded in industry and the survey-based AI implementation measure.

6. **ai_measure, conditions** — p. 516 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 53% word sequence
   > the selected items were used as follows: information and communication technology capabilities (4 items), B2B firm technological readiness (4 items), B2B firm fit (4 items), artificial intelligence partner relationship management (4 items)
   Ctrl+F: „the selected items were used as follows: information“
   → Shows AIPRM is measured as a 4-item survey construct (ai_measure) alongside the three condition constructs.

7. **outcome_construct, ca_measure, effect_direction, key_finding** — p. 510 (PDF p. 1) — ✓ verified, 100% word sequence
   > Furthermore, the implementation of AI-based partner relationship management in B2B firms would help partner engagement and information processing systems for climate management, leading to sustainable firm competitiveness.
   Ctrl+F: „management in B2B firms would help partner engagement“
   → Abstract's statement of the central positive result chain ending in sustainable competitiveness, backing key_finding and the CA half of outcome_construct = both.

8. **outcome_construct, performance_measure, ca_measure** — p. 516 (PDF p. 7) — ✓ verified, 100% word sequence
   > B2B firms' partner engagement for climate management (4 items), B2B firms' information processing for climate management (4 items), B2B firm performance (5 items), and B2B firm sustainable competitiveness (5 items)
   Ctrl+F: „engagement for climate management (4 items), B2B firms'“
   → Shows firm performance and sustainable competitiveness are separate multi-item survey scales, backing performance_measure, ca_measure, and outcome_construct = both.

9. **performance_measure, quality_notes** — p. 519 (PDF p. 10) — ✓ verified, 100% word sequence
   > We believe that AIPRM is helping the company expand financially.
   Ctrl+F: „AIPRM is helping the company expand“
   → Example firm-performance item (FP5) showing the outcome is a perceptual survey scale, backing 'perceived firm performance' and the 'perceptual' quality note.

10. **ca_measure** — p. 511 (PDF p. 2) — ✓ verified, 62% word sequence
   > The term ' sustainable competitiveness ' refers to a company's capacity to fulfil the demands of current shareholders without jeopardising future generations' ability to do the same
   Ctrl+F: „refers to a company's capacity to fulfil the“
   → The paper's definition of the sustainable-competitiveness construct coded as ca_measure.

11. **effect_direction, key_finding** — p. 520 (PDF p. 11) — ⚠ not machine-confirmed on page — open the page, 44% word sequence
   > As a result of the fact that the β value for each of the hypotheses is positive, with corresponding p values of lower than 0.05, we may conclude that all eight hypotheses can be accepted.
   Ctrl+F: „As a result of the fact that the“
   → All eight paths positive and significant, backing effect_direction = positive.
   **⚠ TENSION:** The model contains no direct AIPRM->firm-performance path: AIPRM reaches FP only via the mediators partner engagement (H4/H6) and information processing (H5/H7), and SC only via FP (H8). Under the frozen 'no direct path modeled' precedent (S21, S28) this pattern could argue for conditional; unlike those cases, however, every path here is positive and significant, which supports the final coding of positive with the prerequisites recorded in conditions.

12. **conditions, key_finding** — p. 510 (PDF p. 1) — ✓ verified, 85% word sequence
   > The findings of the study show that information communication technology capability and technological readiness play a significant role in improving the performance of AIbased partner relationship management.
   Ctrl+F: „The findings of the study show that information“
   → Backs the 'provided ICT capability and technological readiness are in place' clause of key_finding and the two prerequisite conditions.

13. **conditions** — p. 510 (PDF p. 1) — ✓ verified, 100% word sequence
   > the study additionally explored the impact of several other dimensions, including information communication technology capability, firm fit, and technological readiness, as fundamental requirements for the implementation of AI-based partner relationship management
   Ctrl+F: „the study additionally explored the impact of several“
   → Names all three coded conditions (ICT capability, technological readiness, firm fit) as fundamental requirements/prerequisites.

14. **conditions** — p. 513 (PDF p. 4) — ✓ verified, 100% word sequence
   > information and communication technology capability, firm technological readiness, and firm fit are prerequisite to implementing AIPRM as all three of them positively affects AIPRM
   Ctrl+F: „readiness, and firm fit are“
   → Table 1's own summary of the present study: the three coded conditions are prerequisites with positive effects on AIPRM.

15. **quality_notes** — p. 523 (PDF p. 14) — ✓ verified, 62% word sequence
   > the current research focuses only on the external elements that influence adoption and implementation; no consideration is given here to the internal aspects that may affect a company's capacity to build AIPRM capabilities
   Ctrl+F: „current research focuses only on the external elements“
   → Authors' own limitation statement, source-based support for quality_notes.

**⚠ ROW CHECK:** All non-empty columns evidenced. Two points for the author: (1) tension flagged on the effect_direction quote — the structural model has no direct AIPRM->performance path (serial mediation via partner engagement and information processing, Table 6 p.12), which resembles the S21/S28 'no direct path modeled -> conditional' precedent, though here all eight paths are positive and significant; relatedly, the mediators FPE/FIP are not listed in conditions (only the three prerequisites are). (2) method = mixed rests on Section 3.1 (p.6): the interview stage 'critically examin[ed] the study's hypotheses' with 'widespread agreement', i.e., it carried some evidential weight beyond instrument piloting — consistent with the mixed coding under the case law, but worth a look since the pilot-phase wording also mentions questionnaire refinement. Cross-industry is additionally supported by Table 3 (p.10): IT services and consulting, logistics, finance and banking, manufacturing.

---

## S16 — Wu C.W. et al. (2023) — Psychology and Marketing (AJG 3)

DOI: 10.1002/mar.21737 · status: final · PDF: `Wu_2023_mar-21737.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Taiwan |
| sample | 278 CEO/marketing-manager responses (food franchises and chain stores), Taiwan, survey Mar-Aug 2020, RR 33%; SEM + supplementary fsQCA |
| method | survey-SEM |
| ai_measure | survey construct (implementation of AI marketing strategy) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | perceived firm performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | fsQCA configurations: marketing capabilities + customer value co-creation + market orientation + AI strategy jointly form necessary and sufficient recipes for high performance |
| key_finding | AI marketing strategy raises firm performance, but only as part of configurations with marketing capabilities, co-creation and market orientation - a configurational result. |
| *not printed (coding data only)* | |
| theoretical_lens | marketing capabilities / market orientation (no grand theory) |
| industry | food service and retail (franchises, chain stores) |
| quality_notes | Perceptual; fsQCA as supplementary configurational analysis (necessary/sufficient recipes) - Fredrich-relevant detail lives in conditions column |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > This study uses questionnaire data from a survey of CEO and marketing managers inTaiwan between March and August 2020
   Ctrl+F: „from a survey of CEO and marketing managers“
   → Backs respondents (CEO/marketing managers), country Taiwan, and the survey window Mar-Aug 2020; 'inTaiwan' spacing is an extraction artifact.

2. **sample** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > The final sample size was 278 participants, with a response rate of 33.01%.
   Ctrl+F: „The final sample size was 278 participants, with“
   → Backs n = 278 firms and the 33% response rate in the coded sample.

3. **sample, industry** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > The study uses food franchises and chain stores to obtain information on the selected firms, and AI development is an important criterion to consider.
   Ctrl+F: „stores to obtain information on the selected firms,“
   → Backs the food-industry setting; note the sample is food franchises/chain stores (incl. coffee shops, restaurants), not manufacturing plants.

4. **method** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > This study used SEM analysis to test the hypotheses after testing the validity of the measurement model.
   Ctrl+F: „This study used SEM analysis to test the“
   → SEM is the hypothesis-testing strategy, backing the adjudicated method = survey-SEM.

5. **method, quality_notes** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > Ragin (2008) and Woodside (2013) emphasize fsQCA analysis to supplement SEM or regression analysis.
   Ctrl+F: „emphasize fsQCA analysis to supplement SEM or regression“
   → The paper itself positions fsQCA as supplementary to SEM, backing the adjudicated decision that two quantitative methods on the same data do not make the study mixed and the quality note's 'supplementary configurational analysis'.

6. **ai_measure** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > Finally, the research measures AI marketing strategy using 11 items adapted from Casillas and Martínez -López (2009) and Davenport (2016).
   Ctrl+F: „marketing strategy using 11 items adapted from Casillas“
   → AI is measured as a multi-item survey construct (implementation of AI marketing strategy), as coded.

7. **outcome_construct, performance_measure** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > The research measures performance using four items adapted from Rego et al. (2013) and Stewart (2009).
   Ctrl+F: „measures performance using four items adapted from Rego“
   → The outcome is a perceptual multi-item performance scale; no distinct CA construct is hypothesized or measured, backing outcome_construct = performance.

8. **performance_measure, ca_measure** — p. 489 (PDF p. 6) — ✓ verified, 100% word sequence
   > Please compare your firm's performance to your competitors' performance over the last 5 years
   Ctrl+F: „Please compare your firm's performance to your competitors'“
   → Table 2 shows the performance items (profit, customer satisfaction, sales growth, quality) are competitor-anchored.
   **⚠ TENSION:** Performance scale is anchored relative to competitors; under S05 case law relative-vs-competitor scales are CA boundary cases. Construct is named 'Performance' with no CA hypothesis, so performance/ca_measure-empty follows the frozen rule, but the author may want to see this anchor.

9. **performance_measure, effect_direction** — p. 491 (PDF p. 8) — ✓ verified, 100% word sequence
   > the results show that AI marketing strategy positively impacts organizational performance in terms of increase in profits, quality of service/ products, sales growth, and customer satisfaction
   Ctrl+F: „show that AI marketing strategy positively impacts organizational“
   → The paper's own statement of a positive AI-strategy effect on the four performance facets.

10. **effect_direction** — p. 488 (PDF p. 5) — ✓ verified, 100% word sequence
   > The structural model fit supports all six proposed research hypotheses
   Ctrl+F: „supports all six proposed research hypotheses:“
   → All hypotheses incl. H2 (AI marketing strategy -> performance, 0.62**) are supported — a clear positive main effect, backing effect_direction = positive.

11. **conditions, key_finding** — p. 484 (PDF p. 1) — ✓ verified, 100% word sequence
   > The research results of FsQCA find that causal conditions of marketing capabilities, customer value co -creation, market orientation, and AI marketing strategy are necessary and sufficient recipes for higher firm performance.
   Ctrl+F: „The research results of FsQCA find that causal“
   → Backs the coded fsQCA configurations (capabilities + co-creation + market orientation + AI strategy as necessary/sufficient recipes) and the configurational key finding.

12. **conditions, key_finding** — p. 492 (PDF p. 9) — ✓ verified, 100% word sequence
   > The results also indicate that marketing capabilities, customer value co -creation, market orientation, and AI marketing strategy are not individually relevant; they must be combined to enhance performance.
   Ctrl+F: „and AI marketing strategy are not individually relevant;“
   → The paper's central configurational conclusion: AI strategy raises performance only in combination with the other conditions.

13. **theoretical_lens** — p. 486 (PDF p. 3) — ✓ verified, 100% word sequence
   > Thus, AI marketing strategy implementation is based on marketing capabilities with scarcity, value, inimitability, and nonsubstitutability to achieve competitive advantage
   Ctrl+F: „based on marketing capabilities with scarcity, value, inimitability,“
   → Shows the marketing-capabilities framing (with RBV language) used to derive the hypotheses, matching the coded lens.

14. **theoretical_lens** — p. 485 (PDF p. 2) — ✓ verified, 100% word sequence
   > it seems appropriate to argue that AI marketing strategies and market orientation is an important antecent for company performance
   Ctrl+F: „it seems appropriate to argue that AI marketing“
   → Market orientation is the second pillar of the coded lens; typo 'antecent' is in the original.

15. **quality_notes** — p. 487 (PDF p. 4) — ✓ verified, 100% word sequence
   > Measures capture CEO and marketing managers' perceptions of the relationship with their marketing environment, AI marketing strategy, and performance.
   Ctrl+F: „Measures capture CEO and marketing managers' perceptions of“
   → Backs the 'perceptual' quality note: all constructs including performance are manager perceptions.

**⚠ ROW CHECK:** (1) industry coded 'food manufacturing', but the sample is food franchises and chain stores (fast food, coffee shops, restaurants, beverages, food sales, Table 1) — food service rather than manufacturing; author should confirm the label. (2) Lens coded '(no grand theory)' although the paper explicitly invokes RBV in hypothesis development (pp. 2-3) and discussion (p. 9); lens content (marketing capabilities / market orientation) itself is well evidenced. (3) Performance scale is competitor-anchored (see tension quote); ca_measure = empty remains consistent with the frozen rules. (4) The 'Fredrich-relevant detail lives in conditions column' part of quality_notes is coder commentary, not source-based — no quote possible.

---

## S17 — Babina T. et al. (2024) — Journal of Financial Economics (AJG 4*)

DOI: 10.1016/j.jfineco.2023.103745 · status: final · PDF: `Babina_2024_j-jfineco-2023-103745.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 1,993 US Compustat firms; resume-based AI workforce measure (Cognism), robust to job-postings measure; IV = university AI graduate supply |
| method | panel econometrics |
| ai_measure | resume-based (share of AI-skilled workers as firm AI investment) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | growth in sales, employment, and market valuation |
| ca_measure | — |
| effect_direction | positive |
| conditions | channel: product innovation (not process efficiency); gains concentrate among ex-ante LARGER firms -> rising industry concentration (superstar dynamics) |
| key_finding | BENCHMARK: AI-investing firms grow in sales, employment and value via product innovation; benefits concentrate among large firms, increasing concentration. |
| *not printed (coding data only)* | |
| theoretical_lens | GPT / economics of technology (no management lens) |
| industry | cross-industry |
| quality_notes | IV strategy, very rigorous; JFE 4* |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, sample, ai_measure** — PDF p. 6, 3.1. Employment profiles from Cognism — ✓ verified, 100% word sequence
   > Of the 657 million US-based person-firm-year employment records between 2007 and 2018, 120 million (18%) are matched to U.S. public firms
   Ctrl+F: „employment records between 2007 and 2018, 120“
   → Backs the US setting, the Compustat/public-firm sample frame, and the Cognism resume data base.

2. **sample, quality_notes** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > Our results are robust to instrumenting AI investments using firms' exposure to universities' supply of AI graduates.
   Ctrl+F: „Our results are robust to instrumenting AI investments“
   → Backs the IV = university AI graduate supply noted in sample and the 'IV strategy, very rigorous' quality note.

3. **sample** — PDF p. 9, 4.4. Firm-level determinants of AI investments — ✓ verified, 100% word sequence
   > we further restrict to firms with at least 20 U.S. jobs in both 2010 and 2018 to ensure good coverage of the firm's workforce, which leaves us with 1,993 firms
   Ctrl+F: „U.S. jobs in both 2010 and 2018 to“
   → Backs the coded n = 1,993 firms.

4. **sample, ai_measure** — PDF p. 2, 1. Introduction — ⚠ not machine-confirmed on page — open the page, 0% word sequence
   > Encouragingly, the two measures of AI investments, although based on two independent datasets, are highly correlated and yield consistent results.
   Ctrl+F: „the two measures of AI investments, although based“
   → Backs 'robust to job-postings measure' in the coded sample: the resume-based and Burning Glass measures agree.

5. **method** — PDF p. 10, 5.1. Long-differences results — ⚠ not machine-confirmed on page — open the page, 31% word sequence
   > our primary specification is a long-differences regression of changes in firm outcomes from 2010 to 2018 on changes in AI investments proxied by the share of AI workers
   Ctrl+F: „in AI investments proxied by the share of“
   → The AI-to-outcome evidence comes from firm-level long-differences regressions, backing method = panel econometrics.

6. **method, quality_notes** — PDF p. 2, 1. Introduction — ⚠ not machine-confirmed on page — open the page, 52% word sequence
   > We find no pre-trends in firm growth prior to AI investments, confirming that AI-investing firms are not on differential growth trends
   Ctrl+F: „no pre-trends in firm growth prior to AI“
   → Dynamic lead-lag panel evidence against reverse causality, backing the econometric-rigor quality note.

7. **ai_measure** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > We propose a new measure of firm-level AI investments using employee resumes.
   Ctrl+F: „We propose a new measure of firm-level AI“
   → Backs the resume-based AI investment measure.

8. **outcome_construct, performance_measure, effect_direction, conditions** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > AI-investing firms experience higher growth in sales, employment, and market valuations. This growth comes primarily through increased product innovation.
   Ctrl+F: „experience higher growth in sales, employment, and market“
   → Clear positive main effect on the three coded growth outcomes; product innovation named as the channel (coded under conditions).

9. **performance_measure, effect_direction** — PDF p. 2, 1. Introduction — ⚠ not machine-confirmed on page — open the page, 45% word sequence
   > a one-standard-deviation increase in the resume-based measure of AI investments over the 8-year period corresponds to a 19.5% increase in sales, a 18.1% increase in employment, and a 22.3% increase in market valuation
   Ctrl+F: „the resume-based measure of AI investments over the“
   → Quantified positive main effects on all three coded outcome measures.

10. **conditions, key_finding** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > AI-powered growth concentrates among larger firms and is associated with higher industry concentration. Our results highlight that new technologies like AI can contribute to growth and superstar firms through product innovation.
   Ctrl+F: „associated with higher industry concentration. Our results highlight“
   → Backs the coded condition (gains concentrate among larger firms, superstar dynamics) and the key finding.

11. **conditions** — PDF p. 3, 1. Introduction — ✓ verified, 93% word sequence
   > Empirically, we do not find support for this second channel. AI investments are not associated with changes in sales per worker, total factor productivity, or process patents
   Ctrl+F: „support for this second channel. AI investments are“
   → Backs the coded channel contrast: product innovation, not process efficiency/cost reduction.

12. **conditions** — PDF p. 3, 1. Introduction — ✓ verified, 100% word sequence
   > the positive relationship between AI investments and firm growth is much stronger among ex-ante larger firms, consistent with the theories where AI can increase inequality by favoring large firms with more data
   Ctrl+F: „the theories where AI can increase inequality by“
   → Backs the coded condition that gains concentrate among ex-ante larger firms.

13. **conditions, key_finding** — PDF p. 19, 8. Conclusion — ✓ verified, 96% word sequence
   > This AI-fueled growth does not appear to stem from cost-cutting; instead, AI-investing firms expand through product innovation and increased product offerings.
   Ctrl+F: „This AI-fueled growth does not appear to stem“
   → Restates the product-innovation (not cost/process) channel that the coded key finding and conditions record.

14. **key_finding** — PDF p. 19, 8. Conclusion — ✓ verified, 65% word sequence
   > We find a positive feedback loop between AI investments and firm size: AI investments concentrate among the largest firms, and as firms invest in AI, they grow larger, gaining sales, employment, and market share.
   Ctrl+F: „a positive feedback loop between AI investments and“
   → The paper's own summary of its central result, matching the coded key finding.

15. **theoretical_lens, industry** — PDF p. 2, 1. Introduction — ✓ verified, 100% word sequence
   > The results are ubiquitous across major industry sectors (e.g., manufacturing, finance, and retail), supporting the idea that AI is a general purpose technology.
   Ctrl+F: „supporting the idea that AI is a general“
   → Backs industry = cross-industry and the GPT lens.

16. **theoretical_lens** — PDF p. 3, 2.1. Artificial intelligence: a brief overview — ✓ verified, 60% word sequence
   > Second, economists have argued that AI is a general purpose technology (GPT) and can be leveraged across different business segments and sectors to solve a wide range of business problems.
   Ctrl+F: „a general purpose technology“
   → Backs the coded GPT / economics-of-technology lens.

*Row check OK: ca_measure = empty confirmed: no firm-level competitive-advantage construct is measured; market-share/concentration results are industry-level outcomes, so outcome_construct = performance is consistent with the frozen rules. The 'JFE 4*' part of quality_notes is coder commentary (AJG rating), not source-based — no quote possible. PDF has no printed pagination (article-numbered Elsevier); pdf_page = article-internal page, sections recorded.*

---

## S18 — Cannas V.G. et al. (2024) — International Journal of Production Research (AJG 3)

DOI: 10.1080/00207543.2023.2232050 · status: final · PDF: `Cannas_2024_00207543-2023-2232050.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Italy |
| sample | multiple case study: 6 companies, 17 AI implementation cases, semi-structured interviews |
| method | case study |
| ai_measure | case observation (AI applications in SCOR processes) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | qualitative competitiveness outcomes: costs, lead times, service level, quality, safety, sustainability |
| ca_measure | — |
| effect_direction | positive |
| conditions | barriers as boundary conditions: data quality, AI skills, high investment needs, unclear economic benefits, lack of AI cost-analysis experience |
| key_finding | AI improves supply-chain competitiveness across SCOR processes, but realization depends on overcoming data-quality, skill and investment-evaluation barriers. |
| *not printed (coding data only)* | |
| theoretical_lens | SCOR process framework (OM) |
| industry | manufacturing / supply chain |
| quality_notes | Qualitative multi-case; authors explicitly disclaim generalization |
| coding_status | final |

### Evidence

1. **country_region, sample, ai_measure** — p. 3353 (PDF p. 22) — ✓ verified, 100% word sequence
   > It analyses empirical data concerning 17 applications of AI to the SCOR processes within six Italian companies.
   Ctrl+F: „empirical data concerning 17 applications of AI to“
   → Backs the Italian setting, the 6-firm/17-case sample, and AI measured as observed applications in SCOR processes.

2. **country_region, sample** — p. 3344 (PDF p. 13) — ✓ verified, 100% word sequence
   > A total of six Italian companies were selected.
   Ctrl+F: „A total of six Italian companies were selected.“
   → Direct statement of country = Italy and the six-firm sample.

3. **sample, method** — p. 3333 (PDF p. 2) — ✓ verified, 100% word sequence
   > To this end, it conducts a multiple case study with semi-structured interviews in six companies, totalling 17 implementation cases.
   Ctrl+F: „To this end, it conducts a multiple case“
   → Backs method = case study and the coded sample (6 companies, 17 AI implementation cases, semi-structured interviews).

4. **ai_measure** — p. 3344 (PDF p. 13) — ✓ verified, 100% word sequence
   > the focus of this study and the unit of analysis is the AI application
   Ctrl+F: „the focus of this study and the unit“
   → AI is captured as case observation of concrete AI applications, matching the coded ai_measure.

5. **outcome_construct, performance_measure, effect_direction, key_finding** — p. 3333 (PDF p. 2) — ✓ verified, 100% word sequence
   > The results highlighted how AI methods in OSCM can increase the companies' competitiveness by reducing costs and lead times and improving service levels, quality, safety, and sustainability.
   Ctrl+F: „The results highlighted how AI methods in OSCM“
   → Backs the coded qualitative outcome list (costs, lead times, service level, quality, safety, sustainability) and the positive direction; per adjudication, 'competitiveness' here means operational improvements = performance.

6. **outcome_construct, ca_measure** — p. 3333 (PDF p. 2) — ✓ verified, 100% word sequence
   > Artificial intelligence (AI) is increasingly considered a source of competitive advantage in operations and supply chain management (OSCM).
   Ctrl+F: „Artificial intelligence (AI) is increasingly considered a source“
   → The only CA language is framing rhetoric in the opening sentence; no CA construct is measured, backing outcome_construct = performance (adjudicated) and ca_measure = empty.

7. **effect_direction** — p. 3352 (PDF p. 21) — ✓ verified, 100% word sequence
   > AI projects that have been implemented by companies have had an impact on reducing costs and improving the efficiency of production processes
   Ctrl+F: „projects that have been implemented by companies have“
   → The discussion states across-case positive operational effects, backing effect_direction = positive with barriers relegated to conditions per adjudication.

8. **conditions, key_finding** — p. 3333 (PDF p. 2) — ✓ verified, 100% word sequence
   > barriers in the implementation of AI, such as ensuring data quality, lack of specific skills, need for high investments, lack of clarity on economic benefits and lack of experience in cost analysis for AI projects
   Ctrl+F: „barriers in the implementation of AI, such as“
   → Backs the coded barrier conditions verbatim (data quality, AI skills, investment needs, unclear economic benefits, cost-analysis inexperience) and the key finding's dependency clause.

9. **conditions** — p. 3350 (PDF p. 19) — ⚠ not machine-confirmed on page — open the page, 36% word sequence
   > The results of this study underlined nine main barriers tackled by companies when implementing AI projects, belonging to the financial, organisational, strategic, and technological categories.
   Ctrl+F: „The results of this study underlined nine main“
   → Results chapter confirms barriers as identified boundary conditions of AI benefit realization.

10. **theoretical_lens** — p. 3333 (PDF p. 2) — ✓ verified, 86% word sequence
   > The Supply Chain Operations Reference (SCOR) model guided the entire study and the analysis of the results by targeting specific processes.
   Ctrl+F: „Operations Reference (SCOR) model guided the entire study“
   → Backs the coded SCOR process framework as the study's organizing lens.

11. **industry** — p. 3344 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 47% word sequence
   > The complete list of companies operating in the Italian manufacturing and service industries was extracted from the database 'AIDA'
   Ctrl+F: „The complete list of companies operating in the“
   → Backs the manufacturing/supply-chain industry coding; the six selected cases (Table 3) are manufacturing, textile, and oil-and-gas firms.

12. **quality_notes** — p. 3354 (PDF p. 23) — ✓ verified, 100% word sequence
   > it is a qualitative methodology based on a limited set of companies, which makes it possible to deeply analyse cases but difficult to generalise the results obtained
   Ctrl+F: „methodology based on a limited set of companies,“
   → The authors' own limitation statement backs the quality note that generalization is explicitly disclaimed.

*Row check OK: All non-empty columns evidenced. ca_measure = empty confirmed: 'competitive advantage' appears only as framing in the abstract's opening; the measured outcomes are operational improvements (adjudicated to performance/positive). Coded industry 'manufacturing / supply chain' is consistent with Table 3 (five manufacturing-type firms plus textile and oil-and-gas).*

---

## S19 — Pesqueira A. et al. (2024) — Computers and Industrial Engineering (AJG 2)

DOI: 10.1016/j.cie.2024.110655 · status: final · PDF: `Pesqueira_2024_j-cie-2024-110655.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Europe (EU tendering context) |
| sample | comparative 4 pharma companies (2 AI adopters vs 2 non-adopters) + 2-round Delphi with 53 participants |
| method | mixed |
| ai_measure | adoption status (AI in tender management) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | operational efficiency in tender management (processing times, decision quality, document accuracy) - expert-rated/qualitative |
| ca_measure | expert-rated competitiveness dimensions per company (Delphi, Likert+IQR); bid competitiveness in tendering context |
| effect_direction | conditional |
| conditions | governance and ethical frameworks (contingency, per conclusions); regulatory compliance (EU AI Act, GDPR); organizational readiness; senior management involvement (identified critical factor); alignment with business goals |
| key_finding | AI adopters manage pharmaceutical tendering faster and with better decisions than non-adopters, but only sustainably within robust governance and compliance structures. |
| *not printed (coding data only)* | |
| theoretical_lens | governance/compliance frameworks (no grand theory) |
| industry | pharmaceuticals |
| quality_notes | Dual-method: comparative 4-firm cases + 2-round Delphi (53 participants) with quantified consensus; expert-judgment based evidence |
| coding_status | final |

### Evidence

1. **country_region, conditions, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > aligning the adoption of AI with the latest European directives, such as the AI Act and General Data Protection Regulation (GDPR), to ensure both operational efficiency and adherence to ethical standards
   Ctrl+F: „aligning the adoption of AI with the latest“
   → Backs the coded regulatory-compliance conditions (EU AI Act, GDPR) and the European context.

2. **country_region, industry** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > The European tendering system plays a pivotal role in guaranteeing that healthcare providers can obtain essential medicines at competitive prices.
   Ctrl+F: „system plays a pivotal role in guaranteeing that“
   → Backs the EU tendering context and the pharmaceutical industry coding.

3. **sample, method, ai_measure, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > A comparative analysis of four companies -two that have adopted AI and two that have not -reveals significant discrepancies in the management of TM processes between AI-driven and traditional companies.
   Ctrl+F: „significant discrepancies in the management of TM processes“
   → Backs the comparative 4-firm design, the adopter-vs-non-adopter contrast as the AI measure, and the tender-management setting.

4. **sample, method** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > the study employs a comparative case study approach, in which four pharmaceutical companies are analyzed and 53 involved participants in interviews and Delphi rounds
   Ctrl+F: „study approach, in which four pharmaceutical companies are“
   → Backs the coded sample: 4 pharma companies plus 53 Delphi/interview participants; both strands carry outcome evidence (adjudicated mixed).

5. **sample, method, quality_notes** — p. 17 (PDF p. 17) — ✓ verified, 100% word sequence
   > These were designed to assess the likelihood and impact of various scenarios in the two rounds of discussions and interviews.
   Ctrl+F: „These were designed to assess the likelihood and“
   → Backs the 2-round Delphi design in sample and the dual-method quality note.

6. **method, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study employs the Delphi method to ascertain expert consensus on eight critical areas of AI governance, including data privacy, transparency, and ethical AI use.
   Ctrl+F: „The study employs the Delphi method to ascertain“
   → Backs the second evidential strand (Delphi) of the adjudicated mixed method and the governance/compliance framing coded as lens.

7. **outcome_construct, performance_measure, effect_direction, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The findings indicate that companies integrating AI demonstrate enhanced decision-making capabilities, accelerated processing times, and enhanced stakeholder engagement. However, they also encounter challenges pertaining to ethical governance and regulatory compliance.
   Ctrl+F: „demonstrate enhanced decision-making capabilities, accelerated processing times, and“
   → Backs the operational-efficiency outcome (processing times, decision quality) as the performance side of 'both' and the governance caveat behind the conditional coding.

8. **outcome_construct, ca_measure** — p. 16 (PDF p. 16) — ✓ verified, 96% word sequence
   > AI also supports dynamic pricing strategies by analyzing competitor pricing, demand elasticity, and cost structures, thus recommending optimal bid prices that maximize both competitiveness and profitability.
   Ctrl+F: „also supports dynamic pricing strategies by analyzing competitor“
   → Backs 'bid competitiveness in tendering context' as the CA side of the coded 'both'.

9. **outcome_construct, ca_measure, effect_direction** — p. 19 (PDF p. 19) — ✓ verified, 100% word sequence
   > These companies are better positioned to leverage real-time data analysis, optimize tendering strategies, and maintain competitive advantages in a rapidly evolving market.
   Ctrl+F: „leverage real-time data analysis, optimize tendering strategies, and“
   → Competitor-comparative CA statement about the AI adopters, backing outcome_construct = both (adjudicated: CA expert-rated in tender context).

10. **performance_measure** — p. 16 (PDF p. 16) — ✓ verified, 100% word sequence
   > This automation accelerates the submission process while enhancing the accuracy and thoroughness of bids, which is crucial for passing qualification stages.
   Ctrl+F: „enhancing the accuracy and thoroughness of bids, which“
   → Backs the document-accuracy and processing-time elements of the coded performance measure.

11. **ca_measure, quality_notes** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > This scale ranged from 1 (strongly disagree) to 5 (strongly agree), allowing for a nuanced understanding of expert consensus on each topic.
   Ctrl+F: „This scale ranged from 1 (strongly disagree) to“
   → Backs the Likert-based expert rating that underlies the coded ca_measure and the expert-judgment quality note.

12. **ca_measure, quality_notes** — p. 18 (PDF p. 18) — ✓ verified, 100% word sequence
   > Interquartile range (IQR) analysis was also performed to identify the most informative statements.
   Ctrl+F: „was also performed to identify the most informative“
   → Backs the 'Likert+IQR' quantification named in ca_measure and the quantified-consensus quality note.

13. **ca_measure** — p. 13 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 8% word sequence
   > It is noteworthy that Company A exhibits the highest median rating, which reflects a more advanced or successful AI implementation in comparison to its counterparts.
   Ctrl+F: „that Company A exhibits the highest median rating,“
   → Backs the expert-rated per-company comparison (adopters rated above non-adopters) behind the coded CA measure.

14. **effect_direction, conditions, key_finding** — p. 20 (PDF p. 20) — ✓ verified, 100% word sequence
   > it is evident that the successful integration of AI in pharmaceutical TM processes is contingent upon not only technological adoption but also the development of comprehensive governance and ethical frameworks
   Ctrl+F: „integration of AI in pharmaceutical TM processes is“
   → The paper's own 'contingent upon' conclusion — the adjudicated basis for effect_direction = conditional and the governance/ethics condition.

15. **effect_direction, conditions** — p. 20 (PDF p. 20) — ✓ verified, 100% word sequence
   > the study also indicated that the successful implementation of AI is contingent upon several factors, including organizational readiness, senior management involvement, and the alignment of AI initiatives with broader business goals
   Ctrl+F: „implementation of AI is contingent upon several factors,“
   → Backs three coded conditions verbatim: organizational readiness, senior management involvement, alignment with business goals.

16. **conditions** — p. 19 (PDF p. 19) — ✓ verified, 100% word sequence
   > The involvement of senior management from the outset of the AI initiatives was identified as a critical factor in their success
   Ctrl+F: „outset of the AI initiatives was identified as“
   → Backs the coded note that senior management involvement was identified as a critical factor.

*Row check OK: All non-empty columns evidenced; row was adjudicated on all three disputed dimensions (mixed / both / conditional) and the full text supports each. 'Decision quality' in performance_measure appears in the text as 'enhanced decision-making capabilities' (abstract). Quality note is fully source-based (comparative cases + 2-round Delphi with 53 participants, Likert/IQR/Kendall consensus statistics).*

---

## S20 — Pham P. et al. (2024) — Journal of Business Research (AJG 3)

DOI: 10.1016/j.jbusres.2023.114402 · status: final · PDF: `Pham_2024_j-jbusres-2023-114402.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 941 AI hospital-year obs + 941 matched non-AI hospital-year obs (246 matched hospitals), 40 US states, 2000-2020 |
| method | panel econometrics |
| ai_measure | adoption dummy (hospital AI adoption) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | outpatient revenue, inpatient revenue, productivity, occupancy |
| ca_measure | — |
| effect_direction | positive |
| conditions | market share (larger-share hospitals adopt AI and benefit); endogeneity control essential - naive estimates misleading |
| key_finding | Hospitals with larger market share adopt AI and gain in revenue, productivity and occupancy; without endogeneity controls the performance effects are misestimated. |
| *not printed (coding data only)* | |
| theoretical_lens | organizational information processing theory (OIPT) |
| industry | healthcare (hospitals) |
| quality_notes | Matched-sample design with endogeneity controls |
| coding_status | final |

### Evidence

1. **country_region, industry** — p. -4 (PDF p. 1) — ✓ verified, 100% word sequence
   > Determinants and performance outcomes of artificial intelligence adoption: Evidence from U.S. Hospitals
   Ctrl+F: „Determinants and performance outcomes of artificial intelligence adoption:“
   → Title fixes the setting as US hospitals, i.e. USA and healthcare (hospitals).

2. **country_region, sample** — p. 1 (PDF p. 6) — ✓ verified, 100% word sequence
   > These observations include hospitals situated across 40 distinct states; the data covers the time frame spanning from 2000 to 2020.
   Ctrl+F: „observations include hospitals situated across 40 distinct states;“
   → Backs the coded '40 US states, 2000-2020' sample scope.

3. **sample, conditions, key_finding** — p. -4 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using an extensive dataset encompassing 941 AI hospital-year observations and 941 non-AI hospital-year observations, we find that hospitals with a larger market share are great candidates to adopt AI.
   Ctrl+F: „hospital-year observations and 941 non-AI hospital-year observations, we“
   → Abstract states the 941+941 matched hospital-year sample and the market-share condition for who adopts AI.

4. **sample, method** — p. 1 (PDF p. 6) — ⚠ not machine-confirmed on page — open the page, 25% word sequence
   > Our ultimate dataset comprises 1,882 observations, collectively reflecting a span of 941 AI-adopting hospital-years and an equivalent count of 941 non-AI-adopting hospital-years.
   Ctrl+F: „and an equivalent count of 941 non-AI-adopting hospital-years.“
   → States the hospital-year panel structure underlying the coded sample and the panel-econometrics method.

5. **sample, quality_notes** — p. 1 (PDF p. 6) — ✓ verified, 78% word sequence
   > This procedure yields 246 AI hospitals with specific adoption years. We then create a matching sample of 246 hospitals that have not incorporated AI into their operations.
   Ctrl+F: „adoption years. We then create a matching sample“
   → Backs the coded 246 matched hospitals and the quality note 'matched-sample design'.

6. **method** — p. 5 (PDF p. 10) — ⚠ not machine-confirmed on page — open the page, 40% word sequence
   > To further mitigate endogeneity concerns, we employ a differencein-difference test to identify the causality between AI adoption and performance.
   Ctrl+F: „To further mitigate endogeneity concerns, we employ a“
   → OLS, instrumental-variable and difference-in-difference regressions on the hospital-year panel back the panel-econometrics method code.

7. **ai_measure** — p. 1 (PDF p. 6) — ✓ verified, 100% word sequence
   > The AI indicator has the value of 1 if the hospital adopted AI (i.e., AI hospital), and the value of 0 if the hospital did not adopt AI (i.e., non-AI hospital).
   Ctrl+F: „The AI indicator has the value of 1“
   → Defines AI as an adoption dummy, matching the coded ai_measure.

8. **outcome_construct, performance_measure** — p. 1 (PDF p. 6) — ✓ verified, 100% word sequence
   > Following the literature, we use three financial measures and two operational measures to assess hospital performance.
   Ctrl+F: „Following the literature, we use three financial measures“
   → Outcomes are financial/operational hospital performance measures, i.e. performance, not a CA construct.

9. **performance_measure, effect_direction, key_finding** — p. -4 (PDF p. 1) — ✓ verified, 100% word sequence
   > these hospitals can leverage AI technology to enhance various aspects of performance, including total outpatient revenue, total inpatient revenue, productivity, and occupancy
   Ctrl+F: „these hospitals can leverage AI technology to enhance“
   → Abstract names the four coded performance measures and states the positive AI effect on them.

10. **performance_measure, effect_direction** — p. 4 (PDF p. 9) — ✓ verified, 100% word sequence
   > The results show a significantly positive association between AI adoption and all performance measures except ROA.
   Ctrl+F: „association between AI adoption and all performance measures“
   → IV estimates give a clear positive main effect on the four coded measures (ROA null), backing effect_direction positive.

11. **ca_measure, conditions, theoretical_lens** — p. -3 (PDF p. 2) — ✓ verified, 100% word sequence
   > Consistent with the OIPT, we find that hospitals with higher market share have greater incentives to adopt AI to further advance their financial and operational competitiveness.
   Ctrl+F: „share have greater incentives to adopt AI to“
   → OIPT frames the market-share condition; 'competitiveness' appears only as rhetoric here, no CA construct is measured, confirming the empty ca_measure per case law.

12. **conditions, key_finding, quality_notes** — p. -4 (PDF p. 1) — ✓ verified, 76% word sequence
   > Importantly, we demonstrate that controlling for endogeneity is essential in assessing the performance outcomes of AI adoption.
   Ctrl+F: „Importantly, we demonstrate that controlling for endogeneity is“
   → Backs the coded condition 'endogeneity control essential' and the quality note on endogeneity controls.

13. **conditions** — p. 4 (PDF p. 9) — ✓ verified, 100% word sequence
   > The OLS regression results in Panel A show that AI adoption has a positive effect on outpatient revenue, no significant effect on inpatient revenue, return on assets, and occupancy, and a negative effect on productivity.
   Ctrl+F: „The OLS regression results in Panel A show“
   → Naive OLS gives misleading estimates versus the IV results, backing the coded condition 'naive estimates misleading'.

14. **conditions, quality_notes** — p. 4 (PDF p. 9) — ✓ verified, 100% word sequence
   > The results indicate that the decision for AI adoption is endogenous, and that the OLS regression will yield biased results.
   Ctrl+F: „results indicate that the decision for AI adoption“
   → Hausman tests establish endogeneity of AI adoption, backing 'endogeneity control essential' and the quality note.

15. **theoretical_lens** — p. -3 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 29% word sequence
   > Drawing upon the principles of the organizational information processing theory (OIPT), we conjecture that market share and average length of stay could be primary determinants to influence the adoption of AI.
   Ctrl+F: „processing theory (OIPT), we conjecture that market share“
   → Explicitly names OIPT as the guiding theoretical framework.

*Row check OK: All non-empty columns evidenced. Empty ca_measure confirmed: 'competitiveness' occurs only as OIPT framing (p.2), no CA construct is measured. quality_notes is source-based (matched sample p.6, endogeneity essential p.1/9). Coded effect_direction 'positive' rests on the preferred IV and DiD estimates (positive on 4 of 5 measures, ROA null); the paper's own ROA explanation is the nonprofit sample composition (p.13). Verifier flagged two quotes page-unconfirmed (OIPT p.2, 1,882-observations p.6); both manually confirmed present on those PDF pages via pdfplumber - the low scores stem from two-column line interleaving.*

---

## S21 — Sullivan Y. et al. (2024) — Journal of Business Research (AJG 3)

DOI: 10.1016/j.jbusres.2024.114500 · status: final · PDF: `Sullivan_2024_j-jbusres-2024-114500.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Europe (France 68.2%, UK 31.8%) |
| sample | two-wave survey, 107 executives completing both waves (of 225 wave-1; 47.5% effective RR), panel-recruited IT+business executives, France + UK |
| method | survey-SEM |
| ai_measure | survey constructs (AI-enabled automation, AI-enabled analytics, AI-enabled relational capabilities) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm performance + process innovation + product innovation (survey scales) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | ARMC full mediator (no direct AI->performance paths modeled); environmental hostility (negative moderator on automation->ARMC -0.23*; relational path turns n.s.); environmental dynamism moderates; only 10/18 conditional indirect effects significant |
| key_finding | AI capabilities pay off through the firm's adaptive response to market changes; environmental hostility/dynamism condition how much each AI capability contributes. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities / organizational agility |
| industry | cross-industry |
| quality_notes | Two-wave design (stronger than cross-section); perceptual measures; effect highly environment-selective |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, sample** — PDF p. 8, 4.3. Sample characteristics — ✓ verified, 100% word sequence
   > Data were collected from firms in France (68.2 %) and the U.K. (31.8 %).
   Ctrl+F: „in France (68.2 %) and the U.K. (31.8“
   → States the sample's actual countries.
   **⚠ TENSION:** Coded country_region is 'USA' and sample says '107 US executives', but the paper's data come from firms in France (68.2%) and the UK (31.8%) via a European panel; only the first author's affiliation is US (Baylor). Coded value contradicts the full text.

2. **country_region, industry** — PDF p. 13, 6.3. Limitations and future research directions — ✓ verified, 100% word sequence
   > Lastly, our data were collected from firms located in France and the U.K., and our sample includes a broad spectrum of industry groups.
   Ctrl+F: „and our sample includes a broad spectrum of“
   → Authors' own statement backs the cross-industry coding and reiterates France/UK data collection (see tension on country_region).

3. **sample, method** — PDF p. 7, 4. Research methodology — ✓ verified, 100% word sequence
   > This study uses a two-stage survey to collect data from IT executives and business decision-makers
   Ctrl+F: „This study uses a two-stage survey to collect“
   → Confirms two-wave survey design and the IT+business executive respondent base.

4. **sample** — PDF p. 8, 4.2. Survey development and administration — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > Of 225 respondents who completed the first survey, a total of 107 respondents completed the second survey for an effective response rate of 47.5 percent.
   Ctrl+F: „225 respondents who completed the first survey, a“
   → Confirms the coded n = 107 of 225 wave-1 respondents and the 47.5% effective response rate.

5. **sample** — PDF p. 8, 4.2. Survey development and administration — ✓ verified, 69% word sequence
   > The samples for both countries were drawn from the panel members of the market research firm. We utilized the prescreening filters provided by this company to select appropriate respondents, such as IT or business executives.
   Ctrl+F: „The samples for both countries were drawn from“
   → Confirms panel-recruited IT/business executives as coded in sample.

6. **method** — PDF p. 8, 5.1. Measurement validation — ✓ verified, 100% word sequence
   > We used Partial Least Squares (PLS) in the package WarpPLS 7.0 (Kock, 2022) to perform the data analysis.
   Ctrl+F: „We used Partial Least Squares (PLS) in the“
   → Confirms PLS structural equation modeling, i.e. the coded survey-SEM method.

7. **method, quality_notes** — PDF p. 13, 6.3. Limitations and future research directions — ✓ verified, 100% word sequence
   > Fourth, although we conducted a two-stage survey to address the threats of common method bias, we still used the same respondent for both our independent and dependent variables.
   Ctrl+F: „Fourth, although we conducted a two-stage survey to“
   → Authors' own admission backs the quality note: two-wave design as a strength, but perceptual same-respondent measures remain a limitation.

8. **ai_measure** — PDF p. 7, 4.1. Measures — ⚠ not machine-confirmed on page — open the page, 38% word sequence
   > We measured three AI capabilities: AI-enabled automation, AI-enabled analytics, and AI-enabled relational capabilities.
   Ctrl+F: „automation, AI-enabled analytics, and AI-enabled relational“
   → Confirms the three coded AI survey constructs.

9. **outcome_construct, performance_measure, ca_measure** — PDF p. 7, 4.1. Measures — ✓ verified, 100% word sequence
   > We adapted five items from Queiroz et al. (2018) to measure market share, revenues, sales growth, and profitability relative to competitors.
   Ctrl+F: „items from Queiroz et al. (2018) to measure“
   → Confirms the perceptual firm-performance survey scale; the scale is relative-to-competitors but no distinct CA construct or CA hypothesis is measured, so ca_measure empty and outcome_construct=performance are consistent with case law.

10. **outcome_construct, performance_measure** — PDF p. 1, Abstract — ⚠ not machine-confirmed on page — open the page, 56% word sequence
   > Additionally, we propose positive associations between ARMC and three organizational outcomes: firm performance, process innovation, and product innovation.
   Ctrl+F: „Additionally, we propose positive associations between ARMC and“
   → Confirms the coded outcome set: firm performance plus process and product innovation.

11. **effect_direction** — PDF p. 9, 5.3. Structural model — ✓ verified, 100% word sequence
   > However, adding the interaction terms to the model significantly altered the direct effects of AI-powered capabilities.
   Ctrl+F: „However, adding the interaction terms to the model“
   → Backs the coded 'conditional' direction: AI effects change once environmental moderators enter the model.

12. **effect_direction** — PDF p. 9, 5.3. Structural model (footnote 3) — ⚠ not machine-confirmed on page — open the page, 15% word sequence
   > the relationships should be interpreted as 'conditional' effects at the different values of the included moderator in the model, and the main effects become less relevant
   Ctrl+F: „at the different values of the included moderator“
   → Authors themselves label the AI-ARMC relationships 'conditional', directly matching the coded effect_direction.

13. **effect_direction, conditions** — PDF p. 9, 5.3. Structural model — ✓ verified, 100% word sequence
   > However, the effect of AI-enabled relational capability became insignificant, failing to support H6.
   Ctrl+F: „However, the effect of AI-enabled relational capability became“
   → Confirms the coded condition that the relational path turns non-significant in the interaction model.

14. **effect_direction, conditions** — PDF p. 9, 5.3. Structural model — ✓ verified, 100% word sequence
   > As shown in Table 7, 10 out of 18 conditional indirect effects of AI-powered capabilities on organizational outcomes were significant, suggesting meaningful moderating roles of environmental conditions.
   Ctrl+F: „As shown in Table 7, 10 out of“
   → Confirms the coded '10/18 conditional indirect effects significant' and the environment-selective, conditional nature of the AI-outcome link.

15. **conditions** — PDF p. 6, 3.2.7. ARMC, process Innovation, and product innovation — ✓ verified, 100% word sequence
   > Thus, we argue that AI indirectly influences firms' innovation through ARMC.
   Ctrl+F: „argue that AI indirectly influences firms’ innovation through“
   → Confirms ARMC's coded role as the mediating mechanism; no direct AI-to-outcome paths are part of the hypothesized model.

16. **conditions** — PDF p. 9, 5.3. Structural model — ✓ verified, 100% word sequence
   > As expected, environmental hostility negatively moderated the relationship between AI-enabled automation and ARMC, supporting H7a.
   Ctrl+F: „As expected, environmental hostility negatively moderated the“
   → Confirms environmental hostility as a coded negative moderator on the automation path (Table 6 reports the interaction as -0.23**).

17. **conditions** — PDF p. 9, 5.3. Structural model — ⚠ not machine-confirmed on page — open the page, 25% word sequence
   > The interaction between AIenabled relational and environmental dynamism was significant, supporting H8c.
   Ctrl+F: „relational and environmental dynamism was“
   → Confirms environmental dynamism as a coded moderator.

18. **key_finding** — PDF p. 10, 6. Discussion — ✓ verified, 75% word sequence
   > Our findings reveal that the relationships between AI-powered capabilities and ARMC depend on environmental conditions.
   Ctrl+F: „the relationships between AI-powered capabilities and ARMC.“
   → Paper's own summary of its central result: AI pays off contingent on environmental hostility/dynamism, as coded.

19. **key_finding** — PDF p. 11, 6. Discussion — ⚠ not machine-confirmed on page — open the page, 27% word sequence
   > Finally, our study establishes significant positive relationships between ARMC and both firm performance and innovation.
   Ctrl+F: „positive relationships between ARMC and both firm performance“
   → Paper's own statement of the second half of the coded key finding: AI capabilities pay off through ARMC into performance and innovation.

20. **theoretical_lens** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > Utilizing insights from organizational agility and the dynamic capability framework, we define ARMC as an organization's ability to promptly identify and adjust to market changes
   Ctrl+F: „Utilizing insights from organizational agility and the dynamic“
   → Names organizational agility and the dynamic capability framework as the study's theoretical basis.

**⚠ ROW CHECK:** country_region ('USA') and the 'US executives' phrase in sample contradict the paper: data were collected from firms in France (68.2%) and the UK (31.8%) via a European market-research panel (population: AI-adopting firms in Europe); possibly confused with the authors' US affiliation or with S29. Everything else checks out. Minor: coded conditions report the automation x hostility interaction as -0.23*, Table 6 shows -0.23**. Note: footnote 5 reports supplementary direct AI->outcome effects (analytics 0.44*** on performance) outside the main model; the adjudicated 'no direct AI->performance paths modeled' refers to the hypothesized structural model and stands. Quality-note element 'effect highly environment-selective' is coder commentary summarizing the 10/18 result (quoted).

---

## S22 — Sun Z. et al. (2024) — Technology in Society (AJG 2)

DOI: 10.1016/j.techsoc.2024.102752 · status: final · PDF: `Sun_2024_j-techsoc-2024-102752.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 3,235 Chinese listed firms, 2007-2021; fixed effects + system GMM + mediation models |
| method | panel econometrics |
| ai_measure | annual-report text (frequency of AI-related terms); controls from CSMAR/RESSET |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm total factor productivity |
| ca_measure | — |
| effect_direction | positive |
| conditions | stronger in state-controlled, internationally oriented, innovative firms; mechanism: reduced information asymmetry (key channel), specialized division of labor, green innovation; supply-chain digitalization policy amplifies; effect SLOWS over the long run |
| key_finding | AI raises firm productivity in China - most for state-controlled, international and innovative firms - but the productivity boost decays over time. |
| *not printed (coding data only)* | |
| theoretical_lens | Solow paradox / production economics (no mgmt lens) |
| industry | cross-industry (listed firms) |
| quality_notes | Large panel, GMM; dynamic decomposition of the effect |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Based on panel data of 3235 listed companies in China from 2007 to 2021, we comprehensively discuss the impact and mechanism of AI on firm productivity using fixed-effects model, systematic GMM model, and mediated-effects model
   Ctrl+F: „Based on panel data of 3235 listed companies“
   → Confirms the coded sample (3,235 Chinese listed firms 2007-2021) and the panel-econometrics toolkit (FE, system GMM, mediation models).

2. **country_region, sample, industry** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > this study compiles and obtains the panel data of China's Shanghai and Shenzhen A-share listed companies from 2007 to 2021 for empirical analysis
   Ctrl+F: „this study compiles and obtains the panel data“
   → The A-share listed universe (Shanghai + Shenzhen) backs China and the cross-industry (listed firms) coding.

3. **sample, ai_measure** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > The data for control variables are obtained from CSMAR database and RESSET financial database.
   Ctrl+F: „The data for control variables are obtained from“
   → Confirms the coded note that controls come from CSMAR/RESSET.

4. **sample** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > According to the above processing, we obtained unbalanced panel data from 3235 companies in China.
   Ctrl+F: „the above processing, we obtained unbalanced panel data“
   → Confirms the exact n = 3,235 after screening.

5. **method, quality_notes** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > Column (3) reports the estimation results for SYS-GMM, and our findings still hold after overcoming the endogeneity problem.
   Ctrl+F: „Column (3) reports the estimation results for SYS-GMM,“
   → Backs the coded method detail (system GMM) and the quality note on GMM robustness.

6. **ai_measure** — p. 5 (PDF p. 5) — ✓ verified, 65% word sequence
   > we build a thesaurus based on crawler technology by crawling the words related to "artificial intelligence" in the annual reports of listed companies
   Ctrl+F: „on crawler technology by crawling the words related“
   → Confirms the coded AI measure: frequency of AI-related terms in annual-report text.

7. **ai_measure, quality_notes** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > In the study, AI is mainly measured by the frequency of relevant terms in annual reports, which may not be able to accurately reflect the development level of enterprise AI.
   Ctrl+F: „In the study, AI is mainly measured by“
   → Authors' own limitation statement on the annual-report term-frequency AI proxy.

8. **outcome_construct, performance_measure** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > Total Factor Productivity (TFP) is an important indicator of the overall productivity of a firm, and there are various methods for calculating TFP
   Ctrl+F: „Total Factor Productivity (TFP) is an important indicator“
   → Confirms firm TFP as the dependent variable, i.e. a pure performance outcome with no CA construct.

9. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Key findings include: AI significantly improves firm productivity, especially in state-controlled, internationally minded, and innovative firms.
   Ctrl+F: „productivity, especially in state-controlled, internationally minded, and innovative“
   → Paper's own summary backs the positive direction, the coded key finding, and the three heterogeneity conditions.

10. **effect_direction** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > As expected from Hypothesis 1, the coefficients of AI in the results all passed the significance level test and showed a positive impact.
   Ctrl+F: „level test and showed a positive impact.“
   → Baseline regressions show a clear positive average main effect, backing effect_direction = positive.

11. **effect_direction, conditions, quality_notes** — p. 11 (PDF p. 11) — ⚠ not machine-confirmed on page — open the page, 43% word sequence
   > The impulse response results show that the instantaneous shock of AI positively affects TFP and reaches its maximum in period 2, then gradually falls back by period 10.
   Ctrl+F: „response results show that the instantaneous shock of“
   → PVAR dynamic decomposition backs the coded long-run slowdown condition and the quality note on dynamic decomposition; average effect remains positive.

12. **conditions, key_finding** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 42% word sequence
   > Additionally, the dynamic decomposition effect shows that the productivityenhancing effect of AI is slowing down in the long run.
   Ctrl+F: „of AI is slowing down in the long“
   → Backs the coded condition that the effect slows over the long run and the decay clause of the key finding.

13. **conditions** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > The productivity-enhancing effect of AI is greater in SOEs compared to non-SOEs and Sino-foreign joint ventures.
   Ctrl+F: „in SOEs compared to non-SOEs and Sino-foreign joint“
   → Confirms the coded condition: stronger effect in state-controlled firms.

14. **conditions** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > As expected, firms with leaders with a strong international perspective show a stronger productivity dividend from AI.
   Ctrl+F: „with leaders with a strong international perspective show“
   → Confirms the coded condition: stronger in internationally oriented firms.

15. **conditions** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > AI can be more effective in enhancing firm productivity in innovation-minded firms
   Ctrl+F: „AI can be more“
   → Confirms the coded condition: stronger in innovative firms.

16. **conditions** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > firms affected by supply chain innovation policies have a more significant effect of AI on their productivity
   Ctrl+F: „by supply chain innovation policies have a more“
   → Confirms the coded condition that the supply-chain digitalization policy amplifies the AI effect.

17. **conditions** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > Again, this study finds that information asymmetry is the main mechanism by which AI enhances firm productivity, and that specialization and green innovation also show potential channel effects
   Ctrl+F: „specialization and green innovation also show potential channel“
   → Confirms the coded mechanisms: information asymmetry as key channel, specialized division of labor and green innovation as potential channels.

18. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Therefore, revealing the impact of AI on firm productivity is an important topic to analyze whether Solow's paradox can be valid in the digital age.
   Ctrl+F: „productivity is an important topic to analyze whether“
   → Frames the study in the Solow productivity-paradox / production-economics tradition, matching the coded lens (no management theory used).

*Row check OK: All non-empty columns evidenced; ca_measure emptiness correct (competitiveness appears only as rhetoric, no CA construct measured). Coded conditions are selective: the paper additionally reports a dampening low-carbon pilot policy moderator, a Ming-Dynasty stagecoach-region moderator, and stronger effects above the 75th productivity percentile - extra moderators not coded, no contradiction. 'Large panel' in quality_notes is coder commentary on the quoted n=3,235/15,213-obs panel.*

---

## S23 — Zebec A. et al. (2024) — Business Process Management Journal (AJG 2)

DOI: 10.1108/BPMJ-07-2023-0566 · status: final · PDF: `Zebec_2024_BPMJ-07-2023-0566.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | EU |
| sample | 448 organisations, EU, serial multiple mediation SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | organizational performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | serial mediation: decision-making quality and business-process performance carry the effect; process automation, organizational learning, process innovation as complementary partial mediators |
| key_finding | AI creates business value indirectly: through better decisions and business-process performance, complemented by automation, learning and process innovation. |
| *not printed (coding data only)* | |
| theoretical_lens | IT business value model |
| industry | cross-industry |
| quality_notes | Perceptual, cross-section; mediation-heavy design |
| coding_status | final |

### Evidence

1. **country_region, sample, method, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The integrative model of IT Business Value was contextualised, and structural equation modelling was applied to validate the proposed serial multiple mediation model using a sample of 448 organisations based in the EU.
   Ctrl+F: „The integrative model of IT Business Value was“
   → One sentence backs the coded lens (IT business value model), method (SEM), sample (448 organisations) and region (EU).

2. **country_region, sample, industry** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > The collected and processed sample included 448 EU organisations. Sample representativeness was ensured in terms of firm size, industry sector, years in business (age) and country.
   Ctrl+F: „The collected and processed sample included 448 EU“
   → Confirms n = 448 EU organisations and the cross-industry composition (representativeness across industry sectors).

3. **country_region** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > with almost half from Germany (21.43%), Italy (10.94%), the Netherlands (10.49%) and France (6.92%)
   Ctrl+F: „(21.43%), Italy (10.94%), the Netherlands (10.49%) and France“
   → Country breakdown confirms a multi-country EU sample, matching country_region = EU.

4. **method, quality_notes** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > In order to empirically examine the research problem, a survey design was employed. A single primary data source, self-report, and cross-sectional design were used.
   Ctrl+F: „In order to empirically examine the research problem,“
   → Confirms survey method and the quality note (perceptual self-report, cross-section).

5. **method** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > AMOS version 28 with the Maximum Likelihood Method was used for performing the CFA and Path Analysis (i.e. to test the hypotheses in the conceptual model).
   Ctrl+F: „AMOS version 28 with the Maximum Likelihood Method“
   → Covariance-based SEM in AMOS confirms the coded survey-SEM method.

6. **ai_measure** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > The operationalisation of AI adoption comprised five underlying sub-constructs: DACQ, CI, CE, CDA and CT.
   Ctrl+F: „The operationalisation of AI adoption comprised five underlying“
   → Confirms AI adoption as a multidimensional survey construct, as coded in ai_measure.

7. **outcome_construct, performance_measure, ca_measure** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > A measurement scale developed by Wang et al. (2012) was used to measure the OP construct. As a second-order construct, it consists of two first-order reflective constructs: Operational Performance and Market Performance.
   Ctrl+F: „A measurement scale developed by Wang et al.“
   → Confirms organizational performance as the survey-scale outcome; no distinct competitive-advantage construct is measured, so ca_measure empty and outcome_construct = performance are right.

8. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results validate the proposed serial multiple mediation model according to which AI adoption increases organisational performance through decision-making and business process performance. Process automation, organisational learning and process innovation are significant complementary partial mediators
   Ctrl+F: „The results validate the proposed serial multiple mediation“
   → Paper's own findings statement matches the coded key finding and the coded conditions (serial mediation via DMP and BPP, three complementary mediators); 'increases' backs the positive direction.

9. **effect_direction** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > Without the mediators, the total effect of AI on OP was tested. The relationship is significant, and the standardised total effect is 0.418
   Ctrl+F: „Without the mediators, the total effect of AI“
   → Significant positive total effect (0.418, p < 0.001) grounds effect_direction = positive under the case-law rule (mediated-positive with significant total effect).

10. **effect_direction, key_finding** — p. 16 (PDF p. 16) — ✓ verified, 100% word sequence
   > Finally, the positive impact of AI adoption on performance was empirically demonstrated with a large-scale EU study.
   Ctrl+F: „AI adoption on performance was empirically demonstrated with“
   → Authors' own summary states a positive AI-performance impact, backing the coded direction.

11. **conditions** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > According to the results shown in Table 3, BPA mediates the positive impact of AI adoption on DMP (support for H4a) but not on BPP (no support for H4b).
   Ctrl+F: „shown in Table 3, BPA mediates the positive“
   → Detail of the coded complementary mediators: process automation carries the effect via decision-making performance.

12. **conditions** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > The results in Table 3 reveal OL mediates the positive impact of AI adoption on DMP and BPP (support for H5a and H5b).
   Ctrl+F: „mediates the positive impact of AI adoption on“
   → Confirms organizational learning as a coded mediator.

13. **conditions** — p. 15 (PDF p. 15) — ✓ verified, 100% word sequence
   > The non-significant direct relationship defined by H1 indicates that the relationship between AI and OP is fully mediated.
   Ctrl+F: „defined by H1 indicates that the relationship between“
   → Backs the coded condition that decision-making and process performance carry the effect (full mediation of the AI-OP link).

14. **theoretical_lens** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > For this purpose, the integrative IT business value model (Melville et al., 2004) was adopted to study AI adoption in the BPM setting.
   Ctrl+F: „For this purpose, the integrative IT business value“
   → Names Melville's IT business value model as the adopted framework, matching the coded lens.

15. **quality_notes** — p. 18 (PDF p. 18) — ✓ verified, 100% word sequence
   > A cross-sectional survey was used to validate the proposed research model. Self-report bias and endogeneity issues are typical limitations of such a research design
   Ctrl+F: „A cross-sectional survey was used to validate the“
   → Authors' own limitation statement backs the quality note (perceptual, cross-section).

*Row check OK: All non-empty columns evidenced. ca_measure emptiness correct: competitive advantage appears only as framing (intro/conclusion rhetoric), no CA construct measured. For the author's awareness: the direct AI->OP path in the full model is non-significant (full mediation, quoted), while the total effect without mediators is significant (0.418***) - the final coding positive follows the case-law rule that a significant total effect takes its sign, with the mediation chain recorded in conditions. 'Mediation-heavy design' in quality_notes is coder commentary on the quoted serial-mediation setup.*

---

## S24 — Alam S.S. et al. (2025) — International Journal of Hospitality Management (AJG 3)

DOI: 10.1016/j.ijhm.2025.104133 · status: final · PDF: `Alam_2025_j-ijhm-2025-104133.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Malaysia |
| sample | 336 respondents, stratified purposive sampling, hospitality industry |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption + technology readiness) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | value creation (survey scale) |
| ca_measure | sustainable competitive advantage (survey scale, modeled as mediator) |
| effect_direction | positive |
| conditions | SCA mediates AI adoption -> value creation; dynamic capabilities initially impede value creation (transition costs), later crucial under turbulence; technological turbulence moderates only the DC -> value creation path |
| key_finding | AI adoption creates value in hospitality mainly through sustainable competitive advantage as transmission channel; dynamic capabilities help only once transition costs are absorbed. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + dynamic capabilities + contingency theory |
| industry | hospitality |
| quality_notes | Perceptual, cross-section; models CA explicitly (as mediator) |
| coding_status | final |

### Evidence

1. **country_region, industry** — p. 1–2 (PDF p. 1) — ✓ verified, 60% word sequence
   > This study explores the relationship between technology readiness, AI adoption, dynamic capabilities, sustainable competitive advantage, and technological turbulence, assessing their collective impact on value creation within the Malaysian hospitality industry.
   Ctrl+F: „This study explores the relationship between technology readiness,“
   → Names Malaysia and the hospitality industry as setting, plus all coded constructs.

2. **sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using stratified purposive sampling, data was collected from 336 respondence. Structural equation modeling was utilized to analyze the relationships among the constructs.
   Ctrl+F: „Using stratified purposive sampling, data was collected from“
   → Confirms stratified purposive sampling, n = 336, and SEM as coded ('respondence' is the paper's own typo).

3. **sample, industry** — p. 7 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 13% word sequence
   > Ultimately, 84 organizations, encompassing both startups and established entities, participated and returned completed questionnaires from four designated respondents each, totalling 336 individual responses.
   Ctrl+F: „both startups and established entities, participated and returned“
   → Confirms the coded n = 336 (84 hospitality organizations x 4 respondents).

4. **method** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > SmartPLS v 4.0.8.1 software for structural equation modeling (SEM), aligning with Hair et al. (2022) recommendations
   Ctrl+F: „modeling (SEM), aligning with Hair et al. (2022)“
   → Confirms PLS-SEM as the analysis method (survey-SEM coding).

5. **ai_measure** — p. 7 (PDF p. 7) — ✓ verified, 82% word sequence
   > Artificial Intelligence Adoption, guided by Chatterjee et al. (2023), probes into the extent and efficacy of AI technology utilization within hospitality operations
   Ctrl+F: „Chatterjee et al. (2023), probes into the extent“
   → Confirms AI adoption as a survey construct, part of the coded ai_measure.

6. **ai_measure** — p. 7 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 45% word sequence
   > Technology Readiness, as outlined by Shehadeh et al. (2022), evaluates an organization's infrastructure, cultural orientation, and strategic inclination towards embracing emerging technologies like AI, analytics, and cloud computing
   Ctrl+F: „outlined by Shehadeh et al. (2022), evaluates an“
   → Confirms technology readiness as the second survey construct in the coded ai_measure.

7. **outcome_construct, ca_measure, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Sustainable competitive advantage emerged as a significant mediator, translating AI adoption and dynamic capabilities into enhanced value creation.
   Ctrl+F: „Sustainable competitive advantage emerged as a significant mediator,“
   → Backs the coded key finding and conditions (SCA as transmission channel) and the ca_measure note that SCA is modeled as mediator.

8. **outcome_construct, performance_measure** — p. 7 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 22% word sequence
   > Value creation is framed within the bifurcates into Enterprise Value (organizational benefits from collaborative endeavors) and User Value (the personalized satisfaction and value derived by the users)
   Ctrl+F: „endeavors) and User Value (the personalized satisfaction and“
   → Confirms value creation as the survey-scale performance outcome (enterprise + user value); wording quirk is the paper's own.

9. **outcome_construct, ca_measure** — p. 7 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 15% word sequence
   > Sustainable Competitive Advantage, drawing from Kim et al. (2011), investigates the long-term strategic assets that facilitate superior organizational performance.
   Ctrl+F: „from Kim et al. (2011), investigates the long-term“
   → Confirms a distinct, own SCA survey scale (SCA1-3, hypotheses H5-H8), grounding outcome_construct = both under the case-law rule.

10. **ca_measure, conditions** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > The mediation effect is significant for both AI adoption ( β = 0.063, p = 0.002) and dynamic capability ( β = 0.131, p = 0.001), underscoring SCA's importance in translating these factors into tangible value.
   Ctrl+F: „AI adoption (β = 0.063, p = 0.002) and dynamic capability“
   → Confirms the coded condition that SCA mediates AI adoption -> value creation, with exact coefficients.

11. **effect_direction, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results reveal that technology readiness and AI adoption positively influence value creation, with AI adoption playing a direct role in enhancing organizational capabilities and efficiencies.
   Ctrl+F: „readiness and AI adoption positively influence value creation,“
   → Abstract states the positive AI-adoption effect on value creation, backing effect_direction = positive.

12. **effect_direction** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > AI adoption itself positively influences value creation ( β = 0.110, p = 0.034), though the effect size is modest
   Ctrl+F: „AI adoption itself positively influences value creation (β = 0.110,“
   → Significant positive direct AI -> value creation path grounds the positive direction.

13. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Interestingly, dynamic capabilities exhibited a complex impact, initially impeding value creation due to transitional challenges, but ultimately proving crucial in navigating technological turbulence.
   Ctrl+F: „initially impeding value creation due to transitional challenges,“
   → Backs the coded condition that dynamic capabilities initially impede value creation (transition costs) but matter under turbulence.

14. **conditions** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 30% word sequence
   > However, the moderating effects of technological turbulence were selective, significantly influencing only the relationship between dynamic capabilities and value creation.
   Ctrl+F: „turbulence were selective, significantly influencing only the relationship“
   → Confirms the coded condition that technological turbulence moderates only the DC -> value creation path.

15. **conditions** — p. 10 (PDF p. 10) — ⚠ not machine-confirmed on page — open the page, 29% word sequence
   > This suggests that while dynamic capabilities are theoretically beneficial, their implementation might initially be associated with disruptions or inefficiencies that can reduce perceived value.
   Ctrl+F: „beneficial, their implementation might initially be associated with“
   → Authors' interpretation of the negative DC -> value creation path backs the coded 'transition costs' condition.

16. **theoretical_lens** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 32% word sequence
   > Employing the Resource-Based View, Dynamic Capabilities Framework, and Contingency Theory, the research analyzes these strategic elements' roles in enhancing organizational performance.
   Ctrl+F: „and Contingency Theory, the research analyzes these strategic“
   → Confirms the coded triple lens: RBV + dynamic capabilities + contingency theory.

17. **quality_notes** — p. 12 (PDF p. 12) — ⚠ not machine-confirmed on page — open the page, 20% word sequence
   > subsequent studies might explore the longitudinal impacts of AI adoption and technology readiness on value creation, particularly examining how these effects evolve as organizations mature
   Ctrl+F: „impacts of AI adoption and technology readiness on“
   → Authors' call for longitudinal follow-up confirms the cross-sectional design noted in quality_notes; perceptual measures follow from the survey scales quoted above.

*Row check OK: All non-empty columns evidenced. outcome_construct 'both' is sound: SCA is measured with its own validated scale (SCA1-3, AVE 0.878) and dedicated hypotheses, per case law. Two caveats for the author: (1) the text extraction drops minus signs in Table 6 - the TR->VC and DC->VC paths are negative per the discussion text ('negatively impacts', 'negative relationship') though the table shows bare 0.275/0.385; (2) the abstract claims technology readiness 'positively influence[s] value creation' while the paper's own H2 result is negative - an internal inconsistency of the paper, not of the coding, since effect_direction is coded on the AI-adoption path (positive, quoted).*

---

## S25 — Alwakid W.N. et al. (2025) — Technology in Society (AJG 2)

DOI: 10.1016/j.techsoc.2025.103007 · status: final · PDF: `Alwakid_2025_j-techsoc-2025-103007.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Saudi Arabia |
| sample | 250 SMEs (managers/owners), manufacturing + services |
| method | survey-SEM |
| ai_measure | survey construct (AI capabilities: infrastructure, business integration, proactive stance) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | sustainable SME performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | SME creativity and green innovations (mediators); green entrepreneurial orientation as parallel driver (risk-taking, innovativeness, proactiveness) |
| key_finding | AI capabilities raise sustainable SME performance through creativity and green innovation - AI infrastructure plus proactive strategy is the entry condition. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV |
| industry | SMEs (manufacturing + service) |
| quality_notes | Perceptual, cross-section |
| coding_status | final |

### Evidence

1. **country_region, sample, method, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > A quantitative research design was applied, utilizing survey data gathered from SME managers and business owners functioning in the manufacturing and service sectors in Saudi Arabia.
   Ctrl+F: „A quantitative research design was applied, utilizing survey“
   → Backs the coded sample (SME managers/owners), Saudi Arabia, manufacturing + service SMEs, and the survey method.

2. **sample** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > Following data cleaning, screening for missing values, and checking for inconsistencies, 250 valid responses were retained for final analysis.
   Ctrl+F: „screening for missing values, and checking for inconsistencies,“
   → Backs the coded n = 250 SMEs.

3. **method, quality_notes** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The research design was structured around a cross-sectional survey, utilizing a structured questionnaire to gather primary data
   Ctrl+F: „a cross-sectional survey, utilizing a structured questionnaire to“
   → States the cross-sectional survey design, backing survey-SEM and the 'cross-section' quality note.

4. **method** — p. 9 (PDF p. 9) — ✓ verified, 90% word sequence
   > The study employed Partial Least Squares Structural Equation Modeling (PLS-SEM) using SmartPLS 4.0 to analyze the proposed conceptual model.
   Ctrl+F: „The study employed Partial Least Squares Structural Equation“
   → Backs the survey-SEM method code (PLS-SEM in SmartPLS).

5. **ai_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > AI Capabilities were measured using dimensions such as infrastructure, business spanning, and proactive stance
   Ctrl+F: „such as infrastructure, business spanning, and proactive stance,“
   → AI is a survey construct with the three coded dimensions; the paper's term for 'business integration' is 'business spanning' (AI integration across functions).

6. **outcome_construct, performance_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > Sustainable Performance (dependent variable) was evaluated using multidimensional economic, social, and environmental measures adapted from sustainable enterprise performance models
   Ctrl+F: „Sustainable Performance (dependent variable) was evaluated using“
   → The dependent variable is a sustainable-performance survey scale, i.e. performance, not a CA construct.

7. **ca_measure** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 28% word sequence
   > By integrating AI capabilities and green entrepreneurship, SMEs can achieve a competitive advantage while achieving world sustainability goals.
   Ctrl+F: „and green entrepreneurship, SMEs can achieve a competitive“
   → Competitive advantage appears only as framing rhetoric; no CA construct is among the eleven measured constructs (Tables 2-3), confirming the empty ca_measure per case law.

8. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results indicate that AI capabilities significantly impact SME creativity and green innovations. Moreover, green entrepreneurial orientation positively influences SME creativity and green innovations, which in turn facilitate sustainable performance.
   Ctrl+F: „The results indicate that AI capabilities significantly impact“
   → Abstract states the positive AI effect running through creativity and green innovation to sustainable performance, with GEO as parallel driver.

9. **effect_direction** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > | Capabilities (AIC) have significant effects on both Green Innovations (GRI) ( β = 0.250, t = 4.280, p < 0.001) and Green SMEs Creativity (GSC) ( β = 0.270, t = 3.980, p <
   Ctrl+F: „Capabilities (AIC) have significant effects on both Green“
   → Significant positive AI paths into both mediating outcomes.

10. **effect_direction, conditions** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > The findings indicate that AI Capabilities (AIC) have indirectly impacted Green SMEs' Sustainable Performance (GSP) (β = 0.220, t = 4.750, p < 0.001)
   Ctrl+F: „(AIC) have indirectly impacted Green SMEs’ Sustainable Performance“
   → The total indirect AI effect on sustainable performance is significantly positive, carried by the coded mediators creativity and green innovation.

11. **effect_direction, conditions, key_finding** — p. 15 (PDF p. 15) — ✓ verified, 100% word sequence
   > SME creativity (p = 0.000) and green innovations (p = 0.000) were confirmed as key drivers of sustainable performance, justifying their mediating role
   Ctrl+F: „creativity (p = 0.000) and green innovations (p = 0.000)“
   → Conclusion confirms creativity and green innovation as the mediators through which AI raises sustainable performance.

12. **conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Moreover, green risk-taking, innovativeness, and proactiveness significantly contribute to green entrepreneurial orientation, affecting SME creativity and green innovations, ultimately resulting in sustainable performance.
   Ctrl+F: „Moreover, green risk-taking, innovativeness, and proactiveness significantly contribute“
   → Backs the coded GEO parallel driver with its three dimensions (risk-taking, innovativeness, proactiveness).

13. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This research identifies the importance of SMEs allocating resources to AI infrastructure, proactive business strategies, and entrepreneurial risk-taking to foster green innovation and sustainability.
   Ctrl+F: „allocating resources to AI infrastructure, proactive business strategies,“
   → Backs the key_finding clause that AI infrastructure plus proactive strategy is the entry condition.

14. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study is based on the Resource-Based View (RBV) theory, which offers a theoretical framework for investigating how AI-based competencies and green entrepreneurial strategies can promote SME performance.
   Ctrl+F: „on the Resource-Based View (RBV) theory, which offers“
   → Abstract names RBV as the study's theoretical basis.

15. **quality_notes** — p. 15 (PDF p. 15) — ⚠ not machine-confirmed on page — open the page, 27% word sequence
   > While surveys effectively capture managerial perceptions and strategic orientations, they are subject to potential biases such as social desirability bias, recall bias, and standard method variance.
   Ctrl+F: „and strategic orientations, they are subject to potential“
   → Authors admit the perceptual self-report nature, backing the 'perceptual' quality note.

16. **quality_notes** — p. 15 (PDF p. 15) — ✓ verified, 100% word sequence
   > Methodologically, the study's use of a cross-sectional approach restricts its ability to identify causality.
   Ctrl+F: „Methodologically, the study’s use of a cross-sectional approach“
   → Authors admit the cross-sectional limitation, backing the 'cross-section' quality note.

*Row check OK: All non-empty columns evidenced; empty ca_measure confirmed (CA is abstract rhetoric only, no measured CA construct). Structural note for the author: no direct AIC->GSP path is modeled - AI reaches sustainable performance entirely via the two mediators; 'positive' stands because the total indirect effect is significant (0.220, p<0.001) and every channel is significant (unlike S28, where a null channel plus no direct path gave 'conditional'). Coded ai_measure wording 'business integration' corresponds to the paper's 'business spanning' dimension.*

---

## S26 — Banna H. et al. (2025) — International Journal of Entrepreneurial Behaviour and Research (AJG 3)

DOI: 10.1108/IJEBR-12-2024-1489 · status: final · PDF: `Banna_2025_IJEBR-12-2024-1489.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | EU (26 countries) |
| sample | unbalanced panel of 1,479 firms (~12,900 obs), 26 EU countries, 2012-2023; CGM multi-way clustering + 2SLS-IV |
| method | panel econometrics |
| ai_measure | country-level AI venture-capital investment (OECD AI Policy Observatory), matched to firms by country of incorporation (log; turning point USD 11.3M); robustness: AI investment count/intensity, AI patents, industry-level IV |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm revenue growth |
| ca_measure | — |
| effect_direction | conditional |
| conditions | U-shape with quantified turning point: ~USD 11.3M AI venture funding (Model 5: -0.679 linear, +0.140 quadratic) - below: revenue drag, above: gains; coupling with R&D innovation strategy amplifies (standalone AI insufficient); firm size: effects only for small/medium firms, null for large firms |
| key_finding | AI investment follows a U-shaped payoff: short-term revenue drag, long-term gains - and only firms coupling AI with R&D strategy capture the upside. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + dynamic capabilities |
| industry | cross-industry |
| quality_notes | IV + clustering robustness; investment timing as condition - direct RQ fit |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, sample** — PDF p. 6, 3.1 Sample — ✓ verified, 100% word sequence
   > due to the unavailability of AI-related data, Lithuania is excluded, resulting in a final sample of 26 EU countries
   Ctrl+F: „due to the unavailability of AI-related data, Lithuania“
   → Confirms the coded country_region of 26 EU countries.

2. **sample, method** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > The analysis uses an unbalanced panel dataset of 1,479 firms, applying the Cameron et al . (2011) multi-way clustering (CGM) estimation technique
   Ctrl+F: „The analysis uses an unbalanced panel dataset of“
   → Confirms panel econometrics as method and the unbalanced 1,479-firm panel with CGM multi-way clustering in the sample string.

3. **sample** — PDF p. 6, 3.1 Sample — ✓ verified, 100% word sequence
   > After filtering missing data, the final unbalanced panel data comprises 1,479 firms and 12,942 firm-year observations. The analysis spans the period from 2012 to 2023
   Ctrl+F: „After filtering missing data, the final unbalanced panel“
   → Confirms 1,479 firms, ~12,900 observations, and the 2012-2023 window coded in sample.

4. **ai_measure** — PDF p. 9, 3.2 Measures — ✓ verified, 100% word sequence
   > This study employs the log transformed VC investments in AI (AI_INV) as the main independent variable.
   Ctrl+F: „This study employs the log transformed VC investments“
   → Confirms log AI venture-capital funding as the AI measure.

5. **ai_measure, quality_notes** — PDF p. 22, 6. Limitation and future research — ✓ verified, 100% word sequence
   > the measurement of AI investment relies on the logarithm of venture capital (VC) investments in AI at the country levels, as provided by the OECD AI Policy Observatory
   Ctrl+F: „the measurement of AI investment relies on the“
   → Confirms the OECD AI Policy Observatory data source and is an author-admitted limitation of the AI proxy.
   **⚠ TENSION:** Coded ai_measure reads 'venture-capital funding received', but the measure is COUNTRY-level VC investment matched to firms by country of incorporation, not funding the firm itself received.

6. **ai_measure** — PDF p. 19, 4.2 Additional analysis and robustness test — ✓ verified, 100% word sequence
   > AI intensity (AI_INT), which represents the venture capital investment divided by the total venture capital investment in AI as well as Patent filings, which represents the count of AI related patent filings
   Ctrl+F: „AI intensity (AI_INT), which represents the venture capital“
   → Documents the robustness proxies: AI intensity, AI patent filings (plus AI_NUM, the number of VC investments).
   **⚠ TENSION:** Coded ai_measure lists 'AI job intensity' as a robustness proxy; the paper's robustness proxies are AI_NUM, AI_INT (investment intensity) and patent filings — no job-based measure is used.

7. **ai_measure, quality_notes** — PDF p. 16, 4.2 Additional analysis and robustness test — ✓ verified, 100% word sequence
   > Industry level venture capital (VC) investment in AI across countries was selected as the instrument for this analysis.
   Ctrl+F: „Industry level venture capital (VC) investment in AI“
   → Confirms the industry-level IV noted in ai_measure and the '2SLS-IV robustness' part of quality_notes.

8. **outcome_construct, performance_measure** — PDF p. 7, 3.2 Measures — ⚠ not machine-confirmed on page — open the page, 28% word sequence
   > This study employs changes in revenue growth ( Δ REV_GR), calculated as the first difference of a firm's revenue growth, as the dependent variable.
   Ctrl+F: „This study employs changes in revenue growth (ΔREV_GR),“
   → Confirms firm revenue growth as the performance measure; the outcome is a performance construct, not a CA construct.

9. **effect_direction, key_finding** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > The results reveal a U-shaped relationship between AI investments and revenue growth, indicating that initial AI adoption may hinder revenue growth due to high upfront costs or inefficiencies.
   Ctrl+F: „The results reveal a U-shaped relationship between AI“
   → States the central U-shaped result: initial revenue drag then gains, backing key_finding and the conditional direction (sign flip).

10. **effect_direction** — PDF p. 11, 4.1 Descriptive statistics and main results — ⚠ not machine-confirmed on page — open the page, 37% word sequence
   > The findings reveal an initially negative relationship between AI_INV and Δ REV_GR, while AI_INV 2 shows a positive and significant association at a 5% level of significance.
   Ctrl+F: „The findings reveal an initially negative relationship between“
   → The negative linear plus positive quadratic term is the U-shape sign flip that grounds the conditional direction coding.

11. **effect_direction, conditions, key_finding** — PDF p. 14, 4.1 Descriptive statistics and main results — ✓ verified, 100% word sequence
   > corresponding to approximately USD 11.3 million in AI-related venture funding. This suggests that firms investing below this level may face short term performance declines, while those exceeding this threshold begin to realise the long-term benefits
   Ctrl+F: „approximately USD 11.3 million in AI-related venture funding.“
   → Confirms the quantified USD 11.3M threshold and the below-drag/above-gain pattern coded in conditions and key_finding.

12. **conditions, key_finding** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > integrating AI with innovation strategies substantially enhances revenue growth, highlighting that standalone AI investments are insufficient for achieving entrepreneurial success.
   Ctrl+F: „with innovation strategies substantially enhances revenue growth, highlighting“
   → Backs the coded condition that coupling with R&D innovation strategy amplifies and that standalone AI is insufficient.

13. **conditions** — PDF p. 14, 4.1 Descriptive statistics and main results — ✓ verified, 100% word sequence
   > Economically, based on the regression estimates in Model 5, the turning point is observed at a log AI investment value of approximately 2.425
   Ctrl+F: „Economically, based on the regression estimates in Model“
   → Confirms the Model 5 turning point underlying the coded quantified threshold (coefficients -0.679 linear / +0.140 quadratic appear in Table 4, Model 5).

14. **conditions** — PDF p. 14, 4.2 Additional analysis and robustness test — ✓ verified, 100% word sequence
   > showing a U-shaped relationship between AI investments and revenue growth, and a significant positive effect of the interaction between AI and R&D on revenue growth. However, for large firms, no significant relationships were observed.
   Ctrl+F: „showing a U-shaped relationship between AI investments and“
   → Confirms the AI x R&D interaction as a condition; also documents a firm-size split of the effect.
   **⚠ TENSION:** The paper identifies firm size as an additional moderator (U-shape and AI x R&D significant only for small/medium firms, null for large firms) — not listed in the coded conditions.

15. **theoretical_lens** — PDF p. 4, 2.2 Theoretical framework and hypotheses — ✓ verified, 100% word sequence
   > Resource Based Theory (RBT) suggests that a firm's resources and capabilities are critical for achieving competitive advantage and sustaining long-term success (Barney, 2001).
   Ctrl+F: „Resource Based Theory (RBT) suggests that a firm’s“
   → Shows the paper's explicit theoretical framework (RBT, extended by Dynamic Capabilities Theory on the same page).
   **⚠ TENSION:** Coded theoretical_lens is 'none explicit (entrepreneurship/innovation economics)', but the paper states an explicit RBT + Dynamic Capabilities framework (Section 2.2) and claims contributions to both.

16. **theoretical_lens** — PDF p. 20, 5.1 Theoretical contributions — ✓ verified, 100% word sequence
   > This study makes several important contributions to the RBT and the DCT.
   Ctrl+F: „This study makes several important contributions to the“
   → The paper frames its contribution explicitly within RBT and Dynamic Capabilities Theory.
   **⚠ TENSION:** Same as above: coded lens 'none explicit' conflicts with the paper's explicit RBT/DCT framing.

17. **industry** — PDF p. 6, 3.1 Sample — ✓ verified, 100% word sequence
   > The sample encompasses firms from a diverse array of industries, including communication services, consumer discretionary, consumer staples, energy, financials, health care, industrials, information technology, materials, real estate, and utilities.
   Ctrl+F: „The sample encompasses firms from a diverse array“
   → Confirms the cross-industry coding.

**⚠ ROW CHECK:** Three points for the author: (1) theoretical_lens coded 'none explicit' although the paper has an explicit RBT + DCT framework (Section 2.2, Section 5.1); (2) ai_measure details: the VC funding proxy is country-level (matched by country of incorporation), not funding 'received' by the firm, and the robustness proxy is AI investment intensity/patents, not 'AI job intensity'; (3) coded conditions omit the firm-size moderator (effects significant only for small/medium firms). ca_measure emptiness confirmed — competitive advantage appears only as RBT framing/conclusion rhetoric, no CA construct is measured. quality_notes part 'investment timing as condition - direct RQ fit' is coder commentary, not source-based; 'IV + clustering robustness' is evidenced. Adjudicated direction=conditional (U-shape sign flip) left untouched per case law.

---

## S27 — Basnet A. et al. (2025) — International Review of Financial Analysis (AJG 3)

DOI: 10.1016/j.irfa.2025.104378 · status: final · PDF: `Basnet_2025_j-irfa-2025-104378.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | US firms, 10-K filings 2005-2018 (pre-hype window); AI mentions classified actionable/speculative/irrelevant; causal design |
| method | panel econometrics |
| ai_measure | 10-K text (actionable vs speculative vs irrelevant AI disclosures) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm value (market valuation); R&D spending, patents, lagged productivity as channels |
| ca_measure | — |
| effect_direction | conditional |
| conditions | disclosure SUBSTANCE: actionable disclosures -> valuation gains + innovation + lagged productivity; speculative/irrelevant -> nothing; silent or vague peers penalized |
| key_finding | Markets reward only substantive (actionable) AI disclosures - early adopters with real implementation plans gain value via innovation; vague AI talk earns nothing. |
| *not printed (coding data only)* | |
| theoretical_lens | disclosure/signaling (finance) |
| industry | cross-industry |
| quality_notes | Causal identification; complements AI-washing evidence (Song X. 2026) |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on a 2005 -2018 sample, a formative period before AI became mainstream, this paper examines how early AI adoption and its disclosure in corporate filings affect U.S. firms.
   Ctrl+F: „before AI became mainstream, this paper examines how“
   → Confirms US firms, the 2005-2018 window, and the coded 'pre-hype window' characterization.

2. **country_region, sample, ai_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > To study the impact of AI narratives on firm performance, we collect 10-K annual filings for all U.S. companies in the Russell 3000 Index from 2005 to 2018.
   Ctrl+F: „To study the impact of AI narratives on“
   → Confirms the US 10-K filings 2005-2018 sample coded in sample and country_region.

3. **sample** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > Our final sample includes 2615 firms.
   Ctrl+F: „Our final sample includes“
   → Gives the sample size (2,615 firms), a detail the coded sample string omits.

4. **sample, method, quality_notes** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > Our identification strategy leverages within-firm variation through panel fixed-effects models, complemented by a Local Projections Difference-in-Differences approach as a robustness check. This allows us to interpret our findings as causal rather than merely associational
   Ctrl+F: „variation through panel fixed-effects models, complemented by a“
   → Confirms panel econometrics (panel fixed-effects + LP-DiD) and the 'causal design'/'causal identification' parts of sample and quality_notes.

5. **ai_measure, outcome_construct, performance_measure, quality_notes** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 48% word sequence
   > Analyzing 10-K filings, we categorize AI-related mentions as actionable, speculative, or irrelevant. We establish causal links between these disclosures and firm value, with innovation and productivity as likely channels.
   Ctrl+F: „we categorize AI-related mentions as actionable, speculative, or“
   → Confirms the 10-K text measure with the three disclosure categories, firm value as outcome, innovation/productivity as channels, and the causal-identification claim in quality_notes.

6. **ai_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > We first identify whether companies mention any AI-related keywords and then classify their usage as actionable , speculative , and irrelevant .
   Ctrl+F: „identify whether companies mention any AI-related keywords and“
   → Confirms the coded actionable/speculative/irrelevant classification of 10-K AI mentions.

7. **performance_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > To capture innovation, we use R & D expenses (the ratio of research and development expenses to total assets) and patent counts (the natural logarithm of one plus the number of patent registrations).
   Ctrl+F: „expenses (the ratio of research and development expenses“
   → Confirms R&D spending and patents as the coded channel measures (labor productivity = sales per employee and Tobin's Q for market valuation follow in the same paragraph).

8. **performance_measure, conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > modest gains in labor productivity (measured by sales per employee) emerging two to three years after an actionable AI disclosure, but only for firms supporting such disclosures with increased subsequent R & D spending
   Ctrl+F: „modest gains in labor productivity (measured by sales“
   → Confirms the coded 'lagged productivity' channel and that it holds only for actionable disclosures backed by R&D — part of the substance condition.

9. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Actionable disclosures outlining clear implementation plans yield significant valuation benefits, particularly upon first introduction, whereas speculative or irrelevant disclosures have no impact.
   Ctrl+F: „particularly upon first introduction, whereas speculative or irrelevant“
   → The effect exists only for the actionable disclosure category — backing the conditional direction and the disclosure-substance condition.

10. **effect_direction, conditions** — p. 8–10 (PDF p. 8) — ✓ verified, 100% word sequence
   > we find no significant effect for the Speculative or Irrelevant dummies (Columns 4 and 5). In other words, first-time mentions that are vague or tangential do not meaningfully affect firm valuation.
   Ctrl+F: „for the Speculative or Irrelevant dummies (Columns 4“
   → Confirms 'speculative/irrelevant -> nothing' in conditions and the null branch of the conditional direction.

11. **effect_direction, conditions** — p. 9 (PDF p. 9) — ✓ verified, 91% word sequence
   > the impact of an Actionable keyword introduction is essentially on par with the overall Keyword introduction effect (~5.0 %). This indicates that valuation gains from initial AI disclosures are driven largely by substantive, actionable narratives.
   Ctrl+F: „impact of an Actionable keyword introduction is essentially“
   → Shows the aggregate keyword effect is carried by the actionable subset — the basis for coding direction as conditional on disclosure substance rather than positive on average.

12. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We show that early adopters of actionable disclosures gain competitive advantages, while peers that either remain silent or offer only vague AI disclosures face market penalties.
   Ctrl+F: „show that early adopters of actionable disclosures gain“
   → Backs the coded condition 'silent or vague peers penalized'. Note: 'competitive advantages' here is framing rhetoric, no CA construct is measured (case law: framing = performance).

13. **conditions** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > firms that only offer speculative AI mentions ( Speculative Treated ) when competitors make actionable AI disclosures ( Competitor Actionable Treated ) are penalized by the market
   Ctrl+F: „Treated) when competitors make actionable AI disclosures (Competitor“
   → Confirms the peer-penalty condition: vague disclosers are penalized when competitors make actionable commitments.

14. **key_finding** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > We find that financial markets distinguish between ' AI hype ' and genuine AI-driven strategies in corporate narratives. Firms announcing credible AI initiatives in their business descriptions enjoy significant valuation premiums
   Ctrl+F: „credible AI initiatives in their business descriptions enjoy“
   → The paper's own conclusion statement of the central result: only substantive AI disclosures are rewarded.

15. **theoretical_lens** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > Drawing on signaling theory, the disclosure of actionable AI narratives provides firms with a strategic tool to credibly communicate their intent to lead in technological innovation.
   Ctrl+F: „Drawing on signaling theory, the disclosure of actionable“
   → Confirms the signaling side of the coded disclosure/signaling (finance) lens.

16. **theoretical_lens** — p. 3 (PDF p. 3) — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > Given the limited research on the subject, we examine the authenticity of AI disclosures and their impact on firm valuation.
   Ctrl+F: „Given the limited research on the subject, we“
   → Confirms the disclosure-credibility framing of the coded lens (Section 2.3 on disclosure, narrative credibility, and financial markets).

17. **industry** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > AI-related keywords are mentioned more frequently after 2015 and are mostly concentrated in the business equipment industry.
   Ctrl+F: „mentioned more frequently after 2015 and are mostly“
   → The Fama-French industry heat map discussion shows the Russell 3000 sample spans all industries, backing the cross-industry coding.

*Row check OK: quality_notes part 'complements AI-washing evidence (Song X. 2026)' is coder cross-corpus commentary, not sourced from this paper. ca_measure emptiness confirmed: 'competitive advantages' appears only as abstract/introduction rhetoric, the measured outcome is Tobin's Q. One nuance for the author: the aggregate first-time Keyword effect is itself positive and significant (~5.0%, Table 5 Col. 1), but the paper attributes it to the actionable subset (speculative/irrelevant null) — consistent with the conditional coding on disclosure substance. Direction quote wording like 'Speculative Treated' kept with the source's spacing around italics.*

---

## S28 — Bin-Nashwan S.A. et al. (2025) — Technology in Society (AJG 2)

DOI: 10.1016/j.techsoc.2025.102913 · status: final · PDF: `BinNashwan_2025_j-techsoc-2025-102913.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 433 valid responses (461 screened, 5000+ invitations), Chinese accounting professionals, online survey Dec 2023-Jan 2024, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI-infused knowledge systems) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | accounting-firm performance: efficiency, accuracy, compliance, reporting innovation, timeliness (survey) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | no direct AIK->performance path modeled; mediators: green human capital + green structural capital (carry effect), green RELATIONAL capital channel NULL; sustainability culture (moderator on GIC->performance) |
| key_finding | AI-infused knowledge improves accounting-firm performance through green human and structural capital, amplified by sustainability culture; relational capital plays no role. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + KBV |
| industry | accounting services |
| quality_notes | Perceptual panel survey; author affiliations (Oman/Malaysia) misleading - respondents are Chinese; GIC items benchmarked vs competitors |
| coding_status | final |

### Evidence

1. **country_region, sample, quality_notes** — p. 5 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 52% word sequence
   > The online survey took place from December 21, 2023 to January 7, 2024. Over 5000 invitations via online platforms were sent to Chinese panelists to participate in the study.
   Ctrl+F: „took place from December 21, 2023 to January“
   → Backs the coded survey window, the 5000+ invitations, the Chinese sample, and the online-panel nature of the survey.

2. **sample, industry** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > The sample was chosen randomly and fulfilled specific criteria, including accounting firms, and to be responded to by accounting professionals, such as chief financial officers (CFOs), audit managers, senior accountants, or senior auditors.
   Ctrl+F: „specific criteria, including accounting firms, and to be“
   → Respondents are accounting professionals in accounting firms, backing sample and the accounting-services industry code.

3. **sample** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > The survey included 461 respondents who managed to pass the screening criterion among all who took the assessment. An analysis was performed using 433 valid responses because the remaining data underwent an outlier exclusion process.
   Ctrl+F: „The survey included 461 respondents who managed to“
   → Backs the coded 433 valid responses out of 461 screened.

4. **method, ai_measure, outcome_construct** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > The researchers used 44 indicators in an online survey to assess 6 constructs which were AI-infused knowledge and green human capital, green structural capital, green rational capital, sustainability culture and accounting performance.
   Ctrl+F: „The researchers used 44 indicators in an online“
   → AI-infused knowledge is a survey construct, and accounting performance is the measured outcome construct.

5. **method** — p. 7 (PDF p. 7) — ✓ verified, 90% word sequence
   > The researchers used SmartPLS variance-based partial least squares structural equation modeling (PLS-SEM) software for assessing the integrated model.
   Ctrl+F: „The researchers used SmartPLS variance-based partial least squares“
   → Backs the survey-SEM method code (PLS-SEM in SmartPLS).

6. **method, quality_notes** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > The study employed a cross-sectional survey, capturing the nexuses between AI and GIC, and accounting firm performance at a single point in time.
   Ctrl+F: „survey, capturing the nexuses between AI and GIC,“
   → Authors admit the cross-sectional perceptual survey design, backing the quality note.

7. **outcome_construct, performance_measure, effect_direction, conditions** — p. 1 (PDF p. 1) — ✓ verified, 81% word sequence
   > In turn, these two internal dimensions, GHC and GSC, had a significant impact on accounting performance across various aspects, including efficiency, accuracy, compliance with environmental standards, innovation in reporting, and timeliness.
   Ctrl+F: „In turn, these two internal dimensions, GHC and“
   → The outcome is accounting-firm performance with exactly the coded facets; the AI effect reaches it via the GHC/GSC mediating channels.

8. **ca_measure, quality_notes** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > GHC1: The contribution of environmental protection by employees in our firm is better than our major competitors.
   Ctrl+F: „by employees in our firm is better than“
   → GIC items are benchmarked against competitors (quality note); the competitor comparison sits in mediator items, not in a measured CA outcome construct, confirming the empty ca_measure.

9. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The analysis shows interesting outcomes: AIK positively and significantly affected the internal dimensions of GIC, green human capital (GHC) and green structural capital (GSC) within accounting firms, while green rational capital (GRC) had no effect.
   Ctrl+F: „The analysis shows interesting outcomes: AIK positively and“
   → AIK works through GHC/GSC while the GRC channel is null - the paper's 'green rational capital' is the relational dimension, backing 'conditional' and the coded null channel.

10. **effect_direction, conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The analysis shows that the explanatory power of the collectively direct impact of the proposed model, i.e., GHC, GSC, and GRC, as well as the moderating role of SUC, in ADP was 42 %.
   Ctrl+F: „explanatory power of the collectively direct impact of“
   → Accounting performance is predicted only by the GIC dimensions plus SUC - no direct AIK->performance path is modeled, backing 'conditional' ('ADP' is the paper's typo for ACP).

11. **effect_direction, conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > However, the impact of AIK on GRC (β = 0.016; p = 0.865) within accounting firms was insignificant. Thus, H3 is rejected.
   Ctrl+F: „However, the impact of AIK on GRC (β = 0.016;“
   → The AIK->GRC path is null, backing the coded null relational-capital channel.

12. **effect_direction, conditions, key_finding** — p. 7 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 26% word sequence
   > Additionally, we found that accounting firms' performance is influenced by two components of GIC, i.e., GHC (β = 0.390; p = 0.000), and GSC (β = 0.194; p = 0.005).
   Ctrl+F: „Additionally, we found that accounting firms’ performance is“
   → Green human and structural capital are the mediating channels that carry the effect into performance.

13. **conditions, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawn from the resource-based view (RBV) and knowledge-based view (KBV), sustainability culture (SUC) is integrated into the model as a moderator variable to provide an in-depth understanding of this matter.
   Ctrl+F: „Drawn from the resource-based view (RBV) and knowledge-based“
   → Abstract names RBV + KBV as the theoretical frame and SUC as the moderator condition.

14. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Intriguingly, SUC was found to significantly moderate the association between GIC dimensions and accounting firm performance.
   Ctrl+F: „significantly moderate the association between GIC dimensions and“
   → Backs the coded moderator: sustainability culture on the GIC->performance link.

15. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > In contrast, GRC failed to report a significant effect on accounting performance (β = 0.074; p = 0.616). Hence, H4 and H5 are accepted, while H6 is rejected.
   Ctrl+F: „In contrast, GRC failed to report a significant“
   → The GRC->performance path is also null, completing the coded 'relational capital plays no role'.

16. **quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Department of Accounting, College of Commerce and Business Administration, Dhofar University, Oman
   Ctrl+F: „Department of Accounting, College of Commerce and Business“
   → Author affiliations are Oman/Malaysia while the sample is Chinese - backing the quality note that affiliations are misleading about the sample country.

*Row check OK: Adjudicated row (brief: conditional, no direct path, GRC null, 433 China) fully matches the full text. Empty ca_measure confirmed: competitor-benchmarked wording occurs only inside GIC mediator items, no CA outcome construct. Terminology: the paper mostly writes 'green rational capital' for GRC (its own label; the relational dimension), and 'ADP'/'IAK' typos appear in the original. Quality-note word 'panel' refers to the online panelist pool, not panel data.*

---

## S29 — Cao L. et al. (2025) — European Management Review (AJG 3)

DOI: 10.1111/emre.70042 · status: final · PDF: `Cao_2025_emre-70042.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | Study 1: instrument from 6,519 AI documents of 37 retailers; Study 2: fsQCA on survey of 140 U.S.-based retail managers |
| method | fsQCA |
| ai_measure | validated multi-level instrument (AI integration at task/function/firm level) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | efficiency and innovation outcomes (configurational) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | CONFIGURATIONAL: no single AI function suffices - synergistic combinations (esp. customer service + cybersecurity with other functions); emergent capabilities: adaptive learning, predictive analytics, uncertainty mitigation |
| key_finding | Retail performance comes from configurations of AI-enabled functions, not isolated AI uses - a directly configurational (fsQCA) result. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities + business process perspective |
| industry | retail |
| quality_notes | fsQCA - Fredrich-school methodology; two-stage instrument validation \| SAMPLE-CHECK OK: fsQCA/conditional confirmed (configurational design) |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 6 (PDF p. 6) — ✓ verified, 94% word sequence
   > In Study 2, we surveyed 140 U.S.-based retail managers to measure AI engagement and performance outcomes.
   Ctrl+F: „In Study 2, we surveyed 140 U.S.-based“
   → Backs the coded Study-2 sample of 140 U.S.-based retail managers (USA, retail).

2. **country_region, quality_notes** — p. 14 (PDF p. 14) — ✓ verified, 81% word sequence
   > First, the data in Study 1 spans 2017-2022, and Study 2 draws from U.S.-based retail firms, which may limit the generalizability of findings across time, regions, and industries.
   Ctrl+F: „1 spans 2017–2022, and Study 2 draws from“
   → Authors confirm the U.S. base of the firm sample and admit its generalizability limits.

3. **sample, ai_measure, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using a sequential mixed-methods design, we first construct a validated measurement instrument based on grounded analysis of 6,519 AI-related documents from 37 retailers.
   Ctrl+F: „first construct a validated measurement instrument based on“
   → Backs the Study-1 sample (6,519 documents, 37 retailers), the validated multi-level AI instrument, and the two-stage instrument-validation quality note.

4. **sample, method, performance_measure** — p. 1 (PDF p. 1) — ✓ verified, 75% word sequence
   > We then apply fuzzy-set qualitative comparative analysis (fsQCA) to survey data from 140 executives to identify configurations of AI-enabled functions associated with efficiency, innovation, or both.
   Ctrl+F: „comparative analysis (fsQCA) to survey data from 140“
   → fsQCA on the 140-executive survey generates the AI-outcome evidence (Study 1 is instrument development), backing the fsQCA method code and the efficiency/innovation outcomes.

5. **ai_measure** — p. 9 (PDF p. 9) — ✓ verified, 65% word sequence
   > Our questionnaire assessed the engagement of their companies in each of the 28 AIenabled tasks (as detailed in Table 1).
   Ctrl+F: „the engagement of their companies in each of“
   → AI is measured through the validated instrument's 28 task-level items aggregated into five business functions.

6. **outcome_construct, performance_measure** — p. 9 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 21% word sequence
   > For organizational performance, we chose to measure AI value creation rather than traditional financial performance to mitigate potential endogeneity.
   Ctrl+F: „we chose to measure AI value creation rather“
   → The outcome is organizational performance (efficiency/innovation value creation), i.e. performance, not a CA construct.

7. **performance_measure** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > we measured efficiency using four items: 'save on labor costs,' 'save transaction costs,' 'increase the speed of the value chain process,' and 'improve operational accuracy.'
   Ctrl+F: „using four items: “save on labor costs,” “save“
   → Gives the concrete efficiency items behind the coded 'efficiency and innovation outcomes'.

8. **ca_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Contextualizing AI within specific business environments enables firms to leverage AI more effectively, fostering competitive advantages and improving performance.
   Ctrl+F: „AI within specific business environments enables firms to“
   → Competitive advantage appears only as theory-section framing; the measured outcomes are efficiency and innovation, confirming the empty ca_measure per case law.

9. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results show that superior performance stems not from isolated AI uses but from synergistic combinations - particularly those involving customer service and cybersecurity - interacting with other functions.
   Ctrl+F: „The results show that superior performance stems not“
   → Performance arises only from configurations, backing 'conditional' and the coded synergistic-combinations condition.

10. **effect_direction, key_finding** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > The fsQCA results demonstrate that AI-enabled business functions enhance firm performance not through isolated applications but through a strategic combination across business processes.
   Ctrl+F: „business functions enhance firm performance not through“
   → The directly configurational (fsQCA) result behind the coded key_finding and 'conditional' direction.

11. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 96% word sequence
   > These configurations appear to give rise to emergent capabilities such as adaptive learning, predictive analytics, and uncertainty mitigation, enabling firms to reconcile exploitation and exploration.
   Ctrl+F: „to give rise to emergent capabilities such as“
   → Backs the coded emergent capabilities: adaptive learning, predictive analytics, uncertainty mitigation.

12. **conditions** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > The analysis showed that none of the variables qualify as a 'must-have' condition for high organizational performance.
   Ctrl+F: „The analysis showed that none of the variables“
   → Necessity analysis backs the coded 'no single AI function suffices'.

13. **conditions, key_finding** — p. 13 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 40% word sequence
   > Overall, the ability to reconcile efficiency and innovation does not stem from individual AI functions but from their coordinated deployment.
   Ctrl+F: „does not stem from individual AI functions but“
   → Restates that only coordinated configurations, not single functions, produce the dual outcomes.

14. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Addressing this gap, we draw on a business process perspective and dynamic capability theory to develop a multi-level framework of AI integration at the task, function, and firm levels.
   Ctrl+F: „Addressing this gap, we draw on a business“
   → Abstract names the two coded lenses: business process perspective and dynamic capability theory.

*Row check OK: Sample-spot-check row (brief: fsQCA/performance/conditional OK, 140 U.S. retail managers) fully matches the full text. Empty ca_measure confirmed (CA only as framing; outcomes are efficiency/innovation). quality_notes partly coder commentary: 'Fredrich-school methodology' and the 'SAMPLE-CHECK OK' tag are coder/process notes without a source passage; the source-based parts (fsQCA, two-stage validated instrument) are quoted.*

---

## S30 — Chakraborty D. (2025) — Current Issues in Tourism (AJG 2)

DOI: 10.1080/13683500.2025.2517829 · status: final · PDF: `Chakraborty_2025_13683500-2025-2517829.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India |
| sample | two-wave online survey, India: 1,487 invited, wave 1 n=437, wave 2 n=408 (hotel/resort managers, multi-channel recruitment) |
| method | survey-SEM |
| ai_measure | survey construct (GenAI adoption) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | firm/organisational performance (survey scales) |
| ca_measure | competitive advantage / competitive positioning (survey scale) |
| effect_direction | positive |
| conditions | technological readiness (TOE driver); leader narcissism moderates adoption-factor relationships and GAI effects on competitive positioning |
| key_finding | GenAI adoption improves hotels competitive advantage and performance, with leadership personality (narcissism) shaping how adoption translates into outcomes. |
| *not printed (coding data only)* | |
| theoretical_lens | TOE + personality (narcissism) |
| industry | hospitality (hotels & resorts) |
| quality_notes | Longitudinal design (rare in corpus); perceptual measures |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 7 (PDF p. 8) — ⚠ not machine-confirmed on page — open the page, 43% word sequence
   > The initial period was from November 2022 to February 2023, and the subsequent was from December 2023 to February 2024. The participants were managers (senior and middle-level employees) of hotels and resorts in India.
   Ctrl+F: „The initial period was from November 2022 to“
   → Backs the two-wave design, the hotel/resort-manager sample, India, and the hospitality industry code.

2. **country_region, sample** — p. 8 (PDF p. 9) — ✓ verified, 100% word sequence
   > An online survey was sent to a diverse pool of 1,487 participants from various cities across India.
   Ctrl+F: „An online survey was sent to a diverse“
   → Backs the coded 1,487 invited participants in India.

3. **sample** — p. 8 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 47% word sequence
   > The survey was distributed via multiple channels such as email, LinkedIn, Facebook Pages, and WhatsApp. In the initial phase, there were 437 responses, and the second wave yielded 408 participants.
   Ctrl+F: „The survey was distributed via multiple channels such“
   → Backs the multi-channel recruitment and the coded wave sizes n=437 (wave 1) and n=408 (wave 2).

4. **method** — p. 8 (PDF p. 9) — ✓ verified, 100% word sequence
   > I used Structural Equation Modeling (SEM) with Smart PLS for this study.
   Ctrl+F: „I used Structural Equation Modeling (SEM) with Smart“
   → Backs the survey-SEM method code (PLS-SEM in SmartPLS).

5. **ai_measure, ca_measure, effect_direction** — p. 6 (PDF p. 7) — ✓ verified, 100% word sequence
   > H4: Intention to adopt GAI is positively related to competitive advantage
   Ctrl+F: „H4: Intention to adopt GAI is positively related“
   → GenAI adoption (intention) is the survey construct, hypothesized to raise the distinct competitive-advantage construct - the own-scale-plus-hypothesis requirement for coding CA.

6. **ai_measure, performance_measure, effect_direction** — p. 6 (PDF p. 7) — ✓ verified, 100% word sequence
   > H5: Intention to adopt GAI is positively related to firm performance
   Ctrl+F: „Intention to adopt GAI is positively related to“
   → Parallel hypothesis for the firm-performance construct, backing the 'both' coding and the positive direction.

7. **outcome_construct, performance_measure, ca_measure** — p. 1 (PDF p. 2) — ✓ verified, 100% word sequence
   > It investigates the implications of GAI towards the competitive advantage, firm performance, and organisation's performance.
   Ctrl+F: „of GAI towards the competitive advantage, firm performance,“
   → Both outcome constructs - competitive advantage and firm/organisational performance - are studied, backing outcome_construct 'both'.

8. **outcome_construct, quality_notes** — p. 7 (PDF p. 8) — ✓ verified, 92% word sequence
   > This study employs a longitudinal research design which allows tracking of generative AI's (GAI) impact on competitive advantage and firm performance over time.
   Ctrl+F: „design which allows tracking of generative AI’s (GAI)“
   → Backs the longitudinal-design quality note and the dual outcome constructs.

9. **outcome_construct, performance_measure, ca_measure** — p. 9 (PDF p. 10) — ✓ verified, 100% word sequence
   > The R-squared (R2) values for the endogenous variables are 18%, 32%, and 32.5% for CGE, FCE, and IAI for t1 and 19%, 20.5%, 33.3%, respectively, in t2
   Ctrl+F: „The R-squared (R2) values for the endogenous variables“
   → Competitive advantage (CGE) and firm performance (FCE) are modeled as separate endogenous constructs, backing the analytic separation behind 'both'.

10. **performance_measure, ca_measure, quality_notes** — p. 8 (PDF p. 9) — ✓ verified, 100% word sequence
   > The items were evaluated using a five-point scale, ranging from 1 ('strongly disagree') to 5 ('strongly agree').
   Ctrl+F: „a five-point scale, ranging from 1 (‘strongly disagree’)“
   → All constructs, including performance and CA, are perceptual five-point survey scales - backing the 'perceptual measures' quality note.

11. **performance_measure, effect_direction, key_finding** — p. 12 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 39% word sequence
   > The positive relationship between intention to adopt GAI and firm performance (H5) shows managers' dedication to using innovative technology to improve operational efficiency, guest experiences, and performance measures.
   Ctrl+F: „The positive relationship between intention to adopt GAI“
   → Discussion confirms the positive GAI-adoption effect on firm performance (H5 supported in both waves: 0.249 t1, 0.235 t2), backing effect_direction positive.

12. **ca_measure, effect_direction, key_finding** — p. 12 (PDF p. 13) — ✓ verified, 100% word sequence
   > Several reasons explain the positive correlation between enterprises' ambition to use Generative AI (GAI) and competitive advantage (H4).
   Ctrl+F: „Several reasons explain the positive correlation between enterprises’“
   → Discussion confirms the positive GAI-adoption effect on competitive advantage (H4 supported in both waves: 0.376 t1, 0.257 t2).

13. **conditions, theoretical_lens** — p. 1 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 6% word sequence
   > the Technological-OrganizationalEnvironmental (TOE) framework, this study further explains how narcissism moderates the relationship between the factors that assist in adopting GAI and GAI's moderating effect on the overall competitive positioning and organisational outcomes.
   Ctrl+F: „narcissism moderates the relationship between the factors that“
   → Abstract names TOE plus narcissism (personality) as the coded lens and states the narcissism-moderation claim behind the coded conditions.

14. **conditions, quality_notes** — p. 1 (PDF p. 2) — ✓ verified, 100% word sequence
   > The study uses longitudinal analysis to shed some light about the influences related to GAI adoption, including the level of technological readiness in the organisation, as well as certain individual traits.
   Ctrl+F: „analysis to shed some light about the influences“
   → Backs the coded condition 'technological readiness (TOE driver)' and the longitudinal-design quality note.

15. **conditions, key_finding** — p. 12 (PDF p. 13) — ✓ verified, 100% word sequence
   > leading narcissistic leaders to play a more significant role in shaping strategic decisions regarding GAI adoption and competitive positioning
   Ctrl+F: „leading narcissistic leaders to play a more significant“
   → Discussion of the t2 moderation backs the coded clause that narcissism shapes how GAI adoption translates into competitive positioning.

**⚠ ROW CHECK:** All columns evidenced and the adjudication fact-gap resolution (India, 1,487 invited, waves 437/408) matches the text. One wording point for the author: the coded conditions clause 'narcissism moderates adoption-factor relationships and GAI effects on competitive positioning' mirrors the paper's abstract, but Table 5 locates the significant moderation on the firm-performance side - NIM x IAI -> FCE is significant in both waves (-0.178 t1, +0.152 t2) and NIM x CGE -> FCE in t2 only, while NIM x IAI -> CGE (competitive positioning) stays non-significant (p = .075) in both waves; no interactions with the TOE adoption factors themselves were tested. Consider tightening the clause to 'narcissism moderates how adoption translates into firm performance'. Direction 'positive' is unaffected (H4/H5 positive and significant in both waves; moderators belong in conditions).

---

## S31 — Chiu S.Y. et al. (2025) — Business Ethics the Environment and Responsibility (AJG 2)

DOI: 10.1111/beer.70054 · status: final · PDF: `Chiu_2025_beer-70054.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Taiwan |
| sample | 33 publicly listed semiconductor firms; three-stage DEA (profit, sustainability, market) + Tobit regressions |
| method | DEA |
| ai_measure | patents (AI-driven innovation proxied by patent activity) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | stage efficiencies: profitability, ESG/sustainability, market valuation |
| ca_measure | — |
| effect_direction | mixed |
| conditions | stage-specific: AI innovation positive on SUSTAINABILITY + MARKET stage efficiency, insignificant on PROFIT stage (size/leverage drive profit); firm scale raises profit efficiency but LOWERS sustainability/market efficiency (asymmetry) |
| key_finding | AI-driven innovation lifts sustainability and market-valuation efficiency in semiconductors but NOT short-term profit efficiency - the payoff is stage-specific. |
| *not printed (coding data only)* | |
| theoretical_lens | efficiency analysis (DEA framework, no grand theory) |
| industry | semiconductors |
| quality_notes | Per full-text verdict: include; AI = patent proxy; n=33 small |
| coding_status | final |

### Evidence

1. **country_region, sample, method, outcome_construct, performance_measure, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > applying a three-stage Data Envelopment Analysis (DEA) to evaluate the performance of 33 publicly listed semiconductor firms in Taiwan across profitability, sustainability, and market value
   Ctrl+F: „Analysis (DEA) to evaluate the performance of 33“
   → Abstract names the DEA method, the 33-firm Taiwanese semiconductor sample, and the three performance dimensions coded as performance_measure.

2. **country_region, sample, industry, quality_notes** — p. 21 (PDF p. 21) — ✓ verified, 100% word sequence
   > This study focuses on 33 publicly listed semiconductor firms in Taiwan from 2018 to 2022.
   Ctrl+F: „This study focuses on 33 publicly listed semiconductor“
   → Limitations section restates the small n=33 single-country, single-industry sample flagged in quality_notes.

3. **sample** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > Financial statement data spanning 5 years (January 1, 2018, to December 31, 2022) was obtained from the Taiwan Economic Journal (TEJ) database.
   Ctrl+F: „(January 1, 2018, to December 31, 2022) was“
   → Specifies the observation window and data source of the 33-firm sample.

4. **method** — p. 5 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 40% word sequence
   > This study adopts a two-phase analytical framework, applying DEA in the first stage and Tobit regression in the second.
   Ctrl+F: „DEA in the first stage and Tobit regression“
   → Methods section confirms DEA as the primary method with Tobit regressions, as coded in method and sample.

5. **ai_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > AI-driven innovation is proxied by patent activity.
   Ctrl+F: „innovation is proxied by patent activity.“
   → Abstract states the patent proxy coded as ai_measure.

6. **ai_measure, effect_direction, conditions** — p. 18 (PDF p. 18) — ✓ verified, 60% word sequence
   > the number of patents-used as a proxy for AI-driven innovations-is positively and significantly associated with efficiency in the Sustainability and Market stages
   Ctrl+F: „associated with efficiency in the Sustainability and“
   → Positive AI effect on the sustainability and market stages — one half of the coded 'mixed' split and the stage-specific condition.

7. **ai_measure, quality_notes** — p. 20 (PDF p. 20) — ✓ verified, 100% word sequence
   > While patent counts are widely used as proxies for AI-driven innovation, they may not fully capture non-patented process innovations or reflect individual patents' quality and strategic relevance.
   Ctrl+F: „While patent counts are widely used as proxies“
   → Authors themselves flag the patent-proxy limitation noted in quality_notes.

8. **performance_measure, theoretical_lens** — p. 2 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 23% word sequence
   > we apply a three-dimensional efficiency framework based on Data Envelopment Analysis (DEA), which evaluates firm performance across the Profit stage, Sustainability stage, and Market stage
   Ctrl+F: „based on Data Envelopment Analysis (DEA), which“
   → The study's framework is the DEA efficiency framework itself, matching the coded lens 'efficiency analysis (DEA framework)' and the stage-efficiency performance measures.

9. **effect_direction, conditions** — p. 18 (PDF p. 18) — ✓ verified, 100% word sequence
   > one additional patent increases Sustainability stage efficiency by 0.0001 and Market stage efficiency by 0.0034, while its impact on Overall and Profit stage efficiency remains economically small (0.0001) and statistically insignificant
   Ctrl+F: „stage efficiency by 0.0001 and Market stage efficiency“
   → Insignificant AI effect on the profit stage — the other half of the coded 'mixed' direction (sign split across outcome components).

10. **effect_direction, key_finding** — p. 18 (PDF p. 18) — ✓ verified, 100% word sequence
   > This pattern suggests that AI-related innovation contributes more to long-term environmental and market-oriented performance than to short-term profitability.
   Ctrl+F: no reliable search string in the PDF text layer — open PDF p. 18 and check visually
   → The paper's own summary of its central result: AI payoff is stage-specific, lifting sustainability/market but not short-term profit efficiency.

11. **conditions** — p. 18 (PDF p. 18) — ⚠ not machine-confirmed on page — open the page, 25% word sequence
   > a one-unit increase in enterprise scale raises Profit stage efficiency by 0.0811 but reduces Sustainability and Market stage efficiency by -0.0380 and -0.5005, respectively
   Ctrl+F: „scale raises Profit stage efficiency by 0.0811 but“
   → Backs the coded condition that firm scale raises profit efficiency but lowers sustainability/market efficiency (asymmetry).

12. **conditions** — p. 18–20 (PDF p. 18) — ✓ verified, 63% word sequence
   > Financial leverage, measured by the debt-to-asset ratio, is positively and statistically significantly associated with Profit stage efficiency
   Ctrl+F: „with Profit stage efficiency,“
   → Backs the coded condition that leverage (with size) drives the profit stage rather than AI.

13. **theoretical_lens** — p. 4 (PDF p. 4) — ⚠ not machine-confirmed on page — open the page, 54% word sequence
   > Based on the creating shared value (CSV) perspective (Porter and Kramer 2011), sustainability is framed as a compliance requirement and a strategic driver of competitive advantage.
   Ctrl+F: „is framed as a compliance requirement and a“
   → The only grand-theory reference is CSV as background framing; competitive advantage appears here as rhetoric only, consistent with the 'no grand theory' lens and empty ca_measure.

*Row check OK: ca_measure empty is correct: competitive advantage appears only as CSV framing rhetoric (p. 4 quote), no CA construct is measured. quality_notes part 'Per full-text verdict: include' is coder commentary, not source-based; the source-based parts (patent proxy, n=33) are evidenced. Adjudicated direction 'mixed' (briefs line 37) matches the stage-split evidence.*

---

## S32 — D’Amico E. et al. (2025) — Journal of Technology Transfer (AJG 3)

DOI: 10.1007/s10961-025-10217-7 · status: final · PDF: `DAmico_2025_s10961-025-10217-7.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | UK |
| sample | 14,143 UK firms, 2004-2020 |
| method | panel econometrics |
| ai_measure | archival: Beauhurst-identified AI technology/product use, matched to Business Structure Database + UK Innovation Survey (2004-2020, biennial) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | innovation performance (knowledge spillover of innovation) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | complementarity with own R&D investment (AI pays only if it complements internal R&D); AI SUBSTITUTES knowledge collaboration with certain external partners |
| key_finding | AI adoption boosts innovation only when paired with the firms own R&D investment - and partly replaces external knowledge collaboration. |
| *not printed (coding data only)* | |
| theoretical_lens | knowledge spillover / innovation economics |
| industry | cross-industry |
| quality_notes | Large archival panel; innovation outcome (performance-near per criteria) \| SAMPLE-CHECK OK: panel/conditional confirmed (R&D complementarity condition) |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, sample, outcome_construct, theoretical_lens** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > Using data from 14,143 firms in the UK between 2004 and 2020, we explore how AI adoption impacts knowledge spillover of innovation.
   Ctrl+F: „Using data from 14,143 firms in the UK“
   → Names the 14,143-firm UK sample 2004-2020 and frames the outcome as knowledge spillover of innovation, the coded lens and performance construct.

2. **country_region, sample, method, ai_measure** — PDF p. 3, 1 Introduction — ✓ verified, 100% word sequence
   > Using novel data on 14,143 firms with 24,017 firm-year observations over 2004-2020 in the United Kingdom from six Business Structure Databases (BSD) and UK Innovation Surveys (UKIS) matched to the Beauhurst database
   Ctrl+F: „Using novel data on 14,143 firms with 24,017“
   → Firm-year panel structure and the BSD/UKIS/Beauhurst data sources coded in sample, country_region and ai_measure.

3. **method** — PDF p. 10, 3.3 Method — ✓ verified, 100% word sequence
   > We use Tobit regression model (Audretsch et al., 2023; Laursen & Salter, 2006 ; Negassi, 2004) to estimate a knowledge production function as our dependent variable which is dou -ble censored,
   Ctrl+F: „We use Tobit regression model (Audretsch et al.,“
   → Econometric estimation (Tobit with fixed effects, plus IV-Tobit robustness) on the firm-year panel — the coded 'panel econometrics'.

4. **ai_measure** — PDF p. 8, 3.1 Data matching and sample description — ✓ verified, 100% word sequence
   > we combine the Busi -ness Structure database (known as the BSD) and the UK Innovation Survey (UKIS) over 2004-2020, and the Beauhurst database for every second year available.
   Ctrl+F: „ness Structure database (known as the BSD) and“
   → Backs the 'biennial' Beauhurst matching in the coded ai_measure.

5. **ai_measure** — PDF p. 8, 3.1 Data matching and sample description — ✓ verified, 100% word sequence
   > We use Beauhurst data to identify technologies and products where use of artificial intelligence including gen -erative AI was a commonplace.
   Ctrl+F: „data to identify technologies and products where use“
   → Backs 'Beauhurst-identified AI technology/product use' in ai_measure.

6. **ai_measure** — PDF p. 9, 3.2.2 Explanatory variables — ✓ verified, 100% word sequence
   > Our key explanatory variable is adoption of artificial intelligence
   Ctrl+F: „Our key explanatory variable is adoption of artificial“
   → Operationalization of the archival AI adoption measure.

7. **outcome_construct, performance_measure** — PDF p. 9, 3.2.1 Dependent variables — ✓ verified, 100% word sequence
   > Our dependent variable is radical innovation which is calculated as share of total sales over the last three years from goods and services that are new to the market.
   Ctrl+F: „Our dependent variable is radical innovation which is“
   → The outcome is innovation performance (innovation sales share), i.e. a performance construct — no competitive-advantage construct is measured.

8. **effect_direction, conditions, key_finding** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > firms adopting AI can enhance their innovation performance if it complements firm's own investment in R&D. AI adoption can substitute knowledge col -laboration with certain external partners.
   Ctrl+F: „firms adopting AI can enhance their innovation performance“
   → The paper's own central result: the AI payoff is conditional on complementing internal R&D, and AI substitutes some external knowledge collaboration — matching key_finding and both coded conditions.

9. **effect_direction** — PDF p. 13, 4.1 Main results — ✓ verified, 100% word sequence
   > Our H4 which states that AI positively moderate the effect of knowledge collaboration with various types of external partners and firm innovation is partly supported.
   Ctrl+F: „Our H4 which states that AI positively moderate“
   → AI's role is tested as a moderator of collaboration effects, consistent with the conditional coding.

10. **effect_direction, conditions** — PDF p. 13, 4.1 Main results — ✓ verified, 100% word sequence
   > switches from positive (spec. 2, Table 3) to negative effect (spec. 6, Table 3). This means that by adopting AI, a firm may substitute information that it receives within its upstream supply chain
   Ctrl+F: „(spec. 2, Table 3) to negative effect (spec.“
   → Direct evidence for the coded condition that AI substitutes knowledge collaboration with certain external partners (suppliers).

11. **effect_direction, conditions** — PDF p. 16, 4.2.2 Second-stage estimation — ✓ verified, 100% word sequence
   > Collaboration with customers and suppliers adds more to product innovation in firms that adopted advanced AI technologies than in firms that do not adopt AI, supporting H4.
   Ctrl+F: „Collaboration with customers and suppliers adds more to“
   → IV second stage confirms the AI effect operates through complementarity with specific collaborations, not as an unconditional main effect — backing 'conditional'.

12. **industry** — PDF p. 8, 3.1 Data matching and sample description — ✓ verified, 100% word sequence
   > Most of the firms in our sample are from the other manufacturing sector, wholesale and retail and professional and scientific services.
   Ctrl+F: „our sample are from the other manufacturing sector,“
   → Sample spans manufacturing, retail and services sectors, backing the cross-industry coding.

13. **quality_notes** — PDF p. 20, 5.3 Limitations and future research — ✓ verified, 100% word sequence
   > Our study has an important limitation related to the measure of AI adoption. We developed a binary variable with a sectoral focus and adopted a couple of filtering criteria.
   Ctrl+F: „Our study has an important limitation related to“
   → Authors' own limitation on the archival sector-based AI measure, relevant to the quality note on the archival panel design.

*Row check OK: ca_measure empty is correct: 'competitive advantage' appears only as rhetoric in the literature review and managerial implications, no CA construct is measured. quality_notes is largely coder/verification commentary ('Large archival panel', 'SAMPLE-CHECK OK'); the innovation-outcome (performance-near) part is evidenced by the dependent-variable quote and the AI-measure limitation is the authors' own. Conditional direction is settled per adjudication briefs (sample check: 'panel / performance / conditional OK'); baseline AI main effect is insignificant in specs without interactions (Table 3 spec 1: -0.005 n.s.; Table 4 spec 1: -0.004 n.s.), consistent with 'conditional'.*

---

## S33 — Feng L. et al. (2025) — Quarterly Review of Economics and Finance (AJG 2)

DOI: 10.1016/j.qref.2025.102042 · status: final · PDF: `Feng_2025_j-qref-2025-102042.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 4,004 Chinese A-share firms, 2011-2023; procurement-based AI adoption index + patents + supply-chain data |
| method | panel econometrics |
| ai_measure | procurement index (AI adoption from procurement records) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | innovation output and innovation efficiency |
| ca_measure | — |
| effect_direction | positive |
| conditions | stronger for large incumbents and growth-stage firms; executives with IT backgrounds amplify; highly innovative firms diversify supply chains to reduce resource risk |
| key_finding | AI adoption raises innovation output and efficiency, most where firm maturity, scale and IT-savvy leadership provide absorptive conditions. |
| *not printed (coding data only)* | |
| theoretical_lens | knowledge orchestration / data assetization (dual-channel model) |
| industry | cross-industry (listed firms) |
| quality_notes | Novel procurement-based AI measure; archival panel |
| coding_status | final |

### Evidence

1. **country_region, ai_measure** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > To construct this variable, we leverage the SSIRD database, which contains over 1.47 million tendering events from Chinese listed firms.
   Ctrl+F: „variable, we leverage the SSIRD database, which contains“
   → The AI measure is built from Chinese firms' procurement/tender records - the coded procurement index.

2. **country_region, sample, method, industry** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The empirical analysis draws on a comprehensive panel dataset spanning 2011-2023, covering 4004 publicly listed firms across 266 Chinese cities, resulting in 27,978 firm-year observations.
   Ctrl+F: „The empirical analysis draws on a comprehensive panel“
   → Panel of 4004 Chinese listed firms with no sector restriction, backing sample, China, and the cross-industry (listed firms) coding.

3. **sample, ai_measure, outcome_construct, performance_measure, effect_direction, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using a procurement-based AI adoption index, patent records, and supply-chain data from 4004 A-share firms over 2011-2023, we find that greater AI adoption significantly increases the output and efficiency of firms' innovation.
   Ctrl+F: „adoption index, patent records, and supply‑chain data from“
   → Abstract states sample (4004 A-share firms 2011-2023), the procurement-based AI index, and the positive main effect on innovation output and efficiency - the coded key finding.

4. **method** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > To empirically examine the relationship between AI adoption and corporate innovation, we employ a two-way fixed effects model to mitigate omitted variable bias.
   Ctrl+F: „To empirically examine the relationship between AI adoption“
   → Two-way fixed-effects estimation on the firm-year panel - the coded 'panel econometrics'.

5. **ai_measure** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Each tender's project title was scanned against this dictionary. Events matching any keyword were classified as AI-related (coded as 1) and aggregated at the firm-year level.
   Ctrl+F: „scanned against this dictionary. Events matching any keyword“
   → Operationalization of AI adoption from procurement records via an AI keyword dictionary.

6. **ai_measure, quality_notes** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > Procurement-based AI measures may undercount in-house development, and patent-based quality metrics could be complemented with commercialization data.
   Ctrl+F: „undercount in-house development, and patent-based quality metrics“
   → Authors' own caveat on the novel procurement-based AI measure noted in quality_notes.

7. **outcome_construct, performance_measure** — p. 3 (PDF p. 3) — ✓ verified, 83% word sequence
   > Corporate innovation is captured through two dimensions: innovation output and innovation efficiency.
   Ctrl+F: „Corporate innovation is captured through two dimensions:“
   → The two coded performance measures; a performance construct, no CA construct is measured.

8. **effect_direction** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > A 1 % increase in AI adoption intensity raises patent applications by 0.145 % (β = 0.145, p < 0.01) after accounting for firm characteristics and fixed effects.
   Ctrl+F: „A 1 % increase in AI adoption intensity raises“
   → Significant positive baseline main effect on innovation output - backing effect_direction = positive.

9. **effect_direction** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > the coefficient (β = 0.005, p < 0.01) indicates that a 1 % increase in AI adoption raises innovation efficiency by 0.005 units
   Ctrl+F: „that a 1 % increase in AI adoption raises“
   → Significant positive baseline effect on the second outcome, innovation efficiency.

10. **conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Heterogeneity analysis reveals that large incumbents and growth-stage firms leverage AI most effectively for innovation outputs and efficiency.
   Ctrl+F: „incumbents and growth‑stage firms leverage AI most effectively“
   → Backs the coded condition 'stronger for large incumbents and growth-stage firms'.

11. **conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Further analysis shows that AI-driven innovation is amplified in firms with executives who have information technology backgrounds, and that highly innovative firms diversify their supply chain to reduce resource risk.
   Ctrl+F: „analysis shows that AI-driven innovation is amplified in“
   → Backs the coded conditions on IT-background executives and supply-chain diversification.

12. **conditions** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > For large firms (Columns 2 and 4), AI adoption significantly enhances both innovation output (β = 0.154, p < 0.01) and efficiency (β = 0.006, p < 0.01)
   Ctrl+F: „For large firms (Columns 2 and 4), AI“
   → Size heterogeneity: the effect concentrates in large firms (small firms are insignificant), backing the 'large incumbents' condition.

13. **conditions** — p. 10 (PDF p. 10) — ✓ verified, 83% word sequence
   > The presence of senior executives with IT backgrounds significantly amplifies AI's impact on innovation, though effects vary across performance dimensions (Table 9).
   Ctrl+F: „The presence of senior executives with IT backgrounds“
   → Moderator evidence for the coded 'executives with IT backgrounds amplify' condition.

14. **conditions** — p. 11 (PDF p. 11) — ✓ verified, 100% word sequence
   > Table 11 shows that AI-driven innovation significantly lowers supply chain concentration, reducing operational risks.
   Ctrl+F: „Table 11 shows that AI-driven innovation significantly lowers“
   → Backs the coded condition that highly innovative firms diversify supply chains to reduce resource risk.

15. **conditions, key_finding** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > The benefits vary across contexts: large, expanding firms capture more gains, whereas IT-savvy leaders enhance patent output more than others, owing to superior absorptive capacity.
   Ctrl+F: „vary across contexts: large, expanding firms capture more“
   → Conclusion restates the coded key finding that firm maturity, scale and IT-savvy leadership provide the absorptive conditions for AI's payoff.

16. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 68% word sequence
   > We propose a dual-channel model in which AI enhances knowledge creation and reuse (knowledge orchestration) and transforms data into actionable environmental assets (data assetization).
   Ctrl+F: „dual‑channel model in which AI enhances knowledge creation“
   → Names the coded lens: knowledge orchestration / data assetization dual-channel model.

*Row check OK: ca_measure empty is correct: 'competitive advantage' appears only as rhetoric in the IV discussion and conclusion, no CA construct is measured. quality_notes ('Novel procurement-based AI measure; archival panel') is coder shorthand but source-anchored via the measure-construction and limitation quotes. Note: the paper also frames AI as a general-purpose technology (Sec. 2.1) alongside the coded dual-channel lens - complementary framing, not a contradiction. Direction 'positive' with heterogeneity-as-conditions matches the case-law main-effect rule (baseline betas 0.145***/0.005***).*

---

## S34 — Fontanelli L. et al. (2025) — Journal of Economic Behavior and Organization (AJG 3)

DOI: 10.1016/j.jebo.2025.107336 · status: final · PDF: `Fontanelli_2025_j-jebo-2025-107336.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | France |
| sample | French ICT survey 2019, firm-level; balancing/matching robustness |
| method | panel econometrics |
| ai_measure | survey (predictive AI use; buyers vs in-house developers) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | VOLATILITY of productivity growth (not the level) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | AI BUYERS: higher volatility; in-house DEVELOPERS: none; complementary human capital (share of ICT engineers/technicians) mitigates the buyer effect |
| key_finding | Off-the-shelf AI raises the riskiness of productivity outcomes; developing in-house or holding complementary ICT human capital neutralizes it. |
| *not printed (coding data only)* | |
| theoretical_lens | none explicit (productivity dynamics) |
| industry | cross-industry |
| quality_notes | Unusual outcome (volatility) - valuable nuance for synthesis |
| coding_status | final |

### Evidence

1. **country_region, sample, outcome_construct, effect_direction** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using firm-level data from the 2019 French ICT survey, we provide robust evidence that AI use is associated with increased volatility.
   Ctrl+F: „the 2019 French ICT survey, we provide robust“
   → Abstract names the 2019 French ICT survey firm-level sample and the baseline AI-volatility association that the coded conditions then qualify.

2. **country_region, sample** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > In this work we make use of a representative ICT survey distributed to about 9000 French firms with 10 or more employees in 2019.
   Ctrl+F: „In this work we make use of a“
   → Data section confirms the French ICT survey 2019 firm-level sample.

3. **sample, method** — p. 2 (PDF p. 2) — ✓ verified, 89% word sequence
   > we account for differences in firm characteristics by employing a Coarsened Exact Matching (CEM) approach, which balances AI users and non-users ex-ante based on characteristics such as size, age, productivity, industry, and digitalization measures
   Ctrl+F: „Exact Matching (CEM) approach, which balances AI users“
   → The balancing/matching robustness noted in the coded sample and part of the econometric identification strategy.

4. **sample, industry** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > They operate across a diverse range of 61 sectors ranging from manufacturing of food products (#10) to services like the repair of computers (#95), reflecting a broad industrial coverage.
   Ctrl+F: „They operate across a diverse range of 61“
   → Backs the cross-industry coding; analysis sample is 7915 firms from the survey.

5. **method** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > we regress the (log) volatility computed over the time span 2014-2019 on an AI adoption indicator while controlling for other ICT technologies adoption, firm characteristics, and sector (2-digit) and region fixed effects
   Ctrl+F: „computed over the time span 2014–2019 on an“
   → Regression design on archival firm data (volatility built from 2007-2019 balance-sheet panels) with fixed effects - the coded panel econometrics.

6. **method, quality_notes** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > While not definitive and still largely correlational, the multiple estimation strategies and robustness checks employed in this work provide reassurance about the robustness of our findings.
   Ctrl+F: „and still largely correlational, the multiple estimation strategies“
   → Authors' own caveat on the correlational nature of the evidence, source-based support for the quality note.

7. **ai_measure** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Firms are asked the following question about AI use: 'In 2018, did your company make use of software and/or equipment incorporating artificial intelligence technologies?'
   Ctrl+F: „use: “In 2018, did your company make use“
   → The survey-based predictive AI use measure coded in ai_measure.

8. **ai_measure, conditions** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Crucially, the survey distinguishes between two types of users: AI buyers, who use externally purchased AI technologies, and AI developers, who rely on AI systems developed in-house.
   Ctrl+F: „of users: AI buyers, who use externally purchased“
   → The buyers-vs-in-house-developers split coded in ai_measure and used for the conditional finding.

9. **outcome_construct, performance_measure** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > The dependent variable in all the empirical investigations below is the volatility of the productivity growth rates of the French firms in our sample.
   Ctrl+F: „The dependent variable in all the empirical investigations“
   → The outcome is the volatility of productivity growth, not the level - as coded in performance_measure; no CA construct is measured.

10. **performance_measure, theoretical_lens, quality_notes** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > our work is the first to shift attention away from expected productivity gains and focus on how the integration of AI systems alters the variability in productivity growth dynamics within firms
   Ctrl+F: „to shift attention away from expected productivity gains“
   → The paper positions itself in productivity dynamics, not a named strategy theory, and confirms the unusual volatility outcome flagged in quality_notes.

11. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Our results show that heightened volatility is concentrated among AI buyers, whereas firms that develop AI internally experience no such association.
   Ctrl+F: „that develop AI internally experience no such“
   → The effect exists only for AI buyers and vanishes for in-house developers - the core of the coded 'conditional' direction and the buyer/developer condition.

12. **effect_direction** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > This difference in volatilities, estimated to be around 10%, holds true when we address potential measurement issues with our dependent variable but disappears in a placebo test
   Ctrl+F: „in volatilities, estimated to be around 10 %, holds“
   → Magnitude of the average AI-volatility association that the sourcing split then shows to be concentrated among buyers only.

13. **effect_direction, conditions, key_finding** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > In particular, we find that firms that develop AI systems in-house do not experience this volatility surge, unlike firms that procure AI from external providers.
   Ctrl+F: „in-house do not experience this volatility surge, unlike“
   → Conclusion restates the coded key finding: off-the-shelf AI raises riskiness, in-house development neutralizes it.

14. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Finally, we find that the AI-volatility link among 'AI buyers' is mitigated in firms with a higher share of ICT engineers and technicians, suggesting that AI's successful integration requires complementary human capital.
   Ctrl+F: „that the AI-volatility link among “AI buyers” is“
   → Backs the coded condition that complementary ICT human capital mitigates the buyer effect and the key finding's neutralization clause.

15. **conditions** — p. 14 (PDF p. 14) — ✓ verified, 67% word sequence
   > the interaction term between AI buyers and ICT share is negative, significant and large enough to indicate that firms with a higher intensity of ICT workers experience a substantially weaker AI-volatility relation
   Ctrl+F: „the interaction term between AI buyers and ICT“
   → Regression evidence for the coded mitigating condition (share of ICT engineers/technicians).

*Row check OK: ca_measure empty is correct: no competitive-advantage construct appears anywhere in the paper. quality_notes ('Unusual outcome (volatility) - valuable nuance') is coder commentary but anchored by the paper's own first-to-study-volatility claim (p. 2 quote) and correlational caveat (p. 14). On direction: the paper does report a significant average AI-volatility association (~6-10%), but volatility is not a signed performance level, and the sourcing split shows the association exists only for AI buyers (developers null) and is neutralized by ICT human capital - consistent with the final 'conditional' coding; no tension flagged.*

---

## S35 — Guo Y. et al. (2025) — International Marketing Review (AJG 3)

DOI: 10.1108/IMR-10-2024-0418 · status: final · PDF: `Guo_2025_IMR-10-2024-0418.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 322 SMEs using cross-border platforms |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption coupled with strategic agility) |
| *Table A.2 columns* | |
| outcome_construct | competitive_advantage |
| performance_measure | — |
| ca_measure | international advantage: product innovation + brand upgrading (GVC position, survey scales) |
| effect_direction | positive |
| conditions | international marketing capabilities (mediator); platform embeddedness DEPTH (inverted U on product innovation) and BREADTH (inverted U on brand upgrading) - medium embeddedness optimal |
| key_finding | AI adoption coupled with strategic agility upgrades SMEs global value-chain position through marketing capabilities - but only at moderate platform embeddedness (inverted-U). |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities hierarchy + international marketing capabilities |
| industry | cross-industry (emerging-market SMEs) |
| quality_notes | Perceptual; non-linear boundary conditions |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 1250 (PDF p. 1) — ✓ verified, 100% word sequence
   > A quantitative approach was employed to analyse data from 322 small and medium-sized enterprises in China utilizing cross-border platforms. The research model was tested using structural equation modelling
   Ctrl+F: „A quantitative approach was employed to analyse data“
   → Survey of 322 Chinese SMEs on cross-border platforms analysed with SEM backs method, sample and country codes.

2. **sample** — p. 1262 (PDF p. 13) — ✓ verified, 100% word sequence
   > Ultimately, a total of 949 questionnaires were collected, yielding a 14.38% response rate, with 322 valid responses, representing a 33.94% effective response rate.
   Ctrl+F: „Ultimately, a total of 949 questionnaires were collected,“
   → Confirms the final n = 322 valid responses.

3. **sample, industry** — p. 1262 (PDF p. 13) — ✓ verified, 100% word sequence
   > In the contract, we clearly stated our data collection requirements, including the definition of SMEs, the random sampling of SMEs from different industrial sectors, and the inclusion of multinational companies, foreign trade firms
   Ctrl+F: „data collection requirements, including the definition of SMEs,“
   → Sampling deliberately spans different industrial sectors, backing the cross-industry coding.

4. **ai_measure** — p. 1263 (PDF p. 14) — ✓ verified, 100% word sequence
   > The coupling of AI adoption and strategic agility is conceptualized and developed as a formative-formative type of second-order construct
   Ctrl+F: „The coupling of AI adoption and strategic agility“
   → The AI measure is a survey second-order construct coupling AI adoption with strategic agility, exactly as coded.

5. **ai_measure** — p. 1264 (PDF p. 15) — ✓ verified, 100% word sequence
   > we used a four-item scale to measure AI adoption on the platform, asking ESME managers how AI helps design products and services, manage and optimize supply chains and reduce shipping costs and transit time
   Ctrl+F: „we used a four-item scale to measure AI“
   → Details the survey scale used for the AI adoption component (Hossain et al. 2022 items).

6. **outcome_construct, ca_measure, theoretical_lens** — p. 1250 (PDF p. 1) — ✓ verified, 100% word sequence
   > how artificial intelligence (AI) adoption and strategic agility coupling shape ESMEs' GVC positioning through the lens of international marketing capabilities (IMCs), differentiating international advantage into two dimensions: product innovation and brand upgrading
   Ctrl+F: „strategic agility coupling shape ESMEs’ GVC positioning through“
   → Outcome is framed and measured as international (competitive) advantage in two dimensions, with IMCs as the theoretical lens.

7. **outcome_construct, ca_measure** — p. 1267 (PDF p. 18) — ✓ verified, 100% word sequence
   > PIA1: Was of higher quality than competing products
   Ctrl+F: „PIA1: Was of higher quality than competing products“
   → Product innovation advantage items are competitor-comparative, evidencing a distinct measured CA construct (satisfies the CA decision rule).

8. **outcome_construct, ca_measure** — p. 1264 (PDF p. 15) — ✓ verified, 100% word sequence
   > was assessed using a four-item scale to evaluate the brand position of an ESMEs' offering in the export market, focusing on brand image, awareness, 'share of mind' and personality, relative to its major competitor
   Ctrl+F: „was assessed using a four-item scale to evaluate“
   → Brand upgrading advantage is a validated survey scale measured relative to major competitors, backing ca_measure and the competitive_advantage coding.

9. **effect_direction** — p. 1268 (PDF p. 19) — ✓ verified, 100% word sequence
   > Our test showed that the coupling of AI adoption and strategic agility exerted significant positive effects on both product innovation advantage (H1a: β 5 0.519, p 5 < 0.001) and brand upgrading advantage
   Ctrl+F: „Our test showed that the coupling of AI“
   → Significant positive direct main effects on both advantage dimensions back effect_direction = positive ('5' is the extraction's rendering of '=' on the printed page).

10. **effect_direction, conditions, key_finding** — p. 1250 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study demonstrates that the coupling of AI adoption and strategic agility positively influences IMCs, product innovation and brand upgrading, while IMCs serve as a mediating mechanism.
   Ctrl+F: „The study demonstrates that the coupling of AI“
   → The paper's own summary of its central result: positive effects plus IMCs as mediating mechanism.

11. **conditions** — p. 1268 (PDF p. 19) — ✓ verified, 100% word sequence
   > The results indicate that an ESME's IMCs mediate the relationship between the coupling of AI adoption and strategic agility on product innovation advantage
   Ctrl+F: „that an ESME’s IMCs mediate the relationship between“
   → Bootstrap mediation evidence for the coded IMC mediator condition.

12. **conditions, key_finding** — p. 1274 (PDF p. 25) — ✓ verified, 100% word sequence
   > embedding breadth improves the effect of coupling AI with strategic agility on brand upgrading up to an optimal point (at a medium level)
   Ctrl+F: „embedding breadth improves the effect of coupling AI“
   → Backs the coded BREADTH inverted-U on brand upgrading with medium embeddedness optimal.

13. **conditions, key_finding** — p. 1274 (PDF p. 25) — ✓ verified, 100% word sequence
   > We also find that embedding depth has an inverted U-shaped moderating effect on the relationship between the coupling of AI with strategic agility and product innovation advantage.
   Ctrl+F: „effect on the relationship between the coupling of“
   → Backs the coded DEPTH inverted-U on product innovation.

14. **theoretical_lens** — p. 1252 (PDF p. 3) — ✓ verified, 100% word sequence
   > we aim to draw on the hierarchy view of dynamic capability (Zollo and Winter, 2002; Winter, 2003), investigating how cross-border platforms' AI adoption, coupled with higher-order dynamic capabilities, systematically alter ESMEs' lower-level IMCs
   Ctrl+F: „we aim to draw on the hierarchy view“
   → Backs the coded lens 'dynamic capabilities hierarchy + international marketing capabilities'.

15. **industry** — p. 1262 (PDF p. 13) — ✓ verified, 100% word sequence
   > Table 1 summarizes the sample demographics, showing that a significant majority of the respondents worked in private companies (74%) and most belonged to manufacturing industries (64%)
   Ctrl+F: „Table 1 summarizes the sample demographics, showing that“
   → Shows the industry composition (manufacturing majority within a multi-industry sample; Table 1 lists nine sectors), consistent with cross-industry coding.

16. **quality_notes** — p. 1277 (PDF p. 28) — ✓ verified, 100% word sequence
   > Finally, self-reported data from SME managers regarding platform AI adoption and agility perceptions risks introducing bias.
   Ctrl+F: „Finally, self-reported data from SME managers regarding platform“
   → Authors' own limitation backs the 'Perceptual' quality note; 'non-linear boundary conditions' is evidenced by the inverted-U quotes above.

*Row check OK: performance_measure empty is correct: the only outcomes are the two advantage scales (PIA/BUA); international sales and profit enter solely as control variables. Coded conditions correctly list only the two SUPPORTED inverted-U moderations (H5b breadth on brand upgrading, H6a depth on product innovation); H5a and H6b were not supported. Not in adjudication_briefs.md.*

---

## S36 — Huang C.K. et al. (2025) — Managerial and Decision Economics (AJG 2)

DOI: 10.1002/mde.4486 · status: final · PDF: `Huang_2025_mde-4486.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | S&P 500 firms: 50 AI adopters (23 first movers, 27 followers) identified via 97 manually screened AI-implementation news items + non-adopter controls; Compustat 2010-2017, baseline 2017 |
| method | panel econometrics |
| ai_measure | news announcements (manually verified AI implementation) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | financial ratios (Compustat), productivity, market value (Tobin q) |
| ca_measure | — |
| effect_direction | mixed |
| conditions | indicator-specific: financial performance + market value positive, productivity insignificant; first movers show partly negative/insignificant effects (no uniform first-mover advantage) |
| key_finding | AI implementation lifts financial performance and market value, but first movers and top performers do not benefit uniformly across all indicators. |
| *not printed (coding data only)* | |
| theoretical_lens | business value of IT |
| industry | cross-industry |
| quality_notes | Small adopter sample (n=50); author affiliation Taiwan but sample = US S&P 500 |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 1860 (PDF p. 5) — ✓ verified, 71% word sequence
   > the sample framework for this study is based on the S&P 500 Index list. The S&P500 Index is the US stock market index based on the market capitalization of 500 large companies
   Ctrl+F: „the sample framework for this study is based“
   → Confirms the sample is drawn from S&P 500 firms and the country is the USA.

2. **sample, ai_measure** — p. 1860 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 28% word sequence
   > Finally, we collected 249 news stories, but we filtered out 152 news stories because they were about IT-related companies. The remainder (97 news) were included in our experiment.
   Ctrl+F: „Finally, we collected 249 news stories, but we“
   → Backs the coded 97 manually screened AI-implementation news items used to identify adopters.

3. **sample, industry** — p. 1861 (PDF p. 6) — ✓ verified, 100% word sequence
   > We collected a total of 300 samples without IT companies; 50 of the companies announced AI news, and 250 did not
   Ctrl+F: „collected a total of 300 samples without IT“
   → Backs the coded 50 AI adopters plus non-adopter controls and the exclusion of IT firms from the cross-industry sample.

4. **sample** — p. 1861 (PDF p. 6) — ✓ verified, 100% word sequence
   > Therefore, the number of first movers is 23 and that of second movers is 27.
   Ctrl+F: „movers is 23 and that of second movers“
   → Backs the coded split of adopters into 23 first movers and 27 followers.

5. **sample** — p. 1860 (PDF p. 5) — ✓ verified, 100% word sequence
   > The data we collected in this study are from 2010 to 2017; however, the baseline for performance analysis is only available in 2017.
   Ctrl+F: „data we collected in this study are from“
   → Backs the coded data window 2010-2017 with baseline year 2017.

6. **sample, performance_measure** — p. 1860 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 37% word sequence
   > In this study, two programs were used to collect data. We confirmed the list of sample companies, collecting data through Compustat and then selected some ratios to evaluate their performance.
   Ctrl+F: „In this study, two programs were used to“
   → Confirms Compustat as the financial data source and financial ratios as performance measures.

7. **method, performance_measure** — p. 1861 (PDF p. 6) — ✓ verified, 100% word sequence
   > Ordinary least squares (OLS) regression method was used to analyze the impact of AI on performance.
   Ctrl+F: „Ordinary least squares (OLS) regression method was used“
   → Identifies OLS regression on archival financial data as the strategy generating the AI-outcome evidence (econometric analysis of Compustat data).

8. **ai_measure** — p. 1860 (PDF p. 5) — ✓ verified, 100% word sequence
   > in order to ensure that companies with news mentioning AI were definitely implementing AI, we carefully read the news content
   Ctrl+F: „in order to ensure that companies with news“
   → Shows the AI measure is news announcements manually verified for actual AI implementation.

9. **outcome_construct, performance_measure** — p. 1856 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study provides a significant contribution by empirically examining AI impact on firm-level performance through three key indicators: financial performance, productivity, and market value.
   Ctrl+F: „This study provides a significant contribution by empirically“
   → The outcome is firm performance via financial ratios, productivity, and market value; no distinct competitive-advantage construct is measured.

10. **effect_direction, conditions** — p. 1856 (PDF p. 1) — ✓ verified, 100% word sequence
   > this research reveals that while AI adoption enhances financial performance and market value, the advantages for AI first movers and better performers are not uniformly positive across all indicators.
   Ctrl+F: „this research reveals that while AI adoption enhances“
   → Backs the mixed direction (positive on financial performance and market value, not uniform elsewhere) and the indicator-specific conditions.

11. **effect_direction, conditions** — p. 1864 (PDF p. 9) — ✓ verified, 100% word sequence
   > Although productivity measurements are not significant, they still have a positive impact on value added and output. Therefore, we still claim that Hypothesis 1b can be partially supported.
   Ctrl+F: „significant, they still have a positive impact on“
   → Backs the coded condition that the productivity component is insignificant, part of the mixed component split.

12. **effect_direction, conditions** — p. 1864 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 16% word sequence
   > In short, the pioneer companies implementing AI showed no significant positive impact on financial performance, and almost half of the financial indicators indicate a negative impact on performance for first movers.
   Ctrl+F: „implementing AI showed no significant positive impact on“
   → Backs the coded condition that first movers show partly negative/insignificant effects (no uniform first-mover advantage).

13. **effect_direction, key_finding** — p. 1869 (PDF p. 14) — ⚠ not machine-confirmed on page — open the page, 53% word sequence
   > Our findings reveal that while AI adoption generally enhances financial performance and market value, the anticipated benefits for first movers and better performers are not uniformly realized across all indicators.
   Ctrl+F: „Our findings reveal that while AI adoption generally“
   → The paper's own conclusion statement of its central result, matching the coded key finding and mixed direction.

14. **theoretical_lens** — p. 1856 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 16% word sequence
   > Managers and operators have long evaluated the value of IT and hoped that their investments in IT could generate authentic benefit; we call this idea the business value of IT (BVIT).
   Ctrl+F: „the value of IT and hoped that their“
   → Names business value of IT (BVIT) as the study's guiding framework, matching the coded theoretical lens.

15. **industry** — p. 1861 (PDF p. 6) — ✓ verified, 94% word sequence
   > According to the Standard Industrial Classification Code (SIC), we divided the S&P 500 companies into six industries
   Ctrl+F: „Code (SIC), we divided the S&P 500 companies“
   → Shows the sample spans six SIC industries, backing the cross-industry coding.

16. **quality_notes** — p. 1856 (PDF p. 1) — ✓ verified, 100% word sequence
   > Department of Business Administration, National Chung Cheng University, Chiayi, Taiwan
   Ctrl+F: „Department of Business Administration, National Chung Cheng University,“
   → Backs the quality note that author affiliation is Taiwan while the sample is US S&P 500 firms.

**⚠ ROW CHECK:** (1) ca_measure empty is correct: competitive advantage appears only as framing (p.14 'This survey confirms that AI is beneficial and provides a competitive advantage to companies') with no measured CA construct — adjudicated as performance, no tension. (2) quality_notes 'small adopter sample (n=50)' is coder commentary; n=50 itself is documented (p.5 quote). (3) Author may want to look at method label 'panel econometrics': the paper runs OLS on a single 2017 baseline cross-section of Compustat data (p.5: 'the baseline for performance analysis is only available in 2017'), not a panel estimation — the archival-econometrics bucket fits, the literal 'panel' does not.

---

## S37 — Kumar A. et al. (2025) — Journal of Business Research (AJG 3)

DOI: 10.1016/j.jbusres.2024.115160 · status: final · PDF: `Kumar_2025_j-jbusres-2024-115160.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | multi-country (7 countries) |
| sample | Study 1: in-depth interviews; Study 2: SEM on 277 B2B managers across USA, UK, Canada, India, Australia, Malaysia, Japan |
| method | survey-SEM |
| ai_measure | survey construct (GenAI adoption) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | perceived firm performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | ethical leadership (moderator of GenAI adoption -> performance); adoption reasons for/against (uniqueness, information completeness, convenience, deceptiveness) |
| key_finding | GenAI adoption boosts perceived firm performance, more strongly under ethical leadership. |
| *not printed (coding data only)* | |
| theoretical_lens | behavioral reasoning theory |
| industry | cross-industry (B2B) |
| quality_notes | Two-study design: Study 1 qualitative (adoption reasons -> hypotheses, own findings Fig. 1), Study 2 SEM n=277 tests AI->performance; perceptual, multi-country |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > A total of 277 responses was collected from respondents in the USA, the UK, Canada, India, Australia, Malaysia, and Japan to test the proposed model using structural equation modeling.
   Ctrl+F: „A total of 277 responses was collected from“
   → Backs method survey-SEM, the n=277 manager sample, and the seven-country coverage.

2. **country_region, sample** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Data were collected from participants across seven countries, including the USA, the UK, Canada, India, Australia, Malaysia, and Japan.
   Ctrl+F: „Data were collected from participants across seven countries,“
   → Backs the coded multi-country (7 countries) value with the exact country list.

3. **sample, quality_notes** — p. 3 (PDF p. 3) — ⚠ not machine-confirmed on page — open the page, 17% word sequence
   > we conducted a small number of additional interviews, yielding a final sample of 27 participants (aged 18-51)
   Ctrl+F: „a small number of additional interviews, yielding a“
   → Documents the Study 1 in-depth interview sample noted in the sample and quality_notes fields.

4. **sample** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > Of 301 potential responses, 277 successfully passed the attention and screening questions.
   Ctrl+F: „Of 301 potential responses, 277 successfully“
   → Backs the coded Study 2 sample size of 277 B2B managers.

5. **method, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Study 1 undertakes a series of in-depth interviews, yielding a set of hypotheses that are tested in Study 2.
   Ctrl+F: „interviews, yielding a set of hypotheses that are“
   → Shows the interviews only develop hypotheses; the AI-performance evidence comes from the Study 2 SEM, backing the adjudicated method survey-SEM and the two-study quality note.

6. **ai_measure, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study examines key reasons (for and against) that influence business-to-business (B2B) managers' intention to adopt generative artificial intelligence (GenAI).
   Ctrl+F: „This study examines key reasons (for and against)“
   → Backs the B2B setting (cross-industry manager sample) and GenAI adoption as the AI construct.

7. **ai_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > I intend to use Generative AI in future
   Ctrl+F: „I intend to use Generative AI in future“
   → Appendix A item ADP1 shows GenAI adoption is measured as a survey construct.

8. **outcome_construct, performance_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > Using Generative AI helps the firm to earn better business profit
   Ctrl+F: „Using Generative AI helps the firm to earn“
   → Appendix A item FP1 shows firm performance is a perceived survey scale, backing outcome_construct performance.

9. **outcome_construct, effect_direction** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > Moreover, GenAI adoption (β = 0.769***) is positively associated with firm performance in B2B firms, supporting H6.
   Ctrl+F: „Moreover, GenAI adoption (β = 0.769***) is positively associated with“
   → Clear positive main effect of GenAI adoption on firm performance, backing effect_direction positive.

10. **performance_measure, quality_notes** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > while we explored the effect of GenAI adoption on firm performance, we only considered this from a perceptual and intentional perspective in terms of measurement
   Ctrl+F: „the effect of GenAI adoption on firm performance,“
   → Authors' own limitation backs the 'perceptual' quality note and the perceived-performance survey measure.

11. **effect_direction, conditions, key_finding** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > The results in Study 2 further highlight that GenAI adoption boosts firm performance and that ethical leadership acts as a significant moderator in the association of GenAI adoption and firm performance.
   Ctrl+F: „The results in Study 2 further highlight that“
   → The paper's own conclusion of its central result, matching the coded key finding (positive effect, stronger under ethical leadership).

12. **conditions** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > The results presented in Tables 4 and 5 illustrate that the impact of GenAI adoption on firm performance in B2B firms is significantly moderated by ethical leadership, supporting H7.
   Ctrl+F: „The results presented in Tables 4 and 5“
   → Backs ethical leadership as the coded moderator of the GenAI adoption-performance link.

13. **conditions** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 56% word sequence
   > The findings highlight that need for uniqueness, information completeness, convenience, and deceptiveness significantly impact GenAI adoption.
   Ctrl+F: „The findings highlight that need for uniqueness, information“
   → Backs the coded adoption reasons for/against (uniqueness, information completeness, convenience, deceptiveness).

14. **conditions, quality_notes** — p. 3 (PDF p. 3) — ✓ verified, 81% word sequence
   > Overall, Study 1 identified three main reasons for adopting GenAI (i.e., need for uniqueness, information completeness, and convenience), and two reasons against its adoption (i.e., deceptiveness and information overload), as shown in Fig. 1
   Ctrl+F: „Overall, Study 1 identified three main reasons for“
   → Backs the quality note that Study 1's own qualitative findings (Fig. 1) generate the adoption reasons fed into Study 2.

15. **theoretical_lens** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > Drawing on behavioral reasoning theory, we consider the moderating role of ethical leadership in the association of B2B managers' GenAI adoption and firm performance
   Ctrl+F: „Drawing on behavioral reasoning theory, we consider the“
   → Names behavioral reasoning theory as the study's theoretical framework.

*Row check OK: ca_measure empty is correct: Appendix item FP2 ('Using Generative AI help the firm to become more competitive') is a single item inside the firm-performance scale, not a distinct validated CA construct with its own hypothesis — per case law this stays performance, no tension. Method was adjudicated to survey-SEM (interviews only develop hypotheses); all coded columns evidenced.*

---

## S38 — Mehta P. et al. (2025) — Journal of Business and Industrial Marketing (AJG 2)

DOI: 10.1108/JBIM-03-2024-0205 · status: final · PDF: `Mehta_2025_JBIM-03-2024-0205.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India |
| sample | Phase 1: 26 key-account-manager interviews (automobile); Phase 2: survey n=496, SEM |
| method | mixed |
| ai_measure | survey construct (adoption of AI technologies by key account managers) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | firm performance (survey scale) |
| ca_measure | competitive advantage (survey scale, modeled as mediator) |
| effect_direction | positive |
| conditions | manager personality traits (Big Five) drive adoption; competitive advantage mediates adoption -> performance; organizational culture moderates (agreeableness -> adoption) |
| key_finding | Individual personality traits shape AI adoption in key account management, which converts into firm performance through competitive advantage - culture conditions the path. |
| *not printed (coding data only)* | |
| theoretical_lens | trait theory + KAM (key account management) |
| industry | automobile (B2B/KAM) |
| quality_notes | Firm-level outcomes from individual-level adoption antecedents; perceptual \| SAMPLE-CHECK OK: CA modeled as own mediator construct (H9), both/positive confirmed |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 547 (PDF p. 5) — ✓ verified, 100% word sequence
   > The data for the qualitative study was collected from National Capital Region of India from the managers working with original equipment manufacturers (OEMs) of automobile industry.
   Ctrl+F: „The data for the qualitative study was collected“
   → Backs India as country and automobile (OEM, B2B/KAM) as industry.

2. **country_region, industry, quality_notes** — p. 558 (PDF p. 16) — ✓ verified, 100% word sequence
   > data was gathered from key account managers used inside the Indian automotive sector. Hence, the conclusions derived from this study lack generalizability to other industries
   Ctrl+F: „data was gathered from key account managers used“
   → Authors' own limitation confirms the Indian automotive KAM setting and its scope limits.

3. **sample, method, industry** — p. 543 (PDF p. 1) — ✓ verified, 100% word sequence
   > In the first phase, an exploratory study was conducted using interviews with 26 key account managers from the automobile industry and thematic analysis to establish 9 constructs.
   Ctrl+F: „phase, an exploratory study was conducted using interviews“
   → Backs Phase 1 of the coded sample (26 KAM interviews, automobile).

4. **sample, method** — p. 543 (PDF p. 1) — ✓ verified, 100% word sequence
   > In the second phase, which is a confirmatory study, 496 respondents finally responded to the questionnaire.
   Ctrl+F: „In the second phase, which is a“
   → Backs Phase 2 of the coded sample (survey n=496, analyzed with SEM).

5. **sample** — p. 552 (PDF p. 10) — ✓ verified, 100% word sequence
   > Of over 2,500 people who were contacted, 496 participants provided their consent to be the respondents in the study by fulfilling the necessary documentation and submitting their responses.
   Ctrl+F: „who were contacted, 496 participants provided their consent“
   → Backs the coded Phase 2 survey sample of n=496.

6. **method** — p. 543 (PDF p. 1) — ✓ verified, 100% word sequence
   > A mixed-method analysis was used to conduct the study.
   Ctrl+F: „A mixed-method analysis was used to conduct the“
   → The paper's own label for its design backs method = mixed.

7. **method** — p. 547 (PDF p. 5) — ✓ verified, 100% word sequence
   > Many of the respondents suggested that their organisation was able to perform better and beat the competition due to timely adoption of newer technologies, like AI based technologies.
   Ctrl+F: „suggested that their organisation was able to perform“
   → Phase 1 interviews also carry outcome-relevant qualitative evidence, consistent with coding the study mixed rather than survey-SEM only.

8. **ai_measure, performance_measure, ca_measure** — p. 551 (PDF p. 9) — ✓ verified, 100% word sequence
   > The questionnaire underwent adaptation and customisation to ensure its alignment with the specific context of the KAMs intention to adopt AI technologies and how it is affecting the competitive advantage and firm performance.
   Ctrl+F: „and customisation to ensure its alignment with the“
   → Shows AI adoption, competitive advantage, and firm performance are all measured as survey constructs.

9. **outcome_construct, theoretical_lens, quality_notes** — p. 545 (PDF p. 3) — ✓ verified, 100% word sequence
   > How the Big-five personality traits of key account managers are affecting the adoption of AI technologies which simultaneously impact the competitive advantage and firm performance?
   Ctrl+F: „How the Big-five personality traits of key account“
   → RQ1 shows the trait-theory + KAM lens and the individual-level antecedents to firm-level CA and performance outcomes noted in quality_notes.

10. **outcome_construct, ca_measure, conditions** — p. 543 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study used competitive advantage as a mediator and organisational culture as a moderator.
   Ctrl+F: „The study used competitive advantage as a mediator“
   → Backs ca_measure as a distinct construct modeled as mediator and org culture as the coded moderator; with firm performance also measured, outcome_construct = both.

11. **ca_measure, conditions** — p. 550 (PDF p. 8) — ✓ verified, 100% word sequence
   > Competitive advantage has a mediating influence on adoption of AI technologies and firm performance.
   Ctrl+F: „Competitive advantage has a mediating influence on“
   → Hypothesis H9 shows CA is an own construct with its own hypothesis (adjudication: CA = own mediator construct, H9), backing the coded mediation condition.

12. **effect_direction** — p. 553 (PDF p. 11) — ✓ verified, 100% word sequence
   > Based on the findings shown in Table 6, there is a positive and statistically significant relationship between all the variables. Therefore, the evidence supports H1 to H8.
   Ctrl+F: „shown in Table 6, there is a positive“
   → All hypothesized paths, including AI adoption to CA (H6) and to firm performance (H7), are positive and significant, backing effect_direction positive.

13. **effect_direction, conditions** — p. 553 (PDF p. 11) — ✓ verified, 100% word sequence
   > The results suggest that CMA has a role in partially mediating the relationship between AAT and FMP.
   Ctrl+F: „suggest that CMA has a role in partially“
   → Partial mediation means the direct AI-performance path stays significant (0.167), so positive stands per the main-effect rule; mediation goes to conditions.

14. **effect_direction, conditions, key_finding** — p. 543 (PDF p. 1) — ✓ verified, 100% word sequence
   > Extraversion, agreeableness, conscientiousness, neuroticism and openness have substantial links to adopting AI technologies, which impacts firms' competitive advantage and performance. Organisational culture significantly moderates the association between agreeableness and the adoption of AI technologies.
   Ctrl+F: „substantial links to adopting AI technologies, which impacts“
   → The paper's own findings statement matches the coded key finding: traits drive adoption, which lifts CA and performance, with culture conditioning one path.

15. **conditions** — p. 553 (PDF p. 11) — ✓ verified, 100% word sequence
   > The findings indicate that ORC does have a moderating effect on the association between AGR and AAT
   Ctrl+F: „does have a moderating effect on the association“
   → Backs the coded condition that organizational culture moderates only the agreeableness-to-adoption link.

16. **theoretical_lens** — p. 546 (PDF p. 4) — ✓ verified, 100% word sequence
   > While factors were identified based on the qualitative study, the theoretical background of the study was based on Big-five personality model, TOE model and RBV of the firm.
   Ctrl+F: „theoretical background of the study was based on“
   → Names the Big-five personality (trait) model as core theory; the coded lens condenses this (paper additionally names TOE and RBV).

*Row check OK: All coded columns evidenced. theoretical_lens 'trait theory + KAM' is a condensation: the paper itself names Big-five personality model, TOE, and RBV (quote p.4). 'perceptual' in quality_notes is coder shorthand for the survey scales (questionnaire quote p.9). method=mixed was spot-checked OK in adjudication; the Phase 1 outcome-relevant testimony (quote p.5) is consistent with the mixed label under the multiple-strands rule.*

---

## S39 — N. Tehrani A. et al. (2025) — European Journal of Marketing (AJG 3)

DOI: 10.1108/EJM-06-2024-0535 · status: final · PDF: `N_2025_EJM-06-2024-0535.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Australia |
| sample | 335 companies across industries, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI-based stakeholder engagement) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | marketing agility (mediator); technological turbulence AMPLIFIES the positive effects (high-turbulence environments gain more) |
| key_finding | AI-based stakeholder engagement improves performance through marketing agility - and the payoff is largest in technologically turbulent environments. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities / marketing agility |
| industry | cross-industry |
| quality_notes | Perceptual, cross-section |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, sample, method, ai_measure, performance_measure, industry** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > Data were collected through a survey of 335 companies across diverse industries in Australia, using validated scales for AI-based stakeholder engagement, marketing agility, firm performance and technology turbulence.
   Ctrl+F: „Data were collected through a survey of 335“
   → One passage backs survey method, n=335, Australia, cross-industry scope, and the survey-scale measurement of AI engagement and firm performance.

2. **country_region, industry** — PDF p. 11, 3.1 Sampling design — ✓ verified, 100% word sequence
   > Our sample includes managers from various major sectors in Australia, such as retailing, health care, IT and ICT, financial services, hospitality and construction.
   Ctrl+F: „Our sample includes managers from various major sectors“
   → Backs cross-industry coding and Australia as country.

3. **sample** — PDF p. 10, 3.1 Sampling design — ✓ verified, 100% word sequence
   > The initial response pool consisted of 339 completed responses. Four responses were flagged for quality issues and subsequently excluded, leaving a final sample size of 335 participants.
   Ctrl+F: „The initial response pool consisted of 339 completed“
   → Backs the coded final sample of 335.

4. **method** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > Partial least squares structural equation modelling was used to analyse the data.
   Ctrl+F: „Partial least squares structural equation modelling was used“
   → Backs the SEM half of the coded method survey-SEM (PLS-SEM as coded in sample).

5. **ai_measure** — PDF p. 11, 3.2 Measurement — ✓ verified, 100% word sequence
   > AI-based stakeholder engagement was measured using an 11-item scale adapted from the stakeholder engagement scale developed by Hughes et al. (2022)
   Ctrl+F: „engagement was measured using an 11-item scale adapted“
   → Backs the coded survey construct 'AI-based stakeholder engagement'.

6. **outcome_construct, performance_measure** — PDF p. 11, 3.2 Measurement — ✓ verified, 100% word sequence
   > To evaluate firm performance, we used a well-established scale from Jaworski and Kohli (1993), which demonstrated a Cronbach's α of 0.86, indicating high reliability.
   Ctrl+F: „To evaluate firm performance, we used a well-established“
   → Backs firm performance as the survey-scale outcome, matching outcome_construct performance.

7. **performance_measure** — PDF p. 11, 3.2 Measurement — ✓ verified, 100% word sequence
   > This scale focuses on two dimensions of the overall performance of the firm and the performance of the firm relative to its major competitors.
   Ctrl+F: „This scale focuses on two dimensions of the“
   → Details the performance scale; the competitor-relative item sits inside the firm-performance scale, not a distinct CA construct, so the empty ca_measure stands (see note).

8. **performance_measure, quality_notes** — PDF p. 10, 3.1 Sampling design — ✓ verified, 100% word sequence
   > We then asked them to rate questionnaire items using a five-point Likert type scale from 1 ('strongly disagree') to 5 ('strongly agree'), based on their firms' practices.
   Ctrl+F: „We then asked them to rate questionnaire items“
   → Backs the 'perceptual' quality note: all constructs are manager-rated Likert perceptions.

9. **effect_direction, conditions, key_finding** — PDF p. 1, Abstract — ✓ verified, 100% word sequence
   > The results indicate that engaging stakeholders through AI technologies positively influences marketing agility, which in turn enhances firm performance. These effects are amplified in conditions of high technology turbulence.
   Ctrl+F: „The results indicate that engaging stakeholders through AI“
   → The paper's own findings statement matches the coded key finding, the positive direction, and the turbulence-amplification condition.

10. **effect_direction, conditions** — PDF p. 19, 5. Discussion — ✓ verified, 100% word sequence
   > Our findings provide compelling evidence that AI-based stakeholder engagement significantly enhances a firm's marketing agility, which in turn positively impacts overall firm performance.
   Ctrl+F: „compelling evidence that AI-based stakeholder engagement significantly enhances“
   → All modeled paths are positive and significant; marketing agility is the coded mediator condition.
   **⚠ TENSION:** The model contains no direct AI-to-performance path (only H1 AI->agility and H3 agility->performance): the performance effect exists only via the mediator, the pattern that S21/S28 precedent coded 'conditional'. Coded 'positive' follows the documented mediated-positive harmonization (every link positive, no null channel) - author should confirm.

11. **conditions** — PDF p. 17, 4. Results — ✓ verified, 100% word sequence
   > The plot reveals that the positive impact of marketing agility on firm performance is amplified under conditions of high technology turbulence.
   Ctrl+F: „positive impact of marketing agility on firm performance“
   → Backs the coded condition that technological turbulence amplifies the positive effects (H4 supported).

12. **theoretical_lens** — PDF p. 3, 1. Introduction — ✓ verified, 100% word sequence
   > We, therefore, examine how AI-based stakeholder engagement functions as a capability that enhances marketing agility and ultimately contributes to firm performance.
   Ctrl+F: „examine how AI-based stakeholder engagement functions as a“
   → Shows the capability/marketing-agility framing behind the coded lens 'dynamic capabilities / marketing agility'.

13. **theoretical_lens** — PDF p. 7, 2.4 Theoretical lenses and hypothesis development — ✓ verified, 100% word sequence
   > Our theoretical framework integrates stakeholder theory and knowledge-based theory, providing a comprehensive perspective on how AI-based stakeholder engagement influences marketing agility and ultimately enhances firm performance.
   Ctrl+F: „Our theoretical framework integrates stakeholder theory and knowledge-based“
   → The paper's own declared theories are stakeholder theory and knowledge-based theory; the coded lens condenses the agility-capability perspective instead (see row_check note).

14. **quality_notes** — PDF p. 21, 5.3 Limitations and future research directions — ⚠ not machine-confirmed on page — open the page, 7% word sequence
   > while our crosssectional findings are valuable, future research could provide a broader perspective by examining the long-term impact of AI-based stakeholder engagement on firm performance.
   Ctrl+F: „findings are valuable, future research could provide a“
   → Authors' own limitation backs the 'cross-section' quality note.

**⚠ ROW CHECK:** (1) effect_direction tension flagged: no direct AI->performance path is modeled; the effect runs entirely through marketing agility (all links positive, bivariate AI-FP correlation 0.326**, Table 4). Structurally this mirrors S21/S28 (coded conditional), while the mediated-positive harmonization rule supports 'positive' - author's call. (2) theoretical_lens: paper self-declares stakeholder theory + knowledge-based theory (sec. 2.4); the coded 'dynamic capabilities / marketing agility' captures the capability framing but not the paper's named theories. (3) ca_measure empty is correct: the competitor-relative item is part of the Jaworski/Kohli firm-performance scale, no distinct CA construct or hypothesis. (4) H2 (turbulence moderating AI->agility) is only 'partially supported' (CI includes zero, Table 6); coded conditions summarize amplification across both links - fine but worth knowing.

---

## S40 — Sandeep M.M. et al. (2025) — Journal of Intellectual Capital (AJG 2)

DOI: 10.1108/JIC-05-2024-0155 · status: final · PDF: `Sandeep_2025_JIC-05-2024-0155.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India (South India) |
| sample | 290 HR professionals in talent acquisition, purposive sampling, South India, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption in recruitment) |
| *Table A.2 columns* | |
| outcome_construct | competitive_advantage |
| performance_measure | — |
| ca_measure | perceived competitive advantage from AI-enabled recruitment (survey scale) |
| effect_direction | positive |
| conditions | HR competencies + open innovation -> dynamic capabilities (mediator); financial support + IT infrastructure as enabling resources |
| key_finding | AI adoption in recruitment yields competitive advantage only where dynamic capabilities, built from HR competencies and open innovation with financial/IT support, are in place. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + dynamic capability framework |
| industry | cross-industry (HR/recruitment function) |
| quality_notes | Perceptual; function-level (recruitment) with org-level outcome \| SAMPLE-CHECK OK: CA measured via established scales (Appendix 1), competitive_advantage confirmed |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 412 (PDF p. 9) — ✓ verified, 100% word sequence
   > Data collection focused on South India and targeted HR professionals actively engaged in Talent Acquisition. Purposive sampling was employed to recruit HR professionals with direct experience in emerging technologies
   Ctrl+F: „India and targeted HR professionals actively engaged in“
   → Backs South India, talent-acquisition focus, and purposive sampling in the sample and country codes.

2. **sample, method** — p. 404 (PDF p. 1) — ✓ verified, 100% word sequence
   > This research utilizes a cross-sectional quantitative approach, applying partial least squares structural equation modeling (PLS-SEM) to data from 290 human resource (HR) professionals.
   Ctrl+F: „This research utilizes a cross-sectional quantitative approach, applying“
   → Survey with PLS-SEM on 290 HR professionals backs method = survey-SEM and the sample coding.

3. **sample** — p. 413 (PDF p. 10) — ✓ verified, 100% word sequence
   > After excluding 64 incomplete or invalid responses, 290 valid questionnaires remained, yielding a final effective response rate of 32% for inclusion in statistical analysis.
   Ctrl+F: „responses, 290 valid questionnaires remained, yielding a final“
   → Confirms the final n = 290 valid responses.

4. **ai_measure, ca_measure** — p. 413 (PDF p. 10) — ✓ verified, 100% word sequence
   > The study adopted constructs from established and reliable scales to measure the key variables. The specific measurement items for each construct are detailed in the questionnaire in Appendix 1.
   Ctrl+F: „The study adopted constructs from established and reliable“
   → All constructs, including AI adoption and competitive advantage, are established survey scales (the point the adjudication sample-check confirmed).

5. **ai_measure** — p. 424 (PDF p. 21) — ✓ verified, 100% word sequence
   > AIA1. AI adoption encourages the integration of automated interviews with other functions AIA2. HR can be involved in strategic-level planning after adopting AI-like automated interviews AIA3. AI improves HR functions in the organization
   Ctrl+F: „AIA1. AI adoption encourages the integration of automated“
   → The AI adoption items show a survey construct on AI adoption in recruitment, as coded.

6. **outcome_construct, ca_measure** — p. 424 (PDF p. 21) — ✓ verified, 100% word sequence
   > CA2: Our firm improved its market position by absorbing advanced AI Recruitment CA3: Our firm attained cost advantage by creatively assimilating advanced process technology
   Ctrl+F: „CA2: Our firm improved its market position by“
   → A distinct three-item competitive-advantage scale (Ferreira et al. 2021) at firm level backs ca_measure and outcome_construct = competitive_advantage.

7. **outcome_construct, effect_direction** — p. 412 (PDF p. 9) — ✓ verified, 100% word sequence
   > H8. The adoption of AI positively influences an organization's competitive advantage.
   Ctrl+F: „H8. The adoption of AI positively influences an“
   → Own hypothesis on measured CA satisfies the CA decision rule (own scale + hypothesis).

8. **effect_direction** — p. 415 (PDF p. 12) — ✓ verified, 100% word sequence
   > Finally, AI adoption significantly enhanced competitive advantage.
   Ctrl+F: „Finally, AI adoption significantly enhanced competitive advantage.“
   → Significant positive main effect (Table 6: AIA to CA, beta 0.466, p 0.000) backs effect_direction = positive.

9. **effect_direction, key_finding** — p. 404 (PDF p. 1) — ✓ verified, 100% word sequence
   > These capabilities enable effective AI adoption, leading to a competitive advantage.
   Ctrl+F: „These capabilities enable effective AI adoption, leading to“
   → Completes the paper's central result statement: capability-enabled AI adoption yields competitive advantage.

10. **conditions, key_finding** — p. 404 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results reveal that HR competencies and open innovation significantly influence dynamic capabilities, which are essential for AI integration, supported by financial support and information technology (IT) infrastructure.
   Ctrl+F: „The results reveal that HR competencies and open“
   → The paper's own findings statement backs the coded conditions: HR competencies + open innovation feeding dynamic capabilities, with financial/IT support as enabling resources.

11. **conditions** — p. 415 (PDF p. 12) — ✓ verified, 100% word sequence
   > The path coefficients confirmed that HR competency and open innovation positively influenced managerial capability. Financial support and IT infrastructure significantly impacted innovation capability.
   Ctrl+F: „The path coefficients confirmed that HR competency and“
   → Structural-model results back the coded resource-to-capability path structure in conditions.

12. **theoretical_lens** — p. 404 (PDF p. 1) — ✓ verified, 100% word sequence
   > It is grounded in the resource-based view (RBV) and dynamic capability framework (DCF).
   Ctrl+F: „It is grounded in the resource-based view (RBV)“
   → Backs the coded lens 'RBV + dynamic capability framework'.

13. **industry** — p. 412 (PDF p. 9) — ✓ verified, 100% word sequence
   > Participants represented a range of industries, enabling a robust quantitative analysis that highlights sector-specific dynamics in AI adoption.
   Ctrl+F: „Participants represented a range of industries, enabling a“
   → Backs cross-industry coding; Table 2 lists IT-software 43%, manufacturing/FMCG 31%, healthcare 14%, banking 12%.

14. **quality_notes** — p. 413 (PDF p. 10) — ✓ verified, 100% word sequence
   > Responses were captured on a 5-point Likert scale, ranging from 1 (Strongly Disagree) to 5 (Strongly Agree).
   Ctrl+F: „Responses were captured on a 5-point Likert scale,“
   → Self-reported Likert measurement backs the 'Perceptual' quality note; the AIA (recruitment-level) vs CA (firm-level) item wording backs the 'function-level with org-level outcome' note.

*Row check OK: performance_measure empty is correct: competitive advantage is the sole final outcome; no separate performance measure. Adjudication brief entry (sample check) confirms CA via established scales, Appendix 1. One oddity for the author: the paper's own limitations section claims a focus on 'a developed economy and the creative industries' (p. 14), contradicting its South-India, IT/manufacturing/healthcare/banking sample - likely authors' boilerplate error; does not affect any coded value.*

---

## S41 — Shi Y. et al. (2025) — International Review of Financial Analysis (AJG 3)

DOI: 10.1016/j.irfa.2025.104694 · status: final · PDF: `Shi_2025_j-irfa-2025-104694.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | Chinese listed companies 2010-2022 (~22,900 firm-year obs); Heckman correction, endogeneity tests |
| method | panel econometrics |
| ai_measure | annual-report text (Word2vec-based AI dictionary) + secondary measure |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | enterprise value (Tobins Q) |
| ca_measure | — |
| effect_direction | positive |
| conditions | data assets mediate 45.6% (direct effect 0.0483*** remains); managerial capability moderates; boundary nulls: heavily polluting industries insignificant (unless credible green transition), asset-intensive firms null; SOE premium 0.035*** vs non-SOE 0.019** |
| key_finding | AI adoption raises enterprise value through data assets, and only under capable management and agile (non-asset-heavy) structures - the study explicitly maps when AI becomes a source of advantage. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + dynamic capabilities + stakeholder perspective |
| industry | cross-industry (listed firms) |
| quality_notes | Causal robustness checks; very high RQ fit (boundary conditions explicit) |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Our empirical investigation examines Chinese listed companies from 2010 to 2022, comprising 22,938 firm-year observations.
   Ctrl+F: „Our empirical investigation examines Chinese listed companies from“
   → Panel of firm-year observations of Chinese listed firms matches method (panel econometrics), sample size (~22,900) and country (China).

2. **sample** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > The Heckman correction method, utilizing the full sample of 22,938 observations, yields stronger statistical evidence of AI adoption's impact on firm value (t = 11.224).
   Ctrl+F: „The Heckman correction method, utilizing the full sample“
   → Backs the sample note 'Heckman correction, endogeneity tests' and the observation count.

3. **method, industry** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > We include both year and industry fixed effects to control for temporal and sector-specific variations.
   Ctrl+F: „We include both year and industry fixed effects“
   → Fixed-effects panel specification confirms panel econometrics; industry fixed effects imply a cross-industry sample.

4. **ai_measure** — p. 2 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 55% word sequence
   > The primary measurement leverages natural language processing techniques, specifically a Word2vec-based dictionary methodology, to quantify AI adoption levels from corporate disclosures.
   Ctrl+F: „methodology, to quantify AI adoption levels from corporate“
   → Primary AI measure is the annual-report Word2vec-based AI dictionary, as coded.

5. **ai_measure** — p. 2 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 19% word sequence
   > To ensure measurement robustness, we complement this with a patent-based approach that tracks firms' AI-related intellectual property development through the Chinese Patent Office database.
   Ctrl+F: „this with a patent-based approach that tracks firms’“
   → The coded 'secondary measure' is this patent-based robustness measure.

6. **outcome_construct, performance_measure** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > The measurement of enterprise value through Tobin's Q represents a critical component of our research design
   Ctrl+F: „The measurement of enterprise value through Tobin’s Q“
   → Dependent variable is enterprise value operationalized as Tobin's Q — a performance construct, matching performance_measure.

7. **effect_direction** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The direct effect of AI adoption on firm value shows strong statistical significance (Z = 10.26, p < 0.001) with a coefficient of 0.0483.
   Ctrl+F: „The direct effect of AI adoption on firm“
   → Significant positive direct effect despite partial mediation — per the main-effect rule the direction is positive (adjudicated).

8. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The comparable magnitudes of direct (0.0483) and indirect (0.0405) effects suggest that data assets mediate approximately 45.6 % of AI adoption's total effect on firm value
   Ctrl+F: „direct (0.0483) and indirect (0.0405) effects suggest that“
   → Backs the coded mediation share of 45.6% via data assets with a remaining direct effect of 0.0483.

9. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > This positive interaction effect provides strong support for our third hypothesis, indicating that managerial capability enhances the relationship between AI adoption and firm value.
   Ctrl+F: „for our third hypothesis, indicating that managerial capability“
   → Managerial capability as a positive moderator, as coded in conditions.

10. **conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > the valuation premium is stronger for state-owned enterprises, disappears in heavily polluting industries unless AI is part of a credible green transition, and is evident only in non-asset-intensive firms where resource reconfiguration is agile.
   Ctrl+F: „the valuation premium is stronger for state-owned enterprises,“
   → Abstract summarizes the three heterogeneity boundary conditions exactly as coded (SOE premium, polluting-industry null, asset-intensity null).

11. **conditions** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > for SOEs the AI coefficient is 0.035 (t = 3.160, p < 0.01), almost double the 0.019 recorded for non-SOEs (t = 2.327, p < 0.05)
   Ctrl+F: „for SOEs the AI coefficient is 0.035 (t“
   → Exact coefficients behind the coded 'SOE premium 0.035*** vs non-SOE 0.019**'.

12. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Our analysis reveals that AI adoption significantly enhances enterprise value both directly and indirectly through data assets, demonstrating substantial mediation effects.
   Ctrl+F: „Our analysis reveals that AI adoption significantly enhances“
   → The paper's own statement of its central result: AI raises enterprise value directly and via data assets.

13. **key_finding** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > digital capability yields competitive advantage only when either structural flexibility is high or state backing cushions adjustment costs
   Ctrl+F: „only when either structural flexibility is high or“
   → Backs the coded key_finding clause that the study explicitly maps when AI becomes a source of advantage.

14. **theoretical_lens** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 33% word sequence
   > By integrating resource-based, dynamic-capability, and stakeholder perspectives, the study clarifies when AI becomes a genuine source of competitive advantage.
   Ctrl+F: „perspectives, the study clarifies when AI becomes a“
   → Abstract names all three coded lenses: RBV, dynamic capabilities, stakeholder perspective.

15. **industry** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > To ensure data quality, we exclude financial institutions due to their distinct regulatory environment, ST and *ST companies, firms with missing data for key variables
   Ctrl+F: „institutions due to their distinct regulatory environment, ST“
   → All listed firms except financials are covered, evidencing the cross-industry (listed firms) coding.

16. **quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Through extensive robustness checks and endogeneity tests, we establish the causal nature of these relationships.
   Ctrl+F: „endogeneity tests, we establish the causal nature of“
   → Source basis for the quality note 'causal robustness checks' (IV, PSM, Heckman all reported).

*Row check OK: ca_measure empty is correct: 'competitive advantage' appears only as framing in abstract/conclusion, no distinct CA construct is measured (DV is Tobin's Q). The quality_notes clause 'very high RQ fit' is coder commentary, not source-based, so no quote. Spaced apostrophes in the extraction (e.g. 'Tobin ' s') were normalized like split ligatures.*

---

## S42 — Song D. et al. (2025) — Industrial Management and Data Systems (AJG 2)

DOI: 10.1108/IMDS-02-2024-0076 · status: final · PDF: `Song_2025_IMDS-02-2024-0076.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 120 AI service failure events 2010-2024 at NYSE/NASDAQ-listed companies (from 451 initial events) |
| method | event study |
| ai_measure | announcements (AI service FAILURE events) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm value (negative abnormal returns) |
| ca_measure | — |
| effect_direction | negative |
| conditions | small firms hit harder; recent years more negative; failure-type order effect: accuracy > safety > privacy > fairness |
| key_finding | AI service failures destroy market value - most for small firms and accuracy failures; the downside risk of AI implementation is real and priced. |
| *not printed (coding data only)* | |
| theoretical_lens | expectation (dis)confirmation / IS failure literature |
| industry | cross-industry |
| quality_notes | Event study; unique downside-risk evidence \| SAMPLE-CHECK OK: event study/negative confirmed (NYSE/NASDAQ failure events) |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 512 (PDF p. 9) — ✓ verified, 100% word sequence
   > the public stock exchanges NYSE and NASDAQ, resulting in 451 events
   Ctrl+F: „the public stock exchanges NYSE and NASDAQ, resulting“
   → Backs the coded 'NYSE/NASDAQ-listed companies (from 451 initial events)' filtering step.

2. **country_region, sample, method** — p. 526 (PDF p. 23) — ✓ verified, 100% word sequence
   > In this study, we investigated the impacts of AI service failure events on firm stock value using a sample of 120 AI service failure events in publicly traded U.S. firms.
   Ctrl+F: „impacts of AI service failure events on firm“
   → Conclusion confirms the firms are publicly traded U.S. firms (country_region USA) and restates sample and event-study design.

3. **sample, method** — p. 504 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study will conduct an event study of 120 AI service failure events in listed companies to evaluate the costs of such events.
   Ctrl+F: „This study will conduct an event study of“
   → Abstract states the event study method and the 120-event sample of listed companies.

4. **sample** — p. 512 (PDF p. 9) — ✓ verified, 100% word sequence
   > Following these procedures, a total of 120 AI service failure events from 75 firms were identified between 2010 and 2024.
   Ctrl+F: „these procedures, a total of 120 AI service“
   → Final sample of 120 events, 2010-2024, matching the coded sample period and count.

5. **ai_measure** — p. 511 (PDF p. 8) — ✓ verified, 100% word sequence
   > We checked all news announcements links of AI service failure events and used the earliest release date of news as the event date.
   Ctrl+F: „We checked all news announcements links of AI“
   → The AI measure is announcement-based: news announcements of AI service failure events define the events, as coded.

6. **outcome_construct, performance_measure, effect_direction** — p. 515 (PDF p. 12) — ✓ verified, 100% word sequence
   > the portfolio of the firms in the sample experienced an average 1.37% decrease in their stock prices compared with their market valuations based on the CAPM model
   Ctrl+F: „of the firms in the sample experienced an“
   → Outcome is firm market value via negative cumulative abnormal returns (mean CAR -1.37%, p<0.01), backing performance_measure and the negative direction.

7. **conditions** — p. 504 (PDF p. 1) — ✓ verified, 100% word sequence
   > Second, small firms experience more share price declines due to AI service failure events than large firms.
   Ctrl+F: „experience more share price declines due to AI“
   → Backs the coded condition 'small firms hit harder' (firm size moderator, H3 supported).

8. **conditions** — p. 504 (PDF p. 1) — ✓ verified, 100% word sequence
   > Third, AI service failure events in more recent years have a more intensively negative impact than those in more distant years.
   Ctrl+F: „events in more recent years have a more“
   → Backs the coded condition 'recent years more negative' (event-year moderator, H4 supported).

9. **conditions** — p. 504 (PDF p. 1) — ✓ verified, 100% word sequence
   > we identify different types of AI service failure and find that there are order effects on firm value across the service failure event types: accuracy > safety > privacy > fairness.
   Ctrl+F: „identify different types of AI service failure and“
   → Backs the coded failure-type order effect 'accuracy > safety > privacy > fairness' (H5 supported).

10. **key_finding** — p. 526 (PDF p. 23) — ✓ verified, 100% word sequence
   > Based on the empirical analysis, we found a negative effect of AI service failure events on firm stock value.
   Ctrl+F: „of AI service failure events on firm stock“
   → The paper's own conclusion of its central result: AI service failures destroy market value.

11. **theoretical_lens** — p. 506 (PDF p. 3) — ✓ verified, 100% word sequence
   > These definitions emphasize the undesirable outcomes of service delivery and the mismatch between the outcomes and expectations.
   Ctrl+F: „These definitions emphasize the undesirable outcomes of service“
   → AI service failure is defined via expectation disconfirmation (outcome-expectation mismatch), backing the coded lens part 'expectation (dis)confirmation'.

12. **theoretical_lens** — p. 510 (PDF p. 7) — ✓ verified, 100% word sequence
   > It is well documented in the information systems literature that the market value of larger firms is less adversely impacted by announcements of negative events, such as security breaches
   Ctrl+F: „It is well documented in the information systems“
   → Hypotheses are grounded in the IS failure / security-breach event literature, backing the coded lens part 'IS failure literature'.

13. **theoretical_lens** — p. 505 (PDF p. 2) — ✓ verified, 100% word sequence
   > this study is the initial effort to apply signaling theory to explain the market impact of AI service failure events and empirically evaluate their impact on firm value
   Ctrl+F: „this study is the initial effort to apply“
   → The paper's own primary declared framework is signaling theory (section 2.3); included so the author can verify the coded lens label, which does not mention it.

14. **industry** — p. 515 (PDF p. 12) — ✓ verified, 100% word sequence
   > To test H2, we divided the full sample into two sub-samples: technology vs non-technology firms.
   Ctrl+F: „To test H2, we divided the full sample“
   → Sample spans technology and non-technology firms (82 vs 38 events), evidencing the cross-industry coding.

15. **quality_notes** — p. 504 (PDF p. 1) — ✓ verified, 100% word sequence
   > First, this study is the initial effort to empirically examine market reactions to AI service failure events using the event study method.
   Ctrl+F: „First, this study is the initial effort to“
   → Backs the quality note 'unique downside-risk evidence' - the authors claim to be the first firm-value event study of AI service failures.

**⚠ ROW CHECK:** Three items for the author: (1) theoretical_lens - the paper's self-declared primary framework is signaling theory (own section 2.3, 'initial effort to apply signaling theory'); the coded 'expectation (dis)confirmation / IS failure literature' is supportable from the failure definition and hypothesis grounding but omits signaling theory. (2) conditions - the paper also identifies an industry-type moderator (technology firms hit harder, H2 partially supported at the [0,1] window) which is not in the coded conditions. (3) ca_measure empty is correct ('loss of competitive advantage' appears only as an unmeasured intangible-cost example); the 'SAMPLE-CHECK OK' part of quality_notes is process commentary, not source-based.

---

## S43 — Tao Y. et al. (2025) — Journal of Business and Industrial Marketing (AJG 2)

DOI: 10.1108/JBIM-09-2024-0706 · status: final · PDF: `Tao_2025_JBIM-09-2024-0706.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 291 B2B manufacturing firms, multi-wave multi-source, SEM |
| method | survey-SEM |
| ai_measure | survey construct (big data analytical intelligence assimilation + AI capabilities) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | new product performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | AI capabilities (mediator: BDAI assimilation alone insufficient); electronic supply-chain collaboration (moderator, strengthens the indirect effect) |
| key_finding | Big-data/AI assimilation lifts new product performance only when converted into AI capabilities, and more so with electronic supply-chain collaboration. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities theory |
| industry | manufacturing (B2B) |
| quality_notes | Multi-wave, multi-source (stronger than single-informant) \| SAMPLE-CHECK OK with caveat: total effect BDAI->NPP 0.24*** significant, indirect via AI capabilities 0.15* - partial mediation, positive stands per main-effect rule; direct-path row not explicit in text (borderline to conditional) |
| coding_status | final |

### Evidence

1. **country_region, sample, method, theoretical_lens** — p. 44 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 42% word sequence
   > Drawing on the dynamic capabilities theory (DCT), this study tests the moderated-mediation model using multiwave, multi-source data collected from 291 Chinese B2B manufacturing firms. Structural equation modeling was applied to test the proposed hypotheses.
   Ctrl+F: „Drawing on the dynamic capabilities theory (DCT), this“
   → Abstract states the DCT lens, the survey-SEM method, the 291-firm multi-wave multi-source sample, and China in one passage.

2. **sample** — p. 49 (PDF p. 6) — ✓ verified, 65% word sequence
   > A total of 291 firms from the initial pool of 1,500 firms across three key provinces provided consistent and complete responses at all three times, forming the final matched sample
   Ctrl+F: „and complete responses at all three times, forming“
   → Confirms the final n = 291 and the three-wave matched design coded in sample.

3. **sample, quality_notes** — p. 50 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 15% word sequence
   > we collected a multisource data collection approach by gathering information from two informants (i.e. CEOs and senior marketing managers)
   Ctrl+F: „two informants (i.e. CEOs and senior marketing managers)“
   → Backs the quality note 'multi-source (stronger than single-informant)': two informants per firm.

4. **sample, quality_notes** — p. 50 (PDF p. 7) — ✓ verified, 100% word sequence
   > we temporally separated the measurement of constructs by administering our surveys in three distinct phases
   Ctrl+F: „measurement of constructs by administering our surveys in“
   → Backs the 'multi-wave' part of sample and quality_notes: three time-separated survey waves.

5. **ai_measure** — p. 50 (PDF p. 7) — ✓ verified, 100% word sequence
   > BDAI assimilation was measured using a three-item scale validated by Zhang et al. (2020), and AI capabilities were measured using a four-item scale established by Dubey et al. (2022).
   Ctrl+F: „assimilation was measured using a three-item scale validated“
   → Both coded AI constructs (BDAI assimilation and AI capabilities) are survey scales, as coded in ai_measure.

6. **outcome_construct, performance_measure** — p. 50 (PDF p. 7) — ✓ verified, 100% word sequence
   > while a three-item scale of NPP was adapted from the existing research by Jin et al. (2019)
   Ctrl+F: „adapted from the existing research by Jin et“
   → New product performance is measured by a survey scale - a performance construct, matching performance_measure.

7. **effect_direction, quality_notes** — p. 51 (PDF p. 8) — ✓ verified, 100% word sequence
   > the total effect of BDAI assimilation on NPP yielded a statistically significant outcome (β = 0.24, s.e. = 0.06, p < 0.001, 95% CI = [0.15, 0.29])
   Ctrl+F: „of BDAI assimilation on NPP yielded a statistically“
   → Significant positive total effect - per the main-effect rule direction is positive (Arthur's batch decision: S43 stays positive); also the 0.24*** figure cited in quality_notes.

8. **conditions, quality_notes** — p. 51 (PDF p. 8) — ✓ verified, 100% word sequence
   > The results provide robust support for this with a substantial effect (β = 0.15, s.e. = 0.06, p < 0.05, 95% CI = [0.06, 0.22]).
   Ctrl+F: „support for this with a substantial effect (β = 0.15,“
   → H4 mediation result: AI capabilities mediate BDAI assimilation -> NPP with indirect effect 0.15*, backing the coded mediator condition and the quality-note figure.

9. **conditions, key_finding** — p. 44 (PDF p. 1) — ✓ verified, 100% word sequence
   > B2B managers and policy architects should recognize that investment in BDAI assimilation is not sufficient. However, building AI capabilities might fully support BDAI assimilation to gain innovation outcomes such as NPP.
   Ctrl+F: „B2B managers and policy architects should recognize that“
   → The paper's own statement that assimilation alone is insufficient without AI capabilities, backing the coded condition phrasing.

10. **conditions** — p. 44 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study further found that this mediation model is strengthened through the contingency impact of ESCC and increases its indirect effect on NPP.
   Ctrl+F: „This study further found that this mediation model“
   → Abstract states ESCC as the moderator strengthening the indirect effect, exactly as coded.

11. **conditions** — p. 52 (PDF p. 9) — ✓ verified, 100% word sequence
   > the statistical results reveal a significant interaction effect between BDAI assimilation and ESCC (β = 0.21, s.e. = 0.05, p < 0.01, 95% CI = [0.12, 0.38])
   Ctrl+F: „ESCC (β = 0.21, s.e. = 0.05, p < 0.01, 95% CI“
   → Significant BDAI x ESCC interaction (H5), backing ESCC as an identified moderator.

12. **conditions** — p. 52 (PDF p. 9) — ✓ verified, 100% word sequence
   > The steeper slope under low ESCC suggests a stronger impact of BDAI assimilation on AI capabilities when ESCC is low, indicating a compensatory rather than amplifying role
   Ctrl+F: „suggests a stronger impact of BDAI assimilation on“
   → Figure 2 caption on the direction of the ESCC moderation.
   **⚠ TENSION:** The paper is internally inconsistent: this Figure 2 caption calls ESCC compensatory (stronger BDAI effect at LOW ESCC), while the abstract and Table 5 (conditional indirect effects rising 0.06 -> 0.10 -> 0.13 with higher ESCC) say strengthening - the coded 'strengthens the indirect effect' follows the abstract/Table 5, but the author should see this contradiction.

13. **key_finding** — p. 44 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results demonstrate that BDAI assimilation significantly promotes NPP, and AI capabilities act as an intermediary bridge empowering B2B firms to convert BDAI assimilation into enhanced NPP.
   Ctrl+F: „The results demonstrate that BDAI assimilation significantly promotes“
   → The paper's own statement of its central result, matching the coded key_finding.

14. **industry** — p. 48 (PDF p. 5) — ✓ verified, 100% word sequence
   > These selected B2B firms represent a diverse range of manufacturing sectors that include information technology, chemicals, plastics, and rubber production.
   Ctrl+F: „B2B firms represent a diverse range of manufacturing“
   → Backs the coded industry 'manufacturing (B2B)' with the specific sectors sampled.

**⚠ ROW CHECK:** Two items: (1) The quality_notes caveat says the direct-path row is 'not explicit in text' - but Table 4 (PDF p. 8) does list row 5 'The direct effect of BDAI assimilation on NPP' = 0.16, p < 0.05, 95% CI [0.01, 0.31], i.e. a significant direct path; this strengthens the adjudicated 'positive' (partial, not full, mediation) and the caveat could be updated. (2) Figure 2 caption contradiction on the ESCC moderation direction (see tension on the Figure 2 quote). ca_measure empty is correct: 'competitive advantage' appears only in DCT framing, no CA construct is measured.

---

## S44 — Tingbani I. et al. (2025) — International Journal of Finance and Economics (AJG 3)

DOI: 10.1002/ijfe.2945 · status: final · PDF: `Tingbani_2025_ijfe-2945.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 1,950 unique US firms, 1996-2016, Compustat; system GMM |
| method | panel econometrics |
| ai_measure | resume-based (share of employees with AI skills, from resume/job data; Fedyk & Hodson 2023 approach) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm growth (sales growth) |
| ca_measure | — |
| effect_direction | positive |
| conditions | labour market conditions: labour productivity amplifies growth effect; labour cost and labour share weaken it |
| key_finding | AI investment raises firm growth modestly on average; labour-market conditions moderate the size of the gain - productivity-rich, labour-cost-light firms capture more of it. |
| *not printed (coding data only)* | |
| theoretical_lens | none explicit (labour economics framing) |
| industry | cross-industry |
| quality_notes | GMM; small average effect size worth noting in synthesis |
| coding_status | final |

### Evidence

1. **country_region, sample, method, effect_direction, key_finding** — p. 961 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using the generalized method of moments (GMM) estimation on 1950 unique American firms over 1996-2016, we show that a 10% increase in AI investment leads to an increase in firm growth by 0.04%.
   Ctrl+F: „generalized method of moments (GMM) estimation on 1950“
   → Abstract states GMM panel method, the 1,950-firm US sample 1996-2016, and the average positive effect size coded in conditions/key_finding.

2. **country_region, sample, method** — p. 962 (PDF p. 2) — ✓ verified, 100% word sequence
   > we develop a GMM estimation model on a sample of 1950 unique US firms from 1996 to 2016
   Ctrl+F: „develop a GMM estimation model on a sample“
   → Confirms the coded sample size, country, and period.

3. **sample, ai_measure** — p. 965 (PDF p. 5) — ✓ verified, 100% word sequence
   > We then matched the employer's name to the names of publicly traded firms in the Compustat data set using the approach developed by Fedyk and Hodson (2023).
   Ctrl+F: „the employer's name to the names of publicly“
   → Backs the coded 'Fedyk & Hodson 2023 approach' and the Compustat basis of the sample.

4. **sample, effect_direction, key_finding** — p. 977 (PDF p. 17) — ⚠ not machine-confirmed on page — open the page, 14% word sequence
   > Using a sample of publicly traded US firms from the COMPUSTAT annual file from 1996 to 2016, the study finds strong evidence that AI investment positively impacts firm growth.
   Ctrl+F: „traded US firms from the COMPUSTAT annual file“
   → The paper's own concluding statement of its central result; also confirms Compustat and the US sample.

5. **method, quality_notes** — p. 965 (PDF p. 5) — ✓ verified, 100% word sequence
   > To overcome these two challenges, we employ the system GMM dynamic panel estimator (Arellano & Bover, 1995; Blundell & Bond, 1998), which offers several advantages.
   Ctrl+F: „To overcome these two challenges, we employ the“
   → Backs the coded method 'panel econometrics' and the quality note 'GMM' (system GMM addressing endogeneity).

6. **ai_measure** — p. 965 (PDF p. 5) — ✓ verified, 100% word sequence
   > we construct a new measure of firm investments in AI based on the intensity of hiring
   Ctrl+F: „investments in AI based on the intensity of“
   → The AI measure is workforce/hiring-based (AI-skilled labour from job postings and employee profiles), matching the coded resume/job-based measure.

7. **outcome_construct, performance_measure** — p. 965 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 31% word sequence
   > The dependent variable denotes firms' growth for firm i in year t measured as a one-year growth rate of sales (SALE) at time t-1
   Ctrl+F: „denotes firms' growth for firm i in year“
   → DV is sales growth - a performance construct, matching the coded performance_measure 'firm growth (sales growth)'.

8. **effect_direction, conditions, quality_notes** — p. 967 (PDF p. 7) — ✓ verified, 100% word sequence
   > The results show that a 10% decrease (increase) in AI investment leads to a decrease (increase) in firms' growth by 0.04%.
   Ctrl+F: „show that a 10% decrease (increase) in AI“
   → Baseline result: the average AI-growth effect (+0.04% per 10%) coded in conditions, and the 'small average effect size' quality note.
   **⚠ TENSION:** effect_direction is coded 'conditional', but the paper reports a clear, significant average positive main effect that is robust across endogeneity tests, alternative measures and subsamples (conclusion: 'strong evidence that AI investment positively impacts firm growth'). Under the frozen main-effect rule this reads as 'positive' with labour-market moderators in conditions; the row was not among the adjudicated disputes, so the author should re-check.

9. **conditions, key_finding** — p. 961 (PDF p. 1) — ✓ verified, 100% word sequence
   > However, this result is highly sensitive to labour market conditions, as labour productivity can positively impact firm growth, but labour cost and labour share negatively influence firm growth.
   Ctrl+F: „labour market conditions, as labour productivity can positively“
   → Abstract backs the coded conditions: productivity amplifies, labour cost and labour share weaken - the payoff hinges on labour-market conditions.

10. **conditions** — p. 971 (PDF p. 11) — ⚠ not machine-confirmed on page — open the page, 55% word sequence
   > The findings suggest that labour market conditions moderate the relationship between AI investment and firms' growth. The findings suggest efficient labour market conditions further reinforce the positive relationship between AI and firms' growth.
   Ctrl+F: „The findings suggest that labour market conditions“
   → Interaction results (Table 5) identify labour market conditions as moderators of the AI-growth link, matching the coded conditions.

11. **conditions** — p. 970 (PDF p. 10) — ✓ verified, 100% word sequence
   > The results find labour productivity to be positive and statistically significant at 1%
   Ctrl+F: „The results find labour productivity to be positive“
   → Backs the 'labour productivity amplifies' part of the coded conditions (positive significant coefficient on growth).

12. **theoretical_lens** — p. 962 (PDF p. 2) — ✓ verified, 100% word sequence
   > Our paper develops a resource-based framework, using investment in AI, labour market conditions, and firm growth as underlying parameters
   Ctrl+F: „investment in AI, labour market conditions, and firm“
   → Shows the paper's declared framework.
   **⚠ TENSION:** theoretical_lens is coded 'none explicit (labour economics framing)', but the paper explicitly develops a resource-based (RBV) framework - see also section 2.1. The 'none explicit' label looks factually wrong; author should re-check.

13. **theoretical_lens** — p. 962 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > The fundamental theory underlying this evidence is the resource-based view (RBV), which highlights strong internal resources and capabilities as key ingredients required by a firm to achieve positive output
   Ctrl+F: „The fundamental theory underlying this evidence is the“
   → Section 2.1 names RBV as the fundamental theory - further evidence for the tension flagged on the previous quote.

14. **industry** — p. 965 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 11% word sequence
   > resulting in excluding financial firms (SIC codes 6000-6999) and utilities (SIC codes 4900-4999) from the sample
   Ctrl+F: „financial firms (SIC codes 6000-6999) and utilities“
   → Sample spans all industries except financials and utilities, evidencing the cross-industry coding.

**⚠ ROW CHECK:** Three items: (1) theoretical_lens 'none explicit' conflicts with the paper's explicit RBV framework (tensions on quotes 2-3). (2) effect_direction 'conditional' vs the paper's robust significant positive average main effect (tension on the baseline-result quote); this row was not in adjudication_briefs.md, so it never went through individual adjudication. (3) The paper is internally muddled on moderation direction: H2/H3 predict labour share/cost weaken the AI-growth link (as coded), but Table 5 reports significantly POSITIVE interaction terms for all three labour conditions and still claims support for H2-H4 - the coded 'weaken' follows the abstract and the Table 4 direct effects, not Table 5. ca_measure empty is correct: competitive-advantage/VRIN talk is theory framing only, no CA construct is measured.

---

## S45 — Adams J.J. et al. (2026) — Journal of Monetary Economics (AJG 4)

DOI: 10.1016/j.jmoneco.2025.103875 · status: final · PDF: `Adams_2026_j-jmoneco-2025-103875.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | US firms matched to Lightcast job postings 2010Q1-2024Q1 (40,000+ job boards); AI-pricing jobs identified |
| method | panel econometrics |
| ai_measure | job postings (AI-skill + pricing keyword = AI pricing adoption) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | growth in sales, employment, assets, markups; stock-return response to monetary policy |
| ca_measure | — |
| effect_direction | positive |
| conditions | adoption concentrated in larger, more productive firms; adopters more responsive to monetary policy surprises |
| key_finding | Firms adopting AI-powered pricing grow faster in sales, employment and markups - AI pricing is a capability large productive firms exploit first. |
| *not printed (coding data only)* | |
| theoretical_lens | information economics (monopolist pricing model) |
| industry | cross-industry |
| quality_notes | Novel job-postings measure; macro-finance angle (JME 4) |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > We use the Lightcast data, formerly Burning Glass, on U.S. job postings from 2010Q1 to 2024Q1.
   Ctrl+F: „We use the Lightcast data, formerly Burning Glass,“
   → Backs the coded sample window (Lightcast 2010Q1-2024Q1) and USA.

2. **country_region, sample** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > To obtain firm characteristics such as size, age, productivity, and financial conditions, we merge the Lightcast data with Compustat Quarterly. Compustat Quarterly provides detailed balance sheet data for the universe of public US firms.
   Ctrl+F: „To obtain firm characteristics such as size, age,“
   → Backs 'US firms matched to Lightcast job postings': merge with Compustat covering public US firms.

3. **sample** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Lightcast collects job posting data from over 40,000 online job boards and company websites, converting them into a systematic machine-readable form.
   Ctrl+F: „data from over 40,000 online job boards and“
   → Backs the '40,000+ job boards' detail in the coded sample.

4. **sample, method** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > This process results in a quarterly panel dataset with 4695 unique firms and 131,647 firm-quarter observations.
   Ctrl+F: „This process results in a quarterly panel dataset“
   → A firm-quarter panel of 4,695 firms backs method = panel econometrics and quantifies the sample.

5. **sample, industry** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > our focus is on the adoption of AI pricing across the entire economy: We document the adoption of AI pricing for the universe of US firms posting jobs online
   Ctrl+F: „our focus is on the adoption of AI“
   → Economy-wide coverage across all industries backs the cross-industry coding.

6. **method** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > To explore this, we specify a long-difference regression, linking changes in firm outcomes to different indicators of AI pricing adoption
   Ctrl+F: „explore this, we specify a long-difference regression, linking“
   → Long-difference panel regressions (plus event-level monetary-shock regressions with firm fixed effects) generate the AI-outcome evidence, backing panel econometrics.

7. **ai_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We infer that a firm is adopting AI pricing if it posts a job that requires AI-related skills and contains the keyword ''pricing.''
   Ctrl+F: „AI pricing if it posts a job that“
   → Exactly the coded AI measure: job postings with AI skills plus pricing keyword identify AI pricing adoption.

8. **outcome_construct, performance_measure, effect_direction, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Firms that adopted AI pricing experienced faster growth in sales, employment, assets, and markups, and their stock returns are also more responsive to high-frequency monetary policy surprises than non-adopters.
   Ctrl+F: „Firms that adopted AI pricing experienced faster growth“
   → The paper's summary result backs performance as outcome, the coded performance measures (growth in sales/employment/assets/markups; stock-return response to monetary policy), and the positive direction.

9. **outcome_construct, effect_direction, key_finding** — p. 23 (PDF p. 23) — ✓ verified, 100% word sequence
   > Our evidence suggests that larger and more productive firms are more likely to adopt AI pricing, and such adoption improves firm performance and increases the sensitivity of a firm's stock returns to monetary policy surprises.
   Ctrl+F: „suggests that larger and more productive firms are“
   → The paper's own conclusion states the central result exactly as coded: positive performance effect concentrated in larger, more productive adopters.

10. **conditions** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > We next examine the firm-level determinants of AI pricing adoption, and we find that larger, more productive, and R&D-intensive firms tend to adopt AI pricing more aggressively.
   Ctrl+F: „determinants of AI pricing adoption, and we find“
   → Backs the coded condition 'adoption concentrated in larger, more productive firms'.

11. **conditions, key_finding** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > The table shows that the positive relations between the adoption of AI pricing and firm growth are stronger for larger firms.
   Ctrl+F: „The table shows that the positive relations between“
   → Size heterogeneity in the performance effect backs the key finding that AI pricing is a capability large firms exploit first.

12. **conditions** — p. 15 (PDF p. 15) — ✓ verified, 100% word sequence
   > Firms with a higher share of AI pricing benefit significantly more from this monetary expansion.
   Ctrl+F: „Firms with a higher share of AI pricing“
   → Backs the coded condition 'adopters more responsive to monetary policy surprises'.

13. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We show that these empirical observations can be rationalized by a simple model where a monopolist firm with incomplete information about its demand function invests in AI pricing to acquire information.
   Ctrl+F: „observations can be rationalized by a simple model“
   → Backs the coded lens 'information economics (monopolist pricing model)': incomplete-information monopolist investing in AI pricing to acquire information.

14. **quality_notes** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > However, there are several important limitations in using the job postings data for measuring AI pricing adoption. First, our measure is an input-based measure
   Ctrl+F: „However, there are several important limitations in using“
   → Authors' own discussion of their novel job-postings measure and its input-based limitation backs the 'Novel job-postings measure' quality note.

*Row check OK: ca_measure empty is correct: no competitive-advantage construct is measured; all outcomes are performance/growth and stock-return responses. The 'macro-finance angle (JME 4)' part of quality_notes is coder commentary (journal identity), not a source claim. Minor nuance for the author: the monetary-policy shock analysis uses the 2010-2019 Bauer-Swanson subsample (81 FOMC events), while the growth analysis spans 2010-2023/2024Q1. Not in adjudication_briefs.md.*

---

## S46 — Agag G. et al. (2026) — Tourism Management (AJG 4)

DOI: 10.1016/j.tourman.2026.105470 · status: final · PDF: `Agag_2026_j-tourman-2026-105470.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | UK |
| sample | 1,206 UK listed tourism/travel/hospitality firms, 7,539 firm-years 2018-2024; two-step system GMM |
| method | panel econometrics |
| ai_measure | AI human capital (AI-skilled workforce measure) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm value; wage inequality as mediating channel |
| ca_measure | — |
| effect_direction | positive |
| conditions | wage inequality partially mediates (AIHC compresses inequality -> value); stronger in dynamic/complex industries; sector split: value effect strongest in travel, inequality compression in hospitality |
| key_finding | AI human capital raises firm value partly by compressing wage inequality - a workforce-centered pathway to AI-enabled advantage, strongest in dynamic sectors. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV + tournament theory |
| industry | tourism, travel & hospitality |
| quality_notes | GMM with Windmeijer correction; sectoral heterogeneity |
| coding_status | final |

### Evidence

1. **country_region, sample, method, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using an unbalanced panel of 1206 UK listed TTH firms comprising 7539 firm year observations from 2018 to 2024, we estimate internal instrument two step system GMM models with Windmeijer corrected standard errors.
   Ctrl+F: „panel of 1206 UK listed TTH firms comprising“
   → States the coded sample size (1,206 firms, 7,539 firm-years 2018-2024), UK setting, panel-econometric method (two-step system GMM) and the Windmeijer correction noted in quality_notes.

2. **method** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > we adopt a dynamic panel data (DPD) approach in which the one-period lag of the dependent variable enters the model as a regressor.
   Ctrl+F: „panel data (DPD) approach in which the one-period“
   → Methods section confirms dynamic panel econometrics as the strategy generating the AI-outcome evidence.

3. **ai_measure** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > AI human capital was proxied by the share of AI-related workers in total employment at the firm-year level.
   Ctrl+F: „share of AI-related workers in total employment at“
   → Defines the AI measure as an AI-skilled workforce share, matching 'AI human capital (AI-skilled workforce measure)'.

4. **outcome_construct, performance_measure** — p. 8 (PDF p. 8) — ✓ verified, 73% word sequence
   > Firm value was assessed using Tobin's Q, an established indicator of long-term performance and market-based expectations of intangible resources
   Ctrl+F: „assessed using Tobin's Q, an established indicator of“
   → The outcome is firm value measured by Tobin's Q, a performance construct - no distinct CA construct is measured.

5. **effect_direction** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > In Model 1, AIHC is positively associated with Tobin Q (0.065, t = 2.50), supporting H1.
   Ctrl+F: „AIHC is positively associated with Tobin Q (0.065,“
   → Significant positive main effect of AI human capital on firm value backs effect_direction = positive.

6. **effect_direction, conditions** — p. 11 (PDF p. 11) — ⚠ not machine-confirmed on page — open the page, 45% word sequence
   > Taken together, these results indicate complementary partial mediation (H4): AIHC is associated with firm value both directly and indirectly through lower wage inequality, while the direct path remains positive after conditioning on WAGE
   Ctrl+F: „results indicate complementary partial mediation (H4): AIHC is“
   → Backs the coded partial-mediation condition (wage inequality channel) and confirms the direct path stays positive, so direction = positive, not conditional.

7. **conditions** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 45% word sequence
   > Moderation analyses show stronger AIHC and firm value associations in more dynamic and complex industries, whereas munificence shows no systematic moderating effect.
   Ctrl+F: „Moderation analyses show stronger AIHC and firm value“
   → Backs the coded condition 'stronger in dynamic/complex industries'.

8. **conditions** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > The coefficient is largest in Travel (0.018, t = 2.45), followed by Hospitality (0.012, t = 1.87) and Tourism (0.010, t = 1.66).
   Ctrl+F: „coefficient is largest in Travel (0.018, t = 2.45),“
   → Backs the coded sector split: firm-value effect strongest in travel.

9. **conditions, quality_notes** — p. 13 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 11% word sequence
   > AIHC is significantly negatively associated with WAGE in all sectors, again with varying magnitudes (see Appendix C, Table C8). The inequality compression association is strongest in Hospitality
   Ctrl+F: „associated with WAGE in all sectors, again with“
   → Backs the coded sector split (inequality compression strongest in hospitality) and the sectoral-heterogeneity quality note.

10. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Findings indicate that AIHC is positively associated with firm value, negatively associated with wage inequality, and that wage inequality is negatively associated with firm value.
   Ctrl+F: „that AIHC is positively associated with firm value,“
   → The paper's own central-result statement: AI human capital raises firm value partly via compressed wage inequality.

11. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study highlights workforce centered pathways for AI enabled competitive advantage.
   Ctrl+F: „The study highlights workforce centered pathways for AI“
   → Source of the coded 'workforce-centered pathway to AI-enabled advantage' wording; CA here is framing only, consistent with outcome_construct = performance.

12. **theoretical_lens, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Grounded in resource-based view and tournament theory, this study examines how AI human capital (AIHC) is associated with wage inequality and firm value in tourism, travel, and hospitality (TTH).
   Ctrl+F: „Grounded in resource-based view and tournament theory, this“
   → Abstract names RBV and tournament theory as the theoretical lenses and the TTH industry setting.

13. **quality_notes** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > we apply the Windmeijer finite-sample correction to adjust the downward bias in two-step standard errors
   Ctrl+F: „Windmeijer finite-sample correction to adjust the downward bias“
   → Source basis for the quality note 'GMM with Windmeijer correction'.

*Row check OK: ca_measure empty confirmed: competitive advantage appears only as framing/rhetoric (abstract, RBV theory talk), no distinct CA construct is measured - consistent with outcome_construct = performance. All non-empty columns evidenced.*

---

## S47 — Alnofeli K.K. et al. (2026) — International Journal of Information Management (AJG 2)

DOI: 10.1016/j.ijinfomgt.2025.102981 · status: final · PDF: `Alnofeli_2026_j-ijinfomgt-2025-102981.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Australia |
| sample | 3-stage: scoping review + expert interviews -> instrument; survey of 205 banking employees, SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI-powered CRM capability, higher-order) |
| *Table A.2 columns* | |
| outcome_construct | both |
| performance_measure | profitability (survey scale) |
| ca_measure | competitive advantage (survey scale) |
| effect_direction | positive |
| conditions | marketing ambidexterity (mediator: exploration/exploitation balance carries the effect) |
| key_finding | AI-CRM capability lifts profitability and competitive advantage through marketing ambidexterity - capability without ambidexterity closes the value-realisation gap only partially. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities (microfoundations) |
| industry | banking |
| quality_notes | Perceptual; instrument development study \| PROPOSED(batch): Scoping review + 24 expert interviews only IDENTIFY/CONFIRM construct dimensions (instrument development); hypotheses tested solely via survey n=205 (Kumar/Hossain class) |
| coding_status | final |

### Evidence

1. **country_region, sample, method, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Third, a survey of 205 banking employees in Australia tests the influence of AI-powered CRM capability on marketing ambidexterity and, in turn, on organisational outcomes.
   Ctrl+F: „Third, a survey of 205 banking employees in“
   → Stage 3 survey (n=205, Australian banking) is the sole test of the AI-outcome hypotheses, backing method = survey-SEM plus the coded sample, country, and industry.

2. **country_region, industry** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The study focuses on the major banking institutions in Australia, commonly referred to as the "big four" banks
   Ctrl+F: „The study focuses on the major banking institutions“
   → Confirms the banking industry and Australian setting.

3. **sample** — p. 3–5 (PDF p. 3) — ✓ verified, 100% word sequence
   > Finally, we conducted an empirical study (n = 205) to test the hypotheses and validate the research model.
   Ctrl+F: „an empirical study (n = 205) to test the“
   → Backs the coded 3-stage design with the n=205 hypothesis-testing survey.

4. **sample** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > the study conducted 24 in-depth interviews between January and March 2023
   Ctrl+F: „the study conducted 24 in-depth interviews between“
   → Backs the expert-interview stage (n=24) of the coded 3-stage sample description.

5. **method, quality_notes** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 52% word sequence
   > First, a systematic scoping review and in-depth interviews with industry experts identify the core dimensions and subdimensions of AI-powered CRM capability.
   Ctrl+F: „First, a systematic scoping review and in-depth interviews“
   → Stages 1-2 only identify construct dimensions (instrument development), so per the adjudicated decision the study is survey-SEM, not mixed; also backs the 'instrument development study' quality note.

6. **method** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > In this research, SmartPLS 4.0 was employed to analyse the survey data, thereby enabling the prediction of both measurement and structural models
   Ctrl+F: „employed to analyse the survey data, thereby enabling“
   → Confirms PLS-SEM as the analysis generating the AI-outcome evidence.

7. **ai_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study addresses this gap by conceptualising and empirically examining AI-powered CRM as a higher-order organisational capability.
   Ctrl+F: „study addresses this gap by conceptualising and empirically“
   → The AI measure is a higher-order AI-powered CRM capability survey construct.

8. **outcome_construct, ca_measure** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > CA3 Our market share expanded more quickly than our primary competitors after implementing AI-powered CRM systems.
   Ctrl+F: „CA3 Our market share expanded more quickly than“
   → Sample CA scale item is explicitly competitor-comparative, so a distinct CA construct is measured - justifying outcome_construct = both under the case law.

9. **outcome_construct, effect_direction** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > All the path coefficients are positive and statistically significant, thereby supporting hypotheses H4, H5, and H6.
   Ctrl+F: „and statistically significant, thereby supporting hypotheses H4, H5,“
   → Direct paths from AI-CRM capability to sustained profitability (H4) and sustained competitive advantage (H5) are significant and positive - mediated-positive with significant direct effects = positive.

10. **performance_measure, ca_measure** — p. 10 (PDF p. 10) — ✓ verified, 100% word sequence
   > the sustained profitability was measured by Vorhies and Morgan (2005), and the sustained competitive advantage was measured by Cao et al. (2019).
   Ctrl+F: „the sustained profitability was measured by Vorhies and“
   → Both outcomes use established survey scales: profitability (performance_measure) and a distinct competitive-advantage scale (ca_measure).

11. **conditions** — p. 15 (PDF p. 15) — ⚠ not machine-confirmed on page — open the page, 9% word sequence
   > The results further demonstrate that marketing ambidexterity serves as a significant partial mediator in the relationships between AI-powered CRM and sustained profitability, as well as between AI-powered CRM and sustained competitive advantage.
   Ctrl+F: „that marketing ambidexterity serves as a significant partial“
   → Backs the coded condition: marketing ambidexterity as mediator carrying part of the effect.

12. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The quantitative analysis confirms that AI-powered CRM capabilities positively shape marketing ambidexterity, which subsequently enhances profitability and competitive advantage.
   Ctrl+F: „The quantitative analysis confirms that AI-powered CRM capabilities“
   → The paper's own statement of its central result, matching the coded key finding.

13. **key_finding** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 22% word sequence
   > Practically, the study provides actionable guidance for managers seeking to close the 'value realisation gap' by cultivating AI-powered CRM systems as dynamic capabilities that balance exploration and exploitation in volatile markets.
   Ctrl+F: „seeking to close the “value realisation gap” by“
   → Source of the 'value-realisation gap' phrasing in the coded key finding.

14. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on the microfoundations of dynamic capability theory
   Ctrl+F: „Drawing on the microfoundations of dynamic capability theory,“
   → Abstract names microfoundations of dynamic capabilities as the theoretical lens.

15. **quality_notes** — p. 16 (PDF p. 16) — ✓ verified, 100% word sequence
   > We used cross-sectional study to measure managers' perceptions on these two aspects.
   Ctrl+F: „We used cross-sectional study to measure“
   → Authors' own limitation: both outcome constructs are perceptual manager ratings - backs the 'perceptual' quality note.

*Row check OK: Method dispute settled in adjudication_briefs.md (survey-SEM, Kumar/Hossain precedent) - full text confirms interviews only identify/confirm dimensions. The 'PROPOSED(batch)' portion of quality_notes is adjudication commentary, not source text; the source-based parts (perceptual outcomes, instrument development) are quoted. All non-empty columns evidenced.*

---

## S48 — Arshad F.M. et al. (2026) — International Journal of Information Management (AJG 2)

DOI: 10.1016/j.ijinfomgt.2026.103097 · status: final · PDF: `Arshad_2026_j-ijinfomgt-2026-103097.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | multi-country |
| sample | two survey datasets of large firms worldwide (RPA + AI implementation) |
| method | survey-based regression (two cross-sectional surveys) |
| ai_measure | survey (joint implementation of RPA and AI) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | revenue growth (via price increases); cost reduction tested |
| ca_measure | — |
| effect_direction | mixed |
| conditions | component split: joint RPA+AI -> additional REVENUE growth (via price increases), NO additional cost reduction (joint term n.s.; individual techs do reduce costs); strategic revenue-growth intent amplifies revenue outcomes |
| key_finding | Combining RPA and AI pays through revenue enhancement, not cost efficiency - and only for firms whose strategic intent targets growth. |
| *not printed (coding data only)* | |
| theoretical_lens | complementarity theory |
| industry | cross-industry (large firms) |
| quality_notes | Pre-GenAI baseline explicitly noted by authors \| PROPOSED(batch): Method verbatim per scheme rule (neither SEM nor panel): Study 1 = 2018 Deloitte survey n=1219 large firms worldwide + second survey; cross-sectional regressions |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study examines the firms' combined implementation of Robotic Process Automation (RPA) and Artificial Intelligence (AI) and its association with firm performance using two survey datasets covering large firms worldwide.
   Ctrl+F: „This study examines the firms’ combined implementation of“
   → Backs the coded sample (two survey datasets of large firms worldwide) and the survey-based method.

2. **country_region** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > the 2018 survey covers large firms in 24 countries, and the 2020 survey covers large firms in 14 (partially overlapping) countries.
   Ctrl+F: „survey covers large firms in 24 countries, and“
   → Backs country_region = multi-country (24 and 14 countries).

3. **sample, method** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > Study 1 is based on a 2018 survey of 1219 firms worldwide, capturing realized performance outcomes, while Study 2 uses a 2020 survey of 1053 firms, capturing expected performance outcomes.
   Ctrl+F: „Study 1 is based on a 2018 survey“
   → Details the two cross-sectional surveys (2018 n=1219, 2020 n=1053) behind the verbatim method coding.

4. **sample, industry** — p. 12 (PDF p. 12) — ⚠ not machine-confirmed on page — open the page, 26% word sequence
   > Similar to Study 1, the sampling criteria and data collection result in representativeness of the data and statistical results relating to large firms, across a wide range of industries and a range of countries.
   Ctrl+F: „Similar to Study 1, the sampling criteria and“
   → Backs industry = cross-industry (large firms) across a wide range of industries.

5. **method** — p. 17 (PDF p. 17) — ✓ verified, 95% word sequence
   > The cross-sectional character of our datasets is another limitation that restricts causal inference and raises the possibility of reverse causality
   Ctrl+F: „The cross-sectional character of our datasets is another“
   → Authors confirm both surveys are cross-sectional, backing the verbatim method 'survey-based regression (two cross-sectional surveys)'.

6. **ai_measure** — p. 9 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 44% word sequence
   > We operationalize joint implementation of RPA and AI as an interaction term RPA × AI, denoted as RPA_AI_Joint. This indicator is coded 1 when both technologies are implemented and 0 otherwise.
   Ctrl+F: „We operationalize joint implementation of RPA and AI“
   → Backs the AI measure: survey indicator of joint RPA and AI implementation.

7. **outcome_construct, performance_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > We focus on two key firm-level performance dimensions: efficiency-related outcomes, measured as cost reduction, and market-facing outcomes, measured as revenue growth.
   Ctrl+F: „performance dimensions: efficiency-related outcomes, measured as cost“
   → Outcomes are performance dimensions (cost reduction, revenue growth); no distinct CA construct measured.

8. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 45% word sequence
   > We find that joint implementation is positively associated with additional revenue growth (linked primarily to price increases) but is not associated with additional cost reduction beyond the separate effects of RPA and AI.
   Ctrl+F: „We find that joint implementation is positively associated“
   → The sign splits across outcome components (revenue positive, cost null) - the component split backing effect_direction = mixed and the coded conditions.

9. **effect_direction, conditions** — p. 11 (PDF p. 11) — ✓ verified, 76% word sequence
   > Thus, while each technology is independently associated with cost reduction, their joint implementation is not associated with additional cost reduction. Accordingly, H1 is not supported.
   Ctrl+F: „Thus, while each technology is independently associated with“
   → Backs the null cost-reduction component (joint term n.s.) while individual technologies do reduce costs, as coded in conditions.

10. **effect_direction** — p. 11 (PDF p. 11) — ✓ verified, 85% word sequence
   > joint implementation of RPA and AI, represented by RPA_AI_Joint, is positively associated with revenue growth (p = 0.049).
   Ctrl+F: „and AI, represented by RPA_AI_Joint, is positively associated“
   → Backs the positive revenue-growth component of the mixed direction.

11. **conditions** — p. 11 (PDF p. 11) — ✓ verified, 92% word sequence
   > The coefficient on RPA_AI_Joint is positive and significant for price change (p = 0.017), while it is not statistically significant for volume change.
   Ctrl+F: „significant for price change (p = 0.017), while it“
   → Backs the coded 'via price increases' channel of the revenue effect.

12. **conditions** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > However, among firms that have implemented both RPA and AI (column 6), a stronger revenue growth intent is positively associated with realized revenue growth (p = 0.049).
   Ctrl+F: „a stronger revenue growth intent is positively associated“
   → Backs the coded condition that strategic revenue-growth intent amplifies revenue outcomes.

13. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 96% word sequence
   > These findings challenge the prevailing view that combining RPA and AI technologies primarily enhances performance through increased efficiency, suggesting instead that joint implementation is associated with revenue enhancement.
   Ctrl+F: „These findings challenge the prevailing view that combining“
   → The paper's own central-result statement: combination pays through revenue enhancement, not cost efficiency.

14. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > we draw on complementarity theory to hypothesize that their joint implementation is associated with performance outcomes that exceed the independent benefits of each technology.
   Ctrl+F: „we draw on complementarity theory to hypothesize that“
   → Abstract names complementarity theory as the theoretical lens.

15. **quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Our findings provide a baseline analysis of automation complementarities in the pre-Generative-AI era, even as advancements in technology continue and raise new questions.
   Ctrl+F: „Our findings provide a baseline analysis of automation“
   → Authors explicitly note the pre-GenAI baseline, as recorded in quality_notes.

*Row check OK: Method and direction were adjudicated (briefs: verbatim method per scheme rule; mixed per S31/S36 component-split precedent) - full text confirms both. ca_measure empty confirmed: competitive advantage appears only as RBV framing in the introduction, no CA construct measured. The 'PROPOSED(batch)' portion of quality_notes is adjudication commentary; the source-based part (pre-GenAI baseline) is quoted.*

---

## S49 — Bai X. et al. (2026) — Pacific Basin Finance Journal (AJG 2)

DOI: 10.1016/j.pacfin.2025.103039 · status: final · PDF: `Bai_2026_j-pacfin-2025-103039.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | Chinese A-share listed firms; quasi-natural experiment (New-generation AI Pilot Zone Policy); pre-registered |
| method | panel econometrics |
| ai_measure | policy shock (AI pilot zone exposure) as exogenous AI investment driver |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | stock price crash risk (up) + firm value (up) |
| ca_measure | — |
| effect_direction | mixed |
| conditions | crash risk rises via reduced information transparency + managerial optimism; worse for low-transparency and resource-constrained firms; firm value gains may be short-term market optimism |
| key_finding | Policy-driven AI investment inflates firm value but simultaneously raises crash risk - short-term valuation gains trade off against long-term stability. |
| *not printed (coding data only)* | |
| theoretical_lens | information asymmetry / behavioral finance |
| industry | cross-industry (listed firms) |
| quality_notes | Pre-registered + quasi-experiment (highest identification quality in corpus) |
| coding_status | final |

### Evidence

1. **country_region, sample, ai_measure, effect_direction** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using China's 'New-generation Artificial Intelligence Polit Zone Policy' as a quasi-natural experiment, we find robust evidence that AI investment significantly increases firms' stock price crash risk
   Ctrl+F: „Using China’s “New-generation Artificial Intelligence Polit Zone Policy”“
   → Backs the quasi-natural experiment design, the China setting, the policy-shock AI measure, and the crash-risk-increasing component of the mixed direction ('Polit' is the paper's own typo).

2. **sample, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This pre-registered study executes the empirical design approved in the associated pre-registered report (Bai and Zhao, 2025) to investigate the impact of artificial intelligence (AI) investment on stock price crash risk.
   Ctrl+F: „This pre-registered study executes the empirical design approved“
   → Confirms the pre-registered design noted in sample and quality_notes.

3. **sample** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > our treatment group consists of firms headquartered in cities that located in AI pilot zones, while firms in non-pilot cities serve as the control group.
   Ctrl+F: „our treatment group consists of firms headquartered in“
   → Details the quasi-experimental treatment/control construction in the coded sample.

4. **sample** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > The sample period ranges from 2011 to 2024.
   Ctrl+F: „The sample period ranges from 2011 to 2024.“
   → Sample window of the Chinese firm panel.

5. **method, performance_measure** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > we employ a DID model based on the 'New-generation Artificial Intelligence Pilot Zone' policy launched by the Chinese government, to investigate the impact of AI investment on stock price crash risk and firm value.
   Ctrl+F: „we employ a DID model based on the“
   → Confirms panel-econometric DID method and the two outcomes (crash risk, firm value).

6. **method, industry** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > we incorporate year, industry and city levels of fixed effects to control unobserved factors that might influence our results. Standard errors are clustered at the firm level.
   Ctrl+F: „levels of fixed effects to control unobserved factors“
   → Panel-econometric specification; industry fixed effects across 25,746 firm-years indicate a cross-industry listed-firm sample.

7. **ai_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > Its staggered rollout across regions and over time introduces exogenous variation in firms' AI exposure, enabling a more credible identification of the causal effects of AI investment on firm-level outcomes
   Ctrl+F: „Its staggered rollout across regions and over time“
   → Backs the AI measure: pilot-zone policy exposure as exogenous driver of AI investment.

8. **outcome_construct, performance_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > we measure stock price crash risk by the negative skewness of weekly stock returns ( NCSKEW ) and the down-to-up volatility ratio ( DUVOL ), both calculated on a yearly basis.
   Ctrl+F: „we measure stock price crash risk by the“
   → Defines the crash-risk performance measure; no CA construct is measured.

9. **outcome_construct, performance_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > use the market-to-book ratio and Tobin's Q as proxies for firm value.
   Ctrl+F: „use the market-to-book ratio and Tobin’s Q as“
   → Defines the firm-value performance measure.

10. **performance_measure, effect_direction** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > The coefficients on Treat × Post are positive and statistically significant across all specifications for both NCSKEW and DUVOL.
   Ctrl+F: „are positive and statistically significant across all specifications“
   → Crash risk rises (adverse component of the mixed direction).

11. **performance_measure, effect_direction** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > we estimate Eq. (7) and find that the coefficients of Treat × Post are significantly positive at the 1 % level, indicating that firm value increases following the pilot AI-zone policy.
   Ctrl+F: „we estimate Eq. (7) and find that the“
   → Firm value rises (favorable component) - the valence split across the two outcomes backs effect_direction = mixed.

12. **conditions** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > These findings support the hypothesis that AI investment increases stock price crash risk by reducing information transparency.
   Ctrl+F: „These findings support the hypothesis that AI investment“
   → Backs the coded mechanism: crash risk rises via reduced information transparency.

13. **conditions** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > These results indicate that heightened managerial optimism acts as an important transmission channel through which AI investment contributes to increased stock price crash risk.
   Ctrl+F: „optimism acts as an important transmission channel through“
   → Backs the coded managerial-optimism channel.

14. **conditions** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > Cross-sectional analyses further reveal that the positive effect of AI investment on crash risk is more pronounced among firms with lower information transparency and tighter resource constraints.
   Ctrl+F: „positive effect of AI investment on crash risk“
   → Backs the coded moderators: worse for low-transparency and resource-constrained firms.

15. **conditions, key_finding** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > These findings suggest an environment of excessive optimism, where the market initially overreacts to the perceived benefits of AI adoption, thereby inflating firm valuations.
   Ctrl+F: „These findings suggest an environment of excessive optimism,“
   → Backs the coded caveat that firm-value gains may reflect short-term market optimism.

16. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 92% word sequence
   > Furthermore, we also find the policy boosts firm value, suggesting that market optimism may drive short-term valuation gains at the cost of longterm stability.
   Ctrl+F: „Furthermore, we also find the policy boosts firm“
   → The paper's own statement of the central trade-off in the coded key finding ('longterm' is an extraction line-merge of 'long-term').

17. **key_finding** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > the coexistence of short-term valuation gains and long-term crash risk points to an important trade-off for investors and regulators.
   Ctrl+F: „short-term valuation gains and long-term crash risk points“
   → Conclusion restates the coded trade-off between valuation gains and long-term stability.

18. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > the uncertainty and complexity of AI projects may amplify managerial optimism and information asymmetry, encouraging managers to withhold unfavorable information and increasing the likelihood of crashes
   Ctrl+F: „the uncertainty and complexity of AI projects may“
   → The paper's framing rests on information asymmetry and managerial optimism (behavioral finance), matching the coded lens.

**⚠ ROW CHECK:** One sample detail could not be evidenced from this document: 'A-share listed firms' is never stated verbatim in the executed paper - the data section defers to the pre-registered report (Bai and Zhao, 2025) for full sample details; the loaded text gives 25,746 firm-year observations, 2011-2024, Chinese firms in/outside AI pilot zones. Also, industry = 'cross-industry (listed firms)' is supported only indirectly (industry fixed effects over the full firm panel). The '(highest identification quality in corpus)' part of quality_notes is coder commentary; the source-based parts (pre-registered, quasi-experiment) are quoted. ca_measure empty confirmed - no CA construct anywhere in the paper.

---

## S50 — Chen S.S. et al. (2026) — Journal of Empirical Finance (AJG 3)

DOI: 10.1016/j.jempfin.2026.101730 · status: final · PDF: `Chen_2026_j-jempfin-2026-101730.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | US firms; AI mentions in earnings calls, validated vs 10-K; IV = textual proximity to university AI research; 2SLS |
| method | panel econometrics |
| ai_measure | earnings-call text (share of AI terminology in management remarks) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | corporate investment efficiency; Tobins q (long horizon) |
| ca_measure | — |
| effect_direction | positive |
| conditions | mechanisms: better sales forecasts, reporting quality, process/product innovation; data-privacy regulation exposure ATTENUATES the effect |
| key_finding | AI adoption improves how firms allocate capital - unless regulatory friction (data-privacy exposure) blunts it; value shows up in Tobins q only over longer horizons. |
| *not printed (coding data only)* | |
| theoretical_lens | corporate finance (investment efficiency) |
| industry | cross-industry |
| quality_notes | IV design; regulation as boundary condition |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 2 (PDF p. 2) — ✓ verified, 70% word sequence
   > Using a sample of 16,145 firm-year observations for 2401 U.S. firms from the StreetEvents -Compustat -CRSP universe over 2010 -2021
   Ctrl+F: „Using a sample of 16,145 firm-year observations for“
   → Quantifies the US firm panel backing sample and country codes.

2. **sample, ai_measure** — p. 1 (PDF p. 1) — ✓ verified, 63% word sequence
   > and validate this measure by showing that it is positively associated with 10-K discussions of AI applications in operational decision-making, product development, and business expansion
   Ctrl+F: „validate this measure by showing that it is“
   → Backs the 'validated vs 10-K' element of the coded sample description.

3. **sample, method, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We construct an instrumental variable based on exposure to university-authored AI research -measured as a normalized score of textual similarity between non-corporate academic publications and industry descriptions
   Ctrl+F: „construct an instrumental variable based on exposure to“
   → Backs 'IV = textual proximity to university AI research; 2SLS' in the sample coding and the 'IV design' quality note.

4. **method** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > All regressions include firm and year fixed effects.
   Ctrl+F: „All regressions include firm and year fixed effects.“
   → Firm-year panel regressions with two-way fixed effects (plus 2SLS) back method = panel econometrics.

5. **ai_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We measure AI adoption using AI mentions , defined as the proportion of AI-related terminology in senior management remarks during earnings calls
   Ctrl+F: „We measure AI adoption using AI mentions, defined“
   → Exactly the coded AI measure: share of AI terminology in management earnings-call remarks.

6. **outcome_construct, performance_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > We measure investment efficiency following Biddle et al. (2009), a specification widely used in empirical studies of corporate investment decisions
   Ctrl+F: „We measure investment efficiency following Biddle et al.“
   → Backs 'corporate investment efficiency' as the coded performance measure (deviation of actual from predicted investment).

7. **performance_measure, effect_direction, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We also find that firms with higher AI mentions tend to have higher Tobin ' s q over longer horizons, consistent with a gradual reflection of AI-related benefits in firm value.
   Ctrl+F: „firms with higher AI mentions tend to have“
   → Backs the coded 'Tobins q (long horizon)' performance measure and the key-finding phrase that value shows up only over longer horizons.

8. **effect_direction, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Our baseline results indicate that higher AI adoption is associated with greater investment efficiency
   Ctrl+F: „AI adoption is associated with greater investment efficiency,“
   → Positive main association (holding in 2SLS with the exposure instrument) backs effect_direction = positive.

9. **conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Additional analyses suggest several mechanisms: AI adoption is associated with more accurate management sales forecasts, higher financial reporting quality, and greater process and product innovation intensity.
   Ctrl+F: „mechanisms: AI adoption is associated with more accurate“
   → The three empirically tested channels back the coded mechanism conditions (sales forecasts, reporting quality, process/product innovation).

10. **conditions, key_finding, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Cross-sectional evidence further indicates that regulatory frictions, such as exposure to data-privacy regulation, attenuate the association between AI adoption and investment efficiency.
   Ctrl+F: „evidence further indicates that regulatory frictions, such as“
   → Backs the coded condition 'data-privacy regulation exposure ATTENUATES the effect' and the 'regulation as boundary condition' quality note (GDPR difference-in-differences, Table 9).

11. **key_finding** — p. 19 (PDF p. 19) — ✓ verified, 100% word sequence
   > Overall, the evidence suggests that AI adoption is an increasingly relevant factor in how firms allocate capital, as reflected in investment efficiency.
   Ctrl+F: „Overall, the evidence suggests that AI adoption is“
   → The paper's own concluding statement backs the coded key finding on capital allocation.

12. **theoretical_lens** — p. 2 (PDF p. 2) — ✓ verified, 64% word sequence
   > Classic theories link information asymmetry and agency conflicts to deviations from optimal investment, while richer information environments help align financing and investment with underlying fundamentals
   Ctrl+F: „Classic theories link information asymmetry and agency conflicts“
   → The study is grounded in corporate-finance theory of investment efficiency (information asymmetry, agency conflicts), as coded.

13. **industry** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > we also exclude 4587 firm-year observations in AI-innovating industries (North American Industry Classification System (NAICS) codes 51 and 54) to focus on firms that primarily use AI rather than develop AI technologies
   Ctrl+F: „exclude 4587 firm-year observations in AI-innovating industries (North“
   → The sample spans all industries except financials, utilities and AI-producing sectors, backing the cross-industry coding.

14. **quality_notes** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > we interpret them with caution given the untestability of the exclusion restriction
   Ctrl+F: „we interpret them with caution given the untestability“
   → Authors' own caveat on the IV design backs the 'IV design' quality note as source-based.

*Row check OK: ca_measure empty is correct: no competitive-advantage construct is measured; outcomes are investment efficiency, Tobin's q, and (weaker) stock returns. Context for the author: the baseline OLS coefficient on AI mentions is significant only at the 10% level (t about 1.73-1.78), while the 2SLS estimate is significant at 5% - direction positive throughout. The coded 'mechanisms' conditions are empirically tested channels (Tables 5-7), not narrative-only. Not in adjudication_briefs.md.*

---

## S51 — Dinh V.H. (2026) — Industrial Marketing Management (AJG 3)

DOI: 10.1016/j.indmarman.2026.01.006 · status: final · PDF: `Dinh_2026_j-indmarman-2026-01-006.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Vietnam (emerging markets) |
| sample | sequential mixed-methods, 261 manufacturing SMEs |
| method | mixed |
| ai_measure | survey construct (AI-enabled knowledge capabilities) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | new product performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | dual pathway: direct + via digital product innovation radicalness; digital sustainability leadership as BOTH mediator and moderator (reconfigures how AI creates value) |
| key_finding | AI knowledge capabilities lift new product performance in emerging-market SMEs, with digital sustainability leadership as the critical boundary condition. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities + KBV |
| industry | manufacturing SMEs |
| quality_notes | Perceptual, mixed methods |
| coding_status | final |

### Evidence

1. **country_region, industry** — p. 84 (PDF p. 1) — ✓ verified, 68% word sequence
   > Emerging market manufacturing small and medium-sized enterprises (SMEs) struggle to translate artificial intelligence (AI) investments into innovation outcomes.
   Ctrl+F: „Emerging market manufacturing small and medium-sized enterprises (SMEs)“
   → Backs 'manufacturing SMEs' as industry and the '(emerging markets)' element of the country code.

2. **country_region, sample, industry** — p. 96 (PDF p. 13) — ✓ verified, 100% word sequence
   > This study collected data from manufacturing SMEs in Viet Nam through the Keieijuku Vietnam Community to evaluate our conceptual model.
   Ctrl+F: „This study collected data from manufacturing SMEs in“
   → Backs country_region = Vietnam and the manufacturing-SME population of the quantitative study.

3. **sample, method, industry** — p. 84 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 57% word sequence
   > This study investigates how AI-enabled knowledge capabilities drive new product performance by employing a sequential mixed-methods design with 261 manufacturing SMEs.
   Ctrl+F: „drive new product performance by employing a sequential“
   → Backs method = mixed and the coded sample 'sequential mixed-methods, 261 manufacturing SMEs'.

4. **sample, method** — p. 97 (PDF p. 14) — ✓ verified, 100% word sequence
   > The data collection process concluded with 261 valid responses across all three waves.
   Ctrl+F: „The data collection process concluded with 261 valid“
   → Confirms n = 261 from a time-lagged three-wave survey (Study 2).

5. **method** — p. 87 (PDF p. 4) — ✓ verified, 100% word sequence
   > We conducted comprehensive semi-structured interviews with sixteen manufacturing SME managers
   Ctrl+F: „We conducted comprehensive semi-structured interviews with“
   → The qualitative strand (Study 1) that makes the design mixed; its findings also corroborate the hypotheses in the discussion (interviewee quotes I3, I6, I15).

6. **ai_measure** — p. 97 (PDF p. 14) — ✓ verified, 100% word sequence
   > AI-enabled knowledge capabilities were assessed using an eight-item scale from Abou-Foul et al. (2023)
   Ctrl+F: „AI-enabled knowledge capabilities were assessed using an eight-item“
   → Backs ai_measure = survey construct (AI-enabled knowledge capabilities).

7. **outcome_construct, performance_measure** — p. 97 (PDF p. 14) — ✓ verified, 100% word sequence
   > New product performance employed a four-item scale from Story et al. (2015)
   Ctrl+F: „New product performance employed a four-item scale from“
   → Backs performance_measure = new product performance (survey scale).

8. **outcome_construct, performance_measure** — p. 97 (PDF p. 14) — ✓ verified, 100% word sequence
   > assessing market success, competitive advantage, and profitability
   Ctrl+F: „assessing market success, competitive advantage,“
   → The NPP scale includes a competitive-advantage facet, but no distinct CA construct with its own hypothesis is measured - confirming outcome_construct = performance and the empty ca_measure under the frozen CA rule.

9. **effect_direction** — p. 98 (PDF p. 15) — ✓ verified, 72% word sequence
   > H1 receives strong empirical support, revealing that AI-enabled knowledge capabilities significantly enhance new product performance ( β = 0.39, t = 6.78, p < 0.001).
   Ctrl+F: „H1 receives strong empirical support, revealing that AI-enabled“
   → Significant positive DIRECT effect alongside the mediation - a mediated-positive effect with significant direct path = positive under the frozen direction rule.

10. **effect_direction, conditions, key_finding** — p. 84 (PDF p. 1) — ✓ verified, 100% word sequence
   > Our findings reveal that AI-enabled knowledge capabilities operate through dual pathways: directly enhancing performance and indirectly through digital product innovation radicalness.
   Ctrl+F: „Our findings reveal that AI-enabled knowledge capabilities operate“
   → The paper's own result statement backs the coded 'dual pathway: direct + via digital product innovation radicalness'.

11. **conditions, key_finding** — p. 84 (PDF p. 1) — ✓ verified, 100% word sequence
   > this study identifies digital sustainability leadership as a critical boundary condition acting as both mediator and moderator, fundamentally reconfiguring how AI generates value
   Ctrl+F: „study identifies digital sustainability leadership as a critical“
   → Backs the coded condition 'digital sustainability leadership as BOTH mediator and moderator (reconfigures how AI creates value)'; H4 moderation is significant (beta = 0.07, p < 0.05, p. 15).

12. **conditions** — p. 98 (PDF p. 15) — ✓ verified, 88% word sequence
   > H2 is validated through mediation analysis, demonstrating that digital product innovation radicalness mediates the relationship between AI-enabled knowledge capabilities and new product performance.
   Ctrl+F: „H2 is validated through mediation analysis, demonstrating that“
   → Results-section grounding for the coded mediation pathway.

13. **theoretical_lens** — p. 84–85 (PDF p. 1) — ✓ verified, 100% word sequence
   > this study grounds itself in dynamic capabilities theory and the knowledge-based view
   Ctrl+F: „dynamic capabilities theory and the knowledge-based view.“
   → Backs the coded lens 'dynamic capabilities + KBV'.

14. **quality_notes** — p. 97 (PDF p. 14) — ✓ verified, 100% word sequence
   > All items were measured on five-point Likert scales ranging from 1 (strongly disagree) to 5 (strongly agree)
   Ctrl+F: „All items were measured on five-point Likert scales“
   → Self-reported Likert measurement backs 'Perceptual'; the sequential-design quotes back 'mixed methods'.

*Row check OK: ca_measure empty is correct: 'competitive advantage' appears as framing and as one facet inside the Story et al. NPP scale, but no distinct CA construct with its own hypothesis is measured (frozen rule 1 -> performance). Method note: Study 1 interviews built the conceptual model while Study 2 (PLS-SEM + PROCESS + fsQCA) carries the statistical outcome evidence; the discussion additionally uses qualitative evidence to corroborate H1-H4, consistent with the final 'mixed' coding. Minor curiosity: the limitations section calls the design 'cross-sectional' although data collection was time-lagged across three waves - authors' own wording, no effect on coded values. Not in adjudication_briefs.md.*

---

## S52 — Filieri R. et al. (2026) — Journal of Product Innovation Management (AJG 4)

DOI: 10.1111/jpim.70014 · status: final · PDF: `Filieri_2026_jpim-70014.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | Chinese listed manufacturers + WTO tariff records + customs data 2015-2022; IV analysis |
| method | panel econometrics |
| ai_measure | archival AI integration measure (tariff-induced) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | supply chain efficiency, sales performance, market value |
| ca_measure | — |
| effect_direction | conditional |
| conditions | INVERTED U: AI performance benefits diminish at extreme tariff exposure ("optimal investment threshold"); customer engagement needs strengthen the effect (boundary condition); tariff exposure induces AI integration |
| key_finding | Trade tensions push firms into AI integration that improves efficiency, sales and value - up to a threshold where adversity overwhelms the compensation. |
| *not printed (coding data only)* | |
| theoretical_lens | adversity-induced innovation theory (extended induced innovation) + stakeholder engagement |
| industry | manufacturing (exporters) |
| quality_notes | Causal (IV); geopolitics as condition - distinctive for discussion \| PROPOSED(batch): S26 precedent: inverted-U = sign/size flip along adversity level -> conditional |
| coding_status | final |

### Evidence

1. **country_region, sample, theoretical_lens, industry** — p. 57 (PDF p. 1) — ✓ verified, 100% word sequence
   > We reconceptualize induced innovation theory as adversity-induced innovation theory and test hypotheses using data from listed Chinese manufacturing firms, WTO tariff records, and customs data (2015-2022).
   Ctrl+F: „innovation theory and test hypotheses using data from“
   → Abstract names the extended induced-innovation lens and the exact sample composition (Chinese listed manufacturers, WTO tariff records, customs data 2015-2022) coded in sample/country/industry.

2. **country_region, sample, industry** — p. 60 (PDF p. 4) — ✓ verified, 100% word sequence
   > This study uses a large sample of manufacturing firms listed on China's Shanghai and Shenzhen stock exchanges from 2015 to 2022.
   Ctrl+F: „This study uses a large sample of manufacturing“
   → Methodology section confirms Chinese listed manufacturers over 2015-2022 as coded.

3. **method, quality_notes** — p. 57 (PDF p. 1) — ✓ verified, 100% word sequence
   > We establish causal relationships between tariff-induced AI integration and firm performance through instrumental variable analysis and robustness checks.
   Ctrl+F: „AI integration and firm performance through instrumental variable“
   → Documents the IV identification strategy behind the coded 'IV analysis' in sample and the 'Causal (IV)' quality note.

4. **method** — p. 63 (PDF p. 7) — ⚠ not machine-confirmed on page — open the page, 38% word sequence
   > For hypothesis testing, we apply the following OLS regression model to examine the effect of firm tariff exposure on AI integration
   Ctrl+F: „For hypothesis testing, we apply the following OLS“
   → Regression models on firm-year panel data with year and industry fixed effects back the 'panel econometrics' method code.

5. **method, performance_measure** — p. 66 (PDF p. 10) — ✓ verified, 100% word sequence
   > employ a series of firm performance measures that capture supply chain efficiency, sales performance, and valuation as the dependent variable
   Ctrl+F: „series of firm performance measures that capture supply“
   → Results section operationalizes the coded performance measures (supply chain efficiency, sales, Tobin's Q as valuation) within OLS panel models.

6. **ai_measure** — p. 62 (PDF p. 6) — ✓ verified, 64% word sequence
   > We utilize the CSMAR database on firm digital transformation to construct an index measure for firm AI integration, extracting both quantitative indicators and textual information from annual reports.
   Ctrl+F: „We utilize the CSMAR database on firm digital“
   → Shows the AI measure is an archival annual-report-based AI integration index, matching 'archival AI integration measure'.

7. **ai_measure, key_finding** — p. 65 (PDF p. 9) — ✓ verified, 100% word sequence
   > suggesting that firms exposed more to the trade war are more involved in AI integration
   Ctrl+F: „firms exposed more to the trade war are“
   → H1 result showing AI integration is tariff-induced, backing the '(tariff-induced)' qualifier in ai_measure and the induction half of the key finding.

8. **outcome_construct, performance_measure, key_finding** — p. 57 (PDF p. 1) — ✓ verified, 100% word sequence
   > AI integration improves supply chain efficiency, sales performance, and market value.
   Ctrl+F: „AI integration improves supply chain efficiency, sales performance,“
   → Names the three coded performance outcomes; all are performance constructs, supporting outcome_construct = performance.

9. **effect_direction, conditions** — p. 57 (PDF p. 1) — ✓ verified, 100% word sequence
   > However, performance benefits follow an inverted U-shape: extreme tariff exposure diminishes AI's compensatory effects.
   Ctrl+F: „However, performance benefits follow an inverted“
   → The inverted-U sign flip along tariff exposure is the basis for effect_direction = conditional (S26 precedent) and the coded INVERTED U condition.

10. **effect_direction, conditions** — p. 69 (PDF p. 13) — ✓ verified, 100% word sequence
   > This finding suggests the existence of an optimal level of AI investment relative to tariff exposure, beyond which additional AI integration cannot fully offset the adverse effects of extreme tariff exposure.
   Ctrl+F: „the existence of an optimal level of AI“
   → Quadratic Tobin's Q result stating the 'optimal investment threshold' recorded in conditions and grounding the conditional direction.

11. **effect_direction, key_finding** — p. 70 (PDF p. 14) — ✓ verified, 100% word sequence
   > AI integration improves firm performance up to an optimal threshold beyond which extreme tariff exposure overwhelms technological adaptation
   Ctrl+F: „AI integration improves firm performance up to an“
   → Paper's own summary of the central result: benefits up to a threshold where adversity overwhelms compensation — the key_finding's second half and the conditional direction.

12. **conditions, theoretical_lens** — p. 57 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study extends induced innovation theory to geopolitical adversities and advances stakeholder engagement theory by identifying customer engagement as a boundary condition for technology adoption.
   Ctrl+F: „The study extends induced innovation theory to geopolitical“
   → Backs the second lens component (stakeholder engagement) and the coded customer-engagement boundary condition.

13. **conditions** — p. 71 (PDF p. 15) — ✓ verified, 100% word sequence
   > Firms with higher customer engagement needs (measured through overseas sales, asset specificity, and customer concentration) respond more strongly to tariff exposure through AI integration.
   Ctrl+F: „respond more strongly to tariff exposure through AI“
   → Backs the coded condition that customer engagement needs strengthen the tariff-to-AI response, including its three proxies.

14. **conditions, key_finding** — p. 57 (PDF p. 1) — ✓ verified, 100% word sequence
   > Results indicate that higher tariff exposure increases AI integration, particularly among firms with stronger customer engagement needs.
   Ctrl+F: „Results indicate that higher tariff exposure increases AI“
   → Abstract statement of the induction result plus the engagement boundary condition, matching the key_finding's first half.

*Row check OK: ca_measure empty is correct: 'competitive advantage' appears only as rhetoric (managerial summary: 'turn geopolitical adversity into a competitive advantage'), no CA construct is measured — performance coding per case law. In quality_notes, 'Causal (IV)' is source-backed (see IV quote); 'geopolitics as condition - distinctive for discussion' is coder commentary, not evidenced from the paper.*

---

## S53 — Giordino D. et al. (2026) — Technological Forecasting and Social Change (AJG 3)

DOI: 10.1016/j.techfore.2025.124499 · status: final · PDF: `Giordino_2026_j-techfore-2025-124499.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Europe |
| sample | balanced panel, 432 European listed companies 2015-2023 (LSEG data), banks/insurers excluded |
| method | panel econometrics |
| ai_measure | organizational AI focus (archival, LSEG-based) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | ROA + Tobins Q (+ ESG pillar scores) |
| ca_measure | — |
| effect_direction | positive |
| conditions | — |
| key_finding | Organizational AI focus goes hand in hand with better financial performance AND better E/S sustainability scores in European listed firms. |
| *not printed (coding data only)* | |
| theoretical_lens | economic theory framework |
| industry | cross-industry (non-financial) |
| quality_notes | Association study (no causal identification claimed) \| PROPOSED(batch): No moderators/heterogeneity tested; E+S pillar gains and governance-null belong to performance_measure/key_finding (S09/S12 precedent -> unconditional-evidence group) |
| coding_status | final |

### Evidence

1. **country_region, sample** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This manuscript relies on observations from a balanced panel of data comprising 432 publicly listed companies headquartered in Europe.
   Ctrl+F: „balanced panel of data comprising 432 publicly listed“
   → Confirms balanced panel, n = 432 European listed companies as coded in sample and country_region.

2. **sample, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The sample excludes banks and insurance companies, given their distinct accounting, governance, and capital structure standards.
   Ctrl+F: „banks and insurance companies, given their distinct accounting,“
   → Backs the 'banks/insurers excluded' sample detail and the '(non-financial)' qualifier in industry.

3. **sample** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The sample consists of observations spanning from 2015 to 2023. Observations are gathered from LSEG Data & Analytics.
   Ctrl+F: „sample consists of observations spanning from 2015 to“
   → Confirms the 2015-2023 window and LSEG as the data source coded in sample.

4. **method** — p. 5 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 53% word sequence
   > We employ fixed-effects panel regressions because they are particularly well-suited for quantitative studies estimating relationships among variables
   Ctrl+F: „We employ fixed-effects panel regressions because they are“
   → Methodology section states fixed-effects panel regressions, backing method = panel econometrics.

5. **ai_measure** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > the authors constructed the AI focus variable by analyzing firms' textual disclosures and identifying the occurrence of 122 terms associated with AI
   Ctrl+F: „authors constructed the AI focus variable by analyzing“
   → Shows the 'organizational AI focus' measure is archival, built from corporate disclosure texts (LSEG-sourced data), as coded.

6. **ai_measure, quality_notes** — p. 14 (PDF p. 14) — ✓ verified, 100% word sequence
   > the constructed AI variable presents certain limitations, as it relies on data derived from organizations' narrative disclosures
   Ctrl+F: „the constructed AI variable presents certain limitations, as“
   → Authors' own limitation on the disclosure-based AI measure, a source-based quality caveat.

7. **outcome_construct, performance_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Furthermore, this study examines the relationship between organizations' AI focus and financial performance, measured by return on assets (ROA) and Tobin's Q.
   Ctrl+F: „Furthermore, this study examines the relationship between organizations'“
   → Names ROA and Tobin's Q as the financial performance measures; all outcomes are performance constructs, supporting outcome_construct = performance.

8. **performance_measure** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study examines the link between organizations' focus on AI and their environmental, social, and governance (ESG) score.
   Ctrl+F: „This study examines the link between organizations' focus“
   → Backs the '(+ ESG pillar scores)' component of the coded performance_measure.

9. **performance_measure, effect_direction, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The empirical findings indicate: I) a positive and significant association between organizations' AI focus and their environmental (b = 0.127***; p = 0.001) and social pillar scores (b = 0.072**; p = 0.023)
   Ctrl+F: „The empirical findings indicate: I) a positive and“
   → Positive significant E/S pillar results; the paper's own 'association' wording backs the quality note that no causal identification is claimed.

10. **performance_measure, effect_direction** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > II) a positive and significant link with financial performance (ROA: b = 0.094**; p = 0.012; TobinQ: 0.103*; p = 0.051)
   Ctrl+F: „positive and significant link with financial performance (ROA:“
   → Positive significant main effects on both financial performance measures, backing effect_direction = positive.

11. **performance_measure, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > III) a positive but statistically insignificant relationship with governance pillar scores (b = 0.030; p = 0.166)
   Ctrl+F: „III) a positive but statistically insignificant relationship with“
   → The governance null is an outcome description (per adjudication it belongs to performance_measure/key_finding, not conditions).

12. **effect_direction, key_finding** — p. 13 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 55% word sequence
   > the obtained results indicate a positive and significant relationship between firms' AI focus and their financial performance (expressed as ROA and Tobin's Q) and their environmental and social sustainability performance
   Ctrl+F: „the obtained results indicate a positive and significant“
   → Conclusion's own summary of the central result: AI focus with better financial AND E/S sustainability performance, matching the coded key_finding.

13. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The present manuscript is grounded in the economic theory framework.
   Ctrl+F: „The present manuscript is grounded in the economic“
   → Abstract names economic theory as the study's theoretical underpinning, matching the coded lens verbatim.

*Row check OK: conditions empty confirmed: no moderators or heterogeneity tests; the common-law subsample, PSM, two-year lag, MSCI rescoring and non-linear checks are robustness analyses (the non-linear check itself concludes the relationships are linear), not conditions per case law; the governance null is covered as key_finding. ca_measure empty confirmed: 'competitiveness' appears only in intro framing, no CA construct measured. quality_notes 'Association study': the paper uses associational language throughout (see abstract quote) and applies PSM/lags only as endogeneity mitigation without claiming causal identification.*

---

## S54 — Kazakis P. (2026) — Scottish Journal of Political Economy (AJG 2)

DOI: 10.1111/sjpe.70055 · status: final · PDF: `Kazakis_2026_sjpe-70055.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | US Compustat firms; efficiency via DEA (normalized ratio scores); labor-based AI investment measure |
| method | panel econometrics |
| ai_measure | labor-based AI investment measure |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | firm efficiency |
| ca_measure | — |
| effect_direction | conditional |
| conditions | NO unconditional effect; gains only with: capable managers, stronger competitive pressure, stable institutional ownership, long-term debt access |
| key_finding | AI investment alone does nothing for efficiency - gains materialize exclusively under managerial, competitive, ownership and financing conditions ("Conditional Gains"). |
| *not printed (coding data only)* | |
| theoretical_lens | none explicit (efficiency analysis) |
| industry | cross-industry |
| quality_notes | Cleanest single illustration of the thesis RQ - title literally "Conditional Gains" |
| coding_status | final |

*No printed pagination in this PDF — pages below are PDF pages; cite by section/article page per the frozen rule.*

### Evidence

1. **country_region, sample, outcome_construct, performance_measure** — PDF p. 4, 3.1 | Datasets Used and Sample Selection — ✓ verified, 100% word sequence
   > Firm-level accounting data are drawn from Compustat, while firm efficiency is measured using the Data Envelopment Analysis (DEA) approach
   Ctrl+F: „while firm efficiency is measured using the Data“
   → Confirms Compustat (US firm universe) as the sample base and DEA firm efficiency as the performance outcome.

2. **country_region, ai_measure** — PDF p. 5, 3.1.2 | The AI Investment Measure — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > Their second data source is Burning Glass, which provides information on over 180 million U.S. job postings from 2010 to 2018.
   Ctrl+F: „Their second data source is Burning Glass, which“
   → The AI measure is built from U.S. labor-market data, corroborating country_region = USA for the Compustat sample.

3. **sample, performance_measure** — PDF p. 4, 3.1.1 | Calculation of Firm Efficiency With DEA — ✓ verified, 100% word sequence
   > All efficiency scores are subsequently normalized by the highest score within the group, producing an ordinal ranking of DMUs based on relative efficiency.
   Ctrl+F: „All efficiency scores are subsequently normalized by the“
   → Backs the '(normalized ratio scores)' detail of the coded DEA efficiency measure.

4. **sample, industry** — PDF p. 4, 3.1 | Datasets Used and Sample Selection — ⚠ not machine-confirmed on page — open the page, 45% word sequence
   > Firms operating in the financial and utilities sectors are omitted from the analysis (SIC codes 4900-4999 and 6000-6999).
   Ctrl+F: „Firms operating in the financial and utilities sectors“
   → Cross-industry Compustat sample excluding only financials and utilities, consistent with industry = cross-industry.

5. **sample, method** — PDF p. 4, 3.1 | Datasets Used and Sample Selection — ✓ verified, 100% word sequence
   > After completing this process, the baseline sample comprises 51,685 firm-year observations over 1990-2018.
   Ctrl+F: „After completing this process, the baseline“
   → Firm-year panel structure and sample size back the coded sample and the panel econometrics method.

6. **method** — PDF p. 5, 3.2 | Econometric Model — ✓ verified, 81% word sequence
   > To examine the association between AI investment and firm efficiency I use the following OLS model
   Ctrl+F: „To examine the association between AI investment and“
   → OLS regressions with firm and year fixed effects on the firm-year panel back method = panel econometrics.

7. **ai_measure, effect_direction, key_finding** — PDF p. 1, ABSTRACT — ✓ verified, 100% word sequence
   > Using a labor-based measure of AI investment, the baseline results show no direct association between AI investment and firm efficiency.
   Ctrl+F: „measure of AI investment, the baseline results show“
   → Names the labor-based AI investment measure and the null baseline that grounds effect_direction = conditional (null-baseline rule) and the key finding's first half.

8. **ai_measure** — PDF p. 4, 3.1 | Datasets Used and Sample Selection — ✓ verified, 100% word sequence
   > AI investment is based on the share of AI-related workers in a firm
   Ctrl+F: „AI investment is based on the share of“
   → Defines the labor-based AI investment measure (Babina et al. resume-based worker share) as coded.

9. **effect_direction, conditions, key_finding** — PDF p. 1, ABSTRACT — ⚠ not machine-confirmed on page — open the page, 3% word sequence
   > The heterogeneity analysis indicates that efficiency gains materialize primarily when firms pair AI with capable managers, face stronger competitive pressure, have more stable institutional investor ownership, and are able to secure long-term debt.
   Ctrl+F: „analysis indicates that efficiency gains materialize primarily when“
   → Lists all four coded conditions (managerial ability, competition, ownership stability, long-term debt) under which gains materialize.

10. **effect_direction** — PDF p. 7, 4 | Results — ⚠ not machine-confirmed on page — open the page, 7% word sequence
   > the results indicate no statistically significant relationship between AI investment and firm efficiency in isolation. Across all model specifications, the coefficient for the AI variable is insignificant.
   Ctrl+F: „and firm efficiency in isolation. Across all model“
   → Baseline null result: no unconditional AI effect, satisfying the null-baseline rule for effect_direction = conditional.

11. **effect_direction, conditions, key_finding** — PDF p. 10, 6 | Conclusion — ✓ verified, 64% word sequence
   > I find, however, that the returns to AI are larger in more competitive settings and are amplified by higher managerial ability, while they are weakened when ownership is unstable (high institutional investor churn).
   Ctrl+F: „I find, however, that the returns to AI“
   → Paper's own conclusion: gains only under competitive, managerial and ownership conditions - the coded key finding and conditional direction.

12. **conditions** — PDF p. 7, 4 | Results — ⚠ not machine-confirmed on page — open the page, 43% word sequence
   > AI is more strongly linked to efficiency improvements in low-markup (more competitive) settings, while this link weakens, and can turn adverse, for firms with substantial market power.
   Ctrl+F: „settings, while this link weakens, and can turn“
   → Backs the 'stronger competitive pressure' condition (markup interaction).

13. **conditions** — PDF p. 9, 4 | Results — ✓ verified, 100% word sequence
   > The results in Column (3) suggest that a larger share of long-term debt is associated with stronger efficiency gains from AI
   Ctrl+F: „The results in Column (3) suggest that a“
   → Backs the 'long-term debt access' condition.

14. **key_finding, quality_notes** — PDF p. 1, Title — ✓ verified, 100% word sequence
   > Conditional Gains: When AI Investment Enhances Firm Efficiency
   Ctrl+F: „Conditional Gains: When AI Investment Enhances Firm Efficiency“
   → The article title literally reads 'Conditional Gains', backing the quality note's title reference and the conditional framing of the key finding.

15. **theoretical_lens** — PDF p. 2, 2.1 | Why the Average Effect of AI on Efficiency Can Be Nil or Very Small — ⚠ not machine-confirmed on page — open the page, 29% word sequence
   > In this section I argue that the efficiency gains from investing in artificial intelligence (AI) are inherently uneven across firms and are based on the economic and organizational environment in which a firm operates.
   Ctrl+F: „In this section I argue that the efficiency“
   → The paper's theoretical framing is a conditional efficiency argument without adopting a named theory, backing 'none explicit (efficiency analysis)'.

*Row check OK: quality_notes is largely coder commentary ('cleanest single illustration of the thesis RQ'); its factual half (title literally 'Conditional Gains') is evidenced by the title quote. The paper additionally admits a source-based limitation (labor-based AI measure captures capability, not usage; PDF p. 9, section 5) should the author want it. theoretical_lens 'none explicit' confirmed: no named framework is adopted; the only lens-like phrase is a passing 'AI functions as a general-purpose technology' (PDF p. 2). ca_measure empty confirmed: 'competitiveness' appears only in intro framing, no CA construct measured.*

---

## S55 — Li L. et al. (2026) — International Journal of Production Economics (AJG 3)

DOI: 10.1016/j.ijpe.2026.110010 · status: final · PDF: `Li_2026_j-ijpe-2026-110010.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 218 firms in supply chains |
| method | survey-SEM |
| ai_measure | survey construct (responsible AI adoption) |
| *Table A.2 columns* | |
| outcome_construct | competitive_advantage |
| performance_measure | — |
| ca_measure | perceived competitive advantage (survey scale) |
| effect_direction | conditional |
| conditions | FULL mediation: direct responsible-AI -> CA path 0.091 n.s.; effect runs entirely via distributive + procedural justice; supply chain complexity weakens distributive path (-0.233***) but not procedural |
| key_finding | Responsible AI builds competitive advantage through supply-chain justice - in complex networks, only procedural fairness remains a robust channel. |
| *not printed (coding data only)* | |
| theoretical_lens | organizational justice theory |
| industry | cross-industry (supply chains) |
| quality_notes | Perceptual; ethics-as-condition angle \| PROPOSED(batch): Leoni class: direct path n.s. in full text |
| coding_status | final |

### Evidence

1. **country_region, sample, method, outcome_construct, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Survey data from 218 Chinese firms show that responsible AI fosters both distributive and procedural justice, which in turn facilitates firms' competitive advantages.
   Ctrl+F: „Survey data from 218 Chinese firms show that“
   → Abstract states the mediated path to competitive advantages and confirms 218 Chinese survey firms, covering sample, country, method and the CA outcome.

2. **country_region, sample, industry** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > our target population comprised senior managers (e.g., vice presidents, directors, and senior managers) in Chinese manufacturing and IT firms who have actively adopted AI in their supply chain operations
   Ctrl+F: „vice presidents, directors, and senior managers) in Chinese“
   → Specifies the supply-chain firm sample (manufacturing, IT, plus 'other' per Table 1) in China, backing the '(supply chains)' industry qualifier.

3. **sample, method** — p. 5 (PDF p. 5) — ✓ verified, 65% word sequence
   > We invited 335 qualified firms from the survey provider's database and received 218 valid responses after applying exclusion criteria and quality checks
   Ctrl+F: „firms from the survey provider's database and received“
   → Documents the survey procedure and the n = 218 coded in sample.

4. **method** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > we conducted confirmatory factor analysis of all five latent constructs: responsible AI, distributive justice, procedural justice, competitive advantages, and SCC
   Ctrl+F: „we conducted confirmatory factor analysis of all five“
   → Latent-construct measurement model (CFA) on survey data backs method = survey-SEM.

5. **method** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > To test our hypotheses, we used the PROCESS macro in SPSS 23.0 (Hayes, 2014), with responsible AI as the independent variable, distributive justice and procedural justice as the mediators
   Ctrl+F: „To test our hypotheses, we used the PROCESS“
   → Names the moderated-mediation estimation strategy that generates the AI-to-CA evidence.

6. **ai_measure** — p. 4–6 (PDF p. 4) — ✓ verified, 100% word sequence
   > First, responsible AI was measured using four items adapted from P. Kumar et al. (2023).
   Ctrl+F: „First, responsible AI was measured“
   → Responsible AI adoption is a survey construct measured with an established four-item scale, as coded.

7. **outcome_construct, ca_measure** — p. 6 (PDF p. 6) — ✓ verified, 90% word sequence
   > Third, competitive advantages were assessed using three items from L. Li et al. (2023) that benchmark financial performance against industry peers.
   Ctrl+F: „Third, competitive advantages were assessed using three items“
   → Own validated competitive-advantage scale (competitor-benchmarked), satisfying the case-law bar for outcome_construct = competitive_advantage and the coded perceived CA survey scale.

8. **outcome_construct, conditions** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > H1. Distributive justice mediates the positive association between responsible AI and competitive advantages.
   Ctrl+F: „H1. Distributive justice mediates the positive association between“
   → Explicit hypothesis on the CA construct (scale + hypothesis per case law) and on the coded mediation channel.

9. **effect_direction, conditions** — p. 7 (PDF p. 7) — ✓ verified, 80% word sequence
   > However, when distributive and procedural justice are included as mediators in Model 6, the direct positive relationship between responsible AI and competitive advantages becomes nonsignificant (β = 0.091, p > .05).
   Ctrl+F: „included as mediators in Model 6, the direct“
   → The nonsignificant direct path (0.091 n.s.) with significant indirect paths is the full-mediation basis for effect_direction = conditional (Leoni class, adjudicated).

10. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The interaction terms in Model 2 show that SCC significantly and negatively moderates the relationship between responsible AI and distributive justice
   Ctrl+F: „interaction terms in Model 2 show that SCC“
   → Backs the coded condition that supply chain complexity weakens the distributive-justice path (coefficient -0.233, p < .001 in the paper; see row_check note on minus signs).

11. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > In contrast, SCC did not moderate the relationship between responsible AI and procedural justice
   Ctrl+F: „not moderate the relationship between responsible AI and“
   → Backs the coded asymmetry: complexity does not weaken the procedural-justice path.

12. **conditions, key_finding** — p. 9 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 30% word sequence
   > Crucially, our findings highlight a divergence in how SCC conditions these effects: while high SCC weakens the mediating role of distributive justice, the mediating role of procedural justice remains robust.
   Ctrl+F: „Crucially, our findings highlight a divergence in how“
   → Paper's own conclusion: justice-mediated CA with procedural fairness as the only robust channel under complexity - the coded key finding.

13. **theoretical_lens** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > we draw on organizational justice theory (OJT), which posits that perceptions of fairness are fundamental determinants of organizational behavior and performance
   Ctrl+F: „which posits that perceptions of fairness are fundamental“
   → Names organizational justice theory as the study's framework, matching the coded lens.

14. **quality_notes** — p. 9 (PDF p. 9) — ✓ verified, 75% word sequence
   > First, our cross-sectional design could not capture the temporal evolution of justice perceptions; future researchers could use longitudinal designs to validate causal directions.
   Ctrl+F: „First, our cross-sectional design could not capture the“
   → Authors' own limitation backing the 'perceptual' cross-sectional quality note.

*Row check OK: performance_measure empty confirmed: the only outcome construct is the competitive-advantages scale (relative financial performance vs. industry peers); no standalone performance measure. Caution for the audit: the text extraction drops minus signs on some statistics - the prose renders the SCC x responsible-AI interaction as '(β = 0.233, p < .001)' although it 'negatively moderates' (the paper's value is -0.233), so verify the coded -0.233*** on the PDF page rather than the extract. quality_notes' 'ethics-as-condition angle' is coder commentary; the perceptual/cross-sectional half is source-backed (see limitation quote).*

---

## S56 — Li L. et al. (2026) — Journal of Business Research (AJG 3)

DOI: 10.1016/j.jbusres.2026.115974 · status: final · PDF: `Li_2026_j-jbusres-2026-115974.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 223 firms across industries, China, survey |
| method | survey-SEM |
| ai_measure | survey construct (GenAI affordances: organizational memory, collaborative, creational) |
| *Table A.2 columns* | |
| outcome_construct | competitive_advantage |
| performance_measure | — |
| ca_measure | perceived sustained competitive advantage (survey scale) |
| effect_direction | positive |
| conditions | three GenAI affordances mediate technological opportunism -> CA; competitive intensity amplifies ONLY the creational-affordance path |
| key_finding | Technological opportunism converts into competitive advantage through GenAI affordances - under intense competition, only the creational affordance keeps paying. |
| *not printed (coding data only)* | |
| theoretical_lens | affordance theory |
| industry | cross-industry |
| quality_notes | PDF re-downloaded 18 Jul (after dedupe-bug loss); Gemini re-run: FULL AGREEMENT survey-SEM/competitive_advantage/conditional - dispute void; perceptual cross-section |
| coding_status | final |

### Evidence

1. **country_region, sample, method, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We draw on survey data from 223 firms spanning different industries in China
   Ctrl+F: „We draw on survey data from 223 firms“
   → Confirms survey method, n = 223, cross-industry scope, and China as coded.

2. **country_region, industry** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > GenAI adoption in China extends beyond the IT sector, with widespread use across industries including manufacturing, e-commerce, finance, and healthcare.
   Ctrl+F: „adoption in China extends beyond the IT sector,“
   → Backs the cross-industry sampling rationale in the Chinese setting (Table 2: 39% manufacturing, 52% IT, 9% others).

3. **sample, method** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > Following these procedures, 223 valid responses were obtained from 365 distributed surveys, yielding a response rate of approximately 61.10 %.
   Ctrl+F: „223 valid responses were obtained from 365 distributed“
   → Documents the survey procedure and the coded n = 223.

4. **sample, conditions, key_finding** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > Through a survey of 223 Chinese firms, we confirm the significant mediating role of organizational memory, collaborative, and creational affordances in the TO-competitive advantage relationship.
   Ctrl+F: „firms, we confirm the significant mediating role of“
   → Paper's own conclusion stating the central result coded as key_finding: opportunism converts into CA through the GenAI affordances.

5. **method** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > To test our research hypotheses, we utilized the PROCESS macro, a robust tool for mediation and moderation analysis, within the SPSS software
   Ctrl+F: „To test our research hypotheses, we utilized the“
   → Names the mediation/moderation estimation on the survey data (with CFA-validated latent constructs), backing method = survey-SEM.

6. **ai_measure, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > find that three GenAI affordances -organizational memory, collaborative, and creational affordances -mediate the relationship between TO and competitive advantages
   Ctrl+F: „the relationship between TO and competitive advantages.“
   → Abstract result naming the three coded GenAI affordances as the mediating channel to CA.

7. **ai_measure** — p. 6 (PDF p. 6) — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > GenAI affordances comprise three components: organizational memory affordance, collaborative affordance, and creational affordance. Measurements for the first two components were adapted from Chatterjee et al. (2020)
   Ctrl+F: „for the first two components were adapted from“
   → Shows the AI measure is a survey construct of the three coded GenAI affordances, measured with established scales.

8. **outcome_construct, ca_measure, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > we ground in affordance theory to explore how firms can leverage GenAI affordances to transform technological opportunism (TO) into sustained competitive advantages, particularly in highly competitive environments
   Ctrl+F: „we ground in affordance theory to explore how“
   → Abstract names affordance theory as the framework and sustained competitive advantage as the outcome construct.

9. **outcome_construct, ca_measure** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > Competitive advantage was measured using four items reflecting financial and strategic performance, consistent with prior research (Schilke, 2014; Li et al., 2023c).
   Ctrl+F: „advantage was measured using four items reflecting financial“
   → Own validated CA scale (plus mediation hypotheses H1-H3 on the CA link), satisfying the case-law bar for outcome_construct = competitive_advantage.

10. **ca_measure** — p. 6 (PDF p. 6) — ✓ verified, 83% word sequence
   > strategic performance -measured by market share -represents firms' long-term market position and ability to sustain their competitive edge over current and potential rivals
   Ctrl+F: „market position and ability to sustain their competitive“
   → Backs the 'sustained' and competitor-comparative character of the coded perceived CA scale.

11. **effect_direction** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > Without any mediators, the direct effect of TO on competitive advantages is positive and significant (β = 0.588; p < 0.001).
   Ctrl+F: „mediators, the direct effect of TO on competitive“
   → Significant positive total effect - the main-effect basis for effect_direction = positive.

12. **effect_direction, conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > TO and the three mediators demonstrate significant associations with competitive advantages (TO: β = 0.314, p < 0.001; organizational memory affordance: β = 0.186, p < 0.01; collaborative affordance: β = 0.132, p < 0.05; creational affordance: β = 0.177, p < 0.01).
   Ctrl+F: „0.314, p < 0.001; organizational memory affordance: β = 0.186, p“
   → Direct path stays significant alongside the mediators (partial mediation) - per the frozen rule, mediated-positive WITH significant direct effect = positive; mediators go to conditions.

13. **conditions, key_finding** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 29% word sequence
   > Moreover, competitive intensity amplifies the mediation effect of creational affordance instead of the mediation effects of organizational memory and collaborative affordances.
   Ctrl+F: „effect of creational affordance instead of the mediation“
   → Backs the coded condition that competitive intensity amplifies ONLY the creational-affordance path.

14. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > Note that only the indices for creational affordance were significant (index = 0.037, SE = 0.019; 95 % CI [0.006, 0.080]).
   Ctrl+F: „indices for creational affordance were significant (index = 0.037,“
   → Moderated-mediation index significant solely for creational affordance, backing the 'ONLY the creational-affordance path' condition.

**⚠ ROW CHECK:** Coded effect_direction = positive is supported by the full text (total effect 0.588***, direct path with mediators still 0.314*** - partial mediation, positive per the main-effect rule), BUT the row's own quality_notes cell says 'Gemini re-run: FULL AGREEMENT survey-SEM/competitive_advantage/conditional', which contradicts the final 'positive' on its face - likely a stale process note from before the mediated-positive harmonization; author should reword it. Rest of quality_notes is process commentary (PDF re-download); 'perceptual cross-section' is backed by the 7-point-Likert survey design. performance_measure empty confirmed: the financial indicators (EBIT, ROI, ROS vs. industry averages) are items INSIDE the CA construct, no standalone performance outcome.

---

## S57 — Lin M. et al. (2026) — Emerging Markets Finance and Trade (AJG 2)

DOI: 10.1080/1540496X.2026.2691898 · status: final · PDF: `Lin_2026_1540496X-2026-2691898.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | Chinese A-share listed companies, 2007-2022 |
| method | panel econometrics |
| ai_measure | annual-report text-based AI adoption measure (authors explicitly contrast with patent/robot proxies) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | total factor productivity |
| ca_measure | — |
| effect_direction | positive |
| conditions | internal control quality (partial mediator: AI -> better governance/risk management -> TFP) |
| key_finding | AI raises firm productivity partly by improving internal control quality - governance is a transmission channel, not just a moderator. |
| *not printed (coding data only)* | |
| theoretical_lens | internal control / governance channel (no grand theory) |
| industry | cross-industry (listed firms) |
| quality_notes | Robustness checks; mediation design |
| coding_status | final |

### Evidence

1. **country_region, sample, outcome_construct, performance_measure, industry** — p. 1 (PDF p. 2) — ✓ verified, 100% word sequence
   > This research investigates the impact of AI adoption on total factor productivity (TFP) within Chinese A-share listed companies from 2007 to 2022.
   Ctrl+F: „This research investigates the impact of AI adoption“
   → Names the sample (Chinese A-share listed companies 2007-2022, i.e. cross-industry listed firms), the country, and TFP as the performance outcome.

2. **method, quality_notes** — p. 2 (PDF p. 3) — ✓ verified, 100% word sequence
   > We utilize a high-dimensional fixed-effects model for baseline estimation and a formal mediation analysis framework to test the indirect effect.
   Ctrl+F: „a high-dimensional fixed-effects model for baseline estimation and“
   → Panel fixed-effects econometrics as the evidence-generating strategy plus the mediation design noted in quality_notes.

3. **method** — p. 5 (PDF p. 6) — ✓ verified, 100% word sequence
   > All models employ panel fixed effects at the firm, year, industry, and provincial levels to control for unobserved heterogeneity.
   Ctrl+F: „All models employ panel fixed effects at the“
   → Confirms method = panel econometrics (firm/year/industry/province fixed effects).

4. **ai_measure** — p. 4 (PDF p. 5) — ✓ verified, 100% word sequence
   > Following W. Chen and Srinivasan (2024) and the WIPO AI glossary, AI is identified via textual analysis of Chinese AI terms measured as ln(1+ the count of AI-related words)
   Ctrl+F: „Following W. Chen and Srinivasan (2024) and the“
   → Defines the annual-report text-based AI adoption measure coded in ai_measure.

5. **ai_measure** — p. 3 (PDF p. 4) — ✓ verified, 100% word sequence
   > While useful, these proxies suffer from well-known limitations: patents capture invention rather than adoption; robotics data miss software-based AI applications
   Ctrl+F: „suffer from well-known limitations: patents capture invention rather“
   → Authors' explicit contrast of their text measure with patent/robot proxies, as noted in the coded ai_measure.

6. **outcome_construct, effect_direction, quality_notes** — p. 1 (PDF p. 2) — ✓ verified, 100% word sequence
   > We find a significant positive effect of AI on firm-level TFP, a result that holds under a series of rigorous robustness checks.
   Ctrl+F: „positive effect of AI on firm-level TFP, a“
   → States the significant positive main effect on the performance outcome and the robustness checks noted in quality_notes.

7. **effect_direction, conditions** — p. 8 (PDF p. 9) — ✓ verified, 100% word sequence
   > both variables retain positive and statistically significant coefficients for AI at 0.0144 and for ICQ at 0.0133, indicating that higher ICQ partially mediates the effect of AI on TFP.
   Ctrl+F: „significant coefficients for AI at 0.0144 and for“
   → Direct AI path stays significant with the mediator included, so partial mediation: direction = positive per the main-effect rule, ICQ mediator goes to conditions.

8. **effect_direction** — p. 5 (PDF p. 6) — ✓ verified, 100% word sequence
   > Across the baseline models reported in Table 2, AI carries a positive sign and is significant, with point estimates spanning 0.0300 to 0.0690
   Ctrl+F: „Across the baseline models reported in Table 2,“
   → Baseline regressions show the positive significant average main effect coded as effect_direction.

9. **conditions, key_finding** — p. 1 (PDF p. 2) — ✓ verified, 100% word sequence
   > Importantly, we identify a key transmission mechanism: the positive relationship between AI and TFP is partially channeled through enhanced internal control quality (ICQ).
   Ctrl+F: „Importantly, we identify a key transmission mechanism: the“
   → ICQ as partial mediator is exactly the coded condition and the transmission-channel core of the key finding.

10. **conditions, quality_notes** — p. 8 (PDF p. 9) — ✓ verified, 100% word sequence
   > Sobel-Goodman tests confirm the mediation, with an indirect effect of 0.0004, contributing approximately 2.4% of the total effect
   Ctrl+F: „Sobel-Goodman tests confirm the mediation, with an indirect“
   → Formal mediation tests back the coded partial-mediator condition and the mediation-design quality note.

11. **key_finding** — p. 1 (PDF p. 2) — ✓ verified, 100% word sequence
   > This indicates that AI-driven improvements in organizational governance and risk management constitute a vital link to TFP gains.
   Ctrl+F: „governance and risk management constitute a vital link“
   → Paper's own statement that governance/risk management improvements are the link to TFP gains, matching the coded key_finding.

12. **theoretical_lens** — p. 3 (PDF p. 4) — ✓ verified, 100% word sequence
   > ICQ functions as a mediating governance mechanism that translates technological or strategic inputs such as AI adoption into performance outcomes by improving monitoring, reporting, and operational reliability.
   Ctrl+F: „ICQ functions as a mediating governance mechanism that“
   → The paper's framework is the internal-control/governance channel, matching the coded lens (no grand theory adopted as framework).

13. **industry** — p. 9 (PDF p. 10) — ✓ verified, 100% word sequence
   > Columns (5) and (6) of Table 6 distinguish between manufacturing and non-manufacturing firms to assess whether the effect of AI on TFP varies by industry.
   Ctrl+F: „Columns (5) and (6) of Table 6 distinguish“
   → Sample spans manufacturing and non-manufacturing listed firms, backing industry = cross-industry.

14. **quality_notes** — p. 7 (PDF p. 8) — ✓ verified, 100% word sequence
   > The robustness checks indicate that the productivity gains tied to AI are robust to alternative ways of measuring TFP, alternative AI proxies, and varying sample periods.
   Ctrl+F: „The robustness checks indicate that the productivity gains“
   → Source basis for the 'robustness checks' quality note.

*Row check OK: ca_measure empty confirmed: 'competitive advantages' appears only as introduction framing citing prior studies (p.2), no CA construct measured. Lens note: the literature review briefly invokes agency theory and RBV (p.4), but the paper's own framework is the ICQ governance channel, as coded. Heterogeneity results (stronger for non-SOE, larger, non-manufacturing, high-tech firms, Table 6) are in the paper but not in the coded conditions field, which keeps only the ICQ mediator; not a rule violation, listed for completeness.*

---

## S58 — Lin N. et al. (2026) — International Review of Financial Analysis (AJG 3)

DOI: 10.1016/j.irfa.2025.104830 · status: final · PDF: `Lin_2026_j-irfa-2025-104830.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | Chinese listed firms |
| method | panel econometrics |
| ai_measure | tailored AI-keyword dictionary, novel text analysis of company reports |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | investment efficiency + firm value |
| ca_measure | — |
| effect_direction | positive |
| conditions | stronger in high knowledge-intensity, high R&D-intensity firms and firms with sound internal controls; mechanisms: innovation capability + financial health |
| key_finding | AI enhances investment efficiency and firm value most where knowledge intensity, R&D and internal controls provide absorptive capacity. |
| *not printed (coding data only)* | |
| theoretical_lens | corporate finance (investment efficiency) |
| industry | cross-industry (listed firms) |
| quality_notes | Mechanism analysis |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using panel data from Chinese A-share listed companies between 2008 and 2023
   Ctrl+F: „Using panel data from Chinese A-share listed“
   → Names the sample (Chinese A-share listed companies), the country, and the panel-data design.

2. **sample, industry** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > First, ST and ST* listed companies are excluded; second, financial-type listed companies are removed; third, observations with missing financial data are eliminated.
   Ctrl+F: „and ST* listed companies are excluded; second,“
   → Sample construction: all listed firms except financials, backing industry = cross-industry (listed firms).

3. **method** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > This paper employs a fixed-effects model to examine the impact of artificial intelligence on corporate investment efficiency.
   Ctrl+F: „This paper employs a fixed-effects model to examine“
   → Fixed-effects regression on firm-year panel data confirms method = panel econometrics.

4. **ai_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > The corporate artificial intelligence (AI) adoption is measured through text analysis of company annual reports.
   Ctrl+F: „intelligence (AI) adoption is measured through text analysis“
   → Backs the coded ai_measure: text analysis of company reports.

5. **ai_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > Furthermore, by constructing a tailored AI-related keyword dictionary and employing a novel text analysis approach, this study not only introduces an innovative method for measuring corporate AI adoption
   Ctrl+F: „tailored AI-related keyword dictionary and employing a novel“
   → The paper's own wording 'tailored AI-related keyword dictionary' and 'novel text analysis' matches the coded ai_measure verbatim.

6. **outcome_construct, performance_measure, effect_direction** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results show that AI can significantly enhance the investment efficiency of enterprises.
   Ctrl+F: „that AI can significantly enhance the investment“
   → Investment efficiency as the performance outcome with a significant positive main effect.

7. **performance_measure, effect_direction** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Furthermore, we find that AI adoption may lead to a rise in firm value.
   Ctrl+F: „that AI adoption may lead to a rise“
   → Firm value as the second coded performance outcome, also positive.

8. **effect_direction** — p. 6 (PDF p. 6) — ⚠ not machine-confirmed on page — open the page, 9% word sequence
   > The regression findings consistently demonstrate a statistically significant positive relationship between artificial intelligence adoption and corporate investment efficiency at the 1 % significance level
   Ctrl+F: „and corporate investment efficiency at the 1“
   → Clear positive average main effect in the baseline regressions, so direction = positive; mechanisms and heterogeneity belong in conditions.

9. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This effect is more pronounced in high knowledge-intensity firms, high R & D-intensity firms, and firms with sound internal controls.
   Ctrl+F: „This effect is more pronounced in high“
   → The three coded heterogeneity conditions (knowledge intensity, R&D intensity, sound internal controls) in the paper's own words.

10. **conditions, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Mechanism analysis reveals that AI contributes to improved investment efficiency by enhancing innovation capabilities and strengthening the financial health of firms.
   Ctrl+F: „reveals that AI contributes to improved investment“
   → The two coded mechanisms (innovation capability, financial health) and the source basis of the 'Mechanism analysis' quality note.

11. **conditions, key_finding** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > The heterogeneity analysis reveals that the beneficial impact of AI on investment efficiency is stronger among firms with high knowledge intensity, elevated R & D investment, and robust internal control systems.
   Ctrl+F: „reveals that the beneficial impact of AI on“
   → Conclusion's own statement of the central result: effect strongest where knowledge intensity, R&D and internal controls are high, matching key_finding.

12. **conditions, quality_notes** — p. 8 (PDF p. 8) — ✓ verified, 74% word sequence
   > This section employs a mediation effect model, using corporate innovation level and corporate financial condition as mediating variables to conduct mechanism identification tests.
   Ctrl+F: „This section employs a mediation effect model, using“
   → Formal mediation design behind the coded mechanisms and the 'Mechanism analysis' quality note.

13. **theoretical_lens** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > In doing so, it contributes to the literature on corporate investment efficiency by introducing a novel, technology-oriented perspective.
   Ctrl+F: „In doing so, it contributes to the literature“
   → Self-positioning in the corporate-finance investment-efficiency literature, matching the coded lens.

14. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 96% word sequence
   > Prior research has mainly focused on issues such as weak internal controls, information asymmetry, limited access to financing, and agency conflicts as determinants of investment inefficiency
   Ctrl+F: „on issues such as weak internal controls, information“
   → The paper frames itself against the corporate-finance determinants of investment inefficiency (agency, financing constraints), backing the lens coding.

*Row check OK: ca_measure empty confirmed: no competitive-advantage construct is measured; 'market competition' appears only as a future-research topic (p.10). Direction check per mediation rule: baseline direct effect 0.003*** and lnword stays significant with mediators included (Tables 11-12), so partial mediation and positive is correct. Sample detail: 24,768 firm-year observations 2008-2023; note the paper's Table 1 caption erroneously says 'period 2006-2014' - a paper-internal typo, not a coding issue.*

---

## S59 — Liu D. et al. (2026) — International Review of Financial Analysis (AJG 3)

DOI: 10.1016/j.irfa.2026.105163 · status: final · PDF: `Liu_2026_j-irfa-2026-105163.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | Chinese publicly listed firms, 2007-2024 |
| method | panel econometrics |
| ai_measure | textual analysis of annual reports (CNINFO, jieba segmentation), ln(1+AI keyword frequency), following Mishra et al. 2022 |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | M&A likelihood (strategic outcome) + long-term firm value |
| ca_measure | — |
| effect_direction | positive |
| conditions | stronger with abundant cash holdings, less-developed market environments, private ownership |
| key_finding | AI adoption makes firms more acquisitive and raises long-term value - internal resources and institutional context set the boundary. |
| *not printed (coding data only)* | |
| theoretical_lens | RBV |
| industry | cross-industry (listed firms) |
| quality_notes | Strategic-behaviour outcome plus value; RBV framing |
| coding_status | final |

### Evidence

1. **country_region, sample, performance_measure, theoretical_lens, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on the resource based view, this study uses data from publicly listed firms in China from 2007 to 2024 to examine how artificial intelligence (AI) adoption influences M & A activity.
   Ctrl+F: „based view, this study uses data from publicly“
   → Abstract names the RBV lens, the sample (Chinese publicly listed firms 2007-2024), and M&A activity as the outcome; also backs the 'RBV framing' quality note.

2. **sample, industry** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The initial sample is refined as follows: (1) financial firms, including banks, securities companies, and insurance institutions, are excluded
   Ctrl+F: „The initial sample is refined as follows: (1)“
   → All listed firms minus financials (47,509 firm-year observations), backing industry = cross-industry (listed firms).

3. **method** — p. 6 (PDF p. 6) — ⚠ not machine-confirmed on page — open the page, 43% word sequence
   > this study develops a panel data regression model to empirically examine the relationship between firm AI adoption and M & A behavior
   Ctrl+F: „this study develops a panel data regression model“
   → Panel data regression with firm/year/industry fixed effects confirms method = panel econometrics.

4. **ai_measure** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > Following Yao et al. (2024) and Mishra et al. (2022); we constructed a firm-level AI adoption indicator via textual analysis of annual reports from the CNINFO platform.
   Ctrl+F: „Following Yao et al. (2024) and Mishra et“
   → Textual analysis of CNINFO annual reports following Mishra et al. 2022, as coded in ai_measure.

5. **ai_measure** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > We first processed these reports using the ' jieba ' Python library for Chinese word segmentation.
   Ctrl+F: „We first processed these reports using the“
   → The jieba segmentation step named in the coded ai_measure.

6. **ai_measure** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > To mitigate skewness, the final AI adoption measure is the natural logarithm of the aggregated keyword frequency plus one.
   Ctrl+F: „To mitigate skewness, the final AI adoption measure“
   → The ln(1+AI keyword frequency) operationalization named in the coded ai_measure.

7. **outcome_construct, performance_measure, effect_direction, conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > We find that AI adoption significantly increases a firm ' s likelihood of pursuing M & A, with the effect especially pronounced among firms with abundant cash holdings and those operating in less developed market environments.
   Ctrl+F: „We find that AI adoption significantly increases a“
   → Positive significant main effect on M&A likelihood; cash holdings and less-developed markets are moderators of strength, so they go to conditions while direction stays positive.

8. **outcome_construct, performance_measure, effect_direction, conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The relationship is also stronger for privately owned enterprises, and AI adoption is associated with improved long term firm value.
   Ctrl+F: „privately owned enterprises, and AI adoption is associated“
   → Backs the second coded outcome (long-term firm value, positive) and the private-ownership condition.

9. **outcome_construct, performance_measure, quality_notes** — p. 17 (PDF p. 17) — ✓ verified, 100% word sequence
   > To assess the economic implications of AI-driven M & A, Table 23 examines its association with firm value (Tobin ' s Q).
   Ctrl+F: „To assess the economic implications of AI-driven“
   → Firm value (Tobin's Q, incl. forward value in Model 67) as the value outcome; backs the 'strategic-behaviour outcome plus value' quality note.

10. **conditions** — p. 15 (PDF p. 15) — ✓ verified, 67% word sequence
   > For state-owned enterprises (SOEs), the coefficient for AI is small and statistically insignificant ( β = 0.0211, p > 0.1). Conversely, for nonSOEs, the coefficient is positive and significant at the 1% level
   Ctrl+F: „For state-owned enterprises (SOEs), the coefficient for AI“
   → Ownership heterogeneity: effect holds for non-SOEs but not SOEs, backing the coded private-ownership condition.

11. **conditions** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > indicating that the positive effect of AI is weaker in regions with higher levels of marketization
   Ctrl+F: „indicating that the positive effect of AI is“
   → Negative marketization moderation backs the coded condition 'less-developed market environments' (where the effect is stronger).

12. **conditions** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > indicating that the effect of AI on M & A is significantly strengthened when cash holdings increase
   Ctrl+F: „indicating that the effect of AI on“
   → Cash-holdings moderation backs the coded condition 'abundant cash holdings'.

13. **conditions, key_finding** — p. 17 (PDF p. 17) — ✓ verified, 100% word sequence
   > We find this catalytic effect is heterogeneous: it is strongest in firms with substantial cash holdings, suggesting that financial slack is essential to convert technological capability into strategic action.
   Ctrl+F: „find this catalytic effect is heterogeneous: it is“
   → The paper's own boundary statement: internal resources set the boundary of the effect, matching key_finding.

14. **key_finding** — p. 17 (PDF p. 17) — ✓ verified, 100% word sequence
   > Our results show that AI adoption significantly drives M & A strategies.
   Ctrl+F: „Our results show that AI adoption significantly drives“
   → Conclusion's own statement of the central result: AI makes firms more acquisitive.

*Row check OK: ca_measure empty confirmed: 'competitive advantage' appears only as RBV theory framing (p.2) and in managerial implications ('build a competitive advantage in the market for corporate control', p.17); no CA construct is measured, so performance coding is consistent with the case law. Measurement detail: the main DV is ln(1+M&A transaction value); the coded 'M&A likelihood' follows the paper's own abstract wording, and the Heckman first stage additionally models an M&A dummy (likelihood).*

---

## S60 — Liu Z. et al. (2026) — Technology in Society (AJG 2)

DOI: 10.1016/j.techsoc.2026.103434 · status: final · PDF: `Liu_2026_j-techsoc-2026-103434.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | Asia-Pacific (multi-region) |
| sample | Study 1: multilevel survey of 420 firms (HLM); Study 2: vignette experiment with 360 managers |
| method | mixed |
| ai_measure | survey construct (AI-enabled innovation); experimentally manipulated regulatory conditions |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | productivity gains + firm growth |
| ca_measure | — |
| effect_direction | positive |
| conditions | regulatory climate moderates innovation->productivity link strength (clarity + supportive enforcement jointly maximize, moderated mediation); Study 2 experiment: causal evidence for regulatory conditions |
| key_finding | AI-enabled innovation converts into productivity and growth only under clear, supportive regulation - institutional environment is the amplifier. |
| *not printed (coding data only)* | |
| theoretical_lens | institutional + contingency perspectives |
| industry | cross-industry |
| quality_notes | Rare causal experiment component; institution-level condition \| PROPOSED(batch): Direct AND indirect associations present, moderation = strength not existence (Shi rule) -> positive |
| coding_status | final |

### Evidence

1. **country_region** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The firms included in Study 1 were drawn from multiple Asia-Pacific economies, including China, Malaysia, Singapore, and Thailand.
   Ctrl+F: „The firms included in Study 1 were drawn“
   → Backs country_region = Asia-Pacific (multi-region).

2. **sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Study 1 employs multilevel survey data from 420 firms across multiple regions, analyzed using hierarchical linear modeling.
   Ctrl+F: „1 employs multilevel survey data from 420 firms“
   → Backs the coded Study 1 sample (420 firms, multilevel survey, HLM).

3. **sample, method, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Study 2 adopts an experimental vignette design with 360 managerial participants to provide causal evidence.
   Ctrl+F: „Study 2 adopts an experimental vignette design with“
   → Backs the coded Study 2 sample (vignette experiment, 360 managers) and the 'rare causal experiment component' quality note.

4. **method** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > This research employed a mixed-method design consisting of a multilevel field survey (Study 1) and a complementary experimental vignette study (Study 2).
   Ctrl+F: „This research employed a mixed-method design consisting of“
   → Explicit 'mixed-method design'; both strands carry outcome evidence, so method = mixed per the case law.

5. **ai_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > AI-enabled innovation was measured in Study 1 using a four-item scale adapted from prior innovation research
   Ctrl+F: „AI-enabled innovation was measured in Study 1 using“
   → The survey construct (AI-enabled innovation) coded in ai_measure.

6. **ai_measure, conditions, quality_notes** — p. 4 (PDF p. 4) — ✓ verified, 64% word sequence
   > In Study 2, regulatory climate was experimentally manipulated through vignette scenarios varying regulatory clarity and enforcement posture, with manipulation checks confirming successful differentiation between conditions.
   Ctrl+F: „clarity and enforcement posture, with manipulation checks“
   → The experimentally manipulated regulatory conditions named in ai_measure and conditions; also the causal-experiment quality note.

7. **outcome_construct, performance_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > Productivity gains were assessed in Study 1 using a three-item measure adapted from operational performance research (Ketokivi & Schroeder, 2004), capturing efficiency, output quality, and resource utilization
   Ctrl+F: „Productivity gains were assessed in Study 1 using“
   → Productivity gains as the first coded performance measure.

8. **outcome_construct, performance_measure, ca_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The scale explicitly captured managers' assessments of growth in sales, market share, and profitability over the past three years relative to key competitors
   Ctrl+F: „growth in sales, market share, and profitability over“
   → Firm growth as the second coded performance measure (perceptual growth scale).
   **⚠ TENSION:** Growth scale is anchored 'relative to key competitors' - a competitor-comparative wording that is a boundary case under the S05 relative-performance rule. The construct itself is firm economic growth (no distinct CA construct, scale, or CA hypothesis), so outcome_construct = performance and empty ca_measure follow the frozen rule; flagged only so the author sees the anchor.

9. **performance_measure, effect_direction, conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Results suggest that AI-enabled innovation is associated with firm growth both directly and indirectly through productivity gains, with the strength of the innovation -productivity link contingent on the regional regulatory climate.
   Ctrl+F: „Results suggest that AI-enabled innovation is associated with“
   → The adjudication-brief quote: direct AND indirect associations present, regulation moderates strength not existence, so direction = positive per the Shi rule and the regulatory contingency goes to conditions.

10. **effect_direction** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > AI-enabled innovation also exerted a significant direct effect on firm economic growth ( γ = .15, p < .05, 95% CI [.04, .26]), indicating that AI innovation contributes to growth beyond its indirect effects through productivity.
   Ctrl+F: „effect on firm economic growth (γ = .15, p < .05,“
   → Significant direct path alongside the mediation - partial, not full, mediation, confirming positive rather than conditional.

11. **conditions, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on institutional and contingency perspectives, two complementary studies are conducted to test a moderated mediation model.
   Ctrl+F: „contingency perspectives, two complementary studies are conducted to“
   → Abstract names the institutional + contingency lens and the moderated mediation design behind the coded conditions.

12. **conditions, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 84% word sequence
   > Regulatory clarity and supportive enforcement are manipulated, and results indicate that clear and supportive environments are associated with higher levels of intended AI investment, productivity expectations, deployment speed, and growth projections.
   Ctrl+F: „Regulatory clarity and supportive enforcement are manipulated, and“
   → Study 2's causal evidence for the regulatory conditions coded in conditions and noted in quality_notes.

13. **conditions, key_finding** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 41% word sequence
   > moderated mediation findings reveal that the productivity pathway is strongest when both clarity and supportiveness are present
   Ctrl+F: „pathway is strongest when both clarity and supportiveness“
   → Backs the coded condition that clarity and supportive enforcement jointly maximize the productivity pathway.

14. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Together, these studies provide convergent evidence that institutional environments may amplify the benefits of AI adoption
   Ctrl+F: „convergent evidence that institutional environments may amplify the“
   → The paper's own summary statement that the institutional environment is the amplifier, matching key_finding.

15. **industry** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > A stratified sampling approach across industries was used to capture variability in innovation practices while maintaining comparability.
   Ctrl+F: „stratified sampling approach across industries was used to“
   → Sampling stratified across industries backs industry = cross-industry.

**⚠ ROW CHECK:** Two things to look at, neither a rule violation: (1) the firm-growth scale is anchored 'relative to key competitors' (p.4) - see the tension note; performance coding follows the frozen rule because the construct is growth, not a distinct CA construct. (2) Direction adjudication confirmed in the full text: direct effect on growth γ=.15* and the AI->productivity slope stays significant even at low regulatory support (.18*, Table 4 Panel B), so moderation of strength, not existence. The second half of quality_notes ('PROPOSED(batch)...') is adjudication commentary, not source-based, and is deliberately not quote-evidenced.

---

## S61 — Mukherjee S. et al. (2026) — International Journal of Quality and Reliability Management (AJG 2)

DOI: 10.1108/IJQRM-02-2025-0082 · status: final · PDF: `Mukherjee_2026_IJQRM-02-2025-0082.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | India |
| sample | 312 valid responses from luxury hotels (lodging + food services) |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption intention) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | service performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | — |
| key_finding | AI adoption intention lifts hotel service performance; drivers: ease of use, competitive pressure, policy support - the infrastructure estimate is negative. |
| *not printed (coding data only)* | |
| theoretical_lens | TAM + TOE |
| industry | hospitality (luxury hotels) |
| quality_notes | Perceptual, cross-section \| PROPOSED(batch): TOE/TAM factors are ADOPTION antecedents, not conditions on the AI->performance link; AI adoption -> service performance positive main effect |
| coding_status | final |

### Evidence

1. **country_region, sample, industry** — p. 1962 (PDF p. 9) — ✓ verified, 100% word sequence
   > The targeted population of this research was managerial-level employees who are working in four- and five-star luxury hotels located in metropolitan cities of India.
   Ctrl+F: „The targeted population of this research was managerial-level“
   → Backs country_region = India and industry = hospitality (four/five-star luxury hotels).

2. **sample, method, industry** — p. 1954 (PDF p. 1) — ✓ verified, 100% word sequence
   > Data were collected via structured questionnaires from 312 valid responses from luxury hotels offering lodging and food services, and the hypotheses were tested using structural equation modelling.
   Ctrl+F: „Data were collected via structured questionnaires from 312“
   → Backs method = survey-SEM and the coded sample wording (312 valid responses, luxury hotels, lodging + food services).

3. **sample, method** — p. 1962 (PDF p. 9) — ✓ verified, 100% word sequence
   > After removing incomplete and extreme responses, 312 valid samples were analysed using SEM in AMOS 25.0 to examine the proposed relationships between the determinants of AI adoption in luxury hotels and SP.
   Ctrl+F: „incomplete and extreme responses, 312 valid samples were“
   → Confirms the 312 analysed responses and covariance-based SEM as the evidence-generating method.

4. **method, quality_notes** — p. 1961 (PDF p. 8) — ✓ verified, 100% word sequence
   > The research design that was used was quantitative, cross-sectional, to examine the interrelationships between the latent constructs developed in this study in a systematic manner
   Ctrl+F: „The research design that was used was quantitative,“
   → Backs the 'cross-section' part of quality_notes.

5. **ai_measure** — p. 1961 (PDF p. 8) — ✓ verified, 100% word sequence
   > This study analyses the managers' intentions regarding the use of AI in luxury hotels.
   Ctrl+F: „This study analyses the managers’ intentions regarding the“
   → The AI-side construct is a managerial survey construct (intention for the adoption of AI), matching the coded survey construct.

6. **ai_measure, outcome_construct, performance_measure** — p. 1956 (PDF p. 3) — ✓ verified, 100% word sequence
   > Third, it assesses the downstream impact of AI adoption intention on service performance outcomes, namely efficiency, responsiveness, and customer satisfaction.
   Ctrl+F: „downstream impact of AI adoption intention on service“
   → AI adoption intention as predictor and service performance (efficiency, responsiveness, customer satisfaction) as the coded performance outcome.

7. **performance_measure, conditions, theoretical_lens** — p. 1958 (PDF p. 5) — ✓ verified, 100% word sequence
   > The six antecedents hypothesised here are expected to positively affect IAAI, which, in turn, should improve SP, as measured by service quality, responsiveness, operational efficiency, and customer satisfaction.
   Ctrl+F: „antecedents hypothesised here are expected to positively affect“
   → Model structure: the TAM/TOE factors are antecedents of adoption intention, not moderators or mediators of the AI-to-performance link, so conditions is correctly empty per the adjudicated decision.

8. **performance_measure, effect_direction, key_finding** — p. 1968 (PDF p. 15) — ✓ verified, 100% word sequence
   > Moreover, the use of AI shows a significant benefit of a positive impact on the service performance, increasing efficiency, responsiveness, and customer satisfaction.
   Ctrl+F: „Moreover, the use of AI shows a significant“
   → Conclusion's own statement of the positive AI-to-service-performance effect.

9. **performance_measure, quality_notes** — p. 1970 (PDF p. 17) — ✓ verified, 100% word sequence
   > SP 1: AI adoption will increase the hotel's service performance SP 2: Customers will be more satisfied with improving service performance
   Ctrl+F: „SP 1: AI adoption will increase the hotel’s“
   → The SP items (Table A1) show service performance is a perceptual, expectation-worded survey scale - backing performance_measure and the 'perceptual' quality note.

10. **effect_direction** — p. 1964 (PDF p. 11) — ✓ verified, 93% word sequence
   > Hypothesis (H7) tested the relationship between IAAI and SP, and the hypothesis was supported.
   Ctrl+F: „Hypothesis (H7) tested the relationship between IAAI and“
   → H7 (AI adoption intention -> service performance) supported; Table 1 (p.10) reports the positive estimate 0.346*** - a positive main effect, matching direction = positive.

11. **key_finding** — p. 1954 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study demonstrates that perceived ease of use, competitive pressure, robust IT infrastructure and supportive government policies significantly drive AI adoption, thereby enhancing service performance.
   Ctrl+F: „This study demonstrates that perceived ease of use,“
   → The abstract sentence the coded key_finding condenses (ease of use, competitive pressure, infrastructure, policy support as drivers).
   **⚠ TENSION:** The coded key_finding lists infrastructure among the positive drivers, following this abstract claim - but the paper's own Table 1 (p.10) reports the ITI -> adoption-intention estimate as negative (-0.142, p = 0.020, still labeled 'Supported'), and the discussion admits 'the undesirable correlation between ITI and adoption intention' (p.13). Paper-internal inconsistency the author should see before citing infrastructure as a positive driver.

12. **key_finding** — p. 1954 (PDF p. 1) — ✓ verified, 100% word sequence
   > These factors also supplement each other: technological innovations enable new functionality, organisational preparation prepares for implementation and exogenous factors accelerate adoption processes, all together building significant momentum for the digital transformation of the hospitality industry.
   Ctrl+F: „These factors also supplement each other: technological innovations“
   → Backs the 'jointly create momentum' phrasing of the coded key_finding.

13. **theoretical_lens** — p. 1954 (PDF p. 1) — ✓ verified, 100% word sequence
   > utilising the technology acceptance model (TAM) and the technology-organisational-environmental (TOE) framework to understand how Industry 4.0 pressures drive the integration of emerging technologies
   Ctrl+F: „technology acceptance model (TAM) and the technology-organisational-environmental (TOE)“
   → Abstract names the combined TAM + TOE lens coded in theoretical_lens.

14. **quality_notes** — p. 1968 (PDF p. 15) — ✓ verified, 100% word sequence
   > The survey was done at one point in time, so it doesn't show how the use of AI has changed over time.
   Ctrl+F: „The survey was done at one point in“
   → Authors' own limitation statement backing the cross-section quality note.

**⚠ ROW CHECK:** Three notes: (1) key_finding tension - the abstract (and conclusion) claim IT infrastructure as a positive adoption driver, but Table 1's ITI estimate is negative (-0.142, p=0.020) and the discussion calls it an 'undesirable correlation' (p.13); PU and TMS paths are not supported either. The coded sentence mirrors the abstract, but the author should know the paper is internally inconsistent on the infrastructure driver. (2) ai_measure nuance: the measured construct is intention for the adoption of AI (IAAI, survey scale after Chatterjee et al. 2021), i.e. adoption intention rather than realized adoption; SP is likewise expectation-worded. (3) Emptiness confirmed: conditions correctly empty (TAM/TOE factors are adoption antecedents per the adjudicated decision, no moderators/mediators on IAAI->SP); ca_measure correctly empty ('competitive advantage' appears only as implications rhetoric, e.g. 'competitive advantage entrenchment' p.1, no CA construct measured). The 'PROPOSED(batch)' half of quality_notes is adjudication commentary, not source-based, and is deliberately not quote-evidenced.

---

## S62 — Patel P.C. (2026) — Technological Forecasting and Social Change (AJG 3)

DOI: 10.1016/j.techfore.2026.124538 · status: final · PDF: `Patel_2026_j-techfore-2026-124538.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | 1,306 AI-scored service patents (of 758k patents) from 3,899 manufacturing firms, 1980-2020; matched-pair robustness |
| method | event study |
| ai_measure | patents (AI score of service technology patents) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | stock market reaction to patent grants (negative abnormal returns) |
| ca_measure | — |
| effect_direction | negative |
| conditions | idiosyncratic volatility mitigates the negative reaction; tangibility does not; effects only in 2010s/2020s (evolving market perception) |
| key_finding | Markets react NEGATIVELY to AI-heavy service patents in manufacturing - a caution against assuming short-term market value from AI servitization. |
| *not printed (coding data only)* | |
| theoretical_lens | transaction cost economics + organizational information processing |
| industry | manufacturing |
| quality_notes | Long panel, robust; important negative-evidence anchor |
| coding_status | final |

### Evidence

1. **country_region, industry** — p. 20 (PDF p. 20) — ✓ verified, 100% word sequence
   > Finally, the study's findings are based on a sample of US manufacturing firms during a specific time period.
   Ctrl+F: „Finally, the study's findings are based on a“
   → Authors state the sample is US manufacturing firms, backing country_region = USA and industry = manufacturing.

2. **sample, industry** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > Based on casewise deletion, the final sample includes 759,449 patents, 1306 service technology patents, and 758,143 non-service technology patents from 3899 manufacturing firms from 1980q1 to 2020q4.
   Ctrl+F: „on casewise deletion, the final sample includes 759,449“
   → Exact sample composition matches the coded 1,306 AI-scored service patents of ~758k patents from 3,899 manufacturing firms, 1980-2020.

3. **method, performance_measure** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The stock market reaction signifies the abnormal change in the firm's market capitalization on the day of the patent grant.
   Ctrl+F: „signifies the abnormal change in the firm's market“
   → The dependent variable is a grant-day abnormal-return measure (KPSS), backing method = event study and the stock-market-reaction performance measure.

4. **ai_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > In our study, we take the standardized factor score of the AI scores on each of these AI dimensions to create a composite AI score for each patent.
   Ctrl+F: „In our study, we take the standardized factor“
   → AI is measured as a composite AI score of patents (AIPD), matching the coded ai_measure.

5. **outcome_construct, effect_direction, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on transaction cost economics and organizational information processing theory, we challenge the espoused benefits of AI in servitization by demonstrating that stock market reactions to service technology patents with high AI scores are negative.
   Ctrl+F: „Drawing on transaction cost economics and organizational information“
   → Abstract names both coded theories (TCE + OIPT) and states the negative market reaction that anchors effect_direction and the performance outcome.

6. **outcome_construct, quality_notes** — p. 19 (PDF p. 19) — ✓ verified, 100% word sequence
   > Second, the study's focus on short-term stock market reactions as the primary measure of firm performance limits the understanding of the long-term impact of AI-enabled service innovation.
   Ctrl+F: „Second, the study's focus on short-term stock market“
   → Authors call the stock market reaction their measure of firm performance (outcome_construct = performance) and admit the short-term-focus limitation.

7. **performance_measure, effect_direction** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > In model 8 in Table 4 and Fig. 1(a), service technology patents with higher AI scores realize a negative market reaction
   Ctrl+F: „Fig. 1(a), service technology patents with higher AI“
   → Main H1 result: significant negative stock market reaction to high-AI service patents, backing effect_direction = negative.

8. **effect_direction, key_finding** — p. 20 (PDF p. 20) — ✓ verified, 100% word sequence
   > Our findings reveal short-term negative stock market reactions to AI-based service patents in manufacturing firms, with this pattern strengthening from the 2010s onward as AI technologies matured.
   Ctrl+F: „stock market reactions to AI-based service patents in“
   → Authors' own concluding statement of the central result, matching the coded key_finding and negative direction.

9. **conditions** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > we find that idiosyncratic volatility mitigates this negative reaction, while tangibility shows no such effect.
   Ctrl+F: „this negative reaction, while tangibility shows no such“
   → Backs the coded conditions: idiosyncratic volatility mitigates, tangibility does not.

10. **conditions** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > While consistently negative, the effect becomes statistically significant only from 2010 onward, with the magnitude increasing over time.
   Ctrl+F: „While consistently negative, the effect becomes statistically significant“
   → Decade-wise analysis backs the coded temporal condition: effects only significant in the 2010s/2020s (evolving market perception).

11. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study cautions against assuming short-term market value of AI service innovations in manufacturing.
   Ctrl+F: „This study cautions against assuming short-term market value“
   → Backs the coded key_finding's framing as a caution against assuming short-term market value from AI servitization.

12. **quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 89% word sequence
   > Results hold across matched-pair sampling, non-linear effects testing, fixed-effects individual slopes, and alternative moderator analyses.
   Ctrl+F: „across matched-pair sampling, non-linear effects testing, fixed-effects individual“
   → Backs the 'robust' part of quality_notes: the paper's battery of robustness checks.

*Row check OK: quality_notes 'important negative-evidence anchor' is coder commentary, not source-based; 'long panel, robust' is evidenced (1980q1-2020q4 sample + robustness quote). ca_measure empty is correct: no CA construct measured; 'competitive edge' appears only as theory-section rhetoric. Minor nuance: in the matched-pair robustness sample all three hypotheses find support (i.e., tangibility becomes significant there), but the paper's headline conclusion keeps tangibility as a non-mitigator, consistent with the coded condition.*

---

## S63 — Renfei C. et al. (2026) — Technovation (AJG 3)

DOI: 10.1016/j.technovation.2025.103429 · status: final · PDF: `Renfei_2026_j-technovation-2025-103429.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 292 valid responses (295 distributed, two-stage collection; pretest 100/85), 120 Chinese manufacturing enterprises, PLS-SEM |
| method | survey-SEM |
| ai_measure | survey construct (AI capabilities: perceptive, predictive, prescriptive) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | corporate sustainability performance incl. explicit economic dimension (EP01-EP04: cost reduction, waste revenue, spin-offs) |
| ca_measure | — |
| effect_direction | positive |
| conditions | prescriptive capabilities FAIL (component of AI-capability bundle null); firm type boundary: Industry-4.0 manufacturers 0.58*** vs traditional significantly WEAKER (but not null) |
| key_finding | AI capabilities raise sustainability (incl. economic) performance mainly in Industry-4.0-ready manufacturers - prescriptive AI fails, and traditional firms barely benefit. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capabilities + sustainable development theory |
| industry | manufacturing |
| quality_notes | Per full-text verdict: include (economic dimension confirmed); perceptual \| PROPOSED(batch): Traditional firms weaker-not-null + main effect significant -> positive per Shi rule; prescriptive-null stays in conditions |
| coding_status | final |

### Evidence

1. **country_region, sample, method, industry** — p. 2 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 26% word sequence
   > this study uses data from a questionnaire survey of 292 individuals from 120 Chinese manufacturing firms to develop a partial least squares structural equation model (PLS-SEM).
   Ctrl+F: „of 292 individuals from 120 Chinese manufacturing firms“
   → One sentence covers survey-SEM (PLS-SEM), the 292/120 sample, China, and manufacturing.

2. **sample** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > In the first stage, 295 questionnaires were distributed to participants, and in the second stage, 295 of them were returned. 292 valid surveys were received after invalid ones were removed.
   Ctrl+F: „were distributed to participants, and in the second“
   → Backs the coded 292 valid responses with 295 distributed in the two-stage collection.

3. **sample** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > In the pre-test survey, 100 questionnaires were distributed in the first stage and 85 were returned
   Ctrl+F: „In the pre-test survey, 100 questionnaires were distributed“
   → Backs the coded pretest detail (100 distributed / 85 returned).

4. **sample, method** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > this study employs a two-stage approach to data investigation.
   Ctrl+F: „this study employs a two-stage approach to data“
   → Confirms the coded two-stage collection design (AIC in stage 1, CSP in stage 2).

5. **ai_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > The study divided AIC into three sub-dimensions treated as reflective latent constructs in the PLS-SEM model: perceptive capabilities, predictive capabilities, and prescriptive capabilities.
   Ctrl+F: „sub-dimensions treated as reflective latent constructs in the“
   → AI is a survey construct with the three coded sub-capabilities (perceptive, predictive, prescriptive), adopted from Sjodin et al. (2023).

6. **outcome_construct, performance_measure** — p. 8 (PDF p. 8) — ⚠ not machine-confirmed on page — open the page, 54% word sequence
   > CSP was measured using three dimensions, namely economic performance, environmental performance, and social performance, mainly referring to the categorization of CSP by Shang et al. (2020).
   Ctrl+F: „CSP was measured using three dimensions, namely economic“
   → The outcome is corporate sustainability performance with an explicit economic dimension, matching the coded performance_measure.

7. **performance_measure** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > EP02: Reduced costs of inputs for same level of outputs EP03: Sold waste products for revenue EP04: Created spin-off technologies that could be profitably applied to other areas of the business
   Ctrl+F: „EP02: Reduced costs of inputs for same level“
   → Appendix A economic-performance items back the coded detail (cost reduction, waste revenue, spin-offs) that justified inclusion.

8. **effect_direction** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > The results in Table 5 show that AIC has a positive effect on CSP ( β = 0.49; p < 0.001).
   Ctrl+F: „The results in Table 5 show that AIC“
   → Significant positive main effect of AIC on CSP backs effect_direction = positive per the main-effect rule.

9. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The findings reveal that AIC significantly enhances CSP through a tiered enabling mechanism, but prescriptive capabilities fail to achieve their intended effects.
   Ctrl+F: „reveal that AIC significantly enhances CSP through a“
   → Authors' own central-result statement matching the coded key_finding (enhancement plus prescriptive failure).

10. **conditions** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > In hypothesis 1c, the coefficient of the impact of the firm's prescriptive capabilities on CSP is 0.28, with a p-value higher than 0.05, which does not prove the significance of the relationship.
   Ctrl+F: „1c, the coefficient of the impact of the“
   → Backs the coded condition that the prescriptive component of the AI-capability bundle is null.

11. **conditions** — p. 9 (PDF p. 9) — ✓ verified, 69% word sequence
   > In the traditional manufacturing samples, the positive effect of AIC on CSP is significant, but the coefficient is only 0.29*, which is lower than the full sample result
   Ctrl+F: „samples, the positive effect of AIC on CSP“
   → Backs the coded firm-type boundary: traditional manufacturers significantly weaker but not null (basis of the adjudicated positive-per-Shi-rule decision).

12. **conditions** — p. 9 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 44% word sequence
   > the positive effect of AIC in the context of Industry 4.0 manufacturing firms is significant and stronger, with a coefficient higher than the full-sample result at 0.58 and significant at p < 0.001.
   Ctrl+F: „effect of AIC in the context of Industry“
   → Backs the coded 0.58*** for Industry-4.0 manufacturers as the strong end of the firm-type boundary condition.

13. **theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study is based on dynamic capabilities theory (DCT) and sustainable development theory, and reveals the micro-mechanisms and boundary conditions of AIC driving CSP.
   Ctrl+F: „theory (DCT) and sustainable development theory, and reveals“
   → Abstract names both coded lenses: dynamic capabilities theory and sustainable development theory.

14. **quality_notes** — p. 9 (PDF p. 9) — ✓ verified, 100% word sequence
   > Specifically, all items were coded on a Likert scale ranging from 1 (Strongly Disagree) to 5 (Strongly Agree).
   Ctrl+F: „Specifically, all items were coded on a Likert“
   → Backs the 'perceptual' quality note: all constructs are Likert self-reports by senior managers.

15. **quality_notes** — p. 12 (PDF p. 12) — ✓ verified, 100% word sequence
   > This study is mainly based on cross-sectional data and uses static analysis methods.
   Ctrl+F: „based on cross-sectional data and uses static analysis“
   → Author-admitted limitation supporting the perceptual/cross-sectional caution in quality_notes.

*Row check OK: Adjudicated row (brief: PROPOSED positive per Shi rule, accepted in batch) - full text supports it: main effect 0.49***, traditional subsample weaker (0.29*) but not null. ca_measure empty is correct: 'competitive advantage' appears only in theory framing ('from competitive advantage to sustainability'), no CA construct measured. The PROPOSED(batch) part of quality_notes is adjudication commentary, not source-based. Minor source oddity: Appendix A mislabels the prescriptive-capabilities block (PC3) as 'Predictive capabilities'.*

---

## S64 — Singh A. et al. (2026) — Business Strategy and the Environment (AJG 3)

DOI: 10.1002/bse.71134 · status: final · PDF: `Singh_2026_bse-71134.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | S&P 500 companies, 2000-2024; system-GMM + PSM robustness |
| method | panel econometrics |
| ai_measure | AI patents granted per year, identified via PATENTSCOPE AI Index methodology (1 SD = 115.66 patents -> Tobin Q +0.058, ~3% firm value) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | ROA + firm value |
| ca_measure | — |
| effect_direction | conditional |
| conditions | small positive ROA effect, stronger for R&D-intensive firms; firm-value gains ONLY for firms with good sustainability metrics; stronger under Democratic administrations (political environment as condition) |
| key_finding | AI innovation pays modestly and unevenly: R&D intensity, sustainability credentials and even the political climate condition whether markets reward it. |
| *not printed (coding data only)* | |
| theoretical_lens | none explicit (innovation economics + political economy) |
| industry | cross-industry (large caps) |
| quality_notes | Long panel; unusual political-context condition |
| coding_status | final |

### Evidence

1. **country_region, sample, method, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This study analyzes how artificial intelligence (AI) innovation affects firms' financial performance and value among S&P 500 companies in the US market, using a panel data regression model for the period 2000-2024.
   Ctrl+F: „This study analyzes how artificial intelligence (AI) innovation“
   → Abstract states panel regression, S&P 500 sample, US market, and the long 2000-2024 window ('long panel' in quality_notes).

2. **country_region, sample** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > in the US market, we select firms in the S&P 500 as of December 31, 2024, as our sample.
   Ctrl+F: „US market, we select firms in the S&P“
   → Confirms the coded sample (S&P 500 companies) and country (USA).

3. **method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The results remain robust to multiple checks, including system-GMM and PSM.
   Ctrl+F: „The results remain robust to multiple checks, including“
   → Backs the coded 'system-GMM + PSM robustness' in the sample/method description.

4. **ai_measure** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > Following prior literature, we measure AI innovation by the number of AI-related patents granted to S&P 500 firms
   Ctrl+F: „Following prior literature, we measure AI innovation by“
   → AI is measured as AI patents granted per year, matching the coded ai_measure.

5. **ai_measure** — p. 5 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 20% word sequence
   > We utilize the methodology outlined in the PATENTSCOPE Artificial Intelligence Index to identify such patents.
   Ctrl+F: „outlined in the PATENTSCOPE Artificial Intelligence“
   → Backs the coded PATENTSCOPE AI Index identification methodology.

6. **ai_measure, performance_measure** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > An increase in AI patents by one standard deviation (115.66 from Table 1) leads to the Tobin's Q value of the firm rising by 0.058, translating to a 3% increase in firm value
   Ctrl+F: „patents by one standard deviation (115.66 from Table“
   → Backs the coded effect-size detail: 1 SD = 115.66 patents, Tobin's Q +0.058, ~3% firm value.

7. **outcome_construct, performance_measure** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The dependent variable selected for the first hypothesis is return on assets (RoA).
   Ctrl+F: „The dependent variable selected for the first“
   → Backs the ROA half of the coded performance_measure.

8. **outcome_construct, performance_measure** — p. 4 (PDF p. 4) — ✓ verified, 86% word sequence
   > For measuring firm value, we use Tobin's Q as our primary dependent variable.
   Ctrl+F: „For measuring firm value, we use Tobin's Q“
   → Backs the firm-value half of the coded performance_measure (Tobin's Q).

9. **effect_direction, conditions** — p. 8 (PDF p. 8) — ✓ verified, 86% word sequence
   > We observe that while overall, AI innovation does not significantly impact firm value, there is a small but significant positive impact when sustainable business operations support the innovation.
   Ctrl+F: „We observe that while overall, AI innovation does“
   → Null firm-value baseline with a positive effect only under the sustainability condition backs effect_direction = conditional.

10. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study finds mixed evidence of a small positive impact of AI innovation on firms' return on assets, with the effect stronger for more R&D-intensive firms.
   Ctrl+F: „a small positive impact of AI innovation on“
   → Backs the coded 'small positive ROA effect, stronger for R&D-intensive firms' condition and the 'pays modestly' key_finding.

11. **conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The findings demonstrate that AI innovation increases firm value for companies that perform well on sustainability-related metrics.
   Ctrl+F: „The findings demonstrate that AI innovation increases firm“
   → Backs the coded condition that firm-value gains occur only for firms with good sustainability metrics.

12. **conditions, key_finding, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > This effect is stronger under Democratic administrations than under Republican governments, indicating the influence of political environments on the market's perception of firms' actions.
   Ctrl+F: „This effect is stronger under Democratic administrations than“
   → Backs the coded political-environment condition (stronger under Democratic administrations).

13. **conditions** — p. 8 (PDF p. 8) — ⚠ not machine-confirmed on page — open the page, 24% word sequence
   > firms focusing on sustainability, particularly environmental sustainability, experience an increase in firm value with AI innovation, while other firms experience no effect on firm value.
   Ctrl+F: „sustainability, experience an increase in firm value with“
   → Results section confirms the sustainability boundary: value gains ONLY for sustainable firms, others get no effect.

14. **conditions** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > firms with higher ESG and EPS scores exhibit an approximate 8% relative increase in firm value for each standard deviation increase in AI patents during Democratic regimes.
   Ctrl+F: „and EPS scores exhibit an approximate 8% relative“
   → Quantifies the political-administration condition (8% relative value increase under Democratic regimes).

15. **theoretical_lens** — p. 3 (PDF p. 3) — ⚠ not machine-confirmed on page — open the page, 58% word sequence
   > Complementarities research suggests that technological innovation leads to enhanced firm performance when it is combined with aligned organizational capabilities
   Ctrl+F: „leads to enhanced firm performance when it is“
   → Backs the 'innovation economics' half of the coded lens: hypotheses build on complementarities research, not one named theory.

16. **theoretical_lens** — p. 4 (PDF p. 4) — ⚠ not machine-confirmed on page — open the page, 58% word sequence
   > Institutional theory (North 1990) also suggests that the institutional environment (in the form of regulations, laws, and policies) influences firm outcomes and market valuations.
   Ctrl+F: „suggests that the institutional environment (in the form“
   → Backs the 'political economy' half of the coded lens: the political-administration hypothesis draws on institutional arguments.

17. **industry** — p. 1–2 (PDF p. 1) — ✓ verified, 100% word sequence
   > These are the leading 500 US public companies, collectively accounting for approximately 80% of the US equity market capitalization
   Ctrl+F: „These are the leading 500 US public“
   → Backs industry = cross-industry (large caps): the sample spans the largest listed firms across sectors.

18. **industry** — p. 4 (PDF p. 4) — ✓ verified, 82% word sequence
   > Following prior literature, we have excluded financial sector firms from our study due to differences in their capital structure, accounting practices, and regulatory requirements compared to other firms
   Ctrl+F: „excluded financial sector firms from our study due“
   → Qualifies the cross-industry coding: financial firms are excluded, a standard restriction.

*Row check OK: theoretical_lens coded 'none explicit' is defensible: the paper cites complementarities research, TOE, institutional theory, and value-enhancing vs. shareholder theory in passing rather than one framing lens - the two lens quotes document the ingredients. quality_notes 'unusual political-context condition' is coder commentary; the political condition itself is source-backed. ca_measure empty is correct: 'competitive advantage' appears only as motivation/rhetoric (e.g., citing Kemp 2024), no CA construct is measured. Direction note for the author: ROA shows a small positive main effect while firm value is null overall and positive only under sustainability/political conditions; the final coding 'conditional' rests on the firm-value null baseline, consistent with the frozen rules.*

---

## S65 — Song X. et al. (2026) — Finance Research Letters (AJG 2)

DOI: 10.1016/j.frl.2026.109684 · status: final · PDF: `Song_2026_j-frl-2026-109684.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | USA |
| sample | US firms 2018-2023; BERT-classified AI disclosures vs AI patent portfolios |
| method | panel econometrics |
| ai_measure | text-vs-patents gap (unsubstantiated AI claims = AI washing) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | market reactions + long-term operational performance |
| ca_measure | — |
| effect_direction | negative |
| conditions | time path: short-lived positive investor reaction, then negative BHAR + sustained underperformance; substantiation gap (claims vs patents) is the treatment |
| key_finding | AI talk without AI substance backfires: markets initially reward the narrative, then punish rhetoric that outpaces implementation. |
| *not printed (coding data only)* | |
| theoretical_lens | narrative economics / signaling |
| industry | cross-industry |
| quality_notes | Complements Basnet (S27); disclosure-integrity condition \| PROPOSED(batch): Focal treatment = AI overclaiming; its net/long-run effect is negative (markets punish) -> negative per main-effect rule |
| coding_status | final |

### Evidence

1. **country_region, sample, ai_measure, effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 78% word sequence
   > Using BERT-based text classification and AI patent data for U.S. firms (2018-2023), we find that such narratives initially attract investors but ultimately yield negative market reactions and sustained underperformance.
   Ctrl+F: „data for U.S. firms (2018–2023), we find that“
   → Abstract covers the coded sample (US firms 2018-2023), the BERT-vs-patents measurement, the net negative direction, and the coded time-path condition (initial attraction, then punishment).

2. **country_region, sample, industry** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > we collect Form 10-K filings of U.S. publicly listed firms from 2018 to 2023 using the SEC's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system.
   Ctrl+F: „we collect Form 10-K filings of U.S. publicly“
   → Backs sample = US listed firms 2018-2023 (all sectors, hence cross-industry).

3. **method** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > We begin with an event study to assess initial investor reactions to AI overclaiming, measured by buy-and-hold abnormal returns (BHAR) around 10-K filing dates.
   Ctrl+F: „by buy-and-hold abnormal returns (BHAR) around 10-K filing“
   → Documents the descriptive event-study module preceding the panel identification.

4. **method** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > To give support to the causal interpretation, we implement a difference-in-differences (DiD) design.
   Ctrl+F: „To give support to the causal interpretation, we“
   → The causal AI-outcome evidence comes from DiD (plus IV) panel regressions with firm and year fixed effects, backing method = panel econometrics.

5. **ai_measure** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > Using BERT-based classification and patent evidence, we differentiate speculative 'Will-Do AI' from substantive 'Done AI'. The final model achieves an accuracy of 0.87.
   Ctrl+F: „we differentiate speculative “Will-Do AI” from substantive “Done“
   → Backs the coded ai_measure: BERT-classified AI disclosures benchmarked against actual implementation evidence.

6. **ai_measure, conditions** — p. 3 (PDF p. 3) — ✓ verified, 100% word sequence
   > Firms with above-industry disclosure but below-industry AI patenting are classified as overclaiming.
   Ctrl+F: „below-industry AI patenting are classified as overclaiming.“
   → Defines the treatment as the text-vs-patents substantiation gap, matching ai_measure and the coded condition that the gap is the treatment.

7. **outcome_construct, performance_measure** — p. 2 (PDF p. 2) — ⚠ not machine-confirmed on page — open the page, 18% word sequence
   > To examine market responses, we use BHAR and CAR to capture short-term investor reactions and sales growth to measure the long-term effects of speculative AI disclosures.
   Ctrl+F: „we use BHAR and CAR to capture short-term“
   → Backs performance_measure = market reactions + long-term operational performance (sales growth); outcomes are performance, no CA construct.

8. **performance_measure, effect_direction** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > if a firm engages in AI overclaiming in its 10-K filing, the release of the 10-K is followed by a 1.6 % decline in CAR and a 1.4 % decline in BHAR
   Ctrl+F: „if a firm engages in AI overclaiming in“
   → Quantifies the negative short-term market reaction.

9. **performance_measure, effect_direction** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > overclaiming AI adoption would reduce sales growth in the following year by 14.7 percentage points.
   Ctrl+F: „overclaiming AI adoption would reduce sales growth in“
   → Backs the sustained operational underperformance half of the negative direction (long-term outcome).

10. **effect_direction** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > The consistently negative and statistically significant coefficients both on CAR and BHAR across all specifications are consistent with market penalties associated with AI overclaiming.
   Ctrl+F: „both on CAR and BHAR across all specifications“
   → Main DiD result: negative market reaction to the focal treatment (AI overclaiming), backing effect_direction = negative.

11. **effect_direction, key_finding** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > This study shows that when firms exaggerate their adoption of artificial intelligence, markets eventually impose discipline.
   Ctrl+F: „This study shows that when firms exaggerate their“
   → Concluding statement of the central result: net punishment of unsubstantiated AI claims.

12. **conditions** — p. 4 (PDF p. 4) — ✓ verified, 100% word sequence
   > However, this optimism fades significantly by day + 1, with returns declining to 1.81 % and becoming statistically insignificant ( p > 0.10) beyond day + 2
   Ctrl+F: „However, this optimism fades significantly by day +1,“
   → Backs the coded time-path condition: short-lived positive investor reaction that fades before the penalty phase.

13. **key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The study highlights that while narratives can mobilize attention, markets ultimately punish rhetoric that outpaces implementation.
   Ctrl+F: „highlights that while narratives can mobilize attention, markets“
   → Authors' own summary sentence matching the coded key_finding (markets punish rhetoric outpacing implementation).

14. **theoretical_lens** — p. 2 (PDF p. 2) — ✓ verified, 100% word sequence
   > This study draws from signaling theory (Spence, 1978, 2002) and narrative economics (Shiller, 2020) to show how markets react when unverifiable AI claims proliferate.
   Ctrl+F: „This study draws from signaling theory (Spence, 1978,“
   → Names both coded lenses: narrative economics and signaling.

*Row check OK: Adjudicated row (brief: PROPOSED negative - net effect of the focal overclaiming treatment; accepted in batch); full text supports it, time path documented in conditions as required. quality_notes ('Complements Basnet (S27); disclosure-integrity condition | PROPOSED(batch)...') is coder/adjudication commentary, not source-based - no quote possible. ca_measure empty is correct: outcomes are CAR/BHAR and sales growth, no competitive-advantage construct. Method note: the paper pairs a descriptive event-study module with DiD and IV-2SLS panel regressions (firm/year FE, two-way clustering); the panel designs carry the causal evidence, consistent with method = panel econometrics.*

---

## S66 — Ullah A. et al. (2026) — International Journal of Information Management (AJG 2)

DOI: 10.1016/j.ijinfomgt.2026.103059 · status: final · PDF: `Ullah_2026_j-ijinfomgt-2026-103059.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China |
| sample | 419 valid responses from 290 manufacturing firms (38% response rate); SEM + LSTM validation |
| method | survey-SEM |
| ai_measure | survey construct (AI adoption) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | organizational performance (survey scale) |
| ca_measure | — |
| effect_direction | positive |
| conditions | team dynamics, corporate innovation capabilities, high-commitment workforce (mediators) |
| key_finding | AI adoption converts into performance where cohesive teams, innovation capability and a committed workforce absorb it - human/organizational enablers unlock the value. |
| *not printed (coding data only)* | |
| theoretical_lens | innovation diffusion theory |
| industry | manufacturing |
| quality_notes | Perceptual; LSTM validation gimmick - treat SEM results as primary |
| coding_status | final |

### Evidence

1. **country_region, sample, method, industry** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using survey data from 419 Chinese manufacturing firms, the study employs structural equation modeling alongside long short-term memory techniques to validate the proposed framework.
   Ctrl+F: „data from 419 Chinese manufacturing firms, the study“
   → Source sentence for the coded sample '419 manufacturing firms; SEM + LSTM validation', China, manufacturing, survey-SEM.

2. **sample** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > In total, 419 valid questionnaires were obtained from 290 firms, yielding a response rate of 38%, which was deemed satisfactory for analysis.
   Ctrl+F: „In total, 419 valid questionnaires were obtained from“
   → Methods-section sample description with response rate.
   **⚠ TENSION:** Methods report 419 valid questionnaires from 290 firms, while the abstract (and the coded sample '419 manufacturing firms') treats 419 as the number of firms - the paper is internally inconsistent; coded cell follows the abstract.

3. **sample, industry** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > The sample firms represented diverse sectors within the manufacturing industry, including automotive, electronics, textiles, machinery, chemicals, and IT.
   Ctrl+F: „The sample firms represented diverse sectors within the“
   → Confirms industry = manufacturing (multiple manufacturing sectors).

4. **method** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > This study used structural equation modeling (SEM) for analysis with Smart-PLS 4 and Python to examine theorized relationships
   Ctrl+F: „This study used structural equation modeling (SEM) for“
   → Backs method = survey-SEM (PLS-SEM in Smart-PLS 4).

5. **ai_measure, outcome_construct, conditions, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on innovation diffusion theory, this study investigates how team dynamics, high-commitment workforces (HCW), and corporate innovation and innovation capabilities (CIIC) mediate the relationship between AI adoption and organizational performance.
   Ctrl+F: „investigates how team dynamics, high-commitment workforces (HCW), and“
   → Abstract names the coded lens (innovation diffusion theory), the AI-adoption construct, the three coded mediators, and the performance outcome.

6. **ai_measure** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > Our measures of AI were divided into two categories: SPAI and GPAI
   Ctrl+F: „Our measures of AI were divided into two“
   → AI adoption is a multi-item survey construct (service-purpose and general-purpose AI), matching the coded ai_measure.

7. **ai_measure, performance_measure, quality_notes** — p. 5 (PDF p. 5) — ⚠ not machine-confirmed on page — open the page, 20% word sequence
   > We used a fivepoint Likert scale ranging from 1 (strongly disagree) to 5 (strongly agree).
   Ctrl+F: „Likert scale ranging from 1 (strongly disagree) to“
   → All constructs including AI adoption and performance are Likert self-reports, backing the 'perceptual' quality note.

8. **outcome_construct, performance_measure** — p. 5 (PDF p. 5) — ✓ verified, 100% word sequence
   > We measured organizational performance using seven items adapted from Boeker and Goodstein (1991) and Le and Ngoc-Khuong (2025).
   Ctrl+F: „We measured organizational performance using seven items adapted“
   → Backs performance_measure = organizational performance survey scale (outcome_construct = performance).

9. **effect_direction** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > In the first model, the path coefficient from AI to OP is 0.719, showing a strong, unified impact.
   Ctrl+F: „from AI to OP is 0.719, showing a“
   → Strong positive AI-to-performance path alongside the mediators: mediated-positive WITH a significant direct path = positive per the frozen rule.

10. **effect_direction, conditions, key_finding** — p. 9 (PDF p. 9) — ⚠ not machine-confirmed on page — open the page, 31% word sequence
   > The findings indicate that AI adoption positively shapes organizational outcomes through these mediators, highlighting that technological benefits are realized not in isolation but through complementary human and organizational mechanisms.
   Ctrl+F: „The findings indicate that AI adoption positively shapes“
   → Authors' own summary: positive AI effect realized through the human/organizational enablers - matching key_finding and direction.

11. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > Overall paths are statistically significant (p < 0.001), positive that HCW, TD, and CIIC each play a mediating role in how AI influences OP.
   Ctrl+F: „Overall paths are statistically significant (p < 0.001), positive“
   → Backs the coded conditions: team dynamics, innovation capabilities, and high-commitment workforce as significant mediators of the AI-performance link.

12. **conditions** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > The Table 3 presents the indirect effect AI → HCW → OP ( β = 0.345, t = 6.677, p = 0.000), the strongest mediation
   Ctrl+F: „The Table 3 presents the indirect effect AI“
   → Quantifies the high-commitment-workforce mediator as the strongest amplifier, matching the coded conditions.

13. **key_finding** — p. 1 (PDF p. 1) — ⚠ not machine-confirmed on page — open the page, 50% word sequence
   > This study contributes to the literature on organizational behavior and technology management by demonstrating how human and organizational enablers unlock the performance-enhancing potential of AI.
   Ctrl+F: „This study contributes to the literature on organizational“
   → Abstract sentence matching the coded key_finding phrase 'human/organizational enablers unlock the value'.

14. **quality_notes** — p. 13 (PDF p. 13) — ✓ verified, 100% word sequence
   > First, the cross-sectional design and reliance on self-reported survey data may introduce common method bias and limit causal inference.
   Ctrl+F: „First, the cross-sectional design and reliance on self-reported“
   → Author-admitted limitation backing the 'perceptual' quality note.

15. **quality_notes** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > However, the Root Mean Squared Error (RMSE) increases significantly from 0.0116 in training to 0.127 in testing, implying that the model encounters larger deviations from actual values in the testing phase.
   Ctrl+F: „increases significantly from 0.0116 in training to 0.127“
   → Authors themselves report weak LSTM test performance, backing the quality note to treat SEM results as primary over the LSTM add-on.

**⚠ ROW CHECK:** One factual discrepancy for the author: the coded sample '419 manufacturing firms' follows the abstract, but the methods section states 419 valid questionnaires from 290 firms (38% response rate) - the paper is internally inconsistent; consider annotating the sample cell as '419 responses / 290 firms'. Everything else checks out. ca_measure empty is correct: 'sustainable competitive advantage' appears only as closing rhetoric, no CA construct measured. effect_direction = positive holds under the mediation rule: the model reports a strong positive AI-to-OP path (0.719) alongside significant indirect effects, so the mediators stay in conditions. 'LSTM validation gimmick' is coder phrasing, but the underlying concern is source-backed (RMSE degradation in testing).

---

## S67 — Wang S. et al. (2026) — International Journal of Information Management (AJG 2)

DOI: 10.1016/j.ijinfomgt.2026.103057 · status: final · PDF: `Wang_2026_j-ijinfomgt-2026-103057.pdf`

| Column | Coded value |
|---|---|
| *Table A.1 columns* | |
| country_region | China + Europe |
| sample | two-wave survey of 357 early-stage ventures (China + Europe); PLS-SEM + IPMA + fsQCA + interviews |
| method | mixed |
| ai_measure | survey construct (AI innovation capability) |
| *Table A.2 columns* | |
| outcome_construct | performance |
| performance_measure | entrepreneurial success (venture performance, survey scale) |
| ca_measure | — |
| effect_direction | conditional |
| conditions | FULL mediation: strategic resilience fully accounts for AI capability -> success relationship (abstract: "fully accounts"); fsQCA equifinal configurations to high performance |
| key_finding | AI capability makes ventures successful only via organizational resilience - the mechanism is organizational, not technological; multiple configurations lead there. |
| *not printed (coding data only)* | |
| theoretical_lens | dynamic capability theory (information-driven resilience) |
| industry | early-stage ventures (cross-industry) |
| quality_notes | Multi-method incl. fsQCA; full mediation is a strong conditional finding \| PROPOSED(batch): Leoni class: mediation fully carries effect |
| coding_status | final |

### Evidence

1. **country_region, sample, method** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Using a multi-method approach, we collected two-wave survey data from 357 early-stage ventures in China and Europe
   Ctrl+F: „two-wave survey data from 357 early-stage ventures in“
   → Confirms two-wave survey, n=357 early-stage ventures, and the China+Europe setting in one sentence.

2. **country_region, sample** — p. 8 (PDF p. 8) — ✓ verified, 100% word sequence
   > The final sample consisted of 357 valid responses (191 Chinese startups and 166 European startups), representing a 51.0% initial response rate and 89.0% valid response rate.
   Ctrl+F: „The final sample consisted of 357 valid responses“
   → Gives the exact n=357 and the China/Europe split behind the coded sample and country_region.

3. **country_region, sample, industry** — p. 5 (PDF p. 5) — ✓ verified, 75% word sequence
   > The research context focuses on early-stage startups ( ≤ 5 years old) in China and Europe that have actively implemented artificial intelligence technologies in their operations and products/services
   Ctrl+F: „The research context focuses on early-stage startups (≤ 5“
   → Confirms the sample is early-stage ventures (≤5 years) in China and Europe that actively implement AI.

4. **method, quality_notes** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Our convergent multi-method design provides complementary evidence: PLS-SEM establishes the mediation hypothesis, IPMA identifies actionable managerial priorities, fsQCA reveals equifinal configurational pathways to high performance, and interviews illuminate the underlying mechanisms.
   Ctrl+F: „Our convergent multi-method design provides complementary evidence: PLS-SEM“
   → Multiple strands (SEM, fsQCA, interviews) each carry outcome evidence, backing method=mixed and the 'multi-method incl. fsQCA' quality note.

5. **method, conditions, key_finding** — p. 13 (PDF p. 13) — ⚠ not machine-confirmed on page — open the page, 13% word sequence
   > This solution reveals six configurations (see Table 7) that consistently lead to high entrepreneurial success, as indicated by consistency values exceeding 0.90.
   Ctrl+F: „six configurations (see Table 7) that consistently lead“
   → Backs the coded 'fsQCA equifinal configurations to high performance' condition and the key finding that multiple configurations lead to success; fsQCA is an outcome-evidence strand of the mixed design.

6. **method** — p. 15 (PDF p. 15) — ✓ verified, 100% word sequence
   > Such remarks strongly reinforce the quantitative finding that strategic resilience mediates the relationship between artificial intelligence innovation capability and entrepreneurial success.
   Ctrl+F: „reinforce the quantitative finding that strategic resilience mediates“
   → The interview study (Study 4) carries outcome-relevant evidence rather than serving only instrument development, so method=mixed stands under the frozen rule.

7. **ai_measure** — p. 3 (PDF p. 3) — ⚠ not machine-confirmed on page — open the page, 29% word sequence
   > Artificial intelligence innovation capability represents an organization's proficiency in integrating, managing, and applying artificial intelligence technologies to enhance information processes
   Ctrl+F: „proficiency in integrating, managing, and applying artificial“
   → Defines the AI innovation capability construct that is the coded ai_measure.

8. **ai_measure** — p. 7 (PDF p. 7) — ✓ verified, 100% word sequence
   > Other items used a seven-point Likert-type scale (1 = strongly disagree; 7 = strongly agree) to capture nuanced perceptions of artificial intelligence-oriented activities and resilience behaviors
   Ctrl+F: „items used a seven-point Likert-type scale (1 = strongly“
   → Shows the AI capability construct is measured by seven-point Likert survey items, backing 'survey construct'.

9. **outcome_construct, performance_measure** — p. 4 (PDF p. 4) — ✓ verified, 77% word sequence
   > Entrepreneurial success represents the extent to which new ventures achieve their desired information-driven performance outcomes, including knowledge-enabled revenue growth, information-based market share expansion, and customer information base development
   Ctrl+F: „Entrepreneurial success represents the extent to which new“
   → The dependent variable is entrepreneurial success defined as venture performance outcomes (growth), backing outcome_construct=performance and the coded performance_measure.

10. **outcome_construct, theoretical_lens** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > Drawing on dynamic capability theory, we examine how early-stage ventures transform AI capabilities into adaptive capacity and competitive advantage.
   Ctrl+F: „Drawing on dynamic capability theory, we examine how“
   → Shows 'competitive advantage' appears only as theory-section framing; no distinct CA construct is measured, so outcome_construct=performance and empty ca_measure are correct per case law.

11. **performance_measure** — p. 6 (PDF p. 6) — ✓ verified, 100% word sequence
   > Entrepreneurial success (Table 2) is measured using objective data from the past year.
   Ctrl+F: „using objective data from the past year.“
   → Locates the ES measure in the questionnaire (Table 2: one-year revenue, market-share, and customer-base growth); authors call the survey-collected growth items 'objective data' - nuance to the coded 'survey scale'.

12. **effect_direction, conditions** — p. 17 (PDF p. 17) — ✓ verified, 100% word sequence
   > strategic resilience fully mediates the relationship between AI innovation capability and entrepreneurial success (indirect effect β = 0.409, p < 0.001), with no significant direct path from AI capability to success
   Ctrl+F: „the relationship between AI innovation capability and entrepreneurial“
   → Full mediation with an explicitly non-significant direct path - exactly the frozen-rule case for effect_direction=conditional (Leoni class) and the coded FULL-mediation condition.

13. **effect_direction, conditions, key_finding** — p. 1 (PDF p. 1) — ✓ verified, 100% word sequence
   > The mediating effect of strategic resilience is robust and fully accounts for the AI capability -success relationship, indicating that the mechanism through which AI investments generate performance returns is fundamentally organizational rather than technological
   Ctrl+F: „The mediating effect of strategic resilience is robust“
   → The abstract's 'fully accounts for' sentence cited in the coded conditions; also states the key finding that the mechanism is organizational, not technological.

14. **theoretical_lens** — p. 2 (PDF p. 2) — ✓ verified, 97% word sequence
   > We ground our investigation in dynamic capability theory (Barreto, 2010; Teece et al., 1997; Teece, 2007), which provides a foundational framework for understanding how organizations develop and reconfigure information competencies
   Ctrl+F: „We ground our investigation in dynamic capability theory“
   → Names dynamic capability theory as the study's grounding framework, matching the coded lens.

15. **theoretical_lens** — p. 3 (PDF p. 3) — ✓ verified, 90% word sequence
   > We use the term information-driven resilience to capture the process through which ventures leverage AI innovation capability -their proficiency in integrating, managing, and applying AI technologies -to build strategic resilience
   Ctrl+F: „We use the term information-driven resilience to capture“
   → Evidences the 'information-driven resilience' qualifier in the coded theoretical_lens.

16. **industry** — p. 5 (PDF p. 5) — ✓ verified, 78% word sequence
   > The sample spans multiple industries including information technology, healthcare, manufacturing, and financial services, allowing for broader generalizability while controlling for industry-specific effects
   Ctrl+F: „financial services, allowing for broader generalizability while“
   → Backs the 'cross-industry' part of the coded industry value.

*Row check OK: All non-empty columns evidenced. ca_measure emptiness confirmed: 'competitive advantage' appears only as framing/rhetoric (abstract, discussion); the measured DV is entrepreneurial success (growth metrics). effect_direction=conditional is textually exact: p.17 states full mediation 'with no significant direct path from AI capability to success'. quality_notes is only partly source-based - 'multi-method incl. fsQCA' is covered by the p.1 method quote; the rest ('full mediation is a strong conditional finding | PROPOSED(batch): Leoni class') is coder/adjudication commentary, not quotable. Minor wording nuance for the author: performance_measure says 'survey scale', while the paper describes the questionnaire-embedded ES items as one-year objective growth percentages (revenue, market share, customer base; Table 2, p.6-7) rather than Likert perceptions - survey-collected, so the code is defensible, no change implied.*

