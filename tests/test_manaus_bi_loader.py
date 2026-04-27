"""Testes de regressão — manaus_bi_loader.py (Fase 2 Tarefa 2.D).

Cobertura:
  test_t_mort_fix         : MORTE_NUM.sum() == 482 (regressão do bug t_mort=0)
  test_srag_real          : srag is_stub=False (dados reais SIVEP-Gripe)
  test_toh_from_parquet   : TOH carregado do parquet semanal (73 SEs)
  test_t_mort_ratio       : taxa_mortalidade ≈ 0.18 global
  test_series_length      : 73 SEs retornadas
  test_peak_se            : hospital_occupancy_pct máximo em SE 2-4/2021
  test_no_zero_internacoes: nenhuma SE com internacoes = 0 (mapeamento mensal)
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

def test_srag_real():
    """SRAG deve ser dados reais (is_stub=False) após Tarefa 2.B."""
    srag = _load_srag()
    assert not srag["is_stub"].any(), (
        "srag_semanal_manaus.parquet contém is_stub=True. "
        "Deve usar derived/srag_semanal_manaus.parquet (Tarefa 2.B, dados reais)."
    )


def test_srag_weekly_coverage():
    """SRAG deve ter 73 semanas (SE 10/2020 - SE 30/2021)."""
    srag = _load_srag()
    assert len(srag) == 73, f"SRAG deve ter 73 SEs, tem {len(srag)}"


def test_srag_has_covid():
    """SRAG deve ter n_covid > 0 em pelo menos metade das semanas."""
    srag = _load_srag()
    n_with_covid = (srag["n_covid"] > 0).sum()
    assert n_with_covid >= 36, f"Poucas SEs com n_covid>0: {n_with_covid}"


# ── Testes TOH ────────────────────────────────────────────────────────────────

def test_toh_from_parquet():
    """TOH semanal deve ter 74 SEs (Fase 2.1.5-bis: SE 10/2020–SE 30/2021)."""
    toh = _load_toh()
    assert len(toh) == 74, f"TOH parquet deve ter 74 SEs, tem {len(toh)}"


def test_toh_peak_se3_2021():
    """TOH deve ter pico em SE 2-4/2021 (>= 100%) — colapso documentado."""
    toh = _load_toh()
    # SE 2, 3, ou 4 de 2021 devem ser >= 100
    peak_ok = False
    for se in [2, 3, 4]:
        try:
            val = toh.loc[(2021, se), "toh_uti_pct"]
            if val >= 1.0:  # parquet armazena fração (0–2.12); 1.0 = 100%
                peak_ok = True
                break
        except KeyError:
            pass
    assert peak_ok, "TOH deve atingir >= 100% (frac >= 1.0) em SE 2-4/2021 (colapso documentado)"


# ── Testes da série bivariada ─────────────────────────────────────────────────

def test_series_length(series):
    """load_manaus_bi_series() deve retornar exatamente 74 SEs (SE 10/2020–SE 30/2021, incl. SE 53/2020)."""
    assert len(series) == 74, f"Esperado 74 SEs, obtido {len(series)}"


def test_peak_se(series):
    """hospital_occupancy_pct máximo deve ser em SE 2-4/2021."""
    max_row = max(series, key=lambda r: r["hospital_occupancy_pct"])
    assert (max_row["week_se"] in (2, 3, 4) and max_row["year"] == 2021), (
        f"Pico TOH esperado em SE 2-4/2021, obtido SE{max_row['week_se']}/{max_row['year']}"
    )


def test_all_se_have_srag_field(series):
    """Todas as SEs devem ter campo srag_n_covid e srag_is_stub."""
    for row in series:
        assert "srag_n_covid" in row, f"srag_n_covid ausente em {row.get('competencia')}"
        assert "srag_is_stub" in row, f"srag_is_stub ausente em {row.get('competencia')}"


def test_srag_not_stub_in_series(series):
    """Nenhuma SE deve ter srag_is_stub=True (dados reais)."""
    stubs = [r["competencia"] for r in series if r["srag_is_stub"]]
    assert not stubs, f"SEs com srag_is_stub=True: {stubs}"


def test_evento_critico_se3_2021(series):
    """SE 3/2021 deve ter evento_critico=True (TOH > 85%)."""
    se3 = next((r for r in series if r["year"] == 2021 and r["week_se"] == 3), None)
    assert se3 is not None, "SE 3/2021 nao encontrada na serie"
    assert se3["evento_critico"] is True, (
        f"SE 3/2021: evento_critico deve ser True (TOH={se3['hospital_occupancy_pct']})"
    )


def test_theta_t_range(series):
    """theta_t deve estar entre 0° e 180° (compute_theta retorna graus)."""
    for row in series:
        assert 0.0 <= row["theta_t"] <= 180.0, (
            f"theta_t fora do range [0,180] graus em {row['competencia']}: {row['theta_t']}"
        )


def test_no_zero_internacoes(series):
    """Nenhuma SE deve ter internacoes = 0 (mapeamento mensal SIH cobre janela)."""
    zeros = [r["competencia"] for r in series if r["internacoes"] == 0]
    assert not zeros, f"SEs com internacoes=0: {zeros}"
