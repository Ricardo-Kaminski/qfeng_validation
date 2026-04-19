"""E0 — Scope configuration for the Q-FENG C1 pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ScopeConfig:
    """Configuração de escopo para o pipeline C1.

    Nota: `regimes` é list[str] (não list[NormativeRegime]) para evitar
    importação circular com core/schemas.py. Conversão ocorre no runner.
    """

    name: str
    description: str
    regimes: list[str]
    documents: dict[str, list[str]]
    chunk_types: list[str]
    hierarchy_depth: int
    follow_cross_references: bool
    min_chunk_chars: int
    strength_filter: list[str] | None

    def __post_init__(self) -> None:
        valid_regimes = {"brasil", "eu", "usa"}
        invalid = set(self.regimes) - valid_regimes
        if invalid:
            raise ValueError(
                f"Regimes desconhecidos no scope '{self.name}': {invalid}"
            )
        if not 1 <= self.hierarchy_depth <= 4:
            raise ValueError(
                f"hierarchy_depth deve ser 1–4, recebido: {self.hierarchy_depth}"
            )
        if self.min_chunk_chars < 0:
            raise ValueError(
                f"min_chunk_chars não pode ser negativo: {self.min_chunk_chars}"
            )


def load_scope(path: Path) -> ScopeConfig:
    """Stub — implementar no Task 3."""
    raise NotImplementedError


def filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]:
    """Stub — implementar no Task 4."""
    raise NotImplementedError
