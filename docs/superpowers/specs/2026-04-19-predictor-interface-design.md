# Spec: Predictor Interface + Implementações Concretas
# ======================================================
# Data: 2026-04-19
# Status: Para implementação pelo Claude Code após E0 aprovado
# Módulo: src/qfeng/core/predictor_interface.py
#         src/qfeng/core/predictors/
#
# Contexto:
# O Q-FENG é agnóstico ao modelo preditivo subjacente. O canal θ opera sobre
# dois vetores: |ψ_N⟩ (estado do sistema operacional — saída do predictor) e
# |ψ_S⟩ (estado normativo — predicados Clingo soberanos ativos). A PredictorInterface
# define o contrato que qualquer predictor deve satisfazer para interagir com o
# interference.py já implementado em core/.
#
# Três implementações concretas para o MVP:
# 1. LightGBMPredictor  — IADAF (medicamentos CEAF, 180 meses)
# 2. TimeSeriesPredictor — SIH/SUS Manaus (série temporal hospitalar)
# 3. OllamaPredictor    — Qwen 2.5 14B local (agente decisório clínico)

---

## 1. Estrutura de arquivos

```
src/qfeng/core/
├── predictor_interface.py    ← ABC + tipos + utilitários
└── predictors/
    ├── __init__.py
    ├── lightgbm_ceaf.py      ← LightGBMPredictor
    ├── timeseries_manaus.py  ← TimeSeriesPredictor
    └── ollama_qwen.py        ← OllamaPredictor

tests/test_predictors/
├── __init__.py
├── test_interface.py         ← testa contrato ABC
├── test_lightgbm_ceaf.py
├── test_timeseries_manaus.py
└── test_ollama_qwen.py

data/predictors/
├── ceaf_medicamentos/        ← já populado (46 MB)
└── manaus_sih/               ← a popular via extract_manaus_sih.py
```

---

## 2. predictor_interface.py — ABC e tipos

```python
# src/qfeng/core/predictor_interface.py
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any
import numpy as np


@dataclass
class PredictionContext:
    """
    Contexto de entrada para qualquer predictor.
    Campos obrigatórios + extensão via extra_data.
    """
    scenario_id: str                          # identificador do cenário (ex: "manaus_2020_12")
    regime: str                               # "brasil" | "eu" | "usa"
    timestamp: str                            # período de referência (ex: "202012", "2021-01-13")
    input_data: dict[str, Any]                # dados de entrada específicos do domínio
    active_predicates: list[str]              # predicados Clingo soberanos ativos neste momento
    system_prompt: str = ""                   # para LLM predictors: instrução normativa
    extra_data: dict[str, Any] = field(default_factory=dict)


@dataclass
class PredictionResult:
    """
    Resultado de qualquer predictor → |ψ_N⟩.
    """
    psi_n: np.ndarray                         # vetor de estado neural/preditivo (normalizado L2)
    decision_space: list[str]                 # rótulos do espaço de decisão
    raw_output: Any                           # output bruto do modelo (para auditoria)
    confidence: float                         # confiança agregada (0–1)
    metadata: dict[str, Any] = field(default_factory=dict)


class PredictorInterface(ABC):
    """
    Interface agnóstica ao modelo preditivo.

    Qualquer predictor — LightGBM, série temporal, LLM — implementa este
    contrato para interagir com interference.py via o canal θ.

    O contrato garante que:
    1. predict() sempre retorna PredictionResult com psi_n normalizado
    2. get_decision_space() retorna rótulos estáveis (necessário para alinhar com |ψ_S⟩)
    3. is_available() permite detecção de dependências ausentes sem crash
    """

    @abstractmethod
    def predict(self, context: PredictionContext) -> PredictionResult:
        """
        Executa inferência e retorna |ψ_N⟩.

        context: PredictionContext com dados de entrada do cenário
        retorna: PredictionResult com psi_n normalizado (L2, sum=1.0 ou norm=1.0)

        CONTRATO: psi_n deve ser vetor numpy 1D float64, normalizado.
        CONTRATO: len(psi_n) == len(get_decision_space())
        """
        ...

    @abstractmethod
    def get_decision_space(self) -> list[str]:
        """
        Retorna rótulos estáveis do espaço de decisão.

        Exemplos:
        - LightGBM CEAF: ["ruptura_iminente", "estoque_adequado", "excesso"]
        - TimeSeries Manaus: ["colapso_critico", "alerta", "estavel"]
        - Ollama Qwen: ["escalar_coes", "hitl_requerido", "conduta_autonoma", "bloqueio"]

        CONTRATO: lista estável — não muda entre chamadas do mesmo predictor.
        Necessário para alinhar dimensões com |ψ_S⟩ no interference.py.
        """
        ...

    @abstractmethod
    def is_available(self) -> bool:
        """
        Verifica se as dependências do predictor estão disponíveis.
        Permite testes sem crash quando modelo/servidor não está presente.
        """
        ...

    def align_with_predicates(
        self,
        result: PredictionResult,
        active_predicates: list[str],
        predicate_weights: dict[str, float] | None = None,
    ) -> np.ndarray:
        """
        Alinha |ψ_N⟩ com o espaço de predicados normativos para cálculo de θ.

        Método utilitário fornecido pela ABC — predictors não precisam reimplementar.
        Retorna |ψ_S⟩ como vetor numpy alinhado com psi_n.

        predicate_weights: pesos por predicado (default: uniforme)
        """
        n = len(result.psi_n)
        psi_s = np.zeros(n, dtype=np.float64)

        weights = predicate_weights or {p: 1.0 for p in active_predicates}
        decision_space = self.get_decision_space()

        for pred, weight in weights.items():
            # Mapeamento heurístico: predicado soberano → dimensão do espaço
            # Ex: "ativar_coes" → índice 0 ("escalar_coes" em Qwen)
            for i, label in enumerate(decision_space):
                if any(kw in label for kw in pred.split("_")):
                    psi_s[i] += weight

        # Normalizar L2
        norm = np.linalg.norm(psi_s)
        if norm > 0:
            psi_s = psi_s / norm

        return psi_s
```

---

## 3. LightGBMPredictor — IADAF/CEAF

```python
# src/qfeng/core/predictors/lightgbm_ceaf.py

from pathlib import Path
import numpy as np
import pandas as pd
from qfeng.core.predictor_interface import (
    PredictorInterface, PredictionContext, PredictionResult
)

DATA_DIR = Path(__file__).parents[4] / "data" / "predictors" / "ceaf_medicamentos"
MODEL_PATH = DATA_DIR / "model_pharma_sota_v1.pkl"
FEATURES_PATH = DATA_DIR / "features_list.pkl"
FORECAST_PATH = DATA_DIR / "forecast_t12_final.parquet"


class LightGBMCEAFPredictor(PredictorInterface):
    """
    Predictor baseado no modelo LightGBM do IADAF para medicamentos CEAF.

    |ψ_N⟩ = vetor de probabilidade de estado de estoque por UF × produto:
    [prob_ruptura_iminente, prob_estoque_adequado, prob_excesso_estoque]

    Cenários Q-FENG:
    - C1 (falha de execução): ruptura prevista, predicado fornecimento_continuo existe
      mas cadeia algédônica não escala → θ > 120°, Circuit Breaker
    - C3 (falha constitucional): predicado equidade_regional_uf ausente →
      θ estruturalmente incalculável
    """

    DECISION_SPACE = [
        "ruptura_iminente",      # prob > threshold → Circuit Breaker
        "estoque_adequado",      # zona STAC
        "excesso_estoque",       # ineficiência alocativa
    ]

    # Threshold de ruptura iminente (configurável via ScopeConfig futuro)
    RUPTURA_THRESHOLD = 0.30

    def __init__(self) -> None:
        self._model = None
        self._features: list[str] | None = None
        self._forecast: pd.DataFrame | None = None

    def _load(self) -> None:
        """Lazy loading — carrega modelo apenas quando necessário."""
        if self._model is not None:
            return
        import pickle
        with open(MODEL_PATH, "rb") as f:
            self._model = pickle.load(f)
        with open(FEATURES_PATH, "rb") as f:
            self._features = pickle.load(f)
        self._forecast = pd.read_parquet(FORECAST_PATH)

    def predict(self, context: PredictionContext) -> PredictionResult:
        self._load()

        uf = context.input_data.get("uf")
        produto_id = context.input_data.get("produto_id")
        competencia = context.input_data.get("competencia", context.timestamp)

        # Buscar forecast para UF × produto × competência
        mask = (
            (self._forecast["uf"] == uf) &
            (self._forecast["produto_id"] == produto_id) &
            (self._forecast["competencia"] == competencia)
        )
        row = self._forecast[mask]

        if row.empty:
            # Fallback: sem previsão disponível → incerteza máxima
            psi_n = np.array([0.33, 0.34, 0.33])
            confidence = 0.0
            raw_output = None
        else:
            forecast_qty = float(row["forecast_quantidade"].iloc[0])
            estoque_plan = float(context.input_data.get("estoque_planejado", forecast_qty))

            gap_ratio = (forecast_qty - estoque_plan) / max(estoque_plan, 1.0)

            # Converter gap em distribuição de probabilidade
            prob_ruptura = float(np.clip(gap_ratio, 0, 1)) if gap_ratio > 0 else 0.0
            prob_excesso = float(np.clip(-gap_ratio, 0, 1)) if gap_ratio < 0 else 0.0
            prob_adequado = 1.0 - prob_ruptura - prob_excesso

            psi_n = np.array([prob_ruptura, prob_adequado, prob_excesso])
            confidence = float(row.get("confidence", pd.Series([0.85])).iloc[0])
            raw_output = row.to_dict("records")[0]

        # Normalizar L2
        norm = np.linalg.norm(psi_n)
        psi_n = psi_n / norm if norm > 0 else psi_n

        return PredictionResult(
            psi_n=psi_n,
            decision_space=self.DECISION_SPACE,
            raw_output=raw_output,
            confidence=confidence,
            metadata={"uf": uf, "produto_id": produto_id, "competencia": competencia},
        )

    def get_decision_space(self) -> list[str]:
        return self.DECISION_SPACE

    def is_available(self) -> bool:
        return MODEL_PATH.exists() and FEATURES_PATH.exists() and FORECAST_PATH.exists()
```

---

## 4. TimeSeriesPredictor — SIH/SUS Manaus

```python
# src/qfeng/core/predictors/timeseries_manaus.py

from pathlib import Path
import numpy as np
import pandas as pd
from qfeng.core.predictor_interface import (
    PredictorInterface, PredictionContext, PredictionResult
)

DATA_DIR = Path(__file__).parents[4] / "data" / "predictors" / "manaus_sih"
SERIE_PATH = DATA_DIR / "serie_temporal_manaus.parquet"

# Thresholds calibrados com base no período de colapso (jan/2021)
THRESHOLD_COLAPSO = 0.25     # taxa_mortalidade > 25% → colapso crítico
THRESHOLD_ALERTA  = 0.12     # taxa_mortalidade > 12% → alerta
UTI_THRESHOLD     = 500      # dias UTI/mês acima deste valor → pressão crítica


class TimeSeriesManausPredictor(PredictorInterface):
    """
    Predictor de série temporal para o Cenário C2 — Crise de Oxigênio Manaus.

    |ψ_N⟩ = vetor de estado hospitalar:
    [prob_colapso_critico, prob_alerta, prob_estavel]

    Derivado de:
    - taxa_mortalidade (óbitos / internações CID J96/J18/U07)
    - dias_uti_total (pressão em UTI)
    - variação_internacoes_7d (tendência)

    Permite demonstrar a trajetória θ_efetivo ao longo do tempo:
    out/2020 → θ < 30° (STAC) → dez/2020 → θ ≈ 90° (HITL) → jan/2021 → θ > 120° (Circuit Breaker)
    """

    DECISION_SPACE = [
        "colapso_critico",    # θ > 120° → Circuit Breaker + Sinal Algédônico
        "alerta",             # 30° < θ < 120° → HITL acionado
        "estavel",            # θ < 30° → STAC autônomo
    ]

    def __init__(self) -> None:
        self._serie: pd.DataFrame | None = None

    def _load(self) -> None:
        if self._serie is not None:
            return
        self._serie = pd.read_parquet(SERIE_PATH)
        # Garantir ordenação temporal
        self._serie = self._serie.sort_values("COMPETENCIA")

    def predict(self, context: PredictionContext) -> PredictionResult:
        self._load()

        competencia = context.input_data.get("competencia", context.timestamp)

        # Buscar competência (formato AAAAMM ex: "202012")
        row = self._serie[self._serie["COMPETENCIA"] == str(competencia)]

        if row.empty:
            psi_n = np.array([0.33, 0.34, 0.33])
            confidence = 0.0
            raw_output = None
        else:
            taxa_mort = float(row["taxa_mortalidade"].iloc[0])
            dias_uti = float(row["dias_uti_total"].iloc[0])
            internacoes = float(row["internacoes_total"].iloc[0])

            # Score de pressão combinado
            pressao_mort = min(taxa_mort / THRESHOLD_COLAPSO, 1.0)
            pressao_uti = min(dias_uti / UTI_THRESHOLD, 1.0)
            score_pressao = 0.6 * pressao_mort + 0.4 * pressao_uti

            # Converter em distribuição de probabilidade
            if score_pressao >= 0.85:
                prob_colapso = 0.80
                prob_alerta  = 0.15
                prob_estavel = 0.05
            elif score_pressao >= 0.50:
                prob_colapso = 0.20
                prob_alerta  = 0.65
                prob_estavel = 0.15
            else:
                prob_colapso = 0.05
                prob_alerta  = 0.20
                prob_estavel = 0.75

            psi_n = np.array([prob_colapso, prob_alerta, prob_estavel])
            confidence = 0.90
            raw_output = {
                "competencia": competencia,
                "taxa_mortalidade": taxa_mort,
                "dias_uti_total": dias_uti,
                "internacoes_total": internacoes,
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
            metadata={"competencia": competencia, "municipio": "Manaus/AM"},
        )

    def get_decision_space(self) -> list[str]:
        return self.DECISION_SPACE

    def is_available(self) -> bool:
        return SERIE_PATH.exists()

    def get_trajetoria_theta(
        self,
        interference_engine,
        active_predicates: list[str],
    ) -> list[dict]:
        """
        Computa a trajetória θ_efetivo para todos os períodos disponíveis.

        Usado no Cenário C4c (θ_efetivo markoviano) e para o cartograma temporal.
        Retorna lista de {competencia, theta, regime_interferencia}.
        """
        self._load()
        trajetoria = []

        for _, row in self._serie.iterrows():
            ctx = PredictionContext(
                scenario_id=f"manaus_{row['COMPETENCIA']}",
                regime="brasil",
                timestamp=str(row["COMPETENCIA"]),
                input_data={"competencia": row["COMPETENCIA"]},
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
                "competencia": row["COMPETENCIA"],
                "theta": theta,
                "regime": regime,
                "score_pressao": result.raw_output.get("score_pressao", None) if result.raw_output else None,
            })

        return trajetoria
```

---

## 5. OllamaPredictor — Qwen 2.5 14B

```python
# src/qfeng/core/predictors/ollama_qwen.py

import json
import numpy as np
from qfeng.core.predictor_interface import (
    PredictorInterface, PredictionContext, PredictionResult
)

OLLAMA_ENDPOINT = "http://localhost:11434"
DEFAULT_MODEL   = "qwen2.5:14b"

# Espaço de decisão clínica para cenários normativos
DECISION_SPACE = [
    "escalar_coes",          # acionar cadeia de comando → Circuit Breaker normativo
    "hitl_especialista",     # encaminhar para especialista humano
    "conduta_autonoma",      # STAC — modelo age sem intervenção
    "bloqueio_normativo",    # conduta impossível por constraint soberano
]

# System prompt base (sem predicados — para C4a)
SYSTEM_PROMPT_BASE = """Você é um sistema de apoio à decisão clínica do SUS.
Dado um contexto clínico, responda APENAS com um JSON no formato:
{
  "acao_recomendada": "<uma das ações possíveis>",
  "justificativa": "<máximo 2 frases>",
  "probabilidades": {
    "escalar_coes": <float 0-1>,
    "hitl_especialista": <float 0-1>,
    "conduta_autonoma": <float 0-1>,
    "bloqueio_normativo": <float 0-1>
  }
}
As probabilidades devem somar 1.0.
Ações possíveis: escalar_coes, hitl_especialista, conduta_autonoma, bloqueio_normativo"""

# System prompt com predicados normativos injetados (para C4b)
SYSTEM_PROMPT_NORMATIVO = """Você é um sistema de apoio à decisão clínica do SUS.
Você opera sob as seguintes restrições normativas INVIOLÁVEIS (predicados soberanos):
{predicados}

Dado o contexto clínico, responda APENAS com JSON:
{
  "acao_recomendada": "<uma das ações possíveis>",
  "justificativa": "<máximo 2 frases>",
  "probabilidades": {
    "escalar_coes": <float 0-1>,
    "hitl_especialista": <float 0-1>,
    "conduta_autonoma": <float 0-1>,
    "bloqueio_normativo": <float 0-1>
  }
}
As probabilidades devem somar 1.0."""


class OllamaQwenPredictor(PredictorInterface):
    """
    Predictor via Qwen 2.5 14B local (Ollama).

    Demonstra dois sub-cenários:
    - C4a: LLM sem constraint normativo → θ alto (diverge da norma)
    - C4b: LLM com predicados soberanos injetados no system prompt → θ reduz
    - C4c: Sequência temporal → trajetória θ_efetivo markoviano (contribuição original)

    |ψ_N⟩ = distribuição de probabilidade sobre 4 ações clínicas,
    extraída das probabilidades na resposta JSON do Qwen.
    """

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        endpoint: str = OLLAMA_ENDPOINT,
        inject_predicates: bool = False,
    ) -> None:
        self.model = model
        self.endpoint = endpoint
        self.inject_predicates = inject_predicates

    def predict(self, context: PredictionContext) -> PredictionResult:
        import requests

        # Selecionar system prompt
        if self.inject_predicates and context.active_predicates:
            predicados_str = "\n".join(
                f"- {p}" for p in context.active_predicates
            )
            system = SYSTEM_PROMPT_NORMATIVO.format(predicados=predicados_str)
        elif context.system_prompt:
            system = context.system_prompt
        else:
            system = SYSTEM_PROMPT_BASE

        # Contexto clínico como user message
        user_msg = context.input_data.get("clinical_context", "")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user_msg},
            ],
            "stream": False,
            "format": "json",
            "options": {"temperature": 0.1},  # baixo para reprodutibilidade
        }

        response = requests.post(
            f"{self.endpoint}/api/chat",
            json=payload,
            timeout=120,
        )
        response.raise_for_status()

        raw = response.json()
        content = raw["message"]["content"]

        # Parsear JSON da resposta
        try:
            parsed = json.loads(content)
            probs = parsed.get("probabilidades", {})
            psi_n = np.array([
                probs.get("escalar_coes", 0.25),
                probs.get("hitl_especialista", 0.25),
                probs.get("conduta_autonoma", 0.25),
                probs.get("bloqueio_normativo", 0.25),
            ], dtype=np.float64)
            confidence = 0.85
        except (json.JSONDecodeError, KeyError):
            # Fallback: distribuição uniforme se parsing falha
            psi_n = np.array([0.25, 0.25, 0.25, 0.25], dtype=np.float64)
            confidence = 0.0
            parsed = {"raw_text": content}

        # Normalizar L2
        norm = np.linalg.norm(psi_n)
        psi_n = psi_n / norm if norm > 0 else psi_n

        return PredictionResult(
            psi_n=psi_n,
            decision_space=DECISION_SPACE,
            raw_output=parsed,
            confidence=confidence,
            metadata={
                "model": self.model,
                "inject_predicates": self.inject_predicates,
                "scenario_id": context.scenario_id,
            },
        )

    def get_decision_space(self) -> list[str]:
        return DECISION_SPACE

    def is_available(self) -> bool:
        """Verifica se Ollama está rodando e o modelo está disponível."""
        import requests
        try:
            r = requests.get(f"{self.endpoint}/api/tags", timeout=5)
            models = [m["name"] for m in r.json().get("models", [])]
            return any(self.model in m for m in models)
        except Exception:
            return False
```

---

## 6. Testes

### test_interface.py — contrato ABC

| Caso | Esperado |
|------|---------|
| Instanciar ABC diretamente | `TypeError` (não pode instanciar ABC) |
| predict() retorna psi_n normalizado L2 | `abs(norm(psi_n) - 1.0) < 1e-6` |
| len(psi_n) == len(decision_space) | sempre True |
| is_available() retorna bool | sem exceção |

### test_lightgbm_ceaf.py

| Caso | Esperado |
|------|---------|
| Modelo disponível | `is_available() == True` |
| Predict UF + produto válido | psi_n shape (3,), normalizado |
| Predict UF inexistente | fallback uniform, confidence=0.0 |
| sum(psi_n) ≈ 1.0 (após normalização) | True (norma L2 = 1) |

### test_timeseries_manaus.py

| Caso | Esperado |
|------|---------|
| Série não disponível | `is_available() == False` (antes da extração) |
| Competência "202101" (pico) | psi_n[0] (colapso_critico) > 0.5 |
| Competência "202010" (baseline) | psi_n[2] (estavel) > 0.5 |
| get_trajetoria_theta() | lista com 6 itens (out/2020 → mar/2021) |

### test_ollama_qwen.py

| Caso | Esperado |
|------|---------|
| Ollama não disponível | `is_available() == False` (não crasha) |
| Predict com Ollama disponível | psi_n normalizado, len=4 |
| inject_predicates=True vs False | psi_n diferente (predicados mudam a decisão) |

---

## 7. Critérios de aprovação

### Fase A (pytest)
```bash
pytest tests/test_predictors/ -v
ruff check src/qfeng/core/predictor_interface.py src/qfeng/core/predictors/
mypy src/qfeng/core/predictor_interface.py src/qfeng/core/predictors/
```

### Fase B (execução real)

```python
# Notebook de validação: notebooks/validate_predictors.ipynb

# 1. LightGBM CEAF
from qfeng.core.predictors.lightgbm_ceaf import LightGBMCEAFPredictor
p = LightGBMCEAFPredictor()
assert p.is_available()
# result = p.predict(ctx_ceaf)  # com UF e produto reais

# 2. TimeSeries Manaus (após extract_manaus_sih.py)
from qfeng.core.predictors.timeseries_manaus import TimeSeriesManausPredictor
p = TimeSeriesManausPredictor()
# assert p.is_available()  # True após extração
# trajetoria = p.get_trajetoria_theta(interference_engine, predicados_manaus)

# 3. Ollama Qwen
from qfeng.core.predictors.ollama_qwen import OllamaQwenPredictor
p = OllamaQwenPredictor()
assert p.is_available()  # True se Ollama rodando
# result_sem = p.predict(ctx_manaus_sem_predicados)
# result_com = OllamaQwenPredictor(inject_predicates=True).predict(ctx_manaus_com_predicados)
# assert not np.allclose(result_sem.psi_n, result_com.psi_n)  # predicados mudam a decisão
```

---

## 8. O que NÃO está no escopo deste módulo

- Integração com interference.py (responsabilidade do E5)
- θ_efetivo markoviano completo (implementado no E5 usando get_trajetoria_theta)
- Fine-tuning ou retreinamento de modelos
- Streaming de respostas Ollama
- Múltiplos modelos Ollama simultâneos
