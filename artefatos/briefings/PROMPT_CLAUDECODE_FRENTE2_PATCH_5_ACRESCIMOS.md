# Prompt Claude Code — Patch da Frente 2: 5 acréscimos editoriais

**Workspace:** `C:\Workspace\academico\qfeng_validacao` (conda env `qfeng`)
**Branch ativa:** `caminho2`
**Data de despacho:** 27/abr/2026
**Modus operandi:** 24/7, cada etapa gera artefato md/docx para alimentar reescrita do paper depois

---

## Contexto e relação com o briefing original

Este prompt é um **patch** ao plano da Frente 2 originalmente despachado em `artefatos/briefings/PROMPT_CLAUDECODE_FRENTE2_ADVERSARIAL_CLT.md`. **Não substitui** o briefing original — adiciona cinco deltas editoriais identificados na auditoria de fechamento da Frente 1 e na elaboração do argumento *"Q-FENG vs. BI"* registrada em sessão de chat (Bloco B do `INSERCOES_NOVAS_SECOES_CANONICO.md`).

A motivação dos cinco acréscimos é editorial: o briefing original fornece a estrutura experimental sólida (4 braços × 4 modelos × 50 cenários × 3 runs = 2.400 chamadas LLM, métricas D1 alucinação e D2 cobertura, testes McNemar pareados e Wilcoxon), mas não maximiza o potencial editorial do experimento face a revisor JURIX/AI&Law/JAIR. Os cinco acréscimos elevam a defensibilidade do paper, conectam Frente 2 à narrativa Frente 1 e ao argumento de generalidade arquitetônica do canônico, e antecipam objeções previsíveis de revisor.

**Estado atual da Frente 2 (auditado 27/abr/2026):** o Code já criou a estrutura `experiments/adversarial_clt/` com subdiretórios (analysis/, evaluators/, prompts/, relatorio/, results/, runners/, scenarios/), 4 templates YAML para os 4 braços (B1 a B4 em `prompts/`), e os runners (`run_arm.py`, `run_full_experiment.py`, `retry_failed.py`). Os 4 modelos LLM já foram baixados via Ollama (Qwen 3 14B, Phi-4 14B, Gemma 3 12B, Llama 3.3 8B). O Code está atualmente na fase de preparação dos cenários e evaluators, antes de iniciar a execução das 2.400 chamadas.

**Compatibilidade temporal:** este patch deve ser aplicado **antes** do início da geração dos cenários CLT e dos evaluators, mas **depois** da conclusão das tarefas em curso pelo Code no prompt original. O usuário sinalizou explicitamente que aguardará a conclusão das tarefas correntes antes de despachar este patch para evitar reset do trabalho.

---

## Síntese dos cinco acréscimos editoriais

| # | Acréscimo | Impacto editorial | Custo computacional adicional |
|---|---|---|---|
| 1 | Promover H3 a hipótese editorial central + adicionar H5 (cross-architecture invariance) | Sustenta reivindicação de agnosticismo de stack ML do canônico | Zero (mesma execução, novo teste estatístico) |
| 2 | Adicionar 5 cenários T-CTRL-NEG (controle negativo limpo trivialmente válido) | Detecta viés do parser de proposições; defende contra crítica de gabarito enviesado | Zero (substitui 5 cenários, não adiciona) |
| 3 | Adicionar métrica D3 (especificidade de fundamentação normativa) + H6 derivada | Atribui valor explícito à execução Clingo SAT/UNSAT; supera H4 | Marginal (parser existente extendido) |
| 4 | Pré-registro do experimento (OSF-style) com SHA256 commitado em Git | Eleva defensibilidade editorial face a revisor moderno | Marginal (3 horas de redação, antes de execução) |
| 5 | Análise de subgrupos por categoria de Fricção Ontológica do cenário | Costura editorial Frente 1 + Frente 2 + §3 do canônico | Zero (estratificação estatística sobre dados existentes) |

Total de impacto computacional adicional: **mínimo**. Os 5 acréscimos são predominantemente editoriais e estatísticos, e não exigem expansão da grade experimental original.

---

## Acréscimo 1 — Promover H3 a hipótese central + adicionar H5

### Motivação editorial

O briefing original lista quatro hipóteses (H1: D1(B4) < D1(B1); H2: D2(B4) > D2(B1)/D2(B2); H3: efeito independente da arquitetura LLM; H4: B4 > B3). H3 é tratada como auxiliar.

A demonstração editorialmente mais forte da Frente 2 não é "Q-FENG reduz alucinação em quatro modelos" (H1 aplicado quatro vezes). É **"o efeito Q-FENG é estatisticamente invariante face à família arquitetônica do LLM"** — operacionalizado como hipótese estatística testável. Essa hipótese é a evidência empírica do *agnosticismo de stack ML* reivindicado no Bloco B do `INSERCOES_NOVAS_SECOES_CANONICO.md` (§7.4 nova do canônico). Sem ela, a reivindicação fica como argumento teórico sem validação empírica.

### Operações requeridas

1. **Promover H3 a hipótese editorial central** com formulação estatística explícita. Reformular como:

   > **H3 (cross-architecture invariance):** O efeito Q-FENG na redução de alucinação é estatisticamente invariante entre famílias arquitetônicas de LLM. Operacionalmente, na ANOVA two-way `D1 ~ Braço × Modelo`, o termo de interação `Braço × Modelo` é estatisticamente não-significativo após correção Bonferroni (p > 0.05/m onde m é o número de hipóteses simultâneas testadas).

2. **Adicionar H5** como complemento de H3:

   > **H5 (effect-size overlap across architectures):** A magnitude do efeito Q-FENG `[D1(B1) − D1(B4)]_modelo_i` tem intervalo de confiança 95% que se sobrepõe ao IC95% de `[D1(B1) − D1(B4)]_modelo_j` para todos os pares (i,j) ∈ {Qwen, Phi, Gemma, Llama}. Operacionalmente, computar bootstrap 1000-iter sobre a diferença pareada e verificar overlap dos ICs.

3. **Atualizar `experiments/adversarial_clt/README.md`** para listar H1, H2, H3 (promovida), H4, H5 com formulações estatísticas explícitas em vez das atuais formulações narrativas.

4. **Implementar testes em `analysis/`:**
   - `test_h3_anova_interaction.py`: ANOVA two-way `D1 ~ Braço × Modelo` com correção Bonferroni; reportar F-statistic, p-valor da interação, e η² parcial.
   - `test_h5_effect_size_overlap.py`: bootstrap 1000-iter sobre `[D1(B1) − D1(B4)]_modelo_i` para cada modelo; reportar IC95% pareados e matriz de overlap binária 4×4.

### Output esperado
- Commit: `frente2-patch: H3 promovida + H5 cross-architecture invariance`
- Artefato: `experiments/adversarial_clt/analysis/test_h3_anova_interaction.py`, `test_h5_effect_size_overlap.py`

---

## Acréscimo 2 — Cenários T-CTRL-NEG (controle negativo limpo)

### Motivação editorial

O briefing original distribui 50 cenários CLT como: T-CLT-01 (15 phantom citation), T-CLT-02 (12 hour bank sem CCT), T-CLT-03 (12 hour bank com CCT, válido), T-CLT-04 (11 grounded citation, válido). T-CLT-03 e T-CLT-04 são **controles positivos** (decisões corretas que o LLM bruto pode reproduzir; o que importa é Q-FENG não as anular).

Falta um quinto bucket: **5 cenários de controle negativo limpo (T-CTRL-NEG)**. São cenários trivialmente válidos juridicamente, em que qualquer LLM razoável (mesmo bruto) deveria classificar corretamente, e em que D1 deve ser próximo de zero para todos os 4 braços e modelos. Servem dois propósitos editoriais:

1. **Detectar viés do parser de proposições.** Se D1 não cai a próximo de zero nestes cenários, há ruído sistemático no evaluator que invalida as comparações de braço.
2. **Defender contra crítica "gabarito enviesado".** Um revisor pode argumentar que o gabarito Clingo é construído de forma a favorecer Q-FENG; cenários T-CTRL-NEG demonstram que o parser não penaliza respostas corretas espontâneas, neutralizando essa crítica.

### Operações requeridas

1. **Reajustar a distribuição de cenários** preservando o total de 50 cenários e o budget de 2.400 chamadas LLM:

   | Bucket | Briefing original | Patch (esta operação) |
   |---|---|---|
   | T-CLT-01 (phantom citation) | 15 | 13 |
   | T-CLT-02 (hour bank sem CCT) | 12 | 11 |
   | T-CLT-03 (hour bank válido) | 12 | 11 |
   | T-CLT-04 (grounded citation) | 11 | 10 |
   | **T-CTRL-NEG** (controle negativo) | — | **5** |
   | **Total** | **50** | **50** |

2. **Especificação dos 5 cenários T-CTRL-NEG.** São cenários jurídicos triviais com gabarito SAT (decisão correta esperada). Sugestões editoriais (o Code escolhe a redação final):

   - **T-CTRL-NEG-01:** banco de horas com CCT vigente e devidamente registrada, com prazo de compensação dentro de 6 meses (CLT Art. 59 §2°). Decisão correta: válido.
   - **T-CTRL-NEG-02:** jornada compensatória de 8h44min/dia em regime semanal de 5 dias (totalizando 44h/semana, dentro do limite legal). Decisão correta: válido (CLT Art. 58, 59).
   - **T-CTRL-NEG-03:** citação a precedente exato e vinculante de Súmula TST aplicável ao caso (e.g., Súmula 85 sobre banco de horas inválido em jornada noturna). Decisão correta: aplicação correta da súmula.
   - **T-CTRL-NEG-04:** rescisão sem justa causa com aviso prévio de 30 dias devidamente cumprido (CLT Art. 477, 487). Decisão correta: rescisão válida.
   - **T-CTRL-NEG-05:** registro de ponto eletrônico com sistema homologado pela Portaria MTE 671/2021. Decisão correta: meio probatório válido.

3. **Gerar gabarito Clingo SAT** para cada um dos 5 cenários. Estes gabaritos vão para `corpora_clingo/clt_ctrl_neg.lp` (novo arquivo) ou serão integrados ao corpus CLT existente conforme decisão do Code, mantendo coerência arquitetônica.

4. **Validar com `clingo --syntax-check`** sobre o corpus completo expandido com T-CTRL-NEG.

5. **Atualizar `experiments/adversarial_clt/scenarios/manifest.json`** (ou equivalente em uso pelo Code) com a nova distribuição.

6. **Atualizar `experiments/adversarial_clt/README.md`** para documentar a categoria T-CTRL-NEG e seu propósito editorial.

### Output esperado
- Commit: `frente2-patch: 5 cenarios T-CTRL-NEG controle negativo limpo`
- Artefato: 5 entradas em `scenarios/`, atualização de manifest e README

---

## Acréscimo 3 — Métrica D3 (especificidade de fundamentação normativa) + H6

### Motivação editorial

O briefing original define duas métricas:
- **D1** (alucinação): proposições do LLM sem correspondência aos predicados Clingo ativos.
- **D2** (cobertura): predicados ativos mencionados pelo LLM em sua resposta.

Essas métricas capturam o que o Q-FENG reduz (D1) e o que ele expõe (D2). Falta uma métrica que capture o argumento editorial mais forte do framework: **fundamentação juridicamente sustentável face a TST/TRT/CSJT**.

A diferença entre B3 (dPASP-style anchoring com lista de predicados expostos) e B4 (Q-FENG completo com execução Clingo SAT/UNSAT) é que B4 tem **acesso ao predicado completo** (texto, modalidade deôntica, derivação fractal-jurisdicional, antecedentes), não apenas à lista. Esta diferença é potencialmente mensurável como *especificidade de citação* — se o LLM cita o artigo específico (e.g., "CLT Art. 59 §2°") ou faz referência vaga ("a CLT permite o banco de horas").

### Operações requeridas

1. **Definir D3 — Especificidade Normativa:**

   ```
   D3 = (proposições derivadas com citação artigo-específico) / (total de proposições derivadas)
   ```

   Onde "proposição derivada" é uma proposição classificada como "derivada de predicado ativo" (ou seja, não alucinação) pelo evaluator existente.

   **Critério de classificação de citação:** o evaluator considera "artigo-específico" se a proposição contém **(a)** referência a artigo numerado de instrumento normativo (e.g., "CLT Art. 59", "Súmula TST 85", "CF/88 Art. 7°"), OU **(b)** referência a precedente vinculante numerado (e.g., "ARE 791.932", "Súmula Vinculante 4"). Vagueza ("a CLT permite", "o entendimento jurisprudencial é") não conta.

2. **Implementar parser de citação** em `experiments/adversarial_clt/evaluators/d3_specificity.py` ou estendendo o evaluator D1/D2 existente. Usar regex calibrado para os padrões de citação CLT/CF/Súmulas:

   ```python
   PADROES_CITACAO_ESPECIFICA = [
       r'\b(CLT|CC|CF|CPC|CDC)\s+(?:Art\.?|Artigo)\s+\d+',  # CLT Art. 59
       r'\b(?:Súmula|SV)\s+(?:Vinculante\s+)?\d+',           # Súmula 85, SV 4
       r'\b(?:ARE|AI|RE|REsp|HC)\s+\d+',                     # ARE 791.932
       r'\bL\s*\d+(?:\.\d+)?(?:/\d+)?',                       # L 8.080, Lei 13.467/2017
   ]
   ```

   Validar com regex unitários sobre amostras antes de aplicar ao corpus.

3. **Adicionar H6 — métrica D3 supera H4:**

   > **H6 (Clingo SAT/UNSAT execution adds specificity):** D3(B4) > D3(B3) com p < 0.05 (Wilcoxon signed-rank pareado por cenário). A diferença atribui valor à execução Clingo (não apenas à exposição textual dos predicados como em B3).

4. **Estender `experiments/adversarial_clt/analysis/`** com `test_h6_d3_specificity.py` rodando Wilcoxon pareado D3(B4) − D3(B3) e reportando p-valor + tamanho de efeito Cliff's δ.

5. **Atualizar `experiments/adversarial_clt/README.md`** para documentar D3 e H6.

### Output esperado
- Commit: `frente2-patch: metrica D3 especificidade + H6`
- Artefato: `evaluators/d3_specificity.py`, `analysis/test_h6_d3_specificity.py`, atualização README

---

## Acréscimo 4 — Pré-registro do experimento

### Motivação editorial

JURIX, AI&Law e JAIR têm se movido para encorajar **pré-registro de experimentos empíricos** como prática editorial defensiva. A motivação é metodológica: pré-registro elimina a possibilidade de p-hacking, HARKing (Hypothesizing After Results are Known), e seleção post-hoc de testes estatísticos. Cumpre o mesmo papel que pré-registro tem em ensaios clínicos.

Pré-registrar a Frente 2 antes da execução das 2.400 chamadas LLM é editorialmente alta-relevante: é diferencial face à literatura NeSy 1.0 que tipicamente não pré-registra, e antecipa crítica de revisor moderno sobre rigor metodológico.

### Operações requeridas

1. **Criar `experiments/adversarial_clt/PRE_REGISTRATION.md`** com a seguinte estrutura:

   ```markdown
   # Pré-registro do Experimento Adversarial CLT — Q-FENG Frente 2

   **Branch:** caminho2  ·  **Data de pré-registro:** [data do commit]
   **Commit SHA256 deste documento (após commit):** [a ser preenchido]
   **Modelo de pré-registro:** OSF Standard Pre-Registration template (2024) adaptado

   ## 1. Objetivo do experimento
   [Texto curto: testar se Q-FENG (B4) reduz alucinação e aumenta cobertura
   normativa face a baseline LLM bruto (B1), RAG semântico (B2) e dPASP-style
   anchoring (B3), através de 4 modelos LLM e 50 cenários CLT.]

   ## 2. Hipóteses (formulação estatística explícita pré-execução)

   - **H1:** D1(B4) < D1(B1), Wilcoxon signed-rank pareado, p < 0.05/m após Bonferroni.
   - **H2:** D2(B4) > D2(B1) e D2(B4) > D2(B2), Wilcoxon pareado, p < 0.05/m.
   - **H3:** F(Braço × Modelo) ≤ F_critical, p > 0.05/m após Bonferroni (não-significância da interação na ANOVA two-way).
   - **H4:** D1(B4) < D1(B3), Wilcoxon pareado, p < 0.05/m.
   - **H5:** IC95% bootstrap de [D1(B1)−D1(B4)] sobreposto entre todos os pares (Qwen, Phi, Gemma, Llama).
   - **H6:** D3(B4) > D3(B3), Wilcoxon pareado, p < 0.05/m.

   ## 3. Operacionalização das métricas

   - **D1 (alucinação):** ver `evaluators/d1_hallucination.py`. Numerador: proposições do LLM sem correspondência aos predicados Clingo SAT/UNSAT do cenário. Denominador: total de proposições extraídas pelo parser.
   - **D2 (cobertura):** ver `evaluators/d2_coverage.py`. Numerador: predicados ativos mencionados pelo LLM. Denominador: total de predicados ativos no cenário.
   - **D3 (especificidade):** ver `evaluators/d3_specificity.py`. Numerador: proposições derivadas com citação artigo-específico (regex `PADROES_CITACAO_ESPECIFICA`). Denominador: total de proposições derivadas.

   ## 4. Critérios de exclusão de chamadas

   Uma chamada LLM é excluída da análise se:
   - Timeout > 300 segundos sem resposta.
   - OOM (CUDA out of memory) detectado.
   - JSON malformed após 3 tentativas de retry com `runners/retry_failed.py`.
   - Resposta vazia (< 50 caracteres) após 3 retries.

   Exclusões são reportadas por modelo e por braço; se mais de 5% das chamadas
   de um par (Modelo, Braço) forem excluídas, o par é descartado da análise
   estatística e reportado como limitação.

   ## 5. Plano de análise estatística

   - **Teste primário:** McNemar pareado (B1 vs B4) sobre classificação binária correta/incorreta agregada do cenário, por modelo.
   - **Teste secundário:** Wilcoxon signed-rank pareado sobre D1, D2, D3, por modelo.
   - **Correção de comparações múltiplas:** Bonferroni com m = número de hipóteses × número de modelos = 6 × 4 = 24.
   - **Análise de subgrupos:** estratificação por categoria de Fricção Ontológica do cenário (derivacional, procedural, mista, controle).
   - **Tamanhos de efeito:** Cliff's δ para Wilcoxon, Cohen's h para McNemar.

   ## 6. Distribuição de cenários

   | Bucket | N | Tipo de Fricção |
   |---|---|---|
   | T-CLT-01 (phantom citation) | 13 | Derivacional |
   | T-CLT-02 (hour bank sem CCT) | 11 | Procedural |
   | T-CLT-03 (hour bank válido) | 11 | Controle positivo |
   | T-CLT-04 (grounded citation) | 10 | Controle positivo |
   | T-CTRL-NEG (controle negativo limpo) | 5 | Controle negativo |
   | **Total** | **50** | — |

   ## 7. Modelos LLM avaliados (versão exata, hash do peso)

   | Modelo | Tag Ollama | Família | VRAM utilizada |
   |---|---|---|---|
   | Qwen 3 14B | `qwen3:14b` | Alibaba | ~9 GB Q4_K_M |
   | Phi-4 14B | `phi4:14b` | Microsoft | ~9 GB Q4_K_M |
   | Gemma 3 12B | `gemma3:12b` | Google | ~8 GB Q4_K_M |
   | Llama 3.3 8B | `llama3.3:8b` | Meta | ~5 GB Q4_K_M |

   ## 8. Hardware e configuração

   - GPU: NVIDIA RTX 3060 12 GB
   - CUDA: [versão preenchida pelo Code]
   - Ollama: [versão preenchida pelo Code]
   - Temperatura LLM: 0.0 (determinístico)
   - Seed: [a ser preenchido — recomenda-se 42 para reprodutibilidade]
   - Sistema: Windows 11, conda env `qfeng`

   ## 9. Compromisso de transparência

   - Resultados serão reportados independentemente do sentido (incluindo H que falharem).
   - Análises post-hoc não pré-registradas serão explicitamente marcadas como exploratórias.
   - Código completo (runners, evaluators, prompts YAML, scenarios) público em GitHub.
   - Dados brutos das 2.400 chamadas LLM em `experiments/adversarial_clt/results/raw_responses/`, depositados em Zenodo.

   ## 10. Selo SHA256

   Após commit deste documento na branch `caminho2`, o SHA256 do commit
   é registrado abaixo. Qualquer alteração subsequente ao pré-registro
   é rastreável via git log.

   `[a ser preenchido após primeiro commit]`

   ---

   *Fim do pré-registro. Branch `caminho2` · Q-FENG Frente 2 Adversarial CLT.*
   ```

2. **Commit do pré-registro ANTES de iniciar a execução das 2.400 chamadas LLM.** A ordem é editorialmente crítica: o pré-registro perde valor se for commitado depois dos resultados.

3. **Capturar SHA256 do commit do pré-registro** e atualizar a §10 do `PRE_REGISTRATION.md` com o hash. O hash captura o estado *exato* das hipóteses no momento do pré-registro e é o que permite verificação independente.

4. **Adicionar referência ao pré-registro** no `experiments/adversarial_clt/README.md` com a seção:
   ```markdown
   ## Pré-registro

   Este experimento foi pré-registrado em [data] (commit SHA256 [hash]).
   Hipóteses, operacionalização das métricas, critérios de exclusão e plano
   estatístico estão fixados em `PRE_REGISTRATION.md` antes da execução das
   2.400 chamadas LLM.
   ```

### Output esperado
- Commit: `frente2-patch: pre-registration OSF-style commitado antes da execucao`
- Artefato: `experiments/adversarial_clt/PRE_REGISTRATION.md` + atualização README

---

## Acréscimo 5 — Análise de subgrupos por categoria de Fricção Ontológica

### Motivação editorial

Os cenários T-CLT-01 a T-CLT-04 não são uniformes em termos do *tipo* de Fricção Ontológica que envolvem. A distinção é importante editorialmente porque conecta a Frente 2 ao argumento da §3 do canônico (tipologia de Fricção Ontológica) e à Camada 4 da Frente 1 (Fricção institucional, Manaus LSVP).

| Cenário | Tipo de Fricção | Mecanismo |
|---|---|---|
| T-CLT-01 (phantom citation) | **Derivacional** | A citação invocada não deriva do precedente real — falha de derivação na cadeia normativa |
| T-CLT-02 (hour bank sem CCT) | **Procedural** | Falta requisito formal procedimental — o instrumento não foi celebrado conforme a CLT exige |
| T-CLT-03 (hour bank válido) | Controle positivo | Caso jurídico válido sem Fricção Ontológica detectável |
| T-CLT-04 (grounded citation) | Controle positivo | Caso jurídico válido sem Fricção Ontológica detectável |
| T-CTRL-NEG | Controle negativo | Caso trivialmente válido (Acréscimo 2) |

Estratificar D1, D2 e D3 por *tipo de Fricção* (não apenas por T-CLT-XX) produz uma tabela editorial que costura a Frente 2 com o argumento teórico do canônico:

> *"O efeito Q-FENG é maior em cenários de Fricção derivacional (X%) do que de Fricção procedural (Y%), o que sustenta a hipótese de que a execução simbólica é mais valiosa em casos onde a falha não é de forma mas de derivação na cadeia normativa fractal-jurisdicional."*

Esse achado conecta diretamente a Frente 2 com a §3 do canônico (taxonomia de falhas) e com a Camada 4 da Frente 1 (Fricção institucional) — produzindo uma narrativa única integrada para o paper, em vez de dois experimentos separados.

### Operações requeridas

1. **Adicionar campo `friccao_categoria` ao manifesto de cenários** (`scenarios/manifest.json` ou equivalente em uso pelo Code), com valores ∈ {`derivacional`, `procedural`, `controle_positivo`, `controle_negativo`}.

2. **Implementar análise estratificada** em `experiments/adversarial_clt/analysis/test_subgroup_friccao.py`:
   - Para cada métrica D1, D2, D3:
     - Para cada par (Modelo, Braço):
       - Reportar média ± IC95% por categoria de Fricção.
   - Reportar **diferença pareada** D_braço(B4)−D_braço(B1) estratificada por categoria.
   - Testar formalmente se a diferença é maior em Fricção derivacional que em procedural (Mann-Whitney U entre as duas categorias, com tamanho de efeito Cliff's δ).

3. **Tabela proposta para o relatório de resultados Frente 2** (a ser produzida na fase de relatório, não agora):

   | Tipo de Fricção | N cenários | D1(B1) média | D1(B4) média | Δ D1 | IC95% Δ | p Wilcoxon |
   |---|---|---|---|---|---|---|
   | Derivacional | 13 | ... | ... | ... | ... | ... |
   | Procedural | 11 | ... | ... | ... | ... | ... |
   | Controle positivo | 21 | ... | ... | ... | ... | ... |
   | Controle negativo | 5 | ... | ... | ... | ... | ... |

4. **Atualizar `experiments/adversarial_clt/README.md`** para documentar a estratificação por Fricção Ontológica e referência cruzada à §3 do canônico.

### Output esperado
- Commit: `frente2-patch: estratificacao por tipo de Friccao Ontologica`
- Artefato: `analysis/test_subgroup_friccao.py`, atualização manifest e README

---

## Ordem de execução das tarefas do patch

A ordem importa por dependência:

1. **Acréscimo 4 (pré-registro)** primeiro — antes de qualquer código de cenário ou evaluator novo, comitar pré-registro com hipóteses fixadas. Esta é a prática editorialmente mais defensável.
2. **Acréscimo 1 (H3 + H5)** segundo — só atualiza README e cria scripts de análise; não depende de cenários novos.
3. **Acréscimo 2 (T-CTRL-NEG)** terceiro — adiciona 5 cenários e gabaritos Clingo; redistribui contagens.
4. **Acréscimo 3 (D3 + H6)** quarto — implementa parser de citação no evaluator; depende de cenários T-CTRL-NEG já manifestados (porque o parser será aplicado também a estes).
5. **Acréscimo 5 (estratificação Fricção)** por último — adiciona campo ao manifest e script de análise; pode ser feito em qualquer ordem após Acréscimo 2 mas é editorialmente coerente fechá-lo por último para fechar a costura Frente 1 + Frente 2.

---

## Critérios de aceitação patch Frente 2

- [ ] Acréscimo 1: H3 promovida no README, H5 adicionada, scripts `test_h3_anova_interaction.py` e `test_h5_effect_size_overlap.py` em `analysis/`.
- [ ] Acréscimo 2: 5 cenários T-CTRL-NEG manifestados e validados; distribuição final 13+11+11+10+5 = 50 cenários; gabaritos Clingo `clingo --syntax-check` OK.
- [ ] Acréscimo 3: Métrica D3 implementada em `evaluators/d3_specificity.py`, H6 documentada, `test_h6_d3_specificity.py` em `analysis/`.
- [ ] Acréscimo 4: `PRE_REGISTRATION.md` commitado **antes** de qualquer execução LLM, com SHA256 capturado e atualizado no §10 do próprio documento.
- [ ] Acréscimo 5: Campo `friccao_categoria` no manifest, script `test_subgroup_friccao.py`, README atualizado.
- [ ] Total de cenários permanece 50; total de chamadas LLM permanece 2.400 (4 braços × 4 modelos × 50 cenários × 3 runs).
- [ ] Modelos Ollama, runners, templates de prompt YAML, e arquitetura de avaliação **não foram resetados** — apenas estendidos.
- [ ] Cadeia de commits frente2-patch coerente: pre-registration → H3+H5 → T-CTRL-NEG → D3+H6 → Friccao subgroups.
- [ ] `experiments/adversarial_clt/README.md` atualizado integralmente refletindo as cinco mudanças.
- [ ] **Nenhum git push** sem confirmação explícita do autor.

---

## Notas operacionais para o Code

1. **Aplicar este patch APÓS conclusão das tarefas correntes do prompt original.** O usuário sinalizou explicitamente que aguardará a conclusão das tarefas em curso. Isto evita reset do trabalho de scaffolding já feito (estrutura de diretórios, templates YAML dos braços, runners).

2. **O pré-registro (Acréscimo 4) deve ser commitado ANTES de iniciar a execução das 2.400 chamadas LLM.** Esta ordem é editorialmente crítica e não-negociável.

3. **Reaproveitar templates existentes.** Os 4 templates YAML em `prompts/B1_llm_bruto.yaml`, `B2_rag_baseline.yaml`, `B3_dpasp_anchoring.yaml`, `B4_qfeng_completo.yaml` permanecem intocados. Se for necessário ajustar prompts para incorporar D3 (especificidade de citação), fazê-lo como override de instruction no template, não como reescrita do template.

4. **Não tocar Frente 1.** Operação retroativa Opção 2 da Frente 1 (truncar série em SE 14/2020) é independente e está em prompt separado (`PROMPT_CLAUDECODE_FRENTE1_OP2_TRUNCAR_SERIE.md`). As duas operações podem ser executadas em paralelo sem conflito.

5. **Modus operandi de artefatos longos.** Em conformidade com o briefing original e com o modus operandi consolidado do projeto: para qualquer artefato gerado com mais de ~50 linhas, gravar diretamente em arquivo via Desktop Commander e reportar apenas path + tamanho + sumário breve, em vez de renderizar conteúdo inline.

6. **Compatibilidade Windows cmd.exe.** O Code está rodando em Windows com cmd.exe como shell padrão. Evitar PowerShell heredoc para arquivos longos; usar Python `Path.write_text(c, encoding='utf-8')` em scripts `_tmp_*.py` quando necessário, conforme padrão consolidado do projeto.

---

**Fim do prompt patch Frente 2.**
