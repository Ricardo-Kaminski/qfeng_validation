"""Human-readable labels for NormChunks and normative conflicts.

Provides compact, readable representations of chunks and conflict pairs
for use in reports and CLI output.
"""

from __future__ import annotations

from qfeng.core.schemas import NormChunk


def human_label(chunk: NormChunk, text_preview: int = 80) -> str:
    """Gera label legível para um NormChunk.

    Args:
        chunk: NormChunk a rotular.
        text_preview: Número de caracteres do texto a incluir.

    Returns:
        Label no formato ``source hierarchy — preview...``
    """
    hierarchy_str = " ".join(chunk.hierarchy)
    preview = chunk.text[:text_preview].rstrip()
    if len(chunk.text) > text_preview:
        preview += "..."
    return f"{chunk.source} {hierarchy_str} — {preview}"


def conflict_label(
    chunk_a: NormChunk,
    chunk_b: NormChunk,
    jaccard: float,
) -> str:
    """Gera label legível para um par de chunks concorrentes.

    Args:
        chunk_a: Primeiro chunk do par.
        chunk_b: Segundo chunk do par.
        jaccard: Score de Jaccard do par.

    Returns:
        Label multi-linha com ambos os chunks e o score.
    """
    return (
        f"Conflito normativo (Jaccard {jaccard:.3f}):\n"
        f"  [A] {human_label(chunk_a)}\n"
        f"  [B] {human_label(chunk_b)}"
    )
