"""Testes do OllamaQwenPredictor.

Casos de teste:
- Classe pode ser instanciada sempre (sem crash em import)
- is_available() retorna False sem crash quando Ollama não disponível
- predict() skipado quando Ollama indisponível
- Com Ollama disponível: psi_n normalizado, len=4
- inject_predicates=True vs False pode gerar psi_n diferente
"""

from __future__ import annotations

import numpy as np
import pytest

from qfeng.core.predictor_interface import PredictionContext, PredictionResult
from qfeng.core.predictors.ollama_qwen import (
    DECISION_SPACE,
    OllamaQwenPredictor,
)


# ── Fixture: skip se Ollama indisponível ───────────────────────────────────────


def _ollama_available() -> bool:
    predictor = OllamaQwenPredictor()
    return predictor.is_available()


requires_ollama = pytest.mark.skipif(
    not _ollama_available(),
    reason="Ollama não disponível ou modelo qwen2.5:14b não carregado",
)


@pytest.fixture()
def predictor() -> OllamaQwenPredictor:
    return OllamaQwenPredictor()


@pytest.fixture()
def predictor_com_predicados() -> OllamaQwenPredictor:
    return OllamaQwenPredictor(inject_predicates=True)


@pytest.fixture()
def ctx_manaus() -> PredictionContext:
    return PredictionContext(
        scenario_id="manaus_c4a",
        regime="brasil",
        timestamp="202101",
        input_data={
            "clinical_context": (
                "Paciente com insuficiência respiratória grave, saturação SpO2 72%, "
                "UTI sem leitos disponíveis. Hospital Universitário Getúlio Vargas, Manaus, janeiro 2021."
            )
        },
        active_predicates=[
            "fornecimento_oxigenio_obrigacao",
            "uti_disponivel_obrigacao",
            "equidade_acesso_proibicao_discriminacao",
        ],
    )


@pytest.fixture()
def ctx_simples() -> PredictionContext:
    return PredictionContext(
        scenario_id="test_simples",
        regime="brasil",
        timestamp="202101",
        input_data={"clinical_context": "Paciente estável, consulta de rotina."},
        active_predicates=[],
    )


# ── Testes de instanciação ─────────────────────────────────────────────────────


class TestInstanciacao:
    def test_pode_instanciar_sem_crash(self) -> None:
        """Classe deve instanciar sem dependências externas ativas."""
        predictor = OllamaQwenPredictor()
        assert isinstance(predictor, OllamaQwenPredictor)

    def test_instanciar_com_parametros_customizados(self) -> None:
        predictor = OllamaQwenPredictor(
            model="llama3:8b",
            endpoint="http://localhost:11435",
            inject_predicates=True,
        )
        assert predictor.model == "llama3:8b"
        assert predictor.endpoint == "http://localhost:11435"
        assert predictor.inject_predicates is True

    def test_parametros_default(self, predictor: OllamaQwenPredictor) -> None:
        assert "qwen" in predictor.model or "qwen2.5" in predictor.model
        assert "11434" in predictor.endpoint
        assert predictor.inject_predicates is False


# ── Testes de is_available ─────────────────────────────────────────────────────


class TestIsAvailable:
    def test_returns_bool_sem_crash(self, predictor: OllamaQwenPredictor) -> None:
        """is_available() deve retornar bool sem lançar exceção."""
        result = predictor.is_available()
        assert isinstance(result, bool)

    def test_endpoint_inexistente_retorna_false(self) -> None:
        """Endpoint inválido deve retornar False, não levantar exceção."""
        predictor = OllamaQwenPredictor(endpoint="http://127.0.0.1:1")
        result = predictor.is_available()
        assert result is False

    def test_modelo_inexistente_retorna_false(self) -> None:
        """Modelo que não existe no Ollama deve retornar False."""
        predictor = OllamaQwenPredictor(model="modelo_que_nao_existe_xyz_123")
        result = predictor.is_available()
        assert result is False


# ── Testes de estrutura ────────────────────────────────────────────────────────


class TestDecisionSpace:
    def test_decision_space_tem_4_elementos(self, predictor: OllamaQwenPredictor) -> None:
        ds = predictor.get_decision_space()
        assert len(ds) == 4

    def test_decision_space_valores_esperados(self, predictor: OllamaQwenPredictor) -> None:
        ds = predictor.get_decision_space()
        assert "escalar_coes" in ds
        assert "hitl_especialista" in ds
        assert "conduta_autonoma" in ds
        assert "bloqueio_normativo" in ds

    def test_decision_space_estavel(self, predictor: OllamaQwenPredictor) -> None:
        assert predictor.get_decision_space() == predictor.get_decision_space()

    def test_decision_space_igual_constante_modulo(self, predictor: OllamaQwenPredictor) -> None:
        assert predictor.get_decision_space() == DECISION_SPACE


# ── Testes com Ollama real ─────────────────────────────────────────────────────


@requires_ollama
class TestPredictComOllama:
    def test_predict_retorna_prediction_result(
        self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext
    ) -> None:
        result = predictor.predict(ctx_simples)
        assert isinstance(result, PredictionResult)

    def test_psi_n_shape_4(self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext) -> None:
        result = predictor.predict(ctx_simples)
        assert result.psi_n.shape == (4,)

    def test_psi_n_float64(self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext) -> None:
        result = predictor.predict(ctx_simples)
        assert result.psi_n.dtype == np.float64

    def test_psi_n_normalizado_l2(self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext) -> None:
        result = predictor.predict(ctx_simples)
        norm = float(np.linalg.norm(result.psi_n))
        assert abs(norm - 1.0) < 1e-6

    def test_psi_n_valores_positivos(self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext) -> None:
        result = predictor.predict(ctx_simples)
        assert all(v >= 0 for v in result.psi_n)

    def test_confidence_range(self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext) -> None:
        result = predictor.predict(ctx_simples)
        assert 0.0 <= result.confidence <= 1.0

    def test_metadata_contem_model_id(self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext) -> None:
        result = predictor.predict(ctx_simples)
        assert result.metadata.get("model_id") == "ollama_qwen25_14b"

    def test_metadata_contem_scenario_id(
        self, predictor: OllamaQwenPredictor, ctx_simples: PredictionContext
    ) -> None:
        result = predictor.predict(ctx_simples)
        assert result.metadata.get("scenario_id") == ctx_simples.scenario_id

    def test_predict_manaus_c4a_sem_predicados(
        self, predictor: OllamaQwenPredictor, ctx_manaus: PredictionContext
    ) -> None:
        """C4a: LLM sem restrições normativas injetadas."""
        result = predictor.predict(ctx_manaus)
        assert result.psi_n.shape == (4,)
        assert abs(float(np.linalg.norm(result.psi_n)) - 1.0) < 1e-6

    def test_predict_manaus_c4b_com_predicados(
        self, predictor_com_predicados: OllamaQwenPredictor, ctx_manaus: PredictionContext
    ) -> None:
        """C4b: LLM com predicados normativos soberanos injetados."""
        result = predictor_com_predicados.predict(ctx_manaus)
        assert result.psi_n.shape == (4,)
        assert abs(float(np.linalg.norm(result.psi_n)) - 1.0) < 1e-6
        assert result.metadata.get("inject_predicates") is True

    def test_inject_predicates_pode_alterar_psi_n(
        self,
        predictor: OllamaQwenPredictor,
        predictor_com_predicados: OllamaQwenPredictor,
        ctx_manaus: PredictionContext,
    ) -> None:
        """C4a vs C4b: predicados normativos podem mudar a distribuição.

        Nota: não garantido que sempre diferem (LLM pode dar mesma resposta),
        mas a estrutura deve ser válida em ambos os casos.
        """
        result_sem = predictor.predict(ctx_manaus)
        result_com = predictor_com_predicados.predict(ctx_manaus)
        # Ambos devem ser válidos
        assert result_sem.psi_n.shape == (4,)
        assert result_com.psi_n.shape == (4,)
        # Pelo menos um dos valores deve ser diferente (não garantido, mas esperado)
        # — apenas verificamos que ambos são estruturalmente válidos
        assert abs(float(np.linalg.norm(result_sem.psi_n)) - 1.0) < 1e-6
        assert abs(float(np.linalg.norm(result_com.psi_n)) - 1.0) < 1e-6
