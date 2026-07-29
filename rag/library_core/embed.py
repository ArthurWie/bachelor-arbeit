"""Qwen3-Embedding-4B, fp8, 2560 Dimensionen – Laden und Encoden.

Pflichtregeln (§4 Schritt 3 / Harte Regeln 1–3, 11):
1. normalize_embeddings=True bei JEDEM Encode.
2. Asymmetrie: Queries MIT Instruction, Dokumente OHNE.
3. 2560 Dimensionen, keine Truncation.
4. fp8 wird nach dem Laden über die VRAM-Belegung verifiziert (~4 GB, nicht
   ~8 GB). Ist fp8 nicht erreichbar: anhalten und melden – kein Fallback auf
   int8 oder fp16.
Bei CUDA-OOM wird die Batchgröße gesenkt, niemals das Modell getauscht.
"""

from __future__ import annotations

import threading

import numpy as np

from library_core import config

_model = None
_tokenizer = None
_lock = threading.Lock()

_HALT_NO_CUDA = (
    "CUDA ist nicht verfügbar. Das Embedding ist auf fp8 auf der GPU "
    "festgelegt (RTX 4060); ein Ausweichen auf CPU/andere Präzision ist "
    "nicht zulässig. Bitte auf dem Zielrechner ausführen. Anhalten."
)

_HALT_NO_FP8 = (
    "fp8 ist mit dieser Toolchain nicht erreichbar ({reason}). Vorgabe: "
    "anhalten und melden, NICHT auf int8 oder fp16 ausweichen. Mögliche "
    "Wege: neuere transformers-Version (FineGrainedFP8Config) oder ein "
    "vorquantisiertes FP8-Repo des Modells."
)


def get_tokenizer():
    """Nur der Tokenizer – braucht keine GPU. Für Tokenzählung beim Chunking."""
    global _tokenizer
    if _tokenizer is None:
        with _lock:
            if _tokenizer is None:
                from transformers import AutoTokenizer
                _tokenizer = AutoTokenizer.from_pretrained(
                    config.EMBED_MODEL, cache_dir=config.MODEL_CACHE
                )
    return _tokenizer


def count_tokens(text: str) -> int:
    return len(get_tokenizer().encode(text, add_special_tokens=False))


def _verify_fp8_vram() -> float:
    """fp8 verifizieren: 4B-Parameter-Modell muss ~4 GB belegen, nicht ~8 GB."""
    import torch
    allocated_gb = torch.cuda.memory_allocated() / 2**30
    if allocated_gb > 6.0:
        raise RuntimeError(_HALT_NO_FP8.format(
            reason=f"VRAM-Belegung {allocated_gb:.1f} GB statt ~4 GB – das "
                   "Modell liegt offenbar in fp16/bf16 im Speicher"
        ))
    if allocated_gb < 2.5:
        raise RuntimeError(
            f"VRAM-Belegung nur {allocated_gb:.1f} GB – das Modell scheint "
            "nicht (vollständig) auf der GPU zu liegen (CPU-Offload?). "
            "Anhalten und prüfen."
        )
    return allocated_gb


def get_model():
    """Embedding-Modell laden (einmal global, bleibt dauerhaft geladen)."""
    global _model
    if _model is not None:
        return _model
    with _lock:
        if _model is not None:
            return _model
        import torch
        from sentence_transformers import SentenceTransformer

        if not torch.cuda.is_available():
            raise RuntimeError(_HALT_NO_CUDA)
        try:
            from transformers import FineGrainedFP8Config
        except ImportError as exc:
            raise RuntimeError(_HALT_NO_FP8.format(
                reason="transformers kennt FineGrainedFP8Config nicht"
            )) from exc

        model = SentenceTransformer(
            config.EMBED_MODEL,
            model_kwargs={
                "device_map": "cuda",
                "quantization_config": FineGrainedFP8Config(),
            },
            tokenizer_kwargs={"padding_side": "left"},
            truncate_dim=None,
            cache_folder=config.MODEL_CACHE,
        )

        dim = model.get_sentence_embedding_dimension()
        if dim != config.EMBED_DIM:
            raise RuntimeError(
                f"Embedding-Dimension {dim} statt {config.EMBED_DIM} – "
                "Truncation/MRL aktiv? Anhalten."
            )

        # Qwen3-Instruction-Format für Queries; Dokumente laufen ohne Prompt.
        model.prompts["query"] = f"Instruct: {config.QUERY_INSTRUCTION}\nQuery: "

        vram = _verify_fp8_vram()
        print(f"[embed] {config.EMBED_MODEL} geladen, fp8 verifiziert "
              f"({vram:.1f} GB VRAM)")
        _model = model
    return _model


def _encode_with_oom_backoff(texts: list[str], batch_size: int, **kwargs) -> np.ndarray:
    """Harte Regel 11: bei OOM batch_size senken, nicht das Modell tauschen."""
    import torch
    model = get_model()
    while True:
        try:
            return model.encode(
                texts,
                batch_size=batch_size,
                normalize_embeddings=True,   # Harte Regel 1, immer
                convert_to_numpy=True,
                **kwargs,
            )
        except torch.cuda.OutOfMemoryError:
            if batch_size <= 1:
                raise
            batch_size = max(1, batch_size // 2)
            torch.cuda.empty_cache()
            print(f"[embed] CUDA-OOM – batch_size gesenkt auf {batch_size}")


def encode_documents(texts: list[str], batch_size: int = 8) -> np.ndarray:
    """Dokumente: OHNE Instruction (Harte Regel 2)."""
    return _encode_with_oom_backoff(texts, batch_size)


def encode_query(query: str) -> np.ndarray:
    """Queries: MIT Instruction (Harte Regel 2)."""
    return _encode_with_oom_backoff([query], 1, prompt_name="query")[0]
