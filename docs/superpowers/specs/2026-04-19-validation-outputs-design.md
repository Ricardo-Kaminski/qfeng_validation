# Spec: Validation Outputs — Paper-Grade Evidence Design
# =========================================================
# Data: 2026-04-19
# Contexto: paper Q-FENG submetido a avaliadores de nivel IEEE/NMI
# Referencia de qualidade: Diaz-Rodriguez (121k citacoes), Herrera (DaSCI/UGR)
# Objetivo: gerar evidencias irrefutaveis para validacao empirica da arquitetura

---

## 1. Premissa metodologica

Um paper citavel em AI + Law / NeSy / AI Governance precisa de tres camadas
de evidencia que se reforcem mutuamente:

CAMADA 1 — Evidencia estrutural
  Demonstrar que o pipeline gera predicados validos e consistentes
  (ja temos: 4.973 predicados, 99.9% validos — dado irrefutavel)

CAMADA 2 — Evidencia comportamental
  Demonstrar que theta captura corretamente os regimes de interferencia
  nos cenarios empiricos (o que o E5 precisa produzir)

CAMADA 3 — Evidencia comparativa
  Demonstrar que o Q-FENG com predicados SOVEREIGN reduz theta_efetivo
  em relacao ao baseline sem constraints normativos (C4a vs C4b)
  Esta e a contribuicao original mais forte — nenhum paper existente
  tem esta comparacao com dados reais do SUS.

---

## 2. Outputs obrigatorios do E5 para o paper

### 2.1 Arquivo principal: e5_validation_results.parquet

Schema obrigatorio — uma linha por cenario × condicao experimental:

  scenario_id         string    C1, C2, C3, C4a, C4b, C4c, T-CLT-01..04
  corpus              string    sus_validacao | advocacia_trabalhista
  regime              string    brasil | eu | usa
  condition           string    baseline | with_predicates | markovian
  theta_deg           float     angulo em graus [0, 180]
  theta_rad           float     angulo em radianos [0, pi]
  interference_regime string    STAC | HITL | CIRCUIT_BREAKER
  psi_n               string    JSON do array numpy serializado
  psi_s               string    JSON do array numpy serializado
  n_sovereign_active  int       quantos predicados SOVEREIGN ativos
  n_elastic_active    int       quantos predicados ELASTIC ativos
  alhedonic_signal    float     sinal alhedonico do cenario [0,1]
  predictor_type      string    LightGBM | TimeSeries | Qwen
  predictor_confidence float    confianca do predictor [0,1]
  outcome_label       string    STAC_autonomo | HITL_required | circuit_breaker | blocked
  outcome_description string    descricao textual do desfecho
  timestamp           string    ISO 8601
  data_source         string    real | synthetic_calibrated
  n_observations      int       tamanho do dataset empirico subjacente

### 2.2 Arquivo trajetoria: e5_theta_efetivo_manaus.parquet

Schema — uma linha por competencia (serie temporal C2/C4c):

  competencia         string    AAAAMM ex: 202010
  ano_cmpt            int       2020 | 2021
  mes_cmpt            int       1-12
  theta_t             float     theta no instante t
  theta_efetivo       float     theta_efetivo markoviano (media ponderada)
  interference_regime string    STAC | HITL | CIRCUIT_BREAKER
  internacoes_total   int       total AIH no periodo
  obitos_total        int       obitos hospitalares
  taxa_mortalidade    float     obitos/internacoes
  dias_uti_total      int       dias em UTI
  score_pressao       float     score combinado [0,1]
  delta_theta         float     variacao theta em relacao ao periodo anterior
  n_sovereign_ativados int      predicados soberanos que dispararam
  evento_critico      bool      True apenas para jan/2021

### 2.3 Arquivo comparativo LLM: e5_llm_comparison.parquet

Schema — demonstra C4a vs C4b (baseline vs com predicados):

  scenario_id         string    C4a | C4b | C4c
  query_id            int       1-8 (para C4c)
  condition           string    sem_predicados | com_predicados
  theta_deg           float
  psi_n               string    JSON
  action_recommended  string    decisao do Qwen
  action_correct      bool      conforme norma soberana?
  reduction_delta     float     reducao de theta entre C4a e C4b (so para C4b)
  sovereign_injected  list      predicados injetados no system prompt

---

## 3. Tabelas para o paper (geradas a partir dos parquets)

### Tabela 1 — Corpus normativo (ja disponivel, so formatar)

| Corpus | Regime | Docs | Chunks | DeonticAtoms | Predicados ASP | Valid% | SOVEREIGN% | ELASTIC% |
(preencher apos E4 Fase B)

### Tabela 2 — Resultados E5 por cenario (tabela central)

| ID | Dominio | Regime | Predictor | theta | Regime Interf. | Desfecho | n_obs | Fonte |
| C1 | Saude | Brasil | LightGBM | ~0 | STAC | ruptura nao detectada | 180 meses | real |
| C2 | Saude | Brasil | TimeSeries | >120 | Circuit Breaker | colapso O2 jan/2021 | 1.526 AIH | real |
| C3 | Saude | Brasil | LightGBM | ~180 | Bloqueado | concentracao regional | por UF | real |
| C4a | Saude | Brasil | Qwen sem | alto | HITL/CB | decisao sem ancora normativa | - | real |
| C4b | Saude | Brasil | Qwen com | reduzido | STAC/HITL | decisao com ancora normativa | - | real |
| C4c | Saude | Brasil | Qwen seq | trajetoria | markoviano | 8 consultas rescisao | - | real |
| C7 | USA | USA | Statistical | ~180 | Bloqueado | sub-representacao racial | 48.784 | real |
| T-CLT-01 | Juridico | Brasil | ASP | ~180 | Bloqueado | citacao fantasma | jurisprud. | real |
| T-CLT-02 | Juridico | Brasil | ASP | >120 | Circuit Breaker | sumula distorcida | TST | real |
| T-CLT-03 | Juridico | Brasil | ASP | <30 | STAC | banco horas CCT correto | CLT | real |
| T-CLT-04 | Juridico | Brasil | Qwen seq | trajetoria | markoviano | 8 consultas rescisao | - | real |

### Tabela 3 — Comparativo C4a vs C4b (contribuicao original)

| Condicao | theta_medio | Regime_Interf. | Acoes_corretas% | Predicados_ativos |
| Sem predicados (C4a) | X.X | HITL/CB | YY% | 0 |
| Com predicados (C4b) | X.X | STAC | ZZ% | N |
| Delta | -X.X | melhora | +ZZ% | - |

### Tabela 4 — Trajetoria theta_efetivo Manaus (contribuicao original)

| Competencia | theta_t | theta_efetivo | Regime | taxa_mort | score_pressao | evento |
| out/2020 | <30 | <30 | STAC | baixa | 0.1x | - |
| nov/2020 | ~45 | ~38 | HITL | crescente | 0.2x | - |
| dez/2020 | ~89 | ~62 | HITL | alta | 0.5x | - |
| jan/2021 | >127 | >95 | CB | critica | 0.9x | colapso O2 |
| fev/2021 | ~90 | ~98 | CB | decrescente | 0.7x | - |
| mar/2021 | ~60 | ~85 | HITL | estabilizando | 0.4x | - |

---

## 4. Graficos para o paper — especificacao precisa

### Figura 1 — Distribuicao theta por cenario (GRAFICO DE CAPA)
Tipo: bar chart horizontal com faixas de regime
Eixo Y: cenarios (C1, C2, C3, C4a, C4b, C7, T-CLT-01..04)
Eixo X: theta em graus [0, 180]
Faixas coloridas: verde [0-30 STAC], amarelo [30-120 HITL], vermelho [120-180 CB]
Marcadores: triangulo para "com predicados", circulo para "sem predicados"
Mensagem visual: theta agrupa por tipo de falha normativa, predicados deslocam para esquerda

### Figura 2 — Trajetoria theta_efetivo Manaus (FIGURA MAIS IMPORTANTE)
Tipo: line chart com area sombreada
Eixo X: out/2020 a mar/2021
Eixo Y: theta em graus (linha solida) + score_pressao (linha tracejada, eixo secundario)
Anotacoes: "Alerta HITL" em nov/2020, "Circuit Breaker" em jan/2021, "Colapso O2" com seta
Faixas de fundo: verde/amarelo/vermelho por regime
Mensagem: theta_efetivo markoviano captura aceleracao antes do colapso (previsao)

### Figura 3 — SOVEREIGN vs ELASTIC por regime (EVIDENCIA COMPARATIVA)
Tipo: stacked bar normalizado (100%)
Eixo X: brasil | eu | usa
Cores: azul escuro SOVEREIGN, azul claro ELASTIC
Valores numericos em cada barra
Mensagem: heterogeneidade de elasticidade ontologica entre regimes

### Figura 4 — Comparativo C4a vs C4b (CONTRIBUICAO ORIGINAL)
Tipo: paired bar ou arrow plot
Para cada uma das N queries: theta_sem vs theta_com
Seta apontando para baixo = reducao de theta com predicados
Mensagem: injecao de predicados SOVEREIGN reduz friccao ontologica mensuravel

### Figura 5 — Distribuicao DeonticAtoms por modalidade e corpus
Tipo: grouped bar ou heatmap
Eixo X: obligation | prohibition | permission | faculty
Grupos: corpus saude vs trabalhista
Mensagem: distribuicao reflete natureza normativa do corpus (CLT=impeditivo, SUS=prestacional)

### Figura 6 — Sinal Alhedonico por documento (HEATMAP)
Tipo: heatmap ordenado por signal decrescente
Eixo X: documentos (CF88, Lei8080, EU-AI-Act, SSA-XIX, CLT, ...)
Eixo Y: componentes do sinal (concurrent_penalty, modality_conflict, strength_mismatch, low_conf)
Mensagem: documentos com maior friccao ontologica estrutural identificados empiricamente

### Figura 7 — Obermeyer: distribuicao risk_score por raca (USA C7)
Tipo: violin plot ou box plot
Grupos: White vs Black (dado real, 48.784 obs)
Variavel: risk_score normalizado
Anotacao: "predicado equidade_racial ausente -> theta aprox pi"
Mensagem: friccao ontologica tem correlato empirico de disparidade racial mensuravel

---

## 5. Consideracoes metodologicas para o paper

### Sobre dados sinteticos C5/C6/C8
Os cenarios C5 (EU AI Act auditabilidade), C6 (GDPR Art.22) e C8 (Medicaid acesso)
usam datasets sinteticos calibrados sobre parametros reais documentados em:
- EU AI Act Annex III risk categories (2024/1689)
- GDPR Enforcement Tracker statistics 2023-2024
- CMS Medicaid enrollment reports FY2023

Declaracao metodologica obrigatoria no paper:
"Synthetic datasets were generated using calibrated distributions derived from
publicly available enforcement statistics and regulatory reports. While these
datasets do not constitute primary empirical evidence, they serve to validate
the architectural generalizability of Q-FENG across normative regimes where
primary data access is restricted. The empirical anchor for cross-regime
comparison is provided by the Obermeyer et al. (2019) replication dataset
(n=48,784) for the USA regime."

### Sobre theta_efetivo markoviano
Esta e a contribuicao tecnica original mais forte e requer:
1. Definicao formal da extensao markoviana (ja no SSRN WP)
2. Demonstracao empirica com a serie temporal Manaus
3. Comparacao com theta estatico (mostrar que theta_efetivo captura aceleracao)
4. Equacao explicita no paper: theta_efetivo(t) = alpha * theta(t) + (1-alpha) * theta_efetivo(t-1)
   onde alpha e calibrado empiricamente pela taxa de variacao do score_pressao

### Sobre replicabilidade (exigencia IEEE/NMI)
Todo codigo, dados publicos e predicados ASP devem estar no GitHub publico.
Repositorio estruturado com:
- README.md com instrucoes de replicacao completas
- requirements.txt / environment.yaml
- Scripts de reproducao dos graficos e tabelas
- Dados: apenas os publicos (Obermeyer, GDPR enforcement, CMS)
- Predicados ASP: completos (nao ha restricao de publicacao)

---

## 6. Sequencia de geracao dos outputs (ordem de execucao)

1. E4 Fase B — revisao HITL (voce, no Streamlit)
2. E4 export — gerar sovereign/ e elastic/
3. E5 execucao — rodar todos os cenarios, gerar os 3 parquets acima
4. validation_notebook.ipynb — carregar parquets, gerar tabelas e graficos
5. export_figures.py — salvar todos os graficos em docs/figuras/ (300 DPI, PDF+PNG)
6. export_tables.py — salvar todas as tabelas em docs/tabelas/ (LaTeX + CSV)
