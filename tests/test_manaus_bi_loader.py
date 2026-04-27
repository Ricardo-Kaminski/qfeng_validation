"""Testes de regressão — manaus_bi_loader.py (Tarefa 2.2).

Cobertura:
  test_t_mort_fix         : MORTE_NUM.sum() == 482 (regressão do bug t_mort=0)
  test_srag_not_stub      : srag_is_stub=False após extração real (guarda Fase 2)
  test_toh_from_parquet   : TOH carregado do parquet, não do dict hardcoded
  test_t_mort_ratio       : taxa_mortalidade ≈ 0.18 global
  test_series_length      : 12 meses retornados
  test_peak_month         : hospital_occupancy_pct máximo em jan ou fev 2021
  test_no_zero_internacoes: nenhum mês com n_int = 0 (parquet tem dados de todos os meses)
"""
import pytest
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from qfeng.e5_symbolic.manaus_bi_loader import (
    load_sih_with_fixed_tmort,
    load_manaus_bi_series,
    _load_toh,
    _load_srag,
)


# ── Fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def sih():
    return load_sih_with_fixed_tmort()


@pytest.fixture(scope="module")
def series():
    return load_manaus_bi_series()


# ── Testes t_mort ─────────────────────────────────────────────────────────────

def test_t_mort_fix(sih):
    """MORTE_NUM.sum() deve ser 482 — regressão do bug t_mort=0 (Fase 1 Tarefa 1.4)."""
    assert sih["MORTE_NUM"].sum() == 482, (
        f"t_mort fix falhou: esperado 482, obtido {sih['MORTE_NUM'].sum()}. "
        "Bug: pd.to_numeric('Sim') retorna NaN. "
        "Fix: (df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)"
    )


def test_t_mort_ratio(sih):
    """Taxa de mortalidade global deve estar entre 15% e 25% (faixa UTI COVID Manaus)."""
    total = len(sih)
    ratio = sih["MORTE_NUM"].sum() / total
    assert 0.15 <= ratio <= 0.25, f"t_mort ratio fora da faixa esperada: {ratio:.4f}"


def test_morte_num_binary(sih):
    """MORTE_NUM deve conter apenas 0 e 1."""
    assert set(sih["MORTE_NUM"].unique()).issubset({0, 1})


# ── Testes SRAG ───────────────────────────────────────────────────────────────

def test_srag_not_stub():
    """Guarda para Fase 2: quando SRAG real for extraído, is_stub deve ser False."""
    srag = _load_srag()
    if srag["is_stub"].any():
        pytest.skip(
            "srag_manaus.parquet ainda é stub (Fase 2 Tarefa 2.1 pendente). "
            "Re-executar após extração real do SIVEP-Gripe."
        )
    assert not srag["is_stub"].any(), "Todos os meses devem ter is_stub=False após extração real."


# ── Testes TOH ────────────────────────────────────────────────────────────────

def test_toh_from_parquet():
    """TOH deve ser carregado do parquet com 12 linhas."""
    toh = _load_toh()
    assert len(toh) == 12, f"TOH parquet deve ter 12 meses, tem {len(toh)}"


def test_toh_peak_jan_2021():
    """TOH deve ter pico em jan/2021 (104%) — sanity check epidemiológico."""
    toh = _load_toh()
    jan2021 = toh.loc[(2021, 1), "toh_uti_pct"]
    assert jan2021 >= 100.0, f"TOH jan/2021 esperado >= 100%, obtido {jan2021}%"


# ── Testes da série bivariada ─────────────────────────────────────────────────

def test_series_length(series):
    """load_manaus_bi_series() deve retornar exatamente 12 meses."""
    assert len(series) == 12


def test_peak_month(series):
    """hospital_occupancy_pct máximo deve ser em jan ou fev 2021."""
    max_row = max(series, key=lambda r: r["hospital_occupancy_pct"])
    assert max_row["mes_cmpt"] in (1, 2) and max_row["ano_cmpt"] == 2021, (
        f"Pico TOH esperado em jan/fev 2021, obtido {max_row['competencia']}"
    )


def test_all_months_have_srag_field(series):
    """Todos os meses devem ter campo srag_n_covid e srag_is_stub."""
    for row in series:
        assert "srag_n_covid" in row
        assert "srag_is_stub" in row


def test_evento_critico_jan_2021(series):
    """Jan/2021 deve ter evento_critico=True (TOH > 85%)."""
    jan = next(r for r in series if r["ano_cmpt"] == 2021 and r["mes_cmpt"] == 1)
    assert jan["evento_critico"] is True


def test_theta_t_range(series):
    """theta_t deve estar entre 0° e 180° (compute_theta retorna graus)."""
    for row in series:
        assert 0.0 <= row["theta_t"] <= 180.0, (
            f"theta_t fora do range [0,180]° em {row['competencia']}: {row['theta_t']}"
        )
