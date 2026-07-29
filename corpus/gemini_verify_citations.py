"""Blind citation check per finished section: is the prose faithful to its footnote?

    python corpus/gemini_verify_citations.py sections/background.tex
    python corpus/gemini_verify_citations.py sections/background.tex --no-llm

Arbeitsteilung (RAG_INTEGRATION_PLAN.md §3.5 — jede Prüfung bei dem, was sie
deterministisch kann):

  Zitat wörtlich vorhanden   → MCP-Werkzeug `verify_citations` (Substring, exakt)
  Seitenzahl korrekt         → dasselbe Werkzeug, Wortfolge auf der PDF-Seite
  Source-Echo (§9, 3+ Wörter)→ DIESES Skript, mechanisch, ohne LLM
  Paraphrase treu            → Gemini, weil nur das Urteilsvermögen braucht

Gemini sieht ausschließlich Satz + Fußnotenpassage. Nicht: Claudes Begründung,
nicht die übrige Arbeit, nicht die Kodiertabelle. Ergebnis: ein JSON je
Zitatstelle in corpus/gemini_citations/, plus eine Markdown-Übersicht der
Auffälligkeiten zum Adjudizieren.

Resume-safe über einen Inhalts-Hash aus (Schlüssel, Seite, Satz, Passage): wird
ein Satz umformuliert, wird die Stelle automatisch neu geprüft, statt ein
veraltetes Urteil weiterzuschleppen.

Bewusste Abweichung von CLAUDE.md: dort war „Satz + Passage + PDF-Text" skizziert.
Der PDF-Text bleibt draußen, weil die Seitenprüfung schon deterministisch erledigt
ist und die Auflösung Druckseite→PDF-Seite in `rag/` liegt; sie hier zu wiederholen
wäre eine zweite Implementierung derselben Sache. Die Verwechslung Hypothese/Befund
— der Fehler, den der PDF-Kontext fangen sollte — fragt der Prompt direkt ab, weil
Passagen wie „H8. Competitive advantage has..." sich selbst ausweisen.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "gemini_citations"
GEMINI = r"C:\Users\arthu\AppData\Roaming\npm\gemini.cmd"

# „et al." usw. beenden keinen Satz. „p.~215" ist ungefährlich, weil auf den Punkt
# kein Leerzeichen folgt.
_ABBREV = ("et al.", "e.g.", "i.e.", "cf.", "vs.", "Fig.", "Vol.", "No.", "St.")

PROMPT = """You are checking one citation in an academic literature review, blind.

You get two things: a SENTENCE from the running text, and the PASSAGE from the cited source that the sentence is based on. Judge only whether the sentence is a faithful representation of the passage.

Reply with ONLY a JSON object (no markdown fence, no commentary), exactly these keys:

- "supported": "yes" if the passage fully supports what the sentence claims; "partly" if the sentence goes beyond the passage or shifts its emphasis; "no" if the passage does not support the claim or contradicts it
- "overclaim": the specific words in the sentence that the passage does not cover, or "" if there are none
- "passage_is_hypothesis": true if the passage states a hypothesis, an aim, or a definition rather than a result, WHILE the sentence presents it as an empirical finding; false otherwise
- "note": one sentence explaining your judgement

SENTENCE:
{sentence}

PASSAGE:
{passage}
"""


# ---------------------------------------------------------------- LaTeX parsing

def match_brace(s: str, i: int) -> int:
    """Index der schließenden Klammer zu s[i] == '{'. Regex kann das nicht:
    Fußnoten enthalten selbst Klammern ({\\v S}, \\emph{...})."""
    assert s[i] == "{", s[i:i + 20]
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    raise ValueError("unbalanced brace")


def detex(s: str) -> str:
    """LaTeX-Prosa → lesbarer Satz. Nur was in diesen Abschnitten vorkommt."""
    s = re.sub(r"\\(?:emph|textit|textbf)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\(?:label|ref|autoref)\{[^{}]*\}", "", s)
    s = re.sub(r"\\(?:paren|text)cite(?:\[[^\]]*\])*\{[^{}]*\}", "", s)
    s = s.replace("~", " ").replace(r"\&", "&").replace(r"\textemdash{}", "—")
    s = re.sub(r"\{\\v ([A-Za-z])\}", r"\1", s)          # {\v S} → S
    s = s.replace("``", '"').replace("''", '"')
    s = re.sub(r"\\[a-zA-Z]+\s*", " ", s)
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", s).strip()


CITE_RE = re.compile(r"\\(?:paren|text)cite(\[[^\]]*\])?(\[[^\]]*\])?\{")


def strip_comments(tex: str) -> str:
    """LaTeX-Kommentare weg. Sonst prüft das Skript auskommentierte Zitationen —
    in sections/method.tex steht der Transparenzhinweis als Kommentarblock."""
    return re.sub(r"(?<!\\)%.*", "", tex)


def parse_sites(tex: str) -> list[dict]:
    """Zitatstellen in Dokumentreihenfolge, je mit Satz und Fußnotenpassage.

    Baut den Text ohne Fußnoten neu auf, damit der Satz vor der Zitation
    gefunden wird, ohne dass die Fußnote hineinragt.
    """
    tex = strip_comments(tex)
    plain: list[str] = []      # laufender Text ohne Fußnoten
    sites: list[dict] = []
    i = 0
    while i < len(tex):
        m = CITE_RE.match(tex, i)
        if not m:
            if tex.startswith(r"\footnote{", i):      # Fußnoten nicht mitschreiben
                i = match_brace(tex, i + len(r"\footnote")) + 1
                continue
            plain.append(tex[i])
            i += 1
            continue
        # Zitation: [prenote][postnote]{keys}
        brackets = [b for b in (m.group(1), m.group(2)) if b]
        postnote = brackets[-1][1:-1] if brackets else ""
        keys_end = match_brace(tex, m.end() - 1)
        keys = tex[m.end():keys_end]
        j = keys_end + 1
        passage = ""
        if tex.startswith(r"\footnote{", j):
            fn_end = match_brace(tex, j + len(r"\footnote"))
            passage = tex[j + len(r"\footnote") + 1:fn_end]
            j = fn_end + 1
        sites.append({
            "keys": [k.strip() for k in keys.split(",")],
            "page": detex(postnote),
            "sentence": _last_sentence("".join(plain)),
            "passage": detex(passage),
        })
        plain.append(" [CITE]")
        i = j
    return sites


def _last_sentence(text: str) -> str:
    """Letzter Satz des bisherigen Textes — der, in dem die Zitation steht."""
    text = detex(text)
    best = 0
    for m in re.finditer(r"[.!?]\s", text):
        if not any(text[:m.end()].rstrip().endswith(a) for a in _ABBREV):
            best = m.end()
    return text[best:].strip()


# ------------------------------------------------------------- Source-Echo (§9)

def strip_label(passage: str) -> str:
    """Fußnote ohne das „[Autor (Jahr), S. X]"-Label — das ist Metadatum der
    Arbeit, kein Quellentext, und erzeugte sonst Echo-Treffer wie „hossain et al"."""
    return re.sub(r"^\s*\[[^\]]*\]\s*", "", passage)


# rewrite_standards.md §9 nimmt definierte Fachbegriffe vom Echo-Test aus; nach
# WRITING_STANDARDS.md §5 MÜSSEN sie sogar wörtlich wiederholt werden. Nur die
# Konstrukte der Arbeit stehen hier — alles andere wird gemeldet, nicht bewertet.
STOP = "xsperrex"        # Sperrwort, kommt in keinem englischen Text vor
_TERMS = ("sustained competitive advantage", "competitive advantage",
          "firm performance", "artificial intelligence", "resource-based view",
          "general-purpose technology", "general purpose technology",
          "ai investment", "ai adoption")


def echo_runs(sentence: str, passage: str, n: int = 3) -> list[str]:
    """Wortfolgen ab n Wörtern, die Satz und Passage gemeinsam haben.

    Wörtliche Zitate im Satz (in Anführungszeichen) sind laut §9 ausgenommen und
    werden vorher entfernt, ebenso die Fachbegriffe aus `_TERMS`. Ob ein
    übriger Treffer ein echtes Echo oder ein unvermeidlicher Begriff ist,
    entscheidet ein Mensch — deshalb meldet das Skript, statt zu urteilen.
    """
    bare = re.sub(r'"[^"]*"', " ", sentence)
    passage = strip_label(passage)
    # Fachbegriffe werden zur Sperre: eine Wortfolge darf nicht über sie hinweg
    # laufen. Ersatzlos löschen wäre falsch — dann rücken die Nachbarwörter
    # zusammen und bilden ein Echo, das im Text gar nicht steht.
    for term in _TERMS:
        pat = re.compile(re.escape(term), re.I)
        bare, passage = pat.sub(f" {STOP} ", bare), pat.sub(f" {STOP} ", passage)

    def words(s: str) -> list[str]:
        return re.findall(r"[a-z0-9]+", s.lower())

    a, b = words(bare), words(passage)
    joined = " " + " ".join(b) + " "
    found: list[str] = []
    i = 0
    while i <= len(a) - n:
        k = n
        while (i + k <= len(a) and STOP not in a[i:i + k]
               and f" {' '.join(a[i:i + k])} " in joined):
            k += 1
        if k > n:                                    # k-1 Wörter passten
            found.append(" ".join(a[i:i + k - 1]))
            i += k - 1
        else:
            i += 1
    return found


# ------------------------------------------------------------------- Selbsttest
# Konvention wie corpus/make_bib.py: Prüfung beim Import, kein Framework.
_T = r"""Text before. Claim about rivals \parencite[p.~215]{a2021key}\footnote{[A (2021),
p.~215] ``the exact passage about rivals''}. Second claim
here \parencite[pp.~1--2]{b2025key}\footnote{[B (2025), pp.~1--2] ``another
passage''}."""
_S = parse_sites(_T)
assert len(_S) == 2, _S
assert _S[0]["keys"] == ["a2021key"] and _S[0]["page"] == "p. 215"
assert _S[0]["sentence"] == "Claim about rivals", repr(_S[0]["sentence"])
assert _S[0]["passage"].startswith("[A (2021), p. 215]")
assert _S[1]["page"] == "pp. 1--2"
# Fußnotentext darf nie im Satz der naechsten Stelle landen
assert "exact passage" not in _S[1]["sentence"], _S[1]["sentence"]
assert _S[1]["sentence"] == "Second claim here", repr(_S[1]["sentence"])
# „et al." beendet keinen Satz
assert _last_sentence("Foo bar. Hossain et al. put the same argument") == \
    "Hossain et al. put the same argument"
# Echo: 4 gemeinsame Woerter werden gemeldet, wortwoertliche Zitate nicht
assert echo_runs("the firm has close to zero marginal cost",
                 "AI has close to zero marginal reproduction costs") == \
    ["has close to zero marginal"]
assert echo_runs('it makes "new and complementary production methods" available',
                 "to enable new and complementary production methods") == []
assert echo_runs("a wholly different wording", "nothing in common at all") == []
# Auskommentierte Zitationen zaehlen nicht
assert parse_sites("% \\parencite[p.~1]{x}\\footnote{[X] ``y''}\nReal text.") == []
# Fußnoten-Label erzeugt kein Echo mehr
assert echo_runs("Hossain et al. measure it with borrowed items",
                 "[Hossain et al. (2022), p. 247] ``items were taken''") == []
# Fachbegriff allein ist kein Echo, ein echter Wortlauf daneben schon
assert echo_runs("the study measures sustained competitive advantage",
                 "we measure sustained competitive advantage") == []
assert echo_runs("firms build a sustained competitive advantage over rivals here",
                 "firms build a sustained competitive advantage over rivals") == \
    ["firms build a"]


# ------------------------------------------------------------------------ Lauf

def site_id(site: dict) -> str:
    blob = "|".join([",".join(site["keys"]), site["page"],
                     site["sentence"], site["passage"]])
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


def ask_gemini(site: dict, model: str) -> dict:
    prompt = PROMPT.format(sentence=site["sentence"], passage=site["passage"])
    for attempt in range(3):
        try:
            p = subprocess.run([GEMINI, "-m", model], input=prompt,
                               capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=300)
            m = re.search(r"\{.*\}", (p.stdout or "").strip(), re.S)
            data = json.loads(m.group(0))
            need = {"supported", "overclaim", "passage_is_hypothesis", "note"}
            if not need.issubset(data):
                raise ValueError(f"missing keys: {need - set(data)}")
            return data
        except Exception as e:
            print(f"    Versuch {attempt + 1} gescheitert: {str(e)[:110]}", flush=True)
            time.sleep(20 * (attempt + 1))
    return {}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("texfile", type=Path)
    ap.add_argument("--no-llm", action="store_true",
                    help="nur der mechanische Echo-Test, keine Gemini-Aufrufe")
    ap.add_argument("-m", "--model", default="gemini-2.5-pro")
    ap.add_argument("--limit", type=int, help="nur die ersten N Stellen (Rauchtest)")
    args = ap.parse_args()

    tex = args.texfile.read_text(encoding="utf-8")
    sites = [s for s in parse_sites(tex) if s["passage"]][:args.limit]
    print(f"{len(sites)} Zitatstellen mit Fußnote in {args.texfile.name}", flush=True)

    OUT.mkdir(exist_ok=True)
    flagged = []
    for n, site in enumerate(sites, 1):
        sid = site_id(site)
        site["echo_runs"] = echo_runs(site["sentence"], site["passage"])
        cache = OUT / f"{sid}.json"
        if cache.exists():
            site.update(json.loads(cache.read_text(encoding="utf-8")))
        elif not args.no_llm:
            print(f"  [{n}/{len(sites)}] {','.join(site['keys'])} {site['page']}",
                  flush=True)
            verdict = ask_gemini(site, args.model)
            if verdict:
                site["gemini"] = verdict
                cache.write_text(json.dumps(site, indent=1, ensure_ascii=False),
                                 encoding="utf-8")
            time.sleep(5)                      # Free-Tier-Limits
        # Ohne Gemini-Urteil zählt nur der Echo-Test — sonst wäre im --no-llm-Lauf
        # jede Stelle „auffällig", weil kein Urteil vorliegt.
        g = site.get("gemini", {})
        if site["echo_runs"] or (g and (g.get("supported") != "yes"
                                       or g.get("passage_is_hypothesis"))):
            flagged.append(site)

    report = ROOT / f"citation_check_{args.texfile.stem}.md"
    lines = [f"# Zitatprüfung {args.texfile.name}", "",
             f"{len(sites)} Stellen geprüft, {len(flagged)} auffällig. "
             f"Mechanisch: Source-Echo ab 3 Wörtern. Gemini (blind, nur Satz + "
             f"Passage): Paraphrasentreue.", ""]
    for site in flagged:
        g = site.get("gemini", {})
        lines += [f"## {','.join(site['keys'])} — {site['page']}", "",
                  f"**Satz:** {site['sentence']}", "",
                  f"**Passage:** {site['passage'][:400]}", ""]
        if site["echo_runs"]:
            lines.append("**Source-Echo (§9):** " +
                         "; ".join(f"„{r}\"" for r in site["echo_runs"]))
        if g:
            lines.append(f"**Gemini:** supported={g.get('supported')}, "
                         f"Hypothese-statt-Befund={g.get('passage_is_hypothesis')}")
            if g.get("overclaim"):
                lines.append(f"**Zu viel behauptet:** {g['overclaim']}")
            lines.append(f"**Begründung:** {g.get('note', '')}")
        lines += ["", "**Entscheidung Arthur:** ", "", "---", ""]
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n{len(flagged)} von {len(sites)} auffällig → {report.name}", flush=True)


if __name__ == "__main__":
    main()
