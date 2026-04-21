# BRIEFING — Curadoria do Corpus Clingo Q-FENG
# =============================================
# Para: Claude Code + sessão Claude Opus 4
# Data: 2026-04-20
# Workspace: C:\Workspace\academico\qfeng_validacao

---

## DECISÃO ARQUITETURAL TOMADA

Abandonar o pipeline E1/E2/E3 automático para os predicados de validação.
Criar corpus Clingo curado manualmente em:
  C:\Workspace\academico\qfeng_validacao\corpora_clingo\

Os documentos originais permanecem intactos em corpora/ — não modificar.

---

## ESTRUTURA JÁ CRIADA (não recriar)

corpora_clingo/
  brasil/
    constitucional/
      cf88_principios_fundamentais.lp     ✅ CRIADO (90 linhas)
    saude/
      sus_direito_saude.lp                ✅ CRIADO (109 linhas)
    emergencia_manaus/
      emergencia_sanitaria.lp             ✅ CRIADO (110 linhas)
    trabalhista/
      clt_direitos_trabalhistas.lp        ✅ CRIADO (138 linhas)
  eu/
    ai_act/
      eu_ai_act_obligations.lp            ✅ CRIADO (110 linhas)
    gdpr/
      (a criar)
  usa/
    civil_rights/
      (a criar)
    medicaid/
      (a criar)

---

## PRINCÍPIO FUNDAMENTAL (não violar)

Os predicados Clingo NÃO são extração automática de documentos inteiros.
São curadoria jurídica precisa, organizada em camadas:

CAMADA 1 — Princípios pétreos (CF/88 Art. 5°, Art. 60 §4°, Art. 1°, Art. 3°)
  Aplicabilidade UNIVERSAL — regulam TODOS os cenários
  Não podem ser derrogados por nenhuma norma infraconstitucional
  CRÍTICOS para: equidade racial (C7), equidade regional (C3),
  due process (T-CLT-01), dignidade humana (todos)

CAMADA 2 — Direitos sociais específicos por domínio
  Saúde: CF/88 Art. 196-200, Lei 8080 Art. 2°/7°
  Trabalho: CF/88 Art. 7°, CLT Arts. relevantes, TST súmulas/OJs
  Cada domínio tem seu arquivo separado

CAMADA 3 — Regulamentação operacional (portarias, regulamentos)
  Específicos por cenário — ELASTIC em sua maioria
  Exemplo: portarias Manaus 2021 para o cenário C2

CAMADA 4 — Jurisprudência (TST, CJEU, SCOTUS)
  Consolida interpretação autorizada dos dispositivos
  Exemplo: Súmula TST 85, OJ SDI-1 233

---

## TAREFA PARA O CLAUDE CODE

### PASSO 1 — Ler os 4 arquivos já criados
  Ler e validar sintaxe Clingo:
  clingo --syntax-check corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp
  clingo --syntax-check corpora_clingo/brasil/saude/sus_direito_saude.lp
  clingo --syntax-check corpora_clingo/brasil/emergencia_manaus/emergencia_sanitaria.lp
  clingo --syntax-check corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp
  clingo --syntax-check corpora_clingo/eu/ai_act/eu_ai_act_obligations.lp

### PASSO 2 — Criar arquivos faltantes

#### eu/gdpr/gdpr_data_protection.lp
Âncoras:
  GDPR Art. 5° — princípios do tratamento (licitude, lealdade, transparência)
  GDPR Art. 9° — categorias especiais (dados de saúde = categoria especial)
  GDPR Art. 22° — decisões automatizadas e perfilagem
  GDPR Art. 17° — direito ao apagamento
  GDPR Art. 25° — proteção de dados desde a concepção (privacy by design)

Cenário Q-FENG: C6 — GDPR Art. 22 / decisão automatizada em saúde
  theta > 90° quando sistema processa dados de saúde sem base legal explícita
  ou quando decisão automatizada afeta titular sem direito de revisão humana

#### usa/civil_rights/civil_rights_14th.lp
Âncoras:
  14ª Emenda — Equal Protection Clause (Seção 1)
  Civil Rights Act 1964 Title VI — proibição de discriminação em programas
    federais (inclui programas de saúde financiados pelo governo federal)
  42 USC §1983 — ação civil por violação de direitos constitucionais

Cenário Q-FENG: C7 — Bias algorítmico Obermeyer 2019
  theta ~ pi quando sistema de scoring perpetua disparidade racial
  violando Equal Protection (14ª Emenda) e Title VI (Civil Rights)

#### usa/medicaid/medicaid_access.lp
Âncoras:
  SSA XIX §1902(a)(1) — statewideness (acesso em todo o estado)
  SSA XIX §1902(a)(10) — comparability (serviços comparáveis entre beneficiários)
  SSA XIX §1902(a)(19) — dignidade e privacidade dos beneficiários
  42 CFR §435.1 — elegibilidade Medicaid
  42 CFR §440.240 — comparabilidade de serviços

Cenário Q-FENG: C8 — Acesso Medicaid / heterogeneidade por estado
  theta > 90° quando sistema produz acesso não comparável entre beneficiários
  da mesma categoria violando §1902(a)(10)

### PASSO 3 — Criar arquivo de fatos de cenário (facts)

Para cada cenário, criar arquivo de fatos que ativa os predicados:

corpora_clingo/scenarios/
  c1_ceaf_facts.lp          — fatos do cenário CEAF
  c2_manaus_facts.lp        — fatos do cenário Manaus
  c3_concentracao_facts.lp  — fatos do cenário concentração regional
  c7_obermeyer_facts.lp     — fatos do cenário bias algorítmico
  t_clt_01_facts.lp         — fatos do cenário Mata v. Avianca
  t_clt_02_facts.lp         — fatos do cenário Súmula TST 85
  t_clt_03_facts.lp         — fatos do cenário banco de horas CCT

Estrutura de cada facts.lp:
  % Fatos operacionais do cenário (alimentados pelo predictor)
  constitutional_basis("CF88_Art196").
  statutory_basis("Lei8080_Art7_I").
  hospital_occupancy_rate(0.92).          % para C2
  oxygen_days_remaining(1).              % para C2
  % etc.

### PASSO 4 — Teste de integração Clingo

Para cada cenário, verificar que o Clingo detecta a violação:
  clingo corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp \
         corpora_clingo/brasil/saude/sus_direito_saude.lp \
         corpora_clingo/brasil/emergencia_manaus/emergencia_sanitaria.lp \
         corpora_clingo/scenarios/c2_manaus_facts.lp

Resultado esperado: UNSATISFIABLE (constraint violado = Circuit Breaker)

Para T-CLT-03 (caso correto):
  clingo corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp \
         corpora_clingo/scenarios/t_clt_03_facts.lp

Resultado esperado: SATISFIABLE + hour_bank_valid_with_cct (theta < 30°)

### PASSO 5 — Reportar

Para cada arquivo criado:
  - Nome e número de linhas
  - Resultado do syntax-check Clingo
  - Lista de predicados sovereign() e elastic() definidos
  - Resultado do teste de integração (SAT/UNSAT conforme esperado)

---

## RESTRIÇÕES

- NÃO modificar os arquivos em corpora/ (documentos originais intocáveis)
- NÃO usar E1/E2/E3 automático para gerar estes predicados
- NÃO inventar dispositivos normativos — cada predicado tem âncora real
- Motor: Clingo ASP puro (sem dPASP)
- Encoding dos comentários: UTF-8

---

## REFERÊNCIA DE QUALIDADE

Os 4 arquivos já criados são o padrão de qualidade esperado:
  - Comentários com âncora normativa precisa (artigo, inciso)
  - Distinção clara sovereign() vs elastic()
  - Constraints (:- ) derivados dos predicados soberanos
  - Relevância explícita para os cenários Q-FENG

---

## CONTEXTO: SESSÃO OPUS 4 (paralela)

Uma sessão com Claude Opus 4 será aberta para validação jurídica
do corpus Clingo. O Opus revisará:
  1. Hierarquia normativa correta (CF > Lei > Portaria)
  2. Classificação sovereign/elastic juridicamente defensável
  3. Completude dos dispositivos por cenário
  4. Ausência de predicados inválidos ou anacrônicos

O Code implementa a estrutura técnica.
O Opus valida o conteúdo jurídico.
Ricardo aprova o resultado final.
