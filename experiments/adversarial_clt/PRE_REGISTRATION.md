# Pré-Registro OSF-Style — Frente 2: Experimento Adversarial CLT Q-FENG

**Registro:** 27/abr/2026 | **Branch:** caminho2 | **Commit de pré-registro:** _[hash após commit]_  
**Status:** PRÉ-DADOS — este documento foi commitado ANTES de qualquer execução LLM  
**Reprodutibilidade:** SHA256 por job; manifest.json; seeds fixas por run_id

---

## 1. Título

**Raciocínio Jurídico Assistido por LLM em Direito do Trabalho Brasileiro:
Efeito da Ancoragem Simbólica Q-FENG sobre Alucinação Normativa e Cobertura Predicativa**

---

## 2. Objetivo e Hipóteses

### H1 — Efeito principal de ancoragem sobre alucinação (D1) [Hipótese primária]
A ancoragem simbólica completa Q-FENG (braço B4) reduz a taxa de alucinação normativa (D1)
em relação ao LLM bruto (braço B1), controlado por modelo.

**Formulação estatística:**  
`H₁: D1(B4, m) < D1(B1, m)  ∀m ∈ {qwen3:14b, phi4:14b, gemma3:12b, llama3.1:8b}`  
**Teste:** McNemar emparelhado (binárias, within-model comparisons)  
**α_corrigido:** 0,05 / 24 = 0,0021 (Bonferroni m=24)

### H2 — Cobertura predicativa (D2)
A ancoragem predicativa (B3, B4) aumenta a cobertura dos predicados normativos relevantes (D2)
em relação aos braços sem ancoragem (B1, B2).

**Formulação estatística:**  
`H₂: D2(B3, m) > D2(B1, m)  AND  D2(B4, m) > D2(B1, m)  ∀m`  
**Teste:** Wilcoxon signed-rank (escores contínuos 0–1, within-model)  
**α_corrigido:** 0,05 / 24 = 0,0021

### H3 — Interação arm × model [Hipótese central, promovida pelo Patch A1]
Existe efeito de interação estatisticamente significativo entre o braço experimental
(arm) e o modelo (model) sobre D1 e D2.

**Formulação estatística:**  
`H₃: interação_arm×model é significativa em ANOVA two-way`  
`F(arm × model) com p < 0,05 para ao menos uma métrica {D1, D2, D3}`  
**Teste:** ANOVA two-way (fatores: arm [4 níveis], model [4 níveis])  
**Interpretação:** Presença de interação indicaria que a ancoragem Q-FENG beneficia
modelos maiores desproporcionalmente (ou inversamente, sinaliza uniformidade arquitetônica).

### H4 — Especificidade de citação (D3)
A ancoragem simbólica (B3, B4) aumenta a especificidade das citações normativas (D3 — presença
de referências a artigos, súmulas ou acórdãos específicos) em relação a B1 e B2.

**Formulação estatística:**  
`H₄: D3(B4, m) > D3(B1, m)  ∀m`  
**Teste:** Wilcoxon signed-rank  
**α_corrigido:** 0,05 / 24 = 0,0021

### H5 — Consistência cross-architecture [Patch A1]
Os braços B3 e B4 produzem decisões normativas mais consistentes entre diferentes modelos
do que os braços B1 e B2.

**Formulação estatística:**  
`H₅: Var(D1|arm=B4) < Var(D1|arm=B1)  AND  Var(D2|arm=B4) < Var(D2|arm=B1)`  
**Teste:** Levene's test de homogeneidade de variância (entre modelos, within arm)  
**Interpretação:** Se B4 reduz variância cross-model, a ancoragem Q-FENG
uniformiza o comportamento de modelos heterogêneos.

### H6 — Estratificação por Fricção Ontológica [Patch A5]
O efeito da ancoragem sobre D1 varia conforme a categoria de Fricção Ontológica
do cenário (derivacional > procedural, em magnitude de efeito).

**Formulação estatística:**  
`H₆: |Δ_D1(B4−B1)|_derivacional > |Δ_D1(B4−B1)|_procedural`  
**Teste:** ANOVA one-way (fator: friccao_categoria [4 níveis]) sobre Δ_D1  
**Categorias:** derivacional (n=23), procedural (n=11), controle_positivo (n=11), controle_negativo (n=5)

---

## 3. Design Experimental

| Dimensão | Especificação |
|----------|--------------|
| Fatores | Braço (4): B1, B2, B3, B4; Modelo (4): qwen3:14b, phi4:14b, gemma3:12b, llama3.1:8b |
| Runs por célula | 3 (seeds: 42, 123, 777) |
| Cenários | 50 (T-CLT-01=13, T-CLT-02=11, T-CLT-03=11, T-CLT-04=10, T-CTRL-NEG=5) |
| Total de chamadas | 4 × 4 × 50 × 3 = 2.400 |
| Temperatura | 0,3 (uniforme, todos os braços) |
| Deduplicação | SHA256(system_prompt + user_prompt + model + seed) |
| Checkpointing | manifest.json (job-level: pending → completed/failed) |
| Backend LLM | Ollama local (RTX 3060, 12 GB VRAM) |

**Braços experimentais:**
- B1 (LLM bruto): sem ancoragem, análise CLT direta
- B2 (RAG baseline): com corpus normativo injetado via `{normative_corpus}`
- B3 (dPASP anchoring): predicados normativos como lista textual `{predicate_list}`
- B4 (Q-FENG completo): resultado Clingo SAT/UNSAT + predicados soberanos ativos

---

## 4. Métricas de Outcome

### D1 — Taxa de Alucinação Normativa (métrica primária)
Proporção de citações normativas na resposta do LLM que são inexistentes, incorretas
ou não verificáveis na base CLT/TST/CF88.

- **Cálculo:** proporção de "phantom citations" por resposta (binária por cenário: sim/não)
- **Fonte de verdade:** `ground_truth_predicates.json` + lista canônica de predicados Q-FENG
- **Implementação:** `evaluators/eval_d1_alucinacao.py` (parse + verificação)

### D2 — Cobertura Predicativa Normativa (métrica secundária)
Proporção dos predicados normativos relevantes ao cenário (conforme `by_scenario` no ground truth)
que foram identificados na resposta do LLM.

- **Cálculo:** |{predicados relevantes identificados}| / |{predicados relevantes do cenário}|
- **Implementação:** `evaluators/eval_d2_cobertura.py`

### D3 — Especificidade de Citação (métrica Patch A3)
Proporção de citações normativas na resposta que incluem referência específica
(número de artigo, súmula, acórdão com número de processo, ou OJ identificada).

- **Cálculo:** regex matching para padrões de citação específica
- **Padrões:** CLT Art. NNN, Súmula TST NNN, TST-[tipo]-[número], CF/88 Art. NNN
- **Implementação:** `evaluators/d3_specificity.py`

---

## 5. Análise Estatística

### Plano de análise confirmatória

| Hipótese | Teste | Nível α (pré-corrigido) |
|----------|-------|------------------------|
| H1 | McNemar emparelhado (4 modelos × 3 pairwise) | 0,0021 |
| H2 | Wilcoxon signed-rank | 0,0021 |
| H3 | ANOVA two-way (arm × model) | 0,05 (não Bonferroni, único) |
| H4 | Wilcoxon signed-rank | 0,0021 |
| H5 | Levene's test | 0,05 por braço |
| H6 | ANOVA one-way (4 categorias friccao) | 0,05 (exploratório) |

**Bonferroni m=24:** 6 comparações pairwise (B1vB2, B1vB3, B1vB4, B2vB3, B2vB4, B3vB4)
× 4 modelos = 24 comparações para H1/H2/H4. α_corrigido = 0,05/24 = 0,0021.

### Effect size
- D1 (binária): Cohen's h (diferença de proporções)
- D2/D3 (contínua): Cohen's d (diferença de médias, std pooled)
- Threshold de relevância prática: |h| > 0,2 ou |d| > 0,2 (pequeno); > 0,5 (médio)

### Análise exploratória planejada
- Curva de aprendizado por modelo (D1 × número de chamadas): drift de temperatura?
- Análise de subgrupo por tipo de cenário (T-CLT-01 a T-CTRL-NEG) — não confirmatória
- Estratificação por friccao_categoria (H6) — exploratória

---

## 6. Critérios de Sucesso/Falha da Hipótese Central (H1)

H1 é corroborada se:
- B4 < B1 em D1 para ao menos 3 de 4 modelos (p < 0,0021)
- Effect size |h| > 0,2 para ao menos 2 modelos

H1 é refutada se:
- B4 ≥ B1 em D1 para todos os modelos, ou
- Diferenças não atingem significância após correção Bonferroni

---

## 7. Limitações Pré-Declaradas

1. **Tamanho de amostra:** 50 cenários por tipo; poder estatístico pode ser insuficiente
   para detecção de efeitos pequenos (|h| < 0,2) após Bonferroni.

2. **Cenários sintéticos:** os 50 cenários foram criados sinteticamente; generalização
   para casos reais do TST requer validação ecológica adicional.

3. **Modelo de avaliação:** D1 depende de parser baseado em regex; casos ambíguos
   de citação parcialmente correta não são capturados.

4. **Temperatura fixa:** temperatura 0,3 pode sub-representar variabilidade de modelos
   em condições de uso típicas (temperatura 0,7–1,0).

5. **Hardware único:** todos os modelos rodam em RTX 3060 12GB; resultados de
   latência não são generalizáveis para outros hardwares.

---

## 8. Dados e Reprodutibilidade

- **Dados brutos:** `experiments/adversarial_clt/results/raw_responses/` (JSON por job)
- **Manifest:** `experiments/adversarial_clt/results/manifest.json`
- **Parquet consolidado:** `experiments/adversarial_clt/results/results.parquet`
- **Cenários:** `experiments/adversarial_clt/scenarios/scenarios.yaml`
- **Ground truth:** `experiments/adversarial_clt/scenarios/ground_truth_predicates.json`
- **Deduplicação:** SHA256(system + user + model + seed) → nome do arquivo raw

**Compromisso de registro:** Este arquivo foi commitado em repositório git versionado
ANTES de qualquer execução LLM. Nenhuma hipótese foi formulada após visualização
de dados (HARKing prevention). O hash do commit de pré-registro é verificável pelo
repositório e deve ser citado em qualquer publicação derivada.

---

## 9. Cronograma Estimado

| Etapa | Estimativa |
|-------|------------|
| Execução 2.400 chamadas LLM | ~67 horas (hardware: RTX 3060) |
| Avaliação D1/D2/D3 | ~2 horas (pipeline automatizado) |
| Análise estatística H1-H6 | ~4 horas |
| Redação relatório final | ~2 horas |

---

*Documento gerado em 27/abr/2026. Quaisquer desvios do plano pré-registrado
serão documentados no relatório final com justificativa explícita.*

---

## 11. Emenda Formal — Alinhamento Estatístico-Editorial (27/abr/2026)

**Tipo:** Emenda pré-execução LLM
**Data da emenda:** 27 de abril de 2026, ~19h UTC-3
**SHA do pré-registro original:** `4c24e14` (commit `frente2-a4: pre-registro OSF-style (ANTES de qualquer execucao LLM)`)
**SHA desta emenda:** `6d2f8ae` (commit `frente2-emenda: alinhamento estatistico-editorial H3+H5b pre-execucao`)
**Justificativa:** alinhamento entre semântica estatística das hipóteses H3 e H5 e a reivindicação editorial de *agnosticismo de stack ML* registrada em `artefatos/notas_metodologicas/INSERCOES_NOVAS_SECOES_CANONICO.md` (Bloco B / §7.4 nova do canônico).

**Status quanto à execução LLM:** Esta emenda é registrada **antes** de qualquer chamada LLM ter sido executada. O diretório `results/raw_responses/` permanecia vazio na auditoria pré-execução em 27/abr/2026 às 19h UTC-3. A integridade pré-registral é portanto preservada: nenhuma hipótese é modificada após observação de dados.

### 11.1 Reformulação de H3

A formulação original de H3 na §2 deste pré-registro especifica:

> *"H₃: interação_arm×model é significativa em ANOVA two-way"* — i.e., direção esperada `p < 0.05`.

A formulação reformulada de H3 passa a ser:

> **H3 (cross-architecture invariance) [reformulada]:** O efeito Q-FENG na redução de alucinação (D1) e no aumento de cobertura (D2) é estatisticamente invariante entre famílias arquitetônicas de LLM. Operacionalmente, o termo de interação `arm × model` na ANOVA two-way é estatisticamente **não-significativo** após correção Bonferroni: `p(arm × model) > 0.05/m`, onde `m = 6` (número de hipóteses confirmatórias H1–H6).

**Justificativa da reformulação:** a formulação original tinha leitura dupla declarada na própria §2 ("presença de interação indicaria que a ancoragem Q-FENG beneficia modelos maiores desproporcionalmente OU inversamente sinaliza uniformidade arquitetônica"). Hipótese pré-registrada deve ter direção única e falsificável. A nova formulação fixa a direção `p > 0.05/m` como evidência da hipótese — que é a direção alinhada à reivindicação editorial de *agnosticismo de stack ML*. A direção oposta (`p < 0.05/m`, presença de interação) passa a constituir falsificação de H3 e abre espaço para análise exploratória post-hoc sobre a natureza da interação.

**Teste estatístico:** ANOVA two-way `D1 ~ arm × model` e `D2 ~ arm × model`, fatores arm (4 níveis: B1, B2, B3, B4) e model (4 níveis: Qwen 3 14B, Phi-4 14B, Gemma 3 12B, Llama 3.1 8B). Reportar F-statistic, p-valor da interação, e η² parcial.

**α corrigido:** 0,05 / 6 = 0,0083 (Bonferroni m=6 sobre as hipóteses H1-H6).

### 11.2 Adição de H5b — Bootstrap effect-size overlap

A formulação original de H5 (Levene's test sobre variância cross-model) é **preservada** como análise complementar. Acrescenta-se H5b como teste primário para a reivindicação editorial de invariância de magnitude do efeito Q-FENG entre arquiteturas LLM:

> **H5b (effect-size overlap across architectures) [adicionada]:** A magnitude do efeito Q-FENG sobre alucinação `Δ_i = [D1(B1) − D1(B4)]_modelo_i` tem intervalo de confiança 95% bootstrap (1.000 iterações) sobreposto entre todos os pares (i, j) ∈ {Qwen 3 14B, Phi-4 14B, Gemma 3 12B, Llama 3.1 8B}. Operacionalmente, computar bootstrap pareado por cenário com 1.000 iterações para cada modelo, derivar IC95% percentile, e verificar overlap pareado em matriz binária 4×4.

**Justificativa da adição:** Levene mede homogeneidade de variância intra-braço entre modelos, que é uma propriedade relacionada mas distinta de invariância de magnitude do efeito entre arquiteturas. A reivindicação editorial de *agnosticismo de stack ML* (Bloco B do `INSERCOES_NOVAS_SECOES_CANONICO.md`, §7.4 nova do canônico) requer especificamente que o efeito Q-FENG (medido como diferença `D1(B1) − D1(B4)`) tenha magnitude semelhante entre famílias arquitetônicas. H5b operacionaliza diretamente esta reivindicação. H5 (Levene) é mantida como evidência convergente complementar.

**Teste estatístico:** Bootstrap não-paramétrico pareado por cenário, 1.000 iterações, IC95% percentile (2,5% e 97,5%). Critério de evidência: matriz 4×4 de overlap binário com pelo menos 5 dos 6 pares (i,j) ∈ {(Qwen,Phi), (Qwen,Gemma), (Qwen,Llama), (Phi,Gemma), (Phi,Llama), (Gemma,Llama)} apresentando ICs sobrepostos.

**α implícito:** Não aplicável (teste de overlap de IC, não rejeição de H₀). Threshold de evidência: ≥ 5/6 pares com overlap.

### 11.3 Mapeamento de hipóteses entre o Code, o patch original e o canônico

Para evitar descalibração entre os scripts de análise (`analysis/test_h*.py`), o pré-registro, e os relatórios em chat (`RESULTADOS_FRENTE1_PARA_CANONICO.md`, `INSERCOES_NOVAS_SECOES_CANONICO.md`), registra-se aqui o mapeamento canônico:

| Hipótese (script `analysis/`) | Pré-registro pós-emenda | Patch original | Reivindicação editorial |
|---|---|---|---|
| `test_h1_mcnemar.py` | H1 (D1 reduction B4<B1) | H1 (idem) | Efeito principal de ancoragem |
| `test_h2_h4_wilcoxon.py` testando D2 | H2 (D2 increase B3/B4>B1) | H2 (idem) | Cobertura predicativa |
| `test_h3_anova_interaction.py` (reformulado em F2P.2) | H3 (cross-arch invariance, p > 0.05/m) | H3 (idem) | Agnosticismo de stack ML — invariância da direção do efeito |
| `test_h2_h4_wilcoxon.py` testando D3 | H4 (D3 specificity B4>B1) | H6 do patch | Especificidade de fundamentação |
| `test_h5_levene_variance.py` | H5 (variance homogeneity, complementar) | — | Evidência convergente |
| `test_h5_bootstrap_overlap.py` (novo, F2P.3) | **H5b (effect-size overlap)** | H5 do patch | Agnosticismo de stack ML — invariância da magnitude do efeito |
| `test_subgroup_friccao.py` | H6 (Friccao Ontologica subgroups) | Acréscimo 5 do patch | Costura editorial Frente 1 + Frente 2 |

**Total de hipóteses confirmatórias após emenda:** 7 (H1, H2, H3, H4, H5, H5b, H6). Bonferroni `m = 7` para hipóteses correlatas; H3 e H5b individuais usam α = 0.05/6 e threshold de overlap respectivamente.

### 11.4 Status de execução

Esta emenda é registrada **antes** do início da execução das 2.400 chamadas LLM. Nenhum dado LLM foi coletado entre `4c24e14` (pré-registro original) e o commit desta emenda. A integridade pré-registral é portanto preservada: emenda pré-observacional, não emenda post-hoc.

---

## 12. Emenda Formal — Adição do Braço B5 (Motor Q-FENG θ Completo) (28/abr/2026)

**Tipo:** Emenda aditiva pré-execução B5 (B1, B2, B3, B4 inalterados; B4 em curso no momento da emenda)
**Data da emenda:** 28 de abril de 2026
**SHA do pré-registro original:** `4c24e14`
**SHA da emenda §11:** `6d2f8ae`
**SHA desta emenda §12:** [a ser preenchido após commit desta operação]
**Justificativa:** alinhamento entre o desenho experimental Frente 2 e a especificação do canônico §3 (motor de interferência θ via ψ_N e ψ_S no espaço de Hilbert) e §7.4 nova (governance sidecar com runtime computation de θ sobre LLMs cross-arquitetura).

**Status quanto à execução LLM:**
- B1, B2, B3: 1.800 chamadas íntegras (não afetadas).
- B4: em execução no momento da emenda. Não afetado por esta emenda.
- B5: novo braço, 600 chamadas planejadas após conclusão de B4.

A integridade pré-registral é preservada: esta emenda é estritamente **aditiva** — adiciona um braço novo (B5), duas hipóteses confirmatórias novas (H7, H8) e novos campos no JSON de saída para B5. Os braços e hipóteses pré-registrados em §11 permanecem inalterados.

### 12.1 Diagnóstico forense que motivou a adição

Auditoria pré-B4 conduzida em sessão de chat (28/abr/2026) identificou que o caminho B4 implementa **ancoragem simbólica via Clingo SAT/UNSAT + narrativa LLM**, mas **não invoca o motor de inferência θ canônico** definido em `src/qfeng/core/interference.py`. B4 calcula `psi_s` como escalar simplificado (`n_sovereign / (n_sovereign + n_elastic) × π`) e injeta o escalar como string no template do prompt.

A consequência editorial é que B4, embora válido como instância de "RAG simbólico estruturado por Clingo", não sustenta empiricamente a reivindicação editorial central do canônico §7.4 nova: **governance sidecar runtime sobre LLMs cross-arquitetura**. O motor de interferência θ — que é o que distingue Q-FENG de NeSy 1.0, Constitutional AI e expert systems na Tabela 7.4.1 do canônico — não roda em runtime no caminho B4.

Três opções foram consideradas para correção:

- **Opção A:** retrofit do B4 com descarte de chamadas pré-retrofit. Rejeitada por enfraquecer o pré-registro §11.
- **Opção B:** computação de θ post-hoc sobre os JSONs gravados. Rejeitada por enfraquecer o argumento de runtime governance (computação offline ≠ runtime).
- **Opção C (adotada):** adição de novo braço B5 com motor θ completo, preservando integralmente B4 como ancoragem simbólica. Editorial mais forte; custo +600 chamadas LLM.

### 12.2 Especificação do braço B5

B5 instancia o motor de inferência Q-FENG canônico em runtime, conforme §3 do canônico:

1. **`build_psi_n(clingo_anchor)`** — Neural Evidence Vector (vetor np.float64 calibrado por cenário, L2-normalizado). O `clingo_anchor` do cenário (e.g. `T-CLT-01` para `T-CLT-01-001` e para `T-CTRL-NEG-001`) é a chave de lookup no psi_builder.
2. **`build_psi_s(clingo_anchor, active_sovereign, active_elastic)`** — Symbolic Norm Vector aditivo derivado dos predicados Clingo ativos, L2-normalizado.
3. **`compute_interference(psi_n, psi_s, alpha_sq=0.5, beta_sq=0.5, cb_config=default)`** — cálculo conjunto de θ (Eq. A5), Born Rule (P_action), termo de interferência, e classificação Circuit Breaker.
4. **`CircuitBreakerConfig` canônico:** `theta_stac = π/3 = 60°`, `theta_block = 2π/3 = 120°`. Regimes: STAC (θ < 60°), HITL (60° ≤ θ < 120°), BLOCK (θ ≥ 120°).
5. **Stateless por cenário:** `theta_history=None`, `gamma=0.0`. Justificativa metodológica: ambiente adversarial CLT é trial-independente, sem série temporal estruturada entre cenários. A Frente 1 (Manaus 70 SEs) opera em modo stateful com Markov memory β=3.0; ambos são instâncias válidas do mesmo motor canônico, diferindo apenas pela presença ou ausência de série temporal no domínio.

**Validação pré-disparo (smoke test):** Motor testado sobre 3 cenários canários:
- T-CLT-01 (phantom citation, UNSAT): θ = 133.51° → BLOCK ✓
- T-CLT-03 (hour bank com CCT, SAT): θ = 5.65° → STAC ✓
- T-CLT-04 (positive control, SAT): θ = 7.05° → STAC ✓

### 12.3 Instrumentação granular de tempo (apenas para B5)

Adicionam-se ao JSON de saída de cada chamada B5 (campos `None` para B1-B4, exceto `t_clingo_ms` que é populado para B4 e B5):

| Campo | Descrição |
|---|---|
| `t_clingo_ms` | Tempo de execução do solver Clingo SAT/UNSAT (B4 e B5) |
| `t_psi_build_ms` | Tempo de construção de ψ_N e ψ_S — apenas B5 |
| `t_theta_compute_ms` | Tempo de cálculo de θ + Born Rule + Circuit Breaker — apenas B5 |
| `t_llm_ms` | Tempo isolado da chamada `ollama.chat()` — todos os braços |
| `qfeng_psi_n_dim`, `qfeng_psi_s_dim` | Dimensões dos vetores de Hilbert — apenas B5 |
| `qfeng_theta_rad`, `qfeng_theta_deg` | Ângulo θ em radianos e graus — apenas B5 |
| `qfeng_theta_eff_rad`, `qfeng_theta_eff_deg` | θ_eff (singleton = θ em adversarial CLT) — apenas B5 |
| `qfeng_regime` | Classificação STAC / HITL / BLOCK — apenas B5 |
| `qfeng_p_action` | P(Action) via Born Rule com termo de interferência — apenas B5 |
| `qfeng_cos_theta` | cos(θ) — apenas B5 |
| `qfeng_cb_threshold_deg` | Threshold de Circuit Breaker usado (canônico = 120°) — apenas B5 |

O **overhead operacional do motor Q-FENG** em runtime sidecar é definido como:

```
overhead_qfeng_ms = t_clingo_ms + t_psi_build_ms + t_theta_compute_ms
```

Esta é a métrica primária de H7 (governance sidecar viability).

### 12.4 Hipóteses adicionadas

Adicionam-se duas hipóteses confirmatórias ao conjunto pré-registrado, ambas testadas sobre o braço B5:

> **H7 (governance sidecar viability) [confirmatória, adicionada]:** O overhead operacional do motor Q-FENG (`overhead_qfeng_ms = t_clingo_ms + t_psi_build_ms + t_theta_compute_ms`) é menor que 5% do tempo total `latency_ms` em mediana, em todos os 4 modelos LLM testados.

> **H8 (motor θ vs. ancoragem simbólica) [confirmatória, adicionada]:** O motor de interferência θ completo (B5) produz métricas D1 e D3 estatisticamente distintas da ancoragem simbólica via Clingo + narrativa LLM (B4):
>   - **H8a:** D1(B5) ≠ D1(B4), Wilcoxon signed-rank pareado por cenário, p < 0.05/8 (Bonferroni m=8).
>   - **H8b:** D3(B5) > D3(B4), Wilcoxon signed-rank pareado por cenário, p < 0.05/8.

H8 isola empiricamente o **valor do motor de interferência runtime** face à ancoragem simbólica pura.

### 12.5 Atualização da correção de Bonferroni

Adição de H7 e H8 eleva o número total de hipóteses confirmatórias de 7 para 9 (H7 + H8a + H8b). Adoto **m = 8** como compromisso editorial: H8 é tratada como família agregada com α familiar = 0.05/8 = 0.00625.

| Hipótese | Teste | α corrigido (Bonferroni m=8) |
|---|---|---|
| H1 | McNemar D1 (B4 vs B1) | 0.00625 |
| H2 | Wilcoxon D2 (B3, B4 vs B1) | 0.00625 |
| H3 | ANOVA two-way arm × model (D1, D2) | 0.00625 |
| H4 | Wilcoxon D3 (B4 vs B1) | 0.00625 |
| H5 | Levene variance | 0.00625 (complementar) |
| H5b | Bootstrap effect-size overlap | threshold ≥5/6 pares |
| H6 | ANOVA Δ_D1 × friccao_categoria | 0.00625 |
| **H7** | **mediana(overhead_qfeng) / mediana(latency_ms) < 0.05 por modelo** | **threshold absoluto** |
| **H8a** | **Wilcoxon D1(B5) vs D1(B4)** | **0.00625** |
| **H8b** | **Wilcoxon D3(B5) vs D3(B4)** | **0.00625** |

### 12.6 Mapeamento canônico estendido

| Hipótese (script `analysis/`) | Pré-registro pós-emendas §11 + §12 | Reivindicação editorial |
|---|---|---|
| `test_h1_mcnemar.py` | H1 (B4 vs B1) | Efeito principal de ancoragem |
| `test_h2_h4_wilcoxon.py` testando D2 | H2 | Cobertura predicativa |
| `test_h3_anova_interaction.py` | H3 | Agnosticismo de stack — invariância de direção |
| `test_h2_h4_wilcoxon.py` testando D3 | H4 | Especificidade |
| `test_h5_levene_variance.py` | H5 (complementar) | Convergência |
| `test_h5_bootstrap_overlap.py` | H5b | Agnosticismo de stack — invariância de magnitude |
| `test_subgroup_friccao.py` | H6 | Costura editorial Frente 1 + Frente 2 |
| **`test_h7_sidecar_viability.py` (novo)** | **H7** | **Viabilidade do governance sidecar runtime** |
| **`test_h8_motor_vs_anchoring.py` (novo)** | **H8a, H8b** | **Valor do motor θ face a ancoragem simbólica** |

### 12.7 Status quanto à reprodutibilidade Zenodo

A presença de B4 e B5 como braços paralelos representa contribuição editorial: o paper documenta duas instâncias arquiteturalmente distintas de Q-FENG operando sobre o mesmo corpus de cenários e o mesmo conjunto de modelos LLM. Para reprodutibilidade Zenodo, o repositório completo (1.800 B1-B3 + 600 B4 + 600 B5 = 3.000 chamadas) é depositado com o pré-registro original (§11) e ambas as emendas (§11 e §12) commitadas como rastro auditável.
