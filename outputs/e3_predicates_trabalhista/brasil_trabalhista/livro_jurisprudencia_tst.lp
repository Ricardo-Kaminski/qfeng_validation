% atom_id: 9663f97b112087be | chunk: 139f2dc34cf3e90d | strength: regulatory
obligated(employer, worker, calculate_salary_hour_with_divisor_220).

% atom_id: 61ec5831e52dc417 | chunk: 16a822b38f2fdd61 | strength: regulatory
obligated(employer, worker, remunerate_unused_rest_period) :-
    work_hours_exceeded(six_hours).

% atom_id: c874e6d4175521f9 | chunk: 16c3ad0d2a105d96 | strength: statutory
prohibited(worker, contract, enter_into).

% atom_id: cdc556b686daef2d | chunk: 184f9a07f37b72e2 | strength: statutory
obligated(employer, worker, provide_intra_shift_rest_break).

% atom_id: f2228209fd009eb7 | chunk: 1ecda30f2920c9de | strength: statutory
obligated(employer, worker, conduct_concours_public_for_promotion).

% atom_id: 29052e9dc13999be | chunk: 1f2c6e97f3219c9d | strength: statutory
obligated(employer, employee, provide_legal_assistance_to_watchmen).

% atom_id: 989b7c16b8015b89 | chunk: 1f2c6e97f3219c9d | strength: statutory
obligated(employer, employee, grant_cash_box_bonus).

% atom_id: 61a6901347c616e4 | chunk: 1f2c6e97f3219c9d | strength: statutory
obligated(employer, employee, display_notice_board).

% atom_id: c0024204540db17f | chunk: 1f2c6e97f3219c9d | strength: statutory
obligated(employer, employee, provide_legal_representation).

% atom_id: 99546505c3453c6d | chunk: 1f2c6e97f3219c9d | strength: statutory
obligated(employer, employee, provide_legal_representation_for_civil_action).

% atom_id: 1e9abd73d0774845 | chunk: 1f2c6e97f3219c9d | strength: statutory
obligated(employer, employee, provide_legal_representation_for_civil_public_action).

% atom_id: b3500ebae101ad33 | chunk: 2070e67d616cd2d6 | strength: regulatory
prohibited(employer, worker, deduct_from_salary_without_authorization) :-
    percentage_of_deduction(X_0), X_0 > 70.

% atom_id: 9ab9297c2bd51336 | chunk: 2070e67d616cd2d6 | strength: regulatory
prohibited(sindicato, worker, collect_contribution_from_non_sindicalized_workers).

% atom_id: c0e8127a9f0daf97 | chunk: 2070e67d616cd2d6 | strength: regulatory
prohibited(sindicato, employer, establish_preference_for_sindicalized_workers_in_hiring).

% atom_id: b4d2ee55ee92d3f4 | chunk: 2070e67d616cd2d6 | strength: regulatory
obligated(sindicato, worker, seek_authorization_for_collective_dispute) :-
    workers_involved_in_conflict(directly_affected).

% atom_id: 2c93eaa19d7e1a70 | chunk: 2070e67d616cd2d6 | strength: regulatory
obligated(sindicato, sector_professional_and_economic, ensure_correspondence_of_activities_in_conflict_resolution).

% atom_id: 2896efed1030e7f9 | chunk: 2070e67d616cd2d6 | strength: regulatory
prohibited(sindicato, segment_professional_or_patronal, represent_unified_category_in_separate_segments).

% atom_id: 1ca5d11daae75cd9 | chunk: 232430ecd0af5bc2 | strength: statutory
obligated(employer, worker, provide_perilous_work_compensation) :-
    work_environment(electrical_power_system),
    risk_level(high).

% atom_id: ba71c1d25ec8bd51 | chunk: 232430ecd0af5bc2 | strength: statutory
obligated(employer, worker, participate_in_salary_adjustment_negotiation) :-
    salary_increase_type(real).

% atom_id: 8fc3c0ed92e2737e | chunk: 232430ecd0af5bc2 | strength: statutory
obligated(employer, worker, record_time_for_uniform_change_lunch_and_personal_hygiene) :-
    time_spent(X_0), X_0 >= 10.

% atom_id: 44cda768f2a37ba3 | chunk: 232430ecd0af5bc2 | strength: statutory
obligated(justice_of_labor, worker, resolve_moral_damage_disputes) :-
    damage_origin(work_relationship).

% atom_id: b632208c1aa230bc | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(employer, worker, equalize_salaries_without_same_function) :-
    job_functions(different).

% atom_id: ad005a1229d9d90d | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(employer, worker, terminate_stability_period_without_company_closure) :-
    company_status(closed).

% atom_id: 9e125ca8353f3a26 | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(employer, worker, submit_representation_before_authorization) :-
    representation_status(unauthorized).

% atom_id: 46f0a84673b2bfe9 | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(employer, worker, require_specific_powers_for_inadequacy_declaration) :-
    declaration_type(economic_insufficiency).

% atom_id: 20d9bcc69a6b4962 | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(employer, worker, use_tacografo_as_only_time_control_method) :-
    work_activity(external).

% atom_id: 372ae0df99b870bc | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(employer, worker, change_shift_pattern_to_fixed_hours_without_legal_permission) :-
    legal_provision(article_10_of_law_5811).

% atom_id: 19218f4afea68953 | chunk: 232430ecd0af5bc2 | strength: statutory
prohibited(public_administration, worker, submit_voluntary_regular_recourse_without_previous_interposi) :-
    recourse_type(ordinary).

% atom_id: 5548a6e98292b8f7 | chunk: 36602cde1474156b | strength: statutory
obligated(employer, worker, provide_minimum_rest_period).

% atom_id: e4fb9ac12b771f51 | chunk: 381ebb665a5a7843 | strength: regulatory
obligated(employer, worker, pay_extra_hours_notional_value) :-
    hour_type(extra),
    work_environment(port).

% atom_id: 01c7c23dfcc20673 | chunk: 381ebb665a5a7843 | strength: regulatory
obligated(employer, worker, calculate_extra_hours_based_on_basic_salary) :-
    work_environment(port).

% atom_id: 9d015e8c3c8b78d6 | chunk: 381ebb665a5a7843 | strength: regulatory
prohibited(employer, worker, include_risk_and_productivity_additions_in_extra_hours_calcu) :-
    work_environment(port).

% atom_id: eeba346e1fe661a0 | chunk: 3a71c74c14b77ed2 | strength: statutory
obligated(parte_recorrente, none, depositar_multa_aplicada_previamente).

% atom_id: 6fb62f64f1b90dcc | chunk: 3c956c81cbc81eea | strength: statutory
obligated(court, litigant, require_absence_of_controversy_on_fact) :-
    controversy_status(absent).

% atom_id: 103bb4da17c2dee8 | chunk: 3c956c81cbc81eea | strength: statutory
obligated(court, litigant, require_judicial_statement_of_evidence) :-
    judicial_statement_status(present).

% atom_id: e7462ad529a3a45c | chunk: 41b09cd376c07a73 | strength: statutory
obligated(employer, worker, provide_minimum_rest_interval) :-
    work_hours(X_0), X_0 >= 6.

% atom_id: 061a7c2f36e908b3 | chunk: 41b09cd376c07a73 | strength: statutory
obligated(employer, worker, compensate_unenjoyed_rest_interval_as_overtime) :-
    work_hours(X_0), X_0 >= 6,
    rest_interval_provided(false).

% atom_id: fc654fa1788e36cb | chunk: 501bacc21488c029 | strength: statutory
obligated(employer, pregnant_worker, pay_stability_indemnity) :-
    knowledge_of_pregnancy_status_by_employer(unknown).

% atom_id: 4f2dd58812fd5d6e | chunk: 501bacc21488c029 | strength: statutory
obligated(employer, pregnant_worker, communicate_pregnancy_status_to_employer) :-
    collective_agreement(exists),
    time_after_rescission(specified_period_in_collective_agreement).

% atom_id: e8cb0f1760f65b37 | chunk: 501bacc21488c029 | strength: statutory
prohibited(employer, pregnant_worker, deny_stability_indemnity_payment) :-
    collective_agreement(exists),
    communication_of_pregnancy_status(not_received_by_employer_within_specified_period).

% atom_id: deeae35558cf0f33 | chunk: 5f852f4b3fff7fb2 | strength: statutory
obligated(employer, worker, pay_double_holiday_wages) :-
    holiday_payment_timing(on_time).

% atom_id: e2448c548e1953e0 | chunk: 5f852f4b3fff7fb2 | strength: statutory
prohibited(employer, worker, condition_participation_in_profits_on_contract_status) :-
    contract_termination_date(profit_distribution_date).

% atom_id: 0a33193b9b5a7b6a | chunk: 5f852f4b3fff7fb2 | strength: statutory
obligated(employer, worker, pay_proportional_participation_in_profits) :-
    contract_termination_date(profit_distribution_date).

% atom_id: c94b353e61d57a3d | chunk: 5f852f4b3fff7fb2 | strength: statutory
obligated(employer, worker, pay_proportional_salary_differences) :-
    promotion_criteria_observed(false).

% atom_id: ea7766832b914f52 | chunk: 5f852f4b3fff7fb2 | strength: statutory
prohibited(employer, worker, require_perilous_work_proof_without_payment) :-
    perilous_work_payment_status(spontaneous).

% atom_id: d1869b4dce2b47df | chunk: 5f852f4b3fff7fb2 | strength: statutory
obligated(justice_of_labor, state, execute_social_contribution_automatically) :-
    contribution_type(work_accident_insurance).

% atom_id: 550c97a21f2019e9 | chunk: 5f852f4b3fff7fb2 | strength: statutory
permitted(mixed_economy_company, worker, equalize_salaries) :-
    employment_status(under_clt).

% atom_id: 1130972b3c758eca | chunk: 64f14df2ce93dd65 | strength: statutory
prohibited(employer, worker, discriminate_based_on_health_status) :-
    disease(hiv),
    disease(grave_disease).

% atom_id: 1a40371c22c4ce3a | chunk: 64f14df2ce93dd65 | strength: statutory
permitted(employer, worker, implement_12_by_36_work_schedule) :-
    work_agreement_type(collective_bargaining).

% atom_id: ec59afc0c3d6e1fc | chunk: 64f14df2ce93dd65 | strength: statutory
prohibited(employer, worker, pay_extra_hours_for_11th_and_12th_hour_work) :-
    work_schedule(n12_by_36).

% atom_id: b8be655ac4b56ac6 | chunk: 64f14df2ce93dd65 | strength: statutory
prohibited(employer, worker, apply_civil_law_fruits_of_misuse_to_unpaid_wages) :-
    unpaid_rights_type(wage).

% atom_id: 8929092e136b504f | chunk: 64f14df2ce93dd65 | strength: statutory
obligated(employer, worker, pay_extra_hours_for_suppressed_breaks) :-
    work_position(railway_operator).

% atom_id: 6efdcd87bac5e375 | chunk: 678ac14706dfdfc7 | strength: statutory
obligated(employer, worker, pay_overtime_for_sunday_and_holiday_work) :-
    work_schedule(turn_shifts).

% atom_id: 50efd66ffa5d8f07 | chunk: 678ac14706dfdfc7 | strength: statutory
prohibited(employer, none, unilaterally_suppress_overtime_payment) :-
    work_schedule(turn_shifts),
    payment_frequency(monthly).

% atom_id: b709853e68c40921 | chunk: 678ac14706dfdfc7 | strength: statutory
prohibited(employer, none, retroactively_apply_collective_agreement_to_suppress_overtim) :-
    work_schedule(turn_shifts),
    payment_frequency(monthly).

% atom_id: 2d0cefe38e8210ba | chunk: 7879d8be720fcb3f | strength: regulatory
obligated(employer, state, reimburse_contributions_from_judicial_award) :-
    judgment_outcome(employee_credit).

% atom_id: e856be0212b49888 | chunk: 7879d8be720fcb3f | strength: regulatory
obligated(employer, state, reimburse_fiscal_contributions_from_judicial_award) :-
    judgment_outcome(employee_credit).

% atom_id: 4785626d7ba08b2e | chunk: 7879d8be720fcb3f | strength: regulatory
obligated(labor_judiciary, state, order_reimbursement_of_contributions_from_sentences).

% atom_id: 54aecf4e8af1f672 | chunk: 7879d8be720fcb3f | strength: regulatory
obligated(labor_judiciary, state, execute_contributions_from_sentences).

% atom_id: ace2029e5ea29af3 | chunk: 7886936d5d983a5a | strength: constitutional
obligated(state, public_administration, conduct_public_competition).

% atom_id: 8d9ee8fd75f49613 | chunk: 7b1bb7301269203a | strength: statutory
obligated(tribunal, process, decide_merit_of_case) :-
    process_conditions(in_order).

% atom_id: 62e98bb7ec61341a | chunk: 7f366e749b22c02c | strength: constitutional
prohibited(state, worker, prevent_salary_equivalence) :-
    employment_type(public).

% atom_id: 255f1c401c0d0d6b | chunk: 7f366e749b22c02c | strength: constitutional
permitted(mixed_economy_company, worker, grant_salary_equivalence) :-
    employment_type(private).

% atom_id: ba27dc064319c306 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empresa, empregado, pode_descontar_da_remuneracao_mensal).

% atom_id: 2ce5bfb58d3d2c1a | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empresa, empregado, deve_pagar_em_dobro_o_trabalho_em_domingos_e_feriados_nao_co).

% atom_id: 0eda0d57ec79c7de | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_reembolso_das_despesas_de_alimentacao_e_perno).

% atom_id: cbc3172cfffde5ad | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_pagamento_do_salario_mediante_recibo).

% atom_id: 15be6e6190a7f0d2 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_direito_aos_salarios_dos_primeiros_15_dias_de).

% atom_id: c496f188916cab87 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_direito_a_ausencia_remunerada_de_1_um_dia_por).

% atom_id: 5240b432ba7be9b9 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_direito_de_reducao_de_2_horas_no_comeco_ou_no).

% atom_id: c04ad1e27731476c | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_indenizacao_correspondente_a_1_um_dia_de_sala).

% atom_id: 7d9eb7619366ac1d | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_integralmente_o_salario_da_nova_funcao).

% atom_id: 82689902ac389205 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_pagamento_do_salario_em_dobro_do_trabalho_not).

% atom_id: 9acc3ecddcf8d08d | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_direito_ao_acesso_as_empresas_nos_intervalos).

% atom_id: 2746742fc774debc | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_repouso_remunerado_quando_chegar_atrasado_e_p).

% atom_id: 05ff2bc04daa2569 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_direito_ao_inicio_das_ferias_coletivas_ou_ind).

% atom_id: 51fdf16f1fbd114c | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_o_direito_ao_seguro_de_vida_em_favor_do_emprega).

% atom_id: 441bb630985b2ff8 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_emprego_durante_os_12_meses_que_a).

% atom_id: a9b5d04d31cd11c9 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_emprego_para_o_representante_com).

% atom_id: ec3214db8d79d6f9 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_repouso_remunerado_quando_chegar).

% atom_id: f81fdc7f42c0d8a9 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_inicio_das_ferias_coletivas_ou_in).

% atom_id: f97dcad03c26baf0 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_seguro_de_vida_em_favor_do_empreg).

% atom_id: d0e7ca6a2c35c047 | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_emprego_durante_os_12_meses_que_a).

% atom_id: 409f849c8597a67f | chunk: 8d7164aba3e84077 | strength: statutory
obligated(empregado, empresa, deve_receber_a_garantia_de_emprego_para_o_representante_com).

% atom_id: cbc536415fbbdb44 | chunk: 992a1e5b600ddeaf | strength: regulatory
obligated(employer, employee, provide_notice_period_during_compensatory_leave) :-
    circumstance(special_circumstances),
    company(csn).

% atom_id: d57716b1b8cf29dc | chunk: 992a1e5b600ddeaf | strength: regulatory
obligated(employer, employee, incorporate_participation_in_profits_as_salary_component) :-
    date_of_incorporation(X_0), X_0 <= 1988.

% atom_id: 53c0f5d316241262 | chunk: 992a1e5b600ddeaf | strength: regulatory
obligated(employer, employee, submit_necessary_documents_for_judgment) :-
    law_vigency_date(X_0), X_0 >= 1998.

% atom_id: 3cc15bff0a51e662 | chunk: 992a1e5b600ddeaf | strength: regulatory
obligated(employer, employee, attach_certificate_of_publication_for_temporal_judgment) :-
    law_vigency_date(X_0), X_0 >= 1998.

% atom_id: c9191c924b57de2d | chunk: 992a1e5b600ddeaf | strength: regulatory
obligated(employer, employee, attach_certificate_of_publication_for_temporal_judgment_exce) :-
    law_vigency_date(X_0), X_0 >= 1998,
    document_inclusion(present_in_records).

% atom_id: 1d037e0a8aad3961 | chunk: 992a1e5b600ddeaf | strength: regulatory
obligated(employer, employee, attach_necessary_documents_for_controversy_understanding) :-
    law_vigency_date(X_0), X_0 >= 1998.

% atom_id: 7943ca6bedaa3b97 | chunk: 9cc67a42885ab80b | strength: regulatory
obligated(employer, employee, comply_with_contractual_obligations).

% atom_id: 30bf21f5ebae77f5 | chunk: 9cc67a42885ab80b | strength: regulatory
obligated(employee, employer, prove_absence_of_work_due_to_holiday) :-
    holiday_type(local_or_judicial).

% atom_id: 9838a3e0e4ec250f | chunk: 9cc67a42885ab80b | strength: regulatory
prohibited(employee, court, file_late_power_of_attorney_in_appellate_court).

% atom_id: 96805477f7ce7e01 | chunk: aaabe70a2851d9b0 | strength: regulatory
obligated(employer, worker, calculate_fine_on_ftgs_balance) :-
    payment_status(rescission_benefits_payment),
    fine_percentage(n40).

% atom_id: e733e878c800f881 | chunk: ac206a6213be39c7 | strength: regulatory
obligated(employer, worker, provide_intra_workday_break) :-
    job_role(maquinista),
    category(c).

% atom_id: 9b6455d1c89fa1a1 | chunk: b46995c3be53df93 | strength: statutory
prohibited(state, public_finance, sequester_public_funds_for_precatorios) :-
    preterition_of_creditor_precedence_right(false).

% atom_id: 40762ffcf25eb40b | chunk: b46995c3be53df93 | strength: statutory
prohibited(tribunal_superior_do_trabalho, mandado_de_seguranca, original_jurisdiction) :-
    decision_origin(trt).

% atom_id: bd9de5221da5a763 | chunk: b46995c3be53df93 | strength: statutory
prohibited(tribunal_superior_do_trabalho, recourse, original_jurisdiction) :-
    decision_origin(aggravated_regimental_remand).

% atom_id: f5817bcd87e28759 | chunk: b46995c3be53df93 | strength: statutory
prohibited(judiciary, condemnation_effect, extend_condemnation_effects_beyond_1990_law) :-
    law_application_date(n1990_12_11).

% atom_id: 579e64186efa6461 | chunk: b46995c3be53df93 | strength: statutory
obligated(state, judgment_condemnation, apply_interest_rates_according_to_criteria) :-
    condemnation_date(X_0), X_0 <= 2001.

% atom_id: 2d986b204c1d8a94 | chunk: bdb0dd3a4bc8243f | strength: statutory
obligated(employer, worker, provide_provisional_stability).

% atom_id: 98e2746faaca23f0 | chunk: bdb0dd3a4bc8243f | strength: statutory
obligated(court, litigant, grant_legal_advocacy_fees) :-
    legal_action_type(indemnity_claim),
    cause_of_action(work_accident_occupational_disease).

% atom_id: c88905d688d29f9b | chunk: bdb0dd3a4bc8243f | strength: statutory
obligated(court, litigant, transfer_case_to_labor_judiciary) :-
    legal_action_type(indemnity_claim),
    cause_of_action(work_accident_occupational_disease),
    court_decision_date(X_2), X_2 > 2004.

% atom_id: 2cc59a036f260ae5 | chunk: c14135d509987bdf | strength: statutory
prohibited(employer, worker, recognize_vinculo_empregaticio_posterior_1988) :-
    constitution_year(1988).

% atom_id: 4a91f2a8fa6f857d | chunk: c14135d509987bdf | strength: statutory
prohibited(employer, worker, grant_indemnification_posterior_1988) :-
    constitution_year(1988).

% atom_id: 66428da48932ac02 | chunk: c14135d509987bdf | strength: statutory
obligated(employer, worker, compute_notice_period_integral_service_time) :-
    collective_agreement(silence_on_legal_effects).

% atom_id: f9ec96ddb0adbd5f | chunk: c2e77a23eaec3c29 | strength: statutory
obligated(employer, worker, guarantee_salary_during_lactation_period).

% atom_id: f91b8e2a21048c0f | chunk: d37580a7c7bb5380 | strength: statutory
obligated(employer, worker, prove_facts_impeding_modifying_extinguishing_salary_equivale).

% atom_id: 09e8c571783ee76a | chunk: d37580a7c7bb5380 | strength: statutory
obligated(worker, court, prove_local_holiday_authorizing_extension_of_recourse_period).

% atom_id: 6b58647e69dc7314 | chunk: d37580a7c7bb5380 | strength: statutory
obligated(employer, worker, prove_facts_impeding_modifying_extinguishing_salary_equivale).

% atom_id: cbc8bf387bdecbef | chunk: d37580a7c7bb5380 | strength: statutory
obligated(worker, employer, prove_refusal_of_presentation_of_time_cards_unjustified).

% atom_id: d6989d531a750394 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(employer, worker, assume_liability_for_obligations_of_succeeded_bank).

% atom_id: c6281c644919afe8 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, evaluate_recourse_based_on_legal_disagreement_or_violation_o).

% atom_id: be1e66970b18ebf5 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, limit_execution_to_date_base_of_category_when_decision_is_si) :-
    decision_exequenda(silent_on_limitation).

% atom_id: 76a6ccd93747b538 | chunk: d5be9daa05b29484 | strength: regulatory
prohibited(court, litigant, violate_res_judicata_when_decision_exequenda_explicitly_affi) :-
    decision_exequenda(explicitly_affirms_limitation).

% atom_id: 5a910382b26ceaf8 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, evaluate_legal_special_law_for_temporary_or_technical_positi).

% atom_id: b575ec4f1bd3f359 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, validate_deposit_recourse_without_pis_pasep_indication_in_th).

% atom_id: 57685da981bc33ca | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, grant_stability_to_celetist_public_servants_in_direct_admini).

% atom_id: 42dbe94fd4e491b2 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, limit_number_of_sindical_directors_to_seven).

% atom_id: 7b3fc5ce75fd4644 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, include_perilousness_addition_in_calculation_of_extra_hours).

% atom_id: c8700ca3774b7f98 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, start_aviso_previo_count_after_stability_period_ends).

% atom_id: 18df50b37378f576 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, grant_free_legal_aid_at_any_time_or_jurisdictional_level).

% atom_id: a68406e0c2550658 | chunk: d5be9daa05b29484 | strength: regulatory
obligated(court, litigant, set_time_limit_for_payment_of_legal_fees_after_free_aid_reje).

% atom_id: 621068c57b5eb034 | chunk: dec5ec392756c00c | strength: statutory
obligated(employer, worker, provide_peril_allowance) :-
    exposure_type(permanent),
    exposure_type(intermittent).

% atom_id: a7f03a2690af6813 | chunk: dec5ec392756c00c | strength: statutory
obligated(employer, worker, respect_agreed_peril_allowance_percentage) :-
    agreement_type(collective).

% atom_id: 5cf393a842f90364 | chunk: dec5ec392756c00c | strength: statutory
prohibited(court, worker, apply_for_court_review) :-
    case_type(rescission),
    case_type(mandado_seguranca).

% atom_id: eaf75f93fa89470c | chunk: dec5ec392756c00c | strength: statutory
obligated(employer, worker, record_time_card_variations) :-
    time_variation_minutes(X_0), X_0 <= 5.

% atom_id: c296a1805e9401d7 | chunk: dec5ec392756c00c | strength: statutory
obligated(employer, worker, record_time_card_variations_extra_hours) :-
    time_variation_minutes(X_0), X_0 > 5.

% atom_id: 859e0b48a7517e51 | chunk: dec5ec392756c00c | strength: statutory
prohibited(employer, worker, include_utilities_in_salary) :-
    utility_type(housing),
    utility_type(electricity),
    utility_type(vehicle).

% atom_id: 7d1ebcce7c360b3e | chunk: dec5ec392756c00c | strength: statutory
prohibited(employer, worker, include_cigarettes_in_salary).

% atom_id: 6053461d760f8ba8 | chunk: dec5ec392756c00c | strength: statutory
obligated(employer, worker, remit_contributions) :-
    contribution_type(previdenciary),
    contribution_type(tax).

% atom_id: f12e89bbe3d32f97 | chunk: dec5ec392756c00c | strength: statutory
obligated(worker, employer, pay_tax_and_contributions) :-
    contribution_type(previdenciary),
    tax_type(income_tax).

% atom_id: 2f3eedf6753dd8bf | chunk: dec5ec392756c00c | strength: statutory
obligated(court, employer, determine_reimbursement_of_contributions).

% atom_id: 1249ab215e09de61 | chunk: def5e53882b6019d | strength: statutory
obligated(regional, parte_contraria, impugnar).

% atom_id: 028a2460d09b0c74 | chunk: def5e53882b6019d | strength: statutory
obligated(parte_contraria, none, impugnar).

% atom_id: ed9d3e1281573e8d | chunk: def5e53882b6019d | strength: statutory
obligated(regional, none, adotar_uma_tese_contraria_a_lei_ou_a_sumula).

% atom_id: 5414a9f2dca1b65f | chunk: def5e53882b6019d | strength: statutory
obligated(parte, none, invocar_expressamente_no_recurso_de_revista_os_preceitos_leg).

% atom_id: d29f224bd8c5760d | chunk: e7969ddc18c0dcf8 | strength: statutory
obligated(employer, worker, provide_unemployment_benefits).

% atom_id: fe1d168a81a12b48 | chunk: e7969ddc18c0dcf8 | strength: constitutional
obligated(justice_of_labor, worker, process_and_judge_indemnity_cases).

% atom_id: 972c3adb0649230a | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, creditor, determine_money_pledge_in_definitive_execution).

% atom_id: f3de1ebfba5e9757 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, debtor, not_deposit_money_pledge_in_bank) :-
    creditor_disagreement(true).

% atom_id: e726b07b45e76536 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, debtor, not_determine_money_pledge_in_provisional_execution) :-
    other_assets_named_for_seizure(true).

% atom_id: f9656254d4c97aa0 | chunk: ebc75b3e3a5dcc8e | strength: statutory
permitted(judiciary_authority, parties, homologate_settlement_agreement).

% atom_id: 24b7d58fcc9bc137 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, third_party_claimant, file_third_party_claims_in_deprecated_judgment) :-
    asset_constrained_by_judgment(false),
    return_of_writ(true).

% atom_id: 906d596bdc99f55f | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, third_party_claimant, file_third_party_claims_in_deprecating_judgment) :-
    asset_constrained_by_judgment(true).

% atom_id: b109183543cce5b4 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, third_party_claimant, file_third_party_claims_in_deprecated_judgment) :-
    asset_constrained_by_judgment(false).

% atom_id: 27f9a2d1f18a9f7f | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, third_party_claimant, file_third_party_claims_in_deprecating_judgment) :-
    asset_constrained_by_judgment(true),
    judicial_vices_or_irregularities(false).

% atom_id: 677b2e964c404723 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, third_party_claimant, file_third_party_claims_in_deprecated_judgment) :-
    asset_constrained_by_judgment(true),
    judicial_vices_or_irregularities(true).

% atom_id: fea90f5c72363c25 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, regional_labor_court_and_local_labor_judge, not_conflict_of_competence).

% atom_id: a77c0e8b4df0c9f6 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, parties, file_embargoes_of_declaration) :-
    monocratic_decision_by_judge(true),
    judicial_integration_and_correction(true).

% atom_id: 67b54130a5313a2c | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, parties, convert_embargoes_of_declaration_to_appeal) :-
    monocratic_decision_by_judge(true),
    revision_in_merit(true).

% atom_id: fa6e5d8d90680393 | chunk: ebc75b3e3a5dcc8e | strength: statutory
obligated(judiciary_authority, parties, complement_appeal_reasons_within_five_days) :-
    monocratic_decision_by_judge(true),
    revision_in_merit(true).

% atom_id: 5a6b574cff4a21a8 | chunk: f4784dc6f4818436 | strength: statutory
obligated(employer, worker, record_time_travel_to_work) :-
    time_spent(X_0), X_0 > 10.

% atom_id: 24c97ea4ebf97796 | chunk: f4784dc6f4818436 | strength: statutory
obligated(employer, worker, pay_overtime_for_excess_hours).

% atom_id: 9d9a012f5d5f8a24 | chunk: fcec0b5e55ceb5c5 | strength: statutory
obligated(tribunal, decisao_monocratica_do_relator, ser_esclarecido).

% atom_id: a865e415eeb04c82 | chunk: fcec0b5e55ceb5c5 | strength: statutory
obligated(tribunal, embargos_declaratorios_postulando_efeito_modificativo, ser_submetidos_ao_pronunciamento_do_colegiado).

% atom_id: 0d2cba5eaebd3424 | chunk: fcec0b5e55ceb5c5 | strength: statutory
obligated(partes_interessadas_na_acao_rescisoria, acao_cautelar_proposta_sob_a_vigencia_do_cpc_de_1973, ser_instruida_com_as_provas_documentais_necessarias_a_aferic).

% atom_id: 5c2dc7d7ca565e76 | chunk: fcec0b5e55ceb5c5 | strength: statutory
obligated(julgador, acao_rescisoria_contendo_mais_de_um_pedido_em_ordem_sucessiv, ser_apreciado).