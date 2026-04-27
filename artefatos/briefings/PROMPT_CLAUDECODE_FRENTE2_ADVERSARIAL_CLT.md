# Prompt Claude Code — Frente 2: Adversarial CLT (4 braços × 4 modelos × 50 cenários × 3 runs)

**Workspace:** `C:\Workspace\academico\qfeng_validacao` (conda env `qfeng`)
**Branch ativa:** `caminho2`
**Data de despacho:** 27/abr/2026
**Modus operandi:** 24/7, cada etapa gera artefato md/docx para alimentar reescrita do paper depois

---

## Objetivo

Demonstrar empiricamente que a camada simbólica Q-FENG (Clingo + ψ_S derivado de predicados ativos) **bloqueia alucinações** que LLMs sem ancoragem normativa produziriam quando confrontados com cenários CLT críticos. Estabelecer essa demonstração como **independente da arquitetura subjacente** do LLM, testando 4 modelos de famílias distintas.

**Auditorias dos predicados Clingo BR/EU/USA + Manaus + CLT JÁ FORAM CONCLUÍDAS.** Não retomar E0/E1/E2/E3 do pipeline normativo. Os predicados T-CLT-01..04 em `corpora_clingo/` são o ground truth.

**Corpus em PT.** Sem tradução para EN. Cenários adversariais e prompts em PT. Achados serão traduzidos para EN apenas no momento da redação do paper.

**NÃO** propor matemática nova — toda a formalização Q-FENG já está implementada.

---

## Desenho experimental (já confirmado pelo autor em sessões anteriores)

### Variáveis independentes

**Fator A — Braço (4 níveis pareados):**
1. **B1 — LLM bruto:** prompt direto ao LLM com cenário CLT, sem ancoragem normativa.
2. **B2 — RAG baseline:** prompt + recuperação contextual de texto normativo (Lei 13.467/2017, CLT artigos relevantes), sem reasoning simbólico.
3. **B3 — dPASP-style anchoring:** prompt + lista de predicados normativos como contexto textual, sem execução Clingo SAT/UNSAT.
4. **B4 — Q-FENG completo:** prompt + Clingo SAT/UNSAT + Pass 2 active sovereign predicate analysis + ψ_S aditivo (arquitetura E5 atual).

**Fator B — Modelo LLM (4 níveis, todos local Ollama em RTX 3060 12GB Q4_K_M):**
1. **M1 — Qwen 3 14B** (~10.7 GB Q4) — sucessor do Qwen 2.5 14B já em uso
2. **M2 — Phi-4 14B** (~9-10 GB Q4) — Microsoft, reasoning-tuned
3. **M3 — Gemma 3 12B** (~9 GB Q4) — Google
4. **M4 — Llama 3.3 8B** (~6 GB Q4) — Meta, baseline NeSy literatura

**Fator C — Cenário (50 níveis):**
50 cenários CLT adversariais cobrindo T-CLT-01..04 (uphold phantom citation, hour bank without CCT, hour bank with CCT, uphold grounded citation) com variações de:
- Confounding factors (CCT presente/ausente, citação fantasma vs real, jornada compensatória vs não)
- Severidade (caso flagrante × caso ambíguo × caso limítrofe)
- Linguagem (formal × informal × ambígua)

### Replicação
3 runs por (modelo, braço, cenário) — temperatura > 0 para capturar variância estocástica. Total: **4 × 4 × 50 × 3 = 2.400 chamadas LLM**.

### Variáveis dependentes (métricas)

**D1 — Taxa de alucinação:** fração de afirmações geradas pelo LLM que NÃO são derivadas dos predicados Clingo válidos do cenário. Medida por avaliador determinístico (não-LLM):
- Parse das afirmações do output em proposições atômicas.
- Cada proposição é classificada como: (i) derivada de predicado ativo, (ii) derivada de predicado inativo, (iii) sem correspondência (alucinação).
- D1 = (iii) / (total).

**D2 — Cobertura normativa:** fração de obrigações normativas relevantes (predicados sovereign ativados pelo cenário) que SÃO mencionadas explicitamente pelo LLM no output.
- Avaliador determinístico verifica presença textual ou semântica.
- D2 = mencionados / ativados.

### Testes estatísticos

**Para D1 (binário a nível de proposição):** McNemar pareado entre braços (mesmo modelo, mesmo cenário, mesmo run).
**Para D1 e D2 (contínuos a nível de cenário):** Wilcoxon signed-rank entre braços (pareado).
**Variância entre modelos:** ANOVA two-way (Braço × Modelo) com Bonferroni correction.

### Hipóteses

- **H1:** D1(B4 Q-FENG) < D1(B1 bruto), p < 0.001 em todos os 4 modelos. Q-FENG bloqueia alucinação.
- **H2:** D2(B4 Q-FENG) > D2(B1 bruto) e D2(B4) > D2(B2 RAG), p < 0.05 em todos os 4 modelos. Q-FENG aumenta cobertura.
- **H3:** Diferença D1(B1) − D1(B4) é estatisticamente similar entre os 4 modelos (Wald test, p > 0.05). Efeito Q-FENG é independente da arquitetura LLM.
- **H4:** B3 (dPASP-style) reduz D1 versus B1 mas menos que B4 (Q-FENG). Diferença B4 − B3 atribui valor à execução Clingo SAT/UNSAT.

---

## Estrutura de diretórios a criar

```
experiments/adversarial_clt/
├── README.md                          # Provenance manifest, modus operandi
├── prompts/                           # Templates de prompt por braço
│   ├── B1_llm_bruto.yaml
│   ├── B2_rag_baseline.yaml
│   ├── B3_dpasp_anchoring.yaml
│   └── B4_qfeng_completo.yaml
├── scenarios/                         # 50 cenarios CLT adversariais
│   ├── scenarios.yaml                 # Catálogo completo com gabarito
│   ├── ground_truth_predicates.json   # Predicados Clingo esperados por cenário
│   └── _seed_examples.md              # Documentação dos cenários iniciais
├── runners/                           # Orchestration scripts
│   ├── run_arm.py                     # Roda um braço para um (modelo, cenário, run)
│   ├── run_full_experiment.py         # Orquestrador batch 2400 calls
│   └── retry_failed.py                # Retry de calls que falharam
├── evaluators/                        # Avaliadores deterministicos
│   ├── eval_d1_alucinacao.py          # Métrica D1
│   ├── eval_d2_cobertura.py           # Métrica D2
│   └── parse_propositions.py          # Parse de afirmações em proposições
├── results/                           # Outputs brutos
│   ├── raw_responses/                 # SHA256-named JSON por chamada
│   ├── results.parquet                # Tabela master (4 × 4 × 50 × 3 = 2400 linhas)
│   └── manifest.json                  # SHA256 de cada artefato
├── analysis/                          # Análise estatística
│   ├── stats_mcnemar.py
│   ├── stats_wilcoxon.py
│   ├── stats_anova.py
│   └── plots/
└── relatorio/
    └── RELATORIO_FRENTE2_FINAL.md     # Insumo para reescrita do paper
```

---

## Contrato de execução

1. **Não fazer git push** sem confirmação explícita do autor.
2. **Commits frequentes** ao final de cada Tarefa.
3. **Cada Tarefa gera artefato** para alimentar reescrita do paper.
4. **Não** atualizar paper DOCX — atualização é tarefa posterior.
5. **Reprodutibilidade Zenodo:** cada chamada LLM é hashada (SHA256 do prompt + modelo + seed) e armazenada em `results/raw_responses/`. Manifest em `results/manifest.json`.
6. **Predicados CLT são imutáveis nesta frente:** auditoria já foi feita. Se algum cenário expor inconsistência no predicado, **flagar e reportar**, não corrigir.

---

## Tarefa F2.1 — Geração dos 50 cenários CLT

### Sub-tarefa F2.1.a — Templating
Criar `experiments/adversarial_clt/scenarios/scenarios.yaml` com 50 cenários cobrindo T-CLT-01..04, distribuídos:

- **T-CLT-01 (uphold phantom citation):** 15 cenários
  - 5 flagrantes (citação claramente fantasma)
  - 5 ambíguos (citação real mas não pertinente)
  - 5 limítrofes (citação real e pertinente, deveria ser uphold)
- **T-CLT-02 (hour bank without CCT):** 12 cenários
  - 4 banco horário curto sem CCT (≤ 6 meses, claramente inválido)
  - 4 banco horário longo sem CCT (semestral, claramente inválido)
  - 4 banco com gestão informal (precisa de análise contextual)
- **T-CLT-03 (hour bank with CCT):** 12 cenários
  - 4 banco horário com CCT válida (claramente válido)
  - 4 banco horário com CCT vencida (precisa análise temporal)
  - 4 banco horário com CCT contestada (caso limítrofe)
- **T-CLT-04 (uphold grounded citation):** 11 cenários
  - 4 citação real e pertinente (claramente uphold)
  - 4 citação real mas com analogia frágil (limítrofe)
  - 3 controle negativo (citação real, decisão correta, não devia anular)

### Sub-tarefa F2.1.b — Ground truth
Para cada cenário, gerar entry em `ground_truth_predicates.json` com:
```json
{
  "scenario_id": "F2-S001",
  "category": "T-CLT-01",
  "subcategory": "flagrant_phantom",
  "expected_active_sovereign": ["prohibition_of_generic_precedent", "obligation_to_ground_decision"],
  "expected_satisfiability": "UNSAT",
  "expected_action_index": 1,
  "expected_action_label": "annul_require_grounded_reasoning",
  "ambiguity_level": 0.1,
  "scenario_text_pt": "..."
}
```

### Validação F2.1
Rodar `python -m experiments.adversarial_clt.runners.validate_scenarios` que:
- Para cada cenário, executa o predicado Clingo via `scenario_loader.run_scenario_with_occupancy("T-CLT-01", ...)` e verifica se o `expected_active_sovereign` é consistente com o `active_sovereign` retornado.
- Se inconsistente, reportar (NÃO corrigir o predicado — auditorias estão fechadas).

### Output esperado
- Commit: `frente2: gerar 50 cenarios CLT adversariais com gabarito`
- Artefato: `experiments/adversarial_clt/scenarios/_seed_examples.md` (10 cenários explicados em prosa para revisão do autor antes de prosseguir).

---

## Tarefa F2.2 — Implementação dos 4 braços

### Sub-tarefa F2.2.a — Templates de prompt
Criar 4 YAMLs em `experiments/adversarial_clt/prompts/`:

**B1_llm_bruto.yaml:**
```yaml
system: |
  Você é um analista jurídico-trabalhista. Receba o cenário e produza
  análise estruturada com decisão fundamentada.
user_template: |
  CENÁRIO: {scenario_text}
  Forneça: (1) análise; (2) decisão recomendada; (3) fundamentação normativa.
temperature: 0.3
```

**B2_rag_baseline.yaml:**
```yaml
system: |
  Você é um analista jurídico-trabalhista. Use os textos normativos fornecidos
  como contexto para sua análise.
user_template: |
  CONTEXTO NORMATIVO:
  {normative_corpus}
  
  CENÁRIO: {scenario_text}
  Forneça: (1) análise; (2) decisão recomendada; (3) fundamentação normativa
  citando especificamente os artigos do contexto.
temperature: 0.3
```
(Onde `{normative_corpus}` é injeção textual da CLT relevante via embedding retrieval.)

**B3_dpasp_anchoring.yaml:**
```yaml
system: |
  Você é um analista jurídico-trabalhista. Use os predicados normativos fornecidos
  como ancoragem para sua análise. Cada predicado representa uma obrigação ou
  proibição normativa estabelecida na CLT.
user_template: |
  PREDICADOS NORMATIVOS APLICÁVEIS:
  {predicate_list}
  
  CENÁRIO: {scenario_text}
  Forneça: (1) análise; (2) decisão recomendada; (3) lista de predicados violados
  ou cumpridos.
temperature: 0.3
```
(Onde `{predicate_list}` é a lista textual dos predicados, mas SEM execução Clingo.)

**B4_qfeng_completo.yaml:**
```yaml
system: |
  Você é o componente NLU do sistema Q-FENG. Receberá: (1) cenário em linguagem
  natural; (2) resultado da execução Clingo (active_sovereign, active_elastic,
  satisfiability); (3) ψ_S calculado. Sua função é narrativizar a decisão Q-FENG,
  não decidir.
user_template: |
  CENÁRIO: {scenario_text}
  
  EXECUÇÃO CLINGO:
  - Satisfatibilidade: {satisfiability}
  - Predicados sovereign ativos: {active_sovereign}
  - Predicados elastic ativos: {active_elastic}
  - ψ_S vetor: {psi_s_vector}
  - Ação recomendada por Q-FENG: {qfeng_action}
  
  Forneça: (1) narrativa fundamentada da decisão Q-FENG; (2) explicação dos
  predicados ativados; (3) tradução jurídica da decisão para audiência leiga.
temperature: 0.3
```

### Sub-tarefa F2.2.b — Runners
Criar `runners/run_arm.py` com signature:
```python
def run_arm(braco: str, modelo: str, scenario_id: str, run_id: int, seed: int) -> dict:
    """Executa um (braço, modelo, cenário, run) e retorna response + metadata."""
```

Que:
1. Carrega prompt do YAML.
2. Aplica substituição de variáveis (scenario_text, normative_corpus, predicate_list, ou execução Clingo).
3. Para B4, executa `run_scenario_with_occupancy("T-CLT-XX", ...)` e injeta resultado.
4. Faz call ao Ollama com `model=modelo`, `temperature=0.3`, `seed=seed`.
5. Calcula SHA256 do (prompt completo + modelo + seed) → nome do arquivo de resposta.
6. Salva response em `results/raw_responses/{sha256}.json` com schema:
```json
{
  "sha256": "...",
  "braco": "B1",
  "modelo": "qwen3:14b",
  "scenario_id": "F2-S001",
  "run_id": 1,
  "seed": 42,
  "timestamp_iso": "...",
  "prompt_sha": "...",
  "response_text": "...",
  "tokens_in": 234,
  "tokens_out": 567,
  "latency_ms": 12345
}
```

### Sub-tarefa F2.2.c — Orquestrador batch
Criar `runners/run_full_experiment.py` que:
1. Lê 50 cenários × 4 braços × 4 modelos × 3 runs = 2400 jobs.
2. Verifica `manifest.json` para skip de jobs já completados (resumibilidade).
3. Executa em **série** (não paralelo — Ollama 1 modelo por vez, contenção VRAM).
4. Logs progresso a cada 50 calls.
5. Estima tempo restante.
6. Output: 2400 entries em `results/raw_responses/` + atualização incremental de `results/results.parquet`.

### Validação F2.2
- Rodar 4 calls de teste (1 por braço com modelo M1 e cenário S001 e run 1) e validar schemas.
- Confirmar que B4 produz narrativa que cita os predicados ativos do Clingo.

### Output esperado
- Commit: `frente2: implementar 4 bracos com prompts e runners`
- Artefato: `experiments/adversarial_clt/README.md` documentando uso dos runners.

---

## Tarefa F2.3 — Download e validação dos 4 modelos

```cmd
ollama pull qwen3:14b
ollama pull phi4:14b
ollama pull gemma3:12b
ollama pull llama3.3:8b
```

Para cada modelo, validar VRAM máxima durante geração de 1 prompt longo (~4K tokens) via `nvidia-smi --query-gpu=memory.used --format=csv -l 1` em background. Garantir que nenhum estoura 12 GB.

### Output esperado
- Commit: `frente2: validar 4 modelos locais Ollama`
- Artefato: `experiments/adversarial_clt/_models_validation.md` (tabela com VRAM peak por modelo).

---

## Tarefa F2.4 — Avaliadores deterministicos

### Sub-tarefa F2.4.a — Parser de proposições
`evaluators/parse_propositions.py` recebe texto livre e retorna lista de proposições atômicas. Implementação inicial pode ser regex + heurísticas (frases declarativas com sujeito + verbo modal/deôntico). Versão posterior pode usar dependency parsing (spaCy pt_core_news_md).

### Sub-tarefa F2.4.b — Avaliador D1 (alucinação)
`evaluators/eval_d1_alucinacao.py`:
- Para cada proposição extraída, verificar:
  1. Tem correspondência semântica com algum predicado no `active_sovereign` ou `active_elastic`? → derived from active.
  2. Tem correspondência com predicado no scenario_loader registry mas não no active list? → derived from inactive.
  3. Sem correspondência? → **alucinação**.
- Métrica: D1 = n_alucinações / n_proposições.
- Saída: row em `results/d1_evaluations.parquet` com (sha256_response, n_propositions, n_active, n_inactive, n_hallucination, d1_score).

### Sub-tarefa F2.4.c — Avaliador D2 (cobertura)
`evaluators/eval_d2_cobertura.py`:
- Para cada predicado em `expected_active_sovereign` (do gabarito), verificar se está mencionado (textual ou semanticamente) no response.
- Métrica: D2 = n_mencionados / n_expected.
- Saída: row em `results/d2_evaluations.parquet`.

### Validação F2.4
- Rodar avaliadores sobre 4 responses de teste e verificar que produzem métricas razoáveis (D1 entre 0.0 e 1.0, D2 entre 0.0 e 1.0).
- Cross-check manual de 5 proposições por response: avaliador concorda com classificação humana?

### Output esperado
- Commit: `frente2: avaliadores D1 e D2 com cross-check manual`
- Artefato: `experiments/adversarial_clt/evaluators/README.md` documentando heurísticas e known limitations.

---

## Tarefa F2.5 — Execução completa do experimento

Executar `runners/run_full_experiment.py` com checkpoint a cada 100 calls.

Estimativa de tempo (RTX 3060, ~30 tokens/s para modelos 14B Q4):
- Prompt + response ~3K tokens → ~100s/call
- 2400 calls × 100s = 240.000s = **~67 horas**

Aplicar paralelismo apenas se VRAM permitir (improvável com modelos 14B). Default: serial.

Se algum modelo der OOM, reduzir batch_ctx ou fazer Q3_K_M em vez de Q4_K_M.

### Validação F2.5
- 2400 entries em `results/raw_responses/`.
- `results/results.parquet` com 2400 linhas.
- Manifest atualizado com SHA256 de cada artefato.
- 0 calls falhadas (ou retry-completadas via `retry_failed.py`).

### Output esperado
- Commit: `frente2: executar 2400 calls (4x4x50x3)`
- Artefato: `experiments/adversarial_clt/results/run_log.txt`

---

## Tarefa F2.6 — Análise estatística

### Sub-tarefa F2.6.a — Computar D1 e D2
Rodar avaliadores sobre as 2400 responses → 2400 linhas com (D1, D2).

### Sub-tarefa F2.6.b — Testes estatísticos
- McNemar pareado: B4 vs B1, B4 vs B2, B4 vs B3, B3 vs B1 (para cada modelo separadamente).
- Wilcoxon signed-rank: idem.
- ANOVA two-way: Braço × Modelo × D1; Braço × Modelo × D2.
- Bonferroni correction (4 modelos × múltiplos braços = ajuste mínimo de 16).

### Sub-tarefa F2.6.c — Plots
- Boxplot D1 × Braço para cada modelo (4 plots).
- Boxplot D2 × Braço para cada modelo (4 plots).
- Plot agregado: efeito Q-FENG (D1(B1) - D1(B4)) por modelo, com IC 95%.
- Heatmap: significância p-valor de cada par (Braço, Modelo) para H1.

### Output esperado
- Commit: `frente2: analise estatistica McNemar Wilcoxon ANOVA`
- Artefato principal: `experiments/adversarial_clt/analysis/stats_summary.md`.

---

## Tarefa F2.7 — Relatório executivo Frente 2

Gerar `experiments/adversarial_clt/relatorio/RELATORIO_FRENTE2_FINAL.md` consolidando:

1. **Sumário executivo** (1 página): hipóteses, design, resultado das 4 hipóteses (H1-H4).
2. **Metodologia** (3 páginas): 4 braços × 4 modelos × 50 cenários × 3 runs; métricas D1 e D2; testes estatísticos.
3. **Resultados** (5-6 páginas):
   - Tabelas: D1 e D2 médios por (Braço, Modelo).
   - Plots: 8 boxplots + 1 plot agregado + 1 heatmap de significância.
   - Estatística: tabela com p-valores McNemar pareados.
4. **Discussão** (2 páginas):
   - Q-FENG bloqueia alucinação? Magnitude do efeito.
   - Efeito independente da arquitetura? Variância entre modelos.
   - Valor agregado da execução Clingo (B4 vs B3)?
   - Cenários onde Q-FENG falhou (false negatives) — importante para honestidade científica.
5. **Limitações** (1 página): 50 cenários × N predicados; modelos locais 12 GB; corpus em PT; avaliador deterministico tem limitações de NLP.
6. **Anexos**: paths dos artefatos, manifest.json, instruções de reprodução.

Esse relatório é o **insumo direto** para a escrita de uma nova §5.4 (ou §5.5) do Paper 1.

### Output esperado
- Commit: `frente2: relatorio final consolidado`
- Artefato: `experiments/adversarial_clt/relatorio/RELATORIO_FRENTE2_FINAL.md`

---

## Critérios de aceitação Frente 2

- [ ] 50 cenários CLT em `scenarios.yaml` validados contra Clingo.
- [ ] 4 braços implementados com YAMLs e runners.
- [ ] 4 modelos baixados e validados em VRAM 12 GB.
- [ ] 2400 calls executadas com 0 falhas pendentes.
- [ ] D1 e D2 computados para 2400 responses.
- [ ] Testes estatísticos rodados (McNemar, Wilcoxon, ANOVA + Bonferroni).
- [ ] H1 sustentada: D1(B4) < D1(B1), p<0.001 em todos os 4 modelos.
- [ ] Relatório `RELATORIO_FRENTE2_FINAL.md` gerado com 6 seções obrigatórias.
- [ ] Reprodutibilidade: manifest SHA256 + container Docker opcional documentado.

---

**Fim do prompt Frente 2.**
