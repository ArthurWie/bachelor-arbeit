# Was wir hier bauen – und warum

Eine Erklärung ohne Code, zum Nachlesen und Weitergeben.

---

## Die Idee in drei Sätzen

Du hast rund 70 wissenschaftliche Papers in Zotero. Wir bauen ein Werkzeug, mit dem du diese Bibliothek befragen kannst wie einen sehr gut eingelesenen Kollegen – und das jede Antwort mit einem wörtlichen Zitat und einer Seitenzahl belegt, die du in zwei Sekunden nachprüfen kannst. Alles läuft auf deinem Rechner, kostet nichts und schickt keine Daten weg.

Das ist im Kern dasselbe, was kommerzielle Werkzeuge wie Anara anbieten. Der Unterschied: Du kontrollierst, wie es funktioniert – und kannst es auf dein Fachgebiet tunen, was ein Allrounder-Tool nie so gut kann.

---

## Warum überhaupt selbst bauen?

Ein fairer Vergleich, damit die Entscheidung informiert bleibt.

Anara Pro kostet etwa 20 Dollar im Monat und funktioniert sofort. Du bekommst einen polierten Reader, Zusammenarbeit im Team, mobile Nutzung und eine Suche, die einfach da ist. Wer wenig Zeit und keine Lust auf Technik hat, ist damit gut beraten.

Selbst bauen lohnt sich, wenn dir drei Dinge wichtig sind: **Kontrolle** darüber, wie gesucht und zitiert wird. **Unabhängigkeit** von einem Anbieter, der Preise ändert oder Modelle abschaltet. Und **Anpassbarkeit** an dein Fachgebiet.

Der Preis dafür ist nicht Geld, sondern Zeit: realistisch vier bis sieben Tage, bis du ein System hast, dem du wirklich traust.

Eine Randnotiz, die zeigt, warum Unabhängigkeit kein abstraktes Argument ist: Während der Planung stellte sich heraus, dass ein weit verbreitetes Cloud-Modell für Suchvektoren im Juli 2026 abgeschaltet wurde. Wer damit seine Bibliothek durchsuchbar gemacht hatte, stand plötzlich vor einem Datenbestand, der auf ein nicht mehr existierendes Modell verweist – und musste alles neu aufbauen. Modelle, die auf deiner Festplatte liegen, haben dieses Problem nicht.

---

## Der eine Trick, der das Ganze kostenlos macht

Hier lohnt es sich, kurz genauer hinzusehen, denn das ist die wichtigste Entscheidung im ganzen Projekt.

Du hast ein Claude-Max-Abo. Naheliegend wäre, ein Programm zu schreiben, das Claude über die Programmierschnittstelle aufruft. Das funktioniert – kostet aber extra, denn das Abo deckt die App, nicht die Schnittstelle. Jeder Aufruf aus eigenem Code wird separat abgerechnet.

Die Lösung dreht die Richtung um. Statt eines Programms, das Claude aufruft, bauen wir einen **Dienst, den Claude aufruft**. Claude Code – das vom Abo gedeckt ist – bekommt neue Werkzeuge an die Hand: „durchsuche meine Bibliothek", „lies mir dieses Paper vollständig vor". Das Denken macht Claude, das Suchen macht dein Rechner.

Ergebnis: Das Teure ist durch dein Abo abgedeckt, der Rest läuft lokal. Gesamtkosten: null.

---

## Wie es funktioniert – in fünf Schritten

### 1. Einlesen

Wir holen die Metadaten aus Zotero – Titel, Autoren, Jahr, DOI – und den Pfad zur PDF-Datei. Zotero hat eine eingebaute lokale Schnittstelle, die genau das liefert. Die Metadaten kommen bewusst immer aus Zotero und nie aus dem PDF: Sie sind dort schon sauber gepflegt, während aus PDFs extrahierte Angaben oft fehlerhaft sind.

### 2. Papers lesbar machen

Ein PDF ist für einen Computer erstaunlich unübersichtlich. Zweispaltige Layouts, Tabellen, Fußnoten, Kopfzeilen – ohne Aufbereitung entsteht Textsalat. Wir nutzen dafür ein Werkzeug namens Docling, das die Struktur eines Papers versteht: Wo beginnt ein Abschnitt, welcher Text gehört zusammen, wo steht eine Tabelle.

Wichtig ist dabei ein Detail, das man leicht übersieht: Für jeden Textabschnitt merken wir uns **die genaue Position auf der Seite**. Diese Koordinaten sind später die Grundlage dafür, dass ein Klick auf ein Zitat direkt zur richtigen Stelle im PDF springt. Wer sie beim Einlesen wegwirft, kann diese Funktion später nicht nachrüsten, ohne alles neu zu machen.

### 3. Der Schritt, den man weglassen möchte

Danach kommt etwas Unglamouröses: **Du schaust dir alle 70 Papers einmal an.** Nicht lesen – nur prüfen, ob die Aufbereitung geklappt hat. Ist die Reihenfolge bei zweispaltigem Text richtig? Sind Tabellen erhalten? Fehlt ein Abschnitt?

Das dauert zwei bis vier Stunden und ist die wertvollste Zeit, die du in dieses Projekt steckst.

Der Grund: Ein falsch gelesenes Paper produziert Unsinn, der durch das ganze System läuft und **niemals einen Fehler auslöst**. Du bekommst einfach schlechtere Antworten und weißt nicht, warum. Bei 500 Papers wäre diese Prüfung undenkbar – bei 70 ist sie machbar, und genau darin liegt ein Vorteil deiner kleinen Bibliothek.

### 4. Durchsuchbar machen

Jetzt wird der Text in überschaubare Häppchen geschnitten – Abschnitte von etwa 600 Wörtern, die nie über eine Kapitelgrenze hinweggehen. Jedes Häppchen bekommt einen kurzen Vermerk, aus welchem Paper und welchem Abschnitt es stammt. Ohne diesen Kontext wäre ein Satz wie „die Gruppe zeigte eine Reduktion um zwölf Prozent" später praktisch unauffindbar.

Dann übersetzt ein KI-Modell jedes Häppchen in eine lange Zahlenreihe, die seine Bedeutung repräsentiert. Texte mit ähnlicher Bedeutung erhalten ähnliche Zahlenreihen. Das ist der Mechanismus, der es erlaubt, nach *Sinn* zu suchen statt nach Wörtern – du findest eine Passage über „Stichprobenumfang", auch wenn du „Teilnehmerzahl" gesucht hast.

Dieser Durchlauf dauert bei 70 Papers etwa eine Stunde auf deiner Grafikkarte. Danach ist er fertig und muss nie wiederholt werden.

### 5. Suchen – und hier liegt der Qualitätsunterschied

Das ist die Stelle, an der selbstgebaute Werkzeuge meistens enttäuschen, und deshalb der wichtigste Teil.

Der naive Ansatz nimmt die Bedeutungssuche und liefert die fünf ähnlichsten Häppchen. Das klingt vernünftig, scheitert aber regelmäßig – und zwar auf die unangenehmste Art: Die Antwort klingt flüssig und plausibel, beruht aber auf den falschen Stellen. Der Fehler ist unsichtbar.

Wir machen es in drei Stufen:

**Erstens: zwei Suchen parallel.** Neben der Bedeutungssuche läuft eine klassische Stichwortsuche. Die braucht man, weil Bedeutungssuche bei exakten Begriffen schwach ist – Autorennamen, Fachtermini, Messgrößen, Aktenzeichen. Beide Verfahren haben unterschiedliche blinde Flecken, zusammen sehen sie mehr.

**Zweitens: zusammenführen.** Die beiden Trefferlisten werden fair verrechnet. Das klingt trivial, ist es aber nicht: Die beiden Suchen liefern Bewertungszahlen auf völlig unterschiedlichen Skalen, die man nicht einfach addieren kann. Stattdessen zählt nur die Platzierung – wer bei beiden Verfahren vorne liegt, gewinnt.

**Drittens: sortieren lassen.** Aus den 200 gesammelten Kandidaten wählt ein zweites, spezialisiertes Modell die besten zwölf aus. Dieses Modell arbeitet anders: Es sieht Frage und Textstelle gleichzeitig und beurteilt deshalb viel genauer, ob die Stelle wirklich passt. Es wäre zu langsam für die ganze Bibliothek – aber für 200 Kandidaten ist es perfekt.

Das Prinzip dahinter ist eine Arbeitsteilung: Die erste Stufe sorgt dafür, dass die richtige Stelle *überhaupt dabei* ist. Die dritte sorgt dafür, dass sie *ganz vorne* steht.

---

## Der Vorteil deiner kleinen Bibliothek

Hier wird es interessant, denn 70 Papers erlauben etwas, das bei 500 unmöglich wäre.

Deine gesamte Bibliothek umfasst etwa 700.000 Wörter. Das ist eine Menge, die Claude in einem Rutsch lesen kann. Deshalb kehren wir den üblichen Ansatz um:

> Die Suche wählt nicht mehr die passenden *Textschnipsel* aus, sondern die passenden *Papers* – und Claude liest sie dann vollständig.

Damit verschwindet die häufigste stille Verlustquelle überhaupt: dass der entscheidende Satz zwei Häppchen weiter stand und deshalb nie auftauchte. Für Fragen wie „wie verhält sich die Methode von X zu der von Y?" ist das ein spürbarer Unterschied, weil solche Antworten sich nie an einer Stelle finden, sondern aus dem Zusammenhang entstehen.

Große Werkzeuge können das nicht anbieten, weil ihre Nutzer Tausende Dokumente haben. Du kannst es.

Ein zweiter Vorteil: Weil ein kompletter Durchlauf nur eine Stunde dauert, kannst du verschiedene Varianten ausprobieren und vergleichen, statt die erste zu nehmen und zu hoffen.

---

## Warum Zitate der eigentliche Kern sind

Es ist verlockend zu denken, ein gutes Recherchewerkzeug sei eines, das richtige Antworten gibt. Das ist zu kurz gedacht.

Kein System dieser Art ist fehlerfrei. Die entscheidende Frage ist deshalb nicht, ob es Fehler macht, sondern **ob du sie bemerkst**.

Ein Werkzeug, das flüssige Antworten ohne prüfbare Belege liefert, ist gefährlich – nicht weil es öfter falsch liegt, sondern weil du keine Möglichkeit hast, es zu kontrollieren. Ein Werkzeug, das jede Aussage mit einem wörtlichen Zitat und einer Seitenzahl belegt, ist auch dann vertrauenswürdig, wenn es gelegentlich daneben liegt: Du siehst es sofort.

Deshalb sind drei Dinge fest eingebaut:

Jede Antwort enthält **wörtliche Zitate mit Seitenzahl**. Nicht „vergleiche Müller 2023", sondern der Satz selbst, den du im PDF suchen kannst.

Eine **automatische Zitatprüfung**: Das System kontrolliert selbst, ob ein angeblich wörtliches Zitat tatsächlich im Quelltext vorkommt. Erfundene Zitate werden markiert, nicht durchgelassen. Das sind zwanzig Zeilen Code und schließt die gefährlichste Fehlerklasse.

Die Erlaubnis, **nichts zu wissen**. Claude wird ausdrücklich angewiesen zu sagen „das steht nicht in deinen Quellen", statt eine plausible Antwort zu erfinden. Ein System, das immer etwas liefert, hat eine hohe Dunkelziffer.

---

## Die 30 Fragen, die alles entscheiden

Es gibt einen Schritt, den fast alle überspringen und der den Unterschied zwischen „scheint zu funktionieren" und „ich verlasse mich darauf" ausmacht.

Du formulierst **30 Fragen zu deinen eigenen Papers, deren Antwort du kennst**, und markierst, wo die Antwort steht. Dann messen wir, wie oft das System die richtige Stelle findet.

Die Mischung ist wichtig: enge Faktenfragen, konzeptuelle Fragen, Fragen über mehrere Papers hinweg – und vier Fragen zu Themen, die in deiner Bibliothek **gar nicht vorkommen**. Die letzten sind die verräterischsten: Sie zeigen, ob das System zugeben kann, dass es nichts findet.

Das kostet einen Abend. Der Gewinn ist doppelt: Du weißt, wo du dem Werkzeug trauen kannst. Und du merkst sofort, wenn eine spätere „Verbesserung" die Qualität verschlechtert – was häufiger vorkommt, als man denkt.

Ohne diese Messung ist jede Aussage über Qualität ein Gefühl. Mit ihr ist sie eine Zahl.

---

## Was auf dem Rechner läuft

Zwei Modelle, zusammen etwa 5 Gigabyte Grafikspeicher – deine Karte hat 8, es passt also mit Luft:

Ein **Übersetzungsmodell**, das Text in Bedeutungs-Zahlenreihen umwandelt. Wir nehmen die mittelgroße Variante aus einer Modellfamilie, die derzeit die Spitze der öffentlichen Vergleichslisten für mehrsprachige Suche belegt – Deutsch also gut abgedeckt.

Ein **Sortiermodell**, das die Kandidaten in die richtige Reihenfolge bringt. Klein, schnell, und in direkten Vergleichen genauso gut wie deutlich größere Alternativen.

Zur größeren Variante des Übersetzungsmodells greifen wir bewusst nicht: Sie bräuchte 16 Gigabyte und passt nicht. Der Qualitätsvorsprung wäre klein, und wichtiger: Er liegt gar nicht dort. Sauberes Einlesen der Papers und gutes Sortieren bringen deutlich mehr als ein größeres Suchmodell.

---

## Die Reihenfolge

| | Schritt | Dauer | Danach hast du |
|---|---|---|---|
| 1 | Einlesen und Aufbereiten | 1 Tag | Lesbare Bibliothek |
| 2 | Sichtprüfung aller 70 Papers | 2–4 Std. | Vertrauen in die Grundlage |
| 3 | Durchsuchbar machen | ½ Tag + 1 Std. Rechnen | Beide Suchindizes |
| 4 | Die dreistufige Suche | 1 Tag | **Den Qualitätssprung** |
| 5 | Die 30 Testfragen | ½ Tag | Zahlen statt Gefühl |
| 6 | Anbindung an Claude Code | ½ Tag | Ein nutzbares Werkzeug |
| 7 | Suchvarianten und Umformulierungen | ½ Tag | Bessere Trefferquote |
| 8 | Der Reader mit Highlights | 2–3 Tage | Die schöne Oberfläche |

Nach Schritt 6 – etwa drei bis vier Tage – hast du den funktional wertvollsten Teil. An dieser Stelle merken viele, dass sie den Reader gar nicht brauchen, weil Recherche direkt im Gespräch mit Claude völlig ausreicht. Entscheide das dann, nicht jetzt.

Und: **Schritt 5 kommt vor 7 und 8.** Wer erst die Oberfläche baut, optimiert blind.

---

## Was es nicht kann

Damit die Erwartung stimmt:

**Zusammenarbeit** ist nicht vorgesehen – keine geteilten Arbeitsbereiche, kein gemeinsames Kommentieren.

**Web-Recherche** ist nicht eingebaut. Die Bibliothek ist geschlossen. Claude kann separat im Netz suchen, aber es fließt nicht in dieselbe Suche ein.

**Weitergeben** kannst du es nicht ohne Umbau, weil die Konstruktion ein Claude-Code-Abo voraussetzt. Wenn daraus einmal ein Produkt werden soll, tauscht man eine Schicht aus – der Rest bleibt.

**Wartung** ist dauerhaft. Modelle veralten, Bibliotheken ändern sich. Das ist kein Projekt, das man einmal fertigstellt.

---

## Was es kostet

Nichts. Keine Abogebühr, keine Abrechnung pro Anfrage, keine Nutzungsgrenzen. Die einzige Investition ist deine Zeit und ein paar Stunden Strom für den Rechendurchlauf.

Der eigentliche Gewinn daran ist nicht das gesparte Geld – 20 Dollar im Monat ruinieren niemanden. Es ist, dass du **beliebig experimentieren kannst**. Verschiedene Aufteilungen probieren, Suchstrategien vergleichen, alles zehnmal neu durchrechnen. Genau diese Iteration entscheidet über die Qualität, und genau sie wird gebremst, wenn jeder Versuch abgerechnet wird.
