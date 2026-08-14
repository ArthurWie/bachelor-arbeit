# Umformulierte Appendix-Zellen — Review (29. Juli 2026)

Nur Wortlaut. Kodierte Werte in coding_table.csv unveraendert; FACT_SHEET bleibt gueltig.
Aendern/verwerfen: Zeile in corpus/appendix_overrides.tsv editieren oder loeschen, dann Skript neu laufen lassen.

**NACHTRAG (14. Aug 2026, Claude): alle Abkuerzungsaufloesungen gegen die Volltexte
geprueft** (Definitionsstellen per pdfplumber aus den PDFs gezogen; Sun 2022 spaltenweise).
Ergebnis: S04, S05, S17, S24–S27, S37–S48, S55–S67 exakt bestaetigt. Vier
Praezisionskorrekturen in appendix_overrides.tsv, Tabelle regeneriert (Self-Checks gruen):

- **S07 Leoni:** Konstrukt heisst „manufacturing *firm* performance" (MFP) — Wort ergaenzt.
- **S10 Sun:** EV/RV = „economic value" und „relationship value" (nicht „relational");
  die Appendix-Fassung hatte deren Null-Pfade zu CA (H5a/b, H6a/b nicht gestuetzt)
  stillschweigend weggelassen — jetzt: „neither value co-creation directly nor the
  economic and relationship value it creates significantly affects competitive advantage".
- **S21 Sullivan:** ARMC = „adaptive response to market change*s*" (Plural) — korrigiert.
- **S28 Bin-Nashwan:** GIC = „green *intellectual* capital" — Wort ergaenzt.

## S04 Chatterjee S. (2022) — conditions

**kodiert:** technology turbulence (negative moderator on ADM->BRS -0.23* and OPE->BRS -0.32***); leadership support (positive moderator on BRS->FP 0.29*); main effect ACRM->FP 0.53*** unconditional

**Appendix:** technology turbulence weakens the paths from automated decision-making and operational efficiency to B2B relationship satisfaction (negative moderator); leadership support strengthens the path from satisfaction to firm performance (positive moderator); the main effect of AI-CRM on firm performance is unconditional

## S05 Hossain M.A. (2022) — conditions

**kodiert:** mediators: market sensing/seizing/reconfiguring (carry MAC->SCA fully, H3a-c); moderator: AI adoption strengthens MAC->sensing (0.104*), ->seizing (0.131*), ->reconfiguring (0.128*)

**Appendix:** mediators: market sensing, seizing and reconfiguring carry the effect of marketing analytics capability on sustained competitive advantage in full; moderator: AI adoption strengthens all three capability paths

## S07 Leoni L. (2022) — conditions

**kodiert:** FULL mediation via knowledge management processes: direct AI->MFP 0.006 n.s. (H2 rejected), AI->KMPs 0.48***, KMPs->MFP 0.51***; also AI->SCR direct n.s.; firm size -> AI maturity (0.26**)

**Appendix:** full mediation through knowledge management processes: the direct path from AI to manufacturing performance is not significant while both legs of the indirect path are; AI has no direct effect on supply chain resilience either; larger firms reach higher AI maturity

## S10 Sun Y. (2022) — conditions

**kodiert:** FULL mediation: direct paths VC->CA and EV/RV->CA not significant; dynamic capabilities + innovation capabilities carry the effect (Leoni/Wang pattern: effect only via mechanism)

**Appendix:** full mediation: value co-creation has no direct effect on competitive advantage; dynamic capabilities and innovation capabilities carry the entire effect

## S17 Babina T. (2024) — conditions

**kodiert:** channel: product innovation (not process efficiency); gains concentrate among ex-ante LARGER firms -> rising industry concentration (superstar dynamics)

**Appendix:** channel: product innovation rather than process efficiency; gains concentrate among firms that were already large, which raises industry concentration (superstar dynamics)

## S21 Sullivan Y. (2024) — conditions

**kodiert:** ARMC full mediator (no direct AI->performance paths modeled); environmental hostility (negative moderator on automation->ARMC -0.23*; relational path turns n.s.); environmental dynamism moderates; only 10/18 conditional indirect effects significant

**Appendix:** adaptive response to market change is a full mediator, with no direct AI-to-performance paths modelled; environmental hostility weakens the automation path (negative moderator) and turns the relational path insignificant; environmental dynamism moderates as well; only ten of eighteen conditional indirect effects are significant

## S24 Alam S.S. (2025) — conditions

**kodiert:** SCA mediates AI adoption -> value creation; dynamic capabilities initially impede value creation (transition costs), later crucial under turbulence; technological turbulence moderates only the DC -> value creation path

**Appendix:** sustainable competitive advantage mediates between AI adoption and value creation; dynamic capabilities first impede value creation through transition costs and become crucial later under turbulence; technological turbulence moderates only the path from capabilities to value creation

## S26 Banna H. (2025) — conditions

**kodiert:** U-SHAPE with QUANTIFIED turning point: ~USD 11.3M AI venture funding (Model 5: -0.679 linear, +0.140 quadratic) - below: revenue drag, above: gains; coupling with R&D innovation strategy amplifies (standalone AI insufficient)

**Appendix:** U-shaped effect with a quantified turning point at roughly USD 11.3M of AI venture funding: below it AI drags revenue, above it AI pays; coupling AI with an R&D innovation strategy amplifies the effect, standalone AI is insufficient

## S27 Basnet A. (2025) — conditions

**kodiert:** disclosure SUBSTANCE: actionable disclosures -> valuation gains + innovation + lagged productivity; speculative/irrelevant -> nothing; silent or vague peers penalized

**Appendix:** what counts is the substance of the disclosure: actionable disclosures bring valuation gains, innovation and lagged productivity, speculative or irrelevant ones bring nothing, and silent or vague peers are penalised

## S28 Bin-Nashwan S.A. (2025) — conditions

**kodiert:** no direct AIK->performance path modeled; mediators: green human capital + green structural capital (carry effect), green RELATIONAL capital channel NULL; sustainability culture (moderator on GIC->performance)

**Appendix:** no direct path from AI-infused knowledge to performance is modelled; green human capital and green structural capital carry the effect, the green relational capital channel is empty; sustainability culture moderates the path from green capital to performance

## S37 Kumar A. (2025) — conditions

**kodiert:** ethical leadership (moderator of GenAI adoption -> performance); adoption reasons for/against (uniqueness, information completeness, convenience, deceptiveness)

**Appendix:** ethical leadership moderates the path from GenAI adoption to performance; adoption reasons for and against it (uniqueness, information completeness, convenience, deceptiveness)

## S38 Mehta P. (2025) — conditions

**kodiert:** manager personality traits (Big Five) drive adoption; competitive advantage mediates adoption -> performance; organizational culture moderates (agreeableness -> adoption)

**Appendix:** manager personality traits (Big Five) drive adoption; competitive advantage mediates between adoption and performance; organizational culture moderates the effect of agreeableness on adoption

## S40 Sandeep M.M. (2025) — conditions

**kodiert:** HR competencies + open innovation -> dynamic capabilities (mediator); financial support + IT infrastructure as enabling resources

**Appendix:** HR competencies and open innovation build dynamic capabilities, which mediate; financial support and IT infrastructure act as enabling resources

## S41 Shi Y. (2025) — conditions

**kodiert:** data assets mediate 45.6% (direct effect 0.0483*** remains); managerial capability moderates; boundary nulls: heavily polluting industries insignificant (unless credible green transition), asset-intensive firms null; SOE premium 0.035*** vs non-SOE 0.019**

**Appendix:** data assets mediate 45.6% of the effect while a significant direct effect remains; managerial capability moderates; boundary conditions: no effect in heavily polluting industries unless the firm has a credible green transition, and none in asset-intensive firms; state-owned enterprises gain about twice as much as private ones

## S44 Tingbani I. (2025) — conditions

**kodiert:** labour market conditions: labour productivity amplifies growth effect; labour cost and labour share weaken it (10% AI investment increase -> +0.04% growth on average)

**Appendix:** labour market conditions: labour productivity amplifies the growth effect, while labour cost and labour share weaken it (a ten percent rise in AI investment adds 0.04% growth on average)

## S46 Agag G. (2026) — conditions

**kodiert:** wage inequality partially mediates (AIHC compresses inequality -> value); stronger in dynamic/complex industries; sector split: value effect strongest in travel, inequality compression in hospitality

**Appendix:** wage inequality partially mediates: AI human capital compresses inequality and thereby raises firm value; the effect is stronger in dynamic and complex industries; by sector, the value effect is strongest in travel and the inequality compression in hospitality

## S48 Arshad F.M. (2026) — conditions

**kodiert:** component split: joint RPA+AI -> additional REVENUE growth (via price increases), NO additional cost reduction (joint term n.s.; individual techs do reduce costs); strategic revenue-growth intent amplifies revenue outcomes

**Appendix:** component split: RPA and AI jointly add revenue growth through price increases but no additional cost reduction (the joint term is insignificant, while each technology on its own does cut costs); a strategic revenue-growth intent amplifies the revenue outcomes

## S55 Li L. (2026) — conditions

**kodiert:** FULL mediation: direct responsible-AI -> CA path 0.091 n.s.; effect runs entirely via distributive + procedural justice; supply chain complexity weakens distributive path (-0.233***) but not procedural

**Appendix:** full mediation: the direct path from responsible AI to competitive advantage is not significant, the effect runs entirely through distributive and procedural justice; supply chain complexity weakens the distributive path but not the procedural one

## S56 Li L. (2026) — conditions

**kodiert:** three GenAI affordances mediate technological opportunism -> CA; competitive intensity amplifies ONLY the creational-affordance path

**Appendix:** three GenAI affordances mediate between technological opportunism and competitive advantage; competitive intensity amplifies only the creational-affordance path

## S57 Lin M. (2026) — conditions

**kodiert:** internal control quality (partial mediator: AI -> better governance/risk management -> TFP)

**Appendix:** internal control quality partially mediates: AI improves governance and risk management, which in turn raises total factor productivity

## S60 Liu Z. (2026) — conditions

**kodiert:** regulatory climate moderates innovation->productivity link strength (clarity + supportive enforcement jointly maximize, moderated mediation); Study 2 experiment: causal evidence for regulatory conditions

**Appendix:** the regulatory climate moderates how strongly innovation translates into productivity, with clarity and supportive enforcement jointly maximising it (moderated mediation); an experiment in study 2 provides causal evidence for the regulatory conditions

## S63 Renfei C. (2026) — conditions

**kodiert:** prescriptive capabilities FAIL (component of AI-capability bundle null); firm type boundary: Industry-4.0 manufacturers 0.58*** vs traditional significantly WEAKER (but not null)

**Appendix:** prescriptive capabilities fail as a component of the AI capability bundle; firm type is a boundary condition: the effect is strong for Industry-4.0 manufacturers and significantly weaker, though not absent, for traditional firms

## S67 Wang S. (2026) — conditions

**kodiert:** FULL mediation: strategic resilience fully accounts for AI capability -> success relationship (abstract: "fully accounts"); fsQCA equifinal configurations to high performance

**Appendix:** full mediation: strategic resilience fully accounts for the relationship between AI capability and venture success; fsQCA identifies equifinal configurations that lead to high performance
