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
