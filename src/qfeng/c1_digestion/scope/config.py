"""E0 — Scope configuration for the Q-FENG C1 pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path


@dataclass
class ScopeConfig:
    """Configuração de escopo para o pipeline C1."""

    name: str
    description: str
    regimes: list[str]
    documents: dict[str, list[str]]
    chunk_types: list[str]
    hierarchy_depth: int
    follow_cross_references: bool
    min_chunk_chars: int
    strength_filter: list[str] | None


def load_scope(path: Path) -> ScopeConfig:
    """Stub — implementar no Task 3."""
    raise NotImplementedError


def filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]:
    """Stub — implementar no Task 4."""
    raise NotImplementedError
