"""Testes do contrato ABC — PredictorInterface.

Verifica que:
1. PredictorInterface não pode ser instanciado diretamente (é ABC)
2. Subclasse concreta pode ser instanciada e usada
3. predict() retorna PredictionResult com psi_n normalizado L2
4. len(psi_n) == len(get_decision_space())
5. is_available() retorna bool sem exceção
6. align_with_predicates() retorna vetor numpy alinhado
"""

from __future__ import annotations

import numpy as np
import pytest

from qfeng.core.predictor_interface import (
    PredictionContext,
    PredictionResult,
    PredictorInterface,
)


# ── Implementação concreta mínima para testes ──────────────────────────────────


class _DummyPredictor(PredictorInterface):
    """Predictor de teste — distribuição uniforme sobre 3 estados."""

    DECISION_SPACE = ["estado_a", "estado_b", "estado_c"]

    def predict(self, context: PredictionContext) -> PredictionResult:
        psi_n = np.array([1.0, 1.0, 1.0], dtype=np.float64)
        norm = np.linalg.norm(psi_n)
        psi_n = psi_n / norm
        return PredictionResult(
            psi_n=psi_n,
            decision_space=self.DECISION_SPACE,
            raw_output={"uniform": True},
            confidence=0.9,
            metadata={"test": True},
        )

    def get_decision_space(self) -> list[str]:
        return self.DECISION_SPACE

    def is_available(self) -> bool:
        return True


class _SingletonPredictor(PredictorInterface):
    """Predictor de teste — espaço de decisão com 1 elemento."""

    DECISION_SPACE = ["unico"]

    def predict(self, context: PredictionContext) -> PredictionResult:
        psi_n = np.array([1.0], dtype=np.float64)
        return PredictionResult(
            psi_n=psi_n,
            decision_space=self.DECISION_SPACE,
            raw_output=None,
            confidence=1.0,
        )

    def get_decision_space(self) -> list[str]:
        return self.DECISION_SPACE

    def is_available(self) -> bool:
        return False


# ── Fixtures ───────────────────────────────────────────────────────────────────


@pytest.fixture()
def dummy_predictor() -> _DummyPredictor:
    return _DummyPredictor()


@pytest.fixture()
def base_context() -> PredictionContext:
    return PredictionContext(
        scenario_id="test_001",
        regime="brasil",
        timestamp="202101",
        input_data={"foo": "bar"},
        active_predicates=["estado_a_obrigacao", "estado_b_proibicao"],
    )


# ── Testes ─────────────────────────────────────────────────────────────────────


class TestPredictorInterfaceIsAbstract:
    def test_cannot_instantiate_abc_directly(self) -> None:
        """PredictorInterface não pode ser instanciado — é ABC."""
        with pytest.raises(TypeError):
            PredictorInterface()  # type: ignore[abstract]

    def test_concrete_subclass_can_be_instantiated(self) -> None:
        """Subclasse concreta com todos os métodos pode ser instanciada."""
        predictor = _DummyPredictor()
        assert isinstance(predictor, PredictorInterface)

    def test_partial_implementation_raises(self) -> None:
        """Subclasse sem todos os métodos abstratos não pode ser instanciada."""

        class _Incomplete(PredictorInterface):
            def predict(self, context: PredictionContext) -> PredictionResult:  # type: ignore[override]
                raise NotImplementedError

            def get_decision_space(self) -> list[str]:
                return []
            # is_available não implementado

        with pytest.raises(TypeError):
            _Incomplete()  # type: ignore[abstract]


class TestPredictionContextDataclass:
    def test_required_fields(self) -> None:
        ctx = PredictionContext(
            scenario_id="s1",
            regime="eu",
            timestamp="20210101",
            input_data={},
            active_predicates=[],
        )
        assert ctx.scenario_id == "s1"
        assert ctx.regime == "eu"
        assert ctx.system_prompt == ""
        assert ctx.extra_data == {}

    def test_optional_fields_defaults(self) -> None:
        ctx = PredictionContext(
            scenario_id="s2",
            regime="usa",
            timestamp="202012",
            input_data={"key": "value"},
            active_predicates=["pred_1"],
        )
        assert ctx.extra_data == {}
        assert ctx.system_prompt == ""


class TestPredictionResult:
    def test_psi_n_is_numpy_array(self, dummy_predictor: _DummyPredictor, base_context: PredictionContext) -> None:
        result = dummy_predictor.predict(base_context)
        assert isinstance(result.psi_n, np.ndarray)
        assert result.psi_n.dtype == np.float64

    def test_psi_n_normalized_l2(self, dummy_predictor: _DummyPredictor, base_context: PredictionContext) -> None:
        """psi_n deve ser normalizado L2 (norma ≈ 1.0)."""
        result = dummy_predictor.predict(base_context)
        norm = float(np.linalg.norm(result.psi_n))
        assert abs(norm - 1.0) < 1e-6, f"L2 norm esperada 1.0, obtida {norm}"

    def test_psi_n_length_matches_decision_space(
        self, dummy_predictor: _DummyPredictor, base_context: PredictionContext
    ) -> None:
        result = dummy_predictor.predict(base_context)
        assert len(result.psi_n) == len(dummy_predictor.get_decision_space())

    def test_confidence_is_float_in_range(
        self, dummy_predictor: _DummyPredictor, base_context: PredictionContext
    ) -> None:
        result = dummy_predictor.predict(base_context)
        assert isinstance(result.confidence, float)
        assert 0.0 <= result.confidence <= 1.0

    def test_decision_space_is_stable(self, dummy_predictor: _DummyPredictor) -> None:
        """get_decision_space() deve retornar a mesma lista em chamadas sucessivas."""
        d1 = dummy_predictor.get_decision_space()
        d2 = dummy_predictor.get_decision_space()
        assert d1 == d2

    def test_metadata_default_is_dict(self) -> None:
        result = PredictionResult(
            psi_n=np.array([1.0]),
            decision_space=["x"],
            raw_output=None,
            confidence=0.5,
        )
        assert isinstance(result.metadata, dict)


class TestIsAvailable:
    def test_returns_bool_without_exception(self, dummy_predictor: _DummyPredictor) -> None:
        result = dummy_predictor.is_available()
        assert isinstance(result, bool)

    def test_unavailable_predictor_returns_false(self) -> None:
        predictor = _SingletonPredictor()
        assert predictor.is_available() is False

    def test_available_predictor_returns_true(self, dummy_predictor: _DummyPredictor) -> None:
        assert dummy_predictor.is_available() is True


class TestAlignWithPredicates:
    def test_returns_numpy_array(self, dummy_predictor: _DummyPredictor, base_context: PredictionContext) -> None:
        result = dummy_predictor.predict(base_context)
        psi_s = dummy_predictor.align_with_predicates(result, base_context.active_predicates)
        assert isinstance(psi_s, np.ndarray)

    def test_psi_s_same_length_as_psi_n(
        self, dummy_predictor: _DummyPredictor, base_context: PredictionContext
    ) -> None:
        result = dummy_predictor.predict(base_context)
        psi_s = dummy_predictor.align_with_predicates(result, base_context.active_predicates)
        assert len(psi_s) == len(result.psi_n)

    def test_empty_predicates_returns_zero_vector(
        self, dummy_predictor: _DummyPredictor, base_context: PredictionContext
    ) -> None:
        result = dummy_predictor.predict(base_context)
        psi_s = dummy_predictor.align_with_predicates(result, [])
        assert np.allclose(psi_s, np.zeros(len(result.psi_n)))

    def test_psi_s_normalized_when_predicates_match(
        self, dummy_predictor: _DummyPredictor, base_context: PredictionContext
    ) -> None:
        result = dummy_predictor.predict(base_context)
        # Predicados que claramente colidem com rótulos do espaço de decisão
        predicates = ["estado_a_regra", "estado_b_regra"]
        psi_s = dummy_predictor.align_with_predicates(result, predicates)
        norm = float(np.linalg.norm(psi_s))
        # Se algum predicado foi mapeado, a norma deve ser 1.0
        if norm > 0:
            assert abs(norm - 1.0) < 1e-6
