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
    Gap > 15,
    statistical_significance_confirmed.

% Sistema Medicaid que usa score com disparate impact
% viola Title VI se recebe funding federal
algorithmic_title_vi_violation :-
    medicaid_algorithm_in_use,
    racial_disparate_impact_in_risk_score,
    sovereign(prohibition_disparate_impact_in_federal_programs).

% Violação derivada de Title VI via cadeia racial_disparate_impact → UNSAT (audit C-2)
:- algorithmic_title_vi_violation.

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
