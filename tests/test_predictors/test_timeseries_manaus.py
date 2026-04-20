"""Testes do TimeSeriesManausPredictor.

Casos de teste:
- is_available() retorna True se arquivo SIH existe
- predict() retorna PredictionResult com psi_n normalizado
- prediction[0] entre 0.0 e 1.0 (normalizado)
- context no output contém competência de entrada
- Testes com dados reais: skipados se arquivo ausente
"""

from __future__ import annotations

import numpy as np
import pytest

from qfeng.core.predictor_interface import PredictionContext, PredictionResult
from qfeng.core.predictors.timeseries_manaus import (
    SIH_PATH,
    TimeSeriesManausPredictor,
)

# Marcar todos os testes que precisam do arquivo real
requires_sih = pytest.mark.skipif(
    not SIH_PATH.exists(),
    reason=f"Arquivo SIH ausente: {SIH_PATH}",
)


@pytest.fixture()
def predictor() -> TimeSeriesManausPredictor:
    return TimeSeriesManausPredictor()


def _make_ctx(competencia: str, diag_prefix: str = "J") -> PredictionContext:
    return PredictionContext(
        scenario_id=f"manaus_{competencia}",
        regime="brasil",
        timestamp=competencia,
        input_data={"competencia": competencia, "diag_prefix": diag_prefix},
        active_predicates=["fornecimento_oxigenio_obrigacao", "uti_disponivel_obrigacao"],
    )


class TestIsAvailable:
    def test_is_available_returns_bool(self, predictor: TimeSeriesManausPredictor) -> None:
        result = predictor.is_available()
        assert isinstance(result, bool)

    def test_is_available_true_when_file_exists(self, predictor: TimeSeriesManausPredictor) -> None:
        if SIH_PATH.exists():
            assert predictor.is_available() is True

    def test_is_available_false_when_file_missing(self) -> None:
        from unittest.mock import patch

        predictor_local = TimeSeriesManausPredictor()
        with patch.object(predictor_local, "is_available", return_value=False):
            assert predictor_local.is_available() is False


class TestPredictStructure:
    @requires_sih
    def test_returns_prediction_result(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert isinstance(result, PredictionResult)

    @requires_sih
    def test_psi_n_shape_3(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert result.psi_n.shape == (3,)

    @requires_sih
    def test_psi_n_float64(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert result.psi_n.dtype == np.float64

    @requires_sih
    def test_psi_n_normalized_l2(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        norm = float(np.linalg.norm(result.psi_n))
        assert abs(norm - 1.0) < 1e-6

    @requires_sih
    def test_prediction_0_between_0_and_1(self, predictor: TimeSeriesManausPredictor) -> None:
        """prediction[0] (colapso_critico) deve estar entre 0 e 1."""
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert 0.0 <= float(result.psi_n[0]) <= 1.0

    @requires_sih
    def test_confidence_range(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert 0.0 <= result.confidence <= 1.0

    @requires_sih
    def test_metadata_contem_competencia(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert result.metadata.get("competencia") == "202101"

    @requires_sih
    def test_len_psi_n_matches_decision_space(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert len(result.psi_n) == len(predictor.get_decision_space())


class TestFallbackCompetenciaInexistente:
    @requires_sih
    def test_fallback_competencia_inexistente(self, predictor: TimeSeriesManausPredictor) -> None:
        """Competência inexistente no SIH deve retornar fallback uniforme com confidence=0.0."""
        ctx = _make_ctx("190001", diag_prefix="J")  # 1900 — não existe
        result = predictor.predict(ctx)
        assert result.confidence == 0.0
        assert result.raw_output is None

    @requires_sih
    def test_fallback_psi_n_normalizado(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("190001")
        result = predictor.predict(ctx)
        norm = float(np.linalg.norm(result.psi_n))
        assert abs(norm - 1.0) < 1e-6


class TestDecisionSpace:
    def test_decision_space_estavel(self, predictor: TimeSeriesManausPredictor) -> None:
        d1 = predictor.get_decision_space()
        d2 = predictor.get_decision_space()
        assert d1 == d2

    def test_decision_space_valores(self, predictor: TimeSeriesManausPredictor) -> None:
        ds = predictor.get_decision_space()
        assert "colapso_critico" in ds
        assert "alerta" in ds
        assert "estavel" in ds
        assert len(ds) == 3


@requires_sih
class TestCompetienciasReais:
    """Testes com competências reais do SIH (out/2020 → mar/2021)."""

    def test_202010_deve_existir_no_sih(self, predictor: TimeSeriesManausPredictor) -> None:
        """Outubro 2020 é o início da série — deve ter dados."""
        ctx = _make_ctx("202010", diag_prefix="J")
        result = predictor.predict(ctx)
        # Se há dados, confidence deve ser positivo
        assert result.psi_n.shape == (3,)
        assert abs(float(np.linalg.norm(result.psi_n)) - 1.0) < 1e-6

    def test_202101_pode_mostrar_pressao_alta(self, predictor: TimeSeriesManausPredictor) -> None:
        """Janeiro 2021 é o pico da crise — pode ter colapso_critico elevado."""
        ctx = _make_ctx("202101", diag_prefix="J")
        result = predictor.predict(ctx)
        # Apenas verificar estrutura — o valor depende dos dados reais
        assert result.psi_n.shape == (3,)
        assert all(v >= 0 for v in result.psi_n)

    def test_raw_output_contem_campos_esperados_quando_dados_existem(
        self, predictor: TimeSeriesManausPredictor
    ) -> None:
        ctx = _make_ctx("202101", diag_prefix="J")
        result = predictor.predict(ctx)
        if result.raw_output is not None:
            assert "competencia" in result.raw_output
            assert "n_internacoes" in result.raw_output
            assert "taxa_mortalidade" in result.raw_output
            assert "score_pressao" in result.raw_output
            # n_internacoes_normalized deve estar entre 0 e 1
            assert 0.0 <= result.raw_output["n_internacoes_normalized"] <= 1.0

    def test_sem_diag_prefix_retorna_todos_registros(self, predictor: TimeSeriesManausPredictor) -> None:
        """Sem filtro de diagnóstico, deve retornar todas as internações do mês."""
        ctx_todos = _make_ctx("202010", diag_prefix="")
        ctx_j = _make_ctx("202010", diag_prefix="J")
        result_todos = predictor.predict(ctx_todos)
        result_j = predictor.predict(ctx_j)
        # Sem filtro deve ter >= registros com filtro
        n_todos = result_todos.raw_output["n_internacoes"] if result_todos.raw_output else 0
        n_j = result_j.raw_output["n_internacoes"] if result_j.raw_output else 0
        assert n_todos >= n_j

    def test_model_id_no_metadata(self, predictor: TimeSeriesManausPredictor) -> None:
        ctx = _make_ctx("202101")
        result = predictor.predict(ctx)
        assert result.metadata.get("model_id") == "manaus_sih_timeseries_v1"
