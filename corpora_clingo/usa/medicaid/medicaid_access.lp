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
    S1 != S2.

% Acesso diferenciado por demografico dentro de um estado
within_state_demographic_gap :-
    demographic_access_rate(Demo1, R1),
    demographic_access_rate(Demo2, R2),
    R1 - R2 > 10,
    Demo1 != Demo2.

% --- Constraints para cenário C8 ---
% Sistema algorítmico não pode produzir acesso não comparável
:- algorithmic_allocation(Beneficiary1, Services1),
   algorithmic_allocation(Beneficiary2, Services2),
   same_eligibility_category(Beneficiary1, Beneficiary2),
   services_not_comparable(Services1, Services2),
   sovereign(comparability_of_services_across_beneficiaries).
