# PROMPT CLAUDE CODE — E5 Symbolic Testing
# ==========================================
# Contexto: C:\Workspace\academico\qfeng_validacao — conda activate qfeng
# Data: 2026-04-20
# Pré-requisito: corpus Clingo 9/9 OK + 7 facts files validados

---

## CONTEXTO

O E5 é o módulo de teste simbólico do Q-FENG. Ele:
1. Carrega os predicados do corpus Clingo curado (corpora_clingo/)
2. Carrega os fatos do cenário (corpora_clingo/scenarios/)
3. Executa o predictor correspondente (LightGBM / TimeSeries / Qwen)
4. Constrói |psi_N> (saída do predictor) e |psi_S> (predicados SOVEREIGN ativos)
5. Calcula theta = arccos(<psi_N|psi_S> / ||psi_N||·||psi_S||)
6. Calcula theta_efetivo markoviano (extensão original Kaminski)
7. Determina o regime: STAC (<30°) / HITL (30-120°) / CIRCUIT_BREAKER (>120°)
8. Persiste resultados em outputs/e5_results/

---

## SPEC E5 — ler antes de implementar

Ler a spec completa:
docs/superpowers/specs/2026-04-19-e5-symbolic-testing-design.md

Ler também a spec de outputs de validação:
docs/superpowers/specs/2026-04-19-validation-outputs-design.md

---

## ESTRUTURA DE ARQUIVOS A CRIAR

src/qfeng/e5_symbolic/
    __init__.py
    interference.py        <- cálculo theta e theta_efetivo
    runner.py              <- orquestra cenário completo
    scenario_loader.py     <- carrega .lp do corpus + facts
    psi_builder.py         <- constrói psi_N e psi_S
    results_exporter.py    <- gera os 3 parquets de output
    __main__.py            <- CLI entry point

outputs/e5_results/
    validation_results.parquet
    theta_efetivo_manaus.parquet
    llm_comparison.parquet

---

## IMPLEMENTAÇÃO — módulo a módulo

### interference.py

import numpy as np

def compute_theta(psi_n: np.ndarray, psi_s: np.ndarray) -> float:
    """
    theta = arccos(<psi_N|psi_S> / (||psi_N|| * ||psi_S||))
    Retorna ângulo em graus [0, 180].
    """
    norm_n = np.linalg.norm(psi_n)
    norm_s = np.linalg.norm(psi_s)
    if norm_n == 0 or norm_s == 0:
        return 90.0  # ortogonalidade por definição se um vetor é zero
    cos_theta = np.dot(psi_n, psi_s) / (norm_n * norm_s)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # evitar erros numéricos
    return float(np.degrees(np.arccos(cos_theta)))

def interference_regime(theta_deg: float) -> str:
    if theta_deg < 30:
        return "STAC"
    elif theta_deg < 120:
        return "HITL"
    else:
        return "CIRCUIT_BREAKER"

def compute_theta_efetivo(
    theta_series: list[float],
    score_pressao_series: list[float],
    beta: float = 2.0,
) -> list[float]:
    """
    theta_efetivo(t) = alpha(t) * theta(t) + (1 - alpha(t)) * theta_efetivo(t-1)
    alpha(t) = sigmoid(beta * delta_pressao(t))
    Contribuição original Kaminski — extensão markoviana do QDT.
    """
    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

    theta_efetivo = []
    for t, (theta, score) in enumerate(zip(theta_series, score_pressao_series)):
        if t == 0:
            theta_efetivo.append(theta)
            continue
        delta = score - score_pressao_series[t - 1]
        alpha = sigmoid(beta * delta)
        te = alpha * theta + (1 - alpha) * theta_efetivo[t - 1]
        theta_efetivo.append(te)
    return theta_efetivo

### scenario_loader.py

Usar subprocess para executar Clingo e capturar os átomos derivados:

import subprocess, pathlib, json

CLINGO_BIN = "clingo"
CORPUS_DIR = pathlib.Path("C:/Workspace/academico/qfeng_validacao/corpora_clingo")

SCENARIO_FILES = {
    "C2": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/saude/sus_direito_saude.lp",
            "brasil/emergencia_manaus/emergencia_sanitaria.lp",
        ],
        "facts": "scenarios/c2_manaus_facts.lp",
    },
    "C3": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/saude/sus_direito_saude.lp",
        ],
        "facts": "scenarios/c3_concentracao_facts.lp",
    },
    "C7": {
        "corpus": [
            "usa/civil_rights/civil_rights_14th.lp",
            "usa/medicaid/medicaid_access.lp",
        ],
        "facts": "scenarios/c7_obermeyer_facts.lp",
    },
    "T-CLT-01": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
            "brasil/processual/cpc_fundamentacao.lp",
        ],
        "facts": "scenarios/t_clt_01_facts.lp",
    },
    "T-CLT-02": {
        "corpus": [
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        ],
        "facts": "scenarios/t_clt_02_facts.lp",
    },
    "T-CLT-03": {
        "corpus": [
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        ],
        "facts": "scenarios/t_clt_03_facts.lp",
    },
}

def run_clingo(corpus_files: list[str], facts_file: str) -> dict:
    """
    Executa Clingo e retorna:
    - satisfiable: bool
    - active_sovereign: list[str]  (átomos sovereign() derivados)
    - active_elastic: list[str]
    - raw_output: str
    """
    lp_files = [str(CORPUS_DIR / f) for f in corpus_files]
    lp_files.append(str(CORPUS_DIR / facts_file))
    
    result = subprocess.run(
        [CLINGO_BIN] + lp_files + ["--models=1", "--outf=2"],
        capture_output=True, text=True, timeout=30
    )
    
    satisfiable = "SATISFIABLE" in result.stdout
    unsatisfiable = "UNSATISFIABLE" in result.stdout
    
    # Extrair átomos derivados do modelo (se SAT)
    active_sovereign = []
    active_elastic = []
    if satisfiable:
        for line in result.stdout.split():
            if line.startswith("sovereign("):
                active_sovereign.append(line)
            elif line.startswith("elastic("):
                active_elastic.append(line)
    
    return {
        "satisfiable": satisfiable,
        "unsatisfiable": unsatisfiable,
        "active_sovereign": active_sovereign,
        "active_elastic": active_elastic,
        "raw_output": result.stdout,
    }

### psi_builder.py

def build_psi_s(active_sovereign: list[str], decision_space: list[str]) -> np.ndarray:
    """
    Constrói |psi_S> a partir dos predicados SOVEREIGN ativos.
    Dimensão = len(decision_space).
    Para cada ação no decision_space, verifica se algum sovereign ativo
    a proíbe ou restringe (reduz o componente) ou a reforça (aumenta).
    """
    psi_s = np.ones(len(decision_space), dtype=np.float64)
    
    # Predicados que bloqueiam ações específicas
    blocking_patterns = {
        "deny_access": ["prohibition", "forbid", "deny"],
        "continue_normal_operations": ["obligation_immediate", "circuit_breaker"],
        "maintain_current_allocation": ["equity", "equality", "reduce_inequality"],
        "autonomous": ["human_oversight", "hitl", "review"],
    }
    
    for i, action in enumerate(decision_space):
        for sovereign in active_sovereign:
            for pattern in blocking_patterns.get(action, []):
                if pattern in sovereign.lower():
                    psi_s[i] *= 0.1  # ação bloqueada por predicado soberano
    
    # Normalizar L2
    norm = np.linalg.norm(psi_s)
    if norm > 0:
        psi_s = psi_s / norm
    return psi_s

### runner.py — orquestração completa

Para cada cenário em SCENARIO_FILES:
1. run_clingo() → satisfiable + active_sovereign
2. predictor.predict() → psi_n (do predictor real ou sintético)
3. build_psi_s() → psi_s
4. compute_theta(psi_n, psi_s) → theta_deg
5. interference_regime(theta_deg) → regime
6. Calcular alhedonic_signal e cybernetic_loss
7. Persistir em validation_results.parquet

Para C2 (série temporal):
8. Iterar sobre todas as competências (out/2020 a mar/2021)
9. compute_theta_efetivo() → trajetória markoviana
10. Persistir em theta_efetivo_manaus.parquet

Para C4a vs C4b (se Ollama disponível):
11. Comparar theta sem predicados vs com predicados
12. Persistir em llm_comparison.parquet

---

## SCHEMAS DE OUTPUT (OBRIGATÓRIOS)

### validation_results.parquet — colunas obrigatórias:
scenario_id, corpus, regime_normativo, condition,
theta_deg, theta_rad, interference_regime,
psi_n_json, psi_s_json,
n_sovereign_active, n_elastic_active,
alhedonic_signal, predictor_type, predictor_confidence,
outcome_label, outcome_description,
data_source, n_observations, cybernetic_loss, timestamp

data_source valores aceitos:
  "real_primary"         <- SIH/DATASUS, CEAF, Obermeyer, TST
  "real_normative"       <- predicados ASP de corpus real
  "synthetic_calibrated" <- C5, C6, C8

### theta_efetivo_manaus.parquet — colunas obrigatórias:
competencia, ano_cmpt, mes_cmpt,
theta_t, theta_efetivo, alpha_t,
interference_regime, internacoes_total, obitos_total,
taxa_mortalidade, score_pressao, delta_pressao,
delta_theta, n_sovereign_ativados, evento_critico

### llm_comparison.parquet — colunas obrigatórias:
scenario_id, query_id, condition,
theta_deg, psi_n_json, action_recommended,
action_normatively_correct, reduction_delta,
n_sovereign_injected

---

## COMANDO DE EXECUÇÃO (uma linha)

python -m qfeng.e5_symbolic --output-dir outputs/e5_results

---

## RELATÓRIO ESPERADO

Tabela com todos os cenários:

| Cenário | theta_deg | Regime | SAT/UNSAT | n_sovereign | outcome | data_source |
|---------|-----------|--------|-----------|-------------|---------|-------------|

Mais:
- Trajetória theta_efetivo Manaus (6 competências: out/2020 a mar/2021)
- Comparativo C4a vs C4b (se Ollama disponível — não bloquear se não estiver)
- Arquivos parquet gerados com tamanho e n_rows

---

## RESTRIÇÕES

- Motor simbólico: Clingo ASP puro
- psi_n e psi_s: numpy array 1D float64, normalizados L2
- Floats não suportados em Clingo: usar inteiros (percentual)
- NÃO modificar corpora_clingo/ (somente leitura)
- NÃO modificar schemas.py
- Se Ollama indisponível: pular C4a/b/c sem erro — registrar como "skipped"
- Se predictor indisponível: usar psi_n sintético calibrado + declarar data_source="synthetic_calibrated"

---

## NAO prosseguir para análise de resultados ou figuras sem aprovação de Ricardo.
