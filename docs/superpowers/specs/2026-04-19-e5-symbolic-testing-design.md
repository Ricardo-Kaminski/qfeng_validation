# Spec: E5 Symbolic Testing — Design para Paper Citavel
# =========================================================
# Data: 2026-04-19
# Nivel de exigencia: IEEE Transactions / NMI / AI & Law
# Avaliadores alvo: perfil Diaz-Rodriguez / Herrera (UGR/DaSCI)
# Objeto do paper: ARQUITETURA Q-FENG — nao os dados empiricos per se

---

## 1. Premissa central para citabilidade

O Q-FENG e um paper de ARQUITETURA de governanca de IA.
Os dados sao contexto de aplicacao, nao objeto de estudo.

O que os revisores de CS/AI vao avaliar com rigor:
  (a) Corretude formal da matematica (theta, psi_N, psi_S, theta_efetivo)
  (b) Implementacao verificavel e reproduzivel (GitHub publico)
  (c) Demonstracao empirica de que a arquitetura funciona nos cenarios
  (d) Comparacao com baseline (sem predicados vs com predicados)

O que NAO e problema para revisores de CS:
  - Dados sinteticos calibrados sobre literatura publica, desde que declarados
  - Cenarios de stress-test arquitetural sem claim quantitativo primario
  - Escopo geografico limitado a dados disponiveis

---

## 2. Formalismo matematico — o que precisa ser irrefutavel

### 2.1 Angulo de interferencia theta

theta = arccos( <psi_N | psi_S> / (||psi_N|| * ||psi_S||) )

onde:
  |psi_N> = vetor de estado do predictor (LightGBM / TimeSeries / Qwen)
             normalizado L2, dimensao = |decision_space|
  |psi_S> = vetor de estado normativo (predicados SOVEREIGN ativos)
             construido a partir das classificacoes HITL
             normalizado L2, mesma dimensao de |psi_N>

Regimes de interferencia:
  STAC:           theta < 30 deg  (interferencia construtiva forte)
  HITL:    30 <= theta < 120 deg  (zona de tensao normativa)
  CIRCUIT_BREAKER: theta >= 120 deg  (interferencia destrutiva)
  BLOQUEADO:       theta = pi  (ortogonalidade total — predicado soberano viola)

### 2.2 Extensao markoviana theta_efetivo (contribuicao original)

DEFINICAO FORMAL:

  theta_efetivo(t) = alpha(t) * theta(t) + (1 - alpha(t)) * theta_efetivo(t-1)

  alpha(t) = sigmoid( beta * delta_pressao(t) )

  delta_pressao(t) = score_pressao(t) - score_pressao(t-1)

  beta calibrado empiricamente nos dados Manaus:
    beta_otimo = argmin sum_t [ L(theta_efetivo(t), regime_observado(t)) ]
    onde L e a cross-entropy entre regime previsto e regime real (jan/2021 = CB)

JUSTIFICATIVA: alpha adaptativo captura a aceleracao da resposta normativa.
Quando delta_pressao e alto (sistema deteriorando rapidamente), o sistema
normativo deve dar mais peso ao estado atual (alpha -> 1).
Quando estavel (delta_pressao ~ 0), mantem memoria historica (alpha -> 0.5).

Esta formulacao e diferenciavel e testavel empiricamente na serie Manaus.
Nenhum paper existente no campo NeSy ou AI Governance formaliza este conceito.

### 2.3 Cybernetic Loss Function

L_Global = lambda_1 * theta + lambda_2 * (1 - confidence_predictor)
           + lambda_3 * alhedonic_signal - lambda_4 * n_sovereign_satisfied

onde lambda_i sao hiperparametros do sistema (reportar valores calibrados).

---

## 3. Cenarios E5 — o que cada um demonstra arquiteturalmente

### CORPUS SAUDE

C1 — CEAF medicamentos (Brasil, LightGBM, dado real 180 meses)
  Demonstra: theta ~ 0 quando predicado soberano nao existe no corpus
  (fornecimento_continuo nao e formalizado como SOVEREIGN)
  Contribuicao: identifica lacuna normativa — o sistema nao tem como saber
  que deve bloquear porque o predicado nao foi classificado como inviolavel.
  Tipo de falha: EXECUCAO (nao constitucional)

C2 — Manaus 2021 (Brasil, TimeSeries, dado real 1.526 AIH)
  Demonstra: trajetoria theta_efetivo captura aceleracao antes do colapso
  jan/2021 = theta > 120 = Circuit Breaker ativado
  Contribuicao: theta_efetivo markoviano e sensivel ao padrao temporal
  que theta estatico nao captaria (out/2020 ja estava em trajetoria critica)
  Tipo de falha: EXECUCAO com degradacao temporal

C3 — Concentracao regional SUS (Brasil, LightGBM, dado real por UF)
  Demonstra: theta ~ pi quando predicado equidade_regional_sus nao e satisfeito
  O predicado existe (CF/88 Art. 196) mas o sistema operacional viola-o
  Contribuicao: diferenca entre falha de execucao (C1) e falha constitucional (C3)
  — a arquitetura distingue os dois tipos sem configuracao especial
  Tipo de falha: CONSTITUCIONAL

C4a — Qwen sem predicados (Brasil, LLM, dado real contexto clinico)
  Demonstra: LLM sem constraints normativos tem theta alto/variavel
  Serve como BASELINE para C4b
  Tipo: stress-test arquitetural baseline

C4b — Qwen com predicados SOVEREIGN injetados (Brasil, LLM, mesmo contexto)
  Demonstra: injecao de predicados SOVEREIGN no system prompt reduz theta
  ESTA E A COMPARACAO MAIS IMPORTANTE DO PAPER
  Claim: delta_theta = theta(C4a) - theta(C4b) > 0 em todos os casos testados
  Tipo: validacao do mecanismo de reducao de friccao ontologica

C4c — theta_efetivo markoviano (Brasil, Qwen, 8 consultas sequenciais rescisao)
  Demonstra: theta_efetivo em sequencia de consultas simula trajetoria
  de um sistema de apoio juridico ao longo do tempo
  Contribuicao: extensao markoviana funciona para LLM sequencial
  nao apenas para serie temporal de dados estruturados
  Tipo: validacao da generalizabilidade da extensao markoviana

### CORPUS SAUDE — REGIMES EU E USA

C5 — EU AI Act auditabilidade (EU, dataset calibrado sobre Annex III 2024/1689)
  Demonstra: arquitetura funciona com predicados de regime diferente
  Tipo: proof-of-concept arquitetural (declarar explicitamente)

C6 — GDPR Art.22 (EU, dataset calibrado sobre GDPR Enforcement Tracker 2024)
  Demonstra: predicados de protecao de dados modulam theta diferentemente
  de predicados de saude — Elasticidade Ontologica diferenciada por regime
  Tipo: proof-of-concept arquitetural (declarar explicitamente)

C7 — Bias algoritmico (USA, Obermeyer 2019, dado REAL n=48.784)
  Demonstra: Q-FENG detecta sub-representacao racial como theta ~ pi
  porque predicado equidade_racial esta ausente do sistema operacional
  Contribuicao: ancora empirica do claim USA — dado real de alta qualidade
  Tipo: VALIDACAO EMPIRICA PRIMARIA (nao proof-of-concept)

C8 — Acesso Medicaid (USA, dataset calibrado sobre CMS FY2023)
  Demonstra: heterogeneidade de acesso modula theta por estado/demografico
  Tipo: proof-of-concept arquitetural (declarar explicitamente)

### CORPUS TRABALHISTA

T-CLT-01 — Mata v. Avianca (Brasil, ASP puro, jurisprudencia real TST)
  Demonstra: citacao fantasma = predicado normativo sem base real -> theta ~ pi
  Tipo: falha constitucional

T-CLT-02 — Sumula TST 85 distorcida (Brasil, ASP puro)
  Demonstra: interpretacao incorreta de sumula = theta > 120
  Tipo: falha de execucao

T-CLT-03 — Banco de horas CCT (Brasil, ASP puro)
  Demonstra: predicado ELASTIC corretamente modulado = theta < 30 (STAC)
  ESTE E O CASO POSITIVO — o sistema funcionando corretamente
  Contribuicao: Q-FENG tambem valida conformidade, nao apenas detecta violacoes
  Tipo: validacao positiva

T-CLT-04 — theta_efetivo markoviano (Brasil, Qwen, 8 consultas rescisao)
  Demonstra: mesmo que C4c mas no dominio juridico-trabalhista
  Generalizabilidade cross-domain da extensao markoviana
  Tipo: validacao da contribuicao original em segundo dominio

---

## 4. Schema de outputs E5 (obrigatorios para reproducibilidade)

### 4.1 e5_validation_results.parquet

Colunas obrigatorias:
  scenario_id, corpus, regime, condition, theta_deg, theta_rad,
  interference_regime, psi_n_json, psi_s_json,
  n_sovereign_active, n_elastic_active, alhedonic_signal,
  predictor_type, predictor_confidence, outcome_label,
  outcome_description, data_source, n_observations,
  cybernetic_loss, timestamp

data_source DEVE ser um dos valores:
  "real_primary"           <- SIH/DATASUS, CEAF, Obermeyer, TST
  "real_normative"         <- predicados ASP derivados de corpus real
  "synthetic_calibrated"   <- C5, C6, C8 — declarar fonte de calibracao

### 4.2 e5_theta_efetivo_manaus.parquet

Colunas obrigatorias (serie temporal Manaus):
  competencia, ano_cmpt, mes_cmpt,
  theta_t, theta_efetivo, alpha_t,
  interference_regime, internacoes_total, obitos_total,
  taxa_mortalidade, dias_uti_total, score_pressao, delta_pressao,
  delta_theta, n_sovereign_ativados, evento_critico

### 4.3 e5_llm_comparison.parquet

Colunas obrigatorias (comparativo C4a vs C4b):
  scenario_id, query_id, condition,
  theta_deg, psi_n_json, action_recommended,
  action_normatively_correct, reduction_delta,
  n_sovereign_injected, sovereign_predicates_list

---

## 5. Graficos — especificacao para publicacao

### Figura 1 — Theta por cenario (FIGURA DE CAPA / ABSTRACT)
Tipo: horizontal bar com faixas de regime coloridas
Dados: e5_validation_results.parquet
Mensagem: a arquitetura distingue tipos de falha normativa por posicionamento angular
Requisito de qualidade: 300 DPI, paleta acessivel (colorblind-safe), legenda bilingue

### Figura 2 — Trajetoria theta_efetivo Manaus (FIGURA MAIS CITAVEL)
Tipo: dual-axis line chart
Eixo esquerdo: theta_t e theta_efetivo (graus)
Eixo direito: score_pressao (0-1)
Anotacoes: setas indicando HITL e Circuit Breaker ativados
Linha vertical: jan/2021 (evento critico)
Mensagem: theta_efetivo antecipa colapso — theta estatico nao anteciparia
Este grafico vai aparecer em slides de apresentacao de outros pesquisadores

### Figura 3 — Delta theta C4a vs C4b (SEGUNDA FIGURA MAIS CITAVEL)
Tipo: paired dot plot ou slopegraph
Cada ponto: uma query
Linha conectando: reducao de theta com predicados SOVEREIGN
Mensagem: predicados SOVEREIGN reduzem friccao ontologica mensuravelmente
Inclui: cohen's d ou effect size para tornar o claim quantitativo preciso

### Figura 4 — SOVEREIGN vs ELASTIC por regime
Tipo: stacked bar normalizado (100%)
Dados: saida do E4 HITL
Mensagem: heterogeneidade de elasticidade ontologica entre regimes normativos

### Figura 5 — Distribuicao DeonticAtoms
Tipo: grouped bar (corpus saude vs trabalhista)
Modalidades: obligation / prohibition / permission / faculty
Mensagem: natureza normativa dos corpora e empiricamente diferenciada

### Figura 6 — Heatmap Sinal Alhedonico por documento
Tipo: heatmap (documentos x componentes do sinal)
Mensagem: Friccao Ontologica estrutural e heterogenea mesmo dentro de um regime

### Figura 7 — Obermeyer violin plot (USA C7, dado real)
Tipo: violin plot + box plot sobrepostos
Grupos: White vs Black
Variavel: risk_score normalizado
Mensagem: theta ~ pi tem correlato empirico de disparidade racial mensuravel

---

## 6. Testes estatisticos obrigatorios (exigencia CS/IEEE)

Para C4a vs C4b (comparativo LLM):
  - Wilcoxon signed-rank test (n pequeno, distribuicao nao-normal)
  - Effect size: Cohen's d
  - Hipotese: theta(C4b) < theta(C4a) para todas as queries (p < 0.05)

Para Obermeyer C7:
  - Mann-Whitney U test (White vs Black risk_score)
  - Replicar resultado original do paper como validacao de baseline

Para theta_efetivo vs theta estatico (Manaus):
  - Comparar MAE de previsao de regime entre os dois metodos
  - Mostrar que theta_efetivo tem menor erro de classificacao de regime
    no periodo out/2020-jan/2021 (especialmente na deteccao precoce)

---

## 7. Declaracoes metodologicas obrigatorias no paper

### Sobre dados sinteticos:
"Datasets for C5 (EU AI Act conformity), C6 (GDPR enforcement), and C8
(Medicaid access) were generated as calibrated synthetic datasets derived
from publicly available regulatory statistics: EU AI Act Annex III risk
categories (Regulation 2024/1689), GDPR Enforcement Tracker 2024 (n=1,400+
decisions), and CMS Medicaid Annual Reports FY2023. These datasets serve to
validate architectural generalizability across normative regimes rather than
to establish regime-specific empirical claims. Primary empirical evidence
is provided by: SIH/DATASUS (n=1,526, Manaus 2020-2021), CEAF/IADAF
LightGBM model (n=180 months), and the Obermeyer et al. (2019) replication
dataset (n=48,784)."

### Sobre reproducibilidade:
"All code, predicates, and public datasets are available at:
github.com/[repositorio]/qfeng-validation
The repository includes: complete pipeline C1 (E0-E5), all ASP predicate
files, Clingo test cases, and figure generation scripts."

### Sobre theta_efetivo (contribuicao original):
"The Markovian extension theta_efetivo is an original contribution not
present in existing QDT or NeSy literature. Unlike static interference angle
computation, theta_efetivo incorporates temporal memory of normative friction
with an adaptive weighting parameter alpha calibrated on empirical data
(Manaus crisis series, 2020-2021). The extension is formally defined in
Section 3.2 and empirically validated in Scenarios C2 and C4c."

---

## 8. Ordem de execucao para gerar todos os outputs

Passo 1: E4 Fase B — revisao HITL (voce, Streamlit)
Passo 2: E4 export — sovereign/ e elastic/
Passo 3: E5 execucao — todos os cenarios -> 3 parquets
Passo 4: validation_analysis.ipynb — tabelas e testes estatisticos
Passo 5: export_figures.py — 7 figuras em 300 DPI (PDF + PNG)
Passo 6: export_tables.py — tabelas em LaTeX + CSV
Passo 7: README_replication.md — instrucoes completas de replicacao
