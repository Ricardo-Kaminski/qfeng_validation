% atom_id: 88b7ec42579fbd1d | chunk: 0053b0c13cb3f811 | strength: statutory
obligated(state, public, provide_collective_passenger_transport).

% atom_id: 6c58ded71cfd07ab | chunk: 0054e24035e8edbb | strength: statutory
obligated(employer, stable_employee, provide_indemnity) :-
    closure_reason(not_force_majeure).

% atom_id: 9e7c292cb1996daf | chunk: 007850bd248682e6 | strength: statutory
permitted(employee, none, reimburse_difference_below_minimum_wage) :-
    monthly_income(minimum_wage).

% atom_id: a6076d96f4d08a07 | chunk: 008e053decd10dce | strength: statutory
prohibited(employee, none, refuse_extraordinary_service_without_justified_cause).

% atom_id: 143b1b02312ab139 | chunk: 00f3641a86b9ca8d | strength: statutory
obligated(president, none, submit_agreement_for_homologation).

% atom_id: 04ddf77824d157be | chunk: 00fcd22454eb8bbe | strength: statutory
obligated(authority, parties, despachar_recursos_interpostos).

% atom_id: 27b9a57161e7fbec | chunk: 013a73ba4359f7dd | strength: statutory
obligated(employer, worker, compute_extra_hours_as_full_hour).

% atom_id: af94a058e51715bc | chunk: 01abe090989c4c9e | strength: statutory
permitted(tribunal_superior_do_trabalho, ministers_of_the_tribunal, substitute_via_convocation) :-
    leave_duration(X_0), X_0 > 30,
    position_filled(false).

% atom_id: cca4af6f11e2e37a | chunk: 01e45ecdc69ff62c | strength: statutory
obligated(employee, none, undertake_employment_duties).

% atom_id: 22aa10dcd26c6a65 | chunk: 01e885d70c49f404 | strength: statutory
obligated(employee, employer, sign_responsibility_term).

% atom_id: 24574bbcc13cb062 | chunk: 024b2732917b5ea3 | strength: statutory
permitted(worker_or_employer, none, appeal_to_superior_labor_tribunal) :-
    decision_level(regional_labor_court),
    case_type(individual_dispute).

% atom_id: 047bf90f174ae0aa | chunk: 0265a3a2d00eec13 | strength: regulatory
obligated(procuradoria_do_departamento_estadual_do_trabalho, public, continue_cobrancas) :-
    estado(sao_paulo).

% atom_id: d0da732e719bd163 | chunk: 02848bbf2ccbf429 | strength: statutory
permitted(worker, none, appeal_tribunal_decisions) :-
    cases(previstos_em_lei).

% atom_id: 799458072975efb4 | chunk: 02a516533ca58021 | strength: regulatory
obligated(authority, conflicting_authorities, communicate_decision_immediately).

% atom_id: db8afdc1d95f0c41 | chunk: 02d830813f2fd787 | strength: statutory
obligated(employer, sindical_entity, remit_to_sindical_entity).

% atom_id: 5a39c6f71394a144 | chunk: 02ed714780f4fbad | strength: statutory
obligated(tribunal, none, reunir_em_dias_fixados).

% atom_id: 18f3497cded5d513 | chunk: 02ed714780f4fbad | strength: statutory
permitted(presidente_tribunal, none, convocar_sessoes_extraordinarias) :-
    necessidade(true).

% atom_id: 563dc69f3d1e606c | chunk: 03201cfb81cc4547 | strength: statutory
obligated(employer, worker, ensure_return_benefits) :-
    employee_status(afastado),
    benefit_type(category_vantagens).

% atom_id: 6780335e8bc146f2 | chunk: 03753a058f3ae227 | strength: statutory
prohibited(employee, none, work_for_another_employer_during_vacation) :-
    contract_status(regular_contract).

% atom_id: fa3f7f9696d0c521 | chunk: 03753a058f3ae227 | strength: statutory
permitted(employee, none, work_for_another_employer_during_vacation) :-
    contract_status(regular_contract),
    obligatory_clause(true).

% atom_id: 323b6f797793babd | chunk: 03df18a7a1e82253 | strength: statutory
obligated(entity_union, directly_affected_workers, call_general_assembly).

% atom_id: f40dd546743bc7d1 | chunk: 0474c28d5c86da3d | strength: statutory
obligated(functionary, none, execute_works_designated).

% atom_id: 3ef626a39a316ebd | chunk: 04f6b482c5f207ad | strength: regulatory
obligated(authority, public, conduct_hearing_within_shortest_possible_period) :-
    hearing_type(ex_officio).

% atom_id: 3f3acbed328cb5b2 | chunk: 053a3ab3ecce40a2 | strength: statutory
prohibited(authority, none, serve_summons_by_announcement).

% atom_id: cf661f8d2805190d | chunk: 053a3ab3ecce40a2 | strength: statutory
obligated(author, reclamado, correctly_indicate_name_and_address).

% atom_id: c9e6da3c026ca833 | chunk: 0547ccb247daefdc | strength: statutory
obligated(employer, worker, pay_within_eight_days_if_payment_is_per_week_or_less).

% atom_id: ef55b09e4bbf7757 | chunk: 0582387ab03129eb | strength: statutory
obligated(authority, tribunal, apply_conflict_resolution_rules) :-
    conflict_type(jurisdiction),
    involved_parties(tribunal_regionals).

% atom_id: a7777a360259e790 | chunk: 05a2e18c7c2382d0 | strength: statutory
obligated(tribunal, president_of_juntas_and_substitutes_vogals_suplentes_and_emp, grant_posse).

% atom_id: 57bfcd89f81b7b18 | chunk: 05a2e18c7c2382d0 | strength: statutory
obligated(tribunal, president_of_juntas_and_substitutes_vogals_suplentes_and_emp, grant_holidays_and_leaves).

% atom_id: cbc9b8cefed20a59 | chunk: 05a8cb833e6a1640 | strength: regulatory
prohibited(employer, none, violate_labor_regulations).

% atom_id: 7baee4510a7e8dfa | chunk: 05cf398525a07550 | strength: statutory
obligated(tribunal, tribunal_server, grant_leave_and_holidays).

% atom_id: 3aeff7a6fbc6a691 | chunk: 05cf398525a07550 | strength: statutory
obligated(tribunal, tribunal_server, impose_disciplinary_penalties).

% atom_id: 9be8908b5d7dfc83 | chunk: 05f4d1ed5542d089 | strength: statutory
obligated(reclamante, none, appear_to_reducel_claim_to_term) :-
    force_majeure_reason(false).

% atom_id: 2a9e46a5406936b6 | chunk: 0660fa1757ceab34 | strength: statutory
obligated(presidente_do_tribunal_nacional_do_trabalho, public, decide_previdencia_social_matters).

% atom_id: c75c72c660aa825f | chunk: 069f91c760a9db03 | strength: statutory
prohibited(individual, none, hold_public_office) :-
    account_status(unapproved).

% atom_id: acbcdb485d5f5885 | chunk: 06ac3143c667b7f1 | strength: statutory
obligated(authority, none, include_party_names_in_decision).

% atom_id: 17f9575893e7be19 | chunk: 06ac3143c667b7f1 | strength: statutory
obligated(authority, none, include_request_summary_in_decision).

% atom_id: f27677fc7a8c86aa | chunk: 06ac3143c667b7f1 | strength: statutory
obligated(authority, none, include_defense_summary_in_decision).

% atom_id: 2ca7de22a034b9e4 | chunk: 06ac3143c667b7f1 | strength: statutory
obligated(authority, none, include_evidence_assessment_in_decision).

% atom_id: b1668e9dfd19ff30 | chunk: 06ac3143c667b7f1 | strength: statutory
obligated(authority, none, include_decision_justification_in_decision).

% atom_id: e4b4fb6cf5c5d68c | chunk: 06ac3143c667b7f1 | strength: statutory
obligated(authority, none, include_decision_conclusion_in_decision).

% atom_id: 64bae8ed589e6f1f | chunk: 06d5ecee9ba420c2 | strength: statutory
obligated(state, public, coordinate_workplace_safety_activities).

% atom_id: 5bbcaedc6dd6cda7 | chunk: 071fa5dea7dcb448 | strength: statutory
permitted(collective_agreement, motorist_professional, establish_special_work_schedule).

% atom_id: 3c0d73dda5981e9c | chunk: 077e6f6d518684f7 | strength: statutory
obligated(authority, interested_party, provide_receipt_for_case_distribution).

% atom_id: bd7c9a296f90d4c2 | chunk: 082e4e770b88c499 | strength: statutory
prohibited(student, none, unjustified_absence_from_school) :-
    absence_impact(loss_of_academic_year).

% atom_id: 89645335467cd323 | chunk: 084bceaa79f999b2 | strength: statutory
obligated(authority, journal_owner_director, register_journal_owner_director).

% atom_id: cbd0c200b9c10480 | chunk: 084c3ee46179f21c | strength: statutory
obligated(sus_manager, tribunal_regional_president, represent_unjustified_absence) :-
    absences(3),
    consecutive_meetings_missed(X_1), X_1 >= 3.

% atom_id: 21d34c7e6b1b6925 | chunk: 08afe27538289c72 | strength: statutory
prohibited(individual, document, use_falsified_documents).

% atom_id: ab45e25f41e86dcf | chunk: 08b1633c0e02a875 | strength: statutory
obligated(employer, worker, respect_prescription_period_labor_claims) :-
    type_of_claim(labor_credits),
    work_type(urban_rural).

% atom_id: c120d03d9bfe95dd | chunk: 08b1633c0e02a875 | strength: statutory
obligated(employer, worker, respect_prescription_period_labor_claims) :-
    type_of_claim(labor_credits),
    work_type(urban_rural).

% atom_id: 45975ecfee39c043 | chunk: 08c6e5988a2c5cb8 | strength: regulatory
permitted(litigant, none, withdraw_from_interrogatory).

% atom_id: f08d52d961fc34aa | chunk: 08e030f72778bdc2 | strength: statutory
obligated(driver, none, monitor_vehicle_safety_conditions).

% atom_id: 7c495a80a6ffbe62 | chunk: 08e2c5d29921ee93 | strength: statutory
obligated(citizen, none, register_as_elector).

% atom_id: 6a39119e9116173f | chunk: 09358810aa82a886 | strength: statutory
obligated(applicant, none, submit_recognition_request_to_minister_of_work).

% atom_id: 370ed95627cfe199 | chunk: 09bfe4ed3dee3f03 | strength: statutory
obligated(tribunal_regional, case, determine_jurisdiction_based_on_article_651).

% atom_id: 235369d28699686b | chunk: 09bfe4ed3dee3f03 | strength: statutory
obligated(tribunal_regional, collective_dispute, determine_jurisdiction_based_on_location_of_occurrence).

% atom_id: a0faed03825132c4 | chunk: 09eb1d5fcd69b296 | strength: statutory
obligated(tribunal, none, elaborate_internal_regulation).

% atom_id: b6b4910ff1bd618c | chunk: 09eb1d5fcd69b296 | strength: statutory
obligated(tribunal, none, exercise_administrative_attributes) :-
    legal_basis(law_or_constitution).

% atom_id: 5840c71878d52bf1 | chunk: 09f469c287a56d20 | strength: statutory
obligated(sindicato, federacao, comply_with_quadro_atividades_profissoes) :-
    quadro_de_atividades_e_profissoes(referenced_by_art_577).

% atom_id: 84af4b0a2eb0c4bb | chunk: 0a4c287a85f4e9d9 | strength: statutory
obligated(authority, worker, continue_salary_payment_during_inquiry) :-
    employee_stability_recognition(previous).

% atom_id: c69c3cac68ce1257 | chunk: 0a71748198c9666e | strength: statutory
obligated(employer, employee, recollect_sindical_contribution_employees).

% atom_id: 0dd8d3aefe4ec50f | chunk: 0a71748198c9666e | strength: statutory
obligated(employer, freelancer_worker, recollect_sindical_contribution_freelancers).

% atom_id: fbf6192263ed7068 | chunk: 0a71748198c9666e | strength: statutory
obligated(freelancer_worker, sindical_entity, pay_sindical_contribution) :-
    authorization(true).

% atom_id: 91fbf05c1d7fe48d | chunk: 0a71748198c9666e | strength: statutory
obligated(sindical_entity, freelancer_worker, authorize_contribution_payment).

% atom_id: 3f28645cfb9433c5 | chunk: 0a7680ae6230abfe | strength: statutory
obligated(judge_or_president, court_proceeding, schedule_continuation_of_hearing) :-
    continuation_possible(false),
    reason(force_majeure).

% atom_id: bbe27f7bcd5b12bb | chunk: 0aa699a6055ec21c | strength: statutory
obligated(tribunal_regional, none, exercise_jurisdiction).

% atom_id: 25487630c34dd93c | chunk: 0affe2f0b79ae539 | strength: statutory
obligated(employer, sus_manager, provide_necessary_clarifications).

% atom_id: a9e50c26f7933762 | chunk: 0affe2f0b79ae539 | strength: statutory
obligated(employer, sus_manager, display_records_when_required).

% atom_id: 87441392f4c3ae56 | chunk: 0b35476c414d46f1 | strength: statutory
obligated(worker, employer, claim_minimum_wage_complement) :-
    salary_amount(minimum_wage).

% atom_id: acbf7646f2e14798 | chunk: 0b35476c414d46f1 | strength: statutory
obligated(employer, worker, pay_minimum_wage_complement) :-
    salary_amount(minimum_wage).

% atom_id: ad177522685f5001 | chunk: 0b4ec7fcbb8ab114 | strength: regulatory
obligated(provider, public, perform_additional_cleaning_and_maintenance).

% atom_id: 305d434d2d407757 | chunk: 0c19ea1be0faa6ca | strength: statutory
obligated(employer, worker, deposit_monthly_fgts).

% atom_id: 72fc094aa5941f09 | chunk: 0c19ea1be0faa6ca | strength: statutory
obligated(employer, worker, calculate_rescission_indemnity_fgts).

% atom_id: ea98c1c00c978834 | chunk: 0c857d7b1948dcd5 | strength: statutory
obligated(authority, public, make_public_certificates_of_chemical_analyses_reports) :-
    professional_qualification(satisfies_conditions_art325_a_b).

% atom_id: 8b13f902bba8e5e9 | chunk: 0cb011269171985c | strength: statutory
permitted(principal_contractor, subcontractor, withhold_amounts_due) :-
    obligations(this_article).

% atom_id: 5cfb998dc2d36089 | chunk: 0cb011269171985c | strength: statutory
permitted(principal_contractor, subcontractor, file_regulatory_action) :-
    obligations(this_article).

% atom_id: c505f4a5b28353cd | chunk: 0cdf555f3be2630c | strength: statutory
obligated(company, none, comply_with_labor_legislation).

% atom_id: 6112e05372b77629 | chunk: 0d3decbcafe25912 | strength: statutory
prohibited(authority, testifier, penalize_absence_for_testimony).

% atom_id: 30c2bfc371eec3c5 | chunk: 0d6687412f8dab2f | strength: statutory
permitted(minor, none, sign_receipt_for_salary_payment).

% atom_id: 433e673672e28e02 | chunk: 0d6687412f8dab2f | strength: statutory
prohibited(minor_under_18, employer, give_quittance_without_legal_guardians_assistance) :-
    age(X_0), X_0 <=18 18.

% atom_id: 3692d664d9a1b65d | chunk: 0d7336e09aa4f998 | strength: regulatory
obligated(sindicato_principal, none, alter_denomination) :-
    hypothetical_condition(previous_article_hypothesis).

% atom_id: cc34f7511cc55824 | chunk: 0de862c7cbe7f32f | strength: statutory
prohibited(company, none, violate_prohibitions_in_title).

% atom_id: 6b0208c5640acc05 | chunk: 0de862c7cbe7f32f | strength: statutory
prohibited(company, none, reoffend_violating_prohibitions_in_title).

% atom_id: f07123beaa1de384 | chunk: 0e973c489e97c450 | strength: statutory
obligated(military_personnel, none, comply_with_military_service_requirements) :-
    time_period(during_military_service_requirements).

% atom_id: c916795d83a137dc | chunk: 0e9d53b07c047680 | strength: statutory
obligated(orgaos_justia_trabalho, none, function_coordinated_collaboration).

% atom_id: f05b7d63f069f79c | chunk: 0e9d53b07c047680 | strength: statutory
obligated(presidente_tribunal_superior_trabalho, orgaos_justia_trabalho, orientate_functioning).

% atom_id: 2223896974b76fe9 | chunk: 0eb9565bf111fa1d | strength: statutory
prohibited(employer, worker, unilaterally_change_contract_terms).

% atom_id: a6680bf2cb248cf8 | chunk: 0ebf2a483080c34f | strength: statutory
obligated(tribunal_regional, none, judge_cases) :-
    case_type(cases_from_previous_article_except_incident_c_i).

% atom_id: 5a6ed8cc480fa002 | chunk: 0ebf2a483080c34f | strength: statutory
obligated(tribunal_regional, none, resolve_jurisdiction_conflicts_between_turmas).

% atom_id: 7b7ecb0c1affa0ef | chunk: 0f6b6247757d758c | strength: statutory
prohibited(authority, public, prejudice_subsequent_acts) :-
    nullity_of_act(true).

% atom_id: 477da0226a988184 | chunk: 0f741279af071b46 | strength: statutory
permitted(employer, worker, define_work_uniform_standard).

% atom_id: afd51c85205e3ed9 | chunk: 0fb8e3f2654d9513 | strength: statutory
prohibited(employer, worker, offend_physically) :-
    legitimate_defense(false).

% atom_id: 677d48a32fd8ee6b | chunk: 0ff4e1fab7c86fd9 | strength: statutory
obligated(authority, worker, distribute_verbal_claim_before_reduction_to_term).

% atom_id: 8b2bf04269b169f7 | chunk: 0ffd791a4043e5a9 | strength: statutory
prohibited(employer, worker, exceed_normal_work_duration).

% atom_id: 2f8cc891c189bc50 | chunk: 10a21ad801ceeba0 | strength: statutory
obligated(employer, worker, provide_indemnity_on_termination) :-
    cause_of_termination(death_of_employer).

% atom_id: 6e4c9baa65ae843d | chunk: 10d750b03eb2ff41 | strength: regulatory
obligated(authority, candidate, challenge_investment_of_conciliation_and_judgment_board_memb).

% atom_id: b0466212e6f2ca93 | chunk: 11acd5fd1ed179aa | strength: regulatory
obligated(employer, worker, calculate_days_of_work_per_month) :-
    number_of_days(X_0), X_0 < 30.

% atom_id: 4fefc0cb939948c1 | chunk: 11fea8bdaafeb743 | strength: statutory
obligated(state, administration, guarantee_information_security_conditions_without_cost_throu).

% atom_id: 0ff52a73a1e58a8a | chunk: 12d44408476147ef | strength: statutory
obligated(authority, investigation, process_and_judge_grave_offense_inquiries).

% atom_id: 998f76f5a2675306 | chunk: 13204a1390c2da05 | strength: statutory
obligated(authority, none, designate_procurator_substitute).

% atom_id: ede149be5a6c786e | chunk: 132d2f1709dbdd43 | strength: statutory
obligated(authority, tribunal_judge_or_president, judge_suspicions_in_pending_cases) :-
    suspect_type(presidente_ou_outros_juizes_do_tribunal),
    case_status(pendente_decisao).

% atom_id: ddf2b8df54298049 | chunk: 1338913715b712f0 | strength: statutory
permitted(president_of_the_republic, civil_associations, grant_prerogative_under_article_513_alinea_d) :-
    reasons(public_utility),
    proposal_originator(ministry_of_labor).

% atom_id: a78062ef550b15b9 | chunk: 1346acce9da4ee8f | strength: statutory
obligated(tribunal_superior_do_trabalho, public, serve_as_supreme_instance_of_labor_justice).

% atom_id: 3c2fb79bf8d15541 | chunk: 1378ce43e1aab66a | strength: statutory
obligated(judge, litigant, discriminate_indemnity_values).

% atom_id: 129afe2f6c6df9a6 | chunk: 13821de51fbb5688 | strength: statutory
obligated(sindicate, resources, apply_budget_according_to_annual_plan).

% atom_id: 409f70192012d4d7 | chunk: 1397b9eb6a5b9715 | strength: statutory
obligated(procurador_geral_previdencia_social, none, lead_procuratorship_of_social_security).

% atom_id: d011d5c6bb23bc53 | chunk: 13c75974108bc448 | strength: statutory
obligated(union_member, union, pay_annual_contribution).

% atom_id: 9a69d7aa8b34ad54 | chunk: 13d64a93a5891005 | strength: statutory
obligated(employer, worker, reinstate_previous_position) :-
    employee_condition(capable_of_working),
    pension_status(cancelled).

% atom_id: 86b1eccdb227224a | chunk: 13d64a93a5891005 | strength: statutory
permitted(employer, worker, indemnify_for_contract_termination) :-
    employee_condition(capable_of_working),
    pension_status(cancelled).

% atom_id: 9df133607d9ddd1c | chunk: 13d64a93a5891005 | strength: statutory
obligated(employer, worker, indemnify_according_to_articles_477_and_478) :-
    employee_condition(capable_of_working),
    pension_status(cancelled).

% atom_id: 28b7b529027eb0f8 | chunk: 13d64a93a5891005 | strength: statutory
obligated(employer, worker, indemnify_according_to_article_497) :-
    employee_condition(capable_of_working),
    pension_status(cancelled),
    stability_status(holder_of_stability).

% atom_id: b48831ab40e161a0 | chunk: 13da5deac369ec22 | strength: statutory
obligated(procurator, court, function_in_judgment_first_instance).

% atom_id: 2993ca662bda4bb7 | chunk: 13da5deac369ec22 | strength: statutory
obligated(procurator, court, designate_procurators_to_function_in_judgment_first_instance).

% atom_id: 40d41fc4fed35ac6 | chunk: 1403be9d3bc9f594 | strength: statutory
prohibited(employer, worker, require_work_on_exam_days) :-
    activity_type(vestibular_exams),
    day_of_week(monday_tuesday_wednesday_thursday_friday_saturday_sunday).

% atom_id: ea1b14f9accb340e | chunk: 1415d58596feaab5 | strength: statutory
obligated(reclamante, none, attend_judgment_hearing).

% atom_id: 6882bf34ec2138f2 | chunk: 1415d58596feaab5 | strength: statutory
obligated(reclamado, none, attend_judgment_hearing).

% atom_id: 02c02d5553189886 | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamante, none, be_represented_in_hearing) :-
    hearing_type(mass_claim).

% atom_id: 2e8f680184a63f70 | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamado, none, be_represented_in_hearing) :-
    hearing_type(mass_claim).

% atom_id: ba316567ff6e7e5b | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamante, none, be_represented_in_hearing) :-
    hearing_type(enforcement_action).

% atom_id: 4b8e47dd51f0fd68 | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamado, none, be_represented_in_hearing) :-
    hearing_type(enforcement_action).

% atom_id: 68d8d2b7ac4f5959 | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamante, none, be_represented_in_hearing) :-
    hearing_type(mass_claim),
    representative(union_of_category).

% atom_id: c92e3635af09a916 | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamado, none, be_represented_in_hearing) :-
    hearing_type(mass_claim),
    representative(union_of_category).

% atom_id: 6a86e0e96c8b469a | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamante, none, be_represented_in_hearing) :-
    hearing_type(enforcement_action),
    representative(union_of_category).

% atom_id: 64ac9ee3625a2b98 | chunk: 1415d58596feaab5 | strength: statutory
permitted(reclamado, none, be_represented_in_hearing) :-
    hearing_type(enforcement_action),
    representative(union_of_category).

% atom_id: 8831210de2e9c4a7 | chunk: 1437686c449f5e6d | strength: statutory
prohibited(non_state_actors, activity_or_profession, use_denominations_privative_of_superior_sindical_entities).

% atom_id: 6d6fa18c699ab354 | chunk: 14657b71777eb657 | strength: regulatory
obligated(ministry_of_education_and_health, professor, determine_equitable_compensation).

% atom_id: 856e7cb8b64ec8d1 | chunk: 14657b71777eb657 | strength: regulatory
obligated(ministry_of_education_and_health, professor, ensure_execution_of_precept).

% atom_id: ad5d7d17667f6746 | chunk: 14753cf2ced50c80 | strength: statutory
obligated(authority, ship_or_vessel, abastecimento_navio_combustivel_rancho) :-
    destination(abastecimento_do_navio_ou_embarcacao).

% atom_id: 1ec42f6400c93765 | chunk: 14753cf2ced50c80 | strength: statutory
obligated(authority, ship_or_vessel, transposicao_passos_pontos_dificeis) :-
    natureza_navegacao(contingencias).

% atom_id: 12c8e435f037277c | chunk: 14753cf2ced50c80 | strength: statutory
obligated(authority, ship_or_vessel, operacoes_alivio_transbordo_carga) :-
    calado_menor(true).

% atom_id: 027a0ddd8f3d23fd | chunk: 14a6b343087421a8 | strength: statutory
obligated(authority, none, judge_in_first_or_final_instance).

% atom_id: 426f4db61c2635ec | chunk: 153a06ff7bc23a42 | strength: statutory
prohibited(employer, worker, apply_dispositions_of_chapter_vii).

% atom_id: a91d1bd4d93c4736 | chunk: 153af4a2a6002788 | strength: statutory
obligated(state, unemployed_worker, provide_unemployment_benefits) :-
    type_of_unemployment(involuntary).

% atom_id: a82add2e59987f19 | chunk: 159c51543dd125df | strength: statutory
obligated(court, litigant, compensate_for_losses_and_damages) :-
    litigation_type(malicious_litigation).

% atom_id: 68d7e611e0eed0c7 | chunk: 1659275c75f1e446 | strength: statutory
obligated(tribunal, none, judge_revision_after_hearing_procurator) :-
    decision_origin(this_tribunal).

% atom_id: aa7f00d5a753b429 | chunk: 167568b18c3181f9 | strength: statutory
prohibited(collective, none, include_provisions_contrary_to_policy) :-
    policy_type(economic_financial_or_salary).

% atom_id: 188459b5adcb6484 | chunk: 167696731b57a20d | strength: statutory
obligated(judge, none, record_consciousness_in_acordao).

% atom_id: 0ed3bdd0a74f7632 | chunk: 175165e589a0a070 | strength: statutory
prohibited(employer, worker, hire_non_brazilian_worker_less_than_two_years_service) :-
    nationality(brasilian),
    years_of_service(X_1), X_1 < 2.

% atom_id: e457a944a45e2a9c | chunk: 175165e589a0a070 | strength: statutory
prohibited(employer, worker, hire_brazilian_worker_more_than_two_years_service) :-
    nationality(foreigner),
    years_of_service(X_1), X_1 > 2.

% atom_id: 47a046b7370aee51 | chunk: 1752e58cc2bb1c79 | strength: regulatory
obligated(deployer, public, open_official_correspondence_junta).

% atom_id: f2d88a8f9b5c4782 | chunk: 1769b6c96b0b5531 | strength: statutory
obligated(employer, worker, provide_adequate_lighting).

% atom_id: 1215980d43a3930f | chunk: 177047a5edaa5dd9 | strength: statutory
prohibited(concessionary_company_or_foreign_society, none, ignore_regulatory_requirements_after_fine) :-
    previous_sanction(true),
    compliance_status(non_compliant).

% atom_id: b8616ea0c76d79d9 | chunk: 1798693c22ad2830 | strength: statutory
permitted(employer, none, represent_in_hearing) :-
    preposto_knowledge(dissidio).

% atom_id: 5d387c9c3297b1b0 | chunk: 1798693c22ad2830 | strength: statutory
obligated(employer, none, be_responsible_for_preposto_statements).

% atom_id: f5ba1cd29383fd6f | chunk: 17d8805bc91a8582 | strength: statutory
obligated(authority, none, maintain_vigorous_quadros_tabelas_modelos).

% atom_id: d24f7c13cbf2d5bf | chunk: 181fe34a8c717ba1 | strength: statutory
obligated(ministry_of_labor, worker, establish_additional_safety_rules_for_machinery_and_equipmen).

% atom_id: 278904dbdf75807a | chunk: 18671261226f667a | strength: statutory
obligated(employer, worker, define_rights_and_obligations).

% atom_id: 7ad43253ab880f7a | chunk: 18671261226f667a | strength: statutory
obligated(employer, company, define_rights_and_obligations).

% atom_id: b187baa02acf67a8 | chunk: 1892536337faf70a | strength: statutory
obligated(teacher, none, register_with_ministry_of_education).

% atom_id: 1822632d4c2e180e | chunk: 19158e22046a24de | strength: statutory
obligated(secretaria_das_juntas, none, perform_secretarial_functions_of_the_juntas).

% atom_id: f89e23cb8bad5874 | chunk: 1951a45427e5f70a | strength: statutory
obligated(employer, child_worker, totalize_work_hours_across_establishments) :-
    age(X_0), X_0 <= 18,
    number_of_employers(X_1), X_1 > 1.

% atom_id: 2199b6504ef6a74e | chunk: 195e261089ac4e1b | strength: statutory
prohibited(individual_or_legal_entity, sindicato, interfere_in_administration_or_services).

% atom_id: 3b24dfffefa2527b | chunk: 19ce842afd4fee07 | strength: statutory
prohibited(worker, none, raise_claim_against_explicit_law_or_uncontested_fact).

% atom_id: 20f91be2a6375bfa | chunk: 19da62e68d94d572 | strength: statutory
permitted(deployer, public, write_processual_documents).

% atom_id: 46850125c32d9fca | chunk: 19fea8cd3f82d1d4 | strength: regulatory
obligated(procuradoria_da_previdencia_social, none, perform_its_duties).

% atom_id: 32458f59b3e4261e | chunk: 1a1c47d43029e599 | strength: statutory
obligated(employer, worker, elect_representation_committee) :-
    number_of_employees(X_0), X_0 > 200.

% atom_id: b4857620e90807e5 | chunk: 1a610bec3486e416 | strength: statutory
obligated(employer, worker, provide_adequate_subsurface_food).

% atom_id: 3f64336644f5780b | chunk: 1a6f068d914d90cb | strength: statutory
permitted(tripulante, none, remain_in_post) :-
    hour_of_day(X_0), X_0 >= 0,
    hour_of_day(X_1), X_1 <= 24.

% atom_id: 174f71f1be4b19d7 | chunk: 1a6f068d914d90cb | strength: statutory
obligated(authority, tripulante, ensure_post_time_limit) :-
    hour_of_day(X_0), X_0 >= 0,
    hour_of_day(X_1), X_1 <= 24.

% atom_id: aa48efdb96dc1a12 | chunk: 1a75ff0895773b04 | strength: statutory
obligated(authority, none, write_official_notification_for_review_requests).

% atom_id: 8fd664643c33ca45 | chunk: 1b1aab19df28d857 | strength: statutory
prohibited(employee, none, vote_by_representation).

% atom_id: a085b5d42065ccb2 | chunk: 1b4fe559022a4c34 | strength: regulatory
obligated(procuradoria, none, direct_services_and_issue_instructions).

% atom_id: 8e044530cbf17414 | chunk: 1b6c8bce3c90a99d | strength: statutory
obligated(commission_member, interested_party, deliver_written_demand_copy).

% atom_id: d11f0cc9190d9136 | chunk: 1b72a40379dd48aa | strength: statutory
obligated(employer, worker, limit_underground_work_hours).

% atom_id: aa6149f97c2f4876 | chunk: 1b8605253877dc16 | strength: statutory
obligated(employer, worker, pay_during_vacation).

% atom_id: a62089a36f00aba0 | chunk: 1be11e6d9d686aa1 | strength: statutory
obligated(employer, worker, ensure_safety_and_hygiene_conditions_during_material_handlin).

% atom_id: ea8b7551e2ec7b14 | chunk: 1c4da59dcef7567a | strength: statutory
prohibited(employer, worker, violate_work_protection_laws).

% atom_id: 56e0e9f754c3162a | chunk: 1c4da59dcef7567a | strength: statutory
obligated(employer, worker, respect_collective_agreements).

% atom_id: b1075cbe495611c9 | chunk: 1c4da59dcef7567a | strength: statutory
obligated(employer, worker, follow_authority_decisions).

% atom_id: 288f984c3002c35f | chunk: 1c8b80dc14e5c674 | strength: statutory
prohibited(employer, worker, lose_work_card).

% atom_id: 9f80d21d24e496db | chunk: 1ca4926f68dbf5e6 | strength: statutory
obligated(employer, worker, provide_protection_from_weather_elements).

% atom_id: 75869076b25dc7fb | chunk: 1ca4926f68dbf5e6 | strength: statutory
obligated(employer, worker, provide_drinking_water_outdoor_work).

% atom_id: 1996e86546fb2366 | chunk: 1ca4926f68dbf5e6 | strength: statutory
obligated(employer, worker, provide_quarantine_accommodation).

% atom_id: b1ee7d1a77e634a4 | chunk: 1cdddd3500297f63 | strength: statutory
prohibited(employer, worker, fail_to_report_data).

% atom_id: 6d3d72351ab54fda | chunk: 1d1b78aff21595ad | strength: statutory
prohibited(sus_manager, none, reincidir_embaracar_resistir_fiscalizacao) :-
    type_of_infraction(fraud).

% atom_id: e78bb73e5513e31a | chunk: 1d1e456a01a84149 | strength: statutory
obligated(authority, reclamant, submit_claim_to_distribution) :-
    number_of_juntas(X_0), X_0 > 1,
    number_of_judges_or_secretaries(X_1), X_1 > 1.

% atom_id: 47a947e2232ff478 | chunk: 1d56de3dcb185ca9 | strength: statutory
obligated(employer, worker, provide_night_shift_compensation) :-
    shift_type(night),
    reversal_frequency(weekly_biweekly).

% atom_id: ac70dc5c1a4c6410 | chunk: 1d74ac8c3d09fac5 | strength: regulatory
prohibited(worker, none, remain_on_leave_for_more_than_30_days).

% atom_id: c5836db077f47350 | chunk: 1d9b980b30d345c1 | strength: statutory
permitted(employee, none, work_without_hour_reduction) :-
    clause_reference(inciso_l).

% atom_id: d2acdbc257856159 | chunk: 1d9b980b30d345c1 | strength: statutory
permitted(employee, none, take_leave_without_salary_deduction) :-
    clause_reference(inciso_l).

% atom_id: 2969b7681ec228f5 | chunk: 1d9b980b30d345c1 | strength: statutory
permitted(employee, none, work_without_hour_reduction) :-
    clause_reference(inciso_lii).

% atom_id: 1f53a42ec7148baf | chunk: 1d9b980b30d345c1 | strength: statutory
permitted(employee, none, take_leave_without_salary_deduction) :-
    clause_reference(inciso_lii).

% atom_id: 4b739406f67a5db1 | chunk: 1db04bc852972efb | strength: statutory
obligated(authority, worker, fiscalize_labor_protection_rules_compliance).

% atom_id: 4ad525ddb06db543 | chunk: 1e4aade4aa97b652 | strength: statutory
obligated(collective, authority_competent, facilitate_exercise_of_supervision).

% atom_id: caaf388917c386d7 | chunk: 1f00c85ae3c349d1 | strength: statutory
permitted(ministry_of_labor, other_federal_state_or_municipal_bodies, delegate_authorities_to_other_organs) :-
    approval_status(approved_by_minister).

% atom_id: d2b45af9b44639ec | chunk: 1f00c85ae3c349d1 | strength: statutory
obligated(other_federal_state_or_municipal_bodies, companies, enforce_compliance_with_chapter_dispositions) :-
    delegation_status(delegated_by_ministry_of_labor).

% atom_id: bdae4465c003c075 | chunk: 1f2d339e96fbb3a4 | strength: statutory
prohibited(non_state_actors, association, use_denomination_sindicato).

% atom_id: 1538f8ef7bc62dde | chunk: 1f2d339e96fbb3a4 | strength: statutory
permitted(state_authority, professional_association, use_denomination_sindicato) :-
    association_type(first_degree),
    recognition_status(recognized_by_law).

% atom_id: 92aa2f48a2cdfa5c | chunk: 1f6f7b6bc0e3d22c | strength: statutory
permitted(minister_of_labor, association, recognize_as_sindicate) :-
    number_of_associates(one_third).

% atom_id: 7d4d2b029a237fb5 | chunk: 1f79e3c3ac8de3e1 | strength: statutory
prohibited(chemist, none, exercise_professional_functions) :-
    violation_type(listed_offenses).

% atom_id: ecb0768cad1f4ce1 | chunk: 1f9fb0337f466be0 | strength: statutory
permitted(ministry_of_work_industry_and_commerce, none, derogate_prohibition_from_quadro_405_a) :-
    dangerous_or_unhealthy_character(partially_or_totally_eliminated).

% atom_id: 619a23c6f894a035 | chunk: 1fad295ed416e651 | strength: statutory
permitted(professor, none, teach_multiple_shifts_at_same_institution) :-
    work_week_hours(legal_limit).

% atom_id: fa928d555d5366e7 | chunk: 1fad295ed416e651 | strength: statutory
obligated(professor, none, ensure_meal_break) :-
    work_week_hours(legal_limit).

% atom_id: c1908c384a9be076 | chunk: 1fad295ed416e651 | strength: statutory
prohibited(professor, none, count_meal_break_as_working_hours) :-
    work_week_hours(legal_limit).

% atom_id: 847555c5672134c1 | chunk: 1fbb650e13a06a78 | strength: statutory
obligated(state, public, maintain_legal_dispositions_in_force) :-
    disposition_type(transitoria),
    disposition_type(emergencia).

% atom_id: e416b95c588035fe | chunk: 1fbb650e13a06a78 | strength: statutory
obligated(state, public, maintain_legal_dispositions_in_force) :-
    disposition_type(nao_aplicavel_em_toda_a_nacionalidade).

% atom_id: a3d4c31c59192fb8 | chunk: 1ff9889da50c8f9b | strength: regulatory
prohibited(authority, sindical_entity, cancel_registration).

% atom_id: 2e228fd576aefe07 | chunk: 1ff9889da50c8f9b | strength: regulatory
prohibited(authority, sindical_entity, dissolve_entity).

% atom_id: 8df1063e59b2079f | chunk: 1ff9889da50c8f9b | strength: regulatory
obligated(authority, sindical_entity, dissolve_according_to_civil_law).

% atom_id: eec5e4570df980f7 | chunk: 202f80535609c5a9 | strength: statutory
obligated(state, federation, observe_dispositions_for_constitution_and_administration) :-
    applicability(relevant).

% atom_id: 750761c3e357bc17 | chunk: 205431c1ab1c33a4 | strength: statutory
obligated(deployer, none, adopt_measures_determined_by_regional_authority).

% atom_id: 192c9c43fc09d3cb | chunk: 20653188079bc2ef | strength: statutory
obligated(employer, foreign_worker, prioritize_layoff_over_brazilian_worker) :-
    service_availability(absent),
    worker_role_similarity(analogous_function).

% atom_id: f39b3e7d8a16eba6 | chunk: 20661bc1bfc81486 | strength: statutory
prohibited(employer, worker, discriminate_based_on_job_type_or_worker_status).

% atom_id: d090a36e37c77d1c | chunk: 20721b557e230ca5 | strength: statutory
obligated(parent_or_tutor, child, prevent_employment_harmful_to_child_development).

% atom_id: a2fd082d53f68fa2 | chunk: 20974d4721d3c4a2 | strength: statutory
obligated(employer, child_worker, pay_extra_wages_for_overtime) :-
    force_majeure_circumstance(true),
    overtime_hours(X_1), X_1 <= 12.

% atom_id: 4edda90444028947 | chunk: 20974d4721d3c4a2 | strength: statutory
obligated(employer, child_worker, ensure_essential_functioning_of_establishment) :-
    force_majeure_circumstance(true),
    overtime_hours(X_1), X_1 <= 12.

% atom_id: 9b168a3ada6d433c | chunk: 20dc7589e4a13701 | strength: regulatory
obligated(authority, none, conduct_necessary_inquiries) :-
    communication_received(true).

% atom_id: 0cf67a2864e46106 | chunk: 20dc7589e4a13701 | strength: regulatory
obligated(authority, none, draft_records_of_inquiries) :-
    communication_received(true).

% atom_id: b81a45764442505e | chunk: 20e10fa16296564b | strength: statutory
permitted(federations_of_professional_sindicatos, none, organize_independently_from_basic_group) :-
    law_dispositions(single_regulation).

% atom_id: 279c9d280c87845d | chunk: 212a7038550f6238 | strength: statutory
permitted(employer, worker, provide_compensatory_overtime_within_agreement).

% atom_id: 30053cc6d84628b4 | chunk: 213e04f3264c12a9 | strength: statutory
permitted(employer, worker, establish_12_hours_work_schedule_with_36_hours_rest) :-
    agreement_type(individual_written_agreement),
    agreement_type(collective_convention),
    agreement_type(collective_agreement).

% atom_id: a2b891701941cc25 | chunk: 213e04f3264c12a9 | strength: statutory
obligated(employer, worker, observe_or_compensate_rest_and_meal_breaks).

% atom_id: 12d7ac094742c6d6 | chunk: 2163b3396aad4bf8 | strength: statutory
obligated(employer, worker, medical_examination_by_employer).

% atom_id: f309cba46cf3bbef | chunk: 21c86653ba82cc44 | strength: statutory
permitted(ministry_of_labor, none, establish_complementary_dispositions).

% atom_id: a9e4f026daf4c86a | chunk: 21d058931ad77398 | strength: statutory
obligated(driver, cargo_and_vehicle, ensure_cargo_safety).

% atom_id: 13135fa72a500633 | chunk: 226224f0ca88980a | strength: statutory
obligated(professional, none, satisfy_legal_requirements).

% atom_id: 6d20e4edb865fa1c | chunk: 226c9f442c6e835c | strength: statutory
obligated(candidate, none, satisfy_qualification_requirements) :-
    date_of_publication(n12_de_julho_de_1934),
    position_type(quimico).

% atom_id: ae3caeeb9698c118 | chunk: 22e2da81dc36e1b3 | strength: statutory
permitted(employee, employer, appear_at_workplace_for_specific_activities).

% atom_id: ad644431ae350e41 | chunk: 234f927448219f7e | strength: statutory
obligated(collective, public, apply_imperative_dispositions) :-
    relationship_status(initiated_not_consummated),
    consolidation_effectiveness(effective_date).

% atom_id: 1a8d0f6f32b6df67 | chunk: 2394fd9fa2ad4dcd | strength: statutory
obligated(employer, worker, supplement_absence_or_repeat_action) :-
    possibility(true).

% atom_id: bae8aebe7995ea31 | chunk: 23c68c96b4f57f90 | strength: statutory
obligated(authority, junta_conciliacao_julgamento, appoint_distributor) :-
    number_of_juntas(X_0), X_0 > 1.

% atom_id: 22ed0cd72d84cc8a | chunk: 242847b90d1c073d | strength: statutory
prohibited(employer, worker, set_salary_payment_period_over_one_month).

% atom_id: 813c34a5c7444bb9 | chunk: 246df0573f83cfd3 | strength: statutory
permitted(worker, authority_competent_ministry_of_work, file_lawful_action_against_sindical_entity) :-
    time_since_atac(X_0), X_0 <= 30.

% atom_id: f694d5137a2eb6b7 | chunk: 247b4d2e90c80d13 | strength: statutory
permitted(part, none, present_expert_or_technician).

% atom_id: 85854dff5f92ef64 | chunk: 255d12862069f5e5 | strength: statutory
obligated(authority, worker, record_oral_complaints).

% atom_id: eadd2b1ec2f1ba4e | chunk: 25a1b21ffeeeee73 | strength: statutory
obligated(employer, worker, notify_professional_diseases) :-
    disease_type(professional),
    work_condition(special_conditions).

% atom_id: 8c22b1cd4da06e0e | chunk: 25c35cc84a5f910a | strength: statutory
prohibited(associado, none, fail_to_comply_with_regulation) :-
    cause_justified(false).

% atom_id: afc3230fa60eb392 | chunk: 25f34562b7b66447 | strength: statutory
obligated(withdrawn_partner, worker, subsidiarily_respond_for_labor_obligations) :-
    time_since_modification_averbation(X_0), X_0 <= 2.

% atom_id: 7749cca6ab44c09d | chunk: 25fae492582746b6 | strength: statutory
permitted(employer, worker, agree_to_in_kind_compensation) :-
    compensation_type(in_natura),
    product_origin(exploitation_of_business),
    maximum_compensation_percentage(X_2), X_2 <= 1.

% atom_id: 8d40312c21e152a8 | chunk: 26074a2a2b8abc18 | strength: statutory
prohibited(collective, sindicato, recognize_more_than_one_sindicato_per_category).

% atom_id: 5a64c6071eaf9d8e | chunk: 2678ad8152a23ab8 | strength: statutory
obligated(employer, worker, provide_hygiene_measures_at_workplace).

% atom_id: 23b2479a723493b7 | chunk: 26c537ff95b7fa1b | strength: statutory
obligated(authority, court_proceedings, follow_order_process_conflict_jurisdiction).

% atom_id: e3410cf08dfe9170 | chunk: 26d30512da21c26a | strength: statutory
prohibited(worker, any_person, act_injurious_to_honor_or_good_reputation) :-
    context(work_service).

% atom_id: a0894f5b4c4e7d1e | chunk: 26d30512da21c26a | strength: statutory
prohibited(worker, any_person, physical_offenses) :-
    context(work_service).

% atom_id: 2cd9deb97c46d998 | chunk: 26d30512da21c26a | strength: statutory
permitted(worker, any_person, physical_offenses) :-
    context(work_service),
    circumstance(self_defense).

% atom_id: 654128c4e126c9f5 | chunk: 26d30512da21c26a | strength: statutory
permitted(worker, any_person, physical_offenses) :-
    context(work_service),
    circumstance(defense_of_another_person).

% atom_id: 0214c4d6142d16e6 | chunk: 26f124da6402663e | strength: statutory
permitted(employer, bank_worker, extend_normal_work_duration) :-
    daily_hours(X_0), X_0 <= 8,
    weekly_hours(X_1), X_1 <= 40.

% atom_id: f1b0b366c3897aa4 | chunk: 2710041b10702a04 | strength: statutory
obligated(employer, worker, provide_equivalent_salary) :-
    salary_agreement(undefined).

% atom_id: 65ef0e2d2d1ce3a1 | chunk: 27e471ce3b4f896f | strength: statutory
obligated(employer, driver_worker, consider_as_effective_work_time) :-
    worker_status(motorist_employee),
    time_period(disposition_of_employer_excluding_meal_rest_breaks).

% atom_id: bd78af43d9877f0a | chunk: 28c9256b10bbb30f | strength: regulatory
obligated(associates, none, contribute_associations_funds) :-
    form_established(statutes_or_general_assemblies).

% atom_id: 194670f05b84d27b | chunk: 28e12db34b4e4cae | strength: statutory
permitted(individual_or_company, union, be_admitted_to_union) :-
    satisfies_legal_requirements(true).

% atom_id: 96285cd68a09e09c | chunk: 28fe0ee916854612 | strength: statutory
obligated(enterprise, none, observe_proportionality_requirements) :-
    activity_type(different_proporcionalities).

% atom_id: bf80ac8beee47a6e | chunk: 28fe0ee916854612 | strength: statutory
obligated(individual, none, observe_proportionality_requirements) :-
    activity_type(different_proporcionalities).

% atom_id: f671cc77759bb3ec | chunk: 29154006391123dd | strength: statutory
obligated(employer, worker, pay_minimum_wage).

% atom_id: 01177853cabf992d | chunk: 2a17aa09c07967cd | strength: statutory
obligated(sindicato, none, maintain_registration_book).

% atom_id: 9603b72a14eeebd6 | chunk: 2a17aa09c07967cd | strength: statutory
obligated(ministerio_do_trabalho_industria_e_comercio_functionary, sindicato_registration_book, authenticate).

% atom_id: c0e284b9903705c3 | chunk: 2a5b495a100cebd6 | strength: statutory
obligated(procuradorias_regionais, none, exercise_attributions_within_jurisdiction).

% atom_id: 441f2a428f3876e3 | chunk: 2a717ad2a2b0b4c7 | strength: statutory
permitted(worker, none, request_intercurrent_prescription_declaration).

% atom_id: 382aee2bffc6d8d4 | chunk: 2a717ad2a2b0b4c7 | strength: statutory
permitted(authority, none, declare_intercurrent_prescription_of_officio).

% atom_id: 97060165aa7f729f | chunk: 2a7667289e4c6143 | strength: statutory
obligated(tribunal, parties_or_their_representatives, notify_decision_by_registered_mail_with_franchise).

% atom_id: 7e0520e741cf1014 | chunk: 2a7667289e4c6143 | strength: statutory
obligated(tribunal, public, publish_decision_in_official_journal).

% atom_id: 0de857dbdb2f5fa9 | chunk: 2a77ed173b84d06d | strength: statutory
obligated(employer, child_worker, take_recommended_measures_by_authority) :-
    authority_recommendations(change_job_function).

% atom_id: c2c61ae9a06c4dd2 | chunk: 2ad38f6d5c32b40a | strength: statutory
obligated(director_of_social_security_department, institutes_and_pension_funds, preside_elections_for_financial_committees).

% atom_id: 691bd3066b5ff0e3 | chunk: 2ad38f6d5c32b40a | strength: statutory
obligated(director_of_social_security_department, institutes_and_pension_funds, judge_technical_administrative_matters_with_appeal_to_superi).

% atom_id: 41569670413dd0bc | chunk: 2adcd6e56b450378 | strength: statutory
obligated(employee, none, appear_personally_or_through_representatives).

% atom_id: ddf92d1695141879 | chunk: 2adcd6e56b450378 | strength: statutory
obligated(employer, none, appear_personally_or_through_representatives).

% atom_id: d404bf8f9b901e6c | chunk: 2adcd6e56b450378 | strength: statutory
obligated(class_sindicate, none, appear_personally_or_through_representatives).

% atom_id: 02877e5db221b5a4 | chunk: 2b1f2af32ac28f50 | strength: statutory
obligated(employer, worker, specify_hourly_wage_in_contract).

% atom_id: 12fe1e09a2359b09 | chunk: 2b1f2af32ac28f50 | strength: statutory
prohibited(employer, worker, set_hourly_wage_below_minimum).

% atom_id: b46a1fe29e227aad | chunk: 2b3ced76a6a83a3d | strength: statutory
obligated(tribunal_regional, secretaria, have_secretariat_directorship).

% atom_id: b136222916fd8ae0 | chunk: 2b3ced76a6a83a3d | strength: statutory
obligated(state, secretaria_director, provide_function_gratification).

% atom_id: c043c564fda1936d | chunk: 2b7f890872f0cb3f | strength: statutory
obligated(employer, employee, provide_technological_infrastructure_for_remote_work).

% atom_id: 80c18222eafdd301 | chunk: 2b7f890872f0cb3f | strength: statutory
obligated(employer, employee, reimburse_remote_work_expenses).

% atom_id: 5153508ff7133db4 | chunk: 2b7fa38f17b33ea9 | strength: statutory
obligated(president_of_the_superior_labor_tribunal, parties_in_dispute, judge_resource_cases_pre_social_security_organic_law).

% atom_id: 2163adec9b9a43f5 | chunk: 2c6464beea64f421 | strength: statutory
obligated(state, president, be_natural_born_brazilian_citizen).

% atom_id: 0138d4f57a53650a | chunk: 2c6464beea64f421 | strength: statutory
obligated(state, administration_and_representation_positions, be_brazilian_citizen).

% atom_id: f1d83268cafbe081 | chunk: 2c91fabb3fd447fd | strength: statutory
prohibited(professional, none, reveal_impropriety).

% atom_id: c0f30d333c242c5c | chunk: 2c91fabb3fd447fd | strength: statutory
prohibited(professional, none, give_false_testimony).

% atom_id: c94542c88f0fd278 | chunk: 2c91fabb3fd447fd | strength: statutory
prohibited(professional, none, breach_professional_confidentiality).

% atom_id: 219614cb4bd3d66a | chunk: 2c91fabb3fd447fd | strength: statutory
prohibited(professional, none, promote_falsifications).

% atom_id: dc22dfd1f4ae843b | chunk: 2ca394bd84017c23 | strength: statutory
obligated(employee, none, observe_employer_instructions).

% atom_id: da0f1c0422a6b11a | chunk: 2cfe75da5b2223ef | strength: statutory
prohibited(employer, worker, suspend_for_more_than_30_days_consecutively).

% atom_id: 46316016dd6affef | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_type(utilidade_publica).

% atom_id: e98cf5da92d591e8 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(armazens_de_generos_alimenticios).

% atom_id: 7156ef82c870b5b9 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(abatedouros).

% atom_id: 13e77d854210dbdb | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(padarias).

% atom_id: 3a37c9cc61643e14 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(leiterias).

% atom_id: b304e521260c03ec | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(farmacias).

% atom_id: 9af043e45129b811 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(hospitais).

% atom_id: 56555c2dac944d01 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(minas).

% atom_id: e10690ca5e27a9fd | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(empresas_de_transportes).

% atom_id: dc20b4fdec76808c | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(empresas_de_comunicacoes).

% atom_id: 35e388d89edc6253 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(bancos).

% atom_id: 277b1d7594e96427 | chunk: 2d1f104eabb907ee | strength: statutory
obligated(state, public, treat_as_public_services) :-
    service_location(estabelecimentos_que_interessam_a_seguranca_nacional).

% atom_id: 30e4f81465a819a2 | chunk: 2d4176798e48277e | strength: statutory
obligated(ministry_of_work_industry_and_commerce, establishment, adapt_to_safety_requirements).

% atom_id: 6a6497878536e968 | chunk: 2d4176798e48277e | strength: statutory
obligated(ministry_of_work_industry_and_commerce, state_authority, set_deadline_for_professional_card_obligation).

% atom_id: 0de30f6621df1939 | chunk: 2d48703369d80163 | strength: statutory
obligated(socio_retirante, demais_socios, responder_solidariamente) :-
    fraude(true).

% atom_id: f0587ae807f821ec | chunk: 2d535b909b5e84c3 | strength: statutory
prohibited(employer, worker, terminate_employment_contract) :-
    reason_for_termination(marriage_or_pregnancy).

% atom_id: 9d19832e01bd4f94 | chunk: 2e1c5abce7146874 | strength: statutory
obligated(state, citizen, participate_in_home_acquisition_concurrencies) :-
    program_type(national_housing_plan).

% atom_id: 7b692c0392302b4e | chunk: 2e32547a2c48f580 | strength: statutory
obligated(employer, worker, provide_correct_seating) :-
    task_requirement(working_sitting).

% atom_id: 0282295be2c83762 | chunk: 2e338ef3e1845d7f | strength: statutory
obligated(state, judicial_representatives_and_suplentes, receive_classist_representation_gratification) :-
    monthly_sessions_attendance(X_0), X_0 <= 15.

% atom_id: eda07a083bdf98d3 | chunk: 2e3dc6831f18892a | strength: statutory
prohibited(representative_of_employers, none, act_as_representative_professionally) :-
    violation_amount(X_0), X_0 >= 100,
    violation_amount(X_1), X_1 <= 1000.

% atom_id: 6843bd48a2414338 | chunk: 2e3dc6831f18892a | strength: statutory
prohibited(representative_of_employers, none, act_as_representative_professionally) :-
    violation_amount(X_0), X_0 > 1000.

% atom_id: addf5a9434b44577 | chunk: 2e73a6fd5faaf27d | strength: statutory
obligated(employer, worker, pay_salary_in_cash).

% atom_id: 6fcb553da6e87dad | chunk: 2ec527199df73b85 | strength: statutory
obligated(employer, worker, maintain_contractual_rights_during_insolvency).

% atom_id: 405fbf74bf27889d | chunk: 2ecc99f0a700a351 | strength: statutory
permitted(recognized_chemists_union, public, assist_in_fiscalization) :-
    union_recognition_status(deemed_valid).

% atom_id: 2ff360dc5a4ff1aa | chunk: 2ee505ff8a5d1d32 | strength: statutory
obligated(employer, worker, provide_superior_nighttime_compensation).

% atom_id: c2cd52be563999d0 | chunk: 2f05d6c39f4ce416 | strength: statutory
obligated(authority, public, charge_fee_for_legal_documents).

% atom_id: 0c8255cb16018f9e | chunk: 2f43ef4684dddc05 | strength: statutory
obligated(ministry_of_labor_industry_and_commerce, public, issue_instructions_for_consolidation_execution).

% atom_id: e4ad81d41cc8abd2 | chunk: 2fb4cb0defce87d3 | strength: statutory
obligated(employer, worker, extend_working_hours_within_limit) :-
    hours_exceeded_in_one_day(X_0), X_0 <= 2,
    weekly_hours_limit(48).

% atom_id: 3da1cb8a8203af95 | chunk: 2fb4cb0defce87d3 | strength: statutory
permitted(employer, worker, extend_working_hours_without_overtime_pay) :-
    collective_agreement(true).

% atom_id: 648eab5982fcf165 | chunk: 2fb4cb0defce87d3 | strength: statutory
obligated(employer, worker, compensate_excess_hours_in_one_day_with_less_hours_another_d).

% atom_id: 2e85c828233f75cb | chunk: 304aa176d9fa6ab4 | strength: statutory
obligated(judge_or_president, legal_case, issue_decision_within_five_days) :-
    testimonies_in_defense(not_arrested).

% atom_id: b6f4b73b70a77295 | chunk: 3060899485ff6cd3 | strength: statutory
obligated(sus_manager, public, superintend_all_tribunal_services).

% atom_id: 79c12a993f76defc | chunk: 30684d37b1bcd0e3 | strength: statutory
obligated(parties, none, argue_nullities_first_opportunity) :-
    opportunity_to_speak(first_in_hearing_or_records).

% atom_id: 1b24b0b5d3dc3e62 | chunk: 30684d37b1bcd0e3 | strength: statutory
prohibited(judiciary, none, declare_nullities_without_proceeding).

% atom_id: c8c96355d45e6f16 | chunk: 306bd4f0a881673f | strength: statutory
permitted(authority, public, authorize_seizure_on_holiday) :-
    day_type(holiday).

% atom_id: 814a1867c0607598 | chunk: 30bf1269badd18c0 | strength: regulatory
obligated(ministry_of_labor_industry_and_commerce, worker, approve_career_structure_with_antiquity_access) :-
    career_structure(organized_in_hierarchy),
    antiquity_access(guaranteed).

% atom_id: 890c1e85ce80696e | chunk: 30d5c8b72a7b5381 | strength: statutory
prohibited(employee, none, unjustified_refusal_to_work).

% atom_id: 9b07e85ea8e6596b | chunk: 314ea7ccd30cc0fb | strength: regulatory
permitted(authority, union_member, require_contributions_from_union_members).

% atom_id: 543307639e17e372 | chunk: 31c36bef2bb9e657 | strength: statutory
obligated(state, foreigner, grant_equivalent_rights_to_brazilians) :-
    residency_duration(X_0), X_0 >= 10,
    marriage_or_child_citizenship(true).

% atom_id: a5e5e4a7f38abd63 | chunk: 31c36bef2bb9e657 | strength: statutory
obligated(state, portuguese_national, grant_equivalent_rights_to_brazilians).

% atom_id: 3014c823b7288ac9 | chunk: 31ca79200ccc7bb9 | strength: statutory
obligated(president_of_junta, none, receive_fixed_salary_by_law).

% atom_id: 9e1d91fcd63da98d | chunk: 31d592925cedc399 | strength: statutory
prohibited(deployer, none, reincidir_embaracar_resistir_fiscalizacao) :-
    type_of_infraction(reincidencia_embaraco_ou_resistencia_a_fiscalizacao).

% atom_id: d87d435d69c699d8 | chunk: 31d592925cedc399 | strength: statutory
prohibited(deployer, none, usar_artificio_simulacao_fraude_lei) :-
    type_of_infraction(emprego_de_artificio_ou_simulao_com_o_objetivo_de_fraudar_a).

% atom_id: 8df2dcbb033bccbd | chunk: 322f26e04c0ffbf8 | strength: statutory
obligated(worker, none, pay_contributive_tax) :-
    professional_status(autonomous_worker).

% atom_id: 4d085c5b23bc6c43 | chunk: 322f26e04c0ffbf8 | strength: statutory
obligated(executive_power, none, fix_reference_value).

% atom_id: 50da517b8577626e | chunk: 3238e128e2290208 | strength: statutory
obligated(procurator_general, secretariat_of_the_procurator_general, direct_secretariat_operations).

% atom_id: 76c7f9566fe04951 | chunk: 3238e128e2290208 | strength: statutory
obligated(ministry_of_labor_industry_and_commerce, secretariat_of_the_procurator_general, appoint_staff_for_secretariat).

% atom_id: 9726d6d57bdbfca0 | chunk: 32423b251c9d5f2e | strength: statutory
prohibited(employer, foreign_worker, hire_without_valid_identification).

% atom_id: 84cb9bd65f2a22da | chunk: 3299c5cf2fc3c622 | strength: statutory
obligated(employer, worker, readmit_worker) :-
    lack_of_serious_offense(false).

% atom_id: c8363247e7e09eb2 | chunk: 3299c5cf2fc3c622 | strength: statutory
obligated(employer, worker, pay_salaries_during_suspension) :-
    lack_of_serious_offense(false).

% atom_id: 31bb5696c66ddffb | chunk: 32b5b23ce07a2792 | strength: statutory
obligated(employer, employee, pay_daily_penalty).

% atom_id: c7bb1996d64f16da | chunk: 32bc7b5b23466ab0 | strength: statutory
obligated(commission_of_sindical_tax, worker, apply_social_fund_in_workers_interests).

% atom_id: e78553c29c1948ef | chunk: 32c1acb01d6f9bb8 | strength: regulatory
obligated(worker, public_company, admit_in_public_services).

% atom_id: 03173e396a968e6b | chunk: 32ef3f5aadfdbd6b | strength: statutory
prohibited(employer, worker, reduce_salary_due_to_application_of_precepts).

% atom_id: 246da4d5a0a837d6 | chunk: 32fe2c71dac66bda | strength: regulatory
obligated(employer, worker, pay_integral_work_verbal_rights).

% atom_id: 710cef8c600e7789 | chunk: 32fe3cc4cf39959e | strength: statutory
prohibited(collective_agreement, worker, suppress_or_reduce_worker_rights).

% atom_id: 8a45d7b48bead7c0 | chunk: 330a0d8d540daea0 | strength: statutory
prohibited(deployer, none, conduct_non_specified_activities) :-
    activity_type(non_compliant_with_article_511).

% atom_id: f3f3a5842cf2b916 | chunk: 330a0d8d540daea0 | strength: statutory
prohibited(deployer, none, conduct_political_party_activities).

% atom_id: ecfaffe98ffc2a48 | chunk: 3314cbbb5f2d1517 | strength: statutory
prohibited(employer, workplace, present_saliences_or_depressions).

% atom_id: 3f0d273e2d62ccd8 | chunk: 3337e2db71a2365f | strength: statutory
permitted(worker, none, appeal_decisions_of_competent_bodies_in_social_security_matt).

% atom_id: 84e496c81bc08d82 | chunk: 3337e2db71a2365f | strength: statutory
permitted(worker, none, request_review_of_decisions_by_superior_social_security_coun).

% atom_id: 3a6589705bfa57b3 | chunk: 33560498fc77e366 | strength: statutory
obligated(authority, candidate, appoint_as_substitute_judge).

% atom_id: e1c7a5a5a518fe95 | chunk: 33560498fc77e366 | strength: statutory
obligated(authority, candidate, appoint_by_promotion_alternately).

% atom_id: 6a40f8b806ed93e4 | chunk: 33560498fc77e366 | strength: statutory
obligated(authority, candidate, appoint_by_antiquity_and_merit).

% atom_id: e0bbd0879361e8cc | chunk: 33619e72544ae049 | strength: statutory
obligated(ministry_of_labor_and_employment, none, regulate_hazardous_activities).

% atom_id: b0c74fe8d1ea56fd | chunk: 3395deeec04676d6 | strength: regulatory
obligated(collective, convenants, suggest_resolution_for_disputes).

% atom_id: f75d4f81cb9e3e9f | chunk: 339bfa38275e9139 | strength: statutory
prohibited(collective, public, propagate_incompatible_doctrines).

% atom_id: cf5c629e11de513d | chunk: 339bfa38275e9139 | strength: statutory
prohibited(collective, public, run_ineligible_candidacies) :-
    candidacy_origin(outsider_to_union).

% atom_id: f299dca291f1a926 | chunk: 33ecfe76584df538 | strength: statutory
obligated(president_of_the_regional_court, vogal_of_juntas, appoint_vogals_to_juntas).

% atom_id: a54fac1f20cfc788 | chunk: 33f56c940479a299 | strength: statutory
obligated(employer, worker, provide_minimum_rest_period_between_shifts).

% atom_id: fe554fb7f1a58afa | chunk: 343f289228cf8de4 | strength: statutory
obligated(employer, woman_employee, provide_special_rest_periods_for_breastfeeding) :-
    child_age_months(X_0), X_0 <= 6.

% atom_id: e2fe2ddf69293081 | chunk: 34547b53f3c5fb48 | strength: regulatory
obligated(authority, worker, impose_fine_for_labor_violations).

% atom_id: de9e0d8a963bf53b | chunk: 34547b53f3c5fb48 | strength: regulatory
obligated(authority, worker, grant_recourse_to_director_general_of_labor_department_or_se).

% atom_id: 7e82a2004ae7aed9 | chunk: 34c40d8d81828826 | strength: statutory
obligated(employer, worker, compensate_overtime_work).

% atom_id: 3583f5b16c6f494b | chunk: 34d1476f46a64165 | strength: statutory
obligated(employer, worker, minimize_offense_effective_effort).

% atom_id: a567ca1f74213a44 | chunk: 34d1e5159a64464a | strength: statutory
obligated(authority, employer, decide_on_transfer_refusal) :-
    employee_action(refuse_transfer).

% atom_id: 2e57516ce4af6b21 | chunk: 34da0aa50ab52fa9 | strength: statutory
obligated(employer, child, certify_necessity_of_employment_for_subsistence) :-
    necessity_of_employment(indispensable_to_own_or_family_substance),
    moral_harm(yes).

% atom_id: bf279768e0709dc6 | chunk: 350c18d0b661c3d9 | strength: statutory
permitted(company, none, establish_prior_conciliation_committees).

% atom_id: b6590f9a7ff9ca93 | chunk: 350c18d0b661c3d9 | strength: statutory
permitted(union, none, establish_prior_conciliation_committees).

% atom_id: e835a6335df668e7 | chunk: 350c18d0b661c3d9 | strength: statutory
permitted(prior_conciliation_committees, none, have_intersindical_character).

% atom_id: eee24588d0625d3b | chunk: 3578fd422f546be7 | strength: statutory
obligated(employer, worker, employ_brazilian_workers_proportionally).

% atom_id: 2d3663ba7e76cb97 | chunk: 3578fd422f546be7 | strength: statutory
permitted(executive_authority, employer, set_lower_worker_proportion) :-
    special_circumstances(special_circumstances).

% atom_id: 5c61b210865207d2 | chunk: 3578fd422f546be7 | strength: statutory
obligated(executive_authority, employer, investigate_worker_shortage) :-
    special_circumstances(special_circumstances).

% atom_id: 7a900510d1117a59 | chunk: 361736f8cb75b1de | strength: statutory
permitted(association, work_dispute, represent_to_institute_instance) :-
    suspension_of_work(true).

% atom_id: f3ec379b4166f44a | chunk: 3618e8bf6a6f6122 | strength: statutory
obligated(authority, case_file, maintain_two_ficharios).

% atom_id: 60d226c6e35a2653 | chunk: 3632187d24fc99f4 | strength: regulatory
obligated(ministry_of_labor, secretariat, designate_staff).

% atom_id: 6ad604295ec5a50b | chunk: 3655a9d1a005967f | strength: statutory
obligated(employer, worker, compute_as_effective_work_time) :-
    employee_status(at_road_disposal).

% atom_id: 91de121f0ad33755 | chunk: 3686a4a07a31836e | strength: regulatory
obligated(procurador, none, designate_substitute_procurator).

% atom_id: b8d2cf89aaea238d | chunk: 3695d09f32c39fb2 | strength: statutory
obligated(labor_judiciary, worker, execute_social_contributions) :-
    sentence_type(judgment),
    sentence_type(agreement).

% atom_id: 5adef024633f8514 | chunk: 36a68d0ed9eaffc9 | strength: statutory
obligated(employer, worker, guarantee_daily_wage_minimum) :-
    salary_adjustment_method(empreitada),
    salary_adjustment_method(tarefa),
    salary_adjustment_method(peca).

% atom_id: b0c70c3b555784c8 | chunk: 36e5ae6b7a38ad26 | strength: statutory
permitted(judge_or_president_of_court, none, execute_decisions) :-
    conciliation_or_judgment_origin(self).

% atom_id: 30bc18a11bb66ac7 | chunk: 37265f9c7ef269ea | strength: statutory
obligated(central_sindical, none, use_resources_for_representation_activities).

% atom_id: 32fd12d8071db396 | chunk: 372ae80df4f6876d | strength: statutory
obligated(authority, none, approve_cost_tables).

% atom_id: 11e6f1a252ef8e34 | chunk: 3795b3b939cd1c10 | strength: statutory
prohibited(employer, worker, pay_salary_without_compliance).

% atom_id: c3ef3a2bbb712689 | chunk: 37a0e04e4083a892 | strength: statutory
permitted(vogal_juntas, none, enjoy_prerrogatives_ensured_to_jurors) :-
    investidura_duration(ongoing).

% atom_id: 20b1d667ed67bd42 | chunk: 3846ad36647a5ba1 | strength: statutory
obligated(association, tribunal_superior_do_trabalho_president, submit_candidate_lists_for_vocational_and_supplementary_posi).

% atom_id: 276faa9c416de145 | chunk: 390c7ceaeaf8aa7e | strength: statutory
permitted(worker, none, prove_individual_labor_contract).

% atom_id: 9f12423271690211 | chunk: 39232a4e0ef11531 | strength: statutory
obligated(employer, worker, provide_rest_period).

% atom_id: c522578248bd9b12 | chunk: 39344c6889a19180 | strength: statutory
obligated(conseil_federal, member_of_the_superior_labor_court, impose_executions).

% atom_id: 662df952fac87eaf | chunk: 39a843aa1c7ef202 | strength: statutory
obligated(authority, worker, determine_jurisdiction_of_conciliation_and_judgment_bodies) :-
    work_location(locality).

% atom_id: 13e4444678d3f71d | chunk: 39b6c72581c1bc2a | strength: statutory
obligated(employer, employee, transfer_to_follow_spouse_or_partner) :-
    spouse_or_partner_employment_status(public_servant),
    spouse_or_partner_transfer_reason(administrative_interest).

% atom_id: 84396c276ca2b4c8 | chunk: 39daec35851564a9 | strength: statutory
permitted(minister_of_labor_industry_and_commerce, institutions_of_social_security, avocate_administrative_issues) :-
    public_interest(true).

% atom_id: aa87212e8783d1b7 | chunk: 39f261688bf56c9a | strength: statutory
obligated(company_director, employee, organize_shifts_for_workers).

% atom_id: caf571bece899e2b | chunk: 3a532fb913afcfdd | strength: statutory
permitted(procurador_geral, procuratoria_da_previdencia_social, appoint_secretary_chief).

% atom_id: d592fd081ac15390 | chunk: 3a608a369d4a572a | strength: statutory
obligated(state, public, guarantee_non_exploitation_of_economic_activity_by_public_en).

% atom_id: 0713457c37ee28ed | chunk: 3a652709f742c3e2 | strength: statutory
obligated(employer, minor_worker, comply_with_work_rules_for_minors) :-
    work_environment(family_business),
    supervisor_relationship(parent_or_tutor).

% atom_id: c3fb8286c848f600 | chunk: 3a6904f510e9f355 | strength: statutory
obligated(employer, woman_worker, provide_superior_nighttime_wage).

% atom_id: dce94ccb99a4c115 | chunk: 3a90bd576871d439 | strength: statutory
obligated(president_of_the_court, court_instance, instaurate_instance_through_written_representation) :-
    representation_type(written).

% atom_id: 786e700e7eb4eea8 | chunk: 3a90bd576871d439 | strength: statutory
permitted(president_of_the_court, court_instance, instaurate_instance_initiative).

% atom_id: 39ff7416e4007b19 | chunk: 3a90bd576871d439 | strength: statutory
permitted(procurator_of_the_labor_justice, court_instance, request_instaurate_instance) :-
    work_suspension_occurrence(true).

% atom_id: d542c538b47a9481 | chunk: 3ab764c551d6a3f2 | strength: statutory
obligated(authority, none, follow_nomination_procedures) :-
    article_reference(arts744_and_745).

% atom_id: c7edad25200351fc | chunk: 3b8f252f55c9283a | strength: statutory
prohibited(collective, none, unprofessional_behavior) :-
    behavior(conduta),
    evidence(devidamente_comprovada).

% atom_id: 8149d5e4849889e6 | chunk: 3b92d67210acd7a2 | strength: statutory
obligated(authority, none, decide_homologation_of_extrajudicial_agreement).

% atom_id: dd4ef195b2e0e6c7 | chunk: 3bb83bb8a39d7a64 | strength: statutory
permitted(employee, none, consider_contract_rescinded_and_claim_indemnity) :-
    contract_status(rescindible).

% atom_id: 908aa2517998a8e5 | chunk: 3bc02cd701a89ba9 | strength: regulatory
permitted(industrial_enterprise_artesanal, none, constitute_separate_sindicals_entities).

% atom_id: 8db124dc0c0d65c5 | chunk: 3bc2d7cd5026f4b6 | strength: statutory
prohibited(worker, none, serve_on_same_junta_with_incompatible_relations) :-
    relation_type(consanguineous_or_affinity_up_to_third_degree_civil).

% atom_id: df487263e0c205eb | chunk: 3c195cefbb07d52e | strength: statutory
obligated(authority, worker, confer_collective_dispute_jurisdiction).

% atom_id: 3dd3d240184b2a67 | chunk: 3c195cefbb07d52e | strength: statutory
obligated(authority, worker, extend_or_reconsider_normative_decisions) :-
    cases(previsto_em_lei).

% atom_id: 7ae2888ac885e1be | chunk: 3c6422bdd9c8f686 | strength: statutory
obligated(procuradoria_justia_trabalho, employer, judicial_collection_of_fines) :-
    location(distrito_federal),
    tribunal_regional_trabalho_functioning(true).

% atom_id: fa2c333779cd0e2a | chunk: 3c6422bdd9c8f686 | strength: statutory
obligated(ministrio_pblico_estadual_territorio_acre, employer, judicial_collection_of_fines) :-
    location(outros_localidades).

% atom_id: 1af845e7222f51a8 | chunk: 3c931b8a566be10b | strength: statutory
obligated(officials_of_justice, none, carry_out_executive_judgments_orders).

% atom_id: f329a834f3284ed8 | chunk: 3d302a077949e576 | strength: statutory
obligated(union_representative, employee, forward_specific_grievances).

% atom_id: 4c33f7366fbd0420 | chunk: 3d57da87ba98b57f | strength: statutory
obligated(employer, employee_with_disability_or_young_child_in_custody, prioritize_allocation_to_remote_work) :-
    age_of_dependent_children(X_0), X_0 <= 4.

% atom_id: a87014da1bca7e45 | chunk: 3d57ebe09aafb314 | strength: statutory
prohibited(reclamante, none, cause_archiving_under_article_844) :-
    occurrences(2).

% atom_id: 819b636335840804 | chunk: 3d659d196870ba9f | strength: statutory
prohibited(authority, procurador_geral_and_procuradores, subject_to_duty_roster).

% atom_id: 6153b1337fc19237 | chunk: 3d8d24a8392e1ae2 | strength: statutory
obligated(collective, public, collaborate_to_protect_legal_rights).

% atom_id: e389c37235598752 | chunk: 3db23d7129ce6cfe | strength: statutory
obligated(employer, worker, seek_conflict_resolution_in_labor_relations).

% atom_id: a2c5131b78d95c9c | chunk: 3e06e19b95342079 | strength: statutory
obligated(court, party, receive_grievance_petition) :-
    justification_provided(true),
    matters_and_values_delimited(true).

% atom_id: b808126470c9c7ad | chunk: 3e06e19b95342079 | strength: statutory
permitted(court, party, execute_immediately_remaining_part) :-
    grievance_petition_received(true).

% atom_id: 1c1f836e458d4ce0 | chunk: 3e1ae6bff39dd684 | strength: statutory
prohibited(worker, none, infringe_minimum_wage_law).

% atom_id: 1206ec5883e04b75 | chunk: 3e1ae6bff39dd684 | strength: statutory
prohibited(worker, none, reinfringe_minimum_wage_law).

% atom_id: 68f10fec3368f606 | chunk: 3e57560536bf8774 | strength: regulatory
obligated(authority, none, review_quadro_bienally).

% atom_id: 0f58f4875d490aa9 | chunk: 3eb4bae46c92b298 | strength: statutory
prohibited(employer, worker, grant_vacation_rights) :-
    course_of_acquisition_period(true).

% atom_id: 74f0c6c41fc45f75 | chunk: 3ec2d0454b2f1475 | strength: statutory
obligated(employer, worker, provide_equal_salary) :-
    function(identical),
    work_value(equal),
    employer(same),
    establishment(same).

% atom_id: 32d006ff3e5736ef | chunk: 3ef80a1e9603c1c8 | strength: statutory
obligated(distributor, interested_party, provide_receipt).

% atom_id: f7b0ca3e1ce10471 | chunk: 3f10bd8f59638a00 | strength: statutory
obligated(authority, infractor, deliver_infraction_notice) :-
    days_since_lavrar_infracao(X_0), X_0 <= 10.

% atom_id: ba4f66a0eb88df2b | chunk: 3f32ccefb370d055 | strength: statutory
obligated(authority, vogal_junta_secretario_demais_funcionarios, grant_posse_to_vocals_secretary_and_other_staff).

% atom_id: 2290764c64b0323d | chunk: 3f34e8d55e9c6ba6 | strength: statutory
obligated(court, citizen, judge_aggravated_orders_of_president) :-
    case_type(previsto_em_lei).

% atom_id: 58ec3f7cc5a1cc0b | chunk: 3f84025fc0945591 | strength: statutory
obligated(authority, public, exercise_jurisdictional_attributes).

% atom_id: 2b167a07b597c95d | chunk: 3fa0bf921598915f | strength: statutory
obligated(authority, judicial_authority, promote_executive_court_collection_of_fines).

% atom_id: 8b32e9235f89631f | chunk: 3fa16a910853d02c | strength: statutory
obligated(judge_or_president, audiencia, declare_open_audiencia).

% atom_id: 17700164622e553b | chunk: 3fa16a910853d02c | strength: statutory
obligated(secretary_or_writ_clerk, parties_testimonies_others, call_parties_testimonies_others).

% atom_id: eb16cdd797c70fca | chunk: 3fc772af3a14dfa6 | strength: statutory
prohibited(judge, legal_proceeding, issue_verdict_in_violation_of_federal_law_or_constitution).

% atom_id: 47a4ca89e9167a16 | chunk: 3fd7c842ca38b318 | strength: statutory
prohibited(employer, worker, contract_wage_below_minimum).

% atom_id: fdb034a8c26620d7 | chunk: 40d59df4c22a9ecc | strength: statutory
obligated(employee, none, perform_any_compatible_service) :-
    proof_of_clause(absent).

% atom_id: ba59b21b20c2ca16 | chunk: 41212b048770e1a9 | strength: statutory
obligated(authority, none, issue_precatoriais).

% atom_id: 14743356391ab548 | chunk: 41212b048770e1a9 | strength: statutory
obligated(authority, none, comply_with_precatoriais).

% atom_id: 7b31a00a43b0459a | chunk: 417a8235a021c8ed | strength: statutory
obligated(employer, worker, apply_special_work_regime_six_hours) :-
    job_role(porter_or_cleaning_staff).

% atom_id: 8b0777e476be7670 | chunk: 41c2c972ba420342 | strength: regulatory
obligated(employer, worker, restablish_reduced_salaries) :-
    force_majeure_effects_ended(true).

% atom_id: c4c3faf218c819f5 | chunk: 42f72843b519286c | strength: statutory
permitted(employee, none, file_labor_claim_personally).

% atom_id: aaa16e460137677e | chunk: 42f72843b519286c | strength: statutory
permitted(employer, none, file_labor_claim_personally).

% atom_id: 262d6145a508b9f9 | chunk: 42f72843b519286c | strength: statutory
permitted(employee, none, follow_claim_until_completion).

% atom_id: a580bdfe29011549 | chunk: 42f72843b519286c | strength: statutory
permitted(employer, none, follow_claim_until_completion).

% atom_id: a28214635070f431 | chunk: 4321b53eef8571be | strength: statutory
prohibited(employee, none, refuse_drug_and_alcohol_testing).

% atom_id: 72b6ceb5043a5338 | chunk: 4330f3bfc8e941a5 | strength: regulatory
obligated(requerente, none, exhibit_documents_for_registration).

% atom_id: 741cdb96a315865e | chunk: 433ff4038d1a2172 | strength: statutory
prohibited(employer, child, employ_minor) :-
    age(X_0), X_0 < 16.

% atom_id: ec549ada4940bacf | chunk: 433ff4038d1a2172 | strength: statutory
permitted(employer, child, employ_minor_as_apprentice) :-
    age(X_0), X_0 >= 14.

% atom_id: 2040a638aa8bf0b9 | chunk: 4352ff56a74f6932 | strength: statutory
prohibited(employer, employee, maintain_employee_in_irregular_situation) :-
    infraction_type(employment_violation).

% atom_id: a310c56df6ef515c | chunk: 44185b3cb6952801 | strength: statutory
obligated(employer, minor_worker, apply_work_restrictions_for_minors).

% atom_id: 7e2b414590e4249b | chunk: 44465461cb96e9ba | strength: statutory
obligated(worker, public, perform_assigned_tasks).

% atom_id: a777b6cc14f18c94 | chunk: 444f4ed08ae7d2ee | strength: statutory
obligated(president, junta_secretariat, appoint_director).

% atom_id: 4c4a1e85a055bb7e | chunk: 44a4a49ca27b6a9c | strength: statutory
obligated(authority, person, provide_information_about_cases) :-
    request_method(verbal_or_certificate).

% atom_id: effb0b834bdbb804 | chunk: 44d6e20bdedf93ae | strength: statutory
obligated(employer, worker, pay_minimum_wage_to_home_worker).

% atom_id: d078e86995a96910 | chunk: 44f0b5aa59ea94b0 | strength: regulatory
obligated(provider, public, pay_registration_fee).

% atom_id: 8889bc07d5fc7de4 | chunk: 4525fa1fae082708 | strength: statutory
obligated(employer, worker, provide_compulsory_rest_day) :-
    work_days(6).

% atom_id: fc167c2cf6ba2034 | chunk: 4525fa1fae082708 | strength: statutory
permitted(employer, worker, agree_on_alternative_rest_day) :-
    agreement(written).

% atom_id: 5d2858fdbb9823bd | chunk: 453916c4769e5626 | strength: statutory
obligated(authority, debtor, penhor_bens_executive_proceeding) :-
    payment_status(not_paid),
    guarantee_status(not_provided).

% atom_id: 5306585077fa4f1a | chunk: 458c8f14f0e68ca7 | strength: statutory
obligated(worker, tribunal_superior_do_trabalho, attend_sessions_personally_or_through_designated_procurator).

% atom_id: 834bad573fcd2014 | chunk: 459b7d612ed14682 | strength: statutory
obligated(authority, previdencia_social, decide_issues).

% atom_id: 35427dafff9f22b4 | chunk: 4667960f33a5183f | strength: statutory
prohibited(reclamante, none, not_attend_hearing).

% atom_id: 1f0912d8da670070 | chunk: 46a182e1b5ac3a94 | strength: statutory
obligated(employer, employee, terminate_employment_for_threat_to_national_security) :-
    threat_to_national_security(true),
    evidence(decently_proven_in_administrative_inquiry).

% atom_id: 76f61e79eff14bcc | chunk: 46d1765d719927da | strength: statutory
obligated(authority, worker, process_complaints_against_administrative_acts) :-
    actor(presidente),
    target(authority_member_or_judge_or_staff).

% atom_id: 67987273f2ddd26d | chunk: 46d937addbf6f301 | strength: statutory
obligated(court, litigant, suspend_prescriptive_period) :-
    type_of_request(homologation_petition),
    agreement_type(extrajudicial_agreement).

% atom_id: d5d0cc34bd26ab55 | chunk: 475bf06b11d67f5f | strength: statutory
obligated(subcontractor, worker, respond_for_work_contract_obligations).

% atom_id: 906a3d634ca7d272 | chunk: 475bf06b11d67f5f | strength: statutory
permitted(worker, principal_contractor, claim_against_principal_contractor_for_non_payment) :-
    non_payment_by_subcontractor(true).

% atom_id: 8f11ffa89e193549 | chunk: 47cdef6c1db40ced | strength: statutory
prohibited(worker, none, alter_fact_truth).

% atom_id: df8ef010e4469b00 | chunk: 47ef5b17170ae47f | strength: statutory
permitted(deployer, worker, operate_on_sunday) :-
    nature_of_activity(domingo),
    public_convenience(true).

% atom_id: 4d5ded3fa7cf8227 | chunk: 47ef5b17170ae47f | strength: statutory
obligated(authority, deployer, specify_activities_for_sunday_operation) :-
    nature_of_activity(domingo),
    public_convenience(true).

% atom_id: 3520ccb44b703d13 | chunk: 47ef5b17170ae47f | strength: statutory
permitted(deployer, worker, operate_temporarily_on_sunday) :-
    nature_of_activity(outros),
    public_convenience(false).

% atom_id: c946afe9c77e77fc | chunk: 47ef5b17170ae47f | strength: statutory
obligated(authority, deployer, grant_temporary_permission_for_sunday_operation) :-
    nature_of_activity(outros),
    public_convenience(false).

% atom_id: 0fdd904d3df37964 | chunk: 47ef5b17170ae47f | strength: statutory
prohibited(deployer, worker, operate_temporarily_on_sunday_for_more_than_60_days) :-
    nature_of_activity(outros),
    public_convenience(false).

% atom_id: a86accb79a811215 | chunk: 47faa1588dfefeec | strength: statutory
obligated(employer, worker, provide_personal_protection_equipment).

% atom_id: 278749cc26fe3ea9 | chunk: 4811cc45417d8aea | strength: statutory
obligated(worker, none, submit_written_claim_with_documents).

% atom_id: 91acfb4938da618c | chunk: 488d17f01b8929c0 | strength: statutory
prohibited(employer, none, violate_medical_work_requirements).

% atom_id: ff2a946f9985f94e | chunk: 488d17f01b8929c0 | strength: statutory
prohibited(employer, none, violate_safety_work_requirements).

% atom_id: 1ffa115596a6f8ca | chunk: 48aba4dfdb864706 | strength: statutory
obligated(authority, public, levy_fee_on_auction_documents) :-
    document_type(auction_document).

% atom_id: 713d5dd06ca9d751 | chunk: 48c7be41eace8aa1 | strength: statutory
obligated(employer, none, recollect_sindical_contribution) :-
    month(january).

% atom_id: f0ed593163015cbb | chunk: 48c7be41eace8aa1 | strength: statutory
obligated(employer, none, recollect_sindical_contribution) :-
    establishment_date(january),
    registration_request(true).

% atom_id: 94cf3ce8d64f238f | chunk: 49096744e045a0ff | strength: statutory
obligated(authority, vogal_juntas, receive_gratification_for_attendance) :-
    attendance_frequency(X_0), X_0 <= 20,
    time_period(monthly).

% atom_id: 7547fb674a57533f | chunk: 4919a2b93412a21a | strength: statutory
permitted(employer, worker, reduce_salary_proportionally) :-
    force_majeure_or_loss(true).

% atom_id: 7f08cc11e8e772a2 | chunk: 4919a2b93412a21a | strength: statutory
obligated(employer, worker, respect_minimum_wage).

% atom_id: c12a04de05d3121a | chunk: 493d550997b0b6f6 | strength: statutory
obligated(authority, empoyee, issue_temporary_document) :-
    carteira_expedida(false).

% atom_id: 903bb2ca9d286d94 | chunk: 495655b9863009f9 | strength: statutory
obligated(employer, worker, provide_notice_period) :-
    payment_frequency(quinzena),
    payment_frequency(mes),
    service_duration_months(X_2), X_2 >= 12.

% atom_id: a6251c1caa6aaa46 | chunk: 49a5de3084b27a8b | strength: statutory
obligated(authority, public, register_essential_actions_in_minutes).

% atom_id: aaf5731eb89f56bf | chunk: 49cb470f0d1f114b | strength: statutory
obligated(procurador_geral, minister_of_labor, submit_annual_report_to_ministry) :-
    date(n31_mar).

% atom_id: c78a2dbe4ef7c756 | chunk: 49e3621e0f988419 | strength: statutory
obligated(judges_and_juntas, legal_cases, carry_out_procedural_acts_and_inquiries).

% atom_id: ad11f54f329db6f2 | chunk: 4a237789359805c4 | strength: statutory
obligated(employee, employer, submit_to_pre_conciliation_committee) :-
    locality_of_service_provision(established_in_company_or_union).

% atom_id: 6a64231e48712abc | chunk: 4a237789359805c4 | strength: statutory
obligated(employer_or_union, employee, establish_pre_conciliation_committee).

% atom_id: acd30267ff2be125 | chunk: 4a611998f643e738 | strength: statutory
obligated(employer, worker, calculate_hourly_wage_for_diarist) :-
    employment_type(diarista).

% atom_id: 5b4faee9816543f7 | chunk: 4aafa0fd00439710 | strength: statutory
obligated(employer, teacher, pay_during_exam_and_vacation_periods).

% atom_id: d6ec95d699953e63 | chunk: 4af9b1f677ab2e3f | strength: statutory
obligated(employer, worker, provide_rest_period_during_work_shift).

% atom_id: 68e95ecd8eb838e6 | chunk: 4b1fe476c1ff709d | strength: statutory
prohibited(employee, employer, negotiate_without_permission) :-
    nature_of_negotiation(competition_to_employer).

% atom_id: 3195aff28a783487 | chunk: 4b1fe476c1ff709d | strength: statutory
prohibited(employee, employer, negotiate_without_permission) :-
    impact_on_service(prejudicial).

% atom_id: b285f051b89e4870 | chunk: 4b53bf860517704a | strength: statutory
permitted(sindicate_of_employees, none, establish_recruitment_agency).

% atom_id: 180f7e43f5ada821 | chunk: 4c3714ca2f1f5e60 | strength: regulatory
obligated(authority, member_and_staff_of_board, sign_payroll_sheets).

% atom_id: a3a2390e3abc534d | chunk: 4c46c678dccb47f6 | strength: statutory
obligated(responsible_party, none, prepare_instruction_for_new_legislation) :-
    legislative_action_type(new_laws_regulations_or_ministerial_instructions).

% atom_id: 3b80dc7f3e69c8e8 | chunk: 4c52d88efe86c7ee | strength: regulatory
permitted(authority, person, provide_certificates_for_hearings) :-
    request(true).

% atom_id: 2cd40d32b1c07d5f | chunk: 4c575bf33d9d019a | strength: statutory
obligated(employer, worker, apply_male_labor_rules_to_female_workers) :-
    protection_conflict(false).

% atom_id: b776deae3c08dfab | chunk: 4c575bf33d9d019a | strength: statutory
obligated(employer, worker, provide_special_protection_to_female_workers) :-
    protection_conflict(true).

% atom_id: a6af37f99eb149c4 | chunk: 4c6062dadeda5766 | strength: statutory
obligated(authority, procurador, nominate_with_requirements) :-
    time_of_service(X_0), X_0 >= 2.

% atom_id: ff7d157ef1c49eef | chunk: 4c8fcb6e6b7fc744 | strength: statutory
prohibited(litigant, none, use_process_for_illegal_purposes).

% atom_id: 349dc1bfcd9201db | chunk: 4d3545045071d687 | strength: statutory
obligated(employer, worker, seek_authorization_for_overtime_in_hazardous_conditions) :-
    activity_type(hazardous).

% atom_id: 4e311cc6c3b0a4ac | chunk: 4d3545045071d687 | strength: statutory
obligated(sus_manager, employer, authorize_overtime_in_hazardous_conditions) :-
    activity_type(hazardous).

% atom_id: 193c6cf61a452288 | chunk: 4d3545045071d687 | strength: statutory
obligated(sus_manager, employer, conduct_local_examinations_in_hazardous_conditions) :-
    activity_type(hazardous).

% atom_id: db4b841bd6d976e9 | chunk: 4d3545045071d687 | strength: statutory
obligated(sus_manager, employer, verify_work_methods_in_hazardous_conditions) :-
    activity_type(hazardous).

% atom_id: 95a1dfe9e9f7486c | chunk: 4d3545045071d687 | strength: statutory
obligated(sus_manager, public_authority, coordinate_with_sanitary_authorities_for_examinations) :-
    activity_type(hazardous).

% atom_id: 17dab79bbfb3818d | chunk: 4d3545045071d687 | strength: statutory
obligated(public_authority, sus_manager, assist_in_examinations_and_verifications) :-
    activity_type(hazardous).

% atom_id: dc6954b9dc779405 | chunk: 4d3d4062a9b238d3 | strength: statutory
permitted(employee, none, file_complaint_with_authority) :-
    company_action(refusal_to_make_annotations_or_return_work_card).

% atom_id: b211fc683436acea | chunk: 4d71eadac2a5ef8f | strength: statutory
obligated(escrivao_or_secretario, autos, conclude_autos_to_judge_or_president).

% atom_id: 7be337952e93d4ff | chunk: 4d71eadac2a5ef8f | strength: statutory
obligated(judge_or_president, autos, issue_decision).

% atom_id: 894a07748641fbc5 | chunk: 4def96765d9bf6e7 | strength: statutory
obligated(tribunal_superior_do_trabalho, varas_do_trabalho_juizos_de_direito_tribunais, issue_instructions_for_payment_form_of_costs_and_fees).

% atom_id: 0d3e98605fda0c1c | chunk: 4dffd46b6193fa5d | strength: statutory
permitted(company, none, sign_collective_labor_contracts) :-
    inclusion_status(not_included).

% atom_id: 4766bd8246a7f766 | chunk: 4e40f82426a2d515 | strength: statutory
obligated(president, none, submit_for_presidential_approval_and_signing).

% atom_id: 9d485b800dc8df56 | chunk: 4e76523d9da4d31a | strength: statutory
obligated(employer, worker, provide_rested_weekend_compensation).

% atom_id: 3d625ae111d2812c | chunk: 4f48f7458e65df0c | strength: statutory
obligated(chemist, none, use_work_and_social_security_card).

% atom_id: 01c851453ae364d5 | chunk: 4f48f7458e65df0c | strength: statutory
obligated(chemist, none, register_diplomas) :-
    condition(a).

% atom_id: b6d31e979581b8d4 | chunk: 4f48f7458e65df0c | strength: statutory
obligated(chemist, none, register_diplomas) :-
    condition(b).

% atom_id: 3616cad3c31b829a | chunk: 4f55c1bbbec96039 | strength: statutory
obligated(worker, employer, pact_journey_work_hours_within_constitutional_limits).

% atom_id: 644549ae1e2d074d | chunk: 4f6b7682bcbb678c | strength: statutory
obligated(authority, none, issue_decision_after_rejection_of_conciliation_proposal) :-
    conciliation_proposal_status(rejected_by_parties).

% atom_id: 95a211d327df6fae | chunk: 4f8518a66e60de77 | strength: statutory
obligated(authority, director_or_board_member, remove_from_position).

% atom_id: 7663b09db81d2220 | chunk: 4f990d804de7558c | strength: statutory
prohibited(sindicato, empresa, refuse_collective_negotiation) :-
    provocation(true).

% atom_id: 2d1fecc4bb1c2902 | chunk: 4f990d804de7558c | strength: statutory
prohibited(empresa, sindicato, refuse_collective_negotiation) :-
    provocation(true).

% atom_id: 0d7a4bdec88e4d64 | chunk: 4fb19fb6ce61898a | strength: statutory
obligated(employer, worker, provide_incomplete_vacation_compensation) :-
    termination_reason(without_just_cause),
    service_duration_months(X_1), X_1 < 12.

% atom_id: 241fa23e113231a2 | chunk: 4fc8fb9adbd5da81 | strength: statutory
obligated(procuradoria_geral_do_trabalho, none, exercise_competence).

% atom_id: 5efb5c3146aded11 | chunk: 4ff3bfe48fe38b16 | strength: statutory
obligated(judge, litigants, distribute_liability_proportionally) :-
    number_of_litigants(X_0), X_0 >= 2,
    litigant_type(minor).

% atom_id: 167511c1fae2897e | chunk: 4ff3bfe48fe38b16 | strength: statutory
obligated(judge, litigants, impose_joint_liability) :-
    number_of_litigants(X_0), X_0 >= 2,
    collusion_intent(true).

% atom_id: a78e9b55e81dd4a8 | chunk: 5026ca1b3da41c20 | strength: statutory
obligated(authority, infractor, grant_defense_period) :-
    infraction_detected(true).

% atom_id: 44d00bb634421a5d | chunk: 5026ca1b3da41c20 | strength: statutory
obligated(authority, infractor, issue_decision_after_defense_period) :-
    defense_period_passed(true).

% atom_id: 489f035947f57c78 | chunk: 5047c3bdcdf4aac5 | strength: statutory
obligated(employer, employee, sign_conciliation_term).

% atom_id: 9778e027c72e5ce6 | chunk: 5047c3bdcdf4aac5 | strength: statutory
obligated(commission_member, employee, sign_conciliation_term).

% atom_id: e8a838ad42937e52 | chunk: 5047c3bdcdf4aac5 | strength: statutory
obligated(commission_member, employer, provide_copies_of_conciliation_term_to_parties).

% atom_id: e6141631f39e9efc | chunk: 504f9d753545e0f8 | strength: statutory
obligated(deployer, none, function_in_tst_sessions).

% atom_id: a3ffa3f3c8e56710 | chunk: 5057e4566cad4ae7 | strength: statutory
prohibited(judge, none, absent_without_permission) :-
    permission_status(denied).

% atom_id: 9d662092e3790ac4 | chunk: 5057e4566cad4ae7 | strength: statutory
permitted(judge, none, absent_with_permission) :-
    permission_status(granted).

% atom_id: 7845966b7c2826f2 | chunk: 5057e4566cad4ae7 | strength: statutory
obligated(judge, none, reside_within_jurisdiction).

% atom_id: e35ff74bb6e86024 | chunk: 50e7d8916c608c87 | strength: statutory
obligated(employer, worker, provide_weekly_rest_period) :-
    day_of_week(sunday).

% atom_id: 6f24ce48347c0ba4 | chunk: 50e7d8916c608c87 | strength: statutory
prohibited(employer, worker, schedule_work_on_sunday) :-
    public_convenience_reason(false),
    imperative_service_need(false).

% atom_id: 1c1823b653770086 | chunk: 5100748bcd2f577a | strength: regulatory
permitted(ministry_of_labor, none, reduce_work_hours) :-
    statistical_data_availability(not_available).

% atom_id: 2fd983ea415e5584 | chunk: 512733155da66137 | strength: statutory
permitted(minister, none, request_affection_of_legal_question_to_specialized_section_o) :-
    relevance_of_matter(relevant),
    existence_of_divergent_opinions(true).

% atom_id: 7e22bb9632978072 | chunk: 512733155da66137 | strength: statutory
obligated(specialized_section_or_plenary_court, none, decide_on_affection_of_legal_question_based_on_majority_vote) :-
    request_received(true).

% atom_id: 8ae7fb6ff94e0d6a | chunk: 51600d71962cfdaa | strength: statutory
obligated(authority, litigant, issue_instrument_denying_resource_filing).

% atom_id: 111f18e32b25f826 | chunk: 517cd1870bb13970 | strength: statutory
prohibited(employer, woman_employee, restrict_employment_rights_due_to_marriage_or_pregnancy).

% atom_id: da56ec0a966282a4 | chunk: 51a0be01cf4ec6d9 | strength: statutory
obligated(municipality, activity, comply_with_regulations).

% atom_id: ac61820e7b88103e | chunk: 51a0be01cf4ec6d9 | strength: statutory
prohibited(municipality, regulation, contradict_precepts).

% atom_id: 02b1e6758408b75e | chunk: 51a0be01cf4ec6d9 | strength: statutory
prohibited(municipality, regulation, contradict_instructions).

% atom_id: 293dab73d9b21a5a | chunk: 51dfc3b0ee60c1cf | strength: statutory
obligated(employer, worker, pay_proportional_salary_for_part_time_work).

% atom_id: c883efb693ccd1d4 | chunk: 523a22325e7ece4f | strength: statutory
permitted(federation, none, instaurate_representation) :-
    representative_sindicato(false).

% atom_id: 85d81a11e676bd7d | chunk: 523a22325e7ece4f | strength: statutory
permitted(confederation, none, instaurate_representation) :-
    representative_sindicato(false),
    representative_federation(false).

% atom_id: 6dda81fd9de25960 | chunk: 523c5fbe049baec8 | strength: statutory
permitted(authority, authorities, request_inquiries_examinations_diligences_certificates_clari).

% atom_id: ddcb2b56cf29f69e | chunk: 52472e60de82bece | strength: statutory
prohibited(non_state_actors, none, be_recongnized_as_sindicato) :-
    association_type(professional),
    registration_status(registered_according_to_art_558).

% atom_id: a648e270afe929ef | chunk: 52472e60de82bece | strength: statutory
permitted(authority, professional_association, recognize_as_sindicato) :-
    association_type(professional),
    registration_status(registered_according_to_art_558).

% atom_id: 5be804e434bc2102 | chunk: 52472e60de82bece | strength: statutory
obligated(professional_association, none, register_according_to_art_558) :-
    association_type(professional).

% atom_id: c421e763fd33609e | chunk: 525335706b8f66a0 | strength: statutory
obligated(authority, none, judge_aggravated_petitions_and_instruments) :-
    decision_type(denegatory),
    resource_category(aggravated_petition_or_instrument).

% atom_id: 3868c6a801e3b50e | chunk: 528bd2a75ab72c0f | strength: statutory
prohibited(collective, none, violate_regulations).

% atom_id: 7f5a987023ca631b | chunk: 528bd2a75ab72c0f | strength: statutory
prohibited(collective, none, violate_regulations) :-
    reincidencia(true).

% atom_id: 24e0079da5232947 | chunk: 528bd2a75ab72c0f | strength: statutory
prohibited(collective, none, violate_regulations) :-
    oposio_fiscalizao(true).

% atom_id: 9e9702bede74f894 | chunk: 528bd2a75ab72c0f | strength: statutory
prohibited(collective, none, violate_regulations) :-
    desacato_autoridade(true).

% atom_id: fcbe74c3801c9f42 | chunk: 52aa9f7983910b4a | strength: statutory
obligated(state, litigant, pay_legal_fees) :-
    case_type(against_public_authority).

% atom_id: 8d88cb84c37529b1 | chunk: 52aa9f7983910b4a | strength: statutory
obligated(state, litigant, pay_legal_fees) :-
    representation_type(union_representation).

% atom_id: c45425ab345a1ec3 | chunk: 52afe26ceddeff1a | strength: statutory
obligated(employer, musician, set_work_duration).

% atom_id: bec8cc9055e2d4ab | chunk: 530b4a55b1a6ec3a | strength: statutory
obligated(employer, worker, calculate_salary_in_cash) :-
    benefit_type(in_natura),
    salary_component(minimum_wage).

% atom_id: d2b66fb36e9028b8 | chunk: 531de509cfb9dcf4 | strength: statutory
obligated(authority, public, decide_on_constitutional_matter) :-
    matter_type(constitutional).

% atom_id: b1fc6d86bb5e4481 | chunk: 5322f6f7b5283170 | strength: statutory
obligated(employer, employee, respect_individual_agreements_precedence) :-
    employee_education_level(higher_degree),
    monthly_salary(X_1), X_1 >= 2.

% atom_id: 6dfa1e3109473bae | chunk: 5334699a29c7c2ef | strength: statutory
obligated(department_national_railways, railway_company, classify_major_intermediate_stations).

% atom_id: 917e72be8d556c55 | chunk: 53880d098195b25e | strength: regulatory
obligated(deployer, ai_system, submit_installation_project_for_approval).

% atom_id: 55673670c921a02f | chunk: 545be2c83d4200b3 | strength: statutory
obligated(collective, none, celebrate_conventions_in_writing).

% atom_id: 18ab26d52176fe39 | chunk: 545fc502c8183423 | strength: statutory
prohibited(minor, none, work).

% atom_id: bfe5309833ab7586 | chunk: 5509f50749537615 | strength: statutory
permitted(sus_manager, none, provide_opinion_in_sessions).

% atom_id: 9f5250928c1d0aa7 | chunk: 5509f50749537615 | strength: statutory
permitted(sus_manager, none, request_requisitions_and_diligences).

% atom_id: afea15a872e4e18a | chunk: 5509f50749537615 | strength: statutory
permitted(sus_manager, none, view_process_when_new_question_arises) :-
    new_question_suspected(true).

% atom_id: 9c3bba62c8b71305 | chunk: 557b4ac849decf40 | strength: statutory
obligated(legal_entity, part_victorious_in_lawsuit, reimburse_legal_expenses) :-
    entity_type(legal_entity),
    professional_practice_regulation_authority(false).

% atom_id: 28d45a874cbe3bc5 | chunk: 5595af554c91c598 | strength: regulatory
permitted(authority, none, impose_penalties) :-
    location(distrito_federal).

% atom_id: 852221a16c8c6158 | chunk: 5595af554c91c598 | strength: regulatory
permitted(authority, none, impose_penalties) :-
    location(estados).

% atom_id: de4a1d134054e5ac | chunk: 5595af554c91c598 | strength: regulatory
permitted(authority, none, impose_penalties) :-
    location(territorio_do_acre).

% atom_id: 7eb7a328a5ea92b3 | chunk: 55a5d7b4c92f4769 | strength: statutory
obligated(escrivao_secretario, none, attend_audience_in_advance).

% atom_id: 3a049fc84022f7b4 | chunk: 561c87a2610a8130 | strength: statutory
obligated(sindicato, professional, issue_professional_qualification_declaration).

% atom_id: 2ea3edb27d3dbb89 | chunk: 5625339ed971fab2 | strength: statutory
obligated(sus_manager, none, declare_self_unqualified) :-
    reason(litigant_person).

% atom_id: afe6dfc7ad104ecb | chunk: 5625339ed971fab2 | strength: statutory
permitted(litigant, sus_manager, challenge_unqualification) :-
    reason(litigant_person).

% atom_id: 058752bb4d43b571 | chunk: 5669596e9d09b638 | strength: statutory
prohibited(employee, employer, repeat_serious_violations_of_duties_and_obligations).

% atom_id: 2f47f674ae83672b | chunk: 56b045d602e49605 | strength: statutory
permitted(judge, none, execute_oficio) :-
    representation_by_lawyer(false).

% atom_id: 7e41259dfbfc1935 | chunk: 56b045d602e49605 | strength: statutory
permitted(tribunal_president, none, execute_oficio) :-
    representation_by_lawyer(false).

% atom_id: 0e456163c68f5d91 | chunk: 56b045d602e49605 | strength: statutory
obligated(parties, none, promote_execution).

% atom_id: bf723c87670485b7 | chunk: 56b782bdbabff7c3 | strength: statutory
obligated(authority, chemical_factory_lab_or_plant, appoint_qualified_chemists_ex_officio) :-
    qualification_status(habilitados).

% atom_id: dec0ebbfa1cacf9a | chunk: 56d6f67670e47cdc | strength: statutory
obligated(worker, none, use_provided_equipment).

% atom_id: 221508b572ae4d38 | chunk: 5795592f3ccae3a0 | strength: statutory
obligated(employer, worker, provide_weekly_rest_period).

% atom_id: 4463e02e5a8df132 | chunk: 5795592f3ccae3a0 | strength: statutory
permitted(authority, employer, authorize_weekly_rest_period_change) :-
    reason(public_convenience_or_emergency_service_need).

% atom_id: b0274050e67ba167 | chunk: 57df1d332e01ff88 | strength: statutory
obligated(employer, worker, notify_vacation_grant_in_writing) :-
    notification_period_days(X_0), X_0 >= 30.

% atom_id: 0f54f92fe7127997 | chunk: 57df1d332e01ff88 | strength: statutory
obligated(worker, employer, acknowledge_vacation_notification).

% atom_id: 931ae78247b405b9 | chunk: 584657b32042aa10 | strength: statutory
obligated(employer, driver, provide_minimum_rest_period) :-
    employment_status(professional_driver).

% atom_id: 6c2d3aa1bbc17475 | chunk: 584657b32042aa10 | strength: statutory
permitted(driver, self, split_rest_period) :-
    rest_period_duration(n1_hour).

% atom_id: 1ae7b88e68a5e1ab | chunk: 584657b32042aa10 | strength: statutory
obligated(driver, self, take_mandatory_break_during_driving) :-
    employment_status(professional_driver).

% atom_id: e5eb7ff035b0c658 | chunk: 584657b32042aa10 | strength: statutory
permitted(driver, self, combine_rest_period_with_mandatory_break) :-
    employment_status(professional_driver),
    rest_period_duration(n1_hour).

% atom_id: 9e9944e5f921ae45 | chunk: 5873a5035676f9be | strength: statutory
prohibited(employer, none, impose_excessive_fine_on_employee) :-
    fine_amount(half_of_company_fine).

% atom_id: 8ee858aa8dd18af2 | chunk: 5879049dcef1247a | strength: statutory
obligated(tribunal_regional, none, deliberate_with_quorum) :-
    presence_of_president(true),
    number_of_judges_present(half_plus_one),
    representatives_from_employees(X_2), X_2 >= 1,
    representatives_from_employers(X_3), X_3 >= 1.

% atom_id: 27c3089bfe823999 | chunk: 58a3d71951571643 | strength: statutory
obligated(judge, tribunal, participate_in_tribunal_meetings).

% atom_id: 736292e30462d63a | chunk: 5934e575fea1a93e | strength: statutory
prohibited(employer, job_seeker, advertise_job_based_on_sex_age_color_or_marital_status) :-
    nature_of_activity(public_and_notoriously_exigent).

% atom_id: fe172adab0fe46a8 | chunk: 598fbcf79990fa9a | strength: statutory
obligated(court_of_first_instance, university, function_in_lawsuits_against_union) :-
    location(distrito_federal),
    subject_matter(previdencia_social).

% atom_id: 37da802ebeb2aaef | chunk: 59ac427c62ccd201 | strength: statutory
obligated(authority, none, exercise_jurisdiction) :-
    location(distrito_federal).

% atom_id: 14766e187d738354 | chunk: 59adc944293f2685 | strength: statutory
obligated(authority, public_funds, deposit_public_funds_in_bank) :-
    exeqente_presence(absent).

% atom_id: 07dd722fffe4a0d6 | chunk: 5a0e585bdda331ab | strength: regulatory
obligated(tripulant, none, assume_personal_responsibility) :-
    position_type(leadership).

% atom_id: 1d424541c09354b6 | chunk: 5a40c9d6e3589a3b | strength: statutory
obligated(collective, worker, celebrate_collective_labor_contracts).

% atom_id: 5cda385270b72247 | chunk: 5a427425418073aa | strength: statutory
permitted(employer, worker, schedule_shift_work) :-
    work_hours(12),
    rest_period(36).

% atom_id: 2562109bae959cff | chunk: 5a52e550e3991218 | strength: statutory
obligated(employer, worker, grant_vacation_leave) :-
    time_since_acquisition_of_right(X_0), X_0 <=12_months 12.

% atom_id: c95f6ccd9a30d523 | chunk: 5aeb62481511ccad | strength: statutory
prohibited(employer, autonomous_worker, treat_as_employee) :-
    contract_type(autonomous),
    legal_requirements(fulfilled).

% atom_id: 7b38ff9c8fa3f435 | chunk: 5af8df80d15193e7 | strength: statutory
obligated(association, member, maintain_legal_aid_services).

% atom_id: a93d079a5ebd125a | chunk: 5b18033066114d86 | strength: statutory
obligated(provider, public, indicate_maximum_load).

% atom_id: f7e62bc1a566d237 | chunk: 5b18033066114d86 | strength: statutory
obligated(provider, public, indicate_no_smoking_warning).

% atom_id: ba9b578fe854da13 | chunk: 5b18033066114d86 | strength: statutory
obligated(provider, public, indicate_health_hazard_warning).

% atom_id: a36f436dde502642 | chunk: 5b18033066114d86 | strength: statutory
obligated(provider, public, indicate_first_aid_recommendations).

% atom_id: 5ccfb5cad2ff8c63 | chunk: 5b18033066114d86 | strength: statutory
obligated(provider, public, indicate_medical_attention_recommendations).

% atom_id: 4f765a65a6cc8617 | chunk: 5b18033066114d86 | strength: statutory
obligated(provider, public, indicate_hazard_symbol).

% atom_id: 792038c9b1f2ef23 | chunk: 5b3d48bc2c18e3b6 | strength: statutory
obligated(employer, worker, provide_information_on_vaccination_campaigns).

% atom_id: b5a15ca5e3f2c7d5 | chunk: 5b3d48bc2c18e3b6 | strength: statutory
obligated(employer, worker, provide_information_on_hpv).

% atom_id: d32aea3ace3dc52c | chunk: 5b3d48bc2c18e3b6 | strength: statutory
obligated(employer, worker, provide_information_on_cancer_prevention).

% atom_id: ca8960c341fcf6ce | chunk: 5b3d48bc2c18e3b6 | strength: statutory
obligated(employer, worker, promote_consciousness_raising_actions).

% atom_id: fe61cb8e809531cf | chunk: 5b3d48bc2c18e3b6 | strength: statutory
obligated(employer, worker, orient_workers_on_diagnostic_services_access).

% atom_id: fc7cbebd6f63444b | chunk: 5b7a176bc7559a90 | strength: statutory
obligated(authority, reclamations, register_in_special_book).

% atom_id: a13da644bfdf2747 | chunk: 5b7a176bc7559a90 | strength: statutory
obligated(authority, book_pages, stamp_by_authority).

% atom_id: 978a7eaa289ff1d3 | chunk: 5ba9b018c13360a6 | strength: statutory
obligated(employer, worker, grant_maternity_leave) :-
    reason_for_license(maternity_or_abortion),
    benefit_status(perceiving_maternity_benefit).

% atom_id: 337492e230394e6a | chunk: 5c67a8b5ad60ac28 | strength: regulatory
obligated(authority, none, fiscalize_own_decisions).

% atom_id: 86c5124205b3fb06 | chunk: 5c6fb4abed1c0bf7 | strength: statutory
obligated(authority, candidate, consider_majority_winner_in_elections) :-
    voting_position(directoria_conselho_fiscal).

% atom_id: 76aab043a1eb0342 | chunk: 5c935900d86f7de1 | strength: regulatory
obligated(operator, worker, resolve_labor_disputes).

% atom_id: 12e408bc68eafeb3 | chunk: 5d0adef774b162d3 | strength: statutory
obligated(authority, public, organize_and_maintain_jurisprudence_file).

% atom_id: 1862772eb7c345eb | chunk: 5d3f2c0a4ecd0dda | strength: statutory
obligated(president_of_the_republic, procuradorias_regionais, designate_substitute_procurator_adjunct_or_regional_procurat).

% atom_id: fa8314e152ed9967 | chunk: 5d5625f412eaeea5 | strength: regulatory
obligated(judge_or_judicial_authority, parties, despachar_recursos_fundamentando_decisao).

% atom_id: a26b53f29f06619f | chunk: 5d68500ae0aac4b7 | strength: statutory
obligated(authority, public, exercise_judicial_attributes_in_interest_of_labor_justice).

% atom_id: 22e2b6b08abb1c17 | chunk: 5d738a07bf2d4818 | strength: statutory
obligated(council_member, conselho, attend_regular_sessions) :-
    number_of_missed_sessions(X_0), X_0 >= 3,
    justification_for_absence(null).

% atom_id: 3d9f725bea8e47eb | chunk: 5dabb5bf670f0e3a | strength: statutory
obligated(authority, worker, characterize_and_classify_hazardous_conditions).

% atom_id: b614cb921e283909 | chunk: 5dd470c8cb2d6b39 | strength: statutory
obligated(authority, judgment, order_liquidation_of_indeterminate_judgment).

% atom_id: c33f411b350c189d | chunk: 5e309e479b6db145 | strength: statutory
obligated(court, litigant, judge_incompetency_exceptions).

% atom_id: b2d80d71fed33b90 | chunk: 5e32d51accf410db | strength: statutory
obligated(state, federation, credit_percentages_to_federation) :-
    sindicato_existence(false).

% atom_id: 5027d73bd6006d05 | chunk: 5e42a73aa2a18b97 | strength: regulatory
permitted(authority, none, impose_fines_and_penalties).

% atom_id: 108bcd803c438abd | chunk: 5e42a73aa2a18b97 | strength: regulatory
permitted(authority, none, judge_appeals_from_judges_decisions).

% atom_id: 99c4809e0b4f52ee | chunk: 5e82f5e5c6d6475f | strength: statutory
obligated(authority, worker, homologate_agreements_in_disputes).

% atom_id: 140c032eeb6286aa | chunk: 5e920e9da6d68a9d | strength: statutory
obligated(employer, public, cover_expenses_from_transfer).

% atom_id: 359e1ac42c780ced | chunk: 5e93320201e07896 | strength: statutory
obligated(judge, litigant_in_bad_faith, pay_penalty).

% atom_id: 48fcce38f7e0189a | chunk: 5e93320201e07896 | strength: statutory
obligated(litigant_in_bad_faith, opposing_party, compensate_for_damages).

% atom_id: ba0cfd475916300c | chunk: 5e93320201e07896 | strength: statutory
obligated(litigant_in_bad_faith, court, cover_legal_fees_and_expenses).

% atom_id: 766d5b638dc04fca | chunk: 5f1cb140abaf4f90 | strength: statutory
permitted(employer, worker, reduce_minimum_working_hours) :-
    lighting_conditions(adequate),
    thermal_comfort(compatible_with_work_nature).

% atom_id: 4cb49fe77560f5f3 | chunk: 5f1cb140abaf4f90 | strength: statutory
obligated(sus_manager, employer, control_reduction_of_minimum_working_hours).

% atom_id: 95cc71da7a2014f5 | chunk: 5f6410597fa8c713 | strength: statutory
permitted(worker, none, affiliate_with_similar_union) :-
    local_sindicato_existence(false).

% atom_id: 335e3a3ec567d494 | chunk: 5fc07964771eceb9 | strength: statutory
obligated(authority, competent_authorities, request_necessary_force) :-
    type_of_dispute(collective_dissident),
    threat_to_order(true).

% atom_id: 629b123f8d17a14b | chunk: 5fc3d401651ae6f9 | strength: regulatory
obligated(tribunal_regional, secretaria_tribunal, establish_attributes_and_operations).

% atom_id: 576ed5c603d551d8 | chunk: 5fe0a24adb472148 | strength: statutory
permitted(president_of_the_tribunal, none, file_appeal_in_collective_dispute_affecting_public_service_c).

% atom_id: 66d0a0e9dac4f023 | chunk: 5fe0a24adb472148 | strength: statutory
permitted(procurator_of_labor_justice, none, file_appeal_in_collective_dispute_affecting_public_service_c).

% atom_id: 2c893837131095a5 | chunk: 5fe828cef23d0475 | strength: statutory
prohibited(employer, apprentice, terminate_contract_inadequate_performance) :-
    type_of_apprentice(non_disabled).

% atom_id: 56577028e5519438 | chunk: 5fe828cef23d0475 | strength: statutory
obligated(employer, disabled_apprentice, provide_accessibility_resources) :-
    type_of_apprentice(disabled),
    accessibility_requirements_met(false).

% atom_id: b1c0d346bdec7a54 | chunk: 5fe828cef23d0475 | strength: statutory
obligated(employer, disabled_apprentice, provide_assistive_technologies) :-
    type_of_apprentise(disabled),
    assistive_technologies_provided(false).

% atom_id: b65581711eebbb10 | chunk: 5fe828cef23d0475 | strength: statutory
obligated(employer, disabled_apprentice, provide_support_services) :-
    type_of_apprentise(disabled),
    support_services_provided(false).

% atom_id: e63b6eeb2ba5cb2f | chunk: 603cdff452f8f8c9 | strength: statutory
obligated(sindicato, worker, establish_collective_bargaining_agreement) :-
    representatives(two_or_more_sindicatos).

% atom_id: 914a9205bdd9d1f4 | chunk: 6077a57f8f164432 | strength: statutory
permitted(collective, none, include_clauses_in_conventions_and_agreements).

% atom_id: a6c52c36ff94448f | chunk: 6077a57f8f164432 | strength: statutory
obligated(collective, none, constitute_and_function_mixed_commissions).

% atom_id: 9d234e42a30f7ec2 | chunk: 6077a57f8f164432 | strength: statutory
obligated(collective, none, define_constitution_and_function_of_commissions).

% atom_id: 7e0a066d72936465 | chunk: 6077a57f8f164432 | strength: statutory
obligated(collective, none, define_plan_of_participation_in_profits).

% atom_id: 0e40e0e988245d80 | chunk: 613f2189e9ecc5f9 | strength: statutory
permitted(woman, none, revert_to_previous_position) :-
    period(art_392_period).

% atom_id: 3977bd7af271b472 | chunk: 613f2189e9ecc5f9 | strength: statutory
obligated(employer, woman, provide_full_salary_during_period) :-
    period(art_392_period).

% atom_id: eac0616f33daf4e0 | chunk: 613f2189e9ecc5f9 | strength: statutory
obligated(employer, woman, calculate_variable_salary_based_on_average) :-
    period(art_392_period),
    salary_type(variable).

% atom_id: 8d85b3517c19a428 | chunk: 613f2189e9ecc5f9 | strength: statutory
obligated(employer, woman, grant_acquired_rights_and_benefits) :-
    period(art_392_period).

% atom_id: c8398ba8f1e62ae4 | chunk: 616fb1837d50bcd6 | strength: statutory
permitted(chemist, none, exercise_profession) :-
    technical_capacity(required).

% atom_id: 6698783c9805f9ad | chunk: 62202f79a66ffc7d | strength: regulatory
prohibited(non_state_actors, public, create_obstacles_to_economic_policy_execution).

% atom_id: 6d920a52cabe0b31 | chunk: 62376803a08fb27e | strength: statutory
obligated(tribunal, authorities_ministry_of_labor, provide_information_on_disputes).

% atom_id: 7ce100f4b09fc989 | chunk: 62376803a08fb27e | strength: statutory
obligated(tribunal, competent_authorities, forward_authenticated_copies_of_decisions).

% atom_id: 6f440348e7818715 | chunk: 6237c2f026543752 | strength: regulatory
obligated(employer, worker, provide_safe_work_environment) :-
    workplace_classification(dangerous_or_unhealthy).

% atom_id: 9317b00444ac942b | chunk: 625a9f7668c835fd | strength: statutory
obligated(tribunal, ministry_of_labor, submit_annual_report_activities) :-
    date(n31_mar).

% atom_id: bcfb4b4e3ead7e7d | chunk: 627c9ae27f0ca168 | strength: statutory
permitted(delegado_regional_do_trabalho, establishment, interdict_establishment) :-
    technical_report(grave_and_imminent_risk_to_worker).

% atom_id: bf7d8cd6c8bc86b3 | chunk: 627c9ae27f0ca168 | strength: statutory
permitted(delegado_regional_do_trabalho, construction_project, embargo_construction_work) :-
    technical_report(grave_and_imminent_risk_to_worker).

% atom_id: 7093b803d1b45560 | chunk: 627c9ae27f0ca168 | strength: statutory
obligated(delegado_regional_do_trabalho, establishment, indicate_preventive_measures) :-
    technical_report(grave_and_imminent_risk_to_worker).

% atom_id: 97b1df665bc4351c | chunk: 627c9ae27f0ca168 | strength: statutory
obligated(establishment_owner, worker, adopt_preventive_measures) :-
    delegado_decision(indicated_preventive_measures).

% atom_id: 474ef32e0b2fffe6 | chunk: 6286c0fd06f6f52d | strength: statutory
obligated(authority, none, compose_procuradorias_regionais).

% atom_id: f6122581786f6a94 | chunk: 62ae1e5c27e346f8 | strength: statutory
obligated(judge, none, determine_award_amount) :-
    liquidated_judgment(false).

% atom_id: e5e4547deb9be1e5 | chunk: 62ae1e5c27e346f8 | strength: statutory
obligated(judge, none, set_procedural_costs) :-
    liquidated_judgment(false).

% atom_id: 3e0fbec6a82def67 | chunk: 633eda54b3db34f3 | strength: statutory
obligated(professional_driver_employee, none, fulfill_professional_duties).

% atom_id: dfbc83f2d844ea3a | chunk: 639462b55c15a16d | strength: statutory
obligated(sus_manager, competent_authorities, request_necessary_inquiries).

% atom_id: c00016f8f90398d4 | chunk: 639cf7bb5a9970c3 | strength: statutory
prohibited(employer, worker, alter_employment_rights).

% atom_id: 966ccebb6a288f77 | chunk: 63b068c375a2b6bb | strength: statutory
obligated(authority, non_compliant_party, intimate_non_attendance) :-
    attendance_status(non_attendance).

% atom_id: 2ffa3e961923dbae | chunk: 63b068c375a2b6bb | strength: statutory
prohibited(non_compliant_party, none, ignore_intimation) :-
    justification_for_non_attendance(none).

% atom_id: 87992d0dd775f82a | chunk: 63ebaf8d312dcda5 | strength: statutory
prohibited(judge, case, consider_outside_instructions) :-
    status_of_case(pending_judicial_review).

% atom_id: 1229b86d4bb6c96d | chunk: 64165b1c9c5d2b46 | strength: statutory
prohibited(worker, employer, cease_work_with_salary_payment) :-
    duration_of_ceased_work(X_0), X_0 > 30.

% atom_id: 1e5a958467129212 | chunk: 6431b3ab869672a1 | strength: statutory
permitted(crew_member, none, file_complaint) :-
    perceived_harm(true).

% atom_id: 8b9061933e357060 | chunk: 6431b3ab869672a1 | strength: statutory
obligated(commander, crew_member, forward_complaint_to_labor_office) :-
    complaint_received(true).

% atom_id: e1447afd279f111b | chunk: 6431b3ab869672a1 | strength: statutory
obligated(commander, none, submit_complaint_within_five_days) :-
    complaint_received(true).

% atom_id: 682c33a859673baa | chunk: 64e037fde0112ee2 | strength: statutory
prohibited(employer, worker, prevent_readmission_within_sixty_days) :-
    days_since_departure(X_0), X_0 <= 60.

% atom_id: c0ca686f35c34501 | chunk: 64e0dc1e50818f14 | strength: statutory
obligated(worker, none, avoid_manifest_danger).

% atom_id: c85a389948e1ee8b | chunk: 654fc5c789c502ba | strength: statutory
obligated(employer, worker, follow_procedure_for_new_hires) :-
    hire_date(aquela_data),
    previous_work_experience(nem_trabalharam_anteriormente),
    quit_certificate(nem_apresentaram_quitacao_respectiva).

% atom_id: 8de1db84e44491d2 | chunk: 655df886ac51b0b7 | strength: statutory
prohibited(employer, worker, require_contraceptive_test).

% atom_id: 90d70f89f6b43c18 | chunk: 656e5883ea173e15 | strength: statutory
prohibited(employer, worker, pay_with_alcoholic_beverages_or_harmful_substances).

% atom_id: ae46f09b919c8234 | chunk: 658230ff547db6ef | strength: statutory
obligated(enterprise, none, undertake_specified_duties).

% atom_id: 508e8f35574e7caa | chunk: 65d370d1641b92b8 | strength: statutory
obligated(president_of_the_republic, tribunal_judges, appoint_tribunal_judges) :-
    regional_court_region(n1st_or_2nd_region),
    judge_type(toga_life_term_or_classist_temporary).

% atom_id: 55703cb4b17fb665 | chunk: 65d370d1641b92b8 | strength: statutory
obligated(president_of_the_republic, tribunal_judges, appoint_tribunal_judges) :-
    regional_court_region(n3rd_or_4th_region),
    judge_type(toga_life_term_or_classist_temporary).

% atom_id: f30411ce9bf5ad1e | chunk: 65d370d1641b92b8 | strength: statutory
obligated(president_of_the_republic, tribunal_judges, appoint_tribunal_judges) :-
    regional_court_region(n5th_or_6th_region),
    judge_type(toga_life_term_or_classist_temporary).

% atom_id: 9558b717c26f590c | chunk: 65d370d1641b92b8 | strength: statutory
obligated(president_of_the_republic, tribunal_judges, appoint_tribunal_judges) :-
    regional_court_region(n7th_or_8th_region),
    judge_type(toga_life_term_or_classist_temporary).

% atom_id: e3e61584ce5252b1 | chunk: 663519ca70052a24 | strength: statutory
obligated(conselho_pleno, none, process_suscitados_between_camaras).

% atom_id: 6a0e8e418df72f3b | chunk: 66a2aff1f1d8af7b | strength: statutory
obligated(employer, worker, provide_rest_period).

% atom_id: abdcd4cda990c513 | chunk: 67323bc6ba7b77b3 | strength: statutory
obligated(president_of_the_republic, judges_class_representatives, designate_judicial_positions).

% atom_id: 47262a0eeae14367 | chunk: 6753c80865f86d96 | strength: statutory
obligated(employer, workplace, promote_dialogue_and_understanding).

% atom_id: 3e611ad27f509e39 | chunk: 67b05ebfd0060215 | strength: statutory
obligated(employer, worker, establish_maximum_work_hours) :-
    work_schedule_type(variable).

% atom_id: 0ae762a3acab632e | chunk: 67b05ebfd0060215 | strength: statutory
obligated(employer, worker, provide_rest_period) :-
    work_schedule_type(variable),
    continuous_effort_duration_minutes(X_1), X_1 > 180.

% atom_id: ef8f7fee0d4b8649 | chunk: 6802aecb754cfe60 | strength: statutory
obligated(government_federal, professional_journalist, promote_creation_of_journalism_schools) :-
    collaboration_partner(governos_estaduais).

% atom_id: 409f10f8ff60eecd | chunk: 6807c8565ceb4aa4 | strength: statutory
obligated(employer, worker, provide_cold_room_rest_period) :-
    work_environment(cold_storage),
    elapsed_time(X_1), X_1 >= 100.

% atom_id: 9e8251cb1a6398e2 | chunk: 6807c8565ceb4aa4 | strength: statutory
obligated(employer, worker, provide_rest_period_during_temperature_change) :-
    work_environment(temperature_change),
    elapsed_time(X_1), X_1 >= 100.

% atom_id: b77987275f493b35 | chunk: 68639261d83e2816 | strength: statutory
obligated(authority, none, judge_embargoes_against_own_decisions).

% atom_id: 863ea4fa1b00012d | chunk: 68e19b962541cdc1 | strength: statutory
obligated(authority, none, exercise_national_authority_in_safety_and_health_at_work).

% atom_id: f58b15ea99f59ba2 | chunk: 6922a8acb55491ea | strength: statutory
obligated(employer, public, disclose_company_information) :-
    type_of_union(sindicate_of_employers).

% atom_id: 2e480c3c0b4aec21 | chunk: 6922a8acb55491ea | strength: statutory
obligated(employer, public, disclose_personal_information_of_representatives) :-
    type_of_union(sindicate_of_employers).

% atom_id: 7c0a3ce2f12f32b0 | chunk: 6922a8acb55491ea | strength: statutory
obligated(employer, public, disclose_personal_information_of_directors_in_case_of_stock) :-
    type_of_union(sindicate_of_employers),
    company_type(stock_company).

% atom_id: 479a008e0593bd43 | chunk: 693c1a898e859081 | strength: statutory
obligated(state, worker, allow_public_service_entry) :-
    collective_work_stoppage_reason(establishment_closure).

% atom_id: a0993c915c5b9806 | chunk: 69919f8d0df36f17 | strength: regulatory
prohibited(worker, none, exercise_profession_within_sindicato_territory) :-
    time_since_exercise_of_activity(X_0), X_0 >= 2.

% atom_id: 7ef53534f1a5f68d | chunk: 69a9c7f660d6f925 | strength: statutory
obligated(authority, testifier, qualify_testifier_before_legal_pledge) :-
    legal_pledge_status(pending).

% atom_id: dac23c9345aec61e | chunk: 69b1e09be76a3e9c | strength: regulatory
obligated(authority, court_case, execute_decision_in_original_court_records).

% atom_id: c930b7b11c6cac9f | chunk: 69b1e09be76a3e9c | strength: regulatory
obligated(authority, court_case, document_execution_with_acordao_and_certidao).

% atom_id: 15d01cbb1308ecf3 | chunk: 69d541bab5dce864 | strength: statutory
permitted(worker, none, work_overtime) :-
    overtime_hours(X_0), X_0 <= 2.

% atom_id: abb278aed8889513 | chunk: 6a2d2e2c06cf73cd | strength: statutory
prohibited(vogal_junta_conciliacao_julgamento, none, miss_three_consecutive_meetings_without_justification).

% atom_id: f52571164bc1664c | chunk: 6a30d7677d7903da | strength: regulatory
obligated(sus_manager, public, superintend_secretariat_works).

% atom_id: 75d60be218e9e8e5 | chunk: 6a5cfd037c74cb33 | strength: statutory
obligated(tribunal, none, fix_execution_date_and_vigency_period).

% atom_id: 66a57adbd6bd6934 | chunk: 6a76110589006dad | strength: statutory
prohibited(employer, worker, classify_as_employee) :-
    contract_type(autonomous_worker),
    legal_requirements_met(true).

% atom_id: b4bd7fa6cc3df0b8 | chunk: 6a7e24527f7ace3b | strength: statutory
permitted(employee_or_union, none, file_claim_with_junta_or_court) :-
    employer_payment_status(unpaid_salaries),
    decision_conformity(non_compliance).

% atom_id: 1ac882b462bebf54 | chunk: 6a7e24527f7ace3b | strength: statutory
prohibited(employee_or_union, none, question_matter_already_judged) :-
    judgment_status(final).

% atom_id: 370a08fd6ac2bc5d | chunk: 6acac974b439ead5 | strength: statutory
obligated(employer, worker, record_work_hours).

% atom_id: 8b7908c0f7e4101e | chunk: 6b5e7c0c09464bbd | strength: statutory
obligated(authority, worker, promote_conciliation_in_work_disputes).

% atom_id: 726939300e4c4c42 | chunk: 6b6ee28bc1555e8d | strength: statutory
obligated(employer, worker, provide_additional_compensation_for_exceeding_production_tar) :-
    remuneration_reason(exceeding_production_target),
    employment_type(commission_task).

% atom_id: 3debb84d9ddc5a53 | chunk: 6b7011c1d369b33c | strength: statutory
permitted(exerciser_of_activities_or_professions, none, sindicalize_by_similar_categories) :-
    number_of_exercisers(reduced_number),
    nature_of_activities_or_professions(specific_nature),
    affinities_between_activities_or_professions(existing_affinities).

% atom_id: 32b05aef36a1665c | chunk: 6b87f6eaec245d70 | strength: statutory
prohibited(employer, none, non_compliance_with_contract_obligations).

% atom_id: a31e658626e690f5 | chunk: 6bbd6dcdc6dc3305 | strength: statutory
obligated(employer, worker, display_hazard_warnings).

% atom_id: b9a0e72805d18675 | chunk: 6c1d0400ebabab46 | strength: statutory
obligated(authority, tribunal_regional, carry_out_procedural_actions_and_inquiries) :-
    decision_origin(tribunal).

% atom_id: b40cbcc98d7cf385 | chunk: 6c1d0400ebabab46 | strength: statutory
obligated(authority, other_justice_organs, carry_out_procedural_actions_and_inquiries) :-
    decision_origin(tribunal).

% atom_id: 85a60b1b99056c7e | chunk: 6ca632ca3d38e9dd | strength: regulatory
obligated(secretary_of_junta_or_designated_staff, testimony, summarize_testimonies_during_hearing).

% atom_id: 20159daa9bf61b04 | chunk: 6ca632ca3d38e9dd | strength: regulatory
obligated(tribunal_president_and_deponents, summary_of_testimonies, sign_summary).

% atom_id: c6dc92fc858e5121 | chunk: 6cbde45dacc18242 | strength: statutory
obligated(employer, worker, grant_marriage_leave) :-
    marriage_occurrence(true).

% atom_id: 086cd07364cc4e7b | chunk: 6d2d9fed7a6e62c8 | strength: statutory
obligated(employer, worker, participate_in_sure_job_program).

% atom_id: bec62dd9f5e601bf | chunk: 6d5c587ca9e9da9f | strength: statutory
obligated(authority, court_decision, review_divergent_decisions) :-
    decision_type(divergent_tourm_decisions),
    decision_type(individual_dispute_section_decision),
    decision_status(contrary_to_summary_or_guideline_of_superior_labor_court_or).

% atom_id: 3330be6a454a45b0 | chunk: 6d9db2571ed5cae7 | strength: statutory
prohibited(employer, worker, make_salary_deduction) :-
    exception_reason(advances_legal_dispositions_or_collective_agreements).

% atom_id: 7c5da9bc48dff29e | chunk: 6df25e4eb9b921b6 | strength: statutory
permitted(ministry_of_labor, none, set_effectiveness_date_for_chapter_provisions) :-
    judgment_convenience(convenient).

% atom_id: c2af44a4183c3bdb | chunk: 6df4c7473da8a160 | strength: statutory
obligated(vice_president_of_the_court, none, substitute_president_in_absence_or_disability) :-
    president_availability(absent_or_disabled).

% atom_id: cb6ff1158fb0932c | chunk: 6e357d6efeb6f39b | strength: statutory
obligated(authority, public, provide_certificates_from_records).

% atom_id: 139fbefe7460d230 | chunk: 6e59855fa99244dd | strength: statutory
obligated(authority, workplace, adopt_measures_and_determine_repairs).

% atom_id: 57f68d69309b7229 | chunk: 6efed03b272e73e1 | strength: regulatory
obligated(deployer, none, perform_assigned_duties).

% atom_id: d617cc934497fbe7 | chunk: 6f71af4a02c70eaf | strength: statutory
obligated(procurador_adjunto, tribunal_regional, attend_sessions_personally_or_through_designated_procurator).

% atom_id: 0c6ba2d35f6ed49d | chunk: 6f967c6241b27a02 | strength: statutory
prohibited(employer, worker, employ_woman_in_excessive_force_work) :-
    force_required(X_0), X_0 >= 20,
    work_type(continuous).

% atom_id: 18109a5b7b5a8bd8 | chunk: 6f967c6241b27a02 | strength: statutory
prohibited(employer, worker, employ_woman_in_excessive_force_work) :-
    force_required(X_0), X_0 >= 25,
    work_type(occasional).

% atom_id: 82de6ebd74631426 | chunk: 6fde565dfa04e877 | strength: statutory
obligated(employer, worker, provide_foliday_compensation).

% atom_id: 4c4a47ff344eeed3 | chunk: 6fde77f762720e81 | strength: statutory
obligated(authority, worker, process_collective_disputes).

% atom_id: 6505d43be546bb4e | chunk: 6fde77f762720e81 | strength: statutory
obligated(authority, worker, mediate_collective_disputes).

% atom_id: 9127b0e5536f7fb5 | chunk: 6fde77f762720e81 | strength: statutory
obligated(authority, worker, judge_collective_disputes_originarily).

% atom_id: f65e286c6f17dbb5 | chunk: 6ff682635a9ec92b | strength: statutory
obligated(tribunal, public, hold_public_sessions).

% atom_id: 8079ee8a3c26d5df | chunk: 6ff682635a9ec92b | strength: statutory
permitted(president_of_tribunal, session_duration, extend_session_time) :-
    manifest_necessity(true).

% atom_id: 9921bf557944c3c4 | chunk: 7055dda9ff622be1 | strength: statutory
obligated(employer, worker, apply_article_301_to_new_relations) :-
    employment_start_date(consolidation_vigency).

% atom_id: a420681dd8ad3e63 | chunk: 7073f56f1d595524 | strength: statutory
prohibited(operator, none, work_ininterruptedly_above_threshold) :-
    speed(X_0), X_0 > 25.

% atom_id: b83a30d5dbb6c2c8 | chunk: 70a78f465ab7f3fd | strength: statutory
obligated(parties, court, authenticate_transfer_of_documents_by_reproduction_copy).

% atom_id: 1504938672cb1f74 | chunk: 70b123288dba32e4 | strength: regulatory
permitted(secretariat, staff, hire_extranumerary_staff).

% atom_id: f77ee6edc96072ea | chunk: 70b123288dba32e4 | strength: regulatory
permitted(secretariat, staff, dismiss_extranumerary_staff).

% atom_id: ae6a65a371680c2e | chunk: 70b123288dba32e4 | strength: regulatory
permitted(secretariat, staff, extend_working_hours_with_compensation).

% atom_id: 20651f250edcdbd1 | chunk: 7130d22a713b8bd3 | strength: statutory
obligated(association_member, association, elect_representative_for_category).

% atom_id: 028ca14a696e7b28 | chunk: 716b4b68876b1024 | strength: regulatory
obligated(sus_manager, conselho_superior_previdencia_social, attend_sessions_personally_or_through_designated_procurator).

% atom_id: 41e2c687367ea688 | chunk: 719f64768f0274ba | strength: statutory
obligated(authority, participant, impose_contributions) :-
    category_type(economic_or_professional_categories),
    professional_status(liberal_professions).

% atom_id: 20f4e7298034358b | chunk: 71b3459dec6adcf0 | strength: statutory
obligated(authority, professor, set_salary_based_on_class_hours).

% atom_id: 2e22ea7d44c5ad20 | chunk: 71c124350557ecf1 | strength: statutory
prohibited(non_state_actors, tribunal_regions, alter_regional_courts).

% atom_id: 42e304fb067a9be6 | chunk: 71c124350557ecf1 | strength: statutory
permitted(president_of_the_republic, tribunal_regions, alter_regional_courts).

% atom_id: e465ed579c3f8290 | chunk: 71f25d064f194f93 | strength: statutory
obligated(judge_or_president, parties_and_witnesses, interrogate_parties_and_witnesses).

% atom_id: 2706011b5f3048bb | chunk: 71f25d064f194f93 | strength: statutory
permitted(vocals_or_parties_advocates, judge_or_president, reinterrogate_parties_and_witnesses).

% atom_id: a8911b3768547fbe | chunk: 7219fb317ea54d49 | strength: statutory
obligated(president_of_the_court, tribunal_session, chair_sessions).

% atom_id: c26a3470db62e5ff | chunk: 7235648f9b5dd9ce | strength: statutory
obligated(procurador_geral_do_trabalho, none, perform_duties).

% atom_id: 595739e75391f004 | chunk: 7235648f9b5dd9ce | strength: statutory
obligated(procurador_regional_do_trabalho, none, perform_duties).

% atom_id: 6bdea14252080b6e | chunk: 72a5af2e4f63ec4e | strength: statutory
obligated(employer, employee, deduct_sindical_contribution_from_salary) :-
    month(marco),
    employee_authorization(true).

% atom_id: 95c4461546ae08c6 | chunk: 72bc69567db6685d | strength: statutory
permitted(ministry_of_work_industry_and_commerce, employer, confer_honorary_degree) :-
    service_type(daycare),
    age_group(pre_school_children).

% atom_id: 0cf622ec654b9437 | chunk: 72db8ea855a700c7 | strength: statutory
obligated(employer, worker, equip_machines_with_safety_devices) :-
    risk_type(accidental_activation).

% atom_id: 3aff77a2f916af40 | chunk: 7311a74fb9f4919d | strength: statutory
obligated(worker, public, perform_labor_judiciary_service) :-
    justified_reason(true).

% atom_id: 94101849846915d6 | chunk: 733a6af04ba522c5 | strength: statutory
obligated(employer, worker, work_on_sunday) :-
    type_of_work(total_or_partial),
    authorization_status(not_received).

% atom_id: 84d0e186af85863d | chunk: 733a6af04ba522c5 | strength: statutory
permitted(authority, employer, grant_permission_to_work_on_sunday) :-
    type_of_work(total_or_partial).

% atom_id: e55e58644dba956b | chunk: 734002ea57929905 | strength: statutory
obligated(employer, workplace, ensure_minimum_ceiling_height).

% atom_id: 7bd2a39973cb6290 | chunk: 737c9dc5aa0eb877 | strength: statutory
prohibited(individual, none, forge_documents_for_labor_purposes).

% atom_id: bd1c8beed9417df1 | chunk: 73af2b028b736521 | strength: statutory
obligated(employer, pregnant_worker, relocate_from_hazardous_activities_during_pregnancy_and_lact) :-
    status(pregnant).

% atom_id: e749b684f0985d33 | chunk: 73af2b028b736521 | strength: statutory
obligated(employer, lactating_worker, relocate_from_hazardous_activities_during_pregnancy_and_lact) :-
    status(lactating).

% atom_id: 99f6513650db59a9 | chunk: 73af2b028b736521 | strength: statutory
obligated(employer, pregnant_worker, assign_to_safe_work_environment_during_pregnancy_and_lactati) :-
    status(pregnant).

% atom_id: 46e4adbd44d0c829 | chunk: 73af2b028b736521 | strength: statutory
obligated(employer, lactating_worker, assign_to_safe_work_environment_during_pregnancy_and_lactati) :-
    status(lactating).

% atom_id: 7b8a40e105ad0693 | chunk: 74d178b08207dfb1 | strength: statutory
obligated(chief_of_department, civil_or_military_employee, requisition_for_testimony) :-
    hour(work_hours).

% atom_id: 46290024ad6edc58 | chunk: 74d6a52de0ce1bc6 | strength: statutory
obligated(company, worker, maintain_special_incentive_and_professional_improvement_prog) :-
    number_of_employees(X_0), X_0 > 100.

% atom_id: 36afb90897b199b0 | chunk: 74e5aa9036054884 | strength: statutory
obligated(losing_party, none, pay_expert_fees) :-
    litigation_outcome(defeated).

% atom_id: ca2155fbfb9aad2f | chunk: 750a8e8e95bafcac | strength: statutory
obligated(judges_and_tribunals, worker, process_labor_disputes).

% atom_id: 768e4e5595e024f3 | chunk: 753cc69b3354a38d | strength: regulatory
permitted(chemical_engineer, public_office, preferential_application_for_public_position) :-
    equal_conditions(true).

% atom_id: e1939ad101688fb3 | chunk: 758ccac62ba547a6 | strength: statutory
obligated(authority, none, appoint_supplementary_member_for_each_vacancy).

% atom_id: 9d86b87da3d0c905 | chunk: 75aae18318e1f873 | strength: statutory
obligated(prejudiced_party, authority, reclaim_non_payment) :-
    non_payment(true).

% atom_id: 481c74c48a366ed3 | chunk: 75aae18318e1f873 | strength: statutory
obligated(authority, company, suspend_circulation) :-
    non_payment(true),
    judgment_issued(true).

% atom_id: b536b833d5fad40e | chunk: 75aae18318e1f873 | strength: statutory
obligated(company, none, deposit_indemnity_amount) :-
    judgment_issued(true),
    appeal_submitted(true).

% atom_id: 91de6052ec9dd734 | chunk: 75aae18318e1f873 | strength: statutory
obligated(company, none, pay_contributions) :-
    due_contributions(true).

% atom_id: c9f845fdada4c61e | chunk: 75aae18318e1f873 | strength: statutory
prohibited(company, none, suspend_circulation) :-
    due_contributions(false).

% atom_id: 44d99b80bf369a74 | chunk: 75ac4cb914da187f | strength: statutory
obligated(tribunal, none, execute_decisions).

% atom_id: 316266f20488e0a6 | chunk: 75b07a03298c8a54 | strength: statutory
permitted(president_of_juntas, none, exercise_privileged_attributions).

% atom_id: 421f917c2887d7e9 | chunk: 75db9f0c32f44255 | strength: statutory
obligated(employer, employee, reintegrate_stable_employees) :-
    false_claim_of_force_majeure(true).

% atom_id: a7a5aa25a85d0b6a | chunk: 75db9f0c32f44255 | strength: statutory
obligated(employer, non_stable_employee, complement_indemnity_received) :-
    false_claim_of_force_majeure(true).

% atom_id: 5abf4ff027e403ec | chunk: 75db9f0c32f44255 | strength: statutory
obligated(employer, employee, pay_arrears) :-
    false_claim_of_force_majeure(true).

% atom_id: fc6420fa8ab3e302 | chunk: 75e22d0f8577ba1c | strength: statutory
obligated(worker, none, carry_work_certificate).

% atom_id: d140dc7755d67eba | chunk: 75f06e80ea01e9a9 | strength: statutory
prohibited(authority, interested_party, issue_certificate) :-
    has_outstanding_issues(true).

% atom_id: 3d61736d58703489 | chunk: 75f5e93dbdea1ff7 | strength: statutory
obligated(judge_or_court, accused, notify_to_submit_written_defense).

% atom_id: 642b2e1b6b0bd4a2 | chunk: 75f701817a6c983a | strength: statutory
obligated(employer, employee_invention, share_patent_equally) :-
    invention_origin(work_contributions_and_company_resources),
    contract_object(scientific_research_explicit_or_implicit).

% atom_id: 5d5d185ac74323cb | chunk: 763fbdb4de8e24e4 | strength: statutory
obligated(employer, worker, provide_overtime_compensation) :-
    overtime_percentage_increase(n25).

% atom_id: 09a0a53575a4b646 | chunk: 764ab79fbc4fddcd | strength: regulatory
obligated(employer, worker, justify_salary_discount) :-
    salary_discount_determined_by_employer(false).

% atom_id: a67db3d5feeade8f | chunk: 766eaa76d2668020 | strength: statutory
obligated(employer, workplace, comply_with_safety_and_hygiene_conditions).

% atom_id: 927a27e44787ca39 | chunk: 766eaa76d2668020 | strength: statutory
obligated(employer, workplace, maintain_cleanliness_and_good_condition).

% atom_id: 204e91128e9744da | chunk: 76a3e4898fafb4ef | strength: statutory
obligated(president_of_the_court, none, exercise_presidency_duties).

% atom_id: ae8bc317fa6a39a5 | chunk: 76d1da5fa4386327 | strength: statutory
obligated(employer, worker, require_explicit_authorization_for_union_contribution_deduct) :-
    authorization_status(explicit_and_prior).

% atom_id: df6c62cc79603aef | chunk: 76d1da5fa4386327 | strength: statutory
obligated(sindical_authority, union_member, authorize_union_contribution_deduction) :-
    authorization_status(explicit_and_prior).

% atom_id: 63b089b58ab00a6e | chunk: 76d263c97cc0c69b | strength: statutory
obligated(authority, worker, resolve_individual_labor_disputes).

% atom_id: 5d5f99bac76230f3 | chunk: 76e5174851b8d149 | strength: statutory
obligated(state, worker, determine_minimum_wage_formula).

% atom_id: 515b16226ca94db9 | chunk: 7702b0c10b29fa2d | strength: statutory
obligated(employer, worker, instruct_precautions_to_avoid_illness_and_accidents).

% atom_id: baa8bd31ebd73ba7 | chunk: 7729fd5cdec8dda4 | strength: statutory
obligated(employer, worker, ensure_continuous_rest_period) :-
    work_nature(intermittent_or_low_intensity).

% atom_id: e1f176fa2f6d7489 | chunk: 772fb4963cee4f7e | strength: regulatory
obligated(association, member, maintain_membership_duration) :-
    membership_duration_months(X_0), X_0 >= 6,
    professional_experience_years(X_1), X_1 >= 2.

% atom_id: ec7d0dfb1dd7ac9d | chunk: 775264b88b114405 | strength: statutory
obligated(authority, litigant, notify_personally_in_audience).

% atom_id: 9a2c39abdb2675e3 | chunk: 775264b88b114405 | strength: statutory
obligated(authority, litigant, notify_by_established_form_in_case_of_default) :-
    revelia(true).

% atom_id: 79c0ee9890181692 | chunk: 7767fddd2167a9db | strength: statutory
obligated(collective, public, collaborate_with_public_authorities_for_social_solidarity).

% atom_id: dc4fc91486a24f23 | chunk: 77ef6e98b9f879c2 | strength: statutory
obligated(company, worker, maintain_proportion_of_brazilian_workers) :-
    number_of_employees(X_0), X_0 >= 3.

% atom_id: f9aa180636337380 | chunk: 789e5cfaa6049bdf | strength: statutory
obligated(driver, public, respect_traffic_legislation).

% atom_id: e8d15bd5b7974a0c | chunk: 789e5cfaa6049bdf | strength: statutory
obligated(driver, public, comply_with_driving_hours_and_rest_rules).

% atom_id: 048ec258ad6f7ecf | chunk: 78a10999b80aa9d2 | strength: statutory
obligated(deployer, equipment, install_safety_valve) :-
    operating_condition(under_pressure).

% atom_id: 01d940d48c59ea6d | chunk: 78a10999b80aa9d2 | strength: statutory
obligated(deployer, equipment, ensure_pressure_limit) :-
    operating_condition(under_pressure).

% atom_id: 28b95373bd274d6d | chunk: 78c2567d400802bd | strength: statutory
obligated(establishment, none, initiate_activities_after_inspection_approval) :-
    inspection_status(approved).

% atom_id: 179e6c919b10f2a9 | chunk: 78c2567d400802bd | strength: statutory
obligated(authority_regional, establishment, inspect_and_approve_installations).

% atom_id: 9e95b9be5921f8b4 | chunk: 78f7d1e71f897589 | strength: statutory
obligated(party, counter_party, give_notice_of_contract_rescission) :-
    justified_reason(false),
    contract_term(none).

% atom_id: 866fbe058f25eacb | chunk: 790fd0e15b1eb02a | strength: statutory
obligated(employer, worker, pay_compensation_on_contract_termination) :-
    contract_cause(any_reason),
    acquired_vacation_right(true).

% atom_id: bab96bf54055b55e | chunk: 795cd42981d605b6 | strength: statutory
obligated(authority, worker, attempt_conciliation).

% atom_id: 9daf36b10411e1da | chunk: 79c49e06fb551b1d | strength: regulatory
obligated(sindicate, member, register_member_information).

% atom_id: 1c3e848a7d140303 | chunk: 79e9ab569ae73a39 | strength: statutory
prohibited(employee, employer, terminate_contract_without_just_cause) :-
    contract_term(estipulated).

% atom_id: 622bad694c806a18 | chunk: 79e9ab569ae73a39 | strength: statutory
obligated(employee, employer, indemnify_employer_for_losses) :-
    contract_term(estipulated),
    termination_reason(just_cause).

% atom_id: e7d7217dd31fef72 | chunk: 79f257c380c0e18c | strength: statutory
obligated(employer, worker, ensure_full_and_irrevocable_settlement_of_rights) :-
    collective_agreement_type(voluntary_or_incentivized_dismissal_plan).

% atom_id: 4685e741221ffa50 | chunk: 7a401ddf8ea76141 | strength: statutory
prohibited(employer, worker, deduct_from_salary) :-
    salary_type(minimum_wage),
    compensation_reason(previous_month_shortfall).

% atom_id: 2e46f10bc677a1c5 | chunk: 7a401ddf8ea76141 | strength: statutory
obligated(employer, worker, guarantee_minimum_wage) :-
    salary_type(minimum_wage),
    compensation_reason(previous_month_shortfall).

% atom_id: 26524da02046f83b | chunk: 7af607ee10146dd0 | strength: statutory
obligated(authority, none, judge_embargoes_of_decisions) :-
    decision_divergence(true),
    decision_source(turmas_tribunal_pleno).

% atom_id: 8fc37179330bf72f | chunk: 7b0406eb8016fe2e | strength: statutory
obligated(worker, none, execute_assigned_tasks_by_president_of_junta).

% atom_id: 7b828eb16aa83d27 | chunk: 7b050b6c4c06ca6c | strength: statutory
obligated(court, contract_parties, presume_contractual_condition) :-
    agreement_existence(false),
    evidence_of_essential_condition(false).

% atom_id: 89960a4ee9d9e967 | chunk: 7b13d32991e116ff | strength: statutory
obligated(sindical_entities_and_central_sindicals, none, apply_percentages_according_to_statutes_or_contracts).

% atom_id: 0d936c7dda2d21b7 | chunk: 7b3c5d22a65af978 | strength: statutory
obligated(employer, worker, reduce_workload) :-
    work_type(piece_or_task),
    salary_impact(significant).

% atom_id: fc6e7fd2ad53d280 | chunk: 7b6810b00a747aca | strength: statutory
obligated(employer, worker, specify_compensation_details).

% atom_id: a673ee866393f229 | chunk: 7b8565fa65ee1faa | strength: statutory
permitted(employee, none, work_overtime_due_to_force_majeure) :-
    force_majeure_circumstances(true).

% atom_id: 08667b01613af097 | chunk: 7b8565fa65ee1faa | strength: statutory
obligated(employee, labor_authority, report_overtime_within_five_days) :-
    overtime_due_to_force_majeure(true).

% atom_id: 3501404a03c63e52 | chunk: 7bc755948ef0dc30 | strength: statutory
permitted(company, none, hire_apprentice).

% atom_id: 4f6ebf3489d34034 | chunk: 7bc755948ef0dc30 | strength: statutory
prohibited(company, none, generate_employment_relationship_with_service_provider_compa).

% atom_id: 85c034f1239bebb0 | chunk: 7c3cf8c6cefc1ac7 | strength: statutory
obligated(employer, employee, resolve_salary_dispute_in_labor_justice).

% atom_id: a3e3eaccd1b26d2a | chunk: 7c62d8ba4894f781 | strength: statutory
obligated(employer, worker, grant_leave_for_blood_donation) :-
    blood_donation(voluntary_and_proven),
    leave_frequency(one_day_per_twelve_months).

% atom_id: 25627b79910b6813 | chunk: 7c9c149903bad1b2 | strength: statutory
obligated(authority, vocal_supplementaries, convocate_in_vacancy).

% atom_id: 185cf4ebfababfb6 | chunk: 7cb6c014f0d5e4fd | strength: statutory
obligated(authority, worker, resolve_disputes_related_to_compensation_holiday_and_indemni).

% atom_id: c214e71d0d2e3b42 | chunk: 7cdbe6396a483d47 | strength: statutory
obligated(litigant, none, pay_embargo_fee).

% atom_id: 5b7b2ea832b5bf89 | chunk: 7d0739d64d4c6542 | strength: statutory
prohibited(non_state_actors, none, violate_nationality_requirements_professions).

% atom_id: 7a79f0d36b1e0d64 | chunk: 7d0739d64d4c6542 | strength: statutory
prohibited(non_state_actors, none, violate_frontier_zones_requirements).

% atom_id: 500fc1acddfd24ad | chunk: 7d1111989e399d96 | strength: regulatory
obligated(authority, interested_party, examine_documents_for_professional_registration).

% atom_id: 1b1d72893ae1f2ed | chunk: 7d1111989e399d96 | strength: regulatory
obligated(authority, interested_party, proceed_with_registration).

% atom_id: 1e184f36f429c3cf | chunk: 7d1111989e399d96 | strength: regulatory
obligated(authority, interested_party, reject_registration_request) :-
    satisfies_requirements(false).

% atom_id: 8d2149061194ac4c | chunk: 7d24b29088095526 | strength: statutory
permitted(judge, litigant_testimony_experts, formulate_questions).

% atom_id: 563ef5af0504c70f | chunk: 7d2e0ef28b19d14e | strength: statutory
obligated(employer, employee, deduct_contributions_from_payroll) :-
    employee_authorization(true),
    sindicate_notification(received).

% atom_id: 746451f518c2fd14 | chunk: 7d60e145fa0541a4 | strength: statutory
obligated(authority, professional, include_title_of_appointment_or_admission_in_wallet) :-
    employment_status(public_servant).

% atom_id: c13d9fa39294222c | chunk: 7d60e145fa0541a4 | strength: statutory
obligated(authority, professional, include_private_employment_certificate_in_wallet) :-
    employment_status(private_employee),
    job_title(chemist).

% atom_id: c2416dce77757931 | chunk: 7dc09d59ff876e85 | strength: statutory
prohibited(employer, workplace, suspend_operations_without_authorization).

% atom_id: 7252b51bd2fea8ec | chunk: 7dc09d59ff876e85 | strength: statutory
prohibited(employer, court_decision, violate_collective_dispute_resolution).

% atom_id: f6f2e4f78e73d665 | chunk: 7dc09d59ff876e85 | strength: statutory
prohibited(employer, court_decision, refuse_to_obey_collective_dispute_resolution).

% atom_id: 9091f8d2f59d0562 | chunk: 7dc9c9a7abc44b33 | strength: statutory
prohibited(employer, worker, exclude_participant_from_regime) :-
    type_of_benefit(profit_sharing),
    nature_of_profit(social_character).

% atom_id: 963f4b057902e214 | chunk: 7de1a15503895f83 | strength: statutory
obligated(employer, worker, pay_vacation_compensation).

% atom_id: 58009763d6bb14a1 | chunk: 7e39022220d83ce3 | strength: statutory
obligated(employer, worker, set_normal_work_duration_for_women).

% atom_id: 527b335ca09def98 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(rio_de_janeiro).

% atom_id: 3d52051a319b9308 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(sao_paulo).

% atom_id: bf33af6822f266f2 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(belo_horizonte).

% atom_id: 09f5f2f9bc20d0d7 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(porto_alegre).

% atom_id: e8dac5a26a929fc4 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(salvador).

% atom_id: 90058cc098f402f8 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(recife).

% atom_id: c176814559f82ba1 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(fortaleza).

% atom_id: ca8e5c2cc1f7f463 | chunk: 7ed00f851233770a | strength: statutory
obligated(tribunals, none, have_headquarters_in_designated_cities) :-
    city(belem).

% atom_id: f9aa9a126d37f663 | chunk: 7ede9a22acac1a4e | strength: regulatory
obligated(chemist, public, execute_services_requiring_chemical_knowledge) :-
    service_type(not_specified_in_regulation),
    qualification_status(habilitado).

% atom_id: 3d9c585817f599ce | chunk: 7f03fa32afbd2fb1 | strength: statutory
obligated(bank_director, employee, organize_shift_schedule) :-
    shift_time(half_hour_before_and_after_work_end),
    daily_working_hours(X_1), X_1 <= 6.

% atom_id: 2f0e4e2f726249f9 | chunk: 7f5fca05e98c543d | strength: statutory
permitted(worker, none, take_cancer_preventive_tests_days_off) :-
    days_taken_in_12_months(X_0), X_0 <= 3.

% atom_id: 3b5fb693f25f77d0 | chunk: 7fada4ca700a8575 | strength: statutory
obligated(employer, worker, provide_accident_insurance).

% atom_id: ccb594e879b788f2 | chunk: 7fd078f099145cff | strength: statutory
obligated(judiciary_authority, excipiente_and_testimonies, guarantee_oral_proof_production).

% atom_id: 34ed675f296f36f3 | chunk: 7ff92a24d057ad9a | strength: regulatory
obligated(associates, none, attend_and_vote_with_quorum) :-
    number_of_associates(X_0), X_0 > 5000.

% atom_id: 2e2bd3d87767b3dc | chunk: 80188c24b02e5a9e | strength: statutory
obligated(union, public, promote_lotifications).

% atom_id: 387620372e7b021e | chunk: 807ad45eae3006ec | strength: regulatory
obligated(provider, consumer, provide_reparation_in_case_of_cancellation) :-
    service_type(previously_scheduled).

% atom_id: c109c84cb747fcb8 | chunk: 80b9b2dc6b474760 | strength: statutory
obligated(court, litigant, judge_incompetency_exceptions).

% atom_id: 7bb8c6f41a7b2bb1 | chunk: 80d7b5a227907118 | strength: statutory
obligated(employer, child_worker, adhere_to_work_duration_restrictions).

% atom_id: 27f2059f0673b1ed | chunk: 81067cb57fbbc3d6 | strength: statutory
obligated(worker, none, carry_professional_card).

% atom_id: 66dd41371310163f | chunk: 815b18fe0e7753d8 | strength: statutory
prohibited(tribunal_superior_do_trabalho, none, deliberate_without_minimum_quorum) :-
    juiz_count(X_0), X_0 < 9.

% atom_id: b01df44d4eb32d13 | chunk: 819e7d5827d0a74a | strength: statutory
obligated(worker, none, submit_claim_directly_to_secretariat) :-
    juntas_conciliacao_julgamento_count(1).

% atom_id: c7684da74f77b884 | chunk: 819e7d5827d0a74a | strength: statutory
obligated(worker, none, submit_claim_directly_to_cartorio_juizo) :-
    escrivao_civel_count(1).

% atom_id: 9176b2a412abf9ff | chunk: 81cd0fb7bea8b6ce | strength: statutory
obligated(employer, worker, eliminate_or_neutralize_hazardous_conditions).

% atom_id: 49f5191a0e5b95be | chunk: 81cf510290c6c330 | strength: statutory
obligated(delegacia_regional_do_trabalho, worker, enforce_labor_laws).

% atom_id: 8d77c31de7a8c200 | chunk: 8210ff1fb99c90d3 | strength: statutory
obligated(authority, business_entity, legally_protect_image_brand_name_secrets_correspondence).

% atom_id: 280c4060b651ffa3 | chunk: 824142a55a242503 | strength: statutory
obligated(judge_or_president, public, maintain_order_in_hearings).

% atom_id: d0aa87111a94a3f1 | chunk: 824142a55a242503 | strength: statutory
permitted(judge_or_president, assistant, remove_from_hearing_room) :-
    disrupting_order(true).

% atom_id: e1273ca6937ac44e | chunk: 825560d86abad86a | strength: statutory
prohibited(court, litigant, file_embargos_based_on_overruled_divergence) :-
    divergence_status(overruled_by_tst_or_stf_summary).

% atom_id: 3ed90e52824656a8 | chunk: 825560d86abad86a | strength: statutory
prohibited(court, litigant, file_embargos_based_on_overruled_divergence) :-
    divergence_status(overruled_by_iterative_tst_jurisprudence).

% atom_id: 3818cb460770aaf5 | chunk: 82b084c25de52afa | strength: regulatory
obligated(sus_manager, none, provide_information_to_procurator_general).

% atom_id: 40668ef627c98b79 | chunk: 82b084c25de52afa | strength: regulatory
obligated(sus_manager, none, consult_procurator_general_in_doubt_cases).

% atom_id: e47e34017a198bf6 | chunk: 82dea572b273575f | strength: statutory
obligated(deployer, public, make_available_to_authorities_for_inspection).

% atom_id: 35fcc35eff44df6a | chunk: 83280355b4498b43 | strength: statutory
obligated(enterprise, none, form_association) :-
    association_type(employers),
    number_of_enterprises(X_1), X_1 >= 1.

% atom_id: f03d96f108cd9c16 | chunk: 83280355b4498b43 | strength: statutory
obligated(worker, none, form_association) :-
    association_type(employees),
    number_of_workers(X_1), X_1 >= 1.

% atom_id: 1aa297819486f23f | chunk: 83280355b4498b43 | strength: statutory
obligated(professional, none, form_association) :-
    association_type(freelancers),
    number_of_professionals(X_1), X_1 >= 1.

% atom_id: 343918d6a0f506cc | chunk: 837a608778eef512 | strength: statutory
obligated(judiciary_authority, none, function_in_judgment).

% atom_id: 64b72e0ae0ae1f26 | chunk: 839044ff1a791510 | strength: statutory
obligated(escrivao_or_secretario, reclamado, notify_for_hearing).

% atom_id: 3292244108d6e2b3 | chunk: 839044ff1a791510 | strength: statutory
obligated(escrivao_or_secretario, reclamado, send_second_petition_copy).

% atom_id: 18275cacbe7c0a0b | chunk: 83b72ddf14d22cea | strength: statutory
permitted(deployer, none, argue_compensation_as_defense) :-
    defense_matter(compensation_or_retention).

% atom_id: 000914ac262b6cc4 | chunk: 83bda07d00571ee8 | strength: statutory
obligated(authority, public, conduct_public_proceedings) :-
    interest_social(true).

% atom_id: cb2e790fd4f12c0a | chunk: 83bda07d00571ee8 | strength: statutory
prohibited(authority, public, conduct_public_proceedings) :-
    interest_social(true).

% atom_id: 67af56d01b55e854 | chunk: 83bda07d00571ee8 | strength: statutory
obligated(authority, public, conduct_public_proceedings_within_hours).

% atom_id: 5619b06ce9fcc66c | chunk: 83d698dbf4369d30 | strength: statutory
prohibited(part_interested, none, raise_jurisdiction_conflicts) :-
    exception_of_jurisdiction(already_opposed).

% atom_id: 50c2ac4bed79564e | chunk: 849ea36d82cadb7f | strength: statutory
obligated(employer, domestic_worker, provide_domestic_services_conditions).

% atom_id: b7c3743868f8ee77 | chunk: 8538650213fe7fb2 | strength: statutory
obligated(tribunal, tribunal, issue_instructions_for_good_functioning).

% atom_id: 9c27a014fe129eee | chunk: 856cfdda29e1f201 | strength: statutory
obligated(court, litigant, produce_evidence_in_hearing).

% atom_id: 8a57e78fefc3eacc | chunk: 858617d96e9d220e | strength: statutory
obligated(union_authority, worker, pronounce_on_work_relations_or_dispute).

% atom_id: c93c56cd748bf0b5 | chunk: 858617d96e9d220e | strength: statutory
obligated(union_authority, union_member, special_call_for_general_assembly) :-
    purpose_of_call(work_relations_or_dispute).

% atom_id: 1330825bb83fe4e1 | chunk: 858617d96e9d220e | strength: statutory
obligated(union_authority, general_assembly, be_valid_with_quorum_of_half_plus_one) :-
    status_of_associates(up_to_date).

% atom_id: 604d78019ff05e11 | chunk: 858617d96e9d220e | strength: statutory
obligated(union_authority, general_assembly, be_valid_with_quorum_of_two_thirds) :-
    status_of_associates(up_to_date),
    first_call_quorum(half_plus_one).

% atom_id: a171a661e48f64ba | chunk: 85ae5a24b0d36895 | strength: statutory
obligated(employer, worker, pay_overtime_hours) :-
    hours_worked(X_0), X_0 > 8.

% atom_id: affee57c9c161bfe | chunk: 85ae5a24b0d36895 | strength: statutory
obligated(employer, worker, pay_first_two_overtime_hours_with_25_percent_bonus) :-
    hours_worked(X_0), X_0 > 8,
    overtime_hours(X_1), X_1 <= 2.

% atom_id: a147e01037fdc05f | chunk: 85ae5a24b0d36895 | strength: statutory
obligated(employer, worker, pay_next_two_overtime_hours_with_50_percent_bonus) :-
    hours_worked(X_0), X_0 > 8,
    overtime_hours(X_1), X_1 > 2,
    overtime_hours(X_2), X_2 <= 4.

% atom_id: 26a8ae02836460e0 | chunk: 85ae5a24b0d36895 | strength: statutory
obligated(employer, worker, pay_remaining_overtime_hours_with_75_percent_bonus) :-
    hours_worked(X_0), X_0 > 8,
    overtime_hours(X_1), X_1 > 4.

% atom_id: 7a6e8fda11ad1f54 | chunk: 8603d12e9fa43884 | strength: statutory
obligated(employer, worker, provide_indemnity_for_force_majeure_closure) :-
    closure_reason(force_major),
    employment_status(terminated).

% atom_id: 2fbf75714491917e | chunk: 86752cf10ad91b5b | strength: statutory
obligated(authority, directoria, set_term_duration).

% atom_id: 20ac55816ea985c8 | chunk: 86992da29d4e9fea | strength: statutory
permitted(state, public, adopt_temporary_measures_for_gender_equality) :-
    gender_inequality_distorions(affecting_professional_training_access_to_employment_and_wor).

% atom_id: cf9b372ce498bc2b | chunk: 869aa98f11393590 | strength: statutory
obligated(employer, worker, set_normal_work_duration).

% atom_id: 970a4f5794ed7b0b | chunk: 86f75946787e7ff1 | strength: statutory
obligated(designated_personnel, none, function_in_sessions_of_the_regional_court).

% atom_id: 55d5feba013f6b55 | chunk: 86fdd89a7734c7d6 | strength: statutory
prohibited(employer, employee, terminate_employment_contract) :-
    years_of_service(X_0), X_0 >= 10.

% atom_id: c5a5866d303f6861 | chunk: 86fdd89a7734c7d6 | strength: statutory
permitted(employer, employee, terminate_employment_contract) :-
    years_of_service(X_0), X_0 >= 10,
    reason_for_dismissal(serious_offense).

% atom_id: 0193378589e2072f | chunk: 86fdd89a7734c7d6 | strength: statutory
permitted(employer, employee, terminate_employment_contract) :-
    years_of_service(X_0), X_0 >= 10,
    reason_for_dismissal(force_majeure).

% atom_id: 939f847662d03628 | chunk: 871bf311abb2f5ac | strength: statutory
permitted(executed_debtor, none, guarantee_execution_by_deposit) :-
    payment_status(unpaid).

% atom_id: 170a87db087040cf | chunk: 871bf311abb2f5ac | strength: statutory
permitted(executed_debtor, none, guarantee_execution_by_insurance) :-
    payment_status(unpaid).

% atom_id: c42b18925c65adf2 | chunk: 871bf311abb2f5ac | strength: statutory
permitted(executed_debtor, none, guarantee_execution_by_pledging_assets) :-
    payment_status(unpaid).

% atom_id: 94b9178a1ff6a2ca | chunk: 87a12fb5e2462967 | strength: statutory
obligated(employer, worker, transfer_worker_to_surface_jobs) :-
    health_reason(true),
    judgment_by_authority(true).

% atom_id: 4f9cf37e096f8d94 | chunk: 87a12fb5e2462967 | strength: statutory
obligated(employer, transfered_worker, ensure_equivalent_surface_job_compensation) :-
    health_reason(true),
    judgment_by_authority(true).

% atom_id: c866d5dc958acea9 | chunk: 87b02b6ac1801fe6 | strength: statutory
obligated(company, worker, compose_cipa_with_representatives).

% atom_id: 0af662b2bef0f9dc | chunk: 87c7f500232f8cf4 | strength: statutory
obligated(employer, worker, specify_hourly_wage_in_contract).

% atom_id: 7943c3324fe58e3f | chunk: 87c7f500232f8cf4 | strength: statutory
prohibited(employer, worker, set_hourly_wage_below_minimum).

% atom_id: 6e955cf1ee485a67 | chunk: 87e9962a14887e0a | strength: statutory
prohibited(parties, advocate, be_represented_by_common_advocate).

% atom_id: 81b7c55ec8aa5592 | chunk: 87f0ecacaa5ecc37 | strength: statutory
permitted(assembly_general, member_association, grant_compensation_for_mandate_exercise) :-
    work_absence_reason(mandate_exercise).

% atom_id: d1514bc5fe59cb3e | chunk: 8861647e2c031b67 | strength: statutory
obligated(sindicate, commission, define_constitution_and_functioning_rules).

% atom_id: 5bc93f88b5cccfd6 | chunk: 886793e44d607fd0 | strength: statutory
obligated(authority, vogal_juntas_suplentes, serve_for_three_years).

% atom_id: 4ca45a3b1abcbd87 | chunk: 886793e44d607fd0 | strength: statutory
permitted(authority, vogal_juntas_suplentes, grant_discharge_from_service) :-
    service_duration(n15_years).

% atom_id: e8c611d47a1cbc34 | chunk: 896cad2805d7b642 | strength: statutory
prohibited(employer, none, violate_labor_regulations).

% atom_id: d597c35d5f461357 | chunk: 898e47e7de5d999f | strength: regulatory
obligated(employer, rural_worker, apply_labor_dispositions_chapters_i_ii_vi).

% atom_id: 095e22abbba2142e | chunk: 8998ba175a3995a1 | strength: statutory
permitted(devedor, previdencia_social, immediate_payment_of_due_amount).

% atom_id: 1a286420ebfc37a4 | chunk: 899b901f6c68ae92 | strength: statutory
obligated(employer, worker, constitute_cipa).

% atom_id: 85430cfc837fdc52 | chunk: 89af19190ed922cb | strength: statutory
prohibited(collective, none, submit_invalid_petition_grievance).

% atom_id: 09ad234d972ed667 | chunk: 89af19190ed922cb | strength: statutory
obligated(authority, none, impose_petition_grievance_fee).

% atom_id: 4f2d66780aad55e5 | chunk: 89d79e04f809dd2c | strength: statutory
obligated(employer, employee, afastar_employee).

% atom_id: 101873573dacd169 | chunk: 89d993f67b019c3f | strength: statutory
obligated(state, class_representatives, appoint_equivalent_designees_or_elect_via_federations) :-
    confederation_existence(false).

% atom_id: 0c8c07df7440544e | chunk: 89f30e715869be80 | strength: statutory
obligated(employer, worker, pay_overtime_with_majoration) :-
    hour_number(1),
    category(c).

% atom_id: 588391b01f33d47b | chunk: 89f30e715869be80 | strength: statutory
obligated(employer, worker, pay_overtime_with_majoration) :-
    hour_number(2),
    category(c).

% atom_id: d0134d9c6991a8bb | chunk: 89f30e715869be80 | strength: statutory
obligated(employer, worker, pay_overtime_with_majoration) :-
    hour_number(X_0), X_0 > 2,
    category(c).

% atom_id: 99b4eecfc7d39c38 | chunk: 89f30e715869be80 | strength: statutory
prohibited(employer, worker, pay_overtime_with_majoration) :-
    negligence(true),
    category(c).

% atom_id: a36b31183b28206a | chunk: 8a6bac62563c9b2c | strength: statutory
obligated(employer, worker, calculate_rescission_benefits_based_on_average_wages).

% atom_id: 366568e8635ed68b | chunk: 8a7deb1ab0b164ee | strength: statutory
prohibited(authority, process_records, leave_court_registry) :-
    requester(authorized_lawyer),
    purpose(legal_proceeding_request).

% atom_id: 7a13f3e90e38a0a5 | chunk: 8a7deb1ab0b164ee | strength: statutory
permitted(authority, process_records, leave_court_registry) :-
    requester(authorized_lawyer),
    purpose(legal_proceeding_request).

% atom_id: 4d22e14b018800bb | chunk: 8a7deb1ab0b164ee | strength: statutory
obligated(authority, process_records, forward_to_competent_authority) :-
    purpose(appeal_or_request).

% atom_id: 611c8eec67c592a5 | chunk: 8a814b412d72d5e8 | strength: statutory
obligated(ministry_of_labor, professional_association, grant_sindical_investment_to_most_representative_association).

% atom_id: f145dfadde21546b | chunk: 8a9a33f472b46b5f | strength: statutory
obligated(inss, worker, attest_work_accident_or_disease) :-
    reason(work_accident_or_enfermidade),
    exception(inciso_iv_do_art_133).

% atom_id: 67d459eb2ad256e8 | chunk: 8b4418e1afc74781 | strength: regulatory
permitted(president_of_junta, none, decide_in_case_of_divergence) :-
    voting_outcome(divergent).

% atom_id: 462bad38ef1244e4 | chunk: 8b4418e1afc74781 | strength: regulatory
obligated(president_of_junta, none, ensure_legal_compliance_and_social_balance_in_decision) :-
    voting_outcome(divergent).

% atom_id: 24a623992a4c02bb | chunk: 8b521b9547591c10 | strength: statutory
prohibited(testimony_providing_party, none, intentionally_alter_truth_or_omit_essential_facts).

% atom_id: a1c1754d1b0eda6e | chunk: 8bc4e8112a271678 | strength: statutory
obligated(employer, worker, register_workers).

% atom_id: 0fc18a0fb3644f15 | chunk: 8bd1246d31ac72fc | strength: statutory
obligated(employer, labor_authority, submit_written_complaint_to_junta_or_court) :-
    employee_stability_guarantee(true),
    time_since_suspension(X_1), X_1 <= 30.

% atom_id: 5eb5c74d5eeac8d7 | chunk: 8c0b04f85a22d2d0 | strength: statutory
obligated(ministerio_publico_do_trabalho, public, zeal_for_constitution_and_laws_observation).

% atom_id: 11a84d6df8bec28f | chunk: 8c62f1ea7f9d0807 | strength: statutory
obligated(escrivao_judicial, none, perform_secretary_of_labor_conciliation_board_duties).

% atom_id: 95cf7409ad4088e9 | chunk: 8c62f1ea7f9d0807 | strength: statutory
obligated(other_cartorio_employees, none, perform_secretary_of_labor_conciliation_board_duties_within).

% atom_id: 338595c90f5b686c | chunk: 8d5b6c5a14342648 | strength: statutory
obligated(supremo_tribunal_federal, authorities, process_suscitados_between_authorities).

% atom_id: 7b6c7888e1abd5de | chunk: 8e07c6a78ed116e4 | strength: statutory
obligated(judge, litigant, calculate_liquidation_amount).

% atom_id: 533490a9ffee1b05 | chunk: 8e51ee6150f9718b | strength: statutory
obligated(authority, procurator_and_staff, grant_vacations).

% atom_id: 9d6401405387942b | chunk: 8e51ee6150f9718b | strength: statutory
obligated(authority, procurator_and_staff, impose_disciplinary_penalties).

% atom_id: 96284b6030246b90 | chunk: 8e633f44ba7c8aa5 | strength: statutory
obligated(employer, employee, pay_compensation_for_unjust_dismissal) :-
    dismissal_reason(without_just_cause),
    contract_type(fixed_term_contract).

% atom_id: 17e381562b8b00d9 | chunk: 8ecc3697e7b03e5b | strength: statutory
obligated(employer, employee_representatives, appoint_for_one_year_term).

% atom_id: f21612c4a5b529cc | chunk: 8ed9d6bc0d3c8544 | strength: statutory
prohibited(employer, foreign_worker, hire_as_apprentice_helper_or_servant) :-
    worker_nationality(foreign).

% atom_id: ab549c71924ecea0 | chunk: 8ed9d6bc0d3c8544 | strength: statutory
obligated(employer, brasilian_worker, hire_as_apprentice_helper_or_servant) :-
    worker_nationality(brasilian).

% atom_id: 7cf74c30787e1a24 | chunk: 8edc423aefdd841f | strength: statutory
obligated(authority, public, conduct_public_hearings).

% atom_id: c6dca6455a78c1ad | chunk: 8edc423aefdd841f | strength: statutory
prohibited(authority, public, conduct_public_hearings_outside_hours).

% atom_id: 252526d9030544df | chunk: 8edc423aefdd841f | strength: statutory
prohibited(authority, public, conduct_public_hearings_longer_than_five_hours).

% atom_id: a9489aeb5e8090c2 | chunk: 8edc423aefdd841f | strength: statutory
permitted(authority, public, extend_hearing_hours_for_emergency_matters).

% atom_id: d8f599b7ca9c8114 | chunk: 8ef1bb439d6bf723 | strength: statutory
obligated(employer, worker, suspend_work_contract_for_training) :-
    duration_of_suspension(n2_to_5_months),
    type_of_program(professional_qualification_course_or_program_offered_by_empl).

% atom_id: c371878acaed6b09 | chunk: 8ef1bb439d6bf723 | strength: statutory
obligated(employer, collective_agreement_or_convention, include_clause_for_suspension_of_contract).

% atom_id: fbb53f2e8a22be38 | chunk: 8ef1bb439d6bf723 | strength: statutory
obligated(worker, employer, formally_agree_to_suspension_of_contract_for_training).

% atom_id: 44d1cea4965b514b | chunk: 8f0018029faae388 | strength: statutory
permitted(employee, none, convert_vacation_period_to_monetary_benefit).

% atom_id: 3cba76ef78bbded9 | chunk: 8f2150b81a29b358 | strength: statutory
prohibited(authority, union_contribution, charge_tax_or_stamp_duty_on_union_contributions).

% atom_id: f5e5fa46494f91f2 | chunk: 8f706b6017cd86b9 | strength: statutory
permitted(operator, none, extend_working_hours_for_extraordinary_showings) :-
    additional_compensation_percentage(n25),
    rest_interval_duration(n2_hours).

% atom_id: 8561352f2125740e | chunk: 8f9ddd9a5f2ea993 | strength: statutory
obligated(employer, worker, grant_entitled_vacation_days).

% atom_id: 1b4fb5bfe18c0755 | chunk: 8fdb4aa2b9cab406 | strength: statutory
obligated(authority, employer, issue_free_electronic_certificate_of_no_debts).

% atom_id: b7c7a6be0ac956d1 | chunk: 900dfa958fca6ad1 | strength: statutory
obligated(employer, child, grant_time_for_school_attendance) :-
    employee_age(minor).

% atom_id: afce56618ec31ead | chunk: 9020b023f2da0a7b | strength: statutory
prohibited(employer, employee_representative, arbitrary_dismissal) :-
    motivation_type(none_of_disciplinary_technical_economic_or_financial).

% atom_id: 8278c494b9ab13ff | chunk: 903e58fa7441cf80 | strength: regulatory
obligated(sindicato, none, celebrate_collective_conventions_or_agreements) :-
    assembly_type(special_assembly),
    statute_provision(convention_or_agreement_statute).

% atom_id: 7b6005967fe420f5 | chunk: 903e58fa7441cf80 | strength: regulatory
obligated(sindicato, none, ensure_quorum_for_conventions_or_agreements) :-
    assembly_type(first_call),
    association_participation(X_1), X_1 >= 2.

% atom_id: 28bebff808ba8c24 | chunk: 903e58fa7441cf80 | strength: regulatory
obligated(sindicato, none, ensure_quorum_for_conventions_or_agreements) :-
    assembly_type(second_call),
    association_participation(X_1), X_1 >= 1.

% atom_id: f3688f97c09e32b9 | chunk: 9066b5f57e473a09 | strength: statutory
permitted(ministry_of_work_industry_and_commerce, none, establish_derivations_from_prohibitions) :-
    authority_opinion(favorable),
    service_type(periculosos_insalubres).

% atom_id: 06e2ee73683c3ef2 | chunk: 906f3dfa3cfdd1a2 | strength: statutory
obligated(authority, reclamant, evaluate_claim_within_fifteen_days).

% atom_id: 36aec1ee3d82af2b | chunk: 907beb879a66ddec | strength: statutory
obligated(employer, worker, comply_with_safety_and_health_rules).

% atom_id: 1c828cd326d908db | chunk: 90c80df869a1d824 | strength: statutory
obligated(judge, debtor_creditor, execute_extrajudicial_title) :-
    judicial_competence(knowledge_process).

% atom_id: 888f8e30a8d23353 | chunk: 90edd3977abb3812 | strength: statutory
obligated(employer, worker, establish_shift_rotation_schedule) :-
    work_day(domingo),
    exception(elencos_teatrais).

% atom_id: 0ffe7cc6548eb62c | chunk: 90f0f489624990f5 | strength: statutory
obligated(employer, worker, prevent_work_accidents).

% atom_id: afc166b0ced28662 | chunk: 919b80d02b2f6a37 | strength: statutory
obligated(employer, employee, record_incompatible_external_activity) :-
    activity_type(external),
    work_schedule_compatibility(incompatible_with_fixed_hours).

% atom_id: 9e7d73f6f2fc7a2c | chunk: 91b802d52d1fdde9 | strength: statutory
permitted(employer, worker, extend_working_hours_beyond_legal_limit) :-
    urgency_level(imperiosa).

% atom_id: fe72b8b6d4105176 | chunk: 91b802d52d1fdde9 | strength: statutory
obligated(employer, worker, extend_working_hours_due_to_force_majeure) :-
    urgency_level(imperiosa),
    circumstance(force_majeure).

% atom_id: 276e889294a3a883 | chunk: 91b802d52d1fdde9 | strength: statutory
obligated(employer, worker, extend_working_hours_for_essential_services) :-
    urgency_level(imperiosa),
    service_type(inadiveis).

% atom_id: 1d540683c657c582 | chunk: 91b802d52d1fdde9 | strength: statutory
obligated(employer, worker, extend_working_hours_to_avoid_manifest_loss) :-
    urgency_level(imperiosa),
    consequence_of_inaction(manifest_loss).

% atom_id: fa8a47c8e1a243dd | chunk: 91f00ba81f992d20 | strength: statutory
obligated(employer, bank_employee, grant_stability_rights) :-
    hire_date(data_vigencia_lei).

% atom_id: 5a56b6f7350010fc | chunk: 921ac7bd1c15875e | strength: statutory
obligated(employer, employee, record_nationality_and_id_number) :-
    employee_citizenship(foreigner).

% atom_id: d482b6c64cd79c1f | chunk: 9354bcb38dfc5f04 | strength: statutory
prohibited(employer, worker, employ_minor_workers_in_violation_of_law) :-
    number_of_infractions(X_0), X_0 > 0.

% atom_id: c54bc95d25afebd8 | chunk: 9354bcb38dfc5f04 | strength: statutory
prohibited(employer, none, exceed_total_fine_limit) :-
    total_fines(X_0), X_0 > 5.

% atom_id: 58d9ea094a787941 | chunk: 9378953d5b3682c2 | strength: statutory
permitted(authority, child, permit_participation_in_representation_with_educational_purp) :-
    representation_purpose(educative),
    performance_harm(not_harmful_to_moral_development).

% atom_id: 6328d5ab63dd396c | chunk: 9382ae0ef2af42bc | strength: statutory
prohibited(collective, none, non_observation_of_article_provisions).

% atom_id: b4728e9163811dc1 | chunk: 93a5e31704341b3e | strength: statutory
obligated(employer, child, provide_childcare_facilities_during_lactation_period) :-
    employee_status(operaria),
    activity_phase(lactacao).

% atom_id: db441f2f6bc85902 | chunk: 93a7fb7ad50419c5 | strength: statutory
obligated(worker, machine, stop_machinery_before_repair) :-
    repair_necessity(true).

% atom_id: 54444e3d8b813f6b | chunk: 93a7fb7ad50419c5 | strength: statutory
permitted(worker, machine, operate_machinery_during_adjustment) :-
    adjustment_necessity(true),
    continuous_operation(indispensable_for_adjustment).

% atom_id: 39342f7b88ad0a04 | chunk: 9435abf1d9440fc8 | strength: statutory
obligated(employer, worker, prohibit_work_on_holidays).

% atom_id: bbc91cd61971c5d0 | chunk: 945a4bdc37f5888d | strength: statutory
obligated(employer, worker, determine_best_fairness_period_for_vacations).

% atom_id: 69ca39c0050a3259 | chunk: 9486c4f73003af94 | strength: statutory
obligated(tribunal_do_trabalho, employer, convert_reintegration_to_indemnity) :-
    reintegration_incompatibility_level(high),
    employer_type(person_fisica).

% atom_id: e6a089660b786496 | chunk: 948737c3c4dbb7b4 | strength: statutory
obligated(authority, reclamations, alternate_distribution_among_registries).

% atom_id: a1e59aca6b89dd75 | chunk: 94ce58f68ad67f4e | strength: statutory
obligated(employer, worker, provide_extraordinary_service_compensation).

% atom_id: a9e80b2a52bba5b8 | chunk: 94ea3eb424906674 | strength: statutory
prohibited(representative_of_employees, none, act_in_contravention_of_labor_rights).

% atom_id: 1369c031dbcd8b65 | chunk: 94f3d2c3a25a4502 | strength: statutory
obligated(collective, none, contain_obligatory_clauses_in_conventions_and_agreements).

% atom_id: 6d864d55d3f424b6 | chunk: 9594f38c40f7fb95 | strength: regulatory
obligated(employer, worker, install_private_lockers_for_women) :-
    establishment_type(commercial_establishments),
    require_uniform_change(true).

% atom_id: def9e4832bc84b8f | chunk: 9594f38c40f7fb95 | strength: regulatory
permitted(authority, employer, allow_alternative_storage_solutions) :-
    establishment_type(commercial_establishments),
    require_uniform_change(false).

% atom_id: a57eb885265f497b | chunk: 95c8b44bd181f552 | strength: statutory
obligated(state, public, establish_and_maintain_literacy_schools).

% atom_id: 32f9096d0a801fb4 | chunk: 95cf039b3b3d9a12 | strength: statutory
obligated(judge, none, exercise_duties) :-
    period(caput_period),
    holiday_type(individual_holiday).

% atom_id: 704f612999a4fb0a | chunk: 95cf039b3b3d9a12 | strength: statutory
obligated(public_ministry_member, none, exercise_duties) :-
    period(caput_period),
    holiday_type(individual_holiday).

% atom_id: 706681792ad7700c | chunk: 95cf039b3b3d9a12 | strength: statutory
obligated(public_defender_member, none, exercise_duties) :-
    period(caput_period),
    holiday_type(individual_holiday).

% atom_id: 3d7c558957f6b05a | chunk: 95cf039b3b3d9a12 | strength: statutory
obligated(public_advocate_member, none, exercise_duties) :-
    period(caput_period),
    holiday_type(individual_holiday).

% atom_id: ceac07e46391f769 | chunk: 95cf039b3b3d9a12 | strength: statutory
obligated(justice_auxiliary, none, exercise_duties) :-
    period(caput_period),
    holiday_type(individual_holiday).

% atom_id: b5fc3a200d4602ed | chunk: 95daefb60f55b674 | strength: statutory
permitted(employer, worker, extend_work_duration_to_seven_hours) :-
    agreement_type(written),
    salary_increase(X_1), X_1 > 0.

% atom_id: 45a18294c92a5f4a | chunk: 95daefb60f55b674 | strength: statutory
obligated(employer, worker, provide_rest_or_meal_break) :-
    agreement_type(written),
    salary_increase(X_1), X_1 > 0.

% atom_id: abe513a8505cad7f | chunk: 960244932a2b64e5 | strength: regulatory
obligated(authority, workplace, conduct_first_inspection) :-
    establishment_status(recently_opened_or_started).

% atom_id: a3f8ec580c5617d7 | chunk: 960ed261722d10e4 | strength: statutory
prohibited(employer, worker, include_furlough_in_salary_for_legal_purposes).

% atom_id: 3361292fb0603774 | chunk: 964b4bf8eef899b3 | strength: statutory
obligated(employer, worker, specify_telework_services_in_individual_contract).

% atom_id: 1b5145222d990bb6 | chunk: 96a724d4d262c26f | strength: statutory
obligated(president_of_the_regional_court, distributors, appoint_from_existing_staff) :-
    staff_location(same_locality),
    staff_subordination(directly_to_president).

% atom_id: f0cb21a8711969ca | chunk: 96f0533a61d75f45 | strength: statutory
obligated(employer, employee, reimburse_previdenciary_contributions).

% atom_id: ab6f7eb4ac22e693 | chunk: 96f0533a61d75f45 | strength: statutory
obligated(employer, employee, deposit_fund_for_the_guarantee_of_timely_payment).

% atom_id: eaaf13ca940872da | chunk: 96f0533a61d75f45 | strength: statutory
obligated(employer, employee, provide_payment_confirmation).

% atom_id: 0af819346fc9cc57 | chunk: 96f2ac59462524c3 | strength: statutory
obligated(collective_agreement, law, prevail_over_law) :-
    subject_of_convention_or_agreement(work_conditions).

% atom_id: c4ce50ac155bcc21 | chunk: 97ec6f33c0b0c86f | strength: statutory
obligated(chemist, product_labeling, include_responsible_chemist_name_on_labels_invoices_and_ads).

% atom_id: c3c45bd759a8e1fe | chunk: 9828330ee54a9b74 | strength: statutory
permitted(establishment, none, be_supplied_by_other_entities) :-
    courses_or_vacancies_offered(demand).

% atom_id: 9b0f27f7537cf004 | chunk: 9828330ee54a9b74 | strength: statutory
obligated(other_entities, establishment, offer_courses_or_vacancies) :-
    qualification_of_other_entities(technical_professional_training).

% atom_id: d6c0fa7c820e8da7 | chunk: 983796f42f749d7d | strength: statutory
prohibited(employer, worker, not_attend_legal_requirements_for_compensation_of_work_hours) :-
    legal_requirements(compensation_of_work_hours),
    agreement_type(tacit_agreement).

% atom_id: d0c8bc375a85606b | chunk: 983796f42f749d7d | strength: statutory
prohibited(employer, worker, repeat_payment_of_excess_hours_within_weekly_limit) :-
    hours_worked(weekly_maximum_duration).

% atom_id: 2101cc719fd00a8a | chunk: 983796f42f749d7d | strength: statutory
obligated(employer, worker, pay_additional_compensation_for_excess_hours_within_weekly_l) :-
    hours_worked(weekly_maximum_duration).

% atom_id: 0424e369c5eb84a9 | chunk: 98657503b4fcfb3e | strength: statutory
obligated(employer, worker, use_cpf_as_unique_identification_in_ctps).

% atom_id: d5e86a659af83c7a | chunk: 98e2ac5839be0aeb | strength: statutory
permitted(tribunal, employer, extend_work_conditions_to_other_employees) :-
    dissidio_causa(novas_condicoes_trabalho),
    parties_involved(fraction_of_employees).

% atom_id: b43bd7943fb0335e | chunk: 9930a45e9d9bfb2f | strength: statutory
obligated(authority, public, declare_nullity_of_offending_acts) :-
    act_status(infringing_authoritative_decisions).

% atom_id: bcb9a1449d2acfc9 | chunk: 9943e47afc279a7c | strength: statutory
obligated(sus_manager, member, judge_suspicions).

% atom_id: 4977bda68dd56a14 | chunk: 999af8b84eec3b16 | strength: regulatory
obligated(secretaria_da_procuradoria_de_previdencia_social, public, execute_services_identical_to_art_753).

% atom_id: afd2dfeba7458566 | chunk: 99f539f74c8e81b2 | strength: statutory
obligated(sindicate, associates, hold_assembly_for_representation_approval) :-
    approval_percentage_first_call(n23),
    approval_percentage_second_call(n23).

% atom_id: 68adfb5054aa2ca7 | chunk: 9a1e86a252f0582c | strength: statutory
prohibited(employer, child, hire_under_18_without_cartao_trabalho) :-
    age(X_0), X_0 < 18.

% atom_id: eca286df81831671 | chunk: 9a1e86a252f0582c | strength: statutory
permitted(employer, child, hire_with_cartao_trabalho) :-
    age(X_0), X_0 < 18,
    cartao_trabalho(true).

% atom_id: dd7050c593847c31 | chunk: 9a1e86a252f0582c | strength: statutory
permitted(employer, child, hire_under_18_exception) :-
    age(X_0), X_0 < 18,
    exception_clause(true).

% atom_id: 7443c56777e964eb | chunk: 9a2b26ea883e1e81 | strength: statutory
obligated(authority, defendant, serve_citation_order) :-
    decision_type(execution_decision).

% atom_id: 3154a18af9893ced | chunk: 9a2b26ea883e1e81 | strength: statutory
obligated(authority, defendant, serve_citation_order) :-
    agreement_status(non_complied).

% atom_id: fbf79a99ab257136 | chunk: 9ad140cde34a066c | strength: statutory
obligated(state, public, promote_foundation_of_consumer_and_credit_cooperatives).

% atom_id: 2e4bb339ad822cd2 | chunk: 9ae31af5be8185fd | strength: statutory
obligated(employer, employee, prove_termination_reasons_in_labor_dispute) :-
    termination_occurred(true),
    labor_dispute_pending(true).

% atom_id: 4546d14b0be5cfe0 | chunk: 9b1a3fdd0bba3b3c | strength: statutory
obligated(chemist, supervisory_authority, notify_employment_within_24_hours).

% atom_id: e39a69476c7cc60b | chunk: 9b1a3fdd0bba3b3c | strength: statutory
obligated(chemist, production_process, assume_technical_responsibility).

% atom_id: c5182d292bd60b6c | chunk: 9b1a3fdd0bba3b3c | strength: statutory
obligated(chemist, manufactured_products, assume_technical_responsibility_of_products).

% atom_id: 6454e009c6492250 | chunk: 9b4b7864f00933c7 | strength: statutory
permitted(commander_or_sus_manager, none, take_preventive_measures_in_imminent_danger) :-
    imminence_of_danger(true).

% atom_id: a89f1b89a867b9f3 | chunk: 9b5a1699fa00ebae | strength: statutory
obligated(judge, court_sentence, include_elements_of_convinction_and_summary_of_relevant_fact).

% atom_id: 222a586d70c5bfff | chunk: 9bb537591d40e517 | strength: statutory
prohibited(employer, worker, require_services_exceeding_strengths).

% atom_id: 32fde0216be90e1b | chunk: 9bb537591d40e517 | strength: statutory
prohibited(employer, worker, require_services_contrary_to_good_customs).

% atom_id: 648d6404f7a6c72f | chunk: 9bb537591d40e517 | strength: statutory
prohibited(employer, worker, require_services_outside_contractual_agreement).

% atom_id: 8b883fcd02c51efe | chunk: 9c4a39fcee3b54f0 | strength: statutory
obligated(employer, spouse_or_partner_of_the_deceased_mother, grant_paternal_leave) :-
    mother_death(true).

% atom_id: e89a8f25d674b255 | chunk: 9c4a39fcee3b54f0 | strength: statutory
obligated(employer, spouse_or_partner_of_the_deceased_mother, grant_paternal_leave_for_remaining_period) :-
    mother_death(true),
    child_alive_and_not_abandoned(false).

% atom_id: d8d409219c7d9c24 | chunk: 9c57a2102f9ce529 | strength: statutory
obligated(employer, worker, compute_travel_time_for_salary_payment).

% atom_id: 458c219cccf4c324 | chunk: 9ca378e86b89affd | strength: statutory
obligated(employer, apprentice, terminate_apprenticeship_contract) :-
    age(24).

% atom_id: 06d2da1fc7449538 | chunk: 9ca378e86b89affd | strength: statutory
obligated(employer, apprentice, terminate_apprenticeship_contract) :-
    contract_term(end_of_term).

% atom_id: 889d21cdf9a1265e | chunk: 9ca378e86b89affd | strength: statutory
obligated(employer, apprentice, terminate_apprenticeship_contract) :-
    exception_clause(art_428_5th_paragraph).

% atom_id: ab7c916b5270c80a | chunk: 9ca378e86b89affd | strength: statutory
obligated(employer, apprentice, terminate_apprenticeship_contract) :-
    other_circumstances(specified_cases).

% atom_id: 840ba23594ae8d7d | chunk: 9cbdf4f14d9d040a | strength: regulatory
obligated(authority, none, judge_regular_appeals).

% atom_id: 081352e82e397a34 | chunk: 9d06983af432f074 | strength: statutory
obligated(union, none, fulfill_union_duties).

% atom_id: 79083e1232573f70 | chunk: 9d19c3462b6aca15 | strength: statutory
permitted(individual, none, promote_journalist_registration) :-
    activity_type(journalistic),
    purpose(cultural_scientific_religious).

% atom_id: 53321f0451147b91 | chunk: 9d2c04df9594c80f | strength: statutory
obligated(employer, worker, compute_work_time_for_military_service) :-
    days_since_baixa(X_0), X_0 <= 90.

% atom_id: 556fab869a3a784e | chunk: 9d4687959505a8f2 | strength: statutory
prohibited(collective, association_or_sindical_entity_patrimony, malversation_or_waste_of_patrimony).

% atom_id: 6ae59528c7d25f1d | chunk: 9d6b50bf6a027530 | strength: statutory
prohibited(collective, none, file_resource_recourse_to_plenary) :-
    decision_origin(turma),
    exception_case(item_i_alinea_c_inciso_1_artigo_atual).

% atom_id: 5bde4bf2d4ac2de3 | chunk: 9d959ae6737ff579 | strength: statutory
obligated(worker, none, observe_safety_and_health_rules).

% atom_id: a408ff4e64d5b1b8 | chunk: 9d9fc07965069d8d | strength: statutory
obligated(authority, worker, resolve_contract_disputes) :-
    contract_type(empreitada),
    employee_status(operario_ou_artefice).

% atom_id: ba850dc4e0d8ef0c | chunk: 9dbc1b0512b74d3e | strength: statutory
prohibited(employee, none, commit_just_cause_offense_during_notice_period).

% atom_id: 72a221b6691c7628 | chunk: 9dc00ccf6b4779c4 | strength: statutory
obligated(employer, adoptive_mother, grant_maternity_leave) :-
    adoption_status(guard_judicial).

% atom_id: e3fe24b8c952c964 | chunk: 9dd1eb1267740d32 | strength: statutory
obligated(tribunal_superior_do_trabalho, cause, examine_transcendence_in_recurso_de_revista).

% atom_id: 82db6d042ad2d1be | chunk: 9dd3308d8a29453b | strength: statutory
obligated(employer, woman, provide_reimbursed_rest_period) :-
    medical_certificate(non_criminal_abortion).

% atom_id: faf4b09a59c42f7b | chunk: 9dd3308d8a29453b | strength: statutory
obligated(employer, woman, guarantee_return_to_previous_position) :-
    medical_certificate(non_criminal_abortion).

% atom_id: d33aff30580690ee | chunk: 9dd88a8ec2edb1f0 | strength: statutory
obligated(employer, sindicato, notify_contract_suspension) :-
    authorization_method(collective_agreement),
    notification_period_days(X_1), X_1 >= 15.

% atom_id: 33286a46be147257 | chunk: 9dfb5b2433e6a59c | strength: statutory
obligated(vogal_juntas_e_suplentes, none, take_office_before_president_of_board).

% atom_id: 7ece2028c861f2d2 | chunk: 9e34e89beac7ac84 | strength: statutory
prohibited(employer, worker, transfer_without_consent).

% atom_id: d056b5cca131d544 | chunk: 9ea79a547aba250e | strength: statutory
obligated(professional_associations, none, satisfy_requirements_to_be_recognized_as_unions).

% atom_id: a2251f6a81676aaa | chunk: 9ecaf5952249260b | strength: statutory
obligated(employer, worker, pay_salaries_on_workday) :-
    payment_method(cash).

% atom_id: dc523f72f1a7a116 | chunk: 9ecaf5952249260b | strength: statutory
obligated(employer, worker, deposit_salaries_in_bank_account) :-
    payment_method(bank_deposit).

% atom_id: 355dd79c7adc30c2 | chunk: 9ecaf5952249260b | strength: statutory
obligated(employer, worker, pay_salaries_within_working_hours_or_immediately_after) :-
    payment_method(cash),
    workday(true).

% atom_id: f46d3683e4337003 | chunk: 9ed36e51eb5bd6ea | strength: statutory
prohibited(employer, none, violate_chapter_provisions).

% atom_id: b215174486abfaf8 | chunk: 9f80e1989d3965e5 | strength: regulatory
obligated(employer, worker, grant_leave_of_absence) :-
    absences(X_0), X_0 <= 5.

% atom_id: b140f632f1bcf442 | chunk: 9f90bcac69b46027 | strength: statutory
obligated(deployer, public, subcribe_certificates_and_procedural_terms).

% atom_id: 7c91207c32476368 | chunk: 9fa19e77bc71e54c | strength: statutory
obligated(authority, public, announce_arrematacao_by_edital) :-
    evaluation_completion(true),
    days_since_appraiser_naming(X_1), X_1 <= 10.

% atom_id: ef588c6e6b594385 | chunk: 9fa19e77bc71e54c | strength: statutory
obligated(authority, public, publish_arrematacao_notice_in_local_newspaper) :-
    evaluation_completion(true),
    days_since_appraiser_naming(X_1), X_1 <= 10.

% atom_id: e91cb009bead6c90 | chunk: 9fa19e77bc71e54c | strength: statutory
obligated(authority, public, announce_arrematacao_in_court_headquarters_or_tribunal) :-
    evaluation_completion(true),
    days_since_appraiser_naming(X_1), X_1 <= 10.

% atom_id: eac2489cb2902254 | chunk: 9fa19e77bc71e54c | strength: statutory
obligated(authority, public, publish_arrematacao_notice_with_20_days_advance) :-
    evaluation_completion(true),
    days_since_appraiser_naming(X_1), X_1 <= 10.

% atom_id: cec9b50350861fb4 | chunk: a000fd8bcbf2f126 | strength: statutory
obligated(authority, public, issue_executive_title) :-
    document_type(term_of_conciliation).

% atom_id: 62be2bd975d0c779 | chunk: a000fd8bcbf2f126 | strength: statutory
obligated(authority, public, grant_general_release_effect) :-
    document_type(term_of_conciliation).

% atom_id: 5f12fccaf4251409 | chunk: a000fd8bcbf2f126 | strength: statutory
prohibited(authority, public, grant_release_effect_for_excluded_parcelas) :-
    document_type(term_of_conciliation),
    parcela_status(expressly_reserved).

% atom_id: f8e0400e8575b961 | chunk: a01e8914419e9c02 | strength: statutory
obligated(state, worker, promote_safety_and_health_inspection).

% atom_id: ce66fe027fb2649b | chunk: a0492a8b031a6a41 | strength: regulatory
obligated(employer, worker, install_water_fountains_and_toilets).

% atom_id: fe939895ef7eb790 | chunk: a0492a8b031a6a41 | strength: regulatory
obligated(employer, worker, provide_sufficient_chairs_or_benches).

% atom_id: d0e663e43954a60d | chunk: a05e77d65e81b1d3 | strength: statutory
permitted(employee_and_employer, none, sign_annual_settlement_of_obligations) :-
    contract_status(during_contract_or_not),
    mediator(employee_sindicate).

% atom_id: e30cb67779fc6f2b | chunk: a0725ad0d1694eef | strength: statutory
obligated(armador, tripulante, grant_vacation_time) :-
    time_of_service_with_first_armador(X_0), X_0 > 0,
    current_armador(armador_in_which_tripulante_is_serving).

% atom_id: 5b46873964d02131 | chunk: a0fbe207a40bb179 | strength: statutory
obligated(judge_or_court, sus_manager, schedule_hearing_within_48_hours).

% atom_id: 9758de36b9c292ca | chunk: a0fc493a9731a968 | strength: statutory
obligated(employer, worker, grant_annual_vacation).

% atom_id: 225f19bcf709cc95 | chunk: a106707a37077934 | strength: statutory
prohibited(employer, worker, set_hourly_or_daily_wage_below_minimum_wage).

% atom_id: 17f819d31cb2ab4f | chunk: a106707a37077934 | strength: statutory
obligated(employer, worker, ensure_higher_night_shift_wage_than_day_shift).

% atom_id: 71537fa5ef5a4f32 | chunk: a12349d11f2a4b33 | strength: statutory
obligated(secretary_of_conciliation_and_judgment_board, none, perform_special_duties).

% atom_id: e9de976010d30606 | chunk: a1a00e5b14d447cc | strength: statutory
obligated(manufacturer, equipment, indicate_approval_certificate) :-
    approval_authority(ministry_of_labor).

% atom_id: 01e837ca38497bdc | chunk: a1a00e5b14d447cc | strength: statutory
prohibited(manufacturer, equipment, sell_or_use_without_certificate).

% atom_id: 0de7434fcffa474d | chunk: a1a1aa76a5619adc | strength: statutory
obligated(authority, procurador_geral, nominate_procurador_geral) :-
    years_of_experience(X_0), X_0 >= 5,
    previous_position(cargo_de_magistratura_ministerio_publico_advocacia).

% atom_id: 61bd8f656f72535e | chunk: a1dd889e7a70f719 | strength: statutory
prohibited(candidate, none, be_elected_for_professional_representation_positions) :-
    suspension_period(n2_to_5_years).

% atom_id: a6b2ae4da6993e69 | chunk: a1fc1fd020ba7882 | strength: regulatory
obligated(authority, candidate, provide_professional_orientation) :-
    selection_outcome(rejected).

% atom_id: 2c1fc96555e66125 | chunk: a200cc3c0292a10f | strength: statutory
obligated(tribunal_regional_president_substitute, public, function_as_auxiliary_of_the_tribunal) :-
    president_availability(absent_or_impaired).

% atom_id: 88b85aa6937464f7 | chunk: a21a7f4aabc01e5e | strength: statutory
permitted(collective, none, permit_reconduction_of_mandate).

% atom_id: 16ef178b901cf2ef | chunk: a281ead9d0fd5328 | strength: statutory
prohibited(trader, public, sell_or_expose_for_sale_similar_cartao).

% atom_id: fc0ef89e9864fa6e | chunk: a2dba85802d274fb | strength: statutory
obligated(vogal_tribunal_regional, none, take_office_before_president).

% atom_id: ec65b2962879d868 | chunk: a30feb65e1efaeab | strength: statutory
permitted(employer, worker, grant_collective_vacation).

% atom_id: caea6ba80df291f3 | chunk: a323a8e9880d59e9 | strength: statutory
obligated(employer, worker, provide_deposit_receipt) :-
    consent(true).

% atom_id: 5ed25d7a6cdb70af | chunk: a323a8e9880d59e9 | strength: statutory
obligated(bank, worker, issue_deposit_receipt) :-
    account_opened_for_worker(true).

% atom_id: 58a4d0e5ac90f341 | chunk: a333d967289d41a4 | strength: statutory
prohibited(company, none, violate_article_13_and_paragraphs).

% atom_id: af71486ae9fb9c40 | chunk: a3864a106e300fa6 | strength: statutory
obligated(crew, ship_nationality, constitute_crew_with_brazilians) :-
    nationality_of_ship(brazilian).

% atom_id: caabb2205a96d03e | chunk: a3d27edc3c7dd8c4 | strength: statutory
obligated(state, worker, establish_basic_sindical_enframing_plan).

% atom_id: 5539eac34cc84c2a | chunk: a3d676d8abfe3d31 | strength: statutory
obligated(authority, litigant, publish_decisions_during_hearing).

% atom_id: 8115b8ff481d3219 | chunk: a4201a3eef09d699 | strength: statutory
obligated(state, citizen, pay_certificate_fee).

% atom_id: bb2503ca33e40d32 | chunk: a4294d49d16a764d | strength: statutory
obligated(employer, pregnant_worker, grant_maternity_leave) :-
    employment_status(employed),
    pregnancy_status(pregnant).

% atom_id: 305df4a22984257b | chunk: a4294d49d16a764d | strength: statutory
obligated(employer, pregnant_worker, maintain_employment_during_maternity_leave) :-
    employment_status(employed),
    pregnancy_status(pregnant).

% atom_id: 32bb7ff1abbb6510 | chunk: a4294d49d16a764d | strength: statutory
obligated(employer, pregnant_worker, continue_salary_during_maternity_leave) :-
    employment_status(employed),
    pregnancy_status(pregnant).

% atom_id: 8939bf9ef435fb4b | chunk: a46297ff25645340 | strength: statutory
obligated(procurator, court, appear_in_court_first_instance).

% atom_id: 134e6bd7e2540860 | chunk: a46297ff25645340 | strength: statutory
obligated(procurator, court, designate_procurators_to_appear_in_court_first_instance).

% atom_id: e8d04d4793e731b7 | chunk: a4771cc92b594504 | strength: statutory
obligated(judge_or_president, non_linguistic_participant, appoint_interpreter_for_deposition) :-
    language_ability(does_not_speak_national_language).

% atom_id: 80fe7a1b90753391 | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, conduct_chemical_analysis).

% atom_id: 45762467508bcf76 | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, prepare_expert_opinions).

% atom_id: d2e3eda4408297d4 | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, issue_certificates).

% atom_id: 5a498f0b8bda38a6 | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, develop_specialty_projects).

% atom_id: 4958432e1876850c | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, execute_civil_or_judicial_expertise).

% atom_id: 5ce7ede67cad505d | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, direct_and_responsible_for_laboratories_or_departments).

% atom_id: 66f5113a192d1a53 | chunk: a48217d3e8c1e8c7 | strength: regulatory
obligated(chemist, public, direct_and_responsible_for_industrial_departments_or_commerc).

% atom_id: 91e5b15469c2ce15 | chunk: a4dce031108f4857 | strength: statutory
prohibited(employer, employee, infringe_article_29_caput_and_paragraph_1).

% atom_id: 5887041cfa790ec7 | chunk: a5b6f17ad1d60452 | strength: statutory
obligated(employer, worker, grant_rest_break_during_continuous_work) :-
    work_duration(X_0), X_0 > 6.

% atom_id: e138830819ce3c14 | chunk: a5b6f17ad1d60452 | strength: statutory
prohibited(employer, worker, extend_rest_break_beyond_two_hours) :-
    work_duration(X_0), X_0 > 6.

% atom_id: 4c202ec01a9b69b8 | chunk: a5b6f17ad1d60452 | strength: statutory
permitted(employer, worker, extend_rest_break_beyond_two_hours_with_agreement) :-
    work_duration(X_0), X_0 > 6,
    agreement_type(written_agreement_or_collective_contract).

% atom_id: 7ad437436c39a3ef | chunk: a5cbe3b3d1d2a431 | strength: statutory
prohibited(court, none, contradict_interpretation_of_federal_law) :-
    interpretation_source(another_regional_labor_court_plenary_or_division).

% atom_id: 06985c8d217a0707 | chunk: a5cbe3b3d1d2a431 | strength: statutory
prohibited(court, none, contradict_interpretation_of_federal_law) :-
    interpretation_source(labor_superior_court_individual_disputes_section).

% atom_id: c3c2f151190a8449 | chunk: a5cbe3b3d1d2a431 | strength: statutory
prohibited(court, none, contradict_interpretation_of_federal_law) :-
    interpretation_source(labor_superior_court_uniform_jurisprudence_summary).

% atom_id: bd6c5a0b21aeb62f | chunk: a5cbe3b3d1d2a431 | strength: statutory
prohibited(court, none, contradict_interpretation_of_federal_law) :-
    interpretation_source(supreme_court_binding_summary).

% atom_id: 40caaeee59aed8d6 | chunk: a5dda9959356aa80 | strength: statutory
obligated(authority, public, collect_fines_through_executive_fiscal).

% atom_id: d1a7ed03614f3a24 | chunk: a60f1f24edb058be | strength: statutory
obligated(deployer, none, convert_deposit_to_payment) :-
    recourse_provision(not_provided).

% atom_id: 85a40d64c72a8014 | chunk: a63d222a72cfc7ab | strength: statutory
permitted(authority, none, correct_errors_in_decision) :-
    type_of_error(writingtypingcalculation),
    status(before_execution).

% atom_id: 9ce82af1a4a2ef2f | chunk: a63d222a72cfc7ab | strength: statutory
permitted(interested_partyprocuradoria_do_trabalho, none, request_correction_of_errors_in_decision) :-
    type_of_error(writingtypingcalculation),
    status(before_execution).

% atom_id: 1844ea776ed0d081 | chunk: a652fcf6e5d43b45 | strength: statutory
obligated(directoria, delegados_sindicais, designate_leadership) :-
    territory(correspondente_delegacia).

% atom_id: 86dd30ebe23662bd | chunk: a6551d773622075e | strength: statutory
obligated(procurador_do_trabalho, ministry_of_labor, submit_annual_report) :-
    date(n31_mar).

% atom_id: 3754b8e90b4adcb4 | chunk: a6648306318aec7c | strength: statutory
obligated(employer, contract, consider_intermittent_contract_rescinded) :-
    time_since_last_call_or_service_day(n1_year).

% atom_id: 323fbf4db687634f | chunk: a666dddf351d57e3 | strength: statutory
prohibited(worker, none, file_labor_claim_without_junta_registration).

% atom_id: 877b835a40edc903 | chunk: a6a3d2cff8886efd | strength: statutory
obligated(employer, worker, set_work_hours_cabiniers).

% atom_id: fcc920a4e8969a64 | chunk: a6c60dcd955af135 | strength: statutory
obligated(caixa_economica_federal, sindical_contribution_revenue, allocate_sindical_contributions).

% atom_id: 43ebe9938036a5d4 | chunk: a6dfeff4427e8c27 | strength: statutory
permitted(beneficiary_of_legal_aid, none, be_exempt_from_payment_of_fees).

% atom_id: ba0317dd6a9b3c44 | chunk: a7027f1df15a415a | strength: statutory
obligated(authority, regional_procuracies, be_subordinate_to_general_procurator).

% atom_id: 22c282c2dd8249c8 | chunk: a71cab9b1bd99591 | strength: regulatory
obligated(authority, none, designate_vocals_and_supervisors_of_juntas).

% atom_id: 9061eb300d51f077 | chunk: a72353e50f936535 | strength: statutory
obligated(deployer, worker, comply_with_technical_requirements_for_safety).

% atom_id: d6198fb4a8280f9d | chunk: a74a43e399c3ff6b | strength: statutory
prohibited(employer, worker, fail_to_report_data).

% atom_id: 7e86d126344da524 | chunk: a7a1adac3fa9cf2d | strength: statutory
obligated(parties, judicial_process, choose_common_evaluator).

% atom_id: f870a3ab57e449a9 | chunk: a7a1adac3fa9cf2d | strength: statutory
obligated(judge_or_tribunal_president, evaluator, set_fees).

% atom_id: bb95454779154440 | chunk: a7a1adac3fa9cf2d | strength: statutory
obligated(superior_labor_tribunal, judicial_process, issue_fee_table).

% atom_id: 1de56f8ef64ff2ab | chunk: a7c075685ae5b364 | strength: statutory
obligated(collective_agreement, law, prevail_over_law) :-
    subject_of_convention_or_agreement(work_conditions).

% atom_id: 9d5410d53682a077 | chunk: a8181cceb039cd56 | strength: statutory
obligated(director_general_of_the_national_labor_department, public, issue_instructions_for_chapter_execution).

% atom_id: 644168f70d45c14b | chunk: a895eaeb2265a4d0 | strength: statutory
obligated(state, public, establish_norms_for_chapter_application).

% atom_id: 08bbe89e611a311a | chunk: a897f1ab1b1cba42 | strength: statutory
obligated(authority, crew_member, follow_hierarchy_regulation) :-
    regulation_approval(capitanias_portos).

% atom_id: f4c54a0dca6636e0 | chunk: a8bbe49560304266 | strength: statutory
prohibited(individual, none, affirm_false_identity_information).

% atom_id: b6c602170cad9f8b | chunk: a8bbe49560304266 | strength: statutory
prohibited(individual, none, attest_false_information_of_other_person).

% atom_id: 4d093d3fd80ae9e9 | chunk: a8e3e787d8734bbc | strength: statutory
permitted(employer, driver, remunerate_based_on_distance_time_or_quantity) :-
    compromised_safety(false),
    violated_norms(false).

% atom_id: cfd13d3059de19d3 | chunk: a964bb7bf4882d89 | strength: statutory
obligated(employer, labor_authority, appear_before_labor_authority).

% atom_id: 558b1f80b189043e | chunk: a964bb7bf4882d89 | strength: statutory
obligated(labor_authority, employer, record_attendance_in_term).

% atom_id: 4ab53bcda73a7139 | chunk: a964bb7bf4882d89 | strength: statutory
obligated(labor_authority, employer, provide_defense_period).

% atom_id: 9a74267984783b61 | chunk: a97b738f362c5b74 | strength: statutory
permitted(legal_entity, none, associate_with_professional_formation_entities).

% atom_id: 322489d97607443a | chunk: a97b738f362c5b74 | strength: statutory
permitted(legal_entity, none, sign_conventions_for_joint_actions).

% atom_id: b63a9a32b75336ed | chunk: a9b2b49d288a6cad | strength: statutory
obligated(employer, employee, condemn_criminal_employee) :-
    criminal_conviction_status(finalized),
    penalty_suspension(false).

% atom_id: 616de26efe5de9d0 | chunk: a9c39b4eec59369b | strength: statutory
obligated(parties_involved, none, sign_legal_documents_in_presence_of_witnesses) :-
    justified_reason(true),
    legal_representative_present(false).

% atom_id: 1d082609ddf8a1b3 | chunk: a9c39b4eec59369b | strength: statutory
obligated(witnesses, none, bear_witness_to_signing) :-
    number_of_witnesses(2).

% atom_id: 29110668c175b8a0 | chunk: a9c534344700c4ef | strength: statutory
obligated(authority, advocate, pay_legal_fees) :-
    case_type(own_case).

% atom_id: 6570ac9e59735d3c | chunk: aa64d7833784ffb2 | strength: statutory
obligated(employer, worker, pay_equivalent_to_one_day_of_work) :-
    employment_status(employee).

% atom_id: 2e78c74e328d67ba | chunk: aaa77c252c1e58e6 | strength: statutory
obligated(legal_representatives, minor_worker, file_labor_claim_on_behalf_of_minor) :-
    age(X_0), X_0 < 18.

% atom_id: cd85162b9e67b6b0 | chunk: aaa77c252c1e58e6 | strength: statutory
obligated(procuradoria_do_trabalho, minor_worker, file_labor_claim_on_behalf_of_minor) :-
    legal_representatives_availability(false).

% atom_id: 0014d405150d059c | chunk: aaa77c252c1e58e6 | strength: statutory
obligated(labor_union, minor_worker, file_labor_claim_on_behalf_of_minor) :-
    legal_representatives_availability(false).

% atom_id: 4217200943774e0c | chunk: aaa77c252c1e58e6 | strength: statutory
obligated(state_public_ministry, minor_worker, file_labor_claim_on_behalf_of_minor) :-
    legal_representatives_availability(false).

% atom_id: af297012c1ed4077 | chunk: aaa77c252c1e58e6 | strength: statutory
obligated(curator_appointed_by_court, minor_worker, file_labor_claim_on_behalf_of_minor) :-
    legal_representatives_availability(false).

% atom_id: d62bddc6590ec036 | chunk: aacaffe85655f4c1 | strength: statutory
obligated(inspector_agent, public, display_tax_identification_card).

% atom_id: 990a451bfefbda2a | chunk: aad1019e7c9f4151 | strength: statutory
obligated(deployer, public_authority, provide_information_to_public_ministry) :-
    request_origin(public_ministry),
    case_status(proposed_in_states_or_territories_for_execution_or_cancellat).

% atom_id: 2db1d7b5085916cf | chunk: ab3d56fb855181dd | strength: statutory
obligated(authority, none, impose_sanctions) :-
    violation_of_norms(true).

% atom_id: 5c0a5dae66079fc5 | chunk: ac4f8eeace818952 | strength: statutory
obligated(employer, chemist, admit_chemist) :-
    industry_type(specified_industries).

% atom_id: f2555e52a9f2e667 | chunk: ac5ff749f8d646ed | strength: statutory
obligated(debtor, receita_federal_brazil_secretariat, attach_adjustment_proof_to_records).

% atom_id: 4ab907930c6977bd | chunk: ac5ff749f8d646ed | strength: statutory
obligated(receita_federal_brazil_secretariat, debt_collection_process, suspend_debt_collection_until_full_payment).

% atom_id: 94a38a81f7dfc76a | chunk: ac777fad0d0eaf9c | strength: statutory
obligated(authority, collective, confer_conciliation_or_judgment_in_collective_disputes) :-
    dispute_type(collective),
    territorial_scope(tribunal_regional_trabalho_territorial_limit).

% atom_id: 3d79e5e63a39722f | chunk: ac777fad0d0eaf9c | strength: statutory
obligated(authority, collective, extend_or_revisit_normative_decisions_of_superior_labor_trib) :-
    legal_basis(prevision_in_legislation).

% atom_id: 369a3fad22af1c0d | chunk: ac8be23dc86e25c0 | strength: statutory
obligated(tribunal_de_trabalho, worker, reduce_indemnity_in_case_of_mutual_fault) :-
    fault_type(mutual).

% atom_id: ab9b79e9b7fd6657 | chunk: acabdc8d8cf88cbf | strength: statutory
obligated(employer, worker, prevent_work_accidents).

% atom_id: abc6a098e87f1e41 | chunk: acba191166840c2b | strength: statutory
obligated(employer, worker, improve_relationship_good_faith_respect).

% atom_id: 7d53a9a31e43ac02 | chunk: acc4ca4e84c484cb | strength: statutory
obligated(employer, child_worker, ensure_good_behavior_and_public_decency) :-
    age_of_employed_person(X_0), X_0 <=18 18.

% atom_id: 612687a133fe2c23 | chunk: acc4ca4e84c484cb | strength: statutory
obligated(employer, child_worker, comply_with_safety_and_health_rules) :-
    age_of_employed_person(X_0), X_0 <=18 18.

% atom_id: 8b47dc3115253030 | chunk: accbc06a3eb0dd75 | strength: statutory
prohibited(employer, work_record, make_other_annotations).

% atom_id: d6b1563f8d8f503b | chunk: acdc840f7df7ab49 | strength: statutory
obligated(authority, worker, resolve_stability_disputes).

% atom_id: 8119e43f7730c235 | chunk: ad065b6a6e8610c9 | strength: statutory
obligated(employer, worker, establish_compatible_position_salaries_and_roles).

% atom_id: 73fb3cd22950ee87 | chunk: ad99880ed2e8ea4d | strength: statutory
obligated(deployer, public, comply_with_orders_from_president_and_superiors).

% atom_id: a353a798334eacdc | chunk: ae38f42b24c40383 | strength: statutory
obligated(employer, operator_cinematographic_worker, limit_daily_work_hours).

% atom_id: a931dfea99192877 | chunk: ae8e6a0a4054c934 | strength: statutory
obligated(procurador_geral, tribunal, issue_ciente).

% atom_id: 23bd0b4e184a0b6f | chunk: ae96a32ff1ab95b8 | strength: regulatory
obligated(authority, none, fundament_decisions).

% atom_id: f7252c2e562d278c | chunk: aeecb7930655e5df | strength: statutory
prohibited(employer, worker, grant_stability_in_confidential_positions).

% atom_id: f21c71157b4b0ee9 | chunk: aeecb7930655e5df | strength: statutory
obligated(employer, worker, compute_service_time_for_confidential_positions).

% atom_id: 6f1f042f961368c9 | chunk: af0de9a6dd620253 | strength: statutory
prohibited(worker, none, recollect_sindical_contribution_outside_period) :-
    spontaneity(true).

% atom_id: 397ac5866c9aaabb | chunk: af0de9a6dd620253 | strength: statutory
obligated(worker, none, pay_financial_penalty) :-
    spontaneity(true),
    days_late(X_1), X_1 <= 30.

% atom_id: 2464e60f3a650256 | chunk: af0de9a6dd620253 | strength: statutory
obligated(worker, none, pay_additional_penalty_per_month_late) :-
    spontaneity(true),
    days_late(X_1), X_1 > 30.

% atom_id: c7cefe8df946d878 | chunk: af0de9a6dd620253 | strength: statutory
obligated(worker, none, pay_interest_on_delayed_contribution) :-
    spontaneity(true).

% atom_id: 4c497aabad9a1b7f | chunk: af0de9a6dd620253 | strength: statutory
obligated(worker, none, pay_monetary_adjustment_on_delayed_contribution) :-
    spontaneity(true).

% atom_id: 4a3c4f192ede7e67 | chunk: af0de9a6dd620253 | strength: statutory
prohibited(worker, none, receive_other_penalties) :-
    spontaneity(true).

% atom_id: 4f81fdd25298cee5 | chunk: af121f16bb25ce90 | strength: statutory
prohibited(employer, worker, reduce_salary_for_safety_measures).

% atom_id: c98462c925ef1e6b | chunk: af3e8e086ab17a2d | strength: statutory
obligated(president_and_substitute_presidents, none, take_office_before_regional_tribunal_president).

% atom_id: 7a812715b3f335aa | chunk: af742a9277e2e5b6 | strength: statutory
obligated(tribunal_authority, vogal_and_tribunal_staff, sign_payroll_sheets).

% atom_id: e55682438d9f6ad6 | chunk: afc52ae6c2e193a9 | strength: statutory
obligated(procuradores_regionais, none, perform_regional_duties).

% atom_id: 6e71e568ba5db7ba | chunk: afd59fe7e1de5b18 | strength: statutory
obligated(authority, reclamation_proceeding, summarize_in_minutes).

% atom_id: 42b1451eca3a4c99 | chunk: afd59fe7e1de5b18 | strength: statutory
obligated(authority, minutes_of_proceeding, include_decision_intact).

% atom_id: bdf3ac5adbc727cc | chunk: b056bbdf29f092a8 | strength: statutory
prohibited(individual, none, hold_position_under_25_years_old) :-
    age(X_0), X_0 <= 25.

% atom_id: 481434acc16c3afe | chunk: b056bbdf29f092a8 | strength: statutory
prohibited(individual, none, hold_position_over_70_years_old) :-
    age(X_0), X_0 >= 70.

% atom_id: 8d9b318bb9c814ee | chunk: b0740a85d17c6237 | strength: statutory
obligated(employer, worker, adopt_measures_to_conserve_work_environment_within_tolerance).

% atom_id: 27869f2694a9e0f0 | chunk: b092d594b016427a | strength: statutory
obligated(worker, none, submit_representation_in_multiple_copies) :-
    number_of_defendants(reclamados).

% atom_id: 63b9a9e6bb387c0d | chunk: b0bc587520c9bfeb | strength: statutory
prohibited(non_brazilian_natural_person, ship_command, exercise_ship_command_on_merchant_vessel).

% atom_id: f3426f6e2f228c40 | chunk: b14183588b755230 | strength: statutory
obligated(builder, public, protect_openings_from_falls).

% atom_id: 1cfd002b6fbdb6b2 | chunk: b274f8b9ac4a4e00 | strength: statutory
obligated(professional, state_authority, collaborate_in_study_and_solution_of_problems).

% atom_id: 0c21ab64a10c8f7b | chunk: b27e7aad9f70a9dd | strength: statutory
obligated(employee_representative, employer, represent_employees_before_company_administration).

% atom_id: ab2bcbe8db50d137 | chunk: b376185086d3e7f0 | strength: statutory
obligated(employer, worker, organize_shift_rotation_for_sunday_work).

% atom_id: c26b82ff6d8a3226 | chunk: b385d951dcfb7b87 | strength: statutory
permitted(employee, none, skip_work_without_salary_penalty).

% atom_id: 8b769b2b6c5b4c69 | chunk: b4031c42af015b7f | strength: statutory
prohibited(worker, none, provocate_unfounded_incident).

% atom_id: 81be79fe751005e7 | chunk: b403de988bd3ab11 | strength: statutory
prohibited(employer, worker, contract_trial_period_exceeding_90_days).

% atom_id: 2228ebbb0a1c274b | chunk: b446df792e2e4e71 | strength: statutory
obligated(authority, public, lavar_termo_conciliacao).

% atom_id: 0081b6bb2c7cf021 | chunk: b446df792e2e4e71 | strength: statutory
obligated(previdencia_social, public, consider_contributions_due) :-
    term_type(conciliacao).

% atom_id: 65897fd60c105ea9 | chunk: b4666bf51cdb31ee | strength: statutory
permitted(ministry_of_works, union, authorize_national_union_recognition) :-
    category_peculiarities(true).

% atom_id: c2edd5c7ba11f704 | chunk: b47f902eeb418b87 | strength: statutory
obligated(employer, worker, provide_productivity_based_compensation_including_tips).

% atom_id: f0a435a1aaec28d1 | chunk: b4a4204ff4e9429f | strength: statutory
obligated(authority, none, inscribe_in_special_book) :-
    infractor_presence(absent),
    fine_deposit(not_received).

% atom_id: d0e0b0ac8b08db8b | chunk: b4a4204ff4e9429f | strength: statutory
obligated(authority, none, send_copy_of_inscription_to_authorities) :-
    infractor_presence(absent),
    fine_deposit(not_received).

% atom_id: d6d40102930941b3 | chunk: b4a4204ff4e9429f | strength: statutory
obligated(authority, none, treat_inscription_as_legal_title) :-
    infractor_presence(absent),
    fine_deposit(not_received).

% atom_id: 429aa0320447dbb1 | chunk: b4be449be30c7e33 | strength: statutory
prohibited(non_state_actors, none, violate_dispositions_of_title).

% atom_id: 5f4a198ceca01906 | chunk: b4be449be30c7e33 | strength: statutory
prohibited(non_state_actors, none, reoffend_violating_dispositions_of_title).

% atom_id: 792140210f50860a | chunk: b54489df77ef6ea6 | strength: statutory
obligated(tribunal, none, mark_date_for_extension_to_take_effect).

% atom_id: a0b802269330cd97 | chunk: b55df71acd94a394 | strength: statutory
prohibited(individual, document, create_false_document).

% atom_id: 7f2f83a6d600ab28 | chunk: b55df71acd94a394 | strength: statutory
prohibited(individual, document, alter_true_document).

% atom_id: 860a70136770a0eb | chunk: b5847e8bad946fe2 | strength: statutory
permitted(pregnant_woman, none, terminate_contract_due_to_pregnancy_risks) :-
    medical_attestation(true),
    contract_harmful_to_pregnancy(true).

% atom_id: 4b1f02db7d0e9cb1 | chunk: b5a980b6bfcbcc82 | strength: statutory
obligated(collective, none, comply_with_agreement_or_judgment).

% atom_id: 7fbd8cd010deb753 | chunk: b5af5e6e67d1a905 | strength: statutory
prohibited(employer, contributor, deduct_contribution_from_salary) :-
    manifestation_of_contributor(true),
    proof_of_quittance(issued_by_professionals_union).

% atom_id: e264e3c16fa8a138 | chunk: b5c0b649b6d797b6 | strength: statutory
obligated(employer, worker, limit_work_hours_telegraph_operator).

% atom_id: 8433bbc6a441a798 | chunk: b668acb30c667413 | strength: statutory
obligated(authority, worker, resolve_disputes_through_labor_justice).

% atom_id: 5cbd30cbb9d70e0e | chunk: b66fd18418ed68ee | strength: statutory
obligated(ministry_of_labor, professional_association, issue_recognition_certificate) :-
    association_type(sindicato).

% atom_id: 92910eab0732ee51 | chunk: b680a1a24a1c0847 | strength: statutory
obligated(establishment, worker, employ_apprentices) :-
    percentage_of_workers(X_0), X_0 >= 5,
    percentage_of_workers(X_1), X_1 <= 15.

% atom_id: 48f24786c84ae4eb | chunk: b680a1a24a1c0847 | strength: statutory
obligated(establishment, apprentice, enroll_in_training_courses) :-
    percentage_of_workers(X_0), X_0 >= 5,
    percentage_of_workers(X_1), X_1 <= 15.

% atom_id: d355e8120dae6078 | chunk: b680a1a24a1c0847 | strength: statutory
obligated(national_training_services, apprentice, offer_courses) :-
    percentage_of_workers(X_0), X_0 >= 5,
    percentage_of_workers(X_1), X_1 <= 15.

% atom_id: 95a0e2ba4430ac1b | chunk: b6898c44f96df510 | strength: statutory
obligated(authority, public, judge_aggravated_dismissal_orders).

% atom_id: ce8e9d8b43e33945 | chunk: b701057a938ad2c3 | strength: statutory
prohibited(employer, candidate, require_experience_proof) :-
    experience_duration_months(X_0), X_0 > 6.

% atom_id: 4c5ef4467266c13f | chunk: b76697c7b4895bc8 | strength: statutory
obligated(worker, none, become_sindicalized) :-
    years_of_experience(X_0), X_0 >= 2.

% atom_id: b6d4675e80ba81fa | chunk: b7a47de5ad97d0b9 | strength: statutory
obligated(employer, worker, grant_vacation_leave) :-
    contract_duration_months(12).

% atom_id: 529bc85fc5378204 | chunk: b7f62d8dce6a5581 | strength: statutory
prohibited(scientist, public, participate_in_crime_or_public_endangerment).

% atom_id: 9fb8248ff76da8e7 | chunk: b81c3ac6de317b7a | strength: statutory
prohibited(individual, none, refuse_jcj_vogal_position) :-
    justification(unjustified).

% atom_id: b2e90a8e159e8afb | chunk: b81c3ac6de317b7a | strength: statutory
prohibited(individual, none, refuse_trb_regional_position) :-
    justification(unjustified).

% atom_id: 2b878727d6fca2f8 | chunk: b8f550ed4e28e338 | strength: statutory
obligated(reclamado, court_proceeding, present_defense_within_time_limit) :-
    agreement_status(no_agreement).

% atom_id: b74f0de45e771e52 | chunk: b9e02ec77401b697 | strength: statutory
permitted(minister_of_labor_and_social_security, trade_union_entity, intervene_in_trade_union) :-
    dissidio_or_circumstances(perturbs_functioning),
    reasons(national_security).

% atom_id: 24501e11fe9e8a94 | chunk: b9e02ec77401b697 | strength: statutory
obligated(delegado_or_interventory_board, trade_union_entity, administrate_trade_union) :-
    dissidio_or_circumstances(perturbs_functioning),
    reasons(national_security).

% atom_id: 48743440c90ab4da | chunk: b9e02ec77401b697 | strength: statutory
obligated(delegado_or_interventory_board, trade_union_entity, execute_measures_to_normalize_functioning) :-
    dissidio_or_circumstances(perturbs_functioning),
    reasons(national_security).

% atom_id: baa35f730556ab04 | chunk: bb21398563ac4b25 | strength: statutory
prohibited(employer, worker, include_utilities_in_salary).

% atom_id: 741038a754f71391 | chunk: bb40ad8e056fdb48 | strength: regulatory
obligated(deployer, none, register_communications_and_contracts).

% atom_id: 1d447b9207a96457 | chunk: bb40ad8e056fdb48 | strength: regulatory
obligated(deployer, none, provide_contract_cancellations).

% atom_id: 7afffe4e748737a2 | chunk: bb45de8a66025c1f | strength: statutory
obligated(federation, none, represent_group_percentage) :-
    confederation_existence(false).

% atom_id: 42a2b1d6b69f3266 | chunk: bb6f15ccc741f681 | strength: statutory
obligated(employer, worker, record_employment_data).

% atom_id: f62a0c2ea8df9fe9 | chunk: bb8768d8274d117e | strength: statutory
obligated(sindicato, federation, obey_rules_for_aggregation_in_federations).

% atom_id: 4d2e2bd305dcdadb | chunk: bb9be60505b8608b | strength: statutory
obligated(employer, worker, maintain_social_worker_in_staff) :-
    possibilities(possible).

% atom_id: a5494a894f301114 | chunk: bb9be60505b8608b | strength: statutory
obligated(employer, worker, promote_operational_cooperation_in_company) :-
    possibilities(possible).

% atom_id: 75be718fe57b6198 | chunk: bb9be60505b8608b | strength: statutory
obligated(employer, worker, promote_professional_integration_in_class) :-
    possibilities(possible).

% atom_id: 94fb4e756cb0b175 | chunk: bc16d7175d6ad15f | strength: statutory
obligated(company, worker, organize_shifts_to_avoid_overtime) :-
    work_category(c).

% atom_id: 764fcfddc8a41075 | chunk: bc16d7175d6ad15f | strength: statutory
prohibited(company, worker, extend_working_hours_beyond_12_hours) :-
    work_category(c).

% atom_id: a0256ee33bc5fdd2 | chunk: bc196d4d92d948fd | strength: statutory
obligated(sus_manager, authority, request_and_monitor_diligence).

% atom_id: dba60d78dd014e57 | chunk: bc1c9b9b1ff5b4c7 | strength: statutory
prohibited(employer, worker, terminate_employment_contract) :-
    reason_for_absence(military_service).

% atom_id: ab18865b97281b7f | chunk: bc1c9b9b1ff5b4c7 | strength: statutory
prohibited(employer, worker, alter_employment_contract_terms) :-
    reason_for_absence(public_duty).

% atom_id: 197d1ea9f0ac00a4 | chunk: bc236798b82f6d9b | strength: regulatory
obligated(sus_manager, juntas, exercise_correction_at_least_once_per_year).

% atom_id: 5507cd9b07c83891 | chunk: bc236798b82f6d9b | strength: regulatory
permitted(sus_manager, president_of_appeals_court, request_correction_when_convenient) :-
    judges_invested_in_labor_justice_administration(true).

% atom_id: 248e19f25729e77f | chunk: bc3e4a0cb72c06b4 | strength: statutory
obligated(authority, procurator_and_staff, grant_vacations).

% atom_id: e63efc2a10df741e | chunk: bc3e4a0cb72c06b4 | strength: statutory
obligated(authority, procurator_and_staff, impose_disciplinary_penalties).

% atom_id: 82c080a4d2af755d | chunk: bc3e516b7d90d8ce | strength: statutory
obligated(authority, public, decide_according_to_legal_principles) :-
    disposicoes_legais_contratuais(null).

% atom_id: e51c40430e7cbbe2 | chunk: bc3e516b7d90d8ce | strength: statutory
prohibited(authority, public, favor_class_or_individual_interest_over_public_interest).

% atom_id: 5ff237fed092e6e9 | chunk: bd3a71517549f313 | strength: statutory
prohibited(authority, judicial_decision, register_in_credit_protection_orgs) :-
    days_since_citation(X_0), X_0 <= 45,
    judgment_guarantee(false).

% atom_id: 5f0231efde8fc20a | chunk: bd3a71517549f313 | strength: statutory
prohibited(authority, judicial_decision, register_in_bndt) :-
    days_since_citation(X_0), X_0 <= 45,
    judgment_guarantee(false).

% atom_id: ae3b74a0efe24e61 | chunk: bd3a71517549f313 | strength: statutory
prohibited(authority, judicial_decision, register_in_credit_protection_orgs) :-
    days_since_citation(X_0), X_0 <= 45,
    judgment_guarantee(false).

% atom_id: 3cb469fa87441412 | chunk: bd3a71517549f313 | strength: statutory
prohibited(authority, judicial_decision, register_in_bndt) :-
    days_since_citation(X_0), X_0 <= 45,
    judgment_guarantee(false).

% atom_id: c4490bd277bcd131 | chunk: bd3a71517549f313 | strength: statutory
permitted(authority, judicial_decision, register_in_credit_protection_orgs) :-
    days_since_citation(X_0), X_0 > 45.

% atom_id: a2d3c04746b46d54 | chunk: bd3a71517549f313 | strength: statutory
permitted(authority, judicial_decision, register_in_bndt) :-
    days_since_citation(X_0), X_0 > 45.

% atom_id: 7f53dffb68be6c1e | chunk: bd3a71517549f313 | strength: statutory
permitted(authority, judicial_decision, register_in_credit_protection_orgs) :-
    judgment_guarantee(true).

% atom_id: bbd6b5504d2b3c22 | chunk: bd3a71517549f313 | strength: statutory
permitted(authority, judicial_decision, register_in_bndt) :-
    judgment_guarantee(true).

% atom_id: a39bc427ba92133d | chunk: bdad04663c928d88 | strength: regulatory
obligated(state, public, define_convocation_forms_and_instruments_for_service_provisi).

% atom_id: 2df49983933479ea | chunk: bdaf5d99399b9193 | strength: statutory
obligated(employee_representatives_committee, none, exercise_assigned_attributions).

% atom_id: 9951230c603dddb9 | chunk: bdc297741c3b9214 | strength: statutory
obligated(worker, employer, receive_insurance_benefit) :-
    work_condition(insalubre),
    tolerance_limit(established_by_ministry_of_labor).

% atom_id: 4b1db8552d8f41b3 | chunk: bdc297741c3b9214 | strength: statutory
obligated(employer, worker, provide_insurance_benefit) :-
    work_condition(insalubre),
    tolerance_limit(established_by_ministry_of_labor).

% atom_id: cf51f648b00c5c29 | chunk: bdc297741c3b9214 | strength: statutory
obligated(employer, worker, provide_insurance_benefit) :-
    work_condition(insalubre),
    tolerance_limit(established_by_ministry_of_labor).

% atom_id: 6325d3c8f866d6cf | chunk: bdc297741c3b9214 | strength: statutory
obligated(employer, worker, provide_insurance_benefit) :-
    work_condition(insalubre),
    tolerance_limit(established_by_ministry_of_labor).

% atom_id: b611908a583ed538 | chunk: bdea05bed341c8c2 | strength: statutory
obligated(sindicato_directoria, empregados_sindicato, nominate_employees_ad_referendum_assembly_general) :-
    employee_conditions(item_ii_item_iv_item_v_item_vi_item_vii_item_viii),
    nominator_conditions(item_i).

% atom_id: 498bb840d27683d0 | chunk: be0fd65ffe0c8c08 | strength: regulatory
obligated(government_financial_agency, borrower, grant_simple_loans).

% atom_id: 1d3da2ebd694cf51 | chunk: be3606a5f895a687 | strength: statutory
permitted(sindicato, none, organize_federation) :-
    number_of_sindical_entities(X_0), X_0 >= 5,
    representation_percentage(majority).

% atom_id: 5879bb93b9b12192 | chunk: bece49da37bee4e8 | strength: statutory
prohibited(litigant, court_proceeding, raise_exception_outside_of_suspension_grounds).

% atom_id: 7efeb898257f9b92 | chunk: bee95237a43df677 | strength: statutory
obligated(distribuidor, reclamacao, remit_to_junta_or_juizo) :-
    distribution_status(completed).

% atom_id: 32ca301cef07aab1 | chunk: bf3bbf1e402e17cb | strength: statutory
prohibited(individual, none, be_elected_for_administrative_positions).

% atom_id: c54c4a170453f0f8 | chunk: bf3bbf1e402e17cb | strength: statutory
prohibited(individual, none, remain_in_economic_or_professional_representation_positions).

% atom_id: 50721468d2c10a98 | chunk: bf572e07c59ba984 | strength: statutory
obligated(authority, diploma_certificate, register_diplomas_certificates) :-
    document_form(devida),
    firm_recognition(regularmente_reconhecida_por_tabeliao_publico).

% atom_id: 5d9aaabe49748744 | chunk: bf572e07c59ba984 | strength: statutory
obligated(authority, foreign_document, register_foreign_documents) :-
    document_form(devida),
    firm_recognition(regularmente_reconhecida_por_secretaria_estado_relacoes_exte).

% atom_id: cc555d63e20395ee | chunk: bf572e07c59ba984 | strength: statutory
obligated(authority, foreign_document_translation, translate_foreign_documents) :-
    document_type(estrangeiros).

% atom_id: da94c6f6c8f575c5 | chunk: bf572e07c59ba984 | strength: statutory
obligated(authority, foreign_document_translation_interpreter, translate_by_brazilian_commercial_interpreter) :-
    document_type(estrangeiros).

% atom_id: ed9e8641f72a79d1 | chunk: bf93d31d72dba5bd | strength: statutory
obligated(part, document, present_authentic_copies_or_original) :-
    autenticidade(impugnada).

% atom_id: 6e61c37721c4b597 | chunk: bf93d31d72dba5bd | strength: statutory
obligated(serventuario_competente, document, confer_and_certify_conformity) :-
    part_action(present_authentic_copies_or_original).

% atom_id: ddf5d1cb51a8beb5 | chunk: bfde3500efdcf928 | strength: statutory
permitted(deployer, none, fracture_driving_interval) :-
    minimum_break_duration(X_0), X_0 >= 5.

% atom_id: 5945eef0bdc64c65 | chunk: bfe5c173b9bdd9cc | strength: statutory
obligated(worker, none, pay_recurso_de_revista_fee).

% atom_id: 139599d78d70a5b9 | chunk: bfeb1bca54055d77 | strength: statutory
obligated(assembly_general, none, take_secret_ballot) :-
    deliberation_topic(specified_subjects).

% atom_id: e5dcab01227b8ce4 | chunk: c0a17ded39e31a46 | strength: statutory
obligated(employer, child_worker, provide_facilities_to_change_service) :-
    article_reference(art_407).

% atom_id: 410a58e0157a0534 | chunk: c0f42f13296337b3 | strength: statutory
obligated(authority, public, publish_election_call_notice) :-
    time_since_previous_term_end(X_0), X_0 >= 30.

% atom_id: 88ddf16b194857ee | chunk: c13a7cde9a355c32 | strength: statutory
prohibited(employer, worker, annotate_falsely_in_work_card).

% atom_id: 9e77679fbcf050db | chunk: c171864e9ceac297 | strength: statutory
permitted(employer, worker, allow_absence_for_child_healthcare) :-
    child_age(X_0), X_0 <= 6.

% atom_id: d6a9b56470c3bd7a | chunk: c1999e372590b722 | strength: statutory
obligated(employer, worker, calculate_hourly_wage_for_monthly_employee).

% atom_id: 21dbe5041d3cee36 | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, ensure_safety_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: f9a74445f66c9f97 | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, prevent_explosions_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: 7e20fe77742a7a3d | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, prevent_fires_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: d7ea59508cdbc5f0 | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, prevent_collapse_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: 9bc55c182169ce75 | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, prevent_entrapment_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: 582b680dc74d6141 | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, eliminate_dust_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: 6e5293cf124b559e | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, eliminate_gases_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: 904989d5c9c1d25c | chunk: c1d23257689ec19b | strength: statutory
obligated(employer, worker, provide_quick_exit_facilities_in_underground_workplaces) :-
    workplace_type(escavacoes_tuneis_galerias_minas_e_pedreiras).

% atom_id: 80e7f80773098ae6 | chunk: c20fba9f5b4c1e14 | strength: statutory
permitted(litigant, none, file_appeal_by_petition).

% atom_id: 6638b15c97b7c9a1 | chunk: c20fba9f5b4c1e14 | strength: statutory
obligated(court, none, grant_provisional_execution_until_levy).

% atom_id: b2501091518abc3e | chunk: c26717a8f0a28003 | strength: statutory
prohibited(employee, none, exercise_elective_office_concurrently_with_paid_employment_i).

% atom_id: ce27c5a84d606991 | chunk: c2af8d9e423f89ca | strength: statutory
obligated(employer, worker, provide_fire_safety_measures).

% atom_id: 1bef73fdb7a00d36 | chunk: c2d13dab198e405c | strength: statutory
obligated(authority, judgment, execute_final_decision) :-
    recourse_effect(no_suspensive_effect).

% atom_id: 8a27c4e408bd86ca | chunk: c2d13dab198e405c | strength: statutory
obligated(authority, agreement, execute_non_compliance_agreement) :-
    compliance_status(non_compliant).

% atom_id: ca4fc67629478b4e | chunk: c2d13dab198e405c | strength: statutory
obligated(authority, adjustment_of_conduct_term, execute_adjustment_of_conduct_term) :-
    term_origin(labor_public_ministry).

% atom_id: e48f4142a3dac2b8 | chunk: c2d13dab198e405c | strength: statutory
obligated(authority, conciliation_term, execute_conciliation_term) :-
    term_origin(preliminary_conciliation_committee).

% atom_id: b01b197713f7fea5 | chunk: c2d9b66d52d507bd | strength: statutory
obligated(employer, employee, annotate_work_termination_in_labor_card).

% atom_id: 3191fdde75c71ad5 | chunk: c2d9b66d52d507bd | strength: statutory
obligated(employer, competent_authorities, notify_termination_to_competent_authorities).

% atom_id: 558764ace0961bcd | chunk: c2d9b66d52d507bd | strength: statutory
obligated(employer, employee, pay_rescission_benefits_within_specified_period_and_form).

% atom_id: f4bc4d66313b1021 | chunk: c343b4356efb658f | strength: statutory
prohibited(employer, employee, fail_to_make_annotations).

% atom_id: bc12a5f39e4a0d4a | chunk: c36591c967e8816c | strength: statutory
permitted(employer, worker, change_holiday_date).

% atom_id: 69b5cbaf9ccb94a6 | chunk: c42dd5db65b2770d | strength: statutory
obligated(company, none, maintain_specialized_services_safety_and_health_at_work).

% atom_id: 60ff958c37f85922 | chunk: c434c1ba9af61ff6 | strength: statutory
permitted(employer, driver, allow_rest_while_driving) :-
    number_of_drivers(2),
    duration_of_drive(X_1), X_1 <= 72.

% atom_id: 18648e4d85a59ea3 | chunk: c434c1ba9af61ff6 | strength: statutory
obligated(employer, driver, ensure_rest_after_72_hours) :-
    duration_of_drive(n72_hours).

% atom_id: 276abc9adf189a77 | chunk: c434c1ba9af61ff6 | strength: statutory
obligated(employer, driver, ensure_rest_in_external_accommodation_or_stationed_vehicle) :-
    duration_of_drive(n72_hours),
    rest_type(external_accommodation).

% atom_id: 412fc5ed396e1e01 | chunk: c434c1ba9af61ff6 | strength: statutory
obligated(employer, driver, ensure_rest_in_stationed_vehicle_with_bed_equivalent_seat) :-
    duration_of_drive(n72_hours),
    rest_type(stationed_vehicle_with_bed_equivalent_seat).

% atom_id: 12a536cef20a7b5d | chunk: c45981247287b384 | strength: statutory
obligated(employer, worker, compute_half_hour_fractions_as_full_half_hour_if_exceeding_t).

% atom_id: 3aff60234ad5723b | chunk: c4bed3e6b2a53522 | strength: statutory
prohibited(employer, worker, affect_work_contracts).

% atom_id: 68b085e22c0ac87d | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, maintain_hygiene_at_workplace).

% atom_id: e19013e5ee3cb25a | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, provide_separate_bathrooms_by_gender).

% atom_id: ebf1d9b3f037b97b | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, provide_showers_at_workplace).

% atom_id: 53e665f00c77d739 | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, provide_washing_facilities_at_workplace).

% atom_id: 595a39ef1bdaa1b6 | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, provide_separate_lockers_at_workplace).

% atom_id: 8f8436e97ed9528f | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, provide_canteen_or_comfortable_conditions_for_meals).

% atom_id: 1260e53468d33a38 | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, worker, provide_clean_drinking_water_at_workplace).

% atom_id: 93150ce344c528e3 | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, workplace, ensure_cleanliness_of_work_environment).

% atom_id: 76b472c7841c9700 | chunk: c4e5ddaa08c7e29d | strength: statutory
obligated(employer, industrial_waste, treat_industrial_waste_properly).

% atom_id: 56bbc1faeeef6855 | chunk: c5ce367d06e56d82 | strength: statutory
permitted(railway_company, none, employ_extra_staff).

% atom_id: 329a05640ca0c7d7 | chunk: c64a69863a47981d | strength: statutory
prohibited(company, worker, make_unauthorized_annotation_in_work_card).

% atom_id: 7b2e9f26700060a7 | chunk: c666ed62c5321d8f | strength: statutory
obligated(employer, worker, ensure_worker_safety_during_emergency) :-
    emergency_condition(true).

% atom_id: bf9c160c9d9d80ed | chunk: c666ed62c5321d8f | strength: statutory
obligated(employer, worker, ensure_shift_rotation_during_emergency) :-
    emergency_condition(true).

% atom_id: 7b8bf4683aa3a9c2 | chunk: c666ed62c5321d8f | strength: statutory
obligated(employer, worker, provide_rest_period_during_emergency) :-
    emergency_condition(true).

% atom_id: 4283fb54dcee616c | chunk: c666ed62c5321d8f | strength: statutory
obligated(employer, ministry_of_labor, notify_emergency_situation_to_ministry) :-
    emergency_condition(true),
    notification_period(X_1), X_1 <= 10.

% atom_id: ef12c9fc23502d6f | chunk: c730783f9a34fe22 | strength: statutory
permitted(juiz_de_menores, minor, authorize_minor_work) :-
    work_type(a),
    work_type(b).

% atom_id: aa01d82e41687210 | chunk: c7512f1de68be427 | strength: statutory
prohibited(authority, non_state_actors, extend_local_labor_regulations_outside_jurisdiction) :-
    regulation_type(state_legislation),
    regulation_type(collective_labor_agreement),
    regulation_type(individual_labor_agreement),
    regulation_type(judicial_normative_sentence),
    regulation_type(company_regulation).

% atom_id: d9caff5ad1941115 | chunk: c795fa2523c13f80 | strength: statutory
prohibited(employer, worker, maintain_unregistered_employment_relationship).

% atom_id: bfd77c8cbcaab354 | chunk: c838f13a82a81fb3 | strength: statutory
obligated(authority, none, conduct_inquiries_and_proceedings) :-
    request_origin(tribunal).

% atom_id: dc313f484e892052 | chunk: c869a281c28775c0 | strength: statutory
prohibited(employer, worker, prevent_access_to_concours_or_apply_subjective_criteria) :-
    reason(sexo_idade_cor_situacao_familiar_estado_gravidez).

% atom_id: a6504dc08e270f7e | chunk: c8a220355f0a0f34 | strength: statutory
obligated(reclamante, none, attend_hearing_with_witnesses_and_provide_evidence).

% atom_id: 19ea637795e1cb0c | chunk: c8a220355f0a0f34 | strength: statutory
obligated(reclamado, none, attend_hearing_with_witnesses_and_provide_evidence).

% atom_id: a0396b2ac923b611 | chunk: c8b24fa579833a99 | strength: statutory
obligated(employer, worker, provide_periodic_rest_breaks) :-
    work_duration_minutes(90).

% atom_id: 1ad1c64580bfd572 | chunk: c92c7798408c0603 | strength: statutory
prohibited(authority, entity, cede_headquarters_to_political_party_entity).

% atom_id: 64e269dafac587d7 | chunk: c9ee30b5c306cb24 | strength: statutory
prohibited(worker, none, hold_professional_representation_position) :-
    violation_of_labor_rights(true).

% atom_id: 8b7abaaef92bbcd4 | chunk: ca1359b1219151d2 | strength: regulatory
obligated(procurador_geral, procuradorias_regionais, direct_services_of_procurator_general_office).

% atom_id: a1142c9bf7bf5e56 | chunk: ca1359b1219151d2 | strength: regulatory
obligated(procurador_geral, procuradorias_regionais, orient_and_supervise_procurator_regions).

% atom_id: 34f7a1bfa3692670 | chunk: ca1359b1219151d2 | strength: regulatory
permitted(procurador_geral, procuradorias_regionais, issue_necessary_instructions).

% atom_id: a7899598f9a487f3 | chunk: ca333422dcf65101 | strength: statutory
obligated(authority_or_tribunal_superior, justice_authority, apply_sanctions) :-
    type_of_infringement(by_justice_authority).

% atom_id: 276a48187148e411 | chunk: ca333422dcf65101 | strength: statutory
permitted(interested_party_or_procurator, authority_or_tribunal_superior, represent_sanctions) :-
    type_of_infringement(by_justice_authority).

% atom_id: 5ac0b33314514c33 | chunk: ca6422d4b9adc719 | strength: statutory
prohibited(employer, woman_worker, discriminate_in_hiring_or_promotion) :-
    legal_disposition(correction_of_market_access_differences).

% atom_id: ea848fdc7959fa6e | chunk: ca71b344a2411fa5 | strength: statutory
obligated(employer, worker, provide_equal_salary_for_equal_work).

% atom_id: efd9ee26162218ba | chunk: ca9df606c7c79bc9 | strength: statutory
prohibited(state_worker, none, sindicalize).

% atom_id: fa008a2e3feb25e4 | chunk: caaf21212cff74fd | strength: regulatory
obligated(employer, worker, establish_shifts_for_calling_services).

% atom_id: 881a82cb6507b446 | chunk: cab7c6c6e8027d29 | strength: statutory
obligated(president, tribunal_staff, appoint_secretary_from_lottery_employees).

% atom_id: bad8c6b6587271a9 | chunk: cab7c6c6e8027d29 | strength: statutory
obligated(president, tribunal_staff, appoint_supporting_staff_from_lottery_employees).

% atom_id: 04ed96bee074afb9 | chunk: cacc2bd0e361987b | strength: regulatory
obligated(fiscal, institutes_and_entities, conduct_fiscalization) :-
    entity_type(institutos_de_seguro_social_entidades_paraestatais).

% atom_id: ad2bfe20bfa9043f | chunk: cacc2bd0e361987b | strength: regulatory
obligated(minister_of_work_industry_and_commerce, fiscal, issue_instructions_for_fiscalization).

% atom_id: a13b0f827fc286c8 | chunk: cacf9487592ee2c6 | strength: statutory
prohibited(deployer, none, fail_to_satisfy_conditions).

% atom_id: 38d04e797a5b8d40 | chunk: cad11f94b51fee30 | strength: statutory
obligated(employer, worker, compute_as_effective_work_time).

% atom_id: 5cf03d0fdbe19e65 | chunk: cb15f82b0fe1a6f3 | strength: statutory
prohibited(citizen, none, hold_elected_office) :-
    criminal_conviction_type(crime_doloso),
    penalty_effects_persist(true).

% atom_id: 718ad6d7822525de | chunk: cb2bc8a6cc9cffff | strength: statutory
obligated(employer, worker, pay_minimum_wage_in_cash).

% atom_id: a1feea88d236134f | chunk: cba1c2ab8ce254fc | strength: statutory
obligated(authority, chemist, conduct_profession_fiscalization).

% atom_id: 5d0cb1c47880af52 | chunk: cc0d200e1095fcb3 | strength: statutory
prohibited(employer, child_worker, perform_work_in_harmful_conditions).

% atom_id: 60d21e1e203a67f1 | chunk: cc129c6f3359997d | strength: regulatory
obligated(authority, case, distribute_cases_and_designate_reporters).

% atom_id: c41385d9c8d56476 | chunk: cc3eb92ecb4b9f36 | strength: statutory
obligated(servico_estatistica_previdencia_trabalho, none, promote_and_maintain_statistical_studies).

% atom_id: 999368ebef75c562 | chunk: cca880fb4ab074ed | strength: statutory
obligated(court, none, process_and_judge_in_final_instance).

% atom_id: 8155ae91ac8289a4 | chunk: cccf84031eb7c976 | strength: statutory
obligated(employer, worker, ensure_just_and_impartial_treatment) :-
    discrimination_reason(sex_age_religion_political_opinion_union_activity).

% atom_id: 3532549324ea5bb2 | chunk: ccfe4be15cd04ede | strength: statutory
obligated(authority, company, classify_companies_by_employees_and_risk).

% atom_id: 5ecfdc1f6d357629 | chunk: cd144b02c7d45bfe | strength: statutory
obligated(secretaries_of_regional_tribunals, none, perform_attributions_confirmed_in_article_712).

% atom_id: 3c2b39d7530cb8b0 | chunk: cd144b02c7d45bfe | strength: statutory
obligated(secretaries_of_regional_tribunals, none, perform_attributions_fixed_in_internal_rules).

% atom_id: 6deab82022dabd2b | chunk: cd23ac8130a18df0 | strength: statutory
obligated(collective, worker, apply_dispositions_in_title) :-
    nucleus_type(intersindicais_conciliation),
    principles_observed(parity_collective_negotiation).

% atom_id: a419433ace5f3d0b | chunk: cd897fa791df169f | strength: statutory
obligated(employer, worker, provide_rest_interval_between_shifts).

% atom_id: e7d49d8770f1fb8e | chunk: cd9f25b57aaf0425 | strength: statutory
obligated(employee_union, none, fulfill_duty).

% atom_id: 97a60c9d2a324a99 | chunk: cdcaea2bb71cc8b3 | strength: statutory
obligated(procurador_and_functionaries, none, perform_assigned_duties).

% atom_id: 87a47d1586354c82 | chunk: ce3ff0e3507dc1c3 | strength: statutory
prohibited(union_entity, none, exercise_economic_activity).

% atom_id: 69211fb4a0c12699 | chunk: ce4ad5baf58a294e | strength: statutory
prohibited(provider, government_entity, supply_without_certificate_of_settlement).

% atom_id: a61675b40d952471 | chunk: ce4ad5baf58a294e | strength: statutory
prohibited(provider, government_entity, contract_without_certificate_of_settlement).

% atom_id: 303fd6ccf9f6aa2f | chunk: ce4ad5baf58a294e | strength: statutory
prohibited(authority, foreign_company, renew_authorization_without_certificate_of_settlement).

% atom_id: b3f8fde9953b4df6 | chunk: ce5322d4bf238998 | strength: statutory
prohibited(state_entity, none, acquire_financed_vehicles_for_profession) :-
    financer_type(autarquia),
    financer_type(sociedade_de_economia_mista),
    financer_type(agencia_financeira_do_governo).

% atom_id: c3c4c8c0f2625e0b | chunk: ce8b33c5270b3ae1 | strength: regulatory
obligated(sus_manager, none, classify_and_archive_documents).

% atom_id: dddeeac00438da7e | chunk: ceb5462228b68675 | strength: regulatory
obligated(authority, none, issue_norms_for_ionizing_radiations_and_explosives) :-
    type_of_substance(ionizing_radiation_or_explosives).

% atom_id: abf99ccd4a998089 | chunk: cecca967d7b62ef8 | strength: statutory
prohibited(parties, none, appoint_more_than_three_witnesses).

% atom_id: a0ec0f14025b42e0 | chunk: cecca967d7b62ef8 | strength: statutory
permitted(parties, none, appoint_more_than_three_witnesses) :-
    case_type(inquiry).

% atom_id: 184e707b177831df | chunk: cee4643c793a466d | strength: statutory
prohibited(non_state_actors, none, violate_regulations) :-
    nature_of_violation(present_chapter).

% atom_id: 867d6f798834bbbd | chunk: cee4643c793a466d | strength: statutory
prohibited(non_state_actors, none, reincidir_violacao) :-
    previous_offense(true).

% atom_id: 4dc17488dad85b84 | chunk: cee4643c793a466d | strength: statutory
prohibited(non_state_actors, none, oposio_fiscalizao).

% atom_id: caf5bfdc460a8df6 | chunk: cee4643c793a466d | strength: statutory
prohibited(non_state_actors, none, desacato_authority).

% atom_id: 9912c959e31cf7f9 | chunk: cf145c26c8c29b1d | strength: statutory
obligated(secretary_of_board, meeting, secretariat_meetings_and_lavrar_ats).

% atom_id: 3e8e260899400bcc | chunk: cf40601f73d5243e | strength: statutory
obligated(association, candidate, submit_lists_for_vocal_selection).

% atom_id: f6b9e3952ea13d73 | chunk: cf40601f73d5243e | strength: statutory
obligated(president_of_regional_court, list, receive_lists_for_vocal_selection).

% atom_id: d61e1e640ed2ce59 | chunk: cf723a605a28619d | strength: regulatory
obligated(commander_of_the_vessel, ship_records, daily_record_keeping).

% atom_id: fa3f8f20e6afd0b4 | chunk: cf723a605a28619d | strength: regulatory
obligated(ministry_of_labor_industry_and_commerce, ship_records, organize_models).

% atom_id: 3a7c8dad054f6fdf | chunk: cf736f37e4d323d3 | strength: statutory
prohibited(testifier, none, refuse_to_testify_without_justified_reason).

% atom_id: 0957da6993814f69 | chunk: cf909c3d388a4f98 | strength: statutory
obligated(employer, worker, participate_in_company_profits_or_results).

% atom_id: df4be2c3905038b6 | chunk: cfa5b205c944e419 | strength: statutory
obligated(employer, worker, extend_normal_work_duration_underground) :-
    agreement_type(individual_contract).

% atom_id: d8d92c6dc19817d7 | chunk: cfa5b205c944e419 | strength: statutory
obligated(employer, worker, extend_normal_work_duration_underground) :-
    agreement_type(collective_contract).

% atom_id: 3bdf182d85f87234 | chunk: cfa5b205c944e419 | strength: statutory
obligated(authority, employer, grant_license_for_extended_work_duration_underground) :-
    agreement_type(individual_contract),
    agreement_type(collective_contract).

% atom_id: 5f733b47e4652944 | chunk: cfcfc9cd23d5bbea | strength: statutory
obligated(employer, worker, limit_daily_work_hours).

% atom_id: 2e04448a23ad753e | chunk: cfcfc9cd23d5bbea | strength: statutory
permitted(employer, worker, extend_work_hours).

% atom_id: 982e8a446b7cf4b9 | chunk: cfcfc9cd23d5bbea | strength: statutory
permitted(employer, worker, extend_work_hours) :-
    collective_agreement(true).

% atom_id: a2f4e138bfc7eea0 | chunk: cff142c001192e20 | strength: statutory
obligated(tribunal, authority, represent_against_non_compliance).

% atom_id: 83eff3bfa523460a | chunk: d057560e2054d71b | strength: statutory
obligated(judge, tribunal, vote_on_judgments_and_internal_matters).

% atom_id: ee88ae465d1df0a2 | chunk: d075951d8114e780 | strength: statutory
obligated(employer, employee, extend_decision_with_consent) :-
    consent_percentage_employers(n34),
    consent_percentage_employees_or_unions(n34).

% atom_id: db3c2e142ec2f894 | chunk: d07d0468863ff36b | strength: statutory
prohibited(employer, worker, treat_with_excessive_rigor).

% atom_id: 9b061bd10dfaf48b | chunk: d08084c57f672796 | strength: statutory
prohibited(employer, worker, refuse_employment_due_to_sex_age_color_family_status_or_preg) :-
    nature_of_activity(notoriously_and_publicly_incompatible).

% atom_id: 3822354232e76f42 | chunk: d094239a05dc09c5 | strength: statutory
obligated(authority, directoria, approve_directorial_accounts).

% atom_id: 17c05d9d153a4b2f | chunk: d0a33319cbf230f0 | strength: statutory
obligated(state, woman, protect_labor_market_through_incentives).

% atom_id: 88fd176fcf77e649 | chunk: d0ae5bf860b8eaa0 | strength: statutory
permitted(authority, child, prohibit_rest_periods_at_workplace).

% atom_id: 54dd4e57117127db | chunk: d0b3031794373115 | strength: regulatory
obligated(deployer, public, provide_cinema_service_for_five_hours_consecutively_in_cabin).

% atom_id: 7f13bdabbad0012b | chunk: d0d7e915604a5fe3 | strength: statutory
obligated(employer, worker, provide_natural_ventilation).

% atom_id: fd9d84051ce01346 | chunk: d12ddc2cbfed53b4 | strength: statutory
prohibited(chemist, none, exercise_profession_without_registration) :-
    registration_status(unregistered).

% atom_id: 7585a521c19fc5d8 | chunk: d12ddc2cbfed53b4 | strength: statutory
prohibited(chemist, none, exercise_profession_without_registration) :-
    registration_status(unregistered),
    reincidence(true).

% atom_id: eb77c9ffdd89b1b6 | chunk: d1353a3b7abd23b7 | strength: statutory
prohibited(employer, worker, assign_underground_work) :-
    age(none),
    age(none).

% atom_id: b2e8a77f91e9a4a6 | chunk: d1353a3b7abd23b7 | strength: statutory
permitted(employer, worker, assign_underground_work) :-
    age(X_0), X_0 >= 21,
    age(X_1), X_1 <= 50.

% atom_id: 1e454e2011d17fa3 | chunk: d1353a3b7abd23b7 | strength: statutory
obligated(employer, worker, transfer_to_surface_work) :-
    age(X_0), X_0 >= 21,
    age(X_1), X_1 <= 50.

% atom_id: b97781d5bb41c5e0 | chunk: d15641e92dee1fb4 | strength: statutory
permitted(public_official_or_sindicato_representative, authority, report_labor_violations).

% atom_id: d7350044d90afa50 | chunk: d179a5d179639450 | strength: statutory
obligated(authority, firm_or_company, verify_compliance_with_dispositions) :-
    number_of_professionals(X_0), X_0 >= 1,
    professional_role(chemist).

% atom_id: b79b98d1cf4efbc3 | chunk: d179a5d179639450 | strength: statutory
obligated(authority, firm_or_company, conduct_investigations) :-
    number_of_professionals(X_0), X_0 >= 1,
    professional_role(chemist).

% atom_id: 0687688d2002c3d4 | chunk: d179a5d179639450 | strength: statutory
obligated(authority, firm_or_company, examine_documents) :-
    number_of_professionals(X_0), X_0 >= 1,
    professional_role(chemist).

% atom_id: 2727bc16d934e281 | chunk: d1aa0b3416de6fe3 | strength: statutory
obligated(ministry_of_public_works, labour_justice_and_ministry_of_labour, coordinate_through_labor_prosecutors_office).

% atom_id: c943780ed2e32fd5 | chunk: d1b1fa73920b6ae6 | strength: statutory
obligated(association, authority_administrative_or_judicial, represent_interests_of_category_or_profession).

% atom_id: a624d4963e210286 | chunk: d1bf7305eea67878 | strength: statutory
prohibited(employer, apprentice, extend_working_hours).

% atom_id: 3f918e2130727651 | chunk: d1bf7305eea67878 | strength: statutory
prohibited(employer, apprentice, compensate_overtime).

% atom_id: 3d4fba337cfa1765 | chunk: d1c5de4d653ab0e0 | strength: statutory
obligated(employer, worker, pay_rescission_benefits) :-
    contract_type(intermittent),
    termination_reason(art_482_art_483).

% atom_id: 36e46d3368def406 | chunk: d1e83dd7c9558739 | strength: statutory
obligated(deployer, none, be_brazilian).

% atom_id: b74d0fb584236eb3 | chunk: d1f91452d7e394d2 | strength: statutory
obligated(employer, worker, conduct_price_increase_audience) :-
    salary_clause_effect(increase_or_adjustment),
    price_fixation_authority(public_authority).

% atom_id: b484506705b6eddb | chunk: d1f91452d7e394d2 | strength: statutory
obligated(public_authority, employer, express_declaration_on_price_increase) :-
    salary_clause_effect(increase_or_adjustment),
    price_fixation_authority(public_authority).

% atom_id: 10cc2e75ad785bd3 | chunk: d204b30a58c26151 | strength: statutory
obligated(ministry_of_public_works, none, govern_by_clt).

% atom_id: 60b691d8833df1c3 | chunk: d221395e5f801940 | strength: statutory
obligated(procurador, public, execute_procuratorship_duties).

% atom_id: 328d79a49ef22cc2 | chunk: d23ec66995974268 | strength: statutory
obligated(worker, company, collaborate_with_company_on_application_of_chapter_dispositi).

% atom_id: 5ca4b0d576cac450 | chunk: d336b25a8daf3c2b | strength: statutory
prohibited(employee, none, engage_in_dishonest_behavior) :-
    outcome_of_behavior(loss_of_professional_license).

% atom_id: 5001a0d2d618ed07 | chunk: d336b25a8daf3c2b | strength: statutory
obligated(employer, employee, terminate_employment_due_to_loss_of_professional_license) :-
    reason_for_loss_of_license(intentional_behavior).

% atom_id: 221c6e44a081aa2d | chunk: d337be57bc232ad7 | strength: statutory
obligated(judiciary_authority, public, administrate_labor_justice_in_uncovered_areas).

% atom_id: 2839b434551f4121 | chunk: d34e3f76b6a8bd6a | strength: statutory
permitted(chemist, student, teach_specialty_in_university) :-
    satisfies_conditions(art_325_alineas_a_e_b).

% atom_id: 8f2f0e84e58247bf | chunk: d38cc8ece29c0077 | strength: statutory
prohibited(employer, worker, pay_commissions_before_transaction_completion).

% atom_id: 42d2a2cb9a701a84 | chunk: d3c89d1e66d5a4be | strength: regulatory
obligated(authority, worker, extend_collective_dispute_decisions).

% atom_id: 65b7517cf3719f09 | chunk: d3df2365c8184231 | strength: statutory
obligated(employer, worker, treat_branches_as_independent_establishments_for_proportiona) :-
    number_of_employees(X_0), X_0 >= 3.

% atom_id: c865d0446a745461 | chunk: d3f8a7dea856ee77 | strength: statutory
obligated(authority, none, judge_embargoes_of_declaration_opposed_to_acordos).

% atom_id: 70396f2374992bd4 | chunk: d4475a0d9e903b72 | strength: statutory
permitted(parties, none, establish_consecutive_work_hours_agreement) :-
    agreement_type(individual_written_agreement),
    agreement_type(collective_convention),
    agreement_type(collective_agreement).

% atom_id: a4360481ef34883b | chunk: d4475a0d9e903b72 | strength: statutory
obligated(parties, worker, provide_rest_period_after_consecutive_work_hours) :-
    work_hours(12),
    rest_hours(36).

% atom_id: 430ae2d876297595 | chunk: d4475a0d9e903b72 | strength: statutory
obligated(parties, worker, provide_rest_periods_and_meal_breaks) :-
    work_hours(12),
    rest_hours(36).

% atom_id: e710917e7d75f7d6 | chunk: d4475a0d9e903b72 | strength: statutory
obligated(parties, worker, compensate_for_missing_rest_periods_and_meal_breaks) :-
    work_hours(12),
    rest_hours(36).

% atom_id: 78e8545837d64c8c | chunk: d475fde167b5dfa9 | strength: statutory
permitted(judge_substitute, none, act_in_conciliation_and_judgment_juntas) :-
    substituting_president(false).

% atom_id: 2d58d635c5157fb6 | chunk: d4816e155bf6b2a1 | strength: statutory
prohibited(individual, carteira_trabalho_previdencia_social, falsify_work_certificate).

% atom_id: 4761015ccda78c46 | chunk: d4816e155bf6b2a1 | strength: statutory
prohibited(individual, carteira_trabalho_previdencia_social, fabricate_work_certificate).

% atom_id: 27211a7cbc105894 | chunk: d4816e155bf6b2a1 | strength: statutory
prohibited(individual, carteira_trabalho_previdencia_social, alter_work_certificate).

% atom_id: a9b558c35c2b3580 | chunk: d4816e155bf6b2a1 | strength: statutory
prohibited(individual, carteira_trabalho_previdencia_social, sell_altered_work_certificate).

% atom_id: 6589aff5cd2a7258 | chunk: d4816e155bf6b2a1 | strength: statutory
prohibited(individual, carteira_trabalho_previdencia_social, use_altered_work_certificate).

% atom_id: fcda231df56ef59e | chunk: d4816e155bf6b2a1 | strength: statutory
prohibited(individual, carteira_trabalho_previdencia_social, possess_altered_work_certificate).

% atom_id: 8456c2b9b170f5b1 | chunk: d4bf07687cb7a7bc | strength: constitutional
obligated(provider, worker, limit_work_duration).

% atom_id: 822b684c3bd415b9 | chunk: d5049efe670e4029 | strength: statutory
prohibited(infractor, none, exemption_from_criminal_liability).

% atom_id: 77df60e93c48a22f | chunk: d53c4aa197ad627f | strength: regulatory
obligated(department_national_labor, public, publish_registered_chemists_list_periodically).

% atom_id: e81327520aa74f51 | chunk: d53c4aa197ad627f | strength: regulatory
obligated(labor_region_delegations, public, publish_registered_chemists_list_periodically).

% atom_id: 98a157e01f7da986 | chunk: d5914c85f74e7605 | strength: statutory
obligated(employee, employer, request_termination_with_sindicato_assistance) :-
    employment_status(stable).

% atom_id: 020c93488dc07dc7 | chunk: d5914c85f74e7605 | strength: statutory
obligated(employee, local_authority, request_termination_without_sindicato_assistance) :-
    employment_status(stable),
    sindicato_availability(not_available).

% atom_id: e2894cf269afb1bc | chunk: d5914c85f74e7605 | strength: statutory
obligated(local_authority, employee, process_termination_request_without_sindicato_assistance) :-
    employment_status(stable),
    sindicato_availability(not_available).

% atom_id: 36bb323048a529de | chunk: d5c544ff2f27b74d | strength: statutory
obligated(association_or_organization, none, conduct_elections_within_specified_period).

% atom_id: 246d60b5ba72a94d | chunk: d62ca7b2c05400cc | strength: statutory
obligated(employer, worker, pay_salary_with_receipt) :-
    employee_literacy_status(literate).

% atom_id: fbfa8fd67a671a3a | chunk: d62ca7b2c05400cc | strength: statutory
obligated(employer, worker, pay_salary_with_fingerprint) :-
    employee_literacy_status(illiterate),
    fingerprint_possible(true).

% atom_id: bcd523e86ab38431 | chunk: d62ca7b2c05400cc | strength: statutory
obligated(employer, worker, pay_salary_with_signature_or_rogo) :-
    employee_literacy_status(illiterate),
    fingerprint_possible(false).

% atom_id: d21a3b14d4eac2b6 | chunk: d62e5c18ccc33941 | strength: statutory
obligated(tribunal_regional, none, follow_incompatibility_rules).

% atom_id: daf907318762f8e7 | chunk: d68930ebd7e89425 | strength: statutory
obligated(employer, worker, guarantee_service_time_counting).

% atom_id: 85626714b6f8da24 | chunk: d68930ebd7e89425 | strength: statutory
obligated(employer, worker, guarantee_return_to_previous_position).

% atom_id: adde04b9551c03ec | chunk: d6915998643a48f2 | strength: statutory
prohibited(licenciado, none, interrupt_public_or_private_function) :-
    reason_for_interrupt(falta_prevista_no_art_346).

% atom_id: 9c3ff8f7beec20f3 | chunk: d6915998643a48f2 | strength: statutory
permitted(departamento_nacional_do_trabalho, none, cassar_garantias_licenciados) :-
    aprovacao_ministro(true).

% atom_id: 418683bb8d2421b6 | chunk: d6997f81891c8fb6 | strength: statutory
prohibited(minor, none, work_at_night) :-
    age(X_0), X_0 <= 18.

% atom_id: 7dddc3f39884bb60 | chunk: d707ec48d096f35c | strength: statutory
obligated(transport_provider, passenger, observe_transport_regulations).

% atom_id: f986478bddc4c04d | chunk: d71eb79533171805 | strength: regulatory
permitted(employer, employee, authorize_position_in_sindicato) :-
    position_type(cargo),
    organization(sindicato).

% atom_id: d0deeb1242772053 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, provide_continuous_attention_workplace) :-
    work_location(determined_places),
    job_requirements(constant_attention).

% atom_id: 85612e383b0145f9 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_office_workers) :-
    job_role(office_staff).

% atom_id: 4399848970ccc141 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_conservation_teams) :-
    job_role(permanent_track_maintenance).

% atom_id: 5fa03f83c856f63e | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_construction_teams) :-
    job_role(permanent_track_construction).

% atom_id: 5ac7330ff46d6276 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_workshop_workers) :-
    job_role(workshop_staff).

% atom_id: 882ef599115a75e4 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_main_station_workers) :-
    job_role(main_station_staff).

% atom_id: 5135cb862d2c2bb6 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_telegraphists) :-
    job_role(telegraphist).

% atom_id: 982bc30e3cb74c29 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_traction_workers) :-
    job_role(traction_staff).

% atom_id: 5e2c8dd93b4c57bc | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_ballast_workers) :-
    job_role(ballast_staff).

% atom_id: f340f6663a073703 | chunk: d7c4f9caebe88a15 | strength: statutory
obligated(employer, worker, assign_inspectors) :-
    job_role(inspector).

% atom_id: 2434185f40282302 | chunk: d87acb0e279af966 | strength: statutory
permitted(worker, none, file_claim_writing_orally).

% atom_id: 913caf553ff97e4d | chunk: d8c692d9a0b32e5e | strength: statutory
obligated(sesi_sesc_lba, child, maintain_or_subsidize_kindergartens_and_nurseries) :-
    density_of_workers(high).

% atom_id: bf22d5078c647065 | chunk: d909e6a66ac1bf0b | strength: statutory
obligated(president_of_juntas, none, fulfill_duties).

% atom_id: 9658de65a02acb76 | chunk: d928484b2c9e4b9d | strength: regulatory
permitted(secretariat, none, admit_extranumerary_staff).

% atom_id: 56fd3c64f7d6ac06 | chunk: d928484b2c9e4b9d | strength: regulatory
permitted(secretariat, none, dismiss_extranumerary_staff).

% atom_id: c03d02543132da9c | chunk: d928484b2c9e4b9d | strength: regulatory
permitted(secretariat, none, extend_working_hours_with_compensation).

% atom_id: c736da0ebdf9a26f | chunk: d9392c535e130580 | strength: statutory
permitted(worker, none, join_professional_association_or_union).

% atom_id: dd71ba1430e4eed9 | chunk: d9392c535e130580 | strength: statutory
obligated(employer, union_member_worker, grant_preferential_conditions).

% atom_id: af874152ef979e30 | chunk: d94f315d80a42aa0 | strength: statutory
prohibited(employer, worker, commit_harmful_act_to_honor_and_good_reputation).

% atom_id: b154fd0662c7870f | chunk: d9ae23ab4650298c | strength: statutory
obligated(employer, ministry_of_labor_authority, submit_annual_employee_list) :-
    company_type(art_352_1),
    submission_period(n02_05_30_06).

% atom_id: 6692cd8a5fd20360 | chunk: d9f7fed599215686 | strength: statutory
obligated(employer, worker, cease_hazard_pay) :-
    risk_elimination(true).

% atom_id: 28909084641bcc2e | chunk: d9f7fed599215686 | strength: regulatory
obligated(ministry_of_labor, employer, issue_hazard_norms).

% atom_id: 810e2fa80dc7bdcb | chunk: d9ffb8147388cda1 | strength: statutory
obligated(state, worker, establish_minimum_wage).

% atom_id: b5d9397900018863 | chunk: da2ad242561c933b | strength: statutory
obligated(procurador_adjunto_procuradoria_regional, none, perform_duties_of_procurator_region).

% atom_id: 31e950aaa04a0027 | chunk: da9ae2868ea5843c | strength: statutory
obligated(employer, worker, compute_previous_work_periods_on_rehire) :-
    termination_reason(not_grave_foul),
    reception_of_legal_compensation(false),
    voluntary_retirement(false).

% atom_id: e5cb266afd7c3702 | chunk: db52dde6cbc0e22c | strength: statutory
obligated(employer, union_representative, grant_leave_during_international_meeting_participation) :-
    meeting_type(official),
    representative_role(union_representative).

% atom_id: 31447424c197d34c | chunk: db60d015d05505af | strength: statutory
prohibited(employer, worker, establish_contract_terms_contrary_to_collective_agreement).

% atom_id: c40fe8b39831ec70 | chunk: db60d015d05505af | strength: statutory
prohibited(company, worker, establish_contract_terms_contrary_to_collective_agreement).

% atom_id: a4815a93c2028eac | chunk: dc299bf31674680f | strength: statutory
permitted(employee, none, accompany_medical_appointments_and_tests_during_pregnancy) :-
    relationship_status(married_or_cohabiting),
    pregnancy_period(true).

% atom_id: dd7400d876991cbb | chunk: dd912572d6c2f635 | strength: regulatory
obligated(ministry_of_labor, public, issue_instructions_for_minimum_wage_enforcement).

% atom_id: 633131b0d978903b | chunk: dd912572d6c2f635 | strength: regulatory
permitted(ministry_of_labor, organs_within_ministry, delegate_minimum_wage_enforcement).

% atom_id: c148a2971b8d7a72 | chunk: dd912572d6c2f635 | strength: regulatory
permitted(ministry_of_labor, pension_institutes_fiscal_officers, delegate_minimum_wage_enforcement).

% atom_id: 168d2c16e66217ef | chunk: ddc367028f41dd91 | strength: statutory
permitted(professional, none, pay_contribution_to_professional_sindicate) :-
    profession(liberal),
    employment_status(registered_in_company).

% atom_id: 59989f89439b936e | chunk: dddbd8309d3cd281 | strength: statutory
obligated(ministry_of_economy, worker, issue_ctps_preferentially_in_electronic_format).

% atom_id: 4eb774523b222ed7 | chunk: de7d8395adabc697 | strength: statutory
permitted(company, none, celebrate_collective_labor_agreements) :-
    sindical_enquadramento(false).

% atom_id: 9d11af44fbb918d5 | chunk: debb081605bd398d | strength: statutory
obligated(president_of_the_republic, classistas, nominate_classists) :-
    mandate_duration(n3_years),
    representation_type(paritaria).

% atom_id: b68a25b402e21013 | chunk: e01219083c9ec29b | strength: statutory
obligated(judge, none, respect_maximum_limit_honorarios_periciais).

% atom_id: 4bb3bf7310b2d1df | chunk: e023f0cca8be31c5 | strength: statutory
obligated(authority, worker, determine_necessary_changes_in_staffing).

% atom_id: 4096c6f0cb409b4c | chunk: e023f0cca8be31c5 | strength: statutory
obligated(authority, worker, make_official_transfers_between_tribunals).

% atom_id: 7a54c42ee02f9ff5 | chunk: e023f0cca8be31c5 | strength: statutory
obligated(authority, worker, grant_requests_considered_convenient_to_service_respecting_o).

% atom_id: e8b780692ab65f7a | chunk: e06e02ed4a7e9d92 | strength: regulatory
obligated(crew_member, none, be_present_on_post) :-
    reason(maneuvers_or_general_work).

% atom_id: 61f2ec5d02a3ecc1 | chunk: e07e70e7e262fa39 | strength: statutory
obligated(employer, employee, comply_with_judgment_on_readmission_or_reintegration).

% atom_id: ac5ccf49d560e698 | chunk: e0bb3e406636f740 | strength: statutory
obligated(interested_party, none, produce_evidence_of_conflict_existence).

% atom_id: c7039f1710dd959a | chunk: e12ad258f2d82c79 | strength: statutory
obligated(employer, worker, provide_intermittent_or_low_intensity_service) :-
    service_type(intermittent_or_low_intensity).

% atom_id: 7646251431bdf687 | chunk: e12ad258f2d82c79 | strength: statutory
obligated(employer, worker, ensure_prolonged_presence_in_workplaces) :-
    service_type(intermittent_or_low_intensity).

% atom_id: ff98de595f972e44 | chunk: e12ad258f2d82c79 | strength: statutory
obligated(employer, worker, provide_services_at_interior_stations) :-
    work_location(interior_stations).

% atom_id: 1f39ca1e1f774035 | chunk: e12ad258f2d82c79 | strength: statutory
obligated(employer, telegraphist, provide_services_at_interior_stations) :-
    work_location(interior_stations).

% atom_id: 08836358a57c5421 | chunk: e153941dcd39fdaf | strength: statutory
obligated(collective, commission, appoint_supplementary_members).

% atom_id: d0709c8756ad089c | chunk: e1a6bba38c5cb225 | strength: statutory
prohibited(worker, employer, act_injurious_to_honor_or_good_reputation).

% atom_id: f40149eb58665ff1 | chunk: e1a6bba38c5cb225 | strength: statutory
prohibited(worker, employer, physical_offenses).

% atom_id: fb71a6d944420db4 | chunk: e1a6bba38c5cb225 | strength: statutory
permitted(worker, employer, act_injurious_to_honor_or_good_reputation) :-
    circumstance(legitimate_defense).

% atom_id: 182bfdfb8325c21f | chunk: e1a6bba38c5cb225 | strength: statutory
permitted(worker, employer, physical_offenses) :-
    circumstance(legitimate_defense).

% atom_id: cfa6a95df02d32a9 | chunk: e1dc386395eeb80a | strength: statutory
obligated(authority, tribunal_member, grant_posse_and_license_to_tribunal_members).

% atom_id: 68c455d88da24b9d | chunk: e1dc386395eeb80a | strength: statutory
obligated(authority, regional_tribunal_president, grant_leave_and_holiday_to_regional_tribunal_presidents).

% atom_id: d5dbaa048aeb2be1 | chunk: e1e4a1db98aa335b | strength: statutory
obligated(testimony_providers, none, appear_in_hearing).

% atom_id: 955301f36d7606d8 | chunk: e298f225425c2271 | strength: statutory
obligated(tribunal_superior_do_trabalho, self, adapt_regiment_to_consolidation).

% atom_id: 566fe8bd1b9c6f3d | chunk: e36e24219e1c2edc | strength: statutory
obligated(judge_or_president, none, propose_conciliation).

% atom_id: 7e35b00489d8c580 | chunk: e38e05ad4e080327 | strength: statutory
obligated(tribunal, none, be_presided_by_oldest_judge) :-
    president_availability(absent),
    vice_president_availability(absent).

% atom_id: 2ffe3ee651571ef4 | chunk: e38e05ad4e080327 | strength: statutory
obligated(tribunal, none, be_presided_by_most_aged_judge_when_equal_antiquity) :-
    president_availability(absent),
    vice_president_availability(absent),
    judges_antiquity(equal).

% atom_id: e1287d99d957e18b | chunk: e3c96bf20b9b1c65 | strength: statutory
obligated(associado, none, vote_in_sindical_elections).

% atom_id: 2c8e298d2f7901c1 | chunk: e3e6a4e50382ead8 | strength: statutory
obligated(authority, worker, know_last_instance_decisions) :-
    decision_origin(delegado_regional_trabalho),
    matter_type(seguranca_medicina_trabalho).

% atom_id: cedae38a24f4859d | chunk: e3fdefa0849b9fe8 | strength: statutory
obligated(president_of_the_court, parties_or_their_representatives, invite_to_pronounce_on_conciliation_bases).

% atom_id: 264b73ac4de0863f | chunk: e3fdefa0849b9fe8 | strength: statutory
obligated(president_of_the_court, interested_parties, submit_solution_to_resolve_dispute) :-
    bases_proposed(not_accepted).

% atom_id: c8ed0dd3643074f1 | chunk: e3ff870d2222a621 | strength: statutory
obligated(state, association_assets, incorporate_to_state_patrimony) :-
    dissolution_reason(crimes_against_international_personality),
    dissolution_reason(threat_to_state_security),
    dissolution_reason(disruption_of_political_order).

% atom_id: 3032848bd5fc2dd5 | chunk: e3ff870d2222a621 | strength: statutory
obligated(state, association_assets, apply_to_social_assistance_projects) :-
    dissolution_reason(crimes_against_international_personality),
    dissolution_reason(threat_to_state_security),
    dissolution_reason(disruption_of_political_order).

% atom_id: d0df8d76911ef5f0 | chunk: e3ff870d2222a621 | strength: statutory
obligated(association, debts, pay_association_debts) :-
    dissolution_reason(crimes_against_international_personality),
    dissolution_reason(threat_to_state_security),
    dissolution_reason(disruption_of_political_order).

% atom_id: 6588a06f8ebdacd7 | chunk: e400fa30845e0863 | strength: statutory
permitted(tribunal_prolator, none, promote_review).

% atom_id: 344e5a92a3a7b805 | chunk: e400fa30845e0863 | strength: statutory
permitted(procuradoria_justica_trabalho, none, promote_review).

% atom_id: 383d47c076a8b41f | chunk: e400fa30845e0863 | strength: statutory
permitted(associations_sindical, none, promote_review).

% atom_id: 183480bc4e7a42a5 | chunk: e400fa30845e0863 | strength: statutory
permitted(empregador, none, promote_review).

% atom_id: 5f80b6163ac58f6d | chunk: e4277c447486ba5d | strength: statutory
obligated(employer, employee, remit_sindical_tax).

% atom_id: a1c6fffb3e99dd72 | chunk: e4277c447486ba5d | strength: statutory
obligated(employer, government_entity, provide_sindical_tax_proof).

% atom_id: ce18316863cc9509 | chunk: e47a2cc9e5c1d1d6 | strength: statutory
obligated(employer, employee, suspend_employee_functions) :-
    accusation_type(grave_offense).

% atom_id: 33cab6d013db7f49 | chunk: e47a2cc9e5c1d1d6 | strength: statutory
obligated(employer, employee, terminate_employment_contract) :-
    accusation_type(grave_offense),
    inquiry_result(proven).

% atom_id: 45b591daf7fe5ed8 | chunk: e49982172ca45ac1 | strength: statutory
obligated(employer, worker, grant_proportional_vacation_days) :-
    employment_duration_months(X_0), X_0 <=12 12.

% atom_id: be51d25d06d69d05 | chunk: e4a704e1ada2af19 | strength: statutory
obligated(juntas, none, conciliate_instruct_or_judge_with_any_number_of_members) :-
    president_presence(present).

% atom_id: 9fc3679c6902a0c9 | chunk: e4a704e1ada2af19 | strength: statutory
obligated(president_of_juntas, none, prevail_in_vote_in_case_of_tie).

% atom_id: 575398ea2edcc84f | chunk: e4d1ab834bd01411 | strength: statutory
obligated(ministry_of_labor_and_social_security, worker, regulate_electronic_workplace_residence).

% atom_id: 936dde6b620892cb | chunk: e4e4ff61c6174278 | strength: statutory
permitted(president_of_regional_tribunal, none, exercise_privileged_attributions).

% atom_id: 90a11cf28e88cd58 | chunk: e50b4f7d1c0749c4 | strength: statutory
obligated(authority, public, providenciate_material_supplies).

% atom_id: 79ec014158987cf8 | chunk: e5174d26be518614 | strength: statutory
obligated(cartorio_judicial, justica_trabalho, administrate_labor_justice).

% atom_id: 95c87c4878428773 | chunk: e546ecf9dc73fc74 | strength: statutory
obligated(employee, none, provide_services_in_telework_regime).

% atom_id: d54fcba4474fb54c | chunk: e61328492e7b3576 | strength: statutory
obligated(president_and_vice_president_of_labor_region_courts, self, take_office_before_respective_court).

% atom_id: ec03926e378e88c3 | chunk: e62eb6912f630426 | strength: statutory
permitted(employer, worker, extend_normal_work_duration_musicians) :-
    work_hours_per_day(X_0), X_0 <= 8.

% atom_id: b28da39bf83c5100 | chunk: e632668b51fb90d5 | strength: statutory
obligated(ministry_of_labor, none, establish_norms).

% atom_id: 35729313fe26bfe8 | chunk: e65a784c21567edb | strength: statutory
obligated(employer, minor_worker, provide_primary_education) :-
    distance_to_school_km(X_0), X_0 > 2,
    number_of_analfabet_workers(X_1), X_1 >= 30.

% atom_id: c70a7d2a0bf53d41 | chunk: e67189a2c482145d | strength: statutory
obligated(authority, none, designate_substitute_procurator).

% atom_id: 6eada725c291fc9d | chunk: e67189a2c482145d | strength: statutory
obligated(authority, none, appoint_secretary_of_procuratorship).

% atom_id: f8606d3dcfe02547 | chunk: e69e16571b5e721c | strength: statutory
obligated(authority, vocal_supplementaries_of_the_court, convocate_in_case_of_vacancy_or_impediment).

% atom_id: 2b5e2d97310ba38e | chunk: e73ae0ac0fb97473 | strength: regulatory
obligated(employee, none, provide_payment_receipt_with_dates).

% atom_id: 3d06a16f183e6a7c | chunk: e776dea296809cbb | strength: statutory
prohibited(public_official, none, refuse_information).

% atom_id: 5e12ac773ef44823 | chunk: e824a55da140e1fb | strength: statutory
prohibited(collective, none, violate_clt_regulations).

% atom_id: 36ad8ca7f3b415f7 | chunk: e8419a2d129ac79d | strength: statutory
permitted(advocate, document_copy, declare_authenticity).

% atom_id: 508c7e2f721e51f0 | chunk: e84f2e5fb891585c | strength: statutory
obligated(employer, worker, annotate_professional_identification_in_work_card).

% atom_id: 259cc6934b001062 | chunk: e859b44533682a9a | strength: statutory
prohibited(employer, worker, discriminate_work_location).

% atom_id: 147149a5b09096ed | chunk: e86f639361d6e6d0 | strength: statutory
obligated(authority, none, execute_decisions) :-
    decision_origin(self).

% atom_id: d26f45507583572e | chunk: e86f639361d6e6d0 | strength: statutory
obligated(authority, none, execute_decisions) :-
    decision_origin(junta).

% atom_id: 19904da202d29f95 | chunk: e86f639361d6e6d0 | strength: statutory
obligated(authority, none, execute_decisions) :-
    decision_origin(delegated).

% atom_id: a2330855adb392fa | chunk: e8b514cf3a3627e6 | strength: statutory
obligated(sus_manager, public, maintain_public_and_private_good_conduct).

% atom_id: d00d368d5344f182 | chunk: e8f2d7f839996133 | strength: statutory
prohibited(worker, none, be_subject_to_articles_above).

% atom_id: f82ba7911b5eeeeb | chunk: e908e14a67ad9062 | strength: statutory
obligated(employer, worker, pay_salaries_punctually).

% atom_id: d68383887b95357e | chunk: e919d09c1b8e6ab3 | strength: statutory
permitted(employer, worker, grant_individual_unmotivated_dismissals).

% atom_id: ed8153c68a86a4b4 | chunk: e97294e5d4a8a0ac | strength: statutory
obligated(union_entities, public, publish_tax_call_editais) :-
    days_before_deposit(X_0), X_0 <= 10,
    publication_duration(3).

% atom_id: 225e88c83b6affda | chunk: e9aedac00275e789 | strength: regulatory
obligated(authority, worker, resume_work_after_inquiry_or_preventive_arrest) :-
    inquiry_outcome(impronounced),
    arrest_type(preventive).

% atom_id: d91e3594953cc0ab | chunk: e9c7a5039ae2a8d1 | strength: statutory
prohibited(employee_representative, none, run_for_election_in_subsequent_terms).

% atom_id: bb8f92e6772c89bb | chunk: e9c89f3ad246270e | strength: statutory
prohibited(employer, worker, remunerate_extraordinary_hours_below_minimum).

% atom_id: 8f76f795db0506d8 | chunk: e9e9a8683555d37c | strength: regulatory
obligated(sindicate_administration, none, constitute_directorate).

% atom_id: 2aeaca1903001516 | chunk: e9e9a8683555d37c | strength: regulatory
obligated(sindicate_administration, none, constitute_financial_advisory_board).

% atom_id: dd90ba24fb5c370a | chunk: e9ffc7fbee4da1a9 | strength: statutory
obligated(authority, none, constitute_procuradoria_geral).

% atom_id: ac50f615b73c4db3 | chunk: ea0ea98499ec297a | strength: statutory
obligated(public_repartition, labor_judges_and_tribunals, provide_information_for_labor_cases).

% atom_id: 7856f73ec721ae21 | chunk: ea0ea98499ec297a | strength: statutory
obligated(trade_unions_associations, labor_judges_and_tribunals, provide_information_for_labor_cases).

% atom_id: eb9506a948d9a53b | chunk: ea0ea98499ec297a | strength: statutory
obligated(public_repartition, labor_procuratorship, provide_information_for_labor_cases).

% atom_id: 6150473d76bed378 | chunk: ea0ea98499ec297a | strength: statutory
obligated(trade_unions_associations, labor_procuratorship, provide_information_for_labor_cases).

% atom_id: b9556b12abf56ced | chunk: ea9b0fa199df4442 | strength: statutory
obligated(employer, worker, pay_pecuniary_effects_of_hazardous_work) :-
    work_condition(insalubridade),
    work_condition(periculosidade).

% atom_id: ede5c847dcb316f1 | chunk: ea9b0fa199df4442 | strength: statutory
obligated(ministry_of_labor, employer, approve_hazardous_work_inclusion).

% atom_id: a8c9577b49d22083 | chunk: ea9b58f0301cfb40 | strength: regulatory
obligated(authority, public, form_separate_files_for_parties).

% atom_id: 7e46bc0423f1c78f | chunk: ea9b58f0301cfb40 | strength: regulatory
permitted(authority, interested_party, consult_separate_files_data).

% atom_id: e70681baa850d388 | chunk: ead5b6ab62e12a1d | strength: statutory
obligated(collective, category_or_profession, elect_or_designate_representatives).

% atom_id: bac4fa9262f7a2ca | chunk: ead98d180f2e4d25 | strength: statutory
obligated(authority, child_worker, order_to_abandon_work) :-
    work_environment(harmful).

% atom_id: 6fd8cbefc3956a55 | chunk: ead98d180f2e4d25 | strength: statutory
obligated(employer, child_worker, provide_facilities_to_change_functions) :-
    work_environment(harmful),
    authority_decision(order_to_abandon_work).

% atom_id: eb567a810ccc9871 | chunk: eae7a45404375273 | strength: statutory
permitted(procurador, none, receive_percentage_for_collection) :-
    debt_type(ativa_uniao),
    penalty_source(administrative_authority_or_judiciary_work_and_social_securi).

% atom_id: 6ef8cf0071f6ae62 | chunk: eb08b7164d45846d | strength: statutory
obligated(authority, worker, review_work_conditions_decisions) :-
    time_since_decision(X_0), X_0 >= 1,
    circumstances_change(true).

% atom_id: 517095c2b9a91cd0 | chunk: eb2ad71ec101e000 | strength: statutory
obligated(capitania_do_porto, tripulante_maritimoo, annotate_vacations_in_registration_card).

% atom_id: 784a835c1110e8e6 | chunk: eb60d681506a1297 | strength: statutory
obligated(sindicato_convenente_empresa_acordante, none, deposit_agreement_for_registration) :-
    days_since_signature(X_0), X_0 <= 8.

% atom_id: c5cb4bbd6892ef8c | chunk: eba39fb4880b077b | strength: statutory
prohibited(employer, chemist, hire_foreign_chemists_above_threshold) :-
    foreign_chemists_ratio(X_0), X_0 > 1.

% atom_id: 67f4991c4d3afe50 | chunk: ebacf6580caf7694 | strength: statutory
obligated(employer, worker, grant_leave_of_absence) :-
    event(spouse_death).

% atom_id: ac69af39aaa4b63f | chunk: ebacf6580caf7694 | strength: statutory
obligated(employer, worker, grant_leave_of_absence) :-
    event(ascendant_death).

% atom_id: 8115bef132ade1a1 | chunk: ebacf6580caf7694 | strength: statutory
obligated(employer, worker, grant_leave_of_absence) :-
    event(descendant_death).

% atom_id: 1759fb0c0e09b37a | chunk: ebacf6580caf7694 | strength: statutory
obligated(employer, worker, grant_leave_of_absence) :-
    event(sibling_death).

% atom_id: 05bb404bd44d9cdb | chunk: ebacf6580caf7694 | strength: statutory
obligated(employer, worker, grant_leave_of_absence) :-
    event(dependent_person_death).

% atom_id: 5a1f208bf43f2799 | chunk: ebb62afcb2412eec | strength: statutory
obligated(establishment_of_education, teacher, remunerate_excess_classes) :-
    number_of_extra_classes(X_0), X_0 > 0.

% atom_id: c81b49e1fc38b197 | chunk: ebc6baa98313364c | strength: statutory
prohibited(worker, none, lift_above_60kg_unassisted).

% atom_id: dcc671211a98b2cb | chunk: ebd89c8d22f3970b | strength: statutory
obligated(employer, worker, instruct_precautions_to_avoid_work_accidents_or_occupational).

% atom_id: 5a1afa75d8249302 | chunk: ebe58390df102ba3 | strength: statutory
obligated(authority, jurisdiction_of_labor_justice_organs, defend_jurisdiction).

% atom_id: 07f04b5e742e9f5e | chunk: ebe72c85f7b8830e | strength: statutory
obligated(authority, case, distribute_cases_by_order_of_entry).

% atom_id: c0de97a9ffe22159 | chunk: ec3b87554cccd535 | strength: statutory
obligated(authority, none, apply_fines) :-
    location(distrito_federal).

% atom_id: b027f9b0ed5f58a2 | chunk: ec3b87554cccd535 | strength: statutory
obligated(authority, none, apply_fines) :-
    location(estados).

% atom_id: dad45ee8131fced1 | chunk: ec3b87554cccd535 | strength: statutory
obligated(authority, none, apply_fines) :-
    location(territorio_do_acre).

% atom_id: c835ec94071f8fe6 | chunk: ec53a3da5eced2b0 | strength: regulatory
permitted(authority, none, impose_penalties).

% atom_id: 304028285b870ad2 | chunk: ec7c7e87ef880d60 | strength: statutory
prohibited(employer, worker, exceed_normal_work_duration).

% atom_id: 281c73cb5f2787ab | chunk: ecb3bc0273ef3ce6 | strength: statutory
prohibited(authority, employer, grant_registration_or_license_without_sindicato_tax_proof).

% atom_id: 5c37eead0a10454f | chunk: eccebf6f173cbb80 | strength: statutory
obligated(authority, none, record_consciousness_in_acordao).

% atom_id: ac90f8b03b30151c | chunk: ece8bfd863f3e211 | strength: statutory
prohibited(collective, none, act_to_violate_clt).

% atom_id: 27bc6cedf6bc0559 | chunk: ecf35ef5ae72c953 | strength: statutory
obligated(authority, none, recourse_of_official_matter) :-
    decision_type(arquivamento),
    law_category(protecao_trabalho).

% atom_id: 6fd56c1869d5b78d | chunk: ed073739ade435d9 | strength: statutory
obligated(employer, worker, maintain_chemical_control_lab).

% atom_id: 4c7bf0959934d3e2 | chunk: ed72df506697ae00 | strength: statutory
obligated(worker, union, pay_union_contribution) :-
    participation_status(member_of_represented_category).

% atom_id: d8de08a7d6daa2d0 | chunk: ed72df506697ae00 | strength: statutory
obligated(union, worker, collect_union_contribution) :-
    participation_status(member_of_represented_category).

% atom_id: 003d545081619228 | chunk: eea8d20bdc22120c | strength: regulatory
obligated(deployer, public, perform_diligences_and_procedural_acts_ordered_by_trt_or_tst).

% atom_id: 93c0d920bf3ddc94 | chunk: eec051f69f971d91 | strength: statutory
obligated(judge_or_court, none, apply_penalties) :-
    disobedience(true),
    violation(true),
    refusal(true),
    omission(true),
    coercion(true).

% atom_id: 73793ff41ad6e5fa | chunk: eec051f69f971d91 | strength: statutory
obligated(judge_or_court, none, initiate_proceedings_ex_officio) :-
    disobedience(true),
    violation(true),
    refusal(true),
    omission(true),
    coercion(true).

% atom_id: b8f7899ab537fd21 | chunk: eec051f69f971d91 | strength: statutory
obligated(judge_or_court, none, initiate_proceedings_upon_representation) :-
    disobedience(true),
    violation(true),
    refusal(true),
    omission(true),
    coercion(true).

% atom_id: 8b46eb75acaf5d12 | chunk: eec051f69f971d91 | strength: statutory
obligated(judge_or_court, none, initiate_proceedings_upon_representation) :-
    representation_source(procuradoria_justica_trabalho).

% atom_id: 0c591ef91c70d9e0 | chunk: eecdb3b9ba0bdce5 | strength: statutory
obligated(ministry_of_labor, cipa, regulate_cipa_attributes_and_functioning).

% atom_id: a35798bbbdf50da8 | chunk: eed36c29127206fb | strength: regulatory
obligated(procurador_geral_staff, none, perform_assigned_tasks_by_procurator_general).

% atom_id: eb1ff156be311c5b | chunk: ef3ff0968da20026 | strength: statutory
obligated(participant, sindicato, pay_contribution) :-
    authorization(express).

% atom_id: dbfcc7ebd104a3d0 | chunk: ef3ff0968da20026 | strength: statutory
obligated(sindicato, contribution, collect_and_apply_contribution) :-
    authorization(express).

% atom_id: e89937efbff77c65 | chunk: ef7070c1872884dc | strength: statutory
obligated(applicant, none, specify_request_value).

% atom_id: 7efcc7f1ffba4f3c | chunk: efc5c2497dd06b01 | strength: statutory
obligated(tribunal_regional, none, establish_session_order).

% atom_id: ce0d777a9b17cfe5 | chunk: efc6552d1024c4f0 | strength: statutory
obligated(sus_manager, competent_authorities, request_necessary_inquiries).

% atom_id: 4107deb75e69bf30 | chunk: f0a5a530420dee9e | strength: statutory
prohibited(litigant, none, raise_defense_matters).

% atom_id: c2c716adb59b245a | chunk: f0b1daa60b12e560 | strength: statutory
obligated(judicial_officials, none, adhere_to_title_xi_of_criminal_code).

% atom_id: 7b348eafbdf1aee7 | chunk: f0e91db18da784f9 | strength: statutory
obligated(tribunal, process, function_with_full_composition_or_divided_into_chambers) :-
    parity_representation(true).

% atom_id: a2525abc7675ec7f | chunk: f0f1127ad72424b2 | strength: statutory
obligated(authority, reclamant, conduct_investigation_for_case_instruction).

% atom_id: 55457463eb04a265 | chunk: f0f1127ad72424b2 | strength: statutory
obligated(authority, reclamado, notify_by_registered_letter).

% atom_id: 7032463ee601770d | chunk: f0f1127ad72424b2 | strength: statutory
obligated(reclamado, authority, appear_to_provide_explanations_or_make_records_in_work_card) :-
    recusa_persistente(true).

% atom_id: ec733f9e736f2e8c | chunk: f15dd762c674c336 | strength: statutory
prohibited(individual, none, exercise_chemistry_without_registration).

% atom_id: e147204f1ef12a96 | chunk: f1730d7af99b1322 | strength: statutory
obligated(sus_manager, none, perform_additional_duties_assigned_by_procurator).

% atom_id: 9b42790daaa11980 | chunk: f1a312cb794833b0 | strength: statutory
obligated(state, elected_official, provide_free_office_for_elected_positions).

% atom_id: fd2cbe76f6b5e594 | chunk: f1a4661b8fb34674 | strength: statutory
permitted(tribunal, none, request_session_extension) :-
    necessity_of_measure(true).

% atom_id: fe2b3fbeba581b0d | chunk: f1a9baa54af10ffc | strength: statutory
obligated(employer, worker, ensure_just_salaries).

% atom_id: 2e8257665de51e10 | chunk: f1a9baa54af10ffc | strength: statutory
obligated(employer, company, ensure_just_company_retribution).

% atom_id: 34af829a73fe2f15 | chunk: f1c29beedfe8eced | strength: statutory
prohibited(worker, none, work_on_holidays) :-
    holiday_type(national_or_religious).

% atom_id: 3d1fe22b9821140a | chunk: f1c54b07ff58b26c | strength: statutory
prohibited(company, brasilian_worker, pay_lower_salary_than_foreign_worker) :-
    judgment_by_ministry_of_work_industry_and_commerce(function_analogous_to_foreign_worker).

% atom_id: 037537f457a56da3 | chunk: f1c65a8923177bf4 | strength: statutory
obligated(employer, worker, consider_excess_hours_as_overtime) :-
    hours_worked(X_0), X_0 > 8.

% atom_id: d7944b4a2ba6f9f2 | chunk: f1c65a8923177bf4 | strength: statutory
obligated(employer, worker, compensate_overtime_work) :-
    hours_worked(X_0), X_0 > 8.

% atom_id: 29df79078078804b | chunk: f1e3c3c3c7e7ceab | strength: statutory
obligated(government, worker, pay_indemnization) :-
    work_stop_reason(authority_municipal_state_federal_order),
    work_stop_reason(legislation_impossibility).

% atom_id: 9601feb189be7b4a | chunk: f1f9457fe95b85bd | strength: regulatory
obligated(sus_manager, procurador_geral, submit_semiannual_report).

% atom_id: 5895874263c5b6a5 | chunk: f202e782e4f4081f | strength: statutory
obligated(authority, employer, promote_instruction_on_labor_laws) :-
    visit_type(double_visit).

% atom_id: f2829bbec0709226 | chunk: f202e782e4f4081f | strength: statutory
obligated(authority, employer, conduct_double_visits) :-
    visit_type(double_visit).

% atom_id: 720f87ccc024c899 | chunk: f23e77e446c45a20 | strength: statutory
prohibited(employer, child_worker, extend_normal_daily_work_duration).

% atom_id: 261af8db6ce1ee75 | chunk: f2869142e1f06cd3 | strength: statutory
obligated(employer, employee, offer_training_courses).

% atom_id: 1a68d9a2964882a5 | chunk: f2b12074605cb6b5 | strength: statutory
obligated(employer, worker, provide_minimum_rest_period).

% atom_id: ebe30f42d42e735d | chunk: f2ee2227beb1f82d | strength: statutory
obligated(authority, professional, suspend_professional_practice) :-
    debt_status(unpaid).

% atom_id: 016dc1c05b5f90d3 | chunk: f2ee2227beb1f82d | strength: statutory
obligated(authority, professional_disciplinary_body, apply_sanction) :-
    communication_source(fiscal_authority).

% atom_id: 9c912dcd4bf17813 | chunk: f442ef44971bc231 | strength: statutory
permitted(tribunal, employer, extend_new_work_conditions_to_all_employees_in_same_professi) :-
    jurisdiction_of_the_tribunal(same_professional_category).

% atom_id: f8a203dd9b897fc3 | chunk: f4c0f8b528fbedbc | strength: statutory
obligated(authority, inscribed_person, provide_work_and_social_security_card).

% atom_id: 47ab48d4671ab5a9 | chunk: f4d9e91516cb1932 | strength: statutory
obligated(employer, authority_regional_trabalho_ministerio_trabalho_industria_co, immediate_report_hazardous_event_subsoil_works) :-
    event_type(compromising_life_health).

% atom_id: 0c4a840b607ffd58 | chunk: f4eb94e4c7a7b2e5 | strength: statutory
obligated(employer, worker, provide_personal_protection_equipment_free_of_charge).

% atom_id: 98e50fc3d5bc44a8 | chunk: f4fceb41760439b5 | strength: statutory
permitted(sus_manager, none, provide_opinion_during_session).

% atom_id: f73ae6dbe74f4f5a | chunk: f4fceb41760439b5 | strength: statutory
permitted(sus_manager, none, request_requisitions_and_inquiries).

% atom_id: 5286842512961486 | chunk: f4fceb41760439b5 | strength: statutory
permitted(sus_manager, none, view_process_when_new_issue_arises) :-
    new_question_raised(true).

% atom_id: e8084180eed18754 | chunk: f4ffa5bc036b0441 | strength: statutory
prohibited(professor, none, conduct_classes_on_sundays).

% atom_id: c2310e16811354a6 | chunk: f4ffa5bc036b0441 | strength: statutory
prohibited(professor, none, work_on_exams_on_sundays).

% atom_id: 2e6da8fdb70850f1 | chunk: f51d7c89f071e3e9 | strength: statutory
obligated(employer, worker, protect_from_hazardous_substances) :-
    substance_type(hazardous_chemicals),
    radiation_type(ionizing_or_non_ionizing),
    environmental_factor(noise_vibration_pressure).

% atom_id: 67ab4b99811efa0c | chunk: f51d7c89f071e3e9 | strength: statutory
obligated(employer, workplace, specify_measures_to_eliminate_or_attenuate_hazards) :-
    hazard_type(chemical_radiation_noise_vibration_pressure).

% atom_id: bf0b7aa2da23063e | chunk: f51d7c89f071e3e9 | strength: statutory
obligated(employer, worker, set_maximum_exposure_limits) :-
    exposure_type(time_intensity_effect_on_organism).

% atom_id: 4e92c57424660e7c | chunk: f51d7c89f071e3e9 | strength: statutory
obligated(employer, worker, conduct_mandatory_medical_examinations).

% atom_id: f8902e30dc30938d | chunk: f51d7c89f071e3e9 | strength: statutory
obligated(employer, workplace, control_age_limits).

% atom_id: 863be800d525f28e | chunk: f51d7c89f071e3e9 | strength: statutory
obligated(employer, workplace, continuously_monitor_workplaces).

% atom_id: 73e633ff27bdf5af | chunk: f52b569be9198356 | strength: statutory
obligated(employer, worker, provide_free_personal_protection_equipment) :-
    general_measures_effectiveness(incomplete).

% atom_id: ab3cd03747d2b253 | chunk: f54eae5afdb48b74 | strength: statutory
permitted(sindicalized_company, public_authority, participate_in_public_contracts) :-
    equality_of_conditions(true).

% atom_id: 3a4b70a7a5aa63dc | chunk: f57622c6546e2ed3 | strength: statutory
obligated(authority, litigant, file_appeal_within_ten_days) :-
    days_since_notification_received(X_0), X_0 <=10 10.

% atom_id: cb7eb0750bc47e71 | chunk: f57622c6546e2ed3 | strength: statutory
obligated(authority, higher_authority, forward_appeal_to_superior_authority) :-
    appeal_received(true).

% atom_id: abab50d1e02ac93a | chunk: f57c9baac16e75f1 | strength: statutory
obligated(employer, worker, reimburse_difference_within_two_years) :-
    payment_date(date_of_payment).

% atom_id: 70e22b09fa36f9d2 | chunk: f58a8d4dc9132d85 | strength: statutory
prohibited(employer, worker, prevail_contractual_disposition_violating_collective_agreeme).

% atom_id: 243e2cb11a815dbe | chunk: f5a91daea61cc3d4 | strength: statutory
prohibited(testemunha, none, take_oath) :-
    relationship_type(relative),
    relationship_degree(X_1), X_1 <= 3.

% atom_id: ac61e0eb6d0e1949 | chunk: f5a91daea61cc3d4 | strength: statutory
prohibited(testemunha, none, take_oath) :-
    relationship_type(close_friend).

% atom_id: 7880167864e8b411 | chunk: f5a91daea61cc3d4 | strength: statutory
prohibited(testemunha, none, take_oath) :-
    relationship_type(enemy).

% atom_id: cfec58756ee1c744 | chunk: f5a91daea61cc3d4 | strength: statutory
obligated(court, testemunha, accept_unsworn_testimony) :-
    relationship_type(relative),
    relationship_degree(X_1), X_1 <= 3.

% atom_id: 9e040fdab2429855 | chunk: f5a91daea61cc3d4 | strength: statutory
obligated(court, testemunha, accept_unsworn_testimony) :-
    relationship_type(close_friend).

% atom_id: 5eb49bb05eb5c707 | chunk: f5a91daea61cc3d4 | strength: statutory
obligated(court, testemunha, accept_unsworn_testimony) :-
    relationship_type(enemy).

% atom_id: 51cfe0439ca3c0cf | chunk: f5a91daea61cc3d4 | strength: statutory
obligated(court, testemunha, treat_as_information) :-
    relationship_type(relative),
    relationship_degree(X_1), X_1 <= 3.

% atom_id: 40ff2efe37b5cc87 | chunk: f5a91daea61cc3d4 | strength: statutory
obligated(court, testemunha, treat_as_information) :-
    relationship_type(close_friend).

% atom_id: d4eab5b73680eb09 | chunk: f5a91daea61cc3d4 | strength: statutory
obligated(court, testemunha, treat_as_information) :-
    relationship_type(enemy).

% atom_id: 4ec04f9af8200b05 | chunk: f5e03f36a29dcb18 | strength: statutory
obligated(authority, public, execute_payment_installments_with_observation_of_rules).

% atom_id: b17db5d2151942f0 | chunk: f5f3ae3bddad4ab0 | strength: statutory
obligated(employer, child_worker, ensure_technical_professional_training) :-
    age(X_0), X_0 >= 14,
    age(X_1), X_1 < 24.

% atom_id: a54a266557ea7e4d | chunk: f5f3ae3bddad4ab0 | strength: statutory
obligated(child_worker, employer, execute_tasks_with_diligence) :-
    age(X_0), X_0 >= 14,
    age(X_1), X_1 < 24.

% atom_id: 836bf7d58838b546 | chunk: f5fab0b7f1e3c841 | strength: statutory
obligated(procurador_geral_do_trabalho, none, lead_procuradoria_geral_do_trabalho).

% atom_id: e86f895dd2df91b2 | chunk: f6038f0e391889fd | strength: statutory
obligated(employer, child_worker, issue_work_card) :-
    age(X_0), X_0 < 18.

% atom_id: d82114b39ef026d7 | chunk: f6409683c99a2e98 | strength: statutory
prohibited(provider, teacher, operate_school_without_condign_payment).

% atom_id: 83288e45cf7bf5f0 | chunk: f66f1f1fd1863878 | strength: statutory
obligated(authority, infractor, forward_criminal_evidence_to_authority) :-
    penalty_type(criminal).

% atom_id: d0e1186b00e356dd | chunk: f6aee419fb6526d7 | strength: statutory
permitted(employer, worker, pact_clause_of_arbitration) :-
    salary(two_times_rbgps_limit).

% atom_id: 4eceb8c6694e4df3 | chunk: f6aee419fb6526d7 | strength: statutory
permitted(worker, employer, initiate_clause_of_arbitration) :-
    salary(two_times_rbgps_limit).

% atom_id: b72a9339aaf2af53 | chunk: f6c636c64ac85531 | strength: regulatory
permitted(employer, none, request_something_from_authority) :-
    number_of_employers(X_0), X_0 >= 1.

% atom_id: db2ae5470195de74 | chunk: f6c636c64ac85531 | strength: regulatory
permitted(union, none, request_something_from_authority).

% atom_id: 0b1e6d800b19da45 | chunk: f7060a399d94ebba | strength: statutory
obligated(employer, worker, apply_dispositions_to_workers_in_media_companies) :-
    job_role(jornalista_revisor_fotografo_ilustrador).

% atom_id: 4c8e498acc17bb0b | chunk: f713d9d3c559a7b3 | strength: statutory
obligated(confederations, none, organize_with_minimum_federations) :-
    number_of_federations(X_0), X_0 >= 3.

% atom_id: 6eefff0711e97f1e | chunk: f713d9d3c559a7b3 | strength: statutory
obligated(confederations, none, establish_headquarters_in_capital).

% atom_id: 3a1386f0a4503eb4 | chunk: f71702064d8218cc | strength: statutory
obligated(employer, worker, provide_weekly_rest_period) :-
    trip_duration_days(X_0), X_0 > 7.

% atom_id: abee7b3dd4b462f4 | chunk: f71702064d8218cc | strength: statutory
obligated(employer, worker, offer_accommodation_for_rest_period) :-
    trip_duration_days(X_0), X_0 > 7.

% atom_id: 9b0d25ff64a9dc50 | chunk: f71702064d8218cc | strength: statutory
obligated(employer, worker, provide_daily_rest_interval) :-
    trip_duration_days(X_0), X_0 > 7.

% atom_id: 933292b02f2edc59 | chunk: f71702064d8218cc | strength: statutory
permitted(employer, worker, allow_rest_period_at_home_or_base) :-
    trip_duration_days(X_0), X_0 > 7,
    company_conditions(inadequate).

% atom_id: f6c6759de1201d4d | chunk: f71702064d8218cc | strength: statutory
obligated(employer, worker, ensure_total_rest_period_of_35_hours) :-
    trip_duration_days(X_0), X_0 > 7.

% atom_id: 9a93d0fa6c2f78fa | chunk: f74616254a99f735 | strength: statutory
obligated(employer, employee, deduct_sindical_contribution) :-
    work_status(not_working),
    authorization(given_explicitly_prior_to_deduction).

% atom_id: 20935ac6d43e6043 | chunk: f786e7a567188d8e | strength: statutory
obligated(employer, tripulant, record_overtime_hours).

% atom_id: a4d8cfac3c4ed9b5 | chunk: f786e7a567188d8e | strength: statutory
obligated(employer, tripulant, document_violations).

% atom_id: f8faf4488fe3e3a8 | chunk: f7f9eec6a079ea11 | strength: statutory
obligated(procurador, servico_procuradoria, direct_services).

% atom_id: 80e93b8bbb3abdcf | chunk: f85649ece7302b5f | strength: statutory
obligated(authority, sus_manager, judge_suspicions_levied_against_members).

% atom_id: 1b5867eb9fa89b18 | chunk: f857c248a0e45e77 | strength: regulatory
obligated(tribunal_president, tribunal_session, preside_sessions).

% atom_id: cc33b8f823243b88 | chunk: f857c248a0e45e77 | strength: regulatory
obligated(tribunal_president, ordinary_session, schedule_sessions).

% atom_id: 1807c41027106477 | chunk: f857c248a0e45e77 | strength: regulatory
obligated(tribunal_president, extraordinary_session, call_sessions).

% atom_id: 89e03064248404e1 | chunk: f94616d866467d22 | strength: statutory
obligated(requerente, none, support_emoluments).

% atom_id: 8ed6384cc6faa395 | chunk: f9a2006181ee75e2 | strength: statutory
permitted(worker, fgts_account, withdraw_funds_from_fgts) :-
    contract_termination_reason(extinction_clause).

% atom_id: 65a5fadaadd99d4c | chunk: f9aafd0430d8d858 | strength: statutory
permitted(collective, none, constitute_superior_sindicale_associations).

% atom_id: 891f09a684b4ed67 | chunk: f9c52109af352a5a | strength: statutory
obligated(worker, none, be_sindicalized_for_representation) :-
    activity_type(economic).

% atom_id: 21b3e508e95ba5b2 | chunk: f9c52109af352a5a | strength: statutory
prohibited(worker, none, enjoy_tax_benefits_without_sindicalization) :-
    activity_type(economic).

% atom_id: 4873303013d1d609 | chunk: f9c52109af352a5a | strength: statutory
permitted(worker, none, enjoy_tax_benefits_without_sindicalization) :-
    activity_type(non_economic).

% atom_id: 18f187f220d4af4f | chunk: fa112c14e120b64f | strength: statutory
obligated(employer, worker, pay_overtime_with_25_percent_increase) :-
    work_duration_exceeds_six_hours(true).

% atom_id: 81bc41abd7f26c1f | chunk: fa9a27a67b7ccce2 | strength: statutory
obligated(tribunal_turma_judge, none, deliberate_with_minimum_quorum) :-
    number_of_present_judges(X_0), X_0 >= 3.

% atom_id: 43ea9d2a9aa76b06 | chunk: fa9a27a67b7ccce2 | strength: statutory
obligated(tribunal_turma_president, none, function_as_revisor_or_relator) :-
    case_distribution(internal_regulation).

% atom_id: a6224cd9559d3dcc | chunk: fa9bec28969e44cd | strength: statutory
obligated(authority, none, preside_conciliation_hearings_in_collective_disputes).

% atom_id: 71797265cb3d696b | chunk: faa6aa25c1b4157d | strength: statutory
obligated(employer, worker_or_worker_child, conform_to_scholarship_legislation) :-
    granting_scholarships(true).

% atom_id: a16f827030784aa9 | chunk: fb0bebfcc7503994 | strength: statutory
obligated(authority, none, despachar_recursos_e_papeis).

% atom_id: e584ceb4b82894f3 | chunk: fb6b96c88be3d436 | strength: statutory
permitted(operator_cinematographic, none, execute_extraordinary_daytime_sessions) :-
    agreement_type(collective_labor_agreement),
    overtime_rate(n25_percent_increase_on_normal_hour_salary).

% atom_id: 76ded9936e71f2e7 | chunk: fb6b96c88be3d436 | strength: statutory
obligated(operator_cinematographic, none, ensure_rest_period_between_sessions) :-
    rest_period_duration(X_0), X_0 >= 1.

% atom_id: b3e5a37053d55e00 | chunk: fb6b96c88be3d436 | strength: statutory
obligated(operator_cinematographic, none, limit_extraordinary_sessions_to_three_times_per_week).

% atom_id: f02a9f7985cc8631 | chunk: fb6dfb6bb1872f4f | strength: statutory
obligated(employer, worker, pay_uncontested_rescission_benefits) :-
    dispute_status(uncontested).

% atom_id: 01559b2eeb16720d | chunk: fb74b8ffb09884fc | strength: statutory
obligated(judge_or_court, legal_proceeding, declare_nullified_acts).

% atom_id: 0b7e658e6b4e7d3c | chunk: fb956e77b0c7761a | strength: statutory
obligated(procurador_com_exercicio_na_procuradoria_geral, none, perform_duties_in_the_general_procuracy).

% atom_id: 1f9106311f583f1d | chunk: fba1eb5c4437e833 | strength: statutory
obligated(auditor_fiscal_do_trabalho, employer, lavratura_de_auto_de_infracao) :-
    violation_of_legal_precept(true).

% atom_id: 098971c7258b5e48 | chunk: fc194d348a956641 | strength: statutory
obligated(employer, worker, provide_severance_benefits_according_to_law).

% atom_id: de2316d201a785ea | chunk: fc6964a444a9a956 | strength: statutory
permitted(legal_responsible_for_minor, contract_of_work, plead_for_contract_extinction) :-
    work_service_risk(physical_or_moral_harm).

% atom_id: 1749b8e09272313e | chunk: fcae2b5fab30d1a8 | strength: statutory
prohibited(manufacturer, none, fabricate_non_compliant_machines).

% atom_id: 09b9b18a8c0e3ba0 | chunk: fcae2b5fab30d1a8 | strength: statutory
prohibited(importer, none, import_non_compliant_machines).

% atom_id: 4aa4fbb88a183c17 | chunk: fcae2b5fab30d1a8 | strength: statutory
prohibited(seller, none, sell_non_compliant_machines).

% atom_id: 7ff21ef691c83c38 | chunk: fcae2b5fab30d1a8 | strength: statutory
prohibited(lessor, none, lease_non_compliant_machines).

% atom_id: 727965b41202a376 | chunk: fcae2b5fab30d1a8 | strength: statutory
prohibited(user, none, use_non_compliant_machines).

% atom_id: 79c758ecccd88f85 | chunk: fd55767d1f18c95c | strength: regulatory
obligated(authority, none, resolve_incompatibility_favor_first_designated_or_empossed_v) :-
    incompatibility_type(designated_or_empossed).

% atom_id: 7d9c89fc63de679d | chunk: fd55767d1f18c95c | strength: regulatory
obligated(authority, none, resolve_incompatibility_by_lottery) :-
    incompatibility_type(same_date_designation_or_empossing).

% atom_id: d2bd5c4caf16cc9a | chunk: fd573d62aaecf96b | strength: statutory
obligated(successor_employer, employee, assume_liabilities_from_predecessor) :-
    employment_succession(true).

% atom_id: 87d6104ecd02b9d8 | chunk: fd5f38e854baa6d7 | strength: statutory
obligated(driver, public, drive_with_care_and_prudence).

% atom_id: 0206424677267907 | chunk: fd6179ebfd318cd1 | strength: statutory
obligated(tribunal_regional, none, compete_when_divided_into_turmas).

% atom_id: c25d6990cbd5488f | chunk: fd7b879d9bb52c8a | strength: statutory
obligated(collective_agreement_parties, labor_relations, prevail_collective_agreement_conditions_over_convention).

% atom_id: 987548492f857f82 | chunk: fde48fa8c7939415 | strength: statutory
obligated(authority, litigant, notify_litigation_actions).

% atom_id: 469e2542d1de3330 | chunk: fe044378e268bb7a | strength: statutory
prohibited(authority, chemist, receive_professional_tax_without_registration_proof).

% atom_id: f509a3ff64f46133 | chunk: fe044378e268bb7a | strength: statutory
obligated(authority, chemist, require_registration_proof_for_official_acts).

% atom_id: a52f2fb77f76cba7 | chunk: fec451dea955917e | strength: statutory
obligated(authority, public, take_necessary_measures_to_preserve_order) :-
    dispute_status(in_progress),
    threat_level(low).

% atom_id: 02f496ddf78f0303 | chunk: ff3002b59836535a | strength: statutory
obligated(authority, public, perform_penalties_and_other_procedural_diligences).

% atom_id: 58ed2fb8d94b37ae | chunk: ff4a9468e24d7696 | strength: statutory
obligated(company, none, employ_minimum_specialized_professionals) :-
    company_group_classification(specific_group).

% atom_id: cb2c6206e33c1c36 | chunk: ff97bfdefc2d65d8 | strength: statutory
prohibited(employer, worker, conduct_intimate_searches).