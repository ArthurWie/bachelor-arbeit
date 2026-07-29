"""Strukturbewusstes Chunking. Regeln (§4 Schritt 3), keine Heuristik-Freiheit:

1. Zielgröße CHUNK_TOKENS (600), Überlappung CHUNK_OVERLAP (15 %).
2. Niemals über Sektionsgrenzen hinweg – ein Chunk gehört zu genau einer Sektion.
3. Nur an Absatzgrenzen schneiden, nie mitten im Satz. (Absätze sind atomar;
   ein Absatz über Zielgröße bleibt ein eigener, übergroßer Chunk.)
4. Tabellen bleiben ein Chunk, auch wenn größer als 600 Tokens.
5. Jeder Chunk erbt section, page_start, page_end und die Vereinigung der
   bboxes seiner Blöcke (eine Vereinigung pro Seite).
6. Kontextpräfix nur in embed_text; `text` bleibt das Original und wird zitiert.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from library_core import config
from library_core.parse import Block


@dataclass
class Chunk:
    ordinal: int
    section: str
    page_start: int
    page_end: int
    bbox: list[dict]         # [{page,x0,y0,x1,y1,coord_origin}]
    text: str
    embed_text: str
    token_count: int


def _default_count_tokens(text: str) -> int:
    """Tokenzählung mit dem Tokenizer des Embedding-Modells (lazy geladen,
    braucht keine GPU)."""
    from library_core.embed import count_tokens
    return count_tokens(text)


def _union_bboxes(blocks: list[Block]) -> list[dict]:
    per_page: dict[int, dict] = {}
    for blk in blocks:
        if blk.bbox is None:
            continue
        lo_y = min(blk.bbox["t"], blk.bbox["b"])
        hi_y = max(blk.bbox["t"], blk.bbox["b"])
        u = per_page.get(blk.page)
        if u is None:
            per_page[blk.page] = {
                "page": blk.page,
                "x0": blk.bbox["l"], "y0": lo_y,
                "x1": blk.bbox["r"], "y1": hi_y,
                "coord_origin": blk.bbox["coord_origin"],
            }
        else:
            u["x0"] = min(u["x0"], blk.bbox["l"])
            u["y0"] = min(u["y0"], lo_y)
            u["x1"] = max(u["x1"], blk.bbox["r"])
            u["y1"] = max(u["y1"], hi_y)
    return [per_page[p] for p in sorted(per_page)]


def chunk_blocks(
    blocks: list[Block],
    title: str,
    year: int | None,
    count_tokens: Callable[[str], int] | None = None,
) -> list[Chunk]:
    count = count_tokens or _default_count_tokens
    target = config.CHUNK_TOKENS
    overlap_budget = int(config.CHUNK_TOKENS * config.CHUNK_OVERLAP)

    chunks: list[Chunk] = []
    buffer: list[tuple[Block, int]] = []   # (Block, token_count)

    def flush() -> None:
        if not buffer:
            return
        blks = [b for b, _ in buffer]
        text = "\n\n".join(b.text for b in blks)
        section = blks[0].section
        chunks.append(
            Chunk(
                ordinal=len(chunks),
                section=section,
                page_start=min(b.page for b in blks),
                page_end=max(b.page for b in blks),
                bbox=_union_bboxes(blks),
                text=text,
                embed_text=(
                    f"Aus '{title}' ({year}), Abschnitt {section}: {text}"
                ),
                token_count=sum(t for _, t in buffer),
            )
        )

    def overlap_tail() -> list[tuple[Block, int]]:
        """Letzte Absätze des Buffers, die zusammen ins Überlappungsbudget
        passen – nie der komplette Buffer (sonst Endlosschleife)."""
        tail: list[tuple[Block, int]] = []
        total = 0
        for pair in reversed(buffer[1:] if len(buffer) > 1 else []):
            if total + pair[1] > overlap_budget:
                break
            tail.insert(0, pair)
            total += pair[1]
        return tail

    current_section: str | None = None
    buffer_tokens = 0

    for blk in blocks:
        # Regel 2: Sektionswechsel beendet den Chunk immer.
        if current_section is not None and blk.section != current_section:
            flush()
            buffer, buffer_tokens = [], 0
        current_section = blk.section

        # Regel 4: Tabellen als eigener Chunk, egal wie groß.
        if blk.kind == "table":
            flush()
            buffer, buffer_tokens = [(blk, count(blk.text))], 0
            buffer_tokens = buffer[0][1]
            flush()
            buffer, buffer_tokens = [], 0
            continue

        tokens = count(blk.text)
        if buffer and buffer_tokens + tokens > target:
            tail = overlap_tail()
            flush()
            buffer = list(tail)
            buffer_tokens = sum(t for _, t in buffer)
        buffer.append((blk, tokens))
        buffer_tokens += tokens

    flush()
    return chunks
