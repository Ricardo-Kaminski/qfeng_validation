% ============================================================
% CORPUS CLINGO — Brasil / Direito Trabalhista
% Arquivo: brasil/trabalhista/clt_direitos_trabalhistas.lp
%
% Âncora normativa:
%   CF/88 Art. 7° XIII — jornada de 8h diárias e 44h semanais
%   CF/88 Art. 7° XV — repouso semanal remunerado
%   CF/88 Art. 7° XVI — horas extras com adicional mínimo de 50%
%   CF/88 Art. 7° XXII — redução de riscos inerentes ao trabalho (NRs)
%   CF/88 Art. 7° XXVI — reconhecimento de acordos e CCTs
%   CF/88 Art. 8° — liberdade sindical
%   CF/88 Art. 9° — direito de greve
%   CLT Art. 59 — horas suplementares (limite e adicional)
%   CLT Art. 59-B — banco de horas
%   CLT Art. 611-A — prevalência do negociado (Reforma 13.467/2017)
%   CLT Art. 611-B — limites do negociado (não pode reduzir)
%   CLT Art. 818 — ônus da prova trabalhista
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

% --- CF/88 Art. 7° XV — repouso semanal remunerado (SOVEREIGN) ---
% Repouso semanal remunerado, preferencialmente aos domingos.
% Piso constitucional trabalhista universal — incluído por completude
% pétrea, mesmo não sendo invocado pelos cenários T-CLT-* atuais.
sovereign(weekly_paid_rest) :-
    constitutional_basis("CF88_Art7_XV").

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
% Ancorado tanto em Art. 611-B XVII (estatutário) quanto em Art. 7° XXII
% CF/88 (constitucional — redução dos riscos inerentes ao trabalho).
% A dupla ancoragem garante que o predicado é pétreo no sentido forte:
% norma infraconstitucional sustentada por garantia constitucional explícita.
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII"),
    constitutional_basis("CF88_Art7_XXII").

% --- CF/88 Art. 7° XXII — redução de riscos do trabalho (SOVEREIGN) ---
% Base constitucional das normas regulamentadoras (NRs) e do princípio
% da redução de riscos inerentes ao trabalho por meio de normas de
% saúde, higiene e segurança.
sovereign(constitutional_obligation_to_reduce_labor_risks) :-
    constitutional_basis("CF88_Art7_XXII").

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

% --- CLT Art. 818 — Ônus da prova trabalhista ---
% Ônus da prova: incumbe ao reclamante quanto ao fato constitutivo
% de seu direito; ao reclamado quanto à existência de fato impeditivo,
% modificativo ou extintivo do direito do reclamante.
% §1°: nos casos de difícil produção de prova ou maior facilidade de
% obtenção pela parte contrária, o juízo poderá atribuir o ônus
% diversamente, decisão fundamentada nos termos do CPC Art. 489.
% Estruturalmente decisivo para T-CLT-01/02 — articula-se com o dever
% de fundamentação: a redistribuição do ônus exige motivação explícita.
sovereign(burden_of_proof_default_distribution) :-
    statutory_basis("CLT_Art818_caput").

elastic(burden_of_proof_redistribution_with_motivation) :-
    statutory_basis("CLT_Art818_par1"),
    statutory_basis("CPC_Art489_par1_V").

% --- Predicados de fundamentação processual (CPC + LINDB) ---
% Os predicados sobre fundamentação de decisões judiciais (CPC Art. 489 §1°
% e LINDB Art. 20) estão centralizados em corpora_clingo/brasil/processual/
% cpc_fundamentacao.lp para evitar duplicação. Os cenários T-CLT-* invocam
% esses predicados via inclusão do arquivo de fundamentação processual.
%
% Predicados disponibilizados pelo cpc_fundamentacao.lp:
%   - obligation_to_ground_decision_in_identified_ratio_decidendi
%     (CPC Art. 489 §1° V)
%   - obligation_to_address_all_legal_arguments (CPC Art. 489 §1° VI)
%   - prohibition_of_generic_precedent_citation (V + VI combinados)
%   - obligation_to_state_practical_consequences_of_decision (LINDB Art. 20)

% --- Constraints para os cenários T-CLT-01/02/03 ---

% T-CLT-01: Citação fantasma — toda fundamentação deve ter base real
:- legal_citation_used(Citation),
   not legal_citation_exists(Citation),
   sovereign(due_process_of_law).

% T-CLT-02: Banco de horas sem CCT não pode ultrapassar 6 meses
% Âncora: Art. 59 §5° (prazo máximo), não Art. 59 caput (limite diário)
% NOTE: P em meses (unidade canônica de hour_bank_period/1)
:- hour_bank_period(P), P > 6,
   not collective_bargaining_agreement_active,
   elastic(hour_bank_without_cct_max_6_months).

% T-CLT-03: Banco de horas COM CCT válido até 1 ano — STAC (theta < 30°)
% (ausência de constraint = predicado ELASTIC corretamente satisfeito)
% NOTE: P em meses (unidade canônica de hour_bank_period/1)
hour_bank_valid_with_cct :-
    hour_bank_period(P), P <= 12,
    collective_bargaining_agreement_active,
    elastic(annual_hour_bank_negotiable).
