"""Eval-Harness (Schritt 5). Erst messen, dann optimieren.

    python -m scripts.run_eval

Liest eval/questions.yaml, führt jede Frage durch die volle Retrieval-
Pipeline und berechnet:

    recall_at_12 = Anteil Fragen mit mindestens einem Gold-Chunk in Top-12
    mrr          = mean(1 / Rang des ersten Gold-Chunks)
    abstain_rate = Anteil der negative-Fragen ohne plausiblen Treffer
                   (kein Ergebnis mit Score >= ABSTAIN_SCORE)

Schwellen: recall_at_12 < 0.70 → Retrieval nicht belastbar. > 0.85 → gut.
abstain_rate < 0.75 → Prompting nachschärfen.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

from library_core import config, db, retrieve


def load_questions(path: Path) -> list[dict]:
    questions = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    for q in questions:
        q.setdefault("gold_chunk_ids", [])
        if q.get("kind") not in ("fact", "concept", "cross", "negative"):
            raise ValueError(f"Ungültiger kind bei Frage: {q.get('question')!r}")
    return questions


def sync_to_db(conn, questions: list[dict]) -> None:
    conn.execute("DELETE FROM eval_questions")
    conn.executemany(
        "INSERT INTO eval_questions (question, gold_chunk_ids, kind) VALUES (?,?,?)",
        [(q["question"], json.dumps(q["gold_chunk_ids"]), q["kind"])
         for q in questions],
    )
    conn.commit()


def run(questions: list[dict], conn) -> dict:
    per_question = []
    for q in questions:
        results = retrieve.search(q["question"], k=config.FINAL_K, conn=conn)
        ranked_ids = [r.chunk_id for r in results]
        gold = set(q["gold_chunk_ids"])
        hit_rank = next(
            (i for i, cid in enumerate(ranked_ids, start=1) if cid in gold), None
        )
        top_score = max((r.score for r in results), default=0.0)
        per_question.append({
            "question": q["question"],
            "kind": q["kind"],
            "gold_chunk_ids": sorted(gold),
            "ranked_chunk_ids": ranked_ids,
            "scores": [round(r.score, 4) for r in results],
            "hit_rank": hit_rank,
            "top_score": round(top_score, 4),
            "abstained": q["kind"] == "negative" and top_score < config.ABSTAIN_SCORE,
        })

    positive = [p for p in per_question if p["kind"] != "negative"]
    negative = [p for p in per_question if p["kind"] == "negative"]

    recall = (
        sum(1 for p in positive if p["hit_rank"] is not None) / len(positive)
        if positive else 0.0
    )
    mrr = (
        sum(1.0 / p["hit_rank"] for p in positive if p["hit_rank"]) / len(positive)
        if positive else 0.0
    )
    abstain = (
        sum(1 for p in negative if p["abstained"]) / len(negative)
        if negative else None
    )

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "config": {
            "embed_model": config.EMBED_MODEL,
            "rerank_model": config.RERANK_MODEL,
            "final_k": config.FINAL_K,
            "cand_per_method": config.CAND_PER_METHOD,
            "rrf_k": config.RRF_K,
            "abstain_score": config.ABSTAIN_SCORE,
        },
        "metrics": {
            "recall_at_12": round(recall, 4),
            "mrr": round(mrr, 4),
            "abstain_rate": round(abstain, 4) if abstain is not None else None,
            "n_positive": len(positive),
            "n_negative": len(negative),
        },
        "per_question": per_question,
    }


def print_table(report: dict) -> None:
    m = report["metrics"]
    print()
    print(f"{'Metrik':<16}{'Wert':>8}   Einordnung")
    print("-" * 60)
    recall = m["recall_at_12"]
    verdict = ("gut" if recall > 0.85
               else "nicht belastbar" if recall < 0.70 else "mittel")
    print(f"{'recall_at_12':<16}{recall:>8.2f}   {verdict} "
          f"({m['n_positive']} Fragen)")
    print(f"{'mrr':<16}{m['mrr']:>8.2f}")
    if m["abstain_rate"] is not None:
        note = ("ok" if m["abstain_rate"] >= 0.75
                else "Prompting nachschärfen")
        print(f"{'abstain_rate':<16}{m['abstain_rate']:>8.2f}   {note} "
              f"({m['n_negative']} negative-Fragen)")
    print("-" * 60)
    misses = [p for p in report["per_question"]
              if p["kind"] != "negative" and p["hit_rank"] is None]
    if misses:
        print("Verfehlt (kein Gold-Chunk in Top-12):")
        for p in misses:
            print(f"  - {p['question']}")
    print()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--questions", default="eval/questions.yaml")
    ap.add_argument("--db", default=None)
    args = ap.parse_args()

    conn = db.connect(args.db)
    db.init_db(conn)

    questions = load_questions(Path(args.questions))
    n_gold = sum(1 for q in questions
                 if q["kind"] != "negative" and not q["gold_chunk_ids"])
    if n_gold:
        print(f"WARNUNG: {n_gold} nicht-negative Frage(n) ohne gold_chunk_ids – "
              "die zählen als verfehlt.")
    sync_to_db(conn, questions)

    report = run(questions, conn)
    print_table(report)

    out_dir = Path("eval/results")
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = out_dir / f"{stamp}.json"
    out_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Ergebnis gespeichert: {out_path} (Läufe sind per diff vergleichbar)")


if __name__ == "__main__":
    main()
