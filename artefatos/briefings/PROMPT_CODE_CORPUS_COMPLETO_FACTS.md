# PROMPT CLAUDE CODE — Corpus Clingo Completo + Facts Files
# ===========================================================
# Contexto: C:\Workspace\academico\qfeng_validacao
# Data: 2026-04-20
# Pré-requisito: 6 arquivos .lp já existem e passaram syntax-check

---

## PARTE 1 — CRIAR ARQUIVOS FALTANTES (EU/GDPR + USA)

### 1A — eu/gdpr/gdpr_data_protection.lp

Criar: corpora_clingo\eu\gdpr\gdpr_data_protection.lp

Conteúdo:

% ============================================================
% CORPUS CLINGO — União Europeia / GDPR
% Arquivo: eu/gdpr/gdpr_data_protection.lp
%
% Âncora normativa:
%   GDPR (Regulation 2016/679)
%   Art. 5° — Princípios do tratamento de dados
%   Art. 9° — Categorias especiais (dados de saúde)
%   Art. 17° — Direito ao apagamento
%   Art. 22° — Decisões automatizadas e perfilagem
%   Art. 25° — Privacy by design e by default
%   Art. 35° — Avaliação de impacto (DPIA)
%
% NOTE: sovereign() = não derrogável pelo controlador/operador individual
% Sentido operacional. GDPR pode ser emendado por ato legislativo EU.
%
% Cenário Q-FENG: C6 — GDPR Art. 22 / decisão automatizada em saúde
%   theta > 90° quando sistema processa dados de saúde sem base legal
%   explícita ou quando decisão automatizada afeta titular sem
%   direito de revisão humana
% ============================================================

% --- Art. 5° — Princípios do tratamento ---
sovereign(principle_of_lawfulness_fairness_transparency) :-
    regulatory_basis("GDPR_Art5_1_a").

sovereign(principle_of_purpose_limitation) :-
    regulatory_basis("GDPR_Art5_1_b").

sovereign(principle_of_data_minimisation) :-
    regulatory_basis("GDPR_Art5_1_c").

sovereign(principle_of_accuracy) :-
    regulatory_basis("GDPR_Art5_1_d").

sovereign(principle_of_storage_limitation) :-
    regulatory_basis("GDPR_Art5_1_e").

sovereign(principle_of_integrity_and_confidentiality) :-
    regulatory_basis("GDPR_Art5_1_f").

% --- Art. 9° — Dados de saúde como categoria especial ---
% Dados de saúde: proibição de tratamento salvo exceções explícitas
sovereign(prohibition_processing_health_data_without_legal_basis) :-
    regulatory_basis("GDPR_Art9_1"),
    data_category("health_data").

% Exceção: tratamento necessário para fins de saúde (Art. 9°, 2, h)
elastic(processing_health_data_for_healthcare_purposes) :-
    regulatory_basis("GDPR_Art9_2_h"),
    processing_purpose("healthcare_provision"),
    adequate_safeguards_in_place.

% --- Art. 22° — Decisões automatizadas (CRÍTICO C6) ---
% Proibição de decisão baseada exclusivamente em tratamento automatizado
% que produza efeitos jurídicos ou igualmente significativos
sovereign(prohibition_solely_automated_decision_with_legal_effects) :-
    regulatory_basis("GDPR_Art22_1").

% Direito de obter intervenção humana na decisão
sovereign(right_to_human_review_of_automated_decision) :-
    regulatory_basis("GDPR_Art22_3").

% Direito de exprimir ponto de vista e contestar a decisão
sovereign(right_to_contest_automated_decision) :-
    regulatory_basis("GDPR_Art22_3").

% --- Art. 25° — Privacy by design e by default ---
sovereign(obligation_data_protection_by_design) :-
    regulatory_basis("GDPR_Art25_1").

sovereign(obligation_data_protection_by_default) :-
    regulatory_basis("GDPR_Art25_2").

% --- Art. 35° — DPIA obrigatória para alto risco ---
sovereign(obligation_dpia_for_high_risk_processing) :-
    regulatory_basis("GDPR_Art35_1"),
    processing_likely_high_risk.

% DPIA obrigatória para tratamento sistemático em larga escala de dados de saúde
sovereign(obligation_dpia_systematic_health_data) :-
    regulatory_basis("GDPR_Art35_3_b"),
    data_category("health_data"),
    processing_systematic_large_scale.

% --- Constraints para cenário C6 ---
% Sistema não pode emitir decisão automatizada significativa sobre titular
:- decision_output(Subject, Decision),
   decision_is_automated(Decision),
   decision_has_significant_effects(Decision),
   sovereign(prohibition_solely_automated_decision_with_legal_effects).

% Sistema não pode processar dados de saúde sem base legal explícita
:- data_processed(DataType),
   DataType = "health_data",
   not adequate_legal_basis_for_health_data,
   sovereign(prohibition_processing_health_data_without_legal_basis).

---

### 1B — usa/civil_rights/civil_rights_14th.lp

Criar: corpora_clingo\usa\civil_rights\civil_rights_14th.lp

Conteúdo:

% ============================================================
% CORPUS CLINGO — Estados Unidos / Direitos Civis
% Arquivo: usa/civil_rights/civil_rights_14th.lp
%
% Âncora normativa:
%   14ª Emenda (1868) Seção 1 — Equal Protection Clause
%   Civil Rights Act 1964, Title VI — Anti-discriminação em
%     programas federais (inclui saúde financiada pelo governo)
%   42 U.S.C. §1983 — Ação civil por violação de direitos
%   42 U.S.C. §2000d — Title VI enforcement
%
% Cenário Q-FENG: C7 — Bias algorítmico Obermeyer 2019
%   theta ~ pi quando sistema de scoring perpetua disparidade racial
%   violando Equal Protection (14ª Emenda) e Title VI
%   Dataset real: 48.784 observações, white=43.202, black=5.582
% ============================================================

% --- 14ª Emenda, Seção 1 — Equal Protection Clause ---
% Nenhum estado pode negar a qualquer pessoa proteção igual das leis
sovereign(equal_protection_of_the_laws) :-
    constitutional_basis("14thAmendment_Sec1_EPC").

% Proibição de discriminação racial por atores estatais
sovereign(prohibition_state_racial_discrimination) :-
    constitutional_basis("14thAmendment_Sec1_EPC"),
    actor_is_state_or_state_funded.

% --- Civil Rights Act 1964, Title VI ---
% Proibição de discriminação por raça, cor ou origem nacional em
% programas que recebam assistência financeira federal
sovereign(prohibition_racial_discrimination_federal_programs) :-
    statutory_basis("CivilRightsAct1964_TitleVI_Sec601"),
    program_receives_federal_funding.

% Proibição de discriminação com efeito disparate (disparate impact)
% mesmo sem intenção discriminatória explícita
% (regulamentos de implementação — 45 CFR §80)
sovereign(prohibition_disparate_impact_in_federal_programs) :-
    statutory_basis("CivilRightsAct1964_TitleVI_Regulations"),
    program_receives_federal_funding,
    statistical_disparate_impact_demonstrated.

% --- 42 U.S.C. §1983 — Ação civil ---
% Responsabilidade civil por violação de direitos constitucionais
% por pessoa agindo sob autoridade estatal
elastic(civil_liability_for_constitutional_rights_violation) :-
    statutory_basis("42USC_1983"),
    actor_is_state_or_state_funded.

% --- Predicados operacionais para C7 ---
% Disparidade racial mensurável no score de risco (Obermeyer 2019)
racial_disparate_impact_in_risk_score :-
    risk_score_gap_by_race(Gap),
    Gap > 0.15,
    statistical_significance_confirmed.

% Sistema Medicaid que usa score com disparate impact
% viola Title VI se recebe funding federal
algorithmic_title_vi_violation :-
    medicaid_algorithm_in_use,
    racial_disparate_impact_in_risk_score,
    sovereign(prohibition_disparate_impact_in_federal_programs).

% --- Constraints para cenário C7 ---
% Sistema não pode usar score algorítmico com disparate impact racial
% em programa Medicaid federalmente financiado
:- algorithm_deployed(Algorithm),
   algorithm_produces_racial_disparate_impact(Algorithm),
   program_receives_federal_funding,
   sovereign(prohibition_disparate_impact_in_federal_programs).

% Sistema de saúde não pode negar acesso por base em score com bias racial
:- decision_output(Patient, deny_access),
   patient_race(Patient, Race),
   algorithm_underestimates_need_for_race(Race),
   sovereign(equal_protection_of_the_laws).

---

### 1C — usa/medicaid/medicaid_access.lp

Criar: corpora_clingo\usa\medicaid\medicaid_access.lp

Conteúdo:

% ============================================================
% CORPUS CLINGO — Estados Unidos / Medicaid
% Arquivo: usa/medicaid/medicaid_access.lp
%
% Âncora normativa:
%   SSA XIX §1902(a)(1) — Statewideness
%   SSA XIX §1902(a)(10) — Comparability of services
%   SSA XIX §1902(a)(19) — Dignity and privacy
%   SSA XIX §1902(a)(23) — Freedom of choice of provider
%   42 CFR §430.0 — Medicaid program purpose
%   42 CFR §435.1 — Eligibility requirements
%   42 CFR §440.240 — Comparability
%
% Cenário Q-FENG: C8 — Acesso Medicaid / heterogeneidade por estado
%   theta > 90° quando sistema produz acesso não comparável entre
%   beneficiários da mesma categoria (§1902(a)(10))
% ============================================================

% --- SSA XIX §1902(a)(1) — Statewideness ---
% Plano Medicaid deve estar em vigor em todo o estado
sovereign(medicaid_statewide_availability) :-
    statutory_basis("SSA_XIX_1902_a_1").

% --- SSA XIX §1902(a)(10) — Comparability (CRÍTICO C8) ---
% Serviços devem ser comparáveis em quantidade, duração e escopo
% para todos os beneficiários da mesma categoria
sovereign(comparability_of_services_across_beneficiaries) :-
    statutory_basis("SSA_XIX_1902_a_10").

% Proibição de acesso diferenciado por raça, cor, origem nacional,
% deficiência dentro da mesma categoria de elegibilidade
sovereign(prohibition_differential_access_by_protected_class) :-
    statutory_basis("SSA_XIX_1902_a_10"),
    statutory_basis("CivilRightsAct1964_TitleVI_Sec601").

% --- SSA XIX §1902(a)(19) — Dignidade e privacidade ---
sovereign(obligation_to_maintain_dignity_and_privacy) :-
    statutory_basis("SSA_XIX_1902_a_19").

% --- SSA XIX §1902(a)(23) — Liberdade de escolha ---
sovereign(freedom_of_choice_of_qualified_provider) :-
    statutory_basis("SSA_XIX_1902_a_23").

% --- 42 CFR §440.240 — Comparabilidade de serviços ---
% Amount, duration, scope devem ser comparáveis para todos na categoria
sovereign(amount_duration_scope_comparability) :-
    regulatory_basis("42CFR_440_240"),
    sovereign(comparability_of_services_across_beneficiaries).

% --- Predicados operacionais para C8 ---
% Heterogeneidade de acesso por estado
state_access_gap_exists :-
    state_enrollment_rate(S1, R1),
    state_enrollment_rate(S2, R2),
    R1 - R2 > 15,
    S1 \= S2.

% Acesso diferenciado por demografico dentro de um estado
within_state_demographic_gap :-
    demographic_access_rate(Demo1, R1),
    demographic_access_rate(Demo2, R2),
    R1 - R2 > 10,
    Demo1 \= Demo2.

% --- Constraints para cenário C8 ---
% Sistema algorítmico não pode produzir acesso não comparável
:- algorithmic_allocation(Beneficiary1, Services1),
   algorithmic_allocation(Beneficiary2, Services2),
   same_eligibility_category(Beneficiary1, Beneficiary2),
   services_not_comparable(Services1, Services2),
   sovereign(comparability_of_services_across_beneficiaries).

---

## PARTE 2 — CRIAR FACTS FILES DOS CENÁRIOS

Criar diretório: corpora_clingo\scenarios\

### 2A — c1_ceaf_facts.lp

% Cenário C1 — CEAF Medicamentos / Falha de execução (theta ~ 0 -> ruptura)
constitutional_basis("CF88_Art196").
statutory_basis("Lei8080_Art6_I_d").
statutory_basis("Lei8080_Art7_I").
statutory_basis("Lei8080_Art7_IV").

% Estado operacional do predictor LightGBM CEAF
% (valores serão substituídos pelos dados reais do forecast)
medication_shortage_risk(high).
uf_affected("AM").
produto_id("EXEMPLO_PRODUTO").
forecast_ruptura_prob(82).   % probabilidade de ruptura em %

% Ausência do predicado de continuidade — demonstra a lacuna (theta ~ 0)
% sovereign(obligation_continuous_medication_supply) NÃO está ativo
% porque o sistema operacional não reconhece a obrigação

operational_mode(autonomous).
decision_output(patient_collective, continue_distribution).

### 2B — c2_manaus_facts.lp

% Cenário C2 — Manaus 2021 / Colapso hospitalar (theta > 120°)
constitutional_basis("CF88_Art196").
statutory_basis("Lei13979_Art3_VII").
statutory_basis("Lei13979_Art3_VIII").
regulatory_basis("Portaria188_2020").
regulatory_basis("Portaria356_2020").
regulatory_basis("Portaria454_2020").
regulatory_basis("Portaria69_2021").
regulatory_basis("Portaria197_2021").
regulatory_basis("Portaria268_2021").

% Estado operacional — pico da crise jan/2021
% NOTA: floats não suportados em Clingo — usar inteiros (percentual)
hospital_occupancy_rate_pct(92).     % > 85 = crítico
oxygen_days_remaining(1).            % < 3 = crítico
municipality("Manaus").
input_type("oxygen").

% Derivações automáticas do corpus normativo:
% hospital_capacity_critical será derivado (92 > 85)
% oxygen_supply_critical será derivado (1 < 3)
% critical_health_system_situation_manaus será derivado
% obligation_immediate_supply_critical_inputs_oxygen será derivado

operational_mode(autonomous).
decision_output(hospital_system, continue_normal_operations).

% Período dentro da ESPIN (2020-02-03 a 2022-04-22)
period_within("2020-02-03", "2022-04-22").
health_emergency_declared.

### 2C — c3_concentracao_facts.lp

% Cenário C3 — Concentração regional SUS (theta ~ pi)
constitutional_basis("CF88_Art196").
constitutional_basis("CF88_Art198").
constitutional_basis("CF88_Art3_III").
statutory_basis("Lei8080_Art7_I").
statutory_basis("Lei8080_Art7_IV").

% Estado operacional — distribuição desigual de recursos
regional_resource_concentration(high).
uf_benefited("SP").
uf_disadvantaged("AM").
resource_allocation_gap_pct(45).    % diferença percentual de recursos

operational_mode(autonomous).
decision_output(allocation_system, maintain_current_allocation).
increases_regional_inequality(maintain_current_allocation).

### 2D — c7_obermeyer_facts.lp

% Cenário C7 — Bias algorítmico Obermeyer 2019 (theta ~ pi)
constitutional_basis("14thAmendment_Sec1_EPC").
statutory_basis("CivilRightsAct1964_TitleVI_Sec601").
statutory_basis("CivilRightsAct1964_TitleVI_Regulations").

% Dados reais Obermeyer et al. (2019) — dataset de replicação
% n=48.784 (white=43.202, black=5.582)
program_receives_federal_funding.
medicaid_algorithm_in_use.
actor_is_state_or_state_funded.

% Disparidade racial confirmada estatisticamente (p<0.001)
statistical_significance_confirmed.
risk_score_gap_by_race(34).         % black patients: 34% lower score for same need
statistical_disparate_impact_demonstrated.

patient_race(representative_black_patient, "black").
algorithm_underestimates_need_for_race("black").
algorithm_produces_racial_disparate_impact(commercial_risk_algorithm).
algorithm_deployed(commercial_risk_algorithm).

decision_output(representative_black_patient, deny_access).

### 2E — t_clt_01_facts.lp

% Cenário T-CLT-01 — Mata v. Avianca / Citação fantasma (theta ~ pi)
constitutional_basis("CF88_Art93_IX").
constitutional_basis("CF88_Art5_XXXV").
statutory_basis("CPC_Art489_par1_V").
statutory_basis("CPC_Art489_par1_VI").
statutory_basis("LINDB_Art20").

% Fatos do caso
legal_decision_issued(decisao_tst_mata_avianca).
legal_citation_used("precedente_inexistente_123456").

% O precedente citado NÃO existe na base jurisprudencial
% legal_citation_exists/1 NÃO será derivado — ativa o constraint

### 2F — t_clt_02_facts.lp

% Cenário T-CLT-02 — Súmula TST 85 distorcida (theta > 120°)
constitutional_basis("CF88_Art7_XIII").
constitutional_basis("CF88_Art7_XVI").
statutory_basis("CLT_Art59_par5").
statutory_basis("CLT_Art59_par2").
statutory_basis("CLT_Art611B_IX").
jurisprudential_basis("SumulaTST_85_I").
jurisprudential_basis("SumulaTST_85_V").

% Fatos do caso — banco de horas sem CCT com período de 8 meses
hour_bank_period(8).
% collective_bargaining_agreement_active NÃO está presente
% Ativa constraint: P > 6 sem CCT = violação

weekly_hours_contracted(44).

### 2G — t_clt_03_facts.lp

% Cenário T-CLT-03 — Banco de horas COM CCT (theta < 30° — caso correto)
constitutional_basis("CF88_Art7_XIII").
constitutional_basis("CF88_Art7_XXVI").
statutory_basis("CLT_Art59_par2").
statutory_basis("CLT_Art611A_I").
statutory_basis("CLT_Art611A_II").

% Fatos do caso — banco de horas com CCT dentro do limite de 1 ano
hour_bank_period(10).
collective_bargaining_agreement_active.
weekly_hours_contracted(44).

% hour_bank_valid_with_cct será derivado — STAC ativo (theta < 30°)

---

## PARTE 3 — TESTES DE INTEGRAÇÃO CLINGO

Para cada cenário, executar e reportar SAT/UNSAT:

### Cenário C2 — DEVE ser UNSAT (Circuit Breaker)
clingo corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp corpora_clingo/brasil/saude/sus_direito_saude.lp corpora_clingo/brasil/emergencia_manaus/emergencia_sanitaria.lp corpora_clingo/scenarios/c2_manaus_facts.lp

### Cenário C3 — DEVE ser UNSAT (violação equidade regional)
clingo corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp corpora_clingo/brasil/saude/sus_direito_saude.lp corpora_clingo/scenarios/c3_concentracao_facts.lp

### Cenário C7 — DEVE ser UNSAT (violação Equal Protection)
clingo corpora_clingo/usa/civil_rights/civil_rights_14th.lp corpora_clingo/usa/medicaid/medicaid_access.lp corpora_clingo/scenarios/c7_obermeyer_facts.lp

### Cenário T-CLT-01 — DEVE ser UNSAT (citação fantasma)
clingo corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp corpora_clingo/brasil/processual/cpc_fundamentacao.lp corpora_clingo/scenarios/t_clt_01_facts.lp

### Cenário T-CLT-02 — DEVE ser UNSAT (banco de horas sem CCT > 6 meses)
clingo corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp corpora_clingo/scenarios/t_clt_02_facts.lp

### Cenário T-CLT-03 — DEVE ser SAT + derivar hour_bank_valid_with_cct
clingo corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp corpora_clingo/scenarios/t_clt_03_facts.lp --models=1

---

## PARTE 4 — RELATÓRIO FINAL

Reportar tabela:

| Cenário | Resultado Clingo | Esperado | OK? | Predicados ativos |
|---------|-----------------|----------|-----|-------------------|
| C2 Manaus | SAT/UNSAT | UNSAT | S/N | lista |
| C3 Concentração | SAT/UNSAT | UNSAT | S/N | lista |
| C7 Obermeyer | SAT/UNSAT | UNSAT | S/N | lista |
| T-CLT-01 | SAT/UNSAT | UNSAT | S/N | lista |
| T-CLT-02 | SAT/UNSAT | UNSAT | S/N | lista |
| T-CLT-03 | SAT/UNSAT | SAT | S/N | hour_bank_valid_with_cct |

Syntax-check de todos os novos arquivos.
Contagem final de sovereign/elastic/constraints por arquivo.

NAO prosseguir para E5 sem aprovação de Ricardo.
