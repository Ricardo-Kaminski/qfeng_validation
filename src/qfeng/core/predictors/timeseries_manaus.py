"""TimeSeries Manaus SIH Predictor — Crise de Oxigênio Manaus 2021.

Predictor de série temporal para o Cenário C2 — Crise de Oxigênio Manaus.

|ψ_N⟩ = vetor de estado hospitalar:
    [prob_colapso_critico, prob_alerta, prob_estavel]

Derivado de dados do SIH/SUS (Sistema de Informações Hospitalares):
    - contagem mensal de internações por prefixo CID (ex: 'J' → respiratórias)
    - dias de UTI total (UTI_MES_TO)
    - taxa de mortalidade (MORTE / N_AIH)

Permite demonstrar a trajetória θ_efetivo ao longo do tempo:
    out/2020 → θ < 30° (STAC) → dez/2020 → θ ≈ 90° (HITL) → jan/2021 → θ > 120° (Circuit Breaker)
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

import numpy as np

from qfeng.core.predictor_interface import (
    PredictionContext,
    PredictionResult,
    PredictorInterface,
)

if TYPE_CHECKING:
    import pandas as pd

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parents[4] / "data" / "predictors" / "manaus_sih"
SIH_PATH = DATA_DIR / "sih_manaus_2020_2021.parquet"

# Thresholds calibrados com base no período de colapso (jan/2021)
THRESHOLD_COLAPSO: float = 0.25  # taxa_mortalidade > 25% → colapso crítico
THRESHOLD_ALERTA: float = 0.12   # taxa_mortalidade > 12% → alerta
UTI_THRESHOLD: float = 500.0     # dias UTI/mês acima deste valor → pressão crítica


class TimeSeriesManausPredictor(PredictorInterface):
    """Predictor de série temporal para o Cenário C2 — Crise de Oxigênio Manaus.

    Espaço de decisão:
        - ``colapso_critico``: θ > 120° → Circuit Breaker + Sinal Algédônico
        - ``alerta``: 30° < θ < 120° → HITL acionado
        - ``estavel``: θ < 30° → STAC autônomo
    """

    DECISION_SPACE: list[str] = [
        "colapso_critico",
        "alerta",
        "estavel",
    ]

    def __init__(self) -> None:
        self._df: pd.DataFrame | None = None  # dados brutos SIH
        self._max_count: float = 1.0          # para normalização

    def _load(self) -> None:
        """Lazy loading dos dados SIH brutos."""
        if self._df is not None:
            return

        import pandas as pd

        logger.info("Carregando SIH Manaus de %s", SIH_PATH)
        df = pd.read_parquet(SIH_PATH)

        # Construir coluna COMPETENCIA no formato YYYYMM
        df["COMPETENCIA"] = (
            df["ANO_CMPT"].astype(str)
            + df["MES_CMPT"].astype(str).str.zfill(2)
        )

        # Converter colunas numéricas relevantes
        for col in ("UTI_MES_TO", "MORTE", "QT_DIARIAS"):
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        self._df = df

        # Calcular contagem máxima de internações mensais para normalização
        monthly_counts = df.groupby("COMPETENCIA").size()
        self._max_count = float(max(monthly_counts.max(), 1))
        logger.info(
            "SIH carregado: %d registros, %d competências, max_mensal=%d",
            len(df),
            df["COMPETENCIA"].nunique(),
            int(self._max_count),
        )

    def predict(self, context: PredictionContext) -> PredictionResult:
        """Executa previsão de estado hospitalar para uma competência × prefixo CID.

        Args:
            context: Deve conter em ``input_data``:
                - ``competencia`` (str): período YYYYMM (ex: ``"202101"``)
                - ``diag_prefix`` (str, opcional): prefixo CID para filtrar
                  (ex: ``"J"`` → respiratórias). Default: sem filtro.

        Returns:
            ``PredictionResult`` com ``psi_n`` shape ``(3,)`` normalizado L2.
            ``prediction[0]`` (colapso_critico) é normalizado 0–1.
        """
        self._load()

        competencia = str(context.input_data.get("competencia", context.timestamp))
        diag_prefix = context.input_data.get("diag_prefix", "")

        df = self._df
        assert df is not None  # satisfaz mypy após _load

        # Filtrar por competência
        mask = df["COMPETENCIA"] == competencia
        if diag_prefix:
            mask = mask & df["DIAG_PRINC"].astype(str).str.startswith(str(diag_prefix))

        subset = df[mask]

        if subset.empty:
            logger.warning(
                "Sem registros para competencia=%s diag_prefix=%s — fallback uniforme",
                competencia,
                diag_prefix,
            )
            psi_n = np.array([0.33, 0.34, 0.33], dtype=np.float64)
            confidence = 0.0
            raw_output: dict[str, Any] | None = None
        else:
            n_internacoes = len(subset)
            n_mortes = int(subset["MORTE"].sum()) if "MORTE" in subset.columns else 0
            dias_uti = float(subset["UTI_MES_TO"].sum()) if "UTI_MES_TO" in subset.columns else 0.0

            taxa_mortalidade = n_mortes / max(n_internacoes, 1)

            # Score de pressão combinado
            pressao_mort = min(taxa_mortalidade / THRESHOLD_COLAPSO, 1.0)
            pressao_uti = min(dias_uti / UTI_THRESHOLD, 1.0)
            score_pressao = 0.6 * pressao_mort + 0.4 * pressao_uti

            # Converter em distribuição de probabilidade
            if score_pressao >= 0.85:
                prob_colapso = 0.80
                prob_alerta = 0.15
                prob_estavel = 0.05
            elif score_pressao >= 0.50:
                prob_colapso = 0.20
                prob_alerta = 0.65
                prob_estavel = 0.15
            else:
                prob_colapso = 0.05
                prob_alerta = 0.20
                prob_estavel = 0.75

            psi_n = np.array([prob_colapso, prob_alerta, prob_estavel], dtype=np.float64)
            confidence = 0.85
            raw_output = {
                "competencia": competencia,
                "diag_prefix": diag_prefix,
                "n_internacoes": n_internacoes,
                "n_internacoes_normalized": n_internacoes / self._max_count,
                "n_mortes": n_mortes,
                "taxa_mortalidade": taxa_mortalidade,
                "dias_uti_total": dias_uti,
                "score_pressao": score_pressao,
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
                "competencia": competencia,
                "diag_prefix": diag_prefix,
                "municipio": "Manaus/AM",
                "model_id": "manaus_sih_timeseries_v1",
            },
        )

    def get_decision_space(self) -> list[str]:
        """Retorna espaço de decisão estável do predictor Manaus."""
        return self.DECISION_SPACE

    def is_available(self) -> bool:
        """Retorna True se o arquivo SIH parquet existe."""
        available = SIH_PATH.exists()
        if not available:
            logger.warning("SIH Manaus indisponível: %s", SIH_PATH)
        return available

    def get_trajetoria_theta(
        self,
        interference_engine: Any,
        active_predicates: list[str],
        diag_prefix: str = "J",
    ) -> list[dict[str, Any]]:
        """Computa a trajetória θ_efetivo para todos os períodos disponíveis.

        Usado no Cenário C4c (θ_efetivo markoviano) e para o cartograma temporal.

        Args:
            interference_engine: Instância de ``InterferenceEngine`` de ``interference.py``.
            active_predicates: Predicados Clingo soberanos a usar no alinhamento.
            diag_prefix: Prefixo CID a filtrar (default: ``"J"`` → respiratórias).

        Returns:
            Lista de ``{competencia, theta, regime, score_pressao}`` ordenada temporalmente.
        """
        self._load()
        df = self._df
        assert df is not None

        competencias = sorted(df["COMPETENCIA"].unique())
        trajetoria = []

        for comp in competencias:
            ctx = PredictionContext(
                scenario_id=f"manaus_{comp}",
                regime="brasil",
                timestamp=comp,
                input_data={"competencia": comp, "diag_prefix": diag_prefix},
                active_predicates=active_predicates,
            )
            result = self.predict(ctx)
            psi_s = self.align_with_predicates(result, active_predicates)
            theta = interference_engine.compute_theta(result.psi_n, psi_s)

            if theta < 30:
                regime = "STAC"
            elif theta < 120:
                regime = "HITL"
            else:
                regime = "CIRCUIT_BREAKER"

            trajetoria.append({
                "competencia": comp,
                "theta": theta,
                "regime": regime,
                "score_pressao": result.raw_output.get("score_pressao") if result.raw_output else None,
            })

        return trajetoria
