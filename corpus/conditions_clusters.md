# Conditions-Clustering für § 4.2 (Vorschlag Claude, 13. Aug 2026)

Grundlage: `conditions`-Spalte der Kodiertabelle (63 Studien mit Conditions).
Eine Studie kann mehreren Clustern angehören (Mehrfach-Conditions). Alle 8
Ermessensfälle am 13. Aug 2026 von Arthur entschieden (Details unten, inkl.
blinder Gemini-Zweitmeinung). Die Übersicht unten ist skriptgeneriert:
`fact_sheet.py` parst die Detailtabelle, validiert die IDs gegen die Kodiertabelle
und schreibt die Zählungen ins `FACT_SHEET.md` — Übersicht und Detail können
nicht mehr auseinanderlaufen.

## Vorgeschlagene Gliederung

| # | Unterabschnitt (Arbeitstitel) | Studien | n |
|---|---|---|---|
| 4.2.1 | Complementary investments and resources (Daten, R&D, Technologie-Infrastruktur) | S01 S02 S06 S15 S18 S26 S32 S34 S40 S41 S48 | 11 |
| 4.2.2 | Organizational capabilities and human capital as the channel (überwiegend Mediatoren) | S03 S05 S07 S10 S11 S14 S16 S18 S21 S22 S23 S24 S25 S28 S29 S35 S39 S40 S43 S46 S47 S51 S56 S63 S66 S67 | 26 |
| 4.2.3 | Leadership, governance, and management | S03 S04 S19 S30 S33 S37 S38 S41 S51 S54 S55 S57 S58 | 13 |
| 4.2.4 | Firm characteristics and market position (Größe, Eigentum, Branche, Finanzlage) | S08 S17 S20 S22 S31 S33 S41 S42 S45 S46 S49 S54 S58 S59 S63 S64 | 16 |
| 4.2.5 | Environmental conditions (Wettbewerb, Regulierung, Turbulenz, Makro) | S04 S11 S19 S21 S22 S24 S39 S44 S50 S52 S54 S56 S60 S62 S64 | 15 |
| 4.2.6 | Dose, credibility, and timing (Schwellen, Nichtlinearitäten, Signalqualität, Zeitpfade) | S01 S06 S13 S22 S26 S27 S34 S35 S36 S42 S48 S52 S62 S65 | 14 |

Kontrastgruppe (im Text von 4.2 als Rahmen, kein eigener Abschnitt): die 4 Studien
ohne identifizierte Conditions = unconditional evidence (S09, S12, S53, S61 —
die vier IDs, die in der Extraktion der conditions-Spalte fehlen; 63 + 4 = 67 ✓).

## Zuordnung je Studie (Kurzbegründung nur bei Ermessensfällen)

| Studie | Cluster | Anmerkung |
|---|---|---|
| S01 | 4.2.1, 4.2.6 | Komplement-Konfiguration; Prozess-Rekonfiguration als Nutzungsweise |
| S02 | 4.2.1 | Readiness als Ressource; Geminis C2-Vorschlag abgelehnt (stützte sich auf die nicht-signifikante „professional expertise") |
| S03 | 4.2.2, 4.2.3 | Mediatoren-Kapabilitäten + Leadership-Support-Moderator |
| S04 | 4.2.3, 4.2.5 | Leadership Support + Technologie-Turbulenz |
| S05 | 4.2.2 | Dynamic-Capabilities-Mediatoren |
| S06 | 4.2.1, 4.2.6 | Komplementär-Investitionen + Intensitätsschwelle |
| S07 | 4.2.2 | Volle Mediation via Knowledge Management |
| S08 | 4.2.4 | Branche, IT-Schwäche, Kreditrating |
| S10 | 4.2.2 | Volle Mediation via Capabilities |
| S11 | 4.2.2, 4.2.5 | Team-Kapabilität + Regulierung/Kultur (Healthcare) |
| S13 | 4.2.6 | Announcement-Detailgrad = Signalqualität |
| S14 | 4.2.2 | Neue Mensch-Maschine-Fähigkeiten |
| S15 | 4.2.1 | ICT capability als Voraussetzungs-Ausstattung, konsistent mit S02; „firm fit" zu vage für eigenen Cluster-Eintrag (Gemini-C4 abgelehnt) |
| S16 | 4.2.2 | fsQCA-Konfigurationen aus Capabilities |
| S17 | 4.2.4 | Größere Firmen, Superstar-Dynamik |
| S18 | 4.2.1, 4.2.2 | Datenqualität/Investitionsbedarf + AI-Skills (Barrieren als Bedingungen) |
| S19 | 4.2.3, 4.2.5 | Governance/Ethik + EU AI Act/GDPR |
| S20 | 4.2.4 | Marktanteil |
| S21 | 4.2.2, 4.2.5 | ARMC-Mediator + Umwelt-Feindlichkeit/-Dynamik |
| S22 | 4.2.2, 4.2.4, 4.2.5, 4.2.6 | Vierfach: getestete Mechanismus-Mediatoren (4.2.2, auf Geminis Hinweis ergänzt) + Eigentum/International + Politik + Langzeit-Abschwächung |
| S23 | 4.2.2 | Serielle Mediation |
| S24 | 4.2.2, 4.2.5 | DC-Mediation + Turbulenz-Moderation |
| S25 | 4.2.2 | Kreativität/Green-Innovation-Mediatoren |
| S26 | 4.2.1, 4.2.6 | R&D-Kopplung + U-Form (USD 11,3M) |
| S27 | 4.2.6 | Disclosure-Substanz = Signalqualität |
| S28 | 4.2.2 | Green-Intellectual-Capital-Mediatoren |
| S29 | 4.2.2 | Synergistische Funktions-Kombinationen |
| S30 | 4.2.3 | Leader-Narzissmus |
| S31 | 4.2.4 | Nur Größen-Asymmetrie; Stage-Split ist Ergebnisstruktur, keine Condition (beide Coder einig) |
| S32 | 4.2.1 | R&D-Komplementarität |
| S33 | 4.2.3, 4.2.4 | IT-Executives + Größe/Wachstumsphase |
| S34 | 4.2.1, 4.2.6 | Buyer vs. In-house = Bezugsweise (4.2.6); ICT-Humankapital als Komplement (4.2.1) — Dissens mit Gemini (C2), Arthur folgt Claude wegen Konsistenz mit dem Theoriekapitel |
| S35 | 4.2.2, 4.2.6 | Marketing-Capabilities + umgekehrte U-Formen |
| S36 | 4.2.6 | First-Mover-Befund als Timing; Indikator-Split ist effect_direction=mixed, keine Condition; 4.2.4 gestrichen (beide Coder einig) |
| S37 | 4.2.3 | Ethical Leadership |
| S38 | 4.2.3 | Manager-Persönlichkeit, Kultur |
| S39 | 4.2.2, 4.2.5 | Marketing-Agilität + Turbulenz verstärkt |
| S40 | 4.2.1, 4.2.2 | Finanzierung/IT-Infrastruktur + HR→DC |
| S41 | 4.2.1, 4.2.3, 4.2.4 | Datenassets + Managerfähigkeit + SOE/Branchen-Nulls |
| S42 | 4.2.4, 4.2.6 | Kleine Firmen + Periodeneffekt |
| S43 | 4.2.2 | AI-Capabilities-Mediator + SC-Kollaboration |
| S44 | 4.2.5 | Arbeitsmarktbedingungen |
| S45 | 4.2.4 | Größere, produktivere Firmen |
| S46 | 4.2.2, 4.2.4 | AIHC/Ungleichheits-Mediation + Sektor-Split |
| S47 | 4.2.2 | Marketing-Ambidextrie |
| S48 | 4.2.1, 4.2.6 | RPA+AI-Komplement; „strategic revenue intent" als Nutzungsabsicht in 4.2.6; Revenue/Kosten-Split ist Outcome-Muster (beide Coder einig) |
| S49 | 4.2.4 | Transparenz-/Ressourcenlage = Firmenmerkmale (von 4.2.5 umgehängt); Crash-Risk-Mechanismus bleibt key_finding, „managerial optimism" ist Mechanismus, keine Condition |
| S50 | 4.2.5 | Datenschutz-Regulierung dämpft |
| S51 | 4.2.2, 4.2.3 | Digital-Sustainability-Leadership (Mediator UND Moderator) |
| S52 | 4.2.5, 4.2.6 | Zoll-Exposition (Umfeld) + umgekehrte U-Form |
| S54 | 4.2.3, 4.2.4, 4.2.5 | Managerfähigkeit + Ownership + Wettbewerbsdruck (Null-Baseline!) |
| S55 | 4.2.3 | Justice-Mediation, SC-Komplexität |
| S56 | 4.2.2, 4.2.5 | Affordance-Mediatoren + Wettbewerbsintensität |
| S57 | 4.2.3 | Internal Control |
| S58 | 4.2.3, 4.2.4 | Interne Kontrollen + Wissens-/R&D-Intensität |
| S59 | 4.2.4 | Cash, Ownership, Marktumfeld |
| S60 | 4.2.5 | Regulierungsklima (moderierte Mediation) |
| S62 | 4.2.5, 4.2.6 | Marktwahrnehmung/Periode |
| S63 | 4.2.2, 4.2.4 | Capability-Bündel + Industry-4.0-Firmentyp |
| S64 | 4.2.4, 4.2.5 | R&D-Intensität/Sustainability + politisches Umfeld |
| S65 | 4.2.6 | Substantiation Gap + Zeitpfad |
| S66 | 4.2.2 | Team/Workforce-Mediatoren |
| S67 | 4.2.2 | Resilienz-Mediation, fsQCA |

**Entscheidung Arthur (13. Aug 2026):** Alle 8 Flaggen entschieden, nach blinder
Zweitmeinung von Gemini (agy, gemini-3.1-pro-high) über dieselben 8 Fälle ohne
Claudes Vorschläge. Ergebnis: 4× beide Coder einig (S31, S36, S48, S49-Kern);
S22 um 4.2.2 ergänzt (Geminis Hinweis übernommen); S02/S15/S49-Zusätze von Gemini
abgelehnt (n.s.-Bedingung, zu vage, Mechanismus statt Condition); S34 = einziger
echter Dissens, entschieden für Claudes 4.2.1 (Konsistenz mit Theoriekapitel).
Damit ist das Clustering eingefroren; Zählungen im FACT_SHEET.md (skriptgeneriert).
