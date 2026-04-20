"""Fixtures compartilhadas para testes E1."""

from pathlib import Path

import pytest


@pytest.fixture()
def corpora_dir() -> Path:
    """Raiz do diretório de corpus."""
    return Path(__file__).parent.parent.parent / "corpora"


@pytest.fixture()
def brasil_lei_8080(corpora_dir: Path) -> Path:
    """Caminho para Lei 8.080/1990."""
    return corpora_dir / "brasil" / "legislacao" / "lei_8080_1990.htm"


@pytest.fixture()
def usa_ssa_1902(corpora_dir: Path) -> Path:
    """Caminho para SSA Title XIX §1902."""
    return corpora_dir / "usa" / "statutory" / "ssa_title_xix_1902.htm"


@pytest.fixture()
def eu_ai_act(corpora_dir: Path) -> Path:
    """Caminho para EU AI Act 2024/1689."""
    return corpora_dir / "eu" / "regulation" / "eu_ai_act_2024_1689.htm"


@pytest.fixture()
def brasil_pdf(corpora_dir: Path) -> Path:
    """Caminho para PDF brasileiro."""
    return corpora_dir / "brasil" / "operacional" / "l14802-texto.pdf"
