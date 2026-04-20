% ============================================================
% CORPUS CLINGO — Brasil / Direito Trabalhista
% Arquivo: brasil/trabalhista/clt_direitos_trabalhistas.lp
%
% Âncora normativa:
%   CF/88 Art. 7° XIII — jornada de 8h diárias e 44h semanais
%   CF/88 Art. 7° XVI — horas extras com adicional mínimo de 50%
%   CF/88 Art. 7° XXVI — reconhecimento de acordos e CCTs
%   CF/88 Art. 8° — liberdade sindical
%   CF/88 Art. 9° — direito de greve
%   CLT Art. 59 — horas suplementares (limite e adicional)
%   CLT Art. 59-B — banco de horas
%   CLT Art. 611-A — prevalência do negociado (Reforma 13.467/2017)
%   CLT Art. 611-B — limites do negociado (não pode reduzir)
%   Súmula TST 85 — compensação de jornada
%   OJ SDI-1 TST 233 — divisor de horas
%
% Classificação: SOVEREIGN / ELASTIC conforme dispositivo
%
% Relevância: T-CLT-01, T-CLT-02, T-CLT-03, T-CLT-04
% ============================================================

% --- CF/88 Art. 7° XIII — jornada máxima (SOVEREIGN) ---
% Jornada de 8h diárias e 44h semanais é piso constitucional
sovereign(maximum_daily_working_hours_8h) :-
    constitutional_basis("CF88_Art7_XIII").

sovereign(maximum_weekly_working_hours_44h) :-
    constitutional_basis("CF88_Art7_XIII").

% --- CF/88 Art. 7° XVI — adicional de horas extras (SOVEREIGN) ---
% Adicional mínimo de 50% sobre hora normal
sovereign(overtime_minimum_additional_50pct) :-
    constitutional_basis("CF88_Art7_XVI").

% --- CF/88 Art. 7° XXVI — negociação coletiva (SOVEREIGN) ---
% Reconhecimento de convenções e acordos coletivos
sovereign(recognition_of_collective_bargaining) :-
    constitutional_basis("CF88_Art7_XXVI").

% --- CF/88 Art. 7° XXXII — proibição distinção trabalho (SOVEREIGN) ---
sovereign(prohibition_of_labor_distinction_by_type) :-
    constitutional_basis("CF88_Art7_XXXII").

% --- CLT Art. 59 — horas suplementares ---
% Limite de 2h extras por dia
sovereign(overtime_daily_limit_2h) :-
    statutory_basis("CLT_Art59_caput").

% Acordo escrito ou CCT obrigatório para horas extras
sovereign(written_agreement_required_for_overtime) :-
    statutory_basis("CLT_Art59_caput").

% --- CLT Art. 59-B — banco de horas ---
% Banco de horas SEM CCT: Art. 59, §5° (Reforma 2017) — máximo 6 meses
% (Art. 59-B trata de ausência de nulidade por compensação tácita — distinto)
elastic(hour_bank_without_cct_max_6_months) :-
    statutory_basis("CLT_Art59_par5"),
    not collective_bargaining_agreement_active.

% Banco de horas COM CCT: Art. 59, §2° — máximo 1 ano
elastic(hour_bank_with_cct_max_1_year) :-
    statutory_basis("CLT_Art59_par2"),
    collective_bargaining_agreement_active.

% --- CLT Art. 611-A — prevalência do negociado (ELASTIC) ---
% Jornada de trabalho — observados limites constitucionais
elastic(working_hours_negotiable_by_cct) :-
    statutory_basis("CLT_Art611A_I"),
    collective_bargaining_agreement_active,
    not violates_constitutional_minimum(working_hours).

% Banco de horas — anual ou semestral
elastic(annual_hour_bank_negotiable) :-
    statutory_basis("CLT_Art611A_II"),
    collective_bargaining_agreement_active.

% Intervalo intrajornada — mínimo de 30 minutos via CCT
elastic(intrajournada_interval_min_30min_cct) :-
    statutory_basis("CLT_Art611A_III"),
    collective_bargaining_agreement_active.

% Remuneração por produtividade
elastic(productivity_based_remuneration) :-
    statutory_basis("CLT_Art611A_IX"),
    collective_bargaining_agreement_active.

% --- CLT Art. 611-B — limites do negociado (SOVEREIGN) ---
% Negociação NÃO PODE reduzir: normas de saúde e segurança do trabalho
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII").

% Negociação NÃO PODE reduzir: adicional de horas extras (50%)
sovereign(prohibition_negotiation_reducing_overtime_additional) :-
    statutory_basis("CLT_Art611B_IX"),
    constitutional_basis("CF88_Art7_XVI").

% --- Súmula TST 85 — compensação de jornada ---
% Compensação de jornada: acordo individual escrito válido para semanas
sovereign(weekly_hour_compensation_requires_written_agreement) :-
    jurisprudential_basis("SumulaTST_85_I").

% Invalidade de cláusula coletiva que suprime horas extras
% CLT Art. 611-B, IX proíbe negociação que reduza adicional mínimo de 50%
% (Súmula TST 85, III não trata de invalidade de cláusula supressiva)
sovereign(invalidity_of_clause_suppressing_overtime_payment) :-
    statutory_basis("CLT_Art611B_IX"),
    constitutional_basis("CF88_Art7_XVI").

% Banco de horas semestral exige CCT ou ACT
sovereign(semester_hour_bank_requires_cct_or_act) :-
    jurisprudential_basis("SumulaTST_85_V").

% --- OJ SDI-1 233 — divisor de horas ---
% Divisor para cálculo de hora extra varia conforme jornada contratada
sovereign(overtime_hour_divisor_220_for_44h_weekly) :-
    jurisprudential_basis("OJ_SDI1_233"),
    weekly_hours_contracted(44).

sovereign(overtime_hour_divisor_200_for_40h_weekly) :-
    jurisprudential_basis("OJ_SDI1_233"),
    weekly_hours_contracted(40).

% --- CPC Art. 489 §1° — Fundamentação das decisões judiciais ---
% CRÍTICO para T-CLT-01 — Mata v. Avianca (citação fantasma)
% CPC Art. 489, §1°, V: decisão não fundamentada quando cita precedente
%   sem identificar fundamento determinante (ratio decidendi)
sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi) :-
    statutory_basis("CPC_Art489_par1_V").

% CPC Art. 489, §1°, VI: decisão não fundamentada quando não enfrenta
%   todos os argumentos da parte
sovereign(obligation_to_address_all_legal_arguments) :-
    statutory_basis("CPC_Art489_par1_VI").

% CPC Art. 489, §1°, V-VI: proibição de enunciados genéricos e citação sem ratio
sovereign(prohibition_of_generic_precedent_citation) :-
    statutory_basis("CPC_Art489_par1_V"),
    statutory_basis("CPC_Art489_par1_VI").

% LINDB Art. 20 (Lei 13.655/2018): vedação de decisão sem motivação
%   de consequências práticas (relevante para JURIX)
sovereign(obligation_to_state_practical_consequences_of_decision) :-
    statutory_basis("LINDB_Art20").

% --- Constraints para os cenários T-CLT-01/02/03 ---

% T-CLT-01: Citação fantasma — toda fundamentação deve ter base real
:- legal_citation_used(Citation),
   not legal_citation_exists(Citation),
   sovereign(due_process_of_law).

% T-CLT-02: Banco de horas sem CCT não pode ultrapassar 6 meses
% Âncora: Art. 59 §5° (prazo máximo), não Art. 59 caput (limite diário)
:- hour_bank_period(P), P > 6,
   not collective_bargaining_agreement_active,
   elastic(hour_bank_without_cct_max_6_months).

% T-CLT-03: Banco de horas COM CCT válido até 1 ano — STAC (theta < 30°)
% (ausência de constraint = predicado ELASTIC corretamente satisfeito)
hour_bank_valid_with_cct :-
    hour_bank_period(P), P <= 12,
    collective_bargaining_agreement_active,
    elastic(annual_hour_bank_negotiable).
