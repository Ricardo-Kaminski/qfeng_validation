% ============================================================
% CORPUS CLINGO — União Europeia / GDPR
% Arquivo: eu/gdpr/gdpr_data_protection.lp
%
% Âncora normativa:
%   GDPR (Regulation 2016/679)
%   Art. 5° — Princípios do tratamento de dados
%   Art. 9° — Categorias especiais (dados de saúde)
%   Art. 22° — Decisões automatizadas e perfilagem
% (Art. 17° direito ao apagamento: referenciado no header anterior mas sem
%  implementação de regra — removido do header; future work para C6 extendido)
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
