#!/usr/bin/env python3
"""Agent 2 – Project Context Matcher.

Reads vocabulary/master_vocabulary.csv, samples the project lightly
(CLAUDE.md header + LaTeX section titles only), infers topic, and scores
each word for relevance to that topic.

Writes:
  vocabulary/project_vocabulary.csv   — word, cefr_level, relevance_to_topic
  vocabulary/vocabulary_report.md     — summary statistics
"""

import csv
import logging
import re
import sys
from pathlib import Path

MASTER_CSV  = Path("vocabulary/master_vocabulary.csv")
OUTPUT_CSV  = Path("vocabulary/project_vocabulary.csv")
REPORT_MD   = Path("vocabulary/vocabulary_report.md")
LOG_DIR     = Path("vocabulary/logs")

log = logging.getLogger(__name__)

HIGH_WORDS = {
    "prompt", "language", "model", "generate", "output", "input",
    "algorithm", "artificial", "intelligence", "neural", "machine",
    "learning", "system", "process", "method", "technique", "strategy",
    "instruction", "response", "query", "text", "word", "sentence",
    "task", "train", "performance", "result", "quality", "accurate",
    "knowledge", "manage", "create", "share", "transfer", "capture",
    "explicit", "tacit", "information", "data", "document", "base",
    "store", "retrieve", "apply", "learn", "understand", "insight",
    "experience", "skill", "expert", "practice",
    "organization", "organisation", "enterprise", "company", "firm",
    "industry", "business", "team", "employee", "manager", "leader",
    "decision", "innovation", "digital", "transform",
    "technology", "tool", "platform", "implement", "deploy", "adopt",
    "small", "medium", "large", "sector", "context",
    "research", "study", "review", "literature", "analysis", "find",
    "evidence", "framework", "theory", "concept", "define",
    "identify", "examine", "investigate", "propose", "suggest", "argue",
    "conclude", "discuss", "compare", "evaluate", "assess", "measure",
    "support", "demonstrate", "indicate", "show", "reveal", "highlight",
    "paper", "journal", "article", "author", "source", "reference",
    "approach", "perspective", "view", "question", "answer", "address",
    "challenge", "gap", "contribution", "implication", "limitation",
    # Additional PE + KM domain terms
    "engineering", "tacit", "generative", "elicit", "codify",
    "retrieval", "inference", "synthesis", "prompt", "prompting",
    "finding", "findings", "output", "workflow", "automate",
    "interaction", "conversational", "semantic", "ontology",
    "capability", "performance", "accuracy", "benchmark",
    "integration", "collaboration", "communication", "coordinate",
    "generate", "augment", "extract", "structure", "classify",
    "summarize", "summarise", "annotate", "validate", "refine",
    # KM / enterprise / academic domain
    "adoption", "application", "barrier", "cognitive", "competence",
    "deployment", "efficiency", "expertise", "factor", "impact",
    "implementation", "interface", "management", "network", "objective",
    "operational", "organizational", "organisational", "potential",
    "productivity", "scope", "software", "strategic", "transformation",
    "transition", "content", "driver", "outcome", "mechanism",
    "dimension", "empirical", "systematic", "theoretical", "variable",
    "hypothesis", "construct", "discipline", "domain",
    # Additional confirmed-in-master domain terms
    "acknowledge", "collaborate", "communicate", "competitive",
    "comprehensive", "coordinate", "effectively", "effectiveness",
    "efficiently", "facilitate", "innovative", "integrate", "integrated",
    "interact", "interactive", "methodology", "organize", "organized",
    "perform", "productive", "researcher", "scholar", "scholarship",
    "skilled", "institutional", "publication", "mixed",
    # Academic process / research terms
    "acquisition", "administration", "alignment", "alternative", "ambiguous",
    "applicable", "assessment", "assumption", "authority", "availability",
    "capacity", "classification", "complexity", "configuration",
    "consistency", "coordination", "documentation", "evaluation",
    "examination", "exploration", "generation", "identification",
    "improvement", "indication", "interpretation", "investigation",
    "justification", "observation", "orientation", "participation",
    "perception", "presentation", "recognition", "recommendation",
    "representation", "requirement", "specification", "combination",
    # Quality / validity / academic property terms
    "reliability", "validity", "flexibility", "accessibility",
    "transparency", "accountability", "functionality", "probability",
    "possibility", "opportunity", "uncertainty", "diversity",
    "clarity", "sensitivity",
}

MEDIUM_WORDS = {
    "develop", "improve", "increase", "reduce", "achieve", "provide",
    "require", "enable", "allow", "include", "involve",
    "design", "build", "use", "test", "run", "check",
    "significant", "important", "critical", "key", "main", "primary",
    "major", "central", "fundamental", "essential", "relevant",
    "general", "specific", "common", "typical", "standard", "formal",
    "basic", "advanced", "current", "recent", "new", "modern", "future",
    "effective", "efficient", "successful", "useful", "practical",
    "various", "multiple", "several", "different", "similar", "related",
    "both", "each", "first", "second", "third", "final", "overall",
    "however", "therefore", "thus", "hence", "although", "while",
    "because", "since", "when", "where", "how", "what", "which",
    "also", "well", "still", "yet", "even", "only", "most", "many",
    "more", "less", "much", "few", "number", "level", "degree",
    "type", "form", "way", "role", "part", "aspect", "element",
    "example", "case", "issue", "problem", "solution", "need", "goal",
    "value", "benefit", "advantage", "feature", "function", "effect",
    "change", "grow", "lead", "become", "remain", "continue",
    "report", "note", "state", "explain", "describe", "present", "introduce",
    "consider", "focus", "aim", "seek", "try", "help", "work", "make",
    "take", "give", "come", "see", "know", "think", "believe",
    # Academic connectives and hedges (confirmed in master)
    "moreover", "furthermore", "nevertheless", "accordingly", "consequently",
    "subsequently", "simultaneously", "specifically", "particularly", "notably",
    "predominantly", "primarily", "essentially", "fundamentally", "significantly",
    "substantially", "considerably", "respectively", "potentially",
    "moreover", "nonetheless", "whereas", "whereby", "thereby",
    "acknowledge", "capable", "challenging", "competitive",
    "institutional", "publication", "scholar", "scholarship",
    "accordingly", "consequently", "furthermore", "moreover",
    "notably", "particularly", "predominantly", "primarily",
    "respectively", "simultaneously", "specifically", "subsequently",
    "substantially", "considerably", "essentially", "fundamentally",
    "innovative", "integrated", "interactive", "organized",
    "productive", "effectively", "efficiently", "comprehensively",
}


def _sample_project() -> str:
    """Return a small text sample: CLAUDE.md first 60 lines + section titles."""
    parts: list[str] = []

    claude_md = Path("CLAUDE.md")
    if claude_md.exists():
        lines = claude_md.read_text(encoding="utf-8").splitlines()[:60]
        parts.append("\n".join(lines))
        log.info("Sampled CLAUDE.md (%d lines)", len(lines))
    else:
        log.warning("CLAUDE.md not found")

    sections_dir = Path("sections")
    if not sections_dir.exists():
        log.warning("sections/ directory not found — no LaTeX headings sampled")
    else:
        for tex in sections_dir.glob("*.tex"):
            text = tex.read_text(encoding="utf-8")
            for m in re.finditer(r"\\(?:section|subsection|subsubsection)\{([^}]+)\}", text):
                parts.append(m.group(1))
            log.info("Sampled headings from %s", tex.name)

    return " ".join(parts)


def _infer_topic(sample: str) -> str:
    """Return a short human-readable topic description."""
    topic_keywords = {
        "prompt engineering": ["prompt", "prompting", "prompt engineering", "llm", "chatgpt"],
        "knowledge management": ["knowledge management", "km", "seci", "tacit", "explicit knowledge"],
        "AI / LLMs": ["large language model", "generative ai", "genai", "artificial intelligence"],
        "SMEs": ["sme", "small and medium", "small firm", "enterprise"],
        "academic research": ["literature review", "research question", "seminar", "academic"],
    }
    low = sample.lower()
    found = [label for label, kws in topic_keywords.items() if any(kw in low for kw in kws)]
    return ", ".join(found) if found else "general academic / professional"


def _score(word: str) -> str:
    if word in HIGH_WORDS:
        return "high"
    if word in MEDIUM_WORDS:
        return "medium"
    return "low"


def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_DIR / "agent2.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    log.info("=== Agent 2 starting ===")

    if not MASTER_CSV.exists():
        log.error("master_vocabulary.csv not found — run Agent 1 first")
        print("ERROR: vocabulary/master_vocabulary.csv missing. Run Agent 1 first.")
        sys.exit(1)

    with MASTER_CSV.open(encoding="utf-8") as fh:
        master = list(csv.DictReader(fh))
    log.info("Loaded %d words from master_vocabulary.csv", len(master))

    sample = _sample_project()
    topic  = _infer_topic(sample)
    log.info("Inferred topic: %s", topic)

    counts = {"high": 0, "medium": 0, "low": 0}
    level_dist: dict[str, int] = {}

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["word", "cefr_level", "relevance_to_topic"])
        for row in master:
            word    = row["word"]
            level   = row["cefr_level"]
            rel     = _score(word)
            writer.writerow([word, level, rel])
            counts[rel] += 1
            level_dist[level] = level_dist.get(level, 0) + 1

    total = sum(counts.values())
    log.info("project_vocabulary.csv written: %d words (high=%d medium=%d low=%d)",
             total, counts["high"], counts["medium"], counts["low"])

    dist_lines = "\n".join(
        f"- **{lvl}:** {level_dist.get(lvl, 0)} words"
        for lvl in ("A1", "A2", "B1", "B2", "C1")
    )
    report = f"""# Vocabulary Pipeline Report

**Inferred project topic:** {topic}

## Word Count
- Total words: {total}
- High relevance: {counts['high']} ({counts['high']*100//total if total else 0}%)
- Medium relevance: {counts['medium']} ({counts['medium']*100//total if total else 0}%)
- Low relevance: {counts['low']} ({counts['low']*100//total if total else 0}%)

## CEFR Level Distribution
{dist_lines}

## Output
Final file: `vocabulary/project_vocabulary.csv`
Columns: word, cefr_level, relevance_to_topic (high/medium/low)

Use the `relevance_to_topic` column to filter: high+medium gives everyday
vocabulary appropriate for writing about {topic}.
"""
    REPORT_MD.write_text(report, encoding="utf-8")
    log.info("vocabulary_report.md written")
    print(f"Agent 2 complete — {total} words scored, report at {REPORT_MD}")


if __name__ == "__main__":
    main()
