"""Zentrale Konstanten. Diese Werte sind bewusst gesetzt – nicht eigenmächtig ändern."""

import os
from pathlib import Path

EMBED_MODEL      = "Qwen/Qwen3-Embedding-4B"
EMBED_PRECISION  = "fp8"
EMBED_DIM        = 2560          # nativ, keine Truncation
RERANK_MODEL     = "BAAI/bge-reranker-v2-m3"
RERANK_MAX_LEN   = 1024
CHUNK_TOKENS     = 600
CHUNK_OVERLAP    = 0.15
SCAN_CHAR_THRESH = 100           # < 100 Zeichen/Seite => Scan-Verdacht
CAND_PER_METHOD  = 200           # dense und BM25 je 200
RRF_K            = 60
FINAL_K          = 12
QUERY_INSTRUCTION = (
    "Given a research question, retrieve passages from scientific "
    "papers that directly answer it."
)
ZOTERO_BASE = os.environ.get("ZOTERO_BASE_URL", "http://localhost:23119")

# Ableitungen / Umgebung (keine Retrieval-Parameter)
DB_PATH     = os.environ.get("DB_PATH", "library.db")
MODEL_CACHE = os.environ.get("MODEL_CACHE") or None

# Korpusquelle statt Zotero: die eingefrorenen Dateien der Bachelorarbeit.
# rag/library_core/config.py -> parents[2] ist der Projektordner der Arbeit.
_THESIS_ROOT   = Path(__file__).resolve().parents[2]
CORPUS_DIR     = Path(os.environ.get("CORPUS_DIR") or _THESIS_ROOT / "corpus")
LITERATURE_DIR = Path(os.environ.get("LITERATURE_DIR") or _THESIS_ROOT / "literature")
CODING_TABLE   = CORPUS_DIR / "coding_table.csv"
SCOPUS_EXPORT  = CORPUS_DIR / "corpus_2026-07-17.csv"   # eingefroren, 17.07.2026

# Druckseiten-Kalibrierung: So viele Seiten mit gedruckter Seitenzahl müssen
# denselben Offset zeigen, damit er für das Dokument gilt (siehe ingest.py).
PAGE_OFFSET_MIN_OBS = 2

# Schwelle für "plausibler Treffer" (Sigmoid über Reranker-Logit).
# Genutzt von run_eval für die abstain_rate der negative-Fragen.
ABSTAIN_SCORE = 0.5
