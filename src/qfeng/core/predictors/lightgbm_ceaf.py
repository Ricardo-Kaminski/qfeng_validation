"""LightGBM CEAF Predictor — Medicamentos do Componente Especializado.

Predictor baseado no modelo LightGBM do IADAF para medicamentos CEAF.

|ψ_N⟩ = vetor de probabilidade de estado de estoque por UF × produto:
    [prob_ruptura_iminente, prob_estoque_adequado, prob_excesso_estoque]

Cenários Q-FENG:
    - C1 (falha de execução): ruptura prevista, predicado fornecimento_continuo existe
      mas cadeia algédônica não escala → θ > 120°, Circuit Breaker
    - C3 (falha constitucional): predicado equidade_regional_uf ausente →
      θ estruturalmente incalculável
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import numpy as np

from qfeng.core.predictor_interface import (
    PredictionContext,
    PredictionResult,
    PredictorInterface,
)

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parents[4] / "data" / "predictors" / "ceaf_medicamentos"
MODEL_PATH = DATA_DIR / "model_pharma_sota_v1.pkl"
FEATURES_PATH = DATA_DIR / "features_list.pkl"
FORECAST_PATH = DATA_DIR / "forecast_t12_final.parquet"


class LightGBMCEAFPredictor(PredictorInterface):
    """Predictor LightGBM para medicamentos CEAF.

    Espaço de decisão:
        - ``ruptura_iminente``: gap positivo entre demanda prevista e estoque → Circuit Breaker
        - ``estoque_adequado``: equilíbrio — zona STAC
        - ``excesso_estoque``: ineficiência alocativa
    """

    DECISION_SPACE: list[str] = [
        "ruptura_iminente",
        "estoque_adequado",
        "excesso_estoque",
    ]

    # Threshold de ruptura iminente (configurável via ScopeConfig futuro)
    RUPTURA_THRESHOLD: float = 0.30

    def __init__(self) -> None:
        self._model: Any = None
        self._features: list[str] | None = None
        self._forecast: Any = None  # pd.DataFrame — importado lazy

    def _load(self) -> None:
        """Lazy loading — carrega modelo apenas quando necessário."""
        if self._model is not None:
            return

        import pickle

        import pandas as pd

        logger.info("Carregando modelo LightGBM CEAF de %s", MODEL_PATH)
        with open(MODEL_PATH, "rb") as f:
            self._model = pickle.load(f)
        with open(FEATURES_PATH, "rb") as f:
            self._features = pickle.load(f)
        self._forecast = pd.read_parquet(FORECAST_PATH)
        logger.info(
            "Modelo carregado. Forecast: %d linhas, %d features",
            len(self._forecast),
            len(self._features) if self._features else 0,
        )

    def predict(self, context: PredictionContext) -> PredictionResult:
        """Executa previsão de estado de estoque para UF × produto × competência.

        Args:
            context: Deve conter em ``input_data``:
                - ``uf`` (str): UF alvo — coluna ``sigla_uf`` (ex: ``"AM"``)
                - ``produto_id`` (str): código do produto CEAF — coluna ``codigo_produto``
                  (ex: ``"604020015"``)
                - ``competencia`` (str, opcional): período YYYYMM; converte para data
                  ``data`` do forecast (fallback: ``context.timestamp``)
                - ``estoque_planejado`` (float, opcional): estoque planejado para a UF;
                  default = ``pred_final`` do forecast

        Returns:
            ``PredictionResult`` com ``psi_n`` shape ``(3,)`` normalizado L2.
        """
        self._load()

        # Mapear campos do context para colunas reais do forecast
        uf = context.input_data.get("uf")
        produto_id = str(context.input_data.get("produto_id", "")) if context.input_data.get("produto_id") else None
        competencia = str(context.input_data.get("competencia", context.timestamp))

        # Converter YYYYMM → data para filtrar coluna 'data' do forecast
        import pandas as pd

        forecast = self._forecast
        assert forecast is not None

        try:
            ano = int(competencia[:4])
            mes = int(competencia[4:6])
            data_ref = pd.Timestamp(year=ano, month=mes, day=1)
        except (ValueError, IndexError):
            data_ref = None

        # Construir mask com as colunas reais
        mask = pd.Series([True] * len(forecast), index=forecast.index)
        if uf is not None:
            mask = mask & (forecast["sigla_uf"].astype(str) == str(uf))
        if produto_id is not None:
            mask = mask & (forecast["codigo_produto"].astype(str) == produto_id)
        if data_ref is not None:
            mask = mask & (forecast["data"] == data_ref)

        row = forecast[mask]

        if row.empty:
            logger.warning(
                "Sem previsão para uf=%s produto_id=%s competencia=%s — fallback uniforme",
                uf,
                produto_id,
                competencia,
            )
            psi_n = np.array([0.33, 0.34, 0.33], dtype=np.float64)
            confidence = 0.0
            raw_output = None
        else:
            # pred_final é a quantidade prevista pelo LightGBM
            forecast_qty = float(row["pred_final"].iloc[0])
            estoque_plan = float(context.input_data.get("estoque_planejado", forecast_qty))

            gap_ratio = (forecast_qty - estoque_plan) / max(abs(estoque_plan), 1.0)

            prob_ruptura = float(np.clip(gap_ratio, 0.0, 1.0)) if gap_ratio > 0 else 0.0
            prob_excesso = float(np.clip(-gap_ratio, 0.0, 1.0)) if gap_ratio < 0 else 0.0
            prob_adequado = max(0.0, 1.0 - prob_ruptura - prob_excesso)

            psi_n = np.array([prob_ruptura, prob_adequado, prob_excesso], dtype=np.float64)
            confidence = 0.85

            raw_output = {
                "sigla_uf": uf,
                "codigo_produto": produto_id,
                "competencia": competencia,
                "pred_final": forecast_qty,
                "estoque_planejado": estoque_plan,
                "gap_ratio": gap_ratio,
            }

        # Normalizar L2
        norm = np.linalg.norm(psi_n)
        psi_n = psi_n / norm if norm > 0 else psi_n

        return PredictionResult(
            psi_n=psi_n,
            decision_space=self.DECISION_SPACE,
            raw_output=raw_output,
            confidence=confidence,
            metadata={
                "uf": uf,
                "produto_id": produto_id,
                "competencia": competencia,
                "model_id": "ceaf_lightgbm_v1",
            },
        )

    def get_decision_space(self) -> list[str]:
        """Retorna espaço de decisão estável do predictor CEAF."""
        return self.DECISION_SPACE

    def is_available(self) -> bool:
        """Retorna True se todos os arquivos de modelo e forecast existem."""
        available = MODEL_PATH.exists() and FEATURES_PATH.exists() and FORECAST_PATH.exists()
        if not available:
            logger.warning(
                "LightGBM CEAF indisponível. Verificar: %s, %s, %s",
                MODEL_PATH,
                FEATURES_PATH,
                FORECAST_PATH,
            )
        return available
