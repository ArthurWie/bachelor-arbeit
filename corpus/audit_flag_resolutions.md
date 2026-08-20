# Audit-Flag-Resolutionen (20. Aug 2026, Claude)

Aufarbeitung aller 62 offenen Flags aus `author_audit.csv` (Stand 20. Aug, last-wins).
Jede Resolution: Verdikt + Beleg (Seite). Alle INCORPORATE-Werte sind in
`coding_table.csv` / `appendix_condensed.tsv` als PROPOSED angewendet — Arthur reviewt
in einem Batch und setzt die Zellen im Audit-Tool auf OK (oder widerspricht).

**⚠ Die zwei Entscheidungen, die Verteilungen ändern bzw. Case Law berühren:**
1. **S20 effect_direction: positive → mixed** (siehe unten) — ändert die Fact-Sheet-Verteilung.
2. **S21 conditions**: Fußnote 5 widerlegt „no direct paths modeled" — Richtung bleibt
   conditional, aber die Begründung musste korrigiert werden.

---

## Bereits erledigt — Flag war schon eingearbeitet, keine Änderung (9)

| Zelle | Flag | Befund |
|---|---|---|
| S26 ai_measure | „AI venture capital invested…" | Druckwert ist exakt dieser Text |
| S26 sample | „1,479 firms in 26 EU countries 2012-2023" | Druckwert identisch |
| S26 theoretical_lens | „replace: RBV + dynamic capabilities" | Kodierwert ist exakt das |
| S44 conditions | „remove (a ten percent…)" | Klammer ist bereits entfernt |
| S60 conditions | „make this shorter" | Druckwert bereits verdichtet (12 Wörter) |
| S61 ai_measure | Diktat | Kodierwert identisch |
| S61 key_finding | Diktat | Kodierwert identisch |
| S66 conditions | „(mediators/amplifiers…) nötig?" | bereits auf „(mediators)" gekürzt |
| S66 sample | „419 responses, 290 firms" | Kodierwert identisch |

→ Im Audit-Tool einfach auf OK setzen.

## IGNORE — geprüft, Zelle ist korrekt (14)

- **S02 ai_measure** („is it not acceptance of AI applications?"): Das Paper nennt das
  Konstrukt durchgehend „acceptance of AI practices" (Titel, Abstract S.255, Discussion
  S.265); „AI applications" steht nur in der Konstrukt-*Definition* (Tabelle S.260:
  "The extent of acceptance of AI applications by SMEs"). Kodierung folgt dem Label.
- **S02 conditions** („expertise not significant???"): Ja — Abstract S.255 wörtlich:
  "significantly influenced by both technology roadmapping and attitude but **not
  professional expertise**".
- **S02 effect_direction** („does that mean positive?"): Ja — γ=0.709*** (financial) und
  γ=0.681*** (non-financial) sind positive Pfadkoeffizienten (S.264).
- **S02 key_finding** („does it really say it?"): Ja, wörtlich im Abstract (s. o.).
- **S03 ai_measure** („is that the only one?"): Ja — AI-CRM-Implementation ist die einzige
  AI-Variable des Modells (H2a–c, S.208 f.); H1a–c sind Implementationsprozess-Qualitäten.
- **S05 performance_measure** („is there no performance_measure"): Leer ist richtig:
  outcome_construct = competitive_advantage (only); die Relativ-Skala „…relative to
  competitors" (S.248) IST das CA-Maß (Case Law S05).
- **S07 ai_measure** („is that the only one?"): Ja — ein AI-Konstrukt, Adoptionsgrad über
  AI-Tool-Liste (S.418).
- **S07 conditions** („is that really so?"): Volle Mediation bestätigt, S.423: "although
  the impact of AI on MFP and SCR is not significant, the results show a significant
  effect stemming from the mediation of KMPs."
- **S07 outcome_construct** („what?"): performance korrekt — DV ist MFP, kein CA-Konstrukt.
- **S07 performance_measure** („is that really so?"): S.417: AI/SCR/MFP reflektiv,
  5-Punkt-Likert, Manager-Einschätzung → „perceived … survey scale" korrekt.
- **S11 outcome_construct** („both?"): bleibt both — [1]/[3] Financial Outcome + Revenue,
  [2] kompetitiv-vergleichende Evidenz (Patientenwahl vs. Wettbewerber, Bargaining
  Power) — adjudiziertes Case Law S11.
- **S15 outcome_construct** („both kategorial?"): Ja, Spalte ist kategorial
  (performance | competitive_advantage | both). FP-Konstrukt (5 Items) + SC-Konstrukt
  (5 Items, eigene Skala, hypothesiert, validiert α=.938) → both nach Case-Law-Regel 1.
  Inhaltliche Schwäche der SC-Skala → ca_measure (INCORPORATE unten).
- **S17 outcome_construct** („nur growth/scale?"): performance bleibt — Sales-/Employment-/
  Marktwert-Wachstum zählt als Performance (Benchmark-Präzedenz; Produktivitäts-Nulls
  stehen in conditions/key_finding).
- **S22 outcome_construct** („nur TFP → productivity?"): performance bleibt — Produktivität
  ist im Schema eine Performance-Größe (Query-Vokabular „firm productivity").
- **S24 effect_direction** („TR→VC −0.275!"): positive bleibt — die Richtung kodiert den
  **AI**-Pfad: ARA→VC 0.110 (p=.034) direkt + 0.063 (p=.002) indirekt. TR (technology
  readiness) ist ein anderer Antezedent, nicht das AI-Investment.

## INCORPORATE — Druckwert-Kürzungen nach Arthurs Diktat (8)

| Zelle | neuer Druckwert |
|---|---|
| S02 sample | 392 B2B SMEs |
| S03 sample | 349 managers |
| S04 sample | 312 manager responses |
| S04 conditions | technology turbulence weakens the paths to relationship satisfaction; leadership support strengthens the satisfaction-to-performance path |
| S05 sample | 257 manager responses |
| S06 sample | 160 high-tech firms |
| S06 conditions | adoption-intensity threshold (low-level adoption shows no effect); complementary cloud and database investments amplify |
| S07 sample | 120 senior executives |

(S06: „cloud and database" gegen Volltext geprüft — Paper benennt genau diese zwei als
komplementäre Technologien, S.7 des PDF: "two potentially complementary technology
investments, namely, in database and cloud computing, and R&D strategy". Arthurs Kürzung
streicht nur die R&D-Klausel aus dem Druck; Kodierwert behält sie.)
(S03 industry zusätzlich: „(B2B)" gestrichen → „manufacturing + service", Arthurs Diktat.)

## INCORPORATE — sachliche Korrekturen (19)

- **S12 performance_measure**: „labor-based" war falsch. PDF S.8 (gedruckt S.195):
  "Output is measured by annual sales (lnSALES) and, alternatively, by value added."
  → `firm productivity (sales- and value-added-based, production function)`.
- **S13 conditions**: H2 bestätigt (detailed > vague), aber Timing-Nuance ergänzt: vague
  reagiert nur am Tag 0 (0.426 %), detailed verzögert und stärker ((-2,+2): 0.839 %,
  Differenz signifikant). „dampens" abgeschwächt → Papier sagt "modest negative
  correlation". IT-Firmen: H4a bestätigt, Non-IT durchweg n.s. (S.21 f.).
- **S13 key_finding**: Timing-Nuance ergänzt, Non-IT-n.s. ergänzt.
- **S13 performance_measure**: „on announcement day" gestrichen — CARs über fünf
  Fenster (0,0) bis (−5,+5) → `firm market value (CARs around the announcement)`.
- **S15 ai_measure**: Paper-Label ist „AIPRM **capabilities**" (Tabelle 2, S.518), Items
  = wahrgenommener Nutzen + Ressourcen-Commitment, nicht „implementation"
  → `survey construct (AIPRM capabilities: AI-based partner relationship management)`.
- **S15 performance_measure**: FP-Items sind durchweg Erwartungssätze ("We anticipate…,
  We believe…", S.519) → `perceived firm performance (survey scale, expectation-worded
  items)`.
- **S15 ca_measure**: SC1–SC5 (S.519): nur SC2 referenziert Wettbewerb; SC1 =
  AIPRM-Strategie-Einbettung, SC3–SC5 = Umwelt/CSR → Schwäche im Maß dokumentiert:
  `perceived sustainable competitiveness (survey scale; only one of five items
  competitor-referencing, rest mixes AIPRM embedding and environmental commitment)`.
- **S17 ai_measure**: Wert ok; Beleg nachgepinnt — PDF S.2: "changes in firm-level
  AI-skilled human capital, **measured by the share of AI workers**".
- **S17 conditions**: Kausalpfeil abgeschwächt — Paper sagt "is **associated with** higher
  industry concentration" → `…gains concentrate among ex-ante larger firms; associated
  with rising industry concentration (superstar dynamics)`.
- **S17 key_finding**: Wert ok („value" = "market valuations" im Abstract); Abstract-Zeile
  als Beleg nachgepinnt.
- **S18 conditions**: Vollzähligkeit ergänzt: Tabelle 6 nennt 9 Barrieren in 4 Kategorien
  → `…(9 barriers total in Table 6: financial, organisational, strategic, technological)`.
- **S18 key_finding**: „across core supply-chain processes" überzeichnet — Tabelle 4
  ausgezählt: Plan 2, **Make 13**, Deliver 2, Source 0, Return 0 von 17 Anwendungen
  → `…evidence concentrated in make/production processes (13 of 17 applications)…`.
- **S18 performance_measure**: „qualitative" war falsch — S.3349 quantifiziert teils
  (30 % Bestandsreduktion, 4 % Maschinenverfügbarkeit/OEE, −30 min Reparaturzeit)
  → `case-reported competitiveness outcomes: costs, lead times, service level, quality,
  safety, sustainability (partly quantified: 30 % stock reduction, 4 % OEE gain)`.
- **S19 ca_measure**: präzisiert — die Delphi-Ratings vergleichen AI-Implementierungs-
  erfolg/Wettbewerbsposition der vier Firmen (Fig. 7, S.13); „bid competitiveness" ist
  der Mechanismus, nicht das Maß → `expert-rated comparative competitiveness of the four
  companies (Delphi, Likert+IQR), tendering context`. CA-Einstufung (Case Law S19) bleibt.
- **S19 quality_notes ergänzt**: Sec. 3 (S.8) behauptet t-Tests/ANOVA auf Zykluszeiten/
  Fehlerraten, berichtet aber nirgends Statistiken → als Evidenzschwäche notiert.
- **S20 conditions**: Marktanteil ist Adoptions-Determinante (Selektion), kein getesteter
  Nutzen-Moderator — S.2: "hospitals with higher market share have greater incentives to
  **adopt** AI" → `market share predicts adoption (self-selection), no test of
  differential benefit; endogeneity control essential — naive OLS misleading`.
- **S20 performance_measure**: ROA fehlte — Paper nutzt 5 Maße (S.6) → `outpatient
  revenue, inpatient revenue, ROA, productivity, occupancy (ROA n.s. in every
  specification)`.
- **⚠ S20 effect_direction: positive → mixed.** ROA ist in JEDER Spezifikation null
  (IV: "positive … except ROA", 2SLS: "except for ROA", DiD: "except for the D_ROA
  column", Trends: "The only exception is ROA"). Das ist ein Indikator-Split wie S36
  (financial+market ✓, productivity n.s. → mixed) und S31 (profit ✗ → mixed), nicht
  ein Subgruppen-Null wie S41. Case-Law-Regel 2 → mixed. **Ändert Verteilung!**
- **⚠ S21 conditions**: Fußnote 5 (S.11 des PDF) berichtet einen supplementären
  Direkteffekt-Check: NUR AI-enabled **analytics** hat signifikante Direkteffekte auf
  alle drei Outcomes (0.44/0.29/0.28, bleiben mit ARMC im Modell bei 0.27/0.27/0.26,
  p<.01) — „no direct AI→performance paths modeled" war so nicht haltbar. Automation
  & relational: direkt n.s.; Hostility moderiert automation→ARMC negativ (H7a),
  relational→ARMC wird n.s. (H6), analytics→ARMC **positiv** (0.21***). →
  `ARMC central mediator; supplementary check (fn. 5): only AI-enabled analytics has
  direct effects on all three outcomes (surviving ARMC inclusion — partial mediation),
  automation and relational only via ARMC; environmental hostility moderates automation
  (−) and analytics (+) paths, relational path n.s. in final model; environmental
  dynamism moderates; 10/18 conditional indirect effects significant`.
  **Richtung bleibt conditional** (2 von 3 Capabilities nur via Mechanismus, moderierte
  Mediation, 10/18) — aber die adjudizierte Begründung ist damit korrigiert.
- **S22 conditions**: Papier selbst nennt SDL + grüne Innovation nur "**potential**
  channel effects" (S.13); SDL-Mediation "weak" (S.10) → Qualifier ergänzt.
- **S23 conditions**: Mediatoren sind pfadspezifisch (Tabelle 3, S.14): BPA nur via
  Entscheidungsqualität (H4b abgelehnt), OL via beide, BPIR nur via Prozessperformance
  → `…path-specific partial mediators: process automation (via decision-making only),
  organizational learning (both paths), process innovation (via process performance
  only)`. Volle Mediation des Direktpfads (S.15) bleibt.
- **S24 conditions**: Abstract-Rhetorik „ultimately proving crucial in navigating
  turbulence" ist durch die eigenen Zahlen widerlegt: DC→VC = **−0.385***, TT×DC =
  **−0.140*** (Turbulenz macht es schlimmer, nicht besser; H9–H11 n.s.) →
  `SCA mediates AI→value creation (0.063**) and DC→value creation (0.131**); DC direct
  effect on value creation NEGATIVE (−0.385***, transition costs); technological
  turbulence moderates only the DC path, weakening it further (−0.140*)`.
- **S24 key_finding**: „mainly through SCA" falsch (direkt 0.110 > indirekt 0.063) und
  „only once transition costs are absorbed" ist eine Temporalaussage ohne Längsschnitt →
  `AI adoption creates value in hospitality directly and via sustainable competitive
  advantage; dynamic capabilities show a negative direct effect on value creation
  (transition costs), aggravated under technological turbulence`.
- **S25 key_finding**: „entry condition" war Überinterpretation; Risk-Taking fehlte —
  Abstract: "allocating resources to AI infrastructure, proactive business strategies,
  **and entrepreneurial risk-taking**" → `AI capabilities raise sustainable SME
  performance through creativity and green innovation; AI infrastructure, proactive
  strategy and entrepreneurial risk-taking are the key resource inputs`.
- **S44 ai_measure (Druckwert)**: verständlicher formuliert → `AI hiring intensity:
  share of AI skills in the firm's workforce, from job postings and employee-profile
  (resume) data (Fedyk & Hodson approach)`.
- **S10 conditions**: Wert ok, Beleg fehlte — nachgepinnt, S.481: "the significance
  levels of the impact of the relationship value on the competitive advantage and
  innovation intelligibility are greater than 0.1, Hypotheses 5a, 5b, 6a, and 6b are
  not supported."
- **S10 key_finding**: „AI ecosystems" → Paper-Begriff „AI innovation ecosystem"
  (Titel!); „entirely" durch „full mediation"-Formulierung ersetzt →
  `Value co-creation in the AI innovation ecosystem has NO significant direct effect
  on competitive advantage — the effect runs through dynamic and innovation
  capabilities (full mediation)`.
- **S11 ai_measure**: Wert ok, Methoden-Beleg nachgepinnt, S.53: "To answer the research
  question in a qualitative approach we used the case study methodology (Yin, 1994)
  investigating the Clemenceau Medical Center in Dubai (CMC) case."

---
Offene Frage an Arthur (Batch-Review): S20-Richtung (positive→mixed) und die
korrigierte S21-Begründung absegnen; S24 outcome_construct „both" wurde bewusst
BEHALTEN (SCA-Konstrukt formal valide + AI→SCA-Pfad signifikant), obwohl SCA als
Mediator modelliert ist — Gegenlesart (nur performance) im Brief oben dokumentiert.
