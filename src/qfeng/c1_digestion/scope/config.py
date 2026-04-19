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
        valid_regimes = {"brasil", "eu", "usa", "brasil_trabalhista"}
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
    """Carrega perfil YAML e instancia ScopeConfig.

    Raises:
        ValueError: Regime desconhecido ou parâmetro fora do intervalo.
        TypeError: Campo obrigatório ausente no YAML.
        FileNotFoundError: Arquivo não encontrado.
    """
    import yaml  # noqa: PLC0415

    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return ScopeConfig(**data)


def filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]:
    """Retorna arquivos do corpus que satisfazem o escopo definido.

    Usa rglob para capturar subdiretórios e fnmatch para pattern matching.

    Args:
        corpus_dir: Raiz do corpus (ex: corpora/).
        scope: Configuração de escopo com regimes e patterns.

    Returns:
        Lista de Path ordenada, contendo apenas arquivos dentro do escopo.
    """
    from fnmatch import fnmatch  # noqa: PLC0415

    _extensions = {".htm", ".html", ".pdf", ".md"}
    result: list[Path] = []

    for regime in scope.regimes:
        regime_dir = corpus_dir / regime
        if not regime_dir.exists():
            continue
        patterns = scope.documents.get(regime, [])
        if not patterns:
            continue
        for path in sorted(regime_dir.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in _extensions:
                continue
            if any(fnmatch(path.name, pat) for pat in patterns):
                result.append(path)

    return result
