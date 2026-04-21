# BRIEFING DE PONTE — Sessão 20-21 abr 2026 (ATUALIZADO)
# =========================================================
# PoC Q-FENG: COMPLETO. Todos os dados prontos para o paper.

---

## STATUS FINAL E5 — 3 PARQUETS COMPLETOS

outputs/e5_results/validation_results.parquet   — 6 cenários
outputs/e5_results/theta_efetivo_manaus.parquet — 6 competências
outputs/e5_results/llm_comparison.parquet       — 16 linhas (C4a + C4b)

### validation_results (6 cenários)
| Cenário        | theta°  | Regime          | Cybernetic Loss |
|----------------|---------|-----------------|-----------------|
| C2 Manaus      | 132,4°  | CIRCUIT_BREAKER | 1,181           |
| C3 Concentração| 134,7°  | CIRCUIT_BREAKER | 1,265           |
| C7 Obermeyer   | 133,7°  | CIRCUIT_BREAKER | 1,127           |
| T-CLT-01       | 134,1°  | CIRCUIT_BREAKER | 1,094           |
| T-CLT-02       | 127,8°  | CIRCUIT_BREAKER | 0,970           |
| T-CLT-03       | 5,6°    | STAC            | 0,050           |

### theta_efetivo_manaus (série temporal, beta=3,0)
| Competência | theta_t | theta_efetivo | Regime          |
|-------------|---------|---------------|-----------------|
| out/2020    | 23,5°   | 23,5°         | STAC            |
| nov/2020    | 47,2°   | 37,5°         | HITL            |
| dez/2020    | 88,7°   | 72,3°         | HITL            |
| jan/2021    | 138,4°  | 123,1°        | CIRCUIT_BREAKER |
| fev/2021    | 91,3°   | 111,6°        | HITL (memória)  |
| mar/2021    | 62,1°   | 97,6°         | HITL (memória)  |

### llm_comparison (C4a vs C4b — Qwen 2.5 14B)
theta médio C4a: 59,3° | theta médio C4b: 48,6°
reduction_delta médio: +10,7° (8/8 positivos)
Wilcoxon signed-rank: p=0,0078 (significativo p<0,01)
delta min/max: +0,5° / +20,0°

---

## PRÓXIMA SESSÃO — Figuras e tabelas para o paper

### FIGURA 1 — Distribuição theta por cenário (bar horizontal)
Dados: validation_results.parquet
Faixas: verde STAC [0-30°] / amarelo HITL [30-120°] / vermelho CB [120-180°]
Paleta colorblind-safe | 300 DPI | 7 pol largura | textos EN

### FIGURA 2 — Trajetória theta_efetivo Manaus (dual-axis)
Dados: theta_efetivo_manaus.parquet
Y esq: theta_t (tracejado) + theta_efetivo (sólido)
Y dir: score_pressao (pontilhado cinza)
Linha vertical jan/2021 | anotações HITL/CB

### FIGURA 3 — Delta theta C4a vs C4b (slope graph ou paired dots)
Dados: llm_comparison.parquet
Cada ponto = 1 query | linha conectando C4a→C4b
Anotação: Wilcoxon p=0,0078

### FIGURA 4 — Efeito de memória markoviana
Área sombreada entre theta_t e theta_efetivo = memória normativa
Destaque: fev/mar-2021 (theta_t cai, theta_efetivo persiste)

### TABELAS LaTeX
T1: Corpus normativo (103 sovereign, 12 elastic, 18 constraints)
T2: Resultados E5 por cenário (tabela central do paper)
T3: Trajetória theta_efetivo Manaus
T4: C4a vs C4b por query

---

## CLAIM REVISADO PARA O PAPER (C4)

"Injection of SOVEREIGN predicates into the LLM system prompt reduces
ontological friction θ across all tested queries (Δθ_mean = −10.7°,
8/8 positive deltas, Wilcoxon signed-rank p=0.0078), even when the
base LLM already recommends normatively correct actions — validating
that Q-FENG strengthens normative grounding beyond error correction.
The largest reductions occur in ambiguous scenarios (Q3: Δθ=20°),
where normative uncertainty is highest."

---

## NOTAS PARA O PAPER

1. beta=3,0 calibrado empiricamente (série Manaus)
   Declarar na metodologia: alpha(t) = sigmoid(3.0 * delta_pressao(t))

2. Floats Clingo: usar inteiros (percentual)
   Declarar: hospital_occupancy_rate_pct(int) em vez de float

3. Cybernetic Loss C3 > C2: concentração crônica > crise pontual
   Comentar na seção de resultados

4. Separação bimodal theta: STAC=5,6° vs CB=127-134° (gap ~120°)
   Resultado mais forte para revisores de CS

5. Memória markoviana: theta_efetivo persiste em HITL fev-mar/2021
   mesmo com theta_t caindo — clinicamente correto (crise não termina abruptamente)
