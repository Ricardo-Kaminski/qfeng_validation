# Auditoria Semântica do Corpus Clingo Q-FENG

**Data:** 26 de abril de 2026
**Escopo:** Auditoria sistemática dos arquivos `.lp` sob `corpora_clingo/` cobrindo as duas frentes ativas de validação simbólica — **Saúde** (CF/88, Lei 8080/1990, Lei 13.979/2020, Decreto AM 43.303/2021, Portarias GM/MS 188/356/454/197/79/2020-2021) e **Trabalhista** (CF/88 Art. 7° e 8°, CLT Arts. 59, 59-B, 611-A, 611-B, 818, Súmulas TST 85, OJ SDI-1 233, CPC Art. 489 §1°, LINDB Art. 20).
**Modus operandi:** Auditoria semântica conduzida em sessão Opus 4.7; aplicação operacional executada por Claude Code local (OpusPlan); validação dogmática intermediária via checkpoint Opus.
**Branch:** `caminho2`
**Commit principal:** `49808c4`
**Validação final:** 7 cenários ativos × 7/7 aprovados em `scripts/validate_clingo_corpus.py` sem regressão.

---

## 1. Sumário executivo

Esta auditoria consolidou 14 auditorias acumuladas no corpus Clingo do Q-FENG, organizadas em quatro classes: **(A) lacunas estruturais** com impacto epistêmico nos cenários ativos, **(B) anti-padrões de engenharia normativa**, **(C) cobertura tipológica incompleta**, e **(D) refinamentos de constraint**. Cinco das 14 auditorias são novas desta rodada (C-5, LAW-BR-05 a LAW-BR-09); as demais estavam previamente registradas e foram revalidadas no escopo da auditoria sistemática.

Adicionalmente, fixou-se uma decisão de escopo: o cenário **C1 CEAF** (predictor LightGBM aplicado a previsão de ruptura de medicamentos) foi **descartado do conjunto canônico de cenários de validação simbólica do Q-FENG**. A engenharia ML para CEAF permanece operacional como artefato de pipeline, mas não alimenta o motor simbólico. O arquivo `c1_ceaf_facts.lp` foi movido para `corpora_clingo/_deprecated/` com header explicativo para preservação histórica, e a cobertura normativa da assistência farmacêutica integral (Lei 8080/1990 Art. 6° I d) foi mantida em `sus_direito_saude.lp` como base dogmática aplicável a futuros cenários de saúde envolvendo continuidade de medicação.

O conjunto canônico de cenários ativos pós-auditoria é:

| Cenário | Domínio | Regime esperado | Falha modelada |
|---|---|---|---|
| **C2** Manaus 2021 | Saúde / Brasil | UNSAT (CIRCUIT_BREAKER) | execution_absent_channel |
| **C3** Concentração regional SUS | Saúde / Brasil | UNSAT (CIRCUIT_BREAKER) | constitutional |
| **C7** Obermeyer 2019 / Medicaid | Saúde / USA | UNSAT (CIRCUIT_BREAKER) | constitutional |
| **T-CLT-01** Mata v. Avianca / citação fantasma | Trabalhista / Brasil | UNSAT (CIRCUIT_BREAKER) | execution_inertia |
| **T-CLT-02** Súmula TST 85 distorcida (banco de horas sem CCT > 6m) | Trabalhista / Brasil | UNSAT (CIRCUIT_BREAKER) | execution_absent_channel |
| **T-CLT-03** Banco de horas com CCT (controle, 10m) | Trabalhista / Brasil | SAT (STAC) | — |
| **T-CLT-04** Citação fundamentada (controle positivo) | Trabalhista / Brasil | SAT (STAC) | — |

---

## 2. Topologia da arquitetura normativa

O corpus está organizado em três camadas hierárquicas, com a seguinte estrutura de diretórios (após auditoria):

```
corpora_clingo/
├── _deprecated/
│   └── c1_ceaf_facts.lp                # Fora do pipeline ativo (rastro histórico)
├── brasil/
│   ├── constitucional/
│   │   └── cf88_principios_fundamentais.lp
│   ├── saude/
│   │   └── sus_direito_saude.lp
│   ├── emergencia_manaus/
│   │   └── emergencia_sanitaria.lp
│   ├── processual/
│   │   └── cpc_fundamentacao.lp
│   └── trabalhista/
│       ├── clt_direitos_trabalhistas.lp
│       └── tst_decisoes/
├── eu/
│   ├── ai_act/
│   │   └── eu_ai_act_obligations.lp
│   └── gdpr/
│       └── gdpr_data_protection.lp
├── usa/
│   ├── civil_rights/
│   │   └── civil_rights_14th.lp
│   └── medicaid/
│       └── medicaid_access.lp
└── scenarios/
    ├── c2_manaus_facts.lp
    ├── c3_concentracao_facts.lp
    ├── c7_obermeyer_facts.lp
    ├── t_clt_01_facts.lp
    ├── t_clt_02_facts.lp
    ├── t_clt_03_facts.lp
    └── t_clt_04_facts.lp
```

A topologia em três camadas espelha a hierarquia formal do direito positivo brasileiro:

- **Camada 1 — Constitucional (`cf88_principios_fundamentais.lp`):** princípios pétreos (CF/88 Art. 60 §4°), fundamentos da República (Art. 1°), objetivos fundamentais (Art. 3°), direitos e garantias fundamentais (Art. 5°), competência comum em saúde (Art. 23 II — adicionado nesta rodada). Predicados desta camada são `sovereign/1` no sentido pétreo formal ou estruturante.

- **Camada 2 — Estatutária e regulamentar:**
  - Saúde: `sus_direito_saude.lp` (CF/88 Arts. 196, 197, 198, 200; Lei 8080/1990 Arts. 2°, 6°, 7°, 15)
  - Emergência sanitária: `emergencia_sanitaria.lp` (Lei 13.979/2020; Portarias GM/MS; Decreto AM 43.303/2021)
  - Processual: `cpc_fundamentacao.lp` (CF/88 Art. 93 IX; CPC Art. 489 §1° I-VI; LINDB Art. 20)
  - Trabalhista: `clt_direitos_trabalhistas.lp` (CF/88 Art. 7°; CLT Arts. 59, 59-B, 611-A, 611-B, 818; Súmulas e OJ TST)
  - Predicados desta camada são `sovereign/1` quando ancorados constitucionalmente, `elastic/1` quando moduláveis por instrumento infralegal.

- **Camada 3 — Cenários (`scenarios/`):** instâncias factuais que invocam predicados das camadas 1 e 2 e fornecem os fatos operacionais (estados de ocupação hospitalar, períodos de banco de horas, decisões emitidas, citações usadas) que disparam constraints e produzem o veredito SAT/UNSAT.

A separação entre camadas é metodologicamente importante porque implementa a hierarquia normativa kelseniana de forma operacional: constraints disparadas na camada constitucional não podem ser derrogadas por predicados da camada infralegal, e instâncias na camada de cenários não podem instanciar fatos que contradigam o que está positivado nas camadas superiores.


---

## 3. Pendências por classe

### 3.1 Classe A — Lacunas estruturais

Foram identificadas cinco lacunas estruturais com impacto direto sobre a robustez epistêmica dos cenários ativos:

**A.1 — Art. 200 II CF/88 (vigilância epidemiológica e sanitária).** Toda a cadeia normativa do C2 Manaus funda-se na vigilância epidemiológica detectando anomalia → ESPIN ativando-se → Decreto AM 43.303/2021 declarando calamidade → obrigações de fornecimento sendo disparadas. O Art. 200 II é a base constitucional dessa cadeia, mas estava ausente do corpus. Sem ele, a fundamentação constitucional do cenário C2 era incompleta — um revisor com perfil constitucionalista detectaria a omissão imediatamente. **Resolução:** dois predicados adicionados em `sus_direito_saude.lp`: `sovereign(obligation_epidemiological_surveillance)` e `sovereign(obligation_sanitary_surveillance)`, ambos ancorados em `constitutional_basis("CF88_Art200_II")`.

**A.2 — Art. 23 II CF/88 (competência comum União-Estados-Municípios em saúde).** Sustenta a articulação federativa entre o Decreto AM 43.303/2021 (estadual) e a Portaria GM/MS 79/2021 (federal). Especialmente relevante após a ADI 6341/STF (16-24/abr/2020), que consolidou a leitura de competência concorrente para medidas sanitárias durante emergências de saúde pública. **Resolução:** `sovereign(common_competence_health_federal_state_municipal)` adicionado em `cf88_principios_fundamentais.lp` com nota dogmática explícita: o Art. 23 não é cláusula pétrea formal (Art. 60 §4° não o lista), mas é norma constitucional estruturante da federação sanitária. A classificação `sovereign/1` aqui assume sentido de "constitucional-aplicável", não pétreo stricto sensu — distinção paralela à dos Arts. 1° e 3°.

**A.3 — Art. 7° XXII CF/88 (redução de riscos do trabalho).** O predicado `prohibition_negotiation_reducing_health_safety` estava ancorado apenas em `CLT_Art611B_XVII` (statutário). Sem ancoragem ao Art. 7° XXII (constitucional), a sovereignty do predicado era dogmaticamente frágil — uma norma infraconstitucional não pode ser pétrea sozinha. **Resolução:** dupla ancoragem aplicada — o predicado agora exige conjunção de `statutory_basis("CLT_Art611B_XVII")` E `constitutional_basis("CF88_Art7_XXII")`. Adicionalmente, `sovereign(constitutional_obligation_to_reduce_labor_risks)` foi adicionado como predicado autônomo, base constitucional explícita das Normas Regulamentadoras (NRs).

**A.4 — Art. 196 CF/88 condensado em duas cláusulas com mesma chave.** O texto pleno do Art. 196 contém três núcleos normativos distintos: direito-dever, redução de risco via políticas sociais e econômicas, e acesso universal igualitário. O `.lp` original colapsava esses núcleos em duas cláusulas com a mesma chave `constitutional_basis("CF88_Art196")`. Essa condensação tornava-se especialmente problemática para o **Caminho 2** (BI multi-fonte): o argumento epistemológico de que TOH + SRAG + O₂ medem precisamente "risco de doença e outros agravos" no sentido constitucional precisa ancorar-se no segundo núcleo do Art. 196, que estava implícito mas não identificado. **Resolução:** três predicados independentes — `right_to_health_as_duty_of_state`, `obligation_reduce_disease_risk_via_social_economic_policies`, `universal_equal_access_to_health_services` — todos ancorados em `constitutional_basis("CF88_Art196")` mas semanticamente desdobrados.

**A.5 — Lei 8080/1990 Art. 15 I referenciada mas não implementada.** O predicado `obligation_immediate_supply_critical_inputs_oxygen` em `emergencia_sanitaria.lp` invocava `statutory_basis("Lei8080_1990_Art15_I")`, mas o predicado correspondente não existia no corpus. Era um link quebrado — o Clingo tolerava (não dispara erro porque o `statutory_basis/1` é apenas asserido como fato), mas a integridade conceitual estava comprometida. **Resolução:** `sovereign(common_competence_health_control_evaluation_oversight)` adicionado em `sus_direito_saude.lp`, ancorado em `statutory_basis("Lei8080_1990_Art15_I")`.

### 3.2 Classe B — Anti-padrões de engenharia normativa

**B.1 — Duplicação de predicados CPC entre `cpc_fundamentacao.lp` e `clt_direitos_trabalhistas.lp`.** Quatro predicados apareciam definidos em ambos os arquivos: `obligation_to_ground_decision_in_identified_ratio_decidendi`, `obligation_to_address_all_legal_arguments`, `prohibition_of_generic_precedent_citation`, `obligation_to_state_practical_consequences_of_decision`. O Clingo tolera por idempotência (mesma regra produzindo mesmo predicado), mas é violação do princípio DRY normativo: quando um dos arquivos for atualizado (e.g., adicionar Art. 489 §1° I-IV), o outro ficará dessincronizado. **Resolução:** predicados centralizados em `cpc_fundamentacao.lp`; em `clt_direitos_trabalhistas.lp`, o bloco original foi substituído por comentário de referência apontando para o arquivo central.

**B.2 — Limiares operacionais (R > 85% e D < 3 dias) sem âncora documental.** Os predicados `hospital_capacity_critical :- hospital_occupancy_rate_pct(R), R > 85` e `oxygen_supply_critical :- oxygen_days_remaining(D), D < 3` estavam implementados sem documentação da proveniência institucional dos limiares. Isto é especialmente problemático porque alimentam diretamente a derivação de `critical_health_system_situation_manaus` e, a partir dela, todas as obrigações disparadas no C2. Um revisor epidemiologista (perfil Sabino, Orellana) perguntaria de onde vêm os limiares; sem resposta documental, o cenário ficaria exposto. **Resolução:**

- Limiar de TOH > 85%: documentado como ancorado na **Ficha Técnica de Indicadores da Atenção Hospitalar do MS** (TOH UTI, elaborada pela CGAH/DAHU/SAES/MS — autor Ricardo Kaminski), com convergência com a literatura crítica brasileira (AMIB) que classifica TOH > 85% como saturação operacional. A nota dogmática inline explicita esse contexto institucional.
- Limiar de oxigênio: documentado via referência ao precedente operacional Manaus 2021 (comunicação White Martins ao MS em 14/jan/2021 sobre impossibilidade de reposição em 24-48h). O limiar de 3 dias é janela de antecedência mínima para acionamento de requisição emergencial (Lei 13.979/2020 Art. 3° VII) ou reorganização logística. Adicionalmente, o limiar foi parametrizado como fato configurável (`oxygen_critical_threshold_days(3)`), permitindo ajuste sem modificação do predicado lógico.

### 3.3 Classe C — Cobertura tipológica incompleta

**C.1 — CPC Art. 489 §1° I-IV ausentes.** Apenas os incisos V e VI estavam implementados. Os incisos I-IV compõem juntos a tipologia completa de "decisão não fundamentada":
- I — paráfrase de ato normativo sem explicação de incidência;
- II — emprego de conceitos jurídicos indeterminados sem grounding;
- III — motivação genérica que serviria a qualquer decisão (boilerplate);
- IV — não enfrentamento de argumentos deduzidos.

O inciso III é particularmente crítico para o eixo de auditoria de decisões algorítmicas geradas por LLM, porque é precisamente esse tipo de motivação genérica que sistemas de geração automática tendem a produzir. **Resolução:** quatro predicados adicionados em `cpc_fundamentacao.lp` — `prohibition_of_normative_act_paraphrase_without_explanation`, `prohibition_of_indeterminate_legal_concepts_without_grounding`, `prohibition_of_generic_template_motivation`, `prohibition_of_ignoring_deduced_arguments`. Nota dogmática inline explicita a distinção entre §1° IV ("argumentos deduzidos no processo") e §1° VI (regra geral de enfrentamento), que jurisprudencialmente são tratados em conjunto mas textualmente são incisos distintos.

**C.2 — Art. 7° XV CF/88 (repouso semanal remunerado).** Ausente do corpus, embora seja piso constitucional trabalhista universal. Não impacta os cenários T-CLT-01 a 04 atuais, mas é completude pétrea importante para futuras extensões. **Resolução:** `sovereign(weekly_paid_rest)` adicionado.

**C.3 — CLT Art. 818 (ônus da prova).** Ausente. Estruturalmente decisivo para T-CLT-01 e T-CLT-02 porque articula-se com o dever de fundamentação (CPC Art. 489 §1°): a redistribuição do ônus de prova trabalhista (Art. 818 §1°) exige motivação explícita nos termos do CPC. **Resolução:** dois predicados adicionados — `sovereign(burden_of_proof_default_distribution)` (regra geral) e `elastic(burden_of_proof_redistribution_with_motivation)` (redistribuição via §1° condicionada à motivação CPC 489 §1° V).

**C.4 — Lei 13.979/2020 Art. 3° §7° (dispensa de licitação emergencial).** Ausente. Completa a cadeia jurídica do C2: Estado pode requisitar (Art. 3° VII) e adquirir sem licitação (Art. 3° §7°), garantindo base legal completa para a obrigação de fornecimento imediato de O₂. **Resolução:** `sovereign(authorization_to_dispense_bidding_in_emergency)` adicionado em `emergencia_sanitaria.lp`, condicionado a `health_emergency_declared`.

### 3.4 Classe D — Refinamentos de constraint

**D.1 — Constraint `regional_allocation` muito específica.** O constraint final em `sus_direito_saude.lp` disparava apenas se a action fosse literalmente `regional_allocation`, ignorando qualquer outra decisão algorítmica que produzisse desigualdade regional. **Resolução:** generalizada para `:- decision_output(_, Action), increases_regional_inequality(Action), sovereign(equity_in_health_assistance)` — análoga ao constraint correspondente em `cf88_principios_fundamentais.lp`.

**D.2 — Constraint T-CLT-01 cobre apenas citação fantasma stricto sensu.** A constraint disparava quando `legal_citation_used(Citation), not legal_citation_exists(Citation)`. Mas o CPC Art. 489 §1° V proíbe também a citação de precedente real **sem identificação da ratio decidendi** (precedent-mining sem fundamentação). **Resolução:** constraint complementar adicionada em `cpc_fundamentacao.lp` com guard explícito (`ratio_decidendi_required(Citation)`), de forma que só dispara quando o cenário declara explicitamente a exigência de identificação de ratio. Em closed-world default, a constraint fica "armada" mas só dispara quando um cenário fornece o fato negativo.

**D.3 — Comentários de unidade temporal em `hour_bank_period`.** As constraints com `P > 6` e `P <= 12` não documentavam inline a unidade. **Resolução:** comentários `% NOTE: P em meses (unidade canônica de hour_bank_period/1)` adicionados.


---

## 4. Auditorias acumuladas (registro consolidado)

A tabela abaixo consolida as 14 auditorias acumuladas no corpus. Auditorias preexistentes foram revalidadas; as cinco marcadas com [novo] são desta rodada.

| Audit | Escopo | Objeto | Status |
|---|---|---|---|
| C-1 | Wrapper sovereign() / átomo plano | `espin_declaration_active`, `espin_renewed_jan2021`, `obligation_expand_medical_workforce_manaus_pandemic` | Revalidada |
| C-3 | Remoção de constraint UNSAT espúrio | `decision_grounded_in_identified_precedent/1` em `cpc_fundamentacao.lp` (closed-world `not P` com P indefinido) | Revalidada |
| C-4 | Substituição Portaria 69/2021 → Decreto AM 43.303/2021 | Portaria 69/2021 trata de registro vacinas SI-PNI, não de calamidade hospitalar | Revalidada |
| **C-5** | Desdobramento Art. 196 em três núcleos | `right_to_health_as_duty_of_state`, `obligation_reduce_disease_risk_via_social_economic_policies`, `universal_equal_access_to_health_services` | **Novo** |
| C-6 | Substituição TST-RR-000200-50.2019.5.02.0020 (fabricado) → TST-Ag-RR-868-65.2021.5.13.0030 (real) | T-CLT-04 controle positivo | Revalidada |
| F0-1 | Detecção de citação sintética | Audit do precedente fabricado em T-CLT-04 anterior | Revalidada |
| H-5 | Remoção Portaria 268/2021 | Portaria SE/MS 29/jun/2021 sobre metas de servidores — sem relação com Manaus | Revalidada |
| H-6 | Scope guard Lei8080_Art7_I | Restringe constraint de `deny_access` ao regime SUS/health-access | Revalidada |
| LAW-BR-04 | Renomeação predicado Mais Médicos | `obligation_additional_response_measures` → `obligation_expand_medical_workforce_manaus_pandemic` | Revalidada |
| **LAW-BR-05** | Ancoragem dupla Art. 611-B XVII + Art. 7° XXII | `prohibition_negotiation_reducing_health_safety` agora pétreo no sentido forte | **Novo** |
| **LAW-BR-06** | Implementação Lei 8080 Art. 15 I | Link quebrado consertado: `common_competence_health_control_evaluation_oversight` | **Novo** |
| **LAW-BR-07** | Deduplicação CPC | Predicados §1° centralizados em `cpc_fundamentacao.lp`, removidos do `clt_direitos_trabalhistas.lp` | **Novo** |
| **LAW-BR-08** | Documentação dos limiares operacionais | TOH > 85% (Ficha Técnica MS/AMIB); oxygen days < 3 (precedente Manaus 2021); parametrização configurável | **Novo** |
| **LAW-BR-09** | Cobertura tipológica CPC §1° I-IV | Quatro predicados adicionais cobrindo paráfrase, conceitos indeterminados, boilerplate, ignorar deduzidos | **Novo** |

---

## 5. Validação integrada

### 5.1 Syntax-checks individuais

Todos os arquivos do corpus foram validados via `clingo --syntax-check`:

```
clingo --syntax-check corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp  → OK
clingo --syntax-check corpora_clingo/brasil/saude/sus_direito_saude.lp                       → OK
clingo --syntax-check corpora_clingo/brasil/emergencia_manaus/emergencia_sanitaria.lp        → OK
clingo --syntax-check corpora_clingo/brasil/processual/cpc_fundamentacao.lp                  → OK
clingo --syntax-check corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp         → OK
clingo --syntax-check corpora_clingo/_deprecated/c1_ceaf_facts.lp                            → OK
```

### 5.2 Validação por cenário

O script `scripts/validate_clingo_corpus.py` executa cada cenário ativo carregando o conjunto canônico de arquivos `.lp` que ele invoca, e checa contra o regime SAT/UNSAT esperado:

```
========================================================================
VALIDAÇÃO INTEGRADA DO CORPUS CLINGO Q-FENG — 26/abr/2026
========================================================================

[OK] C2_Manaus: UNSAT (esperado: UNSAT)
[OK] C3_Concentracao: UNSAT (esperado: UNSAT)
[OK] C7_Obermeyer: UNSAT (esperado: UNSAT)
[OK] T_CLT_01_Mata_Avianca: UNSAT (esperado: UNSAT)
[OK] T_CLT_02_Sumula85_Distorcida: UNSAT (esperado: UNSAT)
[OK] T_CLT_03_Banco_Horas_CCT: SAT (esperado: SAT)
[OK] T_CLT_04_Citacao_Fundamentada: SAT (esperado: SAT)

========================================================================
TODOS OS 7 CENÁRIOS VALIDADOS COM SUCESSO.
========================================================================
```

**Zero regressões introduzidas pelas correções.** Os cenários de circuit-breaker permanecem UNSAT (constraints disparadas corretamente), e os controles positivos permanecem SAT (predicados ELASTIC satisfeitos sem violação de constraints SOVEREIGN).

---

## 6. Discussão dogmática das auditorias significativas

Esta seção desenvolve em maior profundidade as auditorias que envolvem decisões dogmaticamente densas — aquelas em que a engenharia normativa precisou navegar tensões entre fidelidade textual, robustez metodológica, e operacionalidade computacional.

### 6.1 Audit C-5 — Desdobramento do Art. 196 CF/88 e fundamentação epistemológica do Caminho 2

O Art. 196 da Constituição Federal estabelece: *"A saúde é direito de todos e dever do Estado, garantido mediante políticas sociais e econômicas que visem à redução do risco de doença e de outros agravos e ao acesso universal e igualitário às ações e serviços para sua promoção, proteção e recuperação."*

A leitura sistemática reconhece três núcleos normativos distintos no enunciado: (i) **direito-dever** (estrutura subjetiva-objetiva: direito de todos / dever do Estado); (ii) **redução de risco de doença e outros agravos** mediante políticas sociais e econômicas; (iii) **acesso universal e igualitário** às ações e serviços de saúde para promoção, proteção e recuperação.

Na implementação original do `.lp`, esses três núcleos estavam colapsados em duas cláusulas com a mesma chave `constitutional_basis("CF88_Art196")` — uma para o direito-dever, outra para o acesso universal. O segundo núcleo (redução de risco) ficava implícito mas não identificado.

Esse colapso era especificamente problemático para o **Caminho 2 (BI multi-fonte)**, que reconstrói o predictor de Manaus combinando TOH + SRAG + O₂ como série temporal. O argumento epistemológico de defesa do BI é: essas três séries medem precisamente "risco de doença e outros agravos" no sentido do segundo núcleo do Art. 196 — TOH mede o risco de saturação assistencial, SRAG mede o risco epidemiológico de evolução grave, O₂ mede o risco logístico-terapêutico. Sem o predicado autônomo `obligation_reduce_disease_risk_via_social_economic_policies`, a defesa teria que se ancorar em interpretação livre do texto constitucional, frágil sob escrutínio de revisor.

Com o desdobramento aplicado, o argumento ganha estrutura: o predictor BI é instrumento computacional para medir o cumprimento do segundo núcleo do Art. 196 — relação direta entre texto constitucional e arquitetura técnica. Esta é a forma mais robusta de defender a escolha metodológica do Caminho 2 perante revisores constitucionalistas ou de saúde pública.

### 6.2 Audit C-4 — A Portaria 69/2021 e o problema da granularidade documental

A versão anterior do `emergencia_sanitaria.lp` invocava `regulatory_basis("Portaria69_2021")` como uma das fontes regulamentares do C2 Manaus. Auditoria documental revelou que a Portaria GM/MS 69/2021 trata de registro de vacinas no SI-PNI (Sistema de Informações do Programa Nacional de Imunizações) — não de calamidade hospitalar nem de obrigações de fornecimento de insumos.

Esta auditoria é particularmente instrutiva porque ilustra um **modo de falha característico de pipelines LLM-assistidos de extração normativa**: o modelo de extração (E2 do Q-FENG, baseado em few-shots de Qwen 2.5) retornou a Portaria 69/2021 como artefato relevante porque ela aparece em contextos próximos de "COVID-19" e "Manaus" no corpus de treino (registro de vacinação durante a pandemia, território amazônico). A relevância **temática** foi capturada, mas a relevância **deôntica** (a portaria não institui obrigação relevante para o cenário) não foi. A correção passou pela substituição por `Decreto AM 43.303/2021` — que é o instrumento normativo efetivo da declaração de calamidade pública estadual no Amazonas em 23/jan/2021.

Esta é precisamente a função da **HITL Sovereignty Classification (E4)** no pipeline Q-FENG: não como fase decorativa, mas como filtro semântico-jurídico indispensável. Predicados extraídos por LLM precisam ser validados contra o conteúdo deôntico real do instrumento normativo, não apenas contra sua co-ocorrência temática. A Audit C-4 fornece o caso paradigmático que justifica metodologicamente o esforço de revisão humana sistemática dos 537 predicados saúde + 145 predicados trabalhistas amostrados.

### 6.3 Audit F0-1 / C-6 — TST-RR fabricado e o problema das alucinações no controle positivo

A versão anterior do T-CLT-04 (controle positivo) invocava o precedente `TST-RR-000200-50.2019.5.02.0020`. Auditoria revelou que esse número de processo era **fabricado** — não existe na base do TST. A fabricação foi gerada durante uma fase anterior de prototipagem em que se buscava um precedente plausível para o controle, e a alucinação passou pelas validações iniciais porque o formato (TST-RR-NNN-NN.AAAA.5.UF.NNNN) é sintaticamente válido.

A correção (Audit C-6) substituiu o precedente pelo **TST-Ag-RR-868-65.2021.5.13.0030** — acórdão real da 2ª Turma do TST, publicado no DEJT de 06/12/2023, tratando de CCT de bancários articulada com o Tema 1046/STF (ARE 1.121.633). Este é o precedente real que sustenta dogmaticamente o controle positivo do T-CLT-04 (decisão fundamentada com precedente verificável e ratio identificada).

Esta auditoria tem uma dimensão **especialmente crítica** porque o T-CLT-04 é o **controle positivo** do experimento. Se o controle positivo é instanciado com precedente fabricado, a falsificabilidade de todo o framework Q-FENG fica comprometida: como distinguir um cenário SAT genuíno de um cenário SAT que aparenta ser válido apenas porque a alucinação não foi detectada? A Audit F0-1 documenta o protocolo de detecção (cross-referência com bases públicas do TST + verificação de número do processo), e a C-6 documenta a substituição. A combinação garante que o controle positivo do framework é **falsificável e auditável** — propriedade essencial para qualquer sistema de validação científica.

A lição metodológica é direta: alucinações de LLM não se restringem a contextos óbvios (citações em texto livre); podem aparecer em estruturas sintaticamente válidas (números de processo bem formatados) que passam por filtros de regex mas não por validação de existência. Para Q-FENG e para qualquer pipeline NeSy operando sobre corpus jurídico, **detecção de alucinações de citação requer cross-referência sistemática contra bases públicas autoritativas**, não apenas validação sintática.

### 6.4 Audit LAW-BR-05 — Dupla ancoragem e o problema da pétrea sustentada por norma infraconstitucional

A versão anterior do `clt_direitos_trabalhistas.lp` declarava:

```prolog
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII").
```

Esta formulação tem fragilidade dogmática: `sovereign/1` aqui é assumido a partir de uma única âncora estatutária (norma infraconstitucional). Mas norma infraconstitucional não é pétrea por si — ela pode ser revogada ou modificada por outra norma infraconstitucional. A "pétrea-fortaleza" exigida pela classificação `sovereign/1` no sentido forte requer ancoragem constitucional.

A correção (LAW-BR-05) aplica **dupla ancoragem**:

```prolog
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII"),
    constitutional_basis("CF88_Art7_XXII").
```

O Art. 7° XXII CF/88 estabelece "redução dos riscos inerentes ao trabalho, por meio de normas de saúde, higiene e segurança". A combinação `CLT_Art611B_XVII ∧ CF88_Art7_XXII` produz uma cadeia formal: a norma infraconstitucional (Art. 611-B XVII) é blindada como pétrea porque sustenta um direito que tem âncora constitucional explícita (Art. 7° XXII). A cadeia não pode ser rompida pelo legislador ordinário — qualquer revogação do Art. 611-B XVII deixaria intacto o Art. 7° XXII, e este ainda forneceria base constitucional para a proibição.

Esta é a versão computacional do raciocínio kelseniano: a sovereignty de uma norma de hierarquia inferior só é estável se houver ancoragem em norma de hierarquia superior. A engenharia do corpus deve refletir essa estrutura — não basta declarar `sovereign/1` mecanicamente; é preciso garantir que a cadeia de fundamentação chega a uma norma constitucional. A LAW-BR-05 institui esse padrão e abre espaço para que outras pétreas-aparentes sejam revisadas sob o mesmo critério.

### 6.5 Audit LAW-BR-08 — Limiares operacionais e a interface entre direito e dado empírico

Os predicados `hospital_capacity_critical :- hospital_occupancy_rate_pct(R), R > 85` e `oxygen_supply_critical :- oxygen_days_remaining(D), D < 3` definem **limiares quantitativos** que disparam derivações normativas. O problema é: de onde vêm esses números?

Esta é uma das tensões mais delicadas em qualquer sistema NeSy aplicado ao direito: o texto normativo formal (CF/88, Lei 8080, Lei 13.979) raramente especifica limiares numéricos; quem especifica são os **instrumentos infralegais técnicos** (fichas técnicas, portarias, manuais de boas práticas) e a **literatura técnica especializada**. O corpus precisa documentar essa cadeia de fundamentação para que os limiares não pareçam arbitrários.

A LAW-BR-08 implementa essa documentação:

- **TOH > 85%:** ancorada na **Ficha Técnica de Indicadores da Atenção Hospitalar do MS** (TOH UTI), elaborada pela Coordenação-Geral de Atenção Hospitalar / DAHU / SAES / MS. Há convergência com a literatura crítica brasileira (AMIB — Associação de Medicina Intensiva Brasileira) que classifica TOH > 85% como saturação operacional — estado em que o tempo de espera por leito UTI cresce não-linearmente e a mortalidade por priorização inadequada aumenta significativamente. O autor do Q-FENG é também autor da ficha técnica MS, o que dá ancoragem institucional direta.

- **Oxygen days < 3:** ancorada no **precedente operacional Manaus 2021**. White Martins comunicou ao Ministério da Saúde em 14/jan/2021 que não conseguiria repor estoque em 24-48h, configurando ponto de não-retorno operacional. O limiar de 3 dias estabelece janela de antecedência mínima para acionamento de requisição emergencial (Lei 13.979/2020 Art. 3° VII) ou reorganização logística (transporte aéreo, redirecionamento de pacientes).

Adicionalmente, o limiar de oxigênio foi parametrizado como fato configurável: `oxygen_critical_threshold_days(3).` Isso permite ajuste sem modificação do predicado lógico — se em outro cenário (e.g., outra unidade federativa, outro tipo de insumo) o limiar canônico for diferente, basta alterar o fato. A separação entre **predicado lógico** (regra) e **fato paramétrico** (valor) é boa engenharia normativa: torna o código auditável e adaptável sem perder fundamentação documental.

A lição mais ampla da LAW-BR-08 é: **um corpus normativo que opera sobre dados empíricos precisa documentar a proveniência de seus limiares** com o mesmo rigor com que documenta a proveniência de seus predicados. A interface direito ↔ dado é onde sistemas NeSy mais frequentemente falham silenciosamente, porque o leitor humano automaticamente assume que limiares "óbvios" (85%, 3 dias) refletem consenso técnico — quando na verdade refletem decisões institucionais específicas que precisam ser explicitadas para serem auditáveis.


---

## 7. Documentação derivada

Esta auditoria gera três artefatos documentais, com finalidades distintas:

1. **Este relatório** (`artefatos/auditorias/AUDITORIA_CORPUS_CLINGO_26abr2026.md`): documento técnico interno em PT, registro completo da auditoria com diagnóstico, patches aplicados, validação e discussão dogmática.

2. **Apêndice candidato acadêmico** (`docs/papers/paper1/_apendices/apendice_corpus_clingo.md`): versão polida em EN, voltada para incorporação ao Paper 1 ou anexação separada no pré-print Zenodo. Pode compor com os outros apêndices já existentes (`Apendice_Secao_3.docx`, `Apendice_Secao_4.docx`, `Apendice_Secao_5.docx`, `Apendice_Secao_6.docx`).

3. **Notas metodológicas para incorporação ao canônico** (`artefatos/notas_metodologicas/NOTAS_CORPUS_CLINGO_para_canonico.md`): snippets atômicos em EN com indicação de seção-alvo no `PAPER1_CANONICO.md` e diff completo para aplicação via `edit_block`. Cobre §2.7 (Theoretical context), §4 (Pipeline E2-E4), §5 (Validation Results), §7.4 (Limitations).

A política editorial canônica do projeto Q-FENG estabelece que pré-print Zenodo aceita material extenso integral ou múltiplos anexos sem restrição de páginas. Restrições editoriais específicas (limites de páginas, formato, idioma) só serão aplicadas no momento da submissão a journal/evento concreto (JURIX 2026, AI & Law, JAIR, Lancet Digital Health, npj Digital Medicine).

---

## 8. Pendências pós-auditoria

Esta auditoria não esgota todo o trabalho normativo do Q-FENG. Pendências identificadas que não foram tratadas nesta rodada e ficam registradas para sessões futuras:

**8.1 — Auditoria sistemática dos sub-corpora EU e USA.** Os arquivos `eu/ai_act/eu_ai_act_obligations.lp`, `eu/gdpr/gdpr_data_protection.lp`, `usa/civil_rights/civil_rights_14th.lp`, `usa/medicaid/medicaid_access.lp` foram **fora do escopo** desta auditoria, que focou no domínio brasileiro. Auditoria semântica análoga deve ser conduzida sobre eles antes da submissão internacional do Paper 1, com **revisão adicional do `c7_obermeyer_facts.lp`** (verificando os 28.8pp contra Obermeyer et al. 2019 Table 2). Decisão de escopo já tomada (26/abr/2026): execução em paralelo silencioso ao Caminho 2; resultados são reincorporados na fase de regeneração dos outputs.

**8.2 — Tradução EN do corpus para Layer S5 internacional.** A maior parte do corpus está em PT (com identificadores de predicado em EN). Para o Paper 1 (target JURIX/AI&Law/JAIR — audiência internacional) e para o Layer S5 do Q-FENG (governance metanormativa multijurisdicional), uma tradução cuidadosa do conteúdo dos comentários e das notas dogmáticas é necessária. Estimativa preliminar: 6-12 meses como linha de pesquisa preparatória.

**8.3 — Implementação de raciocínio defeasível.** A versão atual do corpus encoda obrigações como hard ASP facts, deferindo o tratamento formal de defeasibility (exceções, prioridade hierárquica de normas, distinção forte/fraca de permissões — Governatori et al. 2013) para a suíte completa de governança. Esta limitação é declarada explicitamente em §7.4 do Paper 1 e é metodologicamente deliberada para o estágio PoC; mas para a versão de produção, a integração com defeasible deontic logic é necessária.

**8.4 — Cobertura de jurisprudência além das Súmulas TST.** As Súmulas 85 e a OJ SDI-1 233 estão implementadas, mas a base jurisprudencial trabalhista é muito mais ampla (Súmulas 90 — adicional noturno, 366 — minutos residuais, 423 — turnos ininterruptos, OJ SDI-1 297, OJ SDI-1 308, etc.). Expansão progressiva conforme cenários adicionais forem instanciados.

**8.5 — Arbitragem de conflitos norma-norma.** Quando dois predicados sovereign entram em colisão (e.g., direito ao trabalho vs. saúde do trabalhador, ou direito à saúde vs. princípio orçamentário), o corpus atual não fornece mecanismo de arbitragem — o Clingo simplesmente retornaria UNSAT. A implementação de regras de arbitragem (lex posterior, lex specialis, ponderação principiológica) é necessária para cenários de maior complexidade.

---

## 9. Reprodutibilidade

**Workspace canônico:** `C:\Workspace\academico\qfeng_validacao\` (conda env `qfeng`).
**Branch:** `caminho2`.
**Commit principal desta auditoria:** `49808c4`.
**Script de validação:** `scripts/validate_clingo_corpus.py` (executável via `conda run -n qfeng python scripts/validate_clingo_corpus.py`).
**Versão Clingo:** Potassco 5.8.

**Para reproduzir a validação completa:**

```cmd
cd C:\Workspace\academico\qfeng_validacao
git checkout caminho2
git log -1 --oneline                  # deve mostrar 49808c4 ou descendente
conda activate qfeng
python scripts\validate_clingo_corpus.py
```

A saída esperada é `TODOS OS 7 CENÁRIOS VALIDADOS COM SUCESSO`.

---

*Fim do relatório.*

*Documento produzido em sessão Opus 4.7 (chat) e gravado por Claude Code local em `artefatos/auditorias/AUDITORIA_CORPUS_CLINGO_26abr2026.md` em 26/abr/2026, branch `caminho2`.*
