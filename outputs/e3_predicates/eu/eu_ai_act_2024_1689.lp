% atom_id: 5b7194434043d835 | chunk: 0097db893574abbe | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    use_cases(high_risk_ai_systems),
    conditions_fulfilled(both).

% atom_id: 1933fa9b65355f5f | chunk: 00f886be50778ea7 | strength: statutory
obligated(authority, information_or_documentation, treat_with_confidentiality) :-
    source(this_article).

% atom_id: 798994cf5e542679 | chunk: 01293f2c7e701ed3 | strength: statutory
obligated(commission, none, take_request_into_account_and_reassess) :-
    request_type(reasoned_request),
    model_status(general_purpose_ai_model_with_systemic_risk).

% atom_id: 2062c264d8cadb95 | chunk: 01293f2c7e701ed3 | strength: statutory
permitted(provider, none, request_reassessment) :-
    model_status(general_purpose_ai_model_with_systemic_risk),
    time_since_designation(X_1), X_1 >= 6.

% atom_id: b258a11622dd0b98 | chunk: 013718f1ceb477a5 | strength: statutory
obligated(provider, market_surveillance_authorities, inform_of_non_compliance) :-
    risk_class(high),
    awareness_of_risk(yes).

% atom_id: 80f01357808672e0 | chunk: 013718f1ceb477a5 | strength: statutory
obligated(provider, notified_body, inform_of_non_compliance) :-
    risk_class(high),
    awareness_of_risk(yes),
    certificate_issued_by_notified_body(yes).

% atom_id: 3d436ce4ff228be6 | chunk: 019a2b80960caed0 | strength: statutory
obligated(expert, none, perform_tasks_impartially_and_objectively).

% atom_id: 87cbbacccf8c2bea | chunk: 019a2b80960caed0 | strength: statutory
obligated(expert, none, ensure_confidentiality_of_information_and_data).

% atom_id: 84d0802aaad8dadb | chunk: 019a2b80960caed0 | strength: statutory
obligated(expert, none, draw_up_declaration_of_interests).

% atom_id: 41d988d6e5b1f32b | chunk: 019a2b80960caed0 | strength: statutory
obligated(ai_office, none, establish_systems_and_procedures_to_manage_conflicts_of_inte).

% atom_id: 43b409e17698d863 | chunk: 01c0035b0526caab | strength: statutory
obligated(importer, none, indicate_contact_information).

% atom_id: cad60ee2239611c8 | chunk: 0315e5bdd352316a | strength: statutory
obligated(market_surveillance_authority, ai_system, evaluate_classification) :-
    classification(non_high_risk),
    provider_reason(sufficient_reason),
    market_authority_reason(consider_high_risk).

% atom_id: e50d3ca91f91a5f9 | chunk: 033d343a3dc963bd | strength: statutory
obligated(provider, personal_data, share_data_within_sandbox).

% atom_id: 7e445b63899a22aa | chunk: 033d343a3dc963bd | strength: statutory
obligated(provider, personal_data, comply_with_data_protection_law).

% atom_id: 038e4f3c78045add | chunk: 038033a94ccbd4b6 | strength: statutory
obligated(union_ai_testing_support_structures, none, provide_independent_advice) :-
    requestor(board_commission_market_surveillance_authorities).

% atom_id: d23e2486e5b722b0 | chunk: 03a7b89867f06fc0 | strength: statutory
obligated(provider, ai_system, register_at_national_level) :-
    risk_class(high).

% atom_id: ce3cc92210a32834 | chunk: 045e54cbfabb28ee | strength: statutory
obligated(provider, ai_system, perform_investigations) :-
    serious_incident_reported(true).

% atom_id: e90dc6b8d2ecb9b0 | chunk: 045e54cbfabb28ee | strength: statutory
obligated(provider, competent_authorities, cooperate_during_investigations) :-
    serious_incident_reported(true).

% atom_id: 530d512793a5783b | chunk: 045e54cbfabb28ee | strength: statutory
obligated(provider, notified_body, cooperate_during_investigations) :-
    serious_incident_reported(true),
    relevance_to_notified_body(true).

% atom_id: fb3bfd85b6dbb3af | chunk: 045e54cbfabb28ee | strength: statutory
obligated(provider, ai_system, not_alter_investigation) :-
    serious_incident_reported(true),
    investigation_action(alteration).

% atom_id: 50d4c7e5456406d3 | chunk: 04928b44712bad29 | strength: statutory
prohibited(national_competent_authority, information, disclose_confidentially_exchanged_information) :-
    context(high_risk_ai_systems_used_by_law_enforcement),
    context(high_risk_ai_systems_used_by_border_control),
    context(high_risk_ai_systems_used_by_immigration_authorities),
    context(high_risk_ai_systems_used_by_asylum_authorities),
    context(disclosure_would_jeopardise_public_and_national_security_int).

% atom_id: 17617d7fc37a57bb | chunk: 04928b44712bad29 | strength: statutory
permitted(national_competent_authority, information, exchange_information_confidentially) :-
    context(high_risk_ai_systems_used_by_law_enforcement),
    context(high_risk_ai_systems_used_by_border_control),
    context(high_risk_ai_systems_used_by_immigration_authorities),
    context(high_risk_ai_systems_used_by_asylum_authorities).

% atom_id: a76a650b94de7f4b | chunk: 04928b44712bad29 | strength: statutory
obligated(national_competent_authority, technical_documentation, remain_within_authorities) :-
    context(law_enforcement_is_provider_of_high_risk_ai_systems).

% atom_id: 5a3b6b21f1c3d6c3 | chunk: 04928b44712bad29 | strength: statutory
obligated(national_competent_authority, market_surveillance_authorities, access_technical_documentation) :-
    context(upon_request),
    context(appropriate_level_of_security_clearance).

% atom_id: a94a35aa935ed5a2 | chunk: 04ef68687878116e | strength: statutory
permitted(market_surveillance_authorities, none, request_commission_to_exercise_powers) :-
    necessity_and_proportionality(necessary_and_proportionate),
    context(assisting_with_the_fulfilment_of_tasks_under_this_regulation).

% atom_id: c88c31797f0c9f69 | chunk: 0574bbfce99d61ea | strength: statutory
permitted(european_parliament_or_council, none, revoke_delegation_of_power).

% atom_id: 5b750c04b6b6f8bd | chunk: 05a24f8c0df8d23c | strength: statutory
permitted(commission, provider_of_the_general_purpose_ai_model, request_documentation_or_additional_information).

% atom_id: 94523f3fe1a76399 | chunk: 0738dfd9bcfda2aa | strength: statutory
permitted(commission, none, adopt_implementing_acts) :-
    common_specifications(requirements_set_out_in_section_2_of_this_chapter),
    obligations(obligations_set_out_in_sections_2_and_3_of_chapter_v).

% atom_id: 8d272fe32b98d7ee | chunk: 0738dfd9bcfda2aa | strength: statutory
obligated(commission, none, consult_advisory_forum) :-
    common_specifications(requirements_set_out_in_section_2_of_this_chapter).

% atom_id: e6e2417921b1fc4b | chunk: 093794d1e5d59599 | strength: statutory
obligated(provider, training_validation_and_testing_data_sets, be_subject_to_data_governance_and_management_practices) :-
    risk_class(high).

% atom_id: 05e9cb1ffb5b737d | chunk: 09db576e68571dac | strength: statutory
obligated(board, commission_and_member_states, advise_and_assist).

% atom_id: 2ae24c2ff20a808f | chunk: 09db576e68571dac | strength: statutory
permitted(board, national_competent_authorities, contribute_to_coordination) :-
    responsibility(application_of_this_regulation).

% atom_id: 0e746fb847f40d15 | chunk: 09db576e68571dac | strength: statutory
permitted(board, market_surveillance_authorities, support_joint_activities) :-
    agreement(yes).

% atom_id: 520b458f4cd025b9 | chunk: 09db576e68571dac | strength: statutory
permitted(board, member_states, collect_and_share_expertise).

% atom_id: 20cbc00ea03b4b69 | chunk: 09db576e68571dac | strength: statutory
permitted(board, commission, provide_advice_on_implementation) :-
    regulation(general_purpose_ai_models).

% atom_id: 83b9478a8c48e7a1 | chunk: 09db576e68571dac | strength: statutory
permitted(board, member_states, contribute_to_harmonisation_of_administrative_practices) :-
    practices(derogation_from_conformity_assessment_procedures_functioning).

% atom_id: 927e733a1b40d4d5 | chunk: 09db576e68571dac | strength: statutory
permitted(board, commission, issue_recommendations_and_opinions) :-
    request(yes_initiative).

% atom_id: f8681ede7444c2ec | chunk: 09db576e68571dac | strength: statutory
obligated(board, commission_and_member_states, support_ai_office_in_establishing_and_developing_ai_regulato).

% atom_id: 9616ab2ed89460ca | chunk: 09db576e68571dac | strength: statutory
permitted(board, national_competent_authorities_and_commission, develop_organisational_and_technical_expertise).

% atom_id: 2d64791d904dce45 | chunk: 09db576e68571dac | strength: statutory
permitted(board, ai_office_and_market_operators, contribute_to_development_of_common_criteria).

% atom_id: 3c11092d957255a2 | chunk: 09db576e68571dac | strength: statutory
permitted(board, union_institutions_bodies_offices_and_agencies, cooperate_with_relevant_expert_groups_and_networks) :-
    fields(product_safety_cybersecurity_competition_digital_and_media_s).

% atom_id: 649df5368818e5c0 | chunk: 09db576e68571dac | strength: statutory
permitted(board, competent_authorities_of_third_countries_and_international_o, contribute_to_effective_cooperation).

% atom_id: ce1dad6ebdf51d68 | chunk: 09db576e68571dac | strength: statutory
permitted(board, national_competent_authorities_and_commission, assess_training_needs).

% atom_id: 07618d3ee31400a0 | chunk: 09db576e68571dac | strength: statutory
permitted(board, ai_office_and_national_competent_authorities, support_establishment_and_development_of_ai_regulatory_sandb).

% atom_id: 6bf4a620c8faa56b | chunk: 09db576e68571dac | strength: statutory
permitted(board, commission, provide_advice_on_international_matters).

% atom_id: 22f88b0d66fc640d | chunk: 09db576e68571dac | strength: statutory
permitted(board, commission, provide_opinions_on_qualified_alerts) :-
    regulation(general_purpose_ai_models).

% atom_id: 620d63114abc3db8 | chunk: 09db576e68571dac | strength: statutory
permitted(board, member_states, receive_opinions_on_qualified_alerts_and_national_experience).

% atom_id: f05385479a87cacf | chunk: 0a1fc364fdbd88e5 | strength: statutory
obligated(authorised_representative, none, perform_tasks_specified_in_mandate).

% atom_id: 68715666314bb06f | chunk: 0a1fc364fdbd88e5 | strength: statutory
obligated(authorised_representative, ai_office, provide_copy_of_mandate) :-
    request(received).

% atom_id: 068aca5a092496dc | chunk: 0a2c152af90592c7 | strength: statutory
obligated(board, market_surveillance_authorities_and_notifying_authorities, establish_standing_sub_groups).

% atom_id: 72a8eadd0a12014e | chunk: 0a2c152af90592c7 | strength: statutory
obligated(board, standing_sub_group_for_market_surveillance, act_as_adco).

% atom_id: bee5e24762ce484a | chunk: 0a2c152af90592c7 | strength: statutory
permitted(board, board, establish_other_standing_or_temporary_sub_groups).

% atom_id: 93cd2895e140eb64 | chunk: 0a2c152af90592c7 | strength: statutory
permitted(board, representatives_of_advisory_forum, be_invited_to_sub_groups_or_specific_meetings_as_observers).

% atom_id: 00d2879f6373f407 | chunk: 0a64bffbf8507241 | strength: statutory
permitted(ai_office, providers_of_general_purpose_ai_models, adhere_to_codes_of_practice) :-
    systemic_risk(present).

% atom_id: 93be779c3ba085ef | chunk: 0a64bffbf8507241 | strength: statutory
obligated(providers_of_general_purpose_ai_models, non_systemic_risk_providers, adhere_to_obligations_in_article_53) :-
    systemic_risk(not_present).

% atom_id: 3c6c143cfd7b6991 | chunk: 0a64bffbf8507241 | strength: statutory
permitted(providers_of_general_purpose_ai_models, non_systemic_risk_providers, declare_interest_to_join_full_code) :-
    systemic_risk(not_present).

% atom_id: 1cccc5480a14dbac | chunk: 0b673cf2d50a8f1a | strength: statutory
obligated(national_competent_authority, none, extend_participation_period) :-
    project_complexity(complex),
    project_scale(large).

% atom_id: 400aab938b4e917b | chunk: 0b9f0165da0fee6f | strength: statutory
obligated(commission, none, submit_report) :-
    date(n2_august_2029).

% atom_id: ecccc9934b8260c2 | chunk: 0b9f0165da0fee6f | strength: statutory
obligated(commission, none, submit_report) :-
    frequency(every_four_years_thereafter).

% atom_id: 6b076a1519ec2174 | chunk: 0c175084808af46c | strength: statutory
obligated(authority, real_time_remote_biometric_identification_system, subject_to_authorisation) :-
    use_purpose(law_enforcement_publicly_accessible_spaces).

% atom_id: 636951378cb162ec | chunk: 0c175084808af46c | strength: statutory
permitted(authority, real_time_remote_biometric_identification_system, commence_use_without_authorisation) :-
    urgency(duly_justified),
    time_limit(X_1), X_1 <= 24.

% atom_id: 10f5bd55ba7f21cf | chunk: 0c175084808af46c | strength: statutory
obligated(authority, authorisation_decision, grant_authorisation) :-
    use_necessity(necessary_for_proportionate_to_objectives),
    time_limit(X_1), X_1 <= 24,
    output(discarded_and_deleted).

% atom_id: e011687e195bcc67 | chunk: 0c175084808af46c | strength: statutory
obligated(authority, authorisation_decision, consider_elements_in_request) :-
    use_scope(limited_to_strictly_necessary).

% atom_id: 38b64afa97a32368 | chunk: 0c175084808af46c | strength: statutory
obligated(authority, authorisation_decision, not_base_decision_on_system_output_alone) :-
    output(adverse_legal_effect).

% atom_id: abe3f978f906e4f2 | chunk: 0c9644bff17ce881 | strength: statutory
obligated(commission, none, issue_standardisation_requests) :-
    regulation(eu_no_10252012).

% atom_id: 10bbb97de4183c31 | chunk: 0c9644bff17ce881 | strength: statutory
obligated(commission, none, consult_board_and_stakeholders) :-
    regulation(eu_no_10252012).

% atom_id: f87dacfe9266f0ed | chunk: 0c9644bff17ce881 | strength: statutory
obligated(commission, european_standardisation_organisations, provide_evidence_of_best_efforts) :-
    regulation(eu_no_10252012).

% atom_id: 356984cb88290d49 | chunk: 0d920861a59c0b92 | strength: statutory
obligated(national_public_authorities_or_bodies, none, treat_with_confidentiality) :-
    information_or_documentation(obtained_pursuant_to_this_article).

% atom_id: 4b9daf9f8412bd35 | chunk: 0d985b79ecc836b6 | strength: statutory
obligated(authority, none, organise_awareness_raising_activities) :-
    target_group(sme_start_ups_deployers_local_public_authorities).

% atom_id: a38329d009db9899 | chunk: 0de73f5dbf7f3bba | strength: statutory
obligated(provider, ai_system, comply_with_obligations) :-
    license_type(free_and_open_source),
    risk_class(general_purpose).

% atom_id: 8aadc1409f2457aa | chunk: 0de73f5dbf7f3bba | strength: statutory
obligated(provider, none, release_ai_model) :-
    license_type(free_and_open_source),
    risk_class(general_purpose).

% atom_id: 748510de5e1fff55 | chunk: 0e4077698ef2bac5 | strength: statutory
obligated(provider, ai_system, justify_technical_solutions) :-
    compliance(non_compliance_with_common_specifications).

% atom_id: 56aee0b2f6ebd489 | chunk: 0ec7e0ced822afbe | strength: statutory
obligated(deployer, data, enter_into_eu_database) :-
    deployer_type(public_authority_agency_or_body_acting_on_behalf_of_a_public).

% atom_id: 5d603c44b8efba3e | chunk: 0fd549d900631c6e | strength: statutory
obligated(provider_or_prospective_provider, none, draw_up_real_world_testing_plan).

% atom_id: b518d4e0eab75520 | chunk: 0fd549d900631c6e | strength: statutory
obligated(provider_or_prospective_provider, none, submit_real_world_testing_plan).

% atom_id: 83ac0b0e759c1251 | chunk: 0feae3a92e7cd208 | strength: statutory
obligated(market_surveillance_authorities, none, cooperate_with_ai_office) :-
    relevant_market_surveillance_authorities(have_sufficient_reason),
    ai_systems(general_purpose),
    deployers(use_for_at_least_one_high_risk_purpose).

% atom_id: 0d44af419bbea902 | chunk: 0feae3a92e7cd208 | strength: statutory
obligated(market_surveillance_authorities, none, inform_board_and_other_authorities) :-
    relevant_market_surveillance_authorities(have_sufficient_reason),
    ai_systems(general_purpose),
    deployers(use_for_at_least_one_high_risk_purpose).

% atom_id: 79dc78bdb471ba58 | chunk: 0feca74fe9914cfb | strength: statutory
obligated(provider, quality_management_system, put_in_place).

% atom_id: d6fe156474c444c1 | chunk: 0feca74fe9914cfb | strength: statutory
obligated(provider, quality_management_system, ensure_compliance).

% atom_id: 14e3699166139209 | chunk: 0feca74fe9914cfb | strength: statutory
obligated(provider, quality_management_system, document_in_systematic_and_orderly_manner).

% atom_id: 6f55a1a24a47d056 | chunk: 0feca74fe9914cfb | strength: statutory
obligated(provider, quality_management_system, include_aspects).

% atom_id: 134a68cf6c52d526 | chunk: 10276680f0c0ad10 | strength: statutory
obligated(commission, none, evaluate_impact_and_effectiveness) :-
    date(by_2_august_2028),
    frequency(every_three_years).

% atom_id: 94bdab637f3b894b | chunk: 1058370dd80ce864 | strength: statutory
obligated(member_states, none, facilitate_tasks).

% atom_id: e1d1152ee9311ba5 | chunk: 10cd1e73a3865bb0 | strength: statutory
obligated(member_state, none, establish_or_designate_authorities).

% atom_id: a663a3832b0ae8fc | chunk: 10cd1e73a3865bb0 | strength: statutory
obligated(national_competent_authorities, none, exercise_powers_independently).

% atom_id: 73373e47cff11064 | chunk: 10cd1e73a3865bb0 | strength: statutory
obligated(national_competent_authorities, none, exercise_powers_impartially).

% atom_id: 8f5f3f515a7ef0b6 | chunk: 10cd1e73a3865bb0 | strength: statutory
obligated(national_competent_authorities, none, exercise_powers_without_bias).

% atom_id: 5c7b11f16492e16d | chunk: 10cd1e73a3865bb0 | strength: statutory
obligated(members_of_authorities, none, refrain_from_incompatible_actions).

% atom_id: 886e8a695edbea29 | chunk: 1105a43559f2d12f | strength: statutory
obligated(provider, none, implement_policy) :-
    law(union_law_on_copyright_and_related_rights).

% atom_id: f627bc773d92cb73 | chunk: 1105a43559f2d12f | strength: statutory
obligated(provider, none, identify_and_comply_with_reservations) :-
    reservation(expressed_pursuant_to_article_43_of_directive_eu_2019790).

% atom_id: 466585e1070bf575 | chunk: 12b2e1be6967fa8b | strength: statutory
obligated(commission, none, take_into_account_requirements) :-
    system_type(safety_component),
    regulation(eu_20241689).

% atom_id: 29ca31565270cb11 | chunk: 13579a757291a7b0 | strength: statutory
obligated(commission, none, enter_into_consultations) :-
    timeframe(within_15_calendar_days),
    event(objections_raised_by_member_state_commission_considers_autho).

% atom_id: 622d7455524690dd | chunk: 13579a757291a7b0 | strength: statutory
obligated(commission, operators, consult_operators) :-
    timeframe(within_15_calendar_days),
    event(objections_raised_by_member_state_commission_considers_autho).

% atom_id: 62342994ab1a3df6 | chunk: 13579a757291a7b0 | strength: statutory
obligated(commission, none, decide_on_authorisation) :-
    timeframe(after_consultations_and_operator_views).

% atom_id: b8c0c0ac2eebee46 | chunk: 13579a757291a7b0 | strength: statutory
obligated(commission, member_state_and_operators, address_decision) :-
    timeframe(after_decision).

% atom_id: c155e6cfcbda641f | chunk: 1390bae72e38ff97 | strength: statutory
obligated(provider, none, handle_communication).

% atom_id: b79fb01682ad8215 | chunk: 152aa8a048af912b | strength: statutory
obligated(authority, none, alert_ai_office) :-
    systemic_risk(general_purpose_ai_models).

% atom_id: f3488cf015547385 | chunk: 152aa8a048af912b | strength: statutory
obligated(authority, none, develop_tools_methodologies) :-
    evaluation(capabilities).

% atom_id: 733590f45d293cf5 | chunk: 152aa8a048af912b | strength: statutory
obligated(authority, none, provide_advice_classification) :-
    systemic_risk(general_purpose_ai_models).

% atom_id: 766c82e4b9dddb9d | chunk: 152aa8a048af912b | strength: statutory
obligated(authority, none, provide_advice_classification) :-
    general_purpose_ai_models(various).

% atom_id: 6af36492cdfd22ea | chunk: 152aa8a048af912b | strength: statutory
obligated(authority, none, contribute_development_tools_templates) :-
    general_purpose_ai_models(various).

% atom_id: a4bdbcb1369d3c0e | chunk: 155384e18210cde9 | strength: statutory
obligated(national_competent_authorities, commission, notify_of_serious_incident) :-
    incident_type(serious).

% atom_id: 05a6afd8a03b14df | chunk: 157b83bf906c476c | strength: statutory
obligated(provider_or_prospective_provider, none, modify_testing_in_real_world_conditions).

% atom_id: c73682b0cd5aa8ab | chunk: 157b83bf906c476c | strength: statutory
obligated(deployer_or_prospective_deployer, none, modify_testing_in_real_world_conditions).

% atom_id: 2dd481c47fc093f0 | chunk: 161e03d576446dfc | strength: statutory
obligated(market_surveillance_authority, none, be_designated) :-
    risk_class(high),
    product_category(section_a_of_annex_i).

% atom_id: 267daa4f5ae74b77 | chunk: 161e03d576446dfc | strength: statutory
obligated(member_states, none, designate_authority) :-
    risk_class(high),
    product_category(section_a_of_annex_i),
    circumstances(appropriate).

% atom_id: 086854b575ce35d4 | chunk: 163307224a1afb2b | strength: statutory
obligated(provider, none, comply_with_obligations) :-
    date_of_model_placement(X_0), X_0 <= 2025.

% atom_id: 84da4dfdebdf9e0e | chunk: 164ad83d8510b3ef | strength: statutory
obligated(none, operator_or_notified_body, non_compliance).

% atom_id: af7caebabf2f7335 | chunk: 16593ee9bedc1b69 | strength: statutory
obligated(subjects_of_testing, vulnerable_persons, appropriate_protection) :-
    status(vulnerable_group).

% atom_id: 0c9883b17348e27b | chunk: 16710efbeceaf3af | strength: statutory
obligated(provider, none, be_subject_to_fines) :-
    misclassification_reason(to_circumvent_application_of_requirements_in_chapter_iii_sec),
    evaluation_result(high_risk_ai_system_misclassified_as_non_high_risk).

% atom_id: 112cc340b753c27e | chunk: 16bbab564321dbce | strength: statutory
obligated(provider, ai_office_and_national_competent_authorities, keep_track_document_report).

% atom_id: 4be8409570406467 | chunk: 1734428358c31338 | strength: statutory
obligated(commission, none, notify_delegated_act).

% atom_id: 55a6ffe4a15ba625 | chunk: 1737e990bdc8aa74 | strength: statutory
prohibited(provider, outcome, considered_easily_corrigible_or_reversible) :-
    adverse_impact(health_safety_fundamental_rights).

% atom_id: 6793e0c1e2e61c49 | chunk: 17a696c123c0fd96 | strength: statutory
obligated(provider, post_market_monitoring_system, collect_and_analyze_data) :-
    risk_class(high).

% atom_id: 14c40b3527724da4 | chunk: 17a696c123c0fd96 | strength: statutory
obligated(provider, post_market_monitoring_system, include_analysis_of_interactions) :-
    risk_class(high).

% atom_id: db43e15eec578b6d | chunk: 17a696c123c0fd96 | strength: statutory
prohibited(provider, deployer, disclose_sensitive_data) :-
    deployer_type(law_enforcement_authority).

% atom_id: 926688c7149db270 | chunk: 17b6925f8c5eda82 | strength: statutory
obligated(developer, high_risk_ai_system, mitigate_risks) :-
    risk_mitigation(reasonably).

% atom_id: 4e6e80899af6ad8d | chunk: 17b6925f8c5eda82 | strength: statutory
obligated(provider, high_risk_ai_system, provide_technical_information) :-
    risk_mitigation(reasonably).

% atom_id: 7cdb260c3717dac0 | chunk: 17ede4c2ff7d509a | strength: statutory
prohibited(commission, provider_of_general_purpose_ai_models, impose_fines) :-
    infringement(intentional_or_negligent).

% atom_id: f91ff54fb4fa92ca | chunk: 1839a4bc6adaa28f | strength: statutory
obligated(authorised_person, personal_data, secure_and_protect).

% atom_id: eefe2eb5b70e0b52 | chunk: 1839a4bc6adaa28f | strength: statutory
obligated(authorised_person, personal_data, access_with_suitable_safeguards).

% atom_id: 37b4e14fe55cbc1e | chunk: 1839a4bc6adaa28f | strength: statutory
obligated(authorised_person, personal_data, document_access).

% atom_id: b8c2df4339a1a708 | chunk: 1839a4bc6adaa28f | strength: statutory
obligated(authorised_person, personal_data, avoid_misuse).

% atom_id: 5a84ccbc39214aba | chunk: 1911bab8ab6d58f2 | strength: statutory
obligated(market_surveillance_authority, none, issue_authorisation) :-
    high_risk_ai_system(complies_with_requirements).

% atom_id: f0a2e03e2398204e | chunk: 1911bab8ab6d58f2 | strength: statutory
obligated(market_surveillance_authority, commission_and_other_member_states, inform_of_authorisation) :-
    authorisation(issued_pursuant_to_paragraphs_1_and_2).

% atom_id: db180f21da104324 | chunk: 1911bab8ab6d58f2 | strength: statutory
prohibited(market_surveillance_authority, none, inform_of_sensitive_data) :-
    sensitive_operational_data(related_to_activities_of_law_enforcement_authorities).

% atom_id: 458cddf554a2f94e | chunk: 191c1fade8f896ee | strength: statutory
obligated(member_states, none, facilitate_coordination).

% atom_id: d0fdc661c59e41b1 | chunk: 198a0d5bd713cbb7 | strength: statutory
obligated(notified_bodies, none, carry_out_tasks_with_integrity_and_competence).

% atom_id: 1a30ba1e413adbad | chunk: 1b0f5e33c84e8ff8 | strength: statutory
obligated(commission, none, evaluate_ai_office).

% atom_id: 8ad5dd657f255906 | chunk: 1b0f5e33c84e8ff8 | strength: statutory
obligated(commission, none, submit_report).

% atom_id: 2e5805e50c139b39 | chunk: 1b5f9e2f8ff9aa71 | strength: statutory
permitted(market_surveillance_authority, none, submit_reasoned_request) :-
    inability_to_access_info(true),
    made_all_appropriate_efforts(true).

% atom_id: 7c8ea50bed699729 | chunk: 1b5f9e2f8ff9aa71 | strength: statutory
obligated(ai_office, market_surveillance_authority, supply_relevant_info) :-
    request_received(true).

% atom_id: 99eb5947518cf5ef | chunk: 1b5f9e2f8ff9aa71 | strength: statutory
obligated(market_surveillance_authority, none, safeguard_confidentiality) :-
    obtained_info(true).

% atom_id: 28d61a32a5764ce1 | chunk: 1bb9e129b1e60241 | strength: statutory
permitted(data_controller, personal_data, process_for_ai_development) :-
    original_purpose(lawfully_collected),
    new_purpose(developing_training_and_testing_ai_systems_in_sandbox),
    all_conditions_met(true).

% atom_id: c59462c3e15feacd | chunk: 1c4e09d0d9d69314 | strength: statutory
obligated(notified_bodies, none, ensure_confidence_performance).

% atom_id: 1443311d75f39aba | chunk: 1c4e09d0d9d69314 | strength: statutory
obligated(notified_bodies, none, ensure_confidence_results_assessment).

% atom_id: bc7b7110761adb0f | chunk: 1d374b88f404aae7 | strength: statutory
obligated(provider, ai_system, provide_logging_capabilities) :-
    risk_class(high).

% atom_id: 596055b4f0e5a43b | chunk: 1de64d687586f70b | strength: statutory
permitted(market_surveillance_authority, none, take_decision_on_territory) :-
    serious_incident(true),
    other_grounds(true).

% atom_id: 7ed7f9cb7be25c55 | chunk: 1e29e38a446b0045 | strength: statutory
obligated(provider, ai_model, presume_high_impact_capabilities) :-
    cumulative_computation(X_0), X_0 > 1025.

% atom_id: 97e73876530d222f | chunk: 1e434f79c241cc3a | strength: statutory
obligated(deployer, none, register_in_eu_database) :-
    risk_class(high),
    entity_type(public_authority_union_institution_body_office_agency_person).

% atom_id: 5f82ab7fc7648f73 | chunk: 1e73c9835c4d94b2 | strength: statutory
obligated(notified_body, none, have_sufficient_internal_competences) :-
    task(evaluation_of_tasks_conducted_by_external_parties_on_its_beh).

% atom_id: 07156c0fb33cff70 | chunk: 1e73c9835c4d94b2 | strength: statutory
obligated(notified_body, none, have_permanent_availability_of_personnel) :-
    type(administrative_technical_legal_and_scientific).

% atom_id: 53bc6d6873afaee9 | chunk: 1f6ac628d7dba0e8 | strength: statutory
obligated(member_state, none, lay_down_rules_on_fines).

% atom_id: c6cefd9c615cf0f2 | chunk: 1fc71844c85b2cda | strength: statutory
obligated(provider_or_deployer, eu_database, contain_relevant_data) :-
    data_necessity(necessary_for_information_collection).

% atom_id: 98fafd028bcae00a | chunk: 1fc71844c85b2cda | strength: statutory
obligated(provider_or_deployer, natural_persons, provide_contact_details) :-
    role(responsible_for_registration).

% atom_id: a56ef35744319992 | chunk: 207c707d89a4ea44 | strength: statutory
prohibited(regulation, none, apply_to_areas_outside_union_scope).

% atom_id: 3dde6ad7402781d5 | chunk: 207c707d89a4ea44 | strength: statutory
prohibited(regulation, none, affect_competences_of_member_states_concerning_national_secu).

% atom_id: 55ab028aaf5f86a1 | chunk: 207c707d89a4ea44 | strength: statutory
prohibited(regulation, ai_systems, be_placed_on_market_put_into_service_or_used_exclusively_for) :-
    use_case(military_defence_or_national_security_purposes).

% atom_id: 33b3450832015068 | chunk: 207c707d89a4ea44 | strength: statutory
prohibited(regulation, ai_systems, be_placed_on_market_put_into_service_or_used_exclusively_for) :-
    use_case(military_defence_or_national_security_purposes),
    location_of_output(in_the_union).

% atom_id: 38866b79fe70237e | chunk: 20892746c07043bd | strength: statutory
obligated(deployer, ai_system, disclose_artificial_generation) :-
    content_type(deep_fake),
    use_case(authorised_by_law_to_detect_prevent_investigate_or_prosecute).

% atom_id: e91e447c97f7aa8e | chunk: 20892746c07043bd | strength: statutory
obligated(deployer, ai_system, disclose_artificial_generation) :-
    content_type(text),
    use_case(publishing_public_interest),
    human_review_or_edit_control(no_human_review_or_edit_control).

% atom_id: 2789c748fa821776 | chunk: 20f2c265a17de3fb | strength: statutory
prohibited(provider, biometric_categorisation_system, use_for_inference_of_protected_characteristics) :-
    categorisation_method(race_political_opinions_trade_union_membership_religious_or).

% atom_id: 054006d8f472a824 | chunk: 20f2c265a17de3fb | strength: statutory
permitted(provider, biometric_categorisation_system, label_or_filter_biometric_data) :-
    data_source(lawfully_acquired),
    purpose(labelling_filtering).

% atom_id: 52e8427a0ab76a0f | chunk: 227d08edf40d35e9 | strength: statutory
permitted(market_surveillance_authorities_and_the_commission, none, propose_joint_activities) :-
    risk_class(high),
    serious_risk(X_1), X_1 >= 2.

% atom_id: 4ff5665d4e611df3 | chunk: 227d08edf40d35e9 | strength: statutory
obligated(market_surveillance_authorities_and_the_commission, none, conduct_joint_investigations) :-
    risk_class(high),
    serious_risk(X_1), X_1 >= 2.

% atom_id: 726d13b4192b29d3 | chunk: 227d08edf40d35e9 | strength: statutory
obligated(ai_office, none, provide_coordination_support) :-
    activity_type(joint_investigations).

% atom_id: 45b4896acc67066b | chunk: 22a3c5ae9ecd2a49 | strength: statutory
obligated(market_surveillance_authorities, high_risk_ai_system, grant_access_to_source_code) :-
    request_reasoned(true),
    both_conditions_fulfilled(true).

% atom_id: 1bc6bb7a2f532033 | chunk: 2375aa620eeea905 | strength: statutory
permitted(provider, none, apply_for_sandbox) :-
    eligibility_criteria(fulfilled),
    selection_criteria(fulfilled).

% atom_id: 340b387eb036df1d | chunk: 2375aa620eeea905 | strength: statutory
obligated(national_competent_authorities, applicants, inform_of_decision) :-
    timeframe(within_three_months).

% atom_id: 58b0671595b96876 | chunk: 23b75446a47eeb22 | strength: statutory
obligated(provider, instructions_for_use, include_relevant_information) :-
    risk_class(high).

% atom_id: 7bf812a51bf69b01 | chunk: 2456f266391ff24f | strength: statutory
obligated(deployer, competent_authorities, cooperate_with_authorities).

% atom_id: 15f4b917e599afc1 | chunk: 258126ae87c23a9f | strength: statutory
obligated(provider, technical_documentation, be_drawn_up) :-
    risk_class(high).

% atom_id: 7206f4fd8f1b61fd | chunk: 258126ae87c23a9f | strength: statutory
obligated(provider, technical_documentation, be_kept_up_to_date) :-
    risk_class(high).

% atom_id: 615dd73bc694e265 | chunk: 258126ae87c23a9f | strength: statutory
obligated(provider, ai_system, comply_with_requirements) :-
    risk_class(high).

% atom_id: 7b1d6e69eea9ffc4 | chunk: 258126ae87c23a9f | strength: statutory
obligated(provider, national_competent_authorities_and_notified_bodies, be_provided_with_information) :-
    risk_class(high).

% atom_id: db783f218798fc24 | chunk: 258126ae87c23a9f | strength: statutory
permitted(sme, technical_documentation, be_provided_in_simplified_manner) :-
    risk_class(high),
    enterprise_type(small_and_microenterprises).

% atom_id: 5de48d98a495755d | chunk: 258126ae87c23a9f | strength: statutory
obligated(provider, simplified_technical_documentation_form, be_used) :-
    risk_class(high),
    enterprise_type(small_and_microenterprises).

% atom_id: 15eb64b9f56c67d9 | chunk: 258126ae87c23a9f | strength: statutory
obligated(notified_bodies, technical_documentation, be_accepted_for_conformity_assessment) :-
    risk_class(high),
    enterprise_type(small_and_microenterprises).

% atom_id: 94abc6f6b18fa4b2 | chunk: 25d53f31b616dd7c | strength: statutory
obligated(provider, operator, develop_and_maintain_information_platform).

% atom_id: ab3e1845dcdad748 | chunk: 266ec058cde797cf | strength: statutory
permitted(test_participant, none, refuse_to_participate).

% atom_id: 18d3680c5e849112 | chunk: 266ec058cde797cf | strength: statutory
permitted(test_participant, none, withdraw_from_testing).

% atom_id: c951baca50e311e7 | chunk: 2679878ba6a3d582 | strength: statutory
obligated(provider, ai_system, test_ai_system) :-
    risk_class(high).

% atom_id: af35850f84ff2455 | chunk: 269031899cfa68d4 | strength: statutory
obligated(operator, ai_system, take_corrective_action).

% atom_id: 7165411542f35b98 | chunk: 26e27609bfd1e44d | strength: statutory
obligated(provider, eu_database, enter_data).

% atom_id: e356ccd2d93b9ab4 | chunk: 26e27609bfd1e44d | strength: statutory
obligated(authorised_representative, eu_database, enter_data).

% atom_id: 00e4b4ee3552e07b | chunk: 2701a4850de45b7b | strength: statutory
obligated(provider, ai_system_or_model, be_in_conformity_with_standards) :-
    risk_class(high),
    conformity_status(in_conformity).

% atom_id: 04f7f1b02080149f | chunk: 273be5af4ca9782d | strength: statutory
obligated(commission, none, assist_with_committee).

% atom_id: 8ae06021bc7b590d | chunk: 27aa954d02d49529 | strength: statutory
obligated(board, commission, provide_information).

% atom_id: 7b422badcfc47d3d | chunk: 27aa954d02d49529 | strength: statutory
obligated(member_states, commission, provide_information).

% atom_id: 6119ceaf0563a498 | chunk: 27aa954d02d49529 | strength: statutory
obligated(national_competent_authorities, commission, provide_information).

% atom_id: d1cdf17a27c5489f | chunk: 27e652ab8f9adbbd | strength: statutory
obligated(provider, national_competent_authorities, keep_declaration_disposable) :-
    risk_class(high).

% atom_id: 6b65f7572a969095 | chunk: 27e652ab8f9adbbd | strength: statutory
obligated(provider, national_competent_authorities, submit_declaration_on_request) :-
    risk_class(high).

% atom_id: 605b2c0a6dbcbe1b | chunk: 282b481e050e43f3 | strength: statutory
obligated(deployer, market_surveillance_authority, notify_use_of_biometric_system) :-
    use_context(real_time_remote),
    space_type(publicly_accessible),
    purpose(law_enforcement).

% atom_id: 6c178d349554cf36 | chunk: 282b481e050e43f3 | strength: statutory
obligated(deployer, national_data_protection_authority, notify_use_of_biometric_system) :-
    use_context(real_time_remote),
    space_type(publicly_accessible),
    purpose(law_enforcement).

% atom_id: e75c95522bff0c46 | chunk: 28bc603dce95454b | strength: statutory
obligated(provider, none, appoint_authorised_representative).

% atom_id: b3a69fcd2749a4c8 | chunk: 299305ce4d2e36b8 | strength: statutory
prohibited(provider, ai_system, infer_emotions) :-
    use_case(workplace_and_education_institutions),
    intended_use(medical_or_safety_reasons).

% atom_id: 2082678f2ffb49fc | chunk: 2a90b773c755e876 | strength: statutory
obligated(provider, ai_system, implement_mitigation_measures) :-
    evaluation_result(serious_and_substantiated_concern_of_a_systemic_risk_at_unio).

% atom_id: 76312c517f61c303 | chunk: 2bd79c719396d25a | strength: statutory
obligated(provider, none, restrict_market_access).

% atom_id: c95d2a46b6bca3c0 | chunk: 2bd79c719396d25a | strength: statutory
obligated(provider, none, withdraw_model).

% atom_id: ccc6e48ff8fcea8f | chunk: 2bd79c719396d25a | strength: statutory
obligated(provider, none, recall_model).

% atom_id: 6396f4608fcc89f3 | chunk: 2c63fa0d2c38c02e | strength: statutory
obligated(provider, none, establish_and_document_post_market_monitoring_system) :-
    risk_class(high).

% atom_id: 2f752c89b79c8f44 | chunk: 2ca8a70e6a0b1282 | strength: statutory
obligated(researcher_developer, none, conduct_activities_in_accordance_with_law) :-
    activity_type(research),
    activity_type(testing),
    activity_type(development).

% atom_id: ce9366e8e580e29f | chunk: 2ca8a70e6a0b1282 | strength: statutory
obligated(researcher_developer, none, conduct_activities_in_accordance_with_law) :-
    activity_type(testing).

% atom_id: 3e78c1fd94c0fd49 | chunk: 2d950531e1f330d2 | strength: statutory
obligated(provider, general_purpose_ai_model_with_systemic_risk, ensure_cybersecurity_protection).

% atom_id: 33c9e8b2ce72ae45 | chunk: 2d950531e1f330d2 | strength: statutory
obligated(provider, physical_infrastructure_of_the_model, ensure_cybersecurity_protection).

% atom_id: 0342742e08d7ac5a | chunk: 2e4de6eaee9afc7a | strength: statutory
obligated(national_competent_authorities, public, ensure_cybersecurity).

% atom_id: 25e9630fc514b3e5 | chunk: 2f04e427c3f781a3 | strength: statutory
obligated(user, ai_system, request_reversal_or_disregarding_predictions_recommendations).

% atom_id: 79bd41a6f70e1853 | chunk: 2f5de1313155d4fc | strength: statutory
obligated(deployer, natural_person, assign_human_oversight) :-
    competence(necessary),
    training(necessary),
    authority(necessary),
    support(necessary).

% atom_id: ed84fa86a473d811 | chunk: 2f9e46fac538b026 | strength: statutory
obligated(commission_and_national_authorities, eu_database, have_access) :-
    system_risk_class(high),
    areas_of_law_enforcement_migration_asylum_border_control_man(true).

% atom_id: d85a0fceb893811e | chunk: 3065eb63b33e7c7f | strength: statutory
obligated(notified_bodies, none, establish_procedures) :-
    provider_size(various_sizes),
    sector(various_sectors),
    structure(various_structures),
    ai_system_complexity(various_complexities).

% atom_id: ccc64e648b00b121 | chunk: 30928f014c318a32 | strength: statutory
permitted(ai_office, none, take_necessary_actions) :-
    purpose(monitoring_implementation_and_compliance).

% atom_id: fdc09a49d7df91c1 | chunk: 30928f014c318a32 | strength: statutory
obligated(provider_of_general_purpose_ai_models, none, adhere_to_approved_codes_of_practice) :-
    regulation(this_regulation).

% atom_id: c2b70984da5abb8a | chunk: 31fc73c45298a516 | strength: statutory
obligated(provider, none, maintain_technical_documentation) :-
    status(financial_institution),
    governance_requirements(subject_to_union_financial_services_law).

% atom_id: bd13b5f399f5b4a6 | chunk: 325d3e63a0ee02cd | strength: statutory
obligated(board, none, provide_standardised_templates).

% atom_id: 26b80a9b61c3e881 | chunk: 33875559449f4d63 | strength: statutory
obligated(commission, none, appoint_members) :-
    role(members_of_advisory_forum).

% atom_id: 841b49b02649c088 | chunk: 3392c9d7e85f2c24 | strength: statutory
obligated(member_states, none, lay_down_rules_on_penalties).

% atom_id: 055079b5a4bccfbd | chunk: 3392c9d7e85f2c24 | strength: statutory
obligated(member_states, none, take_measures_to_ensure_implementations).

% atom_id: 57092a8cfa876e2e | chunk: 33dc3164dabd5745 | strength: statutory
obligated(authorised_representative, none, be_addressed_by_authorities).

% atom_id: d6d1f04b6be4609b | chunk: 346c9b016fb8404b | strength: statutory
obligated(provider, national_competent_authorities, confirm_to_authorities) :-
    time_period(three_months).

% atom_id: 14310be3f631d54b | chunk: 349a10bd74774e76 | strength: statutory
obligated(deployer, none, not_obligated) :-
    activity_type(purely_personal_non_professional).

% atom_id: 6716a2d70f1f1e3f | chunk: 35f7a55801fb136f | strength: statutory
obligated(provider, authorised_representative, perform_tasks_specified_in_mandate).

% atom_id: 8b9ac7598e49efe7 | chunk: 370b66d0cfe6dc4d | strength: statutory
obligated(provider, ai_system, take_corrective_action) :-
    status(made_available_on_union_market).

% atom_id: 00207387f994c5b9 | chunk: 372bdb9b61afa1d2 | strength: statutory
obligated(provider, logs, maintain) :-
    risk_class(high),
    institution_type(financial_institution).

% atom_id: 72f37805a64a0966 | chunk: 373dab9ede9bb4ab | strength: statutory
obligated(commission, none, update_guidelines) :-
    request(member_states_or_ai_office),
    initiative(own).

% atom_id: e60bfc0007b00107 | chunk: 376c93bf53cb027b | strength: statutory
obligated(market_surveillance_authority, none, approve_testing_in_real_world_conditions) :-
    testing_location(member_state).

% atom_id: 7335ebe3103f0b86 | chunk: 376c93bf53cb027b | strength: statutory
obligated(market_surveillance_authority, none, respond_within_30_days) :-
    testing_location(member_state).

% atom_id: 1521cf4001edf0c3 | chunk: 376c93bf53cb027b | strength: statutory
obligated(provider, none, understand_approval_as_given) :-
    market_surveillance_authority_response(no_answer_within_30_days),
    testing_location(member_state).

% atom_id: 503bf11d2e7aec67 | chunk: 376c93bf53cb027b | strength: statutory
obligated(provider, none, remain_subject_to_authorisation) :-
    national_law(no_tacit_approval),
    testing_location(member_state).

% atom_id: bb626d924dabec7f | chunk: 380e2c23cf8908f2 | strength: statutory
obligated(notified_body, providers, inform_within_10_days) :-
    designation_status(suspended_restricted_fully_or_partially_withdrawn).

% atom_id: c24ce1d0078884f9 | chunk: 38690bc3f0064ff8 | strength: statutory
obligated(commission, none, adopt_delegated_acts) :-
    evidence(concrete_and_reliable),
    necessity(necessary_to_maintain_protection).

% atom_id: e49540219c7f020b | chunk: 38ada1d299c3de1d | strength: statutory
obligated(market_surveillance_authority, national_public_authorities_or_bodies, inform_of_serious_incident) :-
    notification_received(serious_incident).

% atom_id: f099d677fa48f5a3 | chunk: 38ada1d299c3de1d | strength: statutory
obligated(commission, non_state_actors, develop_dedicated_guidance) :-
    date(n2_august_2025).

% atom_id: c56e5306ca72e444 | chunk: 38ada1d299c3de1d | strength: statutory
obligated(commission, non_state_actors, regularly_assess_guidance) :-
    date(none).

% atom_id: d0aab616eaf80a82 | chunk: 38da36d6aa68c40a | strength: statutory
obligated(notified_body, relevant_authorities, issue_certificates_in_understandable_language).

% atom_id: 12dd7bb66dc48bdd | chunk: 3a7205377b6e1e84 | strength: statutory
permitted(advisory_forum, none, prepare_opinions_recommendations_contributions).

% atom_id: 6603752bf348a8d3 | chunk: 3b056c49a8e5ea0a | strength: statutory
obligated(union_institution_body_office_or_agency, general_budget_of_the_union, receive_funds).

% atom_id: c94dc0d11f3b3ff9 | chunk: 3b056c49a8e5ea0a | strength: statutory
prohibited(fines_imposer, union_institution_body_office_or_agency, affect_effective_operation).

% atom_id: 345020ff29a3150d | chunk: 3b0e5bbff3b4997f | strength: statutory
obligated(management_and_staff, none, ensure_accountability).

% atom_id: 3860cb1a2a675ae6 | chunk: 3ba451b27830c234 | strength: statutory
obligated(board, none, compose_of_representatives).

% atom_id: 61ea2199f6ac10c4 | chunk: 3ba451b27830c234 | strength: statutory
obligated(european_data_protection_supervisor, none, participate_as_observer).

% atom_id: c47c4dadb5c90cc7 | chunk: 3ba451b27830c234 | strength: statutory
obligated(ai_office, none, attend_meetings_without_voting).

% atom_id: 3fe31497c8a5f725 | chunk: 3ba451b27830c234 | strength: statutory
permitted(board, national_and_union_authorities_bodies_or_experts, be_invited_to_meetings) :-
    issues_discussed(relevance_for_them).

% atom_id: f500dbc9b6602712 | chunk: 3d29ab9d8ce13ec9 | strength: statutory
obligated(notifying_authority, files_of_notified_body, keep_and_make_available) :-
    event(restriction_suspension_or_withdrawal_of_designation).

% atom_id: 086f82d3db0b8db9 | chunk: 3d442c3837fd96a0 | strength: statutory
obligated(distributor, high_risk_ai_system, ensure_compliance_storage_transport) :-
    responsibility(under_distributor).

% atom_id: 9296718d045307b6 | chunk: 3d7b36584cb77f2b | strength: statutory
obligated(provider, ai_system, understand_capacities_and_limitations).

% atom_id: a0e72b30e10d9446 | chunk: 3d7b36584cb77f2b | strength: statutory
obligated(provider, ai_system, monitor_operation).

% atom_id: 7f44e582056656b4 | chunk: 3d7b36584cb77f2b | strength: statutory
obligated(provider, ai_system, detect_and_address_anomalies_dysfunctions).

% atom_id: 989f4d848adb1f83 | chunk: 3e0d4cc85ed10151 | strength: statutory
permitted(provider_or_prospective_provider, high_risk_ai_system, conduct_real_world_testing) :-
    risk_class(high),
    testing_location(real_world_conditions).

% atom_id: 21f7c5eed3086b7c | chunk: 3e0d4cc85ed10151 | strength: statutory
obligated(commission, implementing_acts, specify_real_world_testing_plan).

% atom_id: d3724ad45b2e77f3 | chunk: 3e542b4eb7910613 | strength: statutory
obligated(market_surveillance_authority, none, deem_authorisation_justified) :-
    time_period(n15_calendar_days),
    objection_status(no_objection).

% atom_id: cac36cb709e1fdfc | chunk: 3ed7ba0b85bee918 | strength: statutory
obligated(deployer, logs, keep_logs) :-
    risk_class(high),
    control(under_their).

% atom_id: cfb219f899c8791a | chunk: 3ed7ba0b85bee918 | strength: statutory
obligated(deployer, logs, maintain_logs) :-
    financial_institution(true),
    governance_requirements(union_financial_services_law).

% atom_id: 32d61cbc2f2623c6 | chunk: 3ee8e0492d33a5cf | strength: statutory
obligated(manufacturer, high_risk_ai_system, put_into_service_under_name_ortrademark) :-
    risk_class(high).

% atom_id: f637368185ad0bbf | chunk: 3f8af564732a7a63 | strength: statutory
permitted(competent_authority, none, facilitate_consistency_and_coordination).

% atom_id: f6b7f696bf94b50c | chunk: 3f8af564732a7a63 | strength: statutory
permitted(competent_authority, none, collect_data_and_information).

% atom_id: f56b393be848179e | chunk: 3f8c4d7fe1363957 | strength: statutory
obligated(market_surveillance_authority, non_compliant_ai_system, notify_details) :-
    notification(referred_in_paragraph_5).

% atom_id: 18756f5c0c718166 | chunk: 3fb8f23722282267 | strength: statutory
obligated(provider, ai_system, integrate_necessary_elements) :-
    risk_class(high),
    legislation(union_harmonisation_legislation_listed_in_section_a_of_annex).

% atom_id: 1ce85d645502bcc4 | chunk: 3fb8f23722282267 | strength: statutory
obligated(provider, ai_system, use_template) :-
    risk_class(high),
    legislation(union_harmonisation_legislation_listed_in_section_a_of_annex).

% atom_id: 2b73e378a5cbe5d3 | chunk: 3fb8f23722282267 | strength: statutory
obligated(financial_institution, ai_system, integrate_necessary_elements) :-
    risk_class(high),
    legislation(union_financial_services_law_regarding_internal_governance_a).

% atom_id: 05cff4b7af77cb9a | chunk: 3fb8f23722282267 | strength: statutory
obligated(financial_institution, ai_system, use_template) :-
    risk_class(high),
    legislation(union_financial_services_law_regarding_internal_governance_a).

% atom_id: 0886a659fcf11c45 | chunk: 3fd927e9ea7409d0 | strength: statutory
obligated(law_enforcement_authority, real_time_remote_biometric_identification_system, deploy_for_specific_purpose) :-
    use_case(publicly_accessible_spaces),
    purpose(law_enforcement).

% atom_id: b8cd0d84925df8c6 | chunk: 3fd927e9ea7409d0 | strength: statutory
obligated(law_enforcement_authority, real_time_remote_biometric_identification_system, comply_with_safeguards_and_conditions) :-
    use_case(publicly_accessible_spaces),
    purpose(law_enforcement).

% atom_id: 0183b420daf89146 | chunk: 3fd927e9ea7409d0 | strength: statutory
obligated(law_enforcement_authority, real_time_remote_biometric_identification_system, complete_fundamental_rights_impact_assessment) :-
    use_case(publicly_accessible_spaces),
    purpose(law_enforcement).

% atom_id: 08d0b13274956112 | chunk: 3fd927e9ea7409d0 | strength: statutory
obligated(law_enforcement_authority, real_time_remote_biometric_identification_system, register_in_eu_database) :-
    use_case(publicly_accessible_spaces),
    purpose(law_enforcement).

% atom_id: 7ddf7e7cb9c119d8 | chunk: 3fd927e9ea7409d0 | strength: statutory
permitted(law_enforcement_authority, real_time_remote_biometric_identification_system, deploy_without_registration) :-
    use_case(publicly_accessible_spaces),
    purpose(law_enforcement),
    urgency(duly_justified).

% atom_id: 81cc0facee91d52d | chunk: 3fe1636bdafaa44d | strength: statutory
obligated(provider, competent_authority, provide_access_to_logs) :-
    request_reasoned(true),
    authority_competent(true).

% atom_id: 1af7c48462abf1b9 | chunk: 4140249a028193c6 | strength: statutory
obligated(authorities, none, have_adequate_personnel).

% atom_id: 5bf31459458eb7b5 | chunk: 4140249a028193c6 | strength: statutory
obligated(competent_personnel, none, have_necessary_expertise) :-
    function(information_technologies_ai_law).

% atom_id: d7729aee128a9612 | chunk: 42bd9873e63a46b5 | strength: statutory
obligated(provider_of_high_risk_ai_system_and_third_party, provider_of_high_risk_ai_system, specify_necessary_information_capabilities_technical_access) :-
    risk_class(high).

% atom_id: 8dfdb2628b23d391 | chunk: 43128a87bd352d4f | strength: statutory
obligated(competent_authority, none, establish_sandbox_environment).

% atom_id: c8ed7642bcc3ed3a | chunk: 43128a87bd352d4f | strength: statutory
obligated(provider_or_prospective_provider, none, agree_sandbox_plan).

% atom_id: a337966f80ddd20d | chunk: 43128a87bd352d4f | strength: statutory
obligated(provider_or_prospective_provider, innovative_ai_system, develop_train_test_validate).

% atom_id: aeeb74b0f2f32a9a | chunk: 4436d9f62520ba3e | strength: statutory
obligated(notified_body, other_notified_bodies, provide_information) :-
    activity(conformity_assessment),
    type(similar),
    ai_systems(same_types).

% atom_id: 011119da35fd3f61 | chunk: 455ac1dbdfb25780 | strength: statutory
obligated(provider, ai_system, comply_with_obligations_set_out_in_article) :-
    type_of_ai_model(general_purpose),
    licensing(free_and_open_source),
    public_availability(parameters_and_information_publicly_available),
    systemic_risks(present_systemic_risks).

% atom_id: 38d831f19b4f71fb | chunk: 455ac1dbdfb25780 | strength: statutory
prohibited(provider, ai_system, comply_with_obligations_set_out_in_article) :-
    type_of_ai_model(general_purpose),
    licensing(free_and_open_source),
    public_availability(parameters_and_information_publicly_available),
    systemic_risks(not_present_systemic_risks).

% atom_id: 8ab24a057186aee5 | chunk: 459231de8cda2037 | strength: statutory
obligated(prospective_provider, none, receive_pre_deployment_services) :-
    regulatory_sandbox(yes),
    type_of_entity(sme_start_up).

% atom_id: 82237f49476420fc | chunk: 4598fd0ddbfe7284 | strength: statutory
permitted(notified_body, none, use_documents_and_certificates).

% atom_id: f8a88d479f2930c4 | chunk: 4598fd0ddbfe7284 | strength: statutory
obligated(notified_body, none, update_documentation) :-
    relevant_changes(article_31_requirements).

% atom_id: 155a15ad11956eaf | chunk: 45a87a5c739b30cb | strength: statutory
obligated(market_surveillance_authority, none, inform_commission_and_member_states) :-
    not evaluation_result(restricted_to_national_territory).

% atom_id: ec954df5096b4bf9 | chunk: 45cff1f64aac47f1 | strength: statutory
obligated(market_surveillance_authorities, commission_and_relevant_national_competition_authorities, report_annually) :-
    time_period(annually).

% atom_id: f23e43b0f3cab41b | chunk: 45cff1f64aac47f1 | strength: statutory
obligated(market_surveillance_authorities, commission, report_annually) :-
    time_period(annually).

% atom_id: edbc8f08a74bbd8d | chunk: 45cff1f64aac47f1 | strength: statutory
obligated(market_surveillance_authorities, national_competition_authorities, report_annually) :-
    time_period(annually).

% atom_id: e930ee626ec630c1 | chunk: 46a01cab4a3d84c6 | strength: statutory
obligated(provider, natural_persons, inform_of_ai_interaction) :-
    interaction_context(direct_with_ai_system).

% atom_id: 10a54c10c74690b7 | chunk: 46a01cab4a3d84c6 | strength: statutory
prohibited(provider, obligation, inform_of_ai_interaction) :-
    interaction_context(direct_with_ai_system),
    law_authorization(detect_prevent_investigate_or_prosecute_criminal_offences).

% atom_id: 673996c2aead09cc | chunk: 46bdb406efaa664c | strength: statutory
obligated(ai_office, none, receive_information_and_documentation) :-
    request_reasoned(true).

% atom_id: 15769d70cf1eafb3 | chunk: 471eede1f2f73ad9 | strength: statutory
permitted(commission_and_member_states, none, exchange_confidential_information) :-
    context(necessary),
    agreements(relevant_provisions_of_international_and_trade_agreements).

% atom_id: 08334f8fcc7c0bc3 | chunk: 488a5ea670b0616e | strength: statutory
prohibited(public_authority_in_a_third_country, none, use_ai_systems_without_safeguards) :-
    context(international_cooperation_or_agreements_for_law_enforcement).

% atom_id: 470dff4f0d3a3e8f | chunk: 49fecc03e75ebf82 | strength: statutory
obligated(law_enforcement_authorities, personal_data_in_ai_regulatory_sandboxes, process_based_on_specific_law) :-
    purpose(prevention_investigation_detection_or_prosecution_of_crimina).

% atom_id: 49f1d4e740bce9a8 | chunk: 4ac6ce637a619aff | strength: statutory
prohibited(provider, ai_system, be_considered_high_risk) :-
    risk_class(not_high_risk),
    harm(significant).

% atom_id: 4d7ec2c38df3cf54 | chunk: 4ac6ce637a619aff | strength: statutory
prohibited(provider, ai_system, be_considered_high_risk) :-
    risk_class(high_risk),
    profiling(true).

% atom_id: e854e9cc00b99e06 | chunk: 4bb91b3b897d90ec | strength: statutory
obligated(provider, deployer, provide_ai_system_for_human_oversight) :-
    risk_class(high).

% atom_id: 9117275fd3add86f | chunk: 4bea2143b184cb47 | strength: statutory
obligated(commission, none, enter_into_consultation) :-
    national_measures(taken).

% atom_id: 68626cb663c151cb | chunk: 4bea2143b184cb47 | strength: statutory
obligated(commission, none, evaluate_national_measures) :-
    national_measures(taken).

% atom_id: fd0e63c501a974b2 | chunk: 4bea2143b184cb47 | strength: statutory
obligated(commission, none, decide_on_measure) :-
    evaluation_results(justified).

% atom_id: 2911328132ee2ffc | chunk: 4bea2143b184cb47 | strength: statutory
obligated(commission, none, propose_other_measures) :-
    decided_necessity(necessary).

% atom_id: a988378f35080a6f | chunk: 4c11946e48cda331 | strength: statutory
obligated(commission, none, investigate_competence) :-
    reasons_to_doubt(competence_of_notified_body_or_continued_fulfilment).

% atom_id: ac692f7a789ceac3 | chunk: 4c434ddebad6a232 | strength: statutory
obligated(ai_office, ai_system, monitor_and_supervise_compliance) :-
    model_developer(same_provider),
    system_type(based_on_general_purpose_ai_model).

% atom_id: 9d80369ea3b6ad5f | chunk: 4c9000fc05aa36dc | strength: statutory
obligated(provider, high_risk_ai_system, affix_ce_marking) :-
    risk_class(high),
    other_union_law(applicable).

% atom_id: 1044b765d7eb0a2a | chunk: 4caac8a249360c03 | strength: statutory
obligated(provider, technical_documentation, contain_required_information) :-
    risk_class(high),
    product_category(section_a_of_annex_i).

% atom_id: 6dc0306deceb3282 | chunk: 4f2f2f2a7025ae2e | strength: statutory
obligated(provider, ai_system, avoid_evaluation_classification) :-
    social_score(X_0), X_0 > 0,
    period_of_time(certain).

% atom_id: d4da405f2cc0c00f | chunk: 4f802f874af91dbc | strength: statutory
obligated(distributor, relevant_competent_authority, provide_information_and_documentation) :-
    request(reasoned_request).

% atom_id: daf7559ab18eac0a | chunk: 4f9cfb57dfd2e483 | strength: statutory
obligated(provider, national_competent_authorities, provide_information) :-
    status(suspension_or_withdrawal).

% atom_id: 133b1d73e9569072 | chunk: 4f9cfb57dfd2e483 | strength: statutory
obligated(national_competent_authorities, non_specified, take_appropriate_measures) :-
    risk(health_safety_fundamental_rights).

% atom_id: 17a907f1e1a2b250 | chunk: 5053dad28341f039 | strength: statutory
obligated(provider, high_risk_ai_system, provide_relevant_information) :-
    risk_class(high).

% atom_id: 9dd75c604a83008a | chunk: 50b8cae261022f30 | strength: statutory
obligated(provider_or_prospective_provider, third_party, liable_for_damage).

% atom_id: 2b741c355392be3d | chunk: 512335948cea90cd | strength: statutory
obligated(commission, none, publish_list_of_general_purpose_ai_models_with_systemic_risk).

% atom_id: fa78e77b6322fb5e | chunk: 512335948cea90cd | strength: statutory
obligated(commission, none, keep_list_up_to_date).

% atom_id: 43157730d4fd9846 | chunk: 526dba556f04b1f7 | strength: statutory
obligated(commission, public, make_publicly_available).

% atom_id: 736ec5fd320fc214 | chunk: 526dba556f04b1f7 | strength: statutory
obligated(commission, list_of_bodies_notified, keep_up_to_date).

% atom_id: 64272c69c3025757 | chunk: 5310afea2e8530ec | strength: statutory
obligated(advisory_forum, public, prepare_annual_report).

% atom_id: 5befded2fda90104 | chunk: 5310afea2e8530ec | strength: statutory
obligated(advisory_forum, public, make_report_publicly_available).

% atom_id: 277e31ea332c1b39 | chunk: 536eb098ca065c5a | strength: statutory
obligated(provider, none, adopt_risk_management_measures) :-
    risk_class(identified_pursuant_to_point_a).

% atom_id: 86b940a7f75e14d1 | chunk: 5394e27d01501f42 | strength: statutory
obligated(commission, none, encourage_development_of_benchmarks_and_methods) :-
    context(cooperation_with_stakeholders).

% atom_id: 2241f65df3625f91 | chunk: 53d05d27f5757895 | strength: statutory
obligated(deployer, subject_of_testing, provide_informed_consent) :-
    testing_context(real_world_conditions).

% atom_id: 4f4b287cba38d75c | chunk: 53dd921f94ec49b5 | strength: statutory
obligated(market_surveillance_authority, none, inform_commission_and_member_states) :-
    non_compliance(not_restricted_to_national_territory).

% atom_id: 895ca7813be3e455 | chunk: 53fcc0b08eb30702 | strength: statutory
obligated(provider, ai_system, test_in_real_world_conditions) :-
    risk_class(high).

% atom_id: 0a0a0216eb0d6f0f | chunk: 5407a232fad809c8 | strength: statutory
obligated(market_surveillance_authorities, product_or_ai_system, take_restrictive_measures).

% atom_id: 8dd619f8c9c5014b | chunk: 54bb3841654537c0 | strength: statutory
obligated(provider, commission, notify_without_delay) :-
    general_purpose_ai_model(meets_condition_in_article_51_1_a).

% atom_id: f240d933efdd8524 | chunk: 54bb3841654537c0 | strength: statutory
obligated(commission, none, decide_to_designate_model) :-
    general_purpose_ai_model(presenting_systemic_risks),
    notification_status(received).

% atom_id: d94625d7acf37059 | chunk: 553ab525eb1f0f05 | strength: statutory
obligated(commission, market_surveillance_authority_of_relevant_member_state_and_o, enter_into_consultation) :-
    timeframe(within_three_months).

% atom_id: 8f9d10df2886ff3b | chunk: 553ab525eb1f0f05 | strength: statutory
obligated(commission, national_measure, evaluate) :-
    timeframe(within_six_months).

% atom_id: bea59746f6197bae | chunk: 553ab525eb1f0f05 | strength: statutory
obligated(commission, national_measure, decide_on_justification) :-
    timeframe(within_sixty_days).

% atom_id: 1bedc84b00095f47 | chunk: 553ab525eb1f0f05 | strength: statutory
obligated(commission, market_surveillance_authority_of_member_state_concerned, notify_decision) :-
    timeframe(within_sixty_days).

% atom_id: 1f562a3446282d7d | chunk: 553ab525eb1f0f05 | strength: statutory
obligated(commission, other_market_surveillance_authorities, inform_decision) :-
    timeframe(within_sixty_days).

% atom_id: 46726882abd4fbaa | chunk: 5544cac6e3dba6b3 | strength: statutory
obligated(provider, high_risk_ai_system, enable_logging_capabilities) :-
    risk_class(high).

% atom_id: 88fee15bee0b39df | chunk: 556e7fe9cf4906c8 | strength: statutory
obligated(provider_of_general_purpose_ai_model_or_its_representative, none, supply_information).

% atom_id: b7fb23201ed4c9af | chunk: 556e7fe9cf4906c8 | strength: statutory
obligated(persons_authorized_to_represent_legal_persons_by_law_or_stat, none, provide_access_on_behalf_of_provider).

% atom_id: 1187a80e58337159 | chunk: 55943cb957f2b60a | strength: statutory
obligated(provider, none, notify_authority) :-
    testing_status(suspension_or_termination),
    testing_status(final_outcomes).

% atom_id: a11f214f5b4f5677 | chunk: 55e61712626d4f8d | strength: statutory
obligated(commission, none, exchange_knowledge_and_best_practices).

% atom_id: b69e2225fa2479ee | chunk: 574dc606bbb95e8e | strength: statutory
obligated(member_states, national_competent_authorities, report_on_status_of_resources_and_assessment) :-
    time_period(by_2_august_2025).

% atom_id: a331748063bb4d1e | chunk: 574dc606bbb95e8e | strength: statutory
obligated(member_states, national_competent_authorities, report_on_status_of_resources_and_assessment) :-
    time_period(every_two_years_after_2025).

% atom_id: 4ddf0af30efa161e | chunk: 574dc606bbb95e8e | strength: statutory
obligated(commission, board, transmit_information_for_discussion_and_recommendations) :-
    time_period(upon_receiving_reports).

% atom_id: d42132a778cdfc67 | chunk: 574f1702e4dcfdce | strength: statutory
obligated(notifying_authority, none, notify_restriction_suspension_or_withdrawal) :-
    event(restriction_suspension_or_withdrawal_of_a_designation).

% atom_id: 8671be2b24e7629b | chunk: 57aafb7b87442a83 | strength: statutory
obligated(notifying_authority, none, keep_documents_disposable).

% atom_id: 40b3c9d7477fac6b | chunk: 58503cd769194e85 | strength: statutory
prohibited(deployer, ai_practice, implement_prohibited_practices).

% atom_id: 5e4d50e1848b97ef | chunk: 5886debdc358b18f | strength: statutory
obligated(commission, none, supervise_and_enforce).

% atom_id: 32288c391fe6ff21 | chunk: 5886debdc358b18f | strength: statutory
obligated(commission, ai_office, implement_tasks).

% atom_id: 7a6491f2c7818868 | chunk: 58a26198615f29c3 | strength: statutory
obligated(commission, none, adopt_implementing_acts).

% atom_id: 1ea34df9fa3dcbc3 | chunk: 58be7fcbfd1baf56 | strength: statutory
obligated(deployer, natural_persons, verify_and_confirm_identification) :-
    risk_class(high),
    system_usage(law_enforcement_or_migration).

% atom_id: 7c475512c7438c0f | chunk: 58be7fcbfd1baf56 | strength: statutory
obligated(deployer, natural_persons, verify_and_confirm_identification) :-
    risk_class(high),
    system_usage(law_enforcement_or_migration).

% atom_id: b6918b746b234885 | chunk: 5915361568b1fa68 | strength: statutory
obligated(member_states, competent_authorities, allocate_resources).

% atom_id: a60846c82fd7336c | chunk: 5915361568b1fa68 | strength: statutory
permitted(national_competent_authorities, other_actors, involve_in_ai_ecosystem).

% atom_id: 21da05c4c9b286bf | chunk: 5915361568b1fa68 | strength: statutory
prohibited(this_article, other_regulatory_sandboxes, affecting).

% atom_id: bfce2cdd303a1a99 | chunk: 5915361568b1fa68 | strength: statutory
obligated(member_states, authorities_supervising_other_sandboxes_and_national_compete, ensure_cooperation).

% atom_id: bd7b512254e47c39 | chunk: 5a0f9e8567d499fa | strength: statutory
permitted(law_enforcement_authorities_or_civil_protection_authorities, high_risk_ai_system, put_into_service_without_authorisation) :-
    situation(duly_justified_urgency_for_exceptional_reasons_of_public_sec),
    threat(specific_substantial_and_imminent_threat_to_life_or_physical).

% atom_id: ccfb5a20ce4ba63c | chunk: 5a0f9e8567d499fa | strength: statutory
obligated(authorities, high_risk_ai_system, request_authorisation_during_or_after_use) :-
    use(without_authorisation).

% atom_id: 83d5577dee937ab6 | chunk: 5a0f9e8567d499fa | strength: statutory
obligated(authorities, high_risk_ai_system, stop_use_with_immediate_effect) :-
    authorisation(refused).

% atom_id: 419570208b881da6 | chunk: 5a0f9e8567d499fa | strength: statutory
obligated(authorities, results_and_outputs_of_use, discard_immediately) :-
    authorisation(refused).

% atom_id: 40f439ac9a50139c | chunk: 5a57031ad5880277 | strength: statutory
obligated(deployer, none, comply_with_registration_obligations) :-
    risk_class(high),
    entity_type(public_authority_or_union_institution).

% atom_id: f27e646b1852e603 | chunk: 5a57031ad5880277 | strength: statutory
prohibited(deployer, none, use_high_risk_ai_system) :-
    risk_class(high),
    registration_status(registered_in_eu_database).

% atom_id: b30312f2828dbb43 | chunk: 5a57031ad5880277 | strength: statutory
obligated(deployer, none, inform_provider_or_distributor) :-
    risk_class(high),
    registration_status(registered_in_eu_database).

% atom_id: ab39a7ef82fdb2c5 | chunk: 5a6f69e27dee0853 | strength: statutory
obligated(provider_or_prospective_provider, none, conduct_testing_in_real_world_conditions) :-
    location_of_provider(union).

% atom_id: 7142056d71f839af | chunk: 5a6f69e27dee0853 | strength: statutory
obligated(provider_or_prospective_provider, none, appoint_legal_representative_established_in_union) :-
    location_of_representative(union).

% atom_id: f6b906afb8f5efcc | chunk: 5a7c9b873f888e67 | strength: statutory
obligated(provider, natural_person, interpret_output_correctly) :-
    risk_class(high).

% atom_id: 28414d90aad5875d | chunk: 5abe5d2ada68b2f4 | strength: statutory
obligated(authorised_representative, none, perform_tasks_specified_in_mandate).

% atom_id: 1f6a209dfe23caeb | chunk: 5abe5d2ada68b2f4 | strength: statutory
obligated(authorised_representative, market_surveillance_authorities, provide_copy_of_mandate) :-
    request(yes).

% atom_id: 3a2de4d02f3fd48b | chunk: 5abe5d2ada68b2f4 | strength: statutory
obligated(authorised_representative, competent_authorities, be_addressed) :-
    issues(related_to_compliance).

% atom_id: f23cba9c9b1b57a6 | chunk: 5ac654f3deee12b8 | strength: statutory
obligated(provider, post_market_monitoring_system, be_based_on_plan).

% atom_id: 418e5e6ace7494da | chunk: 5ac654f3deee12b8 | strength: statutory
obligated(provider, post_market_monitoring_plan, be_part_of_technical_documentation).

% atom_id: 2a6a0ffe3bd28b36 | chunk: 5ac654f3deee12b8 | strength: statutory
obligated(commission, implementing_act, be_adopted).

% atom_id: e455c53ef3a159a9 | chunk: 5b0327e7aae338e4 | strength: statutory
obligated(data_controller, data_processed, be_necessary_for_compliance) :-
    requirement(chapter_iii_section_2_requirements).

% atom_id: 02ef7f8a4320b160 | chunk: 5b280a255c23ce3a | strength: statutory
prohibited(national_competent_authorities, none, affect_supervisory_powers) :-
    context(ai_regulatory_sandboxes).

% atom_id: 0d0488ae59bf4c2b | chunk: 5b280a255c23ce3a | strength: statutory
obligated(national_competent_authorities, ai_systems, mitigate_significant_risks) :-
    risk_category(health_and_safety),
    risk_category(fundamental_rights).

% atom_id: 8175fe55e0f7ae53 | chunk: 5b280a255c23ce3a | strength: statutory
permitted(national_competent_authorities, none, suspend_testing_process) :-
    context(ai_regulatory_sandboxes),
    condition(no_effective_mitigation).

% atom_id: 5c665850e4ae1e0a | chunk: 5b280a255c23ce3a | strength: statutory
permitted(national_competent_authorities, none, inform_ai_office) :-
    context(ai_regulatory_sandboxes),
    condition(suspension_of_testing_process).

% atom_id: 4fed5efe89eda840 | chunk: 5b280a255c23ce3a | strength: statutory
obligated(national_competent_authorities, none, exercise_supervisory_powers) :-
    context(ai_regulatory_sandboxes).

% atom_id: e48d8e64094d9680 | chunk: 5b280a255c23ce3a | strength: statutory
permitted(national_competent_authorities, none, implement_legal_provisions_discretely) :-
    context(ai_regulatory_sandboxes).

% atom_id: 336df074cc9d1bf8 | chunk: 5b470b993e8d835a | strength: statutory
prohibited(data_controller, data_subject, processing_data_affecting_rights) :-
    context(sandbox).

% atom_id: 886dcc629300d929 | chunk: 5b805520b71cb1a4 | strength: statutory
obligated(provider, third_party, remain_liable_for_damage) :-
    experimentation_context(ai_regulatory_sandbox).

% atom_id: 3ca222a54d2f6103 | chunk: 5b805520b71cb1a4 | strength: statutory
prohibited(authorities, none, impose_administrative_fines) :-
    provider_behavior(observing_specific_plan_and_terms),
    good_faith(true).

% atom_id: 4a11abaa500efbd4 | chunk: 5b805520b71cb1a4 | strength: statutory
prohibited(authorities, none, impose_administrative_fines) :-
    other_authorities_involvement(true),
    compliance_guidance_provided(true).

% atom_id: a7b3f88445920df8 | chunk: 5ba6a380111788cd | strength: statutory
obligated(provider, ai_office_and_national_competent_authorities, keep_copy_of_technical_documentation_disposable) :-
    time_period(n10_years),
    event(general_purpose_ai_model_placed_on_market).

% atom_id: 48f460bbf0ba1a7a | chunk: 5ba6a380111788cd | strength: statutory
obligated(provider, authorised_representative, provide_contact_details_disposable) :-
    event(general_purpose_ai_model_placed_on_market).

% atom_id: b2e201f61883f3ec | chunk: 5c7156565e865a44 | strength: statutory
obligated(provider, high_risk_ai_system, notify_serious_incidents) :-
    risk_class(high),
    legislative_instrument(union_legislative_instruments_laying_down_reporting_obligati).

% atom_id: a66fe450c9999ae4 | chunk: 5d8dd3351922fdfc | strength: statutory
obligated(commission, none, consult_experts) :-
    act_type(delegated).

% atom_id: 93fb2f10485a6f96 | chunk: 5da3c8a82b22af5f | strength: statutory
obligated(public_authority_or_other_natural_or_legal_person, ai_system, develop_for_public_interest) :-
    area(public_safety_and_public_health_high_level_of_protection_and).

% atom_id: 2e8383c60ff1d6b6 | chunk: 5e1ad75f92aa0692 | strength: statutory
obligated(authority, information_or_documentation, treat_confidentially).

% atom_id: ef04cbb0358893dc | chunk: 5e1f270d944f5cc5 | strength: statutory
permitted(member_state, none, provide_authorization) :-
    system_type(real_time_remote_biometric_identification_systems),
    location(publicly_accessible_spaces),
    purpose(law_enforcement).

% atom_id: 8b771a56403046f8 | chunk: 5e1f270d944f5cc5 | strength: statutory
obligated(member_state, national_law, lay_down_detailed_rules) :-
    authorizations(referred_to_in_paragraph_3).

% atom_id: b6d42e27b46f0191 | chunk: 5e1f270d944f5cc5 | strength: statutory
obligated(member_state, national_law, specify_authorization_conditions) :-
    objectives(listed_in_paragraph_1_first_subparagraph_point_h).

% atom_id: b21a65f5d04fbfe7 | chunk: 5e1f270d944f5cc5 | strength: statutory
obligated(member_state, national_law, specify_criminal_offenses) :-
    objectives(listed_in_paragraph_1_first_subparagraph_point_h).

% atom_id: 989a63141b6fec1a | chunk: 5e1f270d944f5cc5 | strength: statutory
obligated(member_state, national_law, lay_down_supervision_and_reporting_rules) :-
    authorizations(referred_to_in_paragraph_3).

% atom_id: 5554209c27c7c81d | chunk: 5e1f270d944f5cc5 | strength: statutory
obligated(member_state, commission, notify_rules) :-
    rules(adopted).

% atom_id: 2e5224a78f845907 | chunk: 5e1f270d944f5cc5 | strength: statutory
permitted(member_state, none, introduce_more_restrictive_laws) :-
    system_type(remote_biometric_identification_systems).

% atom_id: 93ebb7ff9a4ab28a | chunk: 5f55de9f2a536ae8 | strength: statutory
obligated(provider_of_general_purpose_ai_model_or_its_representative, none, supply_information).

% atom_id: d3d9f19a66df3d42 | chunk: 5f55de9f2a536ae8 | strength: statutory
obligated(persons_authorized_to_represent_legal_persons_by_law_or_stat, none, supply_information_on_behalf_of_provider).

% atom_id: 8e3b8bf9ef76c6f9 | chunk: 5f55de9f2a536ae8 | strength: statutory
obligated(lawyers_duly_authorized_to_act, none, supply_information_on_behalf_of_clients).

% atom_id: 6de50e357464cb7c | chunk: 5f55de9f2a536ae8 | strength: statutory
obligated(clients, none, remain_responsible_for_information_supplied).

% atom_id: e2111c986ee9dbfa | chunk: 5fea6e06377fe274 | strength: statutory
obligated(deployer, monitoring_mechanism, identify_risks) :-
    risk_class(high),
    context(sandbox_experiementation).

% atom_id: 7d67df3160356498 | chunk: 5fea6e06377fe274 | strength: statutory
obligated(deployer, risk_mitigation_mechanism, mitigate_risks) :-
    risk_class(high),
    context(sandbox_experiementation).

% atom_id: 8f0608deb27fa51c | chunk: 5fea6e06377fe274 | strength: statutory
obligated(deployer, processing, stop_processing) :-
    risk_class(high),
    context(sandbox_experiementation).

% atom_id: 9c694e2d9f603365 | chunk: 60e252867f58e584 | strength: statutory
obligated(authority, none, take_appropriate_measures).

% atom_id: 72c8d168c5a69420 | chunk: 61148ad74b51a867 | strength: statutory
obligated(importer, none, keep_records) :-
    time_period(n10_years),
    event(high_risk_ai_system_placed_on_market_or_put_into_service).

% atom_id: ec683d35c680bc16 | chunk: 615a22c1ecd3f176 | strength: statutory
permitted(commission, none, designate_ai_model) :-
    model_type(general_purpose),
    risk_level(systemic).

% atom_id: 3407c94643279fca | chunk: 615a22c1ecd3f176 | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    basis(article_97).

% atom_id: 0c6b90a84adddaf0 | chunk: 621442610b5d5d4d | strength: statutory
obligated(distributor, high_risk_ai_system, not_make_available_on_market) :-
    conformity(not_in_conformity),
    information(considered_reason_to_consider).

% atom_id: 9e7daacb4ba520fa | chunk: 621442610b5d5d4d | strength: statutory
obligated(distributor, provider_or_importer, inform_of_non_conformity) :-
    risk(within_meaning_of_article_791).

% atom_id: 963a0c362c42644c | chunk: 6229707b8316dcf8 | strength: statutory
obligated(ai_office_and_member_states, none, encourage_facilitate_code_of_conduct).

% atom_id: 67d0d31af97d4644 | chunk: 62ed51f6b91283bd | strength: statutory
obligated(board, none, be_chaired_by_representative).

% atom_id: 1ca1ea2a0db7056b | chunk: 62ed51f6b91283bd | strength: statutory
obligated(ai_office, board, provide_secretariat).

% atom_id: 8b1fa159624ad7b9 | chunk: 62ed51f6b91283bd | strength: statutory
obligated(ai_office, board, convene_meetings) :-
    request(chair).

% atom_id: 9c59f0be5d85bd40 | chunk: 62ed51f6b91283bd | strength: statutory
obligated(ai_office, board, prepare_agenda) :-
    tasks(pursuant_to_this_regulation_and_its_rules_of_procedure).

% atom_id: 6a277e11349806c1 | chunk: 632762b3fef8a209 | strength: statutory
obligated(commission, none, develop_guidelines) :-
    regulation_context(practical_implementation).

% atom_id: 2534e5022b05d015 | chunk: 632762b3fef8a209 | strength: statutory
obligated(commission, none, pay_attention_to_needs) :-
    target_groups(sme_startups_local_public_authorities_affected_sectors).

% atom_id: 6f72b561ecf55917 | chunk: 63b03c7bf4af1ebc | strength: statutory
permitted(commission, none, adopt_delegated_acts).

% atom_id: 8bd33f74830bebf3 | chunk: 63b03c7bf4af1ebc | strength: statutory
obligated(commission, none, draw_up_report) :-
    time_period(nine_months_before_end_of_five_year_period).

% atom_id: 4693411ce3877802 | chunk: 63b03c7bf4af1ebc | strength: statutory
obligated(commission, none, tacitly_extend_power) :-
    time_period(each_period).

% atom_id: 43bca20a808b1d3c | chunk: 658ab0af364b4947 | strength: statutory
obligated(national_competent_authorities, none, inform_ai_office_and_board).

% atom_id: d513cf165532d55d | chunk: 658ab0af364b4947 | strength: statutory
permitted(national_competent_authorities, none, ask_for_support_and_guidance).

% atom_id: 0413a40ce7284eae | chunk: 658ab0af364b4947 | strength: statutory
obligated(ai_office, none, make_list_publicly_available_and_update).

% atom_id: 354e262c9ab5997c | chunk: 65b223f86bfad824 | strength: statutory
obligated(deployer, ai_system, request_authorisation_ex_ante) :-
    risk_class(high),
    context(post_remote_biometric_identification_for_targeted_search_of).

% atom_id: 88a8d280b2f451ff | chunk: 65b223f86bfad824 | strength: statutory
obligated(deployer, ai_system, limit_use_to_strictly_necessary) :-
    risk_class(high),
    context(post_remote_biometric_identification_for_targeted_search_of).

% atom_id: 1229b9a4624f5b39 | chunk: 65b223f86bfad824 | strength: statutory
obligated(deployer, post_remote_biometric_identification_system, stop_use_and_delete_data) :-
    risk_class(high),
    context(post_remote_biometric_identification_for_targeted_search_of),
    authorisation_status(granted).

% atom_id: 666093c0012959a6 | chunk: 65b223f86bfad824 | strength: statutory
prohibited(deployer, post_remote_biometric_identification_system, use_in_untargeted_way) :-
    risk_class(high),
    context(post_remote_biometric_identification_for_targeted_search_of).

% atom_id: c5f235230afc083a | chunk: 65b223f86bfad824 | strength: statutory
prohibited(law_enforcement_authority, person, take_adverse_legal_effect_decision_based_on_output) :-
    risk_class(high),
    context(post_remote_biometric_identification_system).

% atom_id: b6e79cbaeae2e228 | chunk: 65b223f86bfad824 | strength: statutory
obligated(deployer, relevant_police_file, document_use) :-
    risk_class(high),
    context(post_remote_biometric_identification_system).

% atom_id: 385787d7f601985d | chunk: 65b223f86bfad824 | strength: statutory
obligated(deployer, relevant_market_surveillance_authority_and_national_data_pro, make_reports_available) :-
    risk_class(high),
    context(post_remote_biometric_identification_system).

% atom_id: e2c934d6cc4fe368 | chunk: 65b223f86bfad824 | strength: statutory
obligated(deployer, relevant_market_surveillance_authority_and_national_data_pro, submit_annual_reports) :-
    risk_class(high),
    context(post_remote_biometric_identification_system).

% atom_id: beb3853b597f4e7c | chunk: 660462e1dbfe8f75 | strength: statutory
obligated(national_competent_authorities, national_data_protection_authorities_and_other_national_or_c, associate_with_ai_sandbox_operation) :-
    system_characteristics(processing_of_personal_data_supervisory_remit).

% atom_id: 7917a326403c3189 | chunk: 660462e1dbfe8f75 | strength: statutory
obligated(national_competent_authorities, national_data_protection_authorities_and_other_national_or_c, involve_in_supervision) :-
    system_characteristics(processing_of_personal_data_supervisory_remit).

% atom_id: b306e0be72a6dbc4 | chunk: 661c7238a9b95c4d | strength: statutory
obligated(commission, none, apply_procedure) :-
    national_measure(justified),
    non_compliance(attributed_to_shortcomings_in_harmonised_standards_or_common).

% atom_id: e6340d7fa4ab6925 | chunk: 67297c9c5f4ca3e3 | strength: statutory
permitted(member_states, none, call_upon_experts).

% atom_id: 2d2ea06343185fcd | chunk: 673febd1fce5ec92 | strength: statutory
obligated(provider, none, limit_testing_duration).

% atom_id: 70d2c1e2ca1efff0 | chunk: 673febd1fce5ec92 | strength: statutory
obligated(provider, none, extend_testing_duration) :-
    extension_request(true),
    notification(prior).

% atom_id: 611886cac3444c9a | chunk: 67e0c3ad0af72696 | strength: statutory
obligated(provider, instructions_of_use, declare_accuracy_levels_and_metrics) :-
    risk_class(high).

% atom_id: b8433e282fd4fe33 | chunk: 688dfa79d97a5039 | strength: statutory
obligated(provider, ai_system, facilitate_inclusive_design).

% atom_id: 43b4aea596b9643c | chunk: 68b089abe6725742 | strength: statutory
obligated(european_data_protection_supervisor, union_institutions_bodies_offices_or_agencies, act_as_market_surveillance_authority) :-
    scope(this_regulation).

% atom_id: e439789334bcb8b3 | chunk: 68b089abe6725742 | strength: statutory
obligated(union_institutions_bodies_offices_or_agencies, market, be_subject_to_market_surveillance) :-
    scope(this_regulation).

% atom_id: d31cc439b66ea980 | chunk: 6900ffee20f18dc9 | strength: statutory
permitted(provider, none, conduct_testing).

% atom_id: 79b22216b227c0e6 | chunk: 6900ffee20f18dc9 | strength: statutory
permitted(prospective_provider, none, conduct_testing).

% atom_id: 5a9c124159fced15 | chunk: 691eff47d7906080 | strength: statutory
obligated(authorities, none, request_data) :-
    data_necessity(strictly_necessary).

% atom_id: f18fd6fa57e9af82 | chunk: 691eff47d7906080 | strength: statutory
obligated(authorities, none, implement_cybersecurity_measures) :-
    data_security(adequate_and_effective).

% atom_id: 8a54246b295512c4 | chunk: 691eff47d7906080 | strength: statutory
obligated(authorities, none, delete_data) :-
    data_relevance(no_longer_needed).

% atom_id: 21a6d87029497c86 | chunk: 69524cc79993b6f5 | strength: statutory
obligated(market_surveillance_authority, ai_system, evaluate_compliance) :-
    risk_class(high).

% atom_id: 32bbcd42fdd57837 | chunk: 69524cc79993b6f5 | strength: statutory
obligated(market_surveillance_authority, vulnerable_groups, give_attention) :-
    risk_class(high).

% atom_id: 4051dbea25613d0d | chunk: 69524cc79993b6f5 | strength: statutory
obligated(market_surveillance_authority, relevant_national_public_authorities_or_bodies, inform_and_cooperate) :-
    risk_class(high),
    fundamental_rights(identified).

% atom_id: 667e029ea1f2d30d | chunk: 69524cc79993b6f5 | strength: statutory
obligated(relevant_operators, market_surveillance_authority_and_other_national_public_auth, cooperate) :-
    risk_class(high).

% atom_id: 5842afcc0a9f294e | chunk: 69524cc79993b6f5 | strength: statutory
obligated(market_surveillance_authority, relevant_operator, require_corrective_actions) :-
    risk_class(high),
    compliance_status(non_compliant).

% atom_id: 2f1ee36b0c16f624 | chunk: 69524cc79993b6f5 | strength: statutory
obligated(market_surveillance_authority, ai_system, withdraw_or_recall) :-
    risk_class(high),
    compliance_status(non_compliant).

% atom_id: 8111644091436a01 | chunk: 6961098aff9863fc | strength: statutory
obligated(provider, ai_system, bring_into_compliance).

% atom_id: c274b3be954c1a0e | chunk: 6961098aff9863fc | strength: statutory
obligated(provider, provider, pay_fines).

% atom_id: 37936e34cf19ace2 | chunk: 69fdbfb9b0b03411 | strength: statutory
obligated(authorised_representative, provider, terminate_mandate) :-
    consideration(acting_contrary_to_obligations).

% atom_id: 1c7c5bc485838644 | chunk: 6a4206e85d025907 | strength: statutory
obligated(commission, none, carry_out_assessment_and_report) :-
    date(n2_august_2031).

% atom_id: 9c370d8c6661064c | chunk: 6d34e01e87b967ff | strength: statutory
obligated(data_controller, special_categories_of_personal_data, delete) :-
    bias_status(corrected),
    retention_period(end).

% atom_id: 1d1a8bc17a38479f | chunk: 6d79dba4a648019b | strength: statutory
obligated(provider, high_risk_ai_system, integrate_measures_technically_feasible) :-
    risk_class(high),
    technical_feasibility(feasible).

% atom_id: 5109bfd06c41e970 | chunk: 7007eccd7f5fc3ef | strength: statutory
obligated(national_competent_authorities, ai_office_and_board, submit_annual_reports).

% atom_id: a21fb68be1050641 | chunk: 7007eccd7f5fc3ef | strength: statutory
obligated(national_competent_authorities, public, make_reports_public).

% atom_id: fa22812634f7264d | chunk: 7007eccd7f5fc3ef | strength: statutory
obligated(commission, itself, consider_reports).

% atom_id: 95efb707e8239a5a | chunk: 7057ab7808f58484 | strength: statutory
obligated(member_state, none, inform_commission) :-
    common_specification(does_not_entirely_meet_requirements),
    section_2_or_applicable_obligations(set_out_in_section_2_or_comply_with_obligations_set_out_in_s).

% atom_id: b554561bd87aee4d | chunk: 7057ab7808f58484 | strength: statutory
obligated(commission, none, assess_information_and_amend_implementing_act) :-
    information_from_member_state(provided).

% atom_id: 6ca48897c5dc1baf | chunk: 711db56d508b71da | strength: statutory
obligated(provider, ai_system, design_for_human_oversight) :-
    risk_class(high).

% atom_id: c4c8217e83416411 | chunk: 7334668793d41b08 | strength: statutory
obligated(provider, ai_system, detect_prevent_mitigate_biases) :-
    bias_identified(point_f).

% atom_id: 008f5280a917852f | chunk: 735ed63e1b03054e | strength: statutory
obligated(deployer_or_prospective_deployer, none, be_informed_and_given_instructions) :-
    testing_context(real_world).

% atom_id: aa3bfc28a372eff5 | chunk: 735ed63e1b03054e | strength: statutory
obligated(provider_or_prospective_provider_deployer_or_prospective_dep, none, conclude_agreement) :-
    testing_context(real_world).

% atom_id: 8d46ab37a8adf9dd | chunk: 740848e4b2118dc9 | strength: statutory
obligated(provider, ai_system, be_resilient) :-
    risk_class(high).

% atom_id: 52e7c96d21f4607e | chunk: 740848e4b2118dc9 | strength: statutory
obligated(provider, technical_solutions, be_appropriate) :-
    risk_class(high).

% atom_id: d85c49ab0b87e343 | chunk: 740848e4b2118dc9 | strength: statutory
obligated(provider, technical_solutions, include_measures) :-
    vulnerability_type(data_poisoning_model_poisoning_adversarial_examples_confiden).

% atom_id: 79c7b2c83dee54f7 | chunk: 7441ac75f5126ef5 | strength: statutory
obligated(deployer, high_risk_ai_system, carry_out_data_protection_impact_assessment) :-
    risk_class(high).

% atom_id: 3b9850f516a15e57 | chunk: 750eb9d9b6b4e43b | strength: statutory
prohibited(supplier, notified_body_or_national_competent_authority, supply_incorrect_information).

% atom_id: 56cb6257acacae20 | chunk: 75ab84aa27126817 | strength: statutory
obligated(ai_office_and_board, none, ensure_clear_objectives).

% atom_id: 1f3a58fd5512b894 | chunk: 75ab84aa27126817 | strength: statutory
obligated(ai_office_and_board, none, include_commitments_or_measures).

% atom_id: 5be1481db3f7ca43 | chunk: 75ab84aa27126817 | strength: statutory
obligated(ai_office_and_board, none, take_due_account_of_interests).

% atom_id: 466028d17320773c | chunk: 762453ccf6af1ead | strength: statutory
obligated(authority, generalpurpose_ai_model_developers_placers_users, assess_and_mitigate_systemic_risks) :-
    risk_class(systemic).

% atom_id: 9d9c346bd9e33d18 | chunk: 76ccc3d175c53cca | strength: statutory
obligated(commission, none, provide_guidelines) :-
    consultation(european_artificial_intelligence_board),
    date(X_1), X_1 >= 2.

% atom_id: c5eacc2dd40efc84 | chunk: 77bf2d412ffabd97 | strength: statutory
obligated(commission, none, publish_annual_reports) :-
    system_type(real_time_remote_biometric_identification_systems),
    use_case(publicly_accessible_spaces_for_law_enforcement_purposes).

% atom_id: ffcbb9e2285f0d5d | chunk: 77bf2d412ffabd97 | strength: statutory
prohibited(commission, none, include_sensitive_data) :-
    system_type(real_time_remote_biometric_identification_systems),
    use_case(publicly_accessible_spaces_for_law_enforcement_purposes).

% atom_id: 1925aca46e8b7a49 | chunk: 77fae2a7ceddcba5 | strength: statutory
obligated(provider, ai_system, understand_as_product_presenting_risk) :-
    risk(health_or_safety),
    risk(fundamental_rights).

% atom_id: 7db49899487904ac | chunk: 78483b278cf8eff2 | strength: statutory
prohibited(other_parties, special_categories_of_personal_data, transmit_or_transfer).

% atom_id: 328d3d882df865f3 | chunk: 7851775ab4b2c1c6 | strength: statutory
obligated(supervisor, commission, notify_of_fines_and_lawsuits).

% atom_id: 5aa5287fd95a8b7c | chunk: 7900694b7b15d7d2 | strength: statutory
obligated(provider, high_risk_ai_system, identify_measures).

% atom_id: 514369511e8fffc0 | chunk: 7900694b7b15d7d2 | strength: statutory
obligated(deployer, high_risk_ai_system, implement_measures).

% atom_id: dd6aa76f157d7850 | chunk: 796632e654804617 | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    technical_progress(necessary).

% atom_id: e3d187554c93c9dc | chunk: 79691fde4d96bf94 | strength: statutory
obligated(provider, high_risk_ai_system, comply_with_requirements) :-
    risk_class(high).

% atom_id: 93955b0842223966 | chunk: 79691fde4d96bf94 | strength: statutory
obligated(provider, risk_management_system, be_considered) :-
    requirement_compliance(true).

% atom_id: a7144b115387b716 | chunk: 7986ee728847de3f | strength: statutory
obligated(distributor_importer_deployer_other_third_party, high_risk_ai_system, be_provider).

% atom_id: 06893f475167bea8 | chunk: 7986ee728847de3f | strength: statutory
obligated(provider, high_risk_ai_system, comply_with_obligations_of_provider).

% atom_id: 56e594a032fedc89 | chunk: 798bd30eeded78c0 | strength: statutory
obligated(provider, none, apply_common_specifications) :-
    common_specifications_exist(true).

% atom_id: 3ca9bb8e4e4daf46 | chunk: 7a568961bce24fa0 | strength: statutory
obligated(authority, none, ensure_consistency_and_protection) :-
    amendment(to_conditions_in_paragraph_3_second_subparagraph).

% atom_id: f8aa56ada2ea4d53 | chunk: 7a61e78be9d47c4e | strength: statutory
permitted(commission, none, adopt_delegated_acts).

% atom_id: 05ec62de20bc03b2 | chunk: 7a84db7adc6451eb | strength: statutory
prohibited(provider, ai_system, process_biometric_data) :-
    purpose(law_enforcement),
    regulation(eu_2016679).

% atom_id: 47aefc3a5f83a3fc | chunk: 7b1091878a406c34 | strength: statutory
permitted(member_state, none, identify_authority) :-
    circumstances(appropriate),
    coordination(ensured).

% atom_id: dadb793ac321e745 | chunk: 7b1091878a406c34 | strength: statutory
obligated(national_market_surveillance_authority, european_central_bank, report_information) :-
    information(specified_prudential_supervisory_tasks).

% atom_id: db891cfda997a476 | chunk: 7b775e45c26493de | strength: statutory
obligated(provider, ai_system, consider_high_risk) :-
    placement_on_market_or_service(yes),
    risk_conditions_fulfilled(true).

% atom_id: d6be0397f191e629 | chunk: 7c6b36010c92a366 | strength: statutory
obligated(national_competent_authorities, none, agree_terms_and_conditions) :-
    testing_context(real_world_conditions_supervised_within_ai_regulatory_sandbo).

% atom_id: e7cda7731cadb994 | chunk: 7c6b36010c92a366 | strength: statutory
obligated(national_competent_authorities, none, cooperate_with_other_authorities) :-
    testing_context(real_world_conditions_supervised_within_ai_regulatory_sandbo).

% atom_id: 0f10316bda0e108a | chunk: 7c83c640721857e2 | strength: statutory
permitted(commission, none, exercise_powers) :-
    qualified_alert(present).

% atom_id: 8ca26c98aaf67845 | chunk: 7d67cd2db0f28c2e | strength: statutory
obligated(authority, none, consider_regulatory_requirements) :-
    delegated_act(safety_components).

% atom_id: a4447bcdba75ae14 | chunk: 7d93d19f23929e8f | strength: statutory
obligated(provider, market_surveillance_authorities, report_incident) :-
    risk_class(high),
    incident_severity(serious).

% atom_id: 735093a1406abe6f | chunk: 7e7db1f39b3772a6 | strength: statutory
obligated(provider_or_deployer, report, provide_immediately) :-
    death_of_person(true),
    causal_relationship_established(true).

% atom_id: 45b7b3e5048b82e3 | chunk: 7e7db1f39b3772a6 | strength: statutory
obligated(provider_or_deployer, report, provide_within_10_days) :-
    death_of_person(true),
    causal_relationship_suspected(true).

% atom_id: 21914dd2f8b011ce | chunk: 7ea1834706fbf61d | strength: statutory
obligated(provider, logs, keep_for_duration) :-
    context(sandbox_processing_of_personal_data).

% atom_id: b2e6ad0436544327 | chunk: 7fb4cedd96809ba6 | strength: statutory
obligated(provider, ai_system, achieve_appropriate_accuracy) :-
    risk_class(high).

% atom_id: 4615dd71506570b1 | chunk: 7fb4cedd96809ba6 | strength: statutory
obligated(provider, ai_system, achieve_appropriate_robustness) :-
    risk_class(high).

% atom_id: c0a3a4fd2a44c66d | chunk: 7fb4cedd96809ba6 | strength: statutory
obligated(provider, ai_system, achieve_appropriate_cybersecurity) :-
    risk_class(high).

% atom_id: b26b8bc1730c0481 | chunk: 7fb4cedd96809ba6 | strength: statutory
obligated(provider, ai_system, perform_consistently_across_lifecycle) :-
    risk_class(high).

% atom_id: 28fdfac4bc14acad | chunk: 7fec512ebdb18e00 | strength: statutory
permitted(provider, none, submit_incomplete_report) :-
    context(timely_reporting).

% atom_id: c6e5e9942b25a0b6 | chunk: 7fec512ebdb18e00 | strength: statutory
permitted(deployer, none, submit_incomplete_report) :-
    context(timely_reporting),
    applicability(where_applicable).

% atom_id: a563b1d733a2e02d | chunk: 8078329d9c32e913 | strength: statutory
obligated(notifying_authority, commission, provide_information) :-
    request(on_request).

% atom_id: ddbd5a4398a195f7 | chunk: 816203ce163ca7f9 | strength: statutory
obligated(commission, none, adopt_implementing_acts).

% atom_id: 6de4b9cb53ab0027 | chunk: 8169259640a68f42 | strength: statutory
obligated(provider, ai_system, ensure_proper_functioning) :-
    risk_class(high).

% atom_id: f151812875f9726f | chunk: 8169259640a68f42 | strength: statutory
obligated(provider, ai_system, provide_computational_resources) :-
    risk_class(high).

% atom_id: 28dfa53b8c9285e8 | chunk: 8169259640a68f42 | strength: statutory
obligated(provider, ai_system, provide_hardware_resources) :-
    risk_class(high).

% atom_id: 0f8901eefe99b2b4 | chunk: 8169259640a68f42 | strength: statutory
obligated(provider, ai_system, ensure_expected_lifetime) :-
    risk_class(high).

% atom_id: a5190419df9be0d8 | chunk: 8169259640a68f42 | strength: statutory
obligated(provider, ai_system, perform_maintenance_and_care_measures) :-
    risk_class(high).

% atom_id: 32e3dd64b4009e8d | chunk: 8169259640a68f42 | strength: statutory
obligated(provider, ai_system, update_software) :-
    risk_class(high).

% atom_id: c2e2aa18a1ede046 | chunk: 83d152de14a6e4ac | strength: statutory
obligated(provider, high_risk_ai_system, affix_ce_marking_visibly).

% atom_id: 64a668a601b955c3 | chunk: 83d152de14a6e4ac | strength: statutory
obligated(provider, high_risk_ai_system, affix_ce_marking_on_packaging_or_documentation) :-
    nature_of_system(not_possible_or_not_warranted).

% atom_id: 1b6a5d6695b1f38f | chunk: 83d5386a865c9c9e | strength: statutory
obligated(provider, national_competent_authority, receive_notification) :-
    risk_class(high),
    device_type(safety_component_of_devices_devices).

% atom_id: 81871ecfb94d22ad | chunk: 840a3b388aba44af | strength: statutory
obligated(market_surveillance_authorities, ai_system, verify_compliance) :-
    testing_context(real_world_conditions),
    supervision_context(ai_regulatory_sandbox).

% atom_id: a14f72d718579990 | chunk: 840a3b388aba44af | strength: statutory
permitted(market_surveillance_authorities, provider_or_prospective_provider, conduct_real_world_testing) :-
    testing_context(real_world_conditions),
    supervision_context(ai_regulatory_sandbox).

% atom_id: ba7aa7c5967d8b8c | chunk: 840a81f7dbd9c19e | strength: statutory
prohibited(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(law_enforcement),
    space(publicly_accessible_spaces),
    necessity(targeted_search_for_specific_victims_of_abduction_traffickin).

% atom_id: abb17397e2620145 | chunk: 840a81f7dbd9c19e | strength: statutory
permitted(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(targeted_search_for_specific_victims_of_abduction),
    space(publicly_accessible_spaces).

% atom_id: 37034fb786a4d5c4 | chunk: 840a81f7dbd9c19e | strength: statutory
permitted(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(trafficking_in_human_beings_or_sexual_exploitation),
    space(publicly_accessible_spaces).

% atom_id: c3042205ac59d0fd | chunk: 840a81f7dbd9c19e | strength: statutory
permitted(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(search_for_missing_persons),
    space(publicly_accessible_spaces).

% atom_id: 26c1aaceedf32b86 | chunk: 840a81f7dbd9c19e | strength: statutory
permitted(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(prevention_of_specific_substantial_and_imminent_threat_to_li),
    space(publicly_accessible_spaces).

% atom_id: 2c7a382c36957b47 | chunk: 840a81f7dbd9c19e | strength: statutory
permitted(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(genuine_and_present_or_foreseeable_threat_of_terrorist_attac),
    space(publicly_accessible_spaces).

% atom_id: d7994cf125a7609c | chunk: 840a81f7dbd9c19e | strength: statutory
permitted(authority, ai_system, use_real_time_remote_biometric_identification) :-
    purpose(localisation_or_identification_of_a_person_suspected_of_havi),
    space(publicly_accessible_spaces),
    purpose(conducting_a_criminal_investigation_or_punishment).

% atom_id: 383b021045cb8b77 | chunk: 8452d070fbf91baa | strength: statutory
obligated(provider, natural_persons_concerned, receive_clear_and_distinguishable_information) :-
    interaction_or_exposure(first).

% atom_id: ae6a608bee24e446 | chunk: 8452d070fbf91baa | strength: statutory
obligated(provider, information, conform_to_applicable_accessibility_requirements).

% atom_id: 4c614bbf279c9223 | chunk: 8485a3f34e1dda1e | strength: statutory
obligated(notifying_authority, notified_body, investigate) :-
    sufficient_reason(considering_non_compliance).

% atom_id: 2d7b7f1b6ebc4222 | chunk: 8485a3f34e1dda1e | strength: statutory
obligated(notifying_authority, notified_body, restrict_suspend_or_withdraw_designation) :-
    conclusion(non_compliance).

% atom_id: 1e30d3162be73b2e | chunk: 85687252ed394466 | strength: statutory
permitted(deployer, high_risk_ai_system, decide_not_to_use_or_override_output).

% atom_id: 923466759589ea6a | chunk: 85af52c3865a3010 | strength: statutory
obligated(provider, none, implement_proportionate_measures) :-
    risk_class(high).

% atom_id: 7c507a0a88914844 | chunk: 85af52c3865a3010 | strength: statutory
obligated(provider, high_risk_ai_systems, ensure_compliance) :-
    risk_class(high).

% atom_id: ed286dd24c827af9 | chunk: 87b372e9db712417 | strength: statutory
obligated(authorities, none, ensure_balanced_membership) :-
    stakeholder_category(industry_start_ups_sme_civil_society_academia).

% atom_id: dab92be5408baa44 | chunk: 882f679fe6818ee3 | strength: statutory
obligated(provider, technical_documentation, draw_up_and_keep_updated).

% atom_id: 0ea4dc460115ff05 | chunk: 882f679fe6818ee3 | strength: statutory
obligated(provider, technical_documentation, contain_minimum_information).

% atom_id: da9ff32e91e0d8fd | chunk: 882f679fe6818ee3 | strength: statutory
obligated(provider, technical_documentation, provide_upon_request).

% atom_id: 6afb74778785cf78 | chunk: 88eaeeb08034ac09 | strength: statutory
obligated(provider, none, register_in_eu_database) :-
    risk_class(high),
    system_status(referred_to_point_2_of_annex_iii).

% atom_id: 729fc7cfb8cac02f | chunk: 88eaeeb08034ac09 | strength: statutory
obligated(authorised_representative, none, register_in_eu_database) :-
    risk_class(high),
    system_status(referred_to_point_2_of_annex_iii).

% atom_id: 08c0139d6e7ef171 | chunk: 892e8ef4f21684d3 | strength: statutory
obligated(member_states, notifying_authorities_and_market_surveillance_authorities, communicate_identity_and_tasks).

% atom_id: 593c3f1bb9d9f3d1 | chunk: 892e8ef4f21684d3 | strength: statutory
obligated(member_states, public, make_information_publicly_available) :-
    date(n2_august_2025).

% atom_id: 68f544c0fd5b0f9d | chunk: 892e8ef4f21684d3 | strength: statutory
obligated(member_states, single_point_of_contact_authority, act_as_single_point_of_contact).

% atom_id: 990a6b2907e9a433 | chunk: 892e8ef4f21684d3 | strength: statutory
obligated(member_states, commission, notify_identity_of_single_point_of_contact).

% atom_id: b9e018b67a1ad6bc | chunk: 892e8ef4f21684d3 | strength: statutory
obligated(commission, public, make_list_publicly_available).

% atom_id: ddcfacff85b08cdb | chunk: 896a58d4a95e2957 | strength: statutory
obligated(notified_body, provider, avoid_unnecessary_burdens) :-
    activity(performing).

% atom_id: 075c962aff5417ee | chunk: 896a58d4a95e2957 | strength: statutory
obligated(notified_body, provider, take_due_account_of_provider_characteristics) :-
    activity(performing),
    characteristic(size_sector_structure_degree_of_complexity).

% atom_id: 31b0a9c024fb172b | chunk: 896a58d4a95e2957 | strength: statutory
obligated(notified_body, high_risk_ai_system, respect_degree_of_rigour_and_level_of_protection) :-
    activity(compliance).

% atom_id: 97702b884267b715 | chunk: 89993771b0f1d78d | strength: statutory
obligated(affected_person, deployer, provide_explanations) :-
    decision(based_on_output_from_high_risk_ai_system),
    risk_class(high),
    annex(annex_iii),
    output(point_2_thereof),
    effect(produces_legal_effects_similarly_significantly_affects).

% atom_id: 7f59454c162f195a | chunk: 8aa145565cc10e0b | strength: statutory
obligated(provider, deployer, interpret_outputs) :-
    risk_class(high).

% atom_id: a111dc4046e4ecdc | chunk: 8ab56259a033a0d0 | strength: statutory
obligated(commission, none, adopt_implementing_acts).

% atom_id: 8944d711409f48ca | chunk: 8ae5792fcb186a43 | strength: statutory
obligated(provider_or_prospective_provider, high_risk_ai_system, register_testing_real_world_conditions) :-
    risk_class(high),
    areas(law_enforcement_migration_asylum_border_control_management).

% atom_id: d3d554ebbee49992 | chunk: 8ae5792fcb186a43 | strength: statutory
obligated(provider_or_prospective_provider, high_risk_ai_system, register_in_secure_non_public_section_eu_database) :-
    risk_class(high),
    areas(law_enforcement_migration_asylum_border_control_management).

% atom_id: 955fd9f9639a94dd | chunk: 8ae5792fcb186a43 | strength: statutory
obligated(provider_or_prospective_provider, high_risk_ai_system, register_testing_real_world_conditions) :-
    risk_class(high),
    areas(law_enforcement_migration_asylum_border_control_management).

% atom_id: 7cbbe0d31659a976 | chunk: 8c258f411f2f9572 | strength: statutory
obligated(provider, none, assume_responsibility_for_compliance).

% atom_id: 7edee615bdeaf74e | chunk: 8c258f411f2f9572 | strength: statutory
obligated(provider, none, keep_declaration_up_to_date).

% atom_id: e25f463324288e70 | chunk: 8d276ff95acb9e68 | strength: statutory
obligated(provider, high_risk_ai_system, aim_to_prevent_minimize_risks) :-
    risk_category(health_safety_fundamental_rights),
    use_context(intended_purpose_reasonably_foreseeable_misuse).

% atom_id: f1aeef64ad4bdf8e | chunk: 8d3d1931930257c2 | strength: statutory
obligated(notifying_authority, none, notify_changes).

% atom_id: 9d53ce9372dd1f1c | chunk: 8d4674f60995951b | strength: statutory
prohibited(provider, ai_system, use_for_risk_assessment) :-
    purpose(risk_assessment_of_natural_persons),
    basis(profiling_or_personality_traits).

% atom_id: f6b39d484fdeea34 | chunk: 8d4674f60995951b | strength: statutory
permitted(provider, ai_system, use_for_assessment_of_involvement) :-
    purpose(support_human_assessment),
    basis(objective_and_verifiable_facts).

% atom_id: 3637f220ce1ee50f | chunk: 8d87dab811a6a2c0 | strength: statutory
obligated(provider, high_risk_ai_system, use_digital_ce_marking) :-
    risk_class(high),
    system_type(digital).

% atom_id: 701ba9f923f01e55 | chunk: 8de93a254fdb8549 | strength: statutory
obligated(market_surveillance_authority, high_risk_ai_system, take_measures_to_restrict_or_prohibit) :-
    non_compliance(persists).

% atom_id: 147cf2641e73193f | chunk: 8de93a254fdb8549 | strength: statutory
obligated(market_surveillance_authority, high_risk_ai_system, ensure_recall_or_withdrawal_from_market) :-
    non_compliance(persists).

% atom_id: ba8b31ae2a7cefd7 | chunk: 8e266a345c416f25 | strength: statutory
obligated(european_data_protection_supervisor, union_institutions_bodies_offices_or_agencies, act_as_competent_authority_for_supervision).

% atom_id: ae5d000589d49f0c | chunk: 90b4c1ad2d6bcd85 | strength: statutory
obligated(notified_bodies, information, safeguard_confidentiality).

% atom_id: 9f290990a3e3baa1 | chunk: 90b70016c97144f1 | strength: statutory
permitted(commission, none, make_commitments_binding) :-
    structured_dialogue(referred_to_in_paragraph_2),
    provider(general_purpose_ai_model_with_systemic_risk),
    commitments(to_implement_mitigation_measures_to_address_a_systemic_risk).

% atom_id: e0e0e8393a8da2ad | chunk: 90b70016c97144f1 | strength: statutory
obligated(commission, none, declare_no_further_grounds_for_action) :-
    structured_dialogue(referred_to_in_paragraph_2),
    provider(general_purpose_ai_model_with_systemic_risk),
    commitments(to_implement_mitigation_measures_to_address_a_systemic_risk).

% atom_id: d69bdd960029e174 | chunk: 922edfdf4b489e83 | strength: statutory
obligated(notified_body, none, established_under_national_law).

% atom_id: bee0c69e412b4011 | chunk: 922edfdf4b489e83 | strength: statutory
obligated(notified_body, none, have_legal_personality).

% atom_id: 7b0a3412acfff711 | chunk: 9252600d1705c18d | strength: statutory
obligated(provider, public, make_publicly_available_summary).

% atom_id: c768462dc4dd912d | chunk: 929ea7223f84e88d | strength: statutory
obligated(market_surveillance_authority_of_a_member_state_or_commissio, operator, raise_objection_within_three_months) :-
    event(receipt_of_notification).

% atom_id: 6f07e2a192132e3d | chunk: 929ea7223f84e88d | strength: statutory
obligated(market_surveillance_authority_of_a_member_state_or_commissio, operator, take_provisional_measure) :-
    event(receipt_of_notification).

% atom_id: cc1d1685946c20ed | chunk: 929ea7223f84e88d | strength: statutory
obligated(market_surveillance_authority_of_a_member_state_or_commissio, operator, comply_with_prohibition) :-
    event(non_compliance).

% atom_id: 2d308c2a9bcfb991 | chunk: 92c60723199e1f14 | strength: statutory
obligated(notified_body, subcontractor_or_subsidiary, meet_requirements) :-
    task_type(conformity_assessment).

% atom_id: 80212168569342bf | chunk: 92da0eb766fa95e5 | strength: statutory
obligated(commission, none, assess_need_for_amendment) :-
    time_period(once_a_year),
    event(entry_into_force_of_this_regulation).

% atom_id: 97e601a29b85c364 | chunk: 92da0eb766fa95e5 | strength: statutory
obligated(commission, none, submit_findings_to_parliament_and_council) :-
    time_period(until_the_end_of_the_period).

% atom_id: c4d95edd8ad1640e | chunk: 92e9f50a101bf192 | strength: statutory
obligated(deployer, none, comply_with_transparency_obligations).

% atom_id: 1ab77d438ef64798 | chunk: 9307c38f1a6adcf0 | strength: statutory
obligated(commission, none, issue_decision) :-
    trigger(ex_officio_qualified_alert).

% atom_id: 8d4a793c8eae0e75 | chunk: 9307c38f1a6adcf0 | strength: statutory
obligated(scientific_panel, none, issue_alert) :-
    trigger(qualified).

% atom_id: b0f207726444ff92 | chunk: 93bdd57ac881e146 | strength: statutory
permitted(commission, none, appoint_independent_experts).

% atom_id: 6c434062ff1c798e | chunk: 93bdd57ac881e146 | strength: statutory
obligated(independent_experts, none, meet_criteria) :-
    appointment(for_this_task).

% atom_id: 63d668c38d2f0889 | chunk: 93bfdc2b021348c4 | strength: statutory
obligated(notified_bodies, none, take_full_responsibility).

% atom_id: 2419222305c1c3b5 | chunk: 942234f81a1d3f2b | strength: statutory
obligated(market_surveillance_authority, national_authority, be_responsible) :-
    risk_class(high),
    context(financial_institutions).

% atom_id: 60cae402876cf627 | chunk: 9486d39daa09d139 | strength: statutory
obligated(provider, product, ensure_compliance) :-
    risk_class(high),
    requirements_applicability(yes).

% atom_id: b93b965e143f92e5 | chunk: 94958f05a20fc662 | strength: statutory
obligated(commission_market_surveillance_authorities_notified_bodies_o, information_and_data, respect_confidentiality).

% atom_id: 0b6a06fd97593e16 | chunk: 9513799bdbd02f62 | strength: statutory
obligated(ai_office, none, encourage_and_facilitate_code_of_practice).

% atom_id: 0b443e193bb5f1a7 | chunk: 95b197a02687a3a9 | strength: statutory
obligated(provider, post_market_monitoring_system, set_up_implementation_maintenance).

% atom_id: bddf314c0fe9974f | chunk: 960474fe7814e6b4 | strength: statutory
permitted(ai_office, none, initiate_structured_dialogue) :-
    request(prior_to_accessing).

% atom_id: 7caeb0d401ab7eb1 | chunk: 972346e599e46a49 | strength: statutory
obligated(authorities, sme, provide_priority_access) :-
    registration_status(registered_office_or_branch_in_union),
    entity_type(start_ups).

% atom_id: a15d2c505602c4a6 | chunk: 972346e599e46a49 | strength: statutory
obligated(authorities, sme, ensure_access) :-
    registration_status(registered_office_or_branch_in_union),
    entity_type(start_ups).

% atom_id: a147e7ecff54dd60 | chunk: 972346e599e46a49 | strength: statutory
obligated(authorities, sme, ensure_access) :-
    registration_status(registered_office_or_branch_in_union),
    entity_type(start_ups).

% atom_id: 0f02bc84437c928c | chunk: 9761e1aa4943ef40 | strength: statutory
obligated(provider, none, provide_general_purpose_ai_models).

% atom_id: 04d207f84f6c20ae | chunk: 9791bbd8899350cd | strength: statutory
obligated(deployer, none, suspend_or_terminate_testing).

% atom_id: 0222f2bca5634110 | chunk: 9831f126be5fa5a8 | strength: statutory
obligated(authority, none, organise_communication_campaigns).

% atom_id: 70b4a7f9b454a87d | chunk: 9873b58df41f8409 | strength: statutory
obligated(commission, sensitive_information, treat_confidentially).

% atom_id: 4597a223970a62d6 | chunk: 98fc1234a3a4be91 | strength: statutory
obligated(requestor, none, state_legal_basis_and_purpose).

% atom_id: c7d36a7a78775f9d | chunk: 98fc1234a3a4be91 | strength: statutory
obligated(requestor, none, specify_required_information).

% atom_id: 1c6023ea32f1d4a8 | chunk: 98fc1234a3a4be91 | strength: statutory
obligated(requestor, none, set_provision_period).

% atom_id: f871dea8a25ac655 | chunk: 98fc1234a3a4be91 | strength: statutory
obligated(requestor, none, indicate_fines_for_incorrect_information).

% atom_id: 110d4776559e4057 | chunk: 99dff5f66b79fa8a | strength: statutory
obligated(market_surveillance_authorities, none, treat_information_confidentially).

% atom_id: 34a18c60809ddc1e | chunk: 99f67ddbb283e0f4 | strength: statutory
permitted(commission, none, adopt_delegated_acts).

% atom_id: 044fa6c16af6d851 | chunk: 9a1a35a8d509300f | strength: statutory
permitted(european_data_protection_supervisor, none, impose_administrative_fines) :-
    subject(union_institutions_bodies_offices_and_agencies).

% atom_id: 2bf5375f09dcad8a | chunk: 9a3099323d54ccd8 | strength: statutory
permitted(ai_office, none, initiate_structured_dialogue) :-
    not measure_status(requested).

% atom_id: 03d18584b273209b | chunk: 9ad265f1314d1af3 | strength: statutory
permitted(union_or_member_states, none, maintain_or_introduce_laws_regulations_admin_provisions).

% atom_id: 94297c693e716afa | chunk: 9ad265f1314d1af3 | strength: statutory
permitted(union_or_member_states, none, encourage_application_of_collective_agreements).

% atom_id: 1e1d603f822d965d | chunk: 9b5281c2249beb88 | strength: statutory
permitted(provider, generalpurpose_ai_model, present_substantiated_arguments) :-
    model_characteristics(specific_characteristics_systemic_risks),
    classification(general_purpose_ai_model_with_systemic_risk).

% atom_id: 217e64f72b04f0da | chunk: 9b707f1e1876bb9e | strength: statutory
obligated(advisory_forum, none, hold_meetings).

% atom_id: d21b4412700721a1 | chunk: 9b707f1e1876bb9e | strength: statutory
permitted(advisory_forum, none, invite_experts_and_stakeholders).

% atom_id: 853488e72376c798 | chunk: 9bafc239aa08c5a1 | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    list_in_annex(high_risk_ai_systems),
    conditions_fulfilled(both).

% atom_id: 9e186d025ec65c63 | chunk: 9c279d5c23c9a253 | strength: statutory
obligated(ai_office, non_state_actors, encourage_and_facilitate_code_of_practice).

% atom_id: c1ca8c4f8aa46f8d | chunk: 9c279d5c23c9a253 | strength: statutory
permitted(commission, non_state_actors, adopt_implementing_acts_to_approve_codes_of_practice).

% atom_id: 230446ee8a57d39d | chunk: 9c279d5c23c9a253 | strength: statutory
obligated(commission, non_state_actors, specify_common_rules_for_implementation_of_obligations) :-
    code_adequacy(inadequate).

% atom_id: b9e08be994c5dbc1 | chunk: 9c3c587b0a8aea0d | strength: statutory
obligated(provider, none, understand_ai_capabilities_and_limitations).

% atom_id: 98ad63f87e5d8c67 | chunk: 9c3c587b0a8aea0d | strength: statutory
obligated(provider, none, comply_with_obligations).

% atom_id: 58057388da71e0a0 | chunk: 9c72f8432fc4d10d | strength: statutory
obligated(provider, high_risk_ai_system, consider_adverse_impact) :-
    intended_purpose(likely_to_have_adverse_impact_on_persons_under_18_and_vulner).

% atom_id: 77ca65b063ec53d6 | chunk: 9c805b8a12863416 | strength: statutory
obligated(deployer, high_risk_ai_system, ensure_acceptable_risk_management_measures) :-
    risk_class(high).

% atom_id: 5a74f52517f55693 | chunk: 9c805b8a12863416 | strength: statutory
obligated(deployer, self, consider_technical_knowledge_and_experience) :-
    risk_class(high).

% atom_id: 59d9b789660f33ee | chunk: 9c805b8a12863416 | strength: statutory
obligated(deployer, self, consider_education_and_training) :-
    risk_class(high).

% atom_id: c0c29bfe6e9c7107 | chunk: 9c805b8a12863416 | strength: statutory
obligated(deployer, system_context, consider_presumable_context_of_use) :-
    risk_class(high).

% atom_id: b9ef4c15972b1745 | chunk: 9d2976417fcf533c | strength: statutory
obligated(product_manufacturer, high_risk_ai_system, provide_high_risk_ai_system) :-
    risk_class(high),
    component_of_product(safety_component),
    product_coverage(union_harmonisation_legislation_listed_in_section_a_of_attac).

% atom_id: 3ccd91fdbab85d39 | chunk: 9dfb577c2a23d056 | strength: statutory
obligated(court_of_justice_of_the_european_union, none, review_decisions).

% atom_id: f75830607d8556f3 | chunk: 9e45c55a73ee330a | strength: statutory
prohibited(authority, ai_system, subject_to_procedures) :-
    product_coverage(union_harmonisation_legislation_listed_in_section_a_of_annex),
    protection_level(equivalent_level_of_protection_and_having_the_same_objective).

% atom_id: f2dbf42e187a8558 | chunk: 9f00f70a6c8f4a45 | strength: statutory
obligated(commission, market_surveillance_authority_of_the_member_state_concerned, withdraw_authorisation) :-
    authorisation_status(unjustified).

% atom_id: 97e685b30f69ac36 | chunk: 9f54ce37bbd23219 | strength: statutory
obligated(provider, sme_startups_deployers_innovators_public_authorities, utilize_communication_channels).

% atom_id: 3c273707f51cd98b | chunk: 9f54ce37bbd23219 | strength: statutory
obligated(provider, sme_startups_deployers_innovators_public_authorities, establish_new_communication_channels) :-
    appropriateness(appropriate).

% atom_id: fc2806e54bf328a3 | chunk: 9f54ce37bbd23219 | strength: statutory
obligated(provider, sme_startups_deployers_innovators_public_authorities, provide_advice_and_response_queries).

% atom_id: 46858f71adefcbe8 | chunk: 9f54ce37bbd23219 | strength: statutory
obligated(provider, ai_regulatory_sandboxes, participation_advice) :-
    regulation(implementation).

% atom_id: 3696fa7d32127dd2 | chunk: a22f9db7c82213d6 | strength: statutory
obligated(prospective_provider, personal_data, process_in_isolated_environment) :-
    context(sandbox).

% atom_id: 4248f49bbf828b32 | chunk: a22f9db7c82213d6 | strength: statutory
obligated(authorised_persons, personal_data, have_access) :-
    context(sandbox).

% atom_id: 394078cfa9f54eb9 | chunk: a2c48de94b6f0a98 | strength: statutory
obligated(national_market_surveillance_authorities_and_national_data_p, commission, submit_reports) :-
    use_of_systems(real_time_remote_biometric_identification_systems_in_publicl).

% atom_id: e267b8248bee1547 | chunk: a2d11b7ccf11ff9a | strength: statutory
obligated(deployer, high_risk_ai_system, monitor_operation) :-
    risk_class(high).

% atom_id: 0a0af0af34c3f89e | chunk: a2d11b7ccf11ff9a | strength: statutory
obligated(deployer, none, inform_provider_and_authority_of_risk) :-
    risk_class(high),
    consideration(may_result_in_risk).

% atom_id: 18764fb1ac552b93 | chunk: a2d11b7ccf11ff9a | strength: statutory
obligated(deployer, none, inform_authorities_of_serious_incident) :-
    incident(serious).

% atom_id: d3f6140c68ad44a1 | chunk: a2d11b7ccf11ff9a | strength: statutory
obligated(deployer, none, inform_authorities_if_unable_to_reach_provider) :-
    communication(unreachable).

% atom_id: c7eea4794e008b90 | chunk: a2d11b7ccf11ff9a | strength: statutory
obligated(deployer, none, comply_with_internal_governance_requirements) :-
    financial_institution(true),
    governance_requirements(internal_governance_arrangements_processes).

% atom_id: 7c9ffba8a1f9c480 | chunk: a31b9425da14311e | strength: statutory
obligated(provider, high_risk_ai_system, take_corrective_actions) :-
    conformity_status(not_conforming).

% atom_id: 189a3c4155879cda | chunk: a31b9425da14311e | strength: statutory
obligated(provider, distributors_of_high_risk_ai_system, inform) :-
    conformity_status(not_conforming).

% atom_id: 02ddfdc3918d4209 | chunk: a31b9425da14311e | strength: statutory
obligated(provider, deployers, inform) :-
    conformity_status(not_conforming).

% atom_id: af6bda5c4d523029 | chunk: a31b9425da14311e | strength: statutory
obligated(provider, authorized_representative, inform) :-
    conformity_status(not_conforming).

% atom_id: cd4b824ec8b71505 | chunk: a31b9425da14311e | strength: statutory
obligated(provider, importers, inform) :-
    conformity_status(not_conforming).

% atom_id: bb518ba3d3bd0545 | chunk: a34c72cc263d7401 | strength: statutory
obligated(provider, commission_and_member_states, inform_about_certificates).

% atom_id: 260c391737de93ba | chunk: a4225334131d7619 | strength: statutory
obligated(provider, ai_system_or_model, be_in_conformity) :-
    risk_class(high),
    conformance(common_specifications).

% atom_id: daa467ac39063267 | chunk: a4b177fa8721a70c | strength: statutory
obligated(provider, ai_system_outputs, mark_as_artificially_generated) :-
    content_type(synthetic_audio_image_video_text).

% atom_id: 18db7725392da151 | chunk: a4b177fa8721a70c | strength: statutory
obligated(provider, technical_solutions, be_effective_interoperable_robust_reliable) :-
    content_type(synthetic_audio_image_video_text).

% atom_id: 248654a91f67f5f1 | chunk: a4b177fa8721a70c | strength: statutory
prohibited(provider, ai_system_outputs, not_be_marked_as_artificially_generated) :-
    content_type(synthetic_audio_image_video_text),
    function(assistive),
    input_data_alteration(substantial).

% atom_id: 9cbe1178e02702f2 | chunk: a4b177fa8721a70c | strength: statutory
prohibited(provider, ai_system_outputs, not_be_marked_as_artificially_generated) :-
    content_type(synthetic_audio_image_video_text),
    legal_authorization(yes).

% atom_id: d2737040c928077d | chunk: a4fd137ae56360a1 | strength: statutory
permitted(supervisor, none, establish_ai_regulatory_sandbox).

% atom_id: 37fdb67354281c89 | chunk: a4fd137ae56360a1 | strength: statutory
permitted(supervisor, union_institutions_bodies_offices_and_agencies, exercise_roles_and_tasks_of_national_competent_authorities).

% atom_id: 6d81266b6df9374e | chunk: a50a4ef952d54eb8 | strength: statutory
prohibited(deployer, ai_system, use_prohibited_practices).

% atom_id: 885ff3d6c2d4c265 | chunk: a54ac13bf06ce2be | strength: statutory
permitted(microenterprise, none, comply_with_simplified_qms) :-
    risk_class(not_high),
    partner_enterprises(no).

% atom_id: 9f8d86f25344e687 | chunk: a5c36e80972955eb | strength: statutory
obligated(provider_or_prospective_provider, national_market_surveillance_authority, report_incident) :-
    incident_severity(serious),
    testing_phase(real_world_conditions).

% atom_id: bbc233e3c761e749 | chunk: a5c36e80972955eb | strength: statutory
obligated(provider_or_prospective_provider, ai_system, adopt_mitigation_measures) :-
    incident_severity(serious),
    testing_phase(real_world_conditions).

% atom_id: 404c77269f6f5485 | chunk: a5c36e80972955eb | strength: statutory
obligated(provider_or_prospective_provider, testing_in_real_world_conditions, suspend_or_terminate) :-
    incident_severity(serious),
    testing_phase(real_world_conditions).

% atom_id: b7212fee706fe8bb | chunk: a5c36e80972955eb | strength: statutory
obligated(provider_or_prospective_provider, ai_system, establish_recall_procedure) :-
    testing_phase_termination(real_world_conditions).

% atom_id: 0a816a31e39bccb0 | chunk: a731e8aadb5a09a0 | strength: statutory
obligated(market_surveillance_authorities, providers, grant_full_access) :-
    risk_class(high),
    powers(regulation_eu_20191020).

% atom_id: ccd5b4eb9b3d2e05 | chunk: a752ca12981de796 | strength: statutory
obligated(manufacturer, none, place_on_market_or_put_into_service_with_product).

% atom_id: 5116b2391b5ae1d1 | chunk: a7bb2fb6e384f28c | strength: statutory
obligated(commission, none, select_experts) :-
    expertise(up_to_date_scientific_or_technical_expertise_in_the_field_of).

% atom_id: b99a35c8954b3779 | chunk: a7bb2fb6e384f28c | strength: statutory
obligated(commission, board, consult_board).

% atom_id: 3299884fb894f0eb | chunk: a7bb2fb6e384f28c | strength: statutory
obligated(commission, none, determine_number_of_experts) :-
    needs(required_needs).

% atom_id: 895ab44790913a14 | chunk: a7bb2fb6e384f28c | strength: statutory
obligated(commission, none, ensure_representation) :-
    gender(fair_gender_representation),
    geography(fair_geographical_representation).

% atom_id: fcdfeeff00b279de | chunk: a7df8a45890d8103 | strength: statutory
obligated(provider, data, transfer_to_third_countries) :-
    purpose(testing_in_real_world_conditions),
    safeguards(appropriate_and_applicable).

% atom_id: 5baf2323d44f40e6 | chunk: a86cc407c568d616 | strength: statutory
obligated(deployer, input_data, ensure_relevance_and_representation) :-
    control_exercise(yes).

% atom_id: eea19eef3d128dd7 | chunk: a8962be423fdd043 | strength: statutory
obligated(deployer, natural_person, remain_aware_of_automation_bias) :-
    risk_class(high).

% atom_id: 472adf2bede32f45 | chunk: a9f52c13597ea2ec | strength: statutory
obligated(market_surveillance_authority, provider, require_compliance_actions) :-
    risk_class(high).

% atom_id: 541ac0078e4157c4 | chunk: a9f52c13597ea2ec | strength: statutory
obligated(market_surveillance_authority, provider, prescribe_corrective_period) :-
    risk_class(high).

% atom_id: c8bd69ca7e637872 | chunk: aacf99dbed6da812 | strength: statutory
obligated(provider, competent_authority, provide_information_and_documentation) :-
    request(reasoned_request_by_a_competent_authority).

% atom_id: a11e7a68dff20d8e | chunk: ab31012b267ec69b | strength: statutory
obligated(provider, authorised_representative, perform_tasks_specified_in_mandate).

% atom_id: 975341a855231c87 | chunk: ac1f9d7e29e6b580 | strength: statutory
obligated(commission, none, designate_union_ai_testing_support_structures).

% atom_id: 15b137a73fce98f7 | chunk: ac3615f2ccc381c7 | strength: statutory
obligated(reporter, person_reporting_infringement, report_infringement).

% atom_id: bd74658dcaf549df | chunk: ac3615f2ccc381c7 | strength: statutory
obligated(authority, person_reporting_infringement, protect_person_reporting_infringement).

% atom_id: 46e7fcd37b6d5cb3 | chunk: acced7326b25e806 | strength: statutory
obligated(ai_regulatory_sandbox_operator, none, facilitate_involvement) :-
    actor_type(notified_bodies_standardisation_organisations_sme_startups_e).

% atom_id: 99ba759ac4bbe47d | chunk: ad1f718189ee55bb | strength: statutory
obligated(provider, ai_system_provider, draw_up_and_make_available_information).

% atom_id: cb29bb82130914f5 | chunk: ad1f718189ee55bb | strength: statutory
obligated(provider, ai_system_provider, keep_up_to_date_information_and_documentation).

% atom_id: e7a621de86c668c8 | chunk: ad1f718189ee55bb | strength: statutory
obligated(provider, ai_system_provider, make_available_information_and_documentation).

% atom_id: 2363cbd76df80354 | chunk: ad7ea70e78199a29 | strength: statutory
obligated(commission, none, inform_committee) :-
    draft_implementing_act_status(prepared).

% atom_id: c789eb390904eb01 | chunk: ad9e0806ea46055b | strength: statutory
obligated(authority, none, take_into_account_requirements) :-
    delegated_act(safety_components).

% atom_id: fe5e5fe084d20c71 | chunk: aea8f30d9f5ffdca | strength: statutory
permitted(commission, provider_of_a_general_purpose_ai_model, issue_request_for_information) :-
    request_origin(scientific_panel),
    request_duly_substantiated(true).

% atom_id: 9802c132624ccb11 | chunk: aecf39b843b1af15 | strength: statutory
obligated(market_surveillance_authority, commission_and_other_member_states, inform_of_measures_and_information) :-
    non_compliance(ai_system).

% atom_id: c0b8cb1435ad6acd | chunk: aecf39b843b1af15 | strength: statutory
obligated(market_surveillance_authority, commission_and_other_member_states, inform_of_objections) :-
    disagreement(notified_national_measure).

% atom_id: 91fcc4ca05926c92 | chunk: aefafe57d28654a9 | strength: statutory
obligated(state, personal_data, apply_technical_limitations).

% atom_id: cbb7f3ae4bb01534 | chunk: aefafe57d28654a9 | strength: statutory
obligated(state, personal_data, implement_security_measures).

% atom_id: 141c41f486f059ae | chunk: aefafe57d28654a9 | strength: statutory
obligated(state, personal_data, implement_privacy_preserving_measures).

% atom_id: 022efdc6a1fa2b1d | chunk: aefafe57d28654a9 | strength: statutory
obligated(state, personal_data, use_pseudonymisation).

% atom_id: 9685521b97f576c9 | chunk: af59ac6d8416befd | strength: statutory
obligated(provider, none, document_assessment) :-
    ai_system_risk(high).

% atom_id: b62e571999629e8f | chunk: af59ac6d8416befd | strength: statutory
obligated(provider, none, comply_with_registration_obligation) :-
    request(national_competent_authorities).

% atom_id: cff8932ade8b25e3 | chunk: af91e7ad1ca4f410 | strength: statutory
obligated(authority, none, take_into_account_requirements) :-
    implementing_act(pursuant_to_paragraph_1),
    ai_systems(safety_components).

% atom_id: eb8937948d6339b8 | chunk: b0631e05750bce89 | strength: statutory
permitted(natural_or_legal_person, market_surveillance_authority, submit_complaints).

% atom_id: 297600afff95dbcf | chunk: b0631e05750bce89 | strength: statutory
obligated(market_surveillance_authority, complaints_submitter, consider_complaints).

% atom_id: f24fb4444e2a57cc | chunk: b1474a6a0304c265 | strength: statutory
obligated(importer, competent_authorities, provide_information_and_documentation) :-
    request_reasoned(true),
    risk_class(high).

% atom_id: 04463bae696593e8 | chunk: b1474a6a0304c265 | strength: statutory
obligated(importer, technical_documentation, ensure_availability) :-
    request_reasoned(true),
    risk_class(high).

% atom_id: fa2f6df0979deb11 | chunk: b2908539368fc8d0 | strength: statutory
permitted(ai_office, none, initiate_structured_dialogue) :-
    request_status(pending).

% atom_id: 394d66d6051b8094 | chunk: b367ac489088f669 | strength: statutory
obligated(provider, ai_system, take_corrective_action).

% atom_id: 9bcee695b168f836 | chunk: b3901574bbaf92fb | strength: statutory
obligated(commission, none, facilitate_access_to_experts).

% atom_id: ba06dc12e5f6bcc7 | chunk: b3901574bbaf92fb | strength: statutory
obligated(commission, none, ensure_efficient_organization_of_support_activities).

% atom_id: d7c2311d4d12123f | chunk: b3c71371c7a2f124 | strength: statutory
obligated(ai_office, none, encourage_and_facilitate_review_and_adaptation_of_codes_of_p).

% atom_id: dbda2952bb454eb5 | chunk: b3c71371c7a2f124 | strength: statutory
obligated(ai_office, none, assist_in_assessment_of_available_standards).

% atom_id: 42d5dce0fdd929d1 | chunk: b3e6f5ed7992c37d | strength: statutory
obligated(provider, risk_management_system, be_understood_as_continuous_process).

% atom_id: 3c5d28980e6935bc | chunk: b3e6f5ed7992c37d | strength: statutory
obligated(provider, risk_management_system, be_planned_and_run_throughout_lifecycle).

% atom_id: 0a4a9aca81d7da9c | chunk: b3e6f5ed7992c37d | strength: statutory
obligated(provider, risk_management_system, require_regular_systematic_review_and_updating).

% atom_id: 185b91bae86d8045 | chunk: b5a537cde975c1f1 | strength: statutory
obligated(provider_deployer, report, provide_immediately) :-
    incident_type(widespread_infringement),
    incident_type(serious_incident).

% atom_id: 7bfb9e079a6080a5 | chunk: b6001dc159903c83 | strength: statutory
permitted(national_competent_authority, certificate, extend_provisional_validity) :-
    circumstances(first_subparagraph).

% atom_id: e012a1b169122686 | chunk: b6001dc159903c83 | strength: statutory
obligated(national_competent_authority_or_notified_body, commission_other_member_states_other_notified_bodies, inform_of_change) :-
    change_of_designation(affected).

% atom_id: 986bc465ef564b1e | chunk: b6a838eecc571ac0 | strength: statutory
obligated(testing_subjects, none, give_informed_consent) :-
    context(real_world_conditions).

% atom_id: c36810a3a030ac9b | chunk: b6a838eecc571ac0 | strength: statutory
prohibited(testing_authority, subjects, have_negative_effect) :-
    context(real_world_conditions),
    testing_status(tested).

% atom_id: 9031e0982b22c72a | chunk: b6a838eecc571ac0 | strength: statutory
obligated(testing_authority, subjects, delete_personal_data) :-
    context(real_world_conditions),
    testing_status(tested).

% atom_id: f06360ef81d98848 | chunk: b71b035a302f2e80 | strength: statutory
obligated(member_states, commission, report_annually).

% atom_id: 638ce42c54c866f0 | chunk: b78ee0775a35a7ee | strength: statutory
obligated(market_surveillance_authority, operator, require_measures_to_ensure_no_risk) :-
    evaluation_result(high_risk_system_complies_but_still_risks),
    consultation_with_public_authority(performed).

% atom_id: 814cf50b311c6377 | chunk: b7d4b029ccc75948 | strength: statutory
obligated(authorised_representative, non_state_actors, terminate_mandate) :-
    provider_action(acting_contrary_to_obligations).

% atom_id: 2a5ceab8266d898d | chunk: b95ddf180c383e0f | strength: statutory
obligated(provider, none, verify_technical_documentation).

% atom_id: 60656826149d7a90 | chunk: b95ddf180c383e0f | strength: statutory
obligated(provider, none, fulfill_obligations) :-
    article(53),
    article(55).

% atom_id: 8f5872c2917b4e1d | chunk: b95f8cfb49ee0e38 | strength: statutory
obligated(provider, ai_system, allow_human_override) :-
    decision_or_recommendation(may_lead_to_potential_harm).

% atom_id: ec71916d3e1fcb10 | chunk: ba60e04af4cf0a2a | strength: statutory
obligated(union_authority, ai_system, provide_effective_redress_measures) :-
    risk_level(low).

% atom_id: 00625bdc4ee49b02 | chunk: ba60e04af4cf0a2a | strength: statutory
obligated(union_authority, ai_system, implement_effective_prevention_measures) :-
    risk_level(low).

% atom_id: 8eae564b960bf853 | chunk: bae545669b7f1de1 | strength: statutory
obligated(commission, none, adopt_delegated_acts) :-
    technological_developments(algorithmic_improvements_increased_hardware_efficiency).

% atom_id: 817f2d3324ff2d96 | chunk: bb8331a19518d628 | strength: statutory
obligated(member_states, none, inform_commission_and_other_member_states) :-
    finding(under_paragraph_1).

% atom_id: 4c3ae444cbb715c1 | chunk: bc2fd2e6e13e6e2d | strength: statutory
obligated(market_surveillance_authority, none, indicate_grounds_and_challenge_mechanism) :-
    decision_taken(yes),
    objection_issued(yes).

% atom_id: 6660b6332fc330f2 | chunk: bc960facf0416a6e | strength: statutory
prohibited(undertaking, none, practice_ai).

% atom_id: b6d512efb7bd69fd | chunk: bd35a500d5e1f814 | strength: statutory
obligated(provider, none, appoint_authorised_representative) :-
    location_of_provider(third_country),
    model_type(general_purpose).

% atom_id: e2b68435b4f6ad61 | chunk: bdea7beaef563917 | strength: statutory
obligated(provider, quality_management_systems, include_aspects) :-
    risk_class(high),
    obligations(quality_management_systems_equivalent_function).

% atom_id: 3e7a6e7d3ce278ba | chunk: bef2616673e0b712 | strength: statutory
obligated(provider, competent_authorities, cooperate) :-
    request_reasoned(true).

% atom_id: 6f392a5b5257ec68 | chunk: bf49ad15f364adcf | strength: statutory
obligated(commission, eu_database, set_up_and_maintain).

% atom_id: d9ee73d8c667eed5 | chunk: bf49ad15f364adcf | strength: statutory
obligated(commission, functional_specifications_of_database, consult_experts).

% atom_id: a3a8f167d6b0638b | chunk: bf49ad15f364adcf | strength: statutory
obligated(commission, functional_specifications_of_database, consult_board).

% atom_id: c36833cccb704a69 | chunk: bfe1d3caede60e42 | strength: statutory
obligated(provider, eu_declaration_of_conformity, state_compliance).

% atom_id: 3bdd273eb7907b4f | chunk: bfe1d3caede60e42 | strength: statutory
obligated(provider, eu_declaration_of_conformity, contain_information).

% atom_id: cb3938268ce5fd3f | chunk: bfe1d3caede60e42 | strength: statutory
obligated(provider, language, be_translated).

% atom_id: 4ce4872d3612c89d | chunk: c0ab7b916c1d1f1b | strength: statutory
obligated(provider, ai_system, eliminate_or_reduce_risks) :-
    risk_identification(yes),
    technical_feasibility(yes).

% atom_id: 9f438c81f7118740 | chunk: c0d44d7d5caa8bdb | strength: statutory
permitted(national_competent_authorities, none, recover_costs) :-
    entity_type(smes),
    status(start_ups).

% atom_id: 4ec0a829cb22f12b | chunk: c16c73b05e6a4f80 | strength: statutory
obligated(notified_bodies, none, participate_in_coordination_activities).

% atom_id: 4b03094f35d7ecde | chunk: c16c73b05e6a4f80 | strength: statutory
obligated(notified_bodies, none, take_part_directly_or_be_represented_in_european_standardisa).

% atom_id: ffbfd69fd7467e94 | chunk: c16c73b05e6a4f80 | strength: statutory
obligated(notified_bodies, none, ensure_awareness_and_up_to_date_of_relevant_standards).

% atom_id: 61e2c1be22a83628 | chunk: c247e6e6757edb23 | strength: statutory
obligated(commission, none, reject_arguments) :-
    commissions_conclusion(arguments_not_sufficiently_substantiated),
    provider_able_to_demonstrate(general_purpose_ai_model_does_not_present_systemic_risks).

% atom_id: cfef68a77eff30e0 | chunk: c26df87b7ec1f182 | strength: statutory
obligated(implementing_authority, none, include_provisions).

% atom_id: 4a5548e03b149370 | chunk: c333bd81f29a6260 | strength: statutory
obligated(provider, public, implement_transparency_obligations).

% atom_id: bc0d9352bf265ddf | chunk: c35ab6c8a3e56eea | strength: statutory
obligated(deployer, fundamental_rights, assess_impact) :-
    risk_class(high),
    system_type(referred_to_in_article_6_2_points_5_b_and_c_of_annex_iii).

% atom_id: 9bc009e29b490320 | chunk: c3f3234900dcea0c | strength: statutory
obligated(member_states, commission, notify_of_penalties_and_enforcement_measures).

% atom_id: c113463daa291629 | chunk: c3f3234900dcea0c | strength: statutory
obligated(member_states, commission, notify_of_amendments_to_rules).

% atom_id: 9c7e1424b60571bb | chunk: c49d98262510bf3c | strength: statutory
obligated(provider, ai_system, bring_into_compliance) :-
    date_of_market_or_service(X_0), X_0 <= 2027,
    large_scale_it_systems(annex_x).

% atom_id: 446723a47c5e6a15 | chunk: c4a34843f882b8a5 | strength: statutory
permitted(ai_office, none, conduct_evaluations) :-
    consultation(after_consulting_board).

% atom_id: 52e520c0960a6850 | chunk: c5e99abf879f8d8e | strength: statutory
obligated(national_competent_authorities, none, act_in_accordance_with_confidentiality_obligations) :-
    task_performance(when_performing_tasks).

% atom_id: 03a29bb04ee39612 | chunk: c5f2d800561e3e42 | strength: statutory
obligated(member_states, national_competent_authorities, ensure_provision_of_resources).

% atom_id: 49a5a4ff78a8dab5 | chunk: c5f2d800561e3e42 | strength: statutory
obligated(member_states, national_competent_authorities, ensure_sufficient_personnel).

% atom_id: 88cfad831b969395 | chunk: c5f2d800561e3e42 | strength: statutory
obligated(member_states, national_competent_authorities, ensure_competence_and_expertise).

% atom_id: 1fe68886b12d4a94 | chunk: c5f2d800561e3e42 | strength: statutory
obligated(member_states, national_competent_authorities, assess_and_update_competence_requirements) :-
    time_period(annually).

% atom_id: 64ffa471c090927b | chunk: c684382d1d3c9d88 | strength: statutory
obligated(provider_or_prospective_provider, none, oversee_testing) :-
    testing(real_world_conditions).

% atom_id: 8c8120804fcf73dd | chunk: c684382d1d3c9d88 | strength: statutory
obligated(deployer_or_prospective_deployer, none, oversee_testing) :-
    testing(real_world_conditions).

% atom_id: b9e139a0882d7d2a | chunk: c6b1bef3663b925c | strength: statutory
obligated(european_data_protection_supervisor, union_institution_body_office_or_agency, give_opportunity_to_be_heard) :-
    proceedings_conducted(yes).

% atom_id: 74097a60742ff22b | chunk: c6b1bef3663b925c | strength: statutory
obligated(european_data_protection_supervisor, parties_concerned, base_decisions_on_commented_elements) :-
    proceedings_conducted(yes).

% atom_id: 2cd833ac669b31a3 | chunk: c6b1bef3663b925c | strength: statutory
obligated(complainants, proceedings, be_associated_closely) :-
    existence_of_complaint(yes).

% atom_id: a5d9962ed39f7f1b | chunk: c6e639c64f20ef39 | strength: statutory
obligated(provider, ai_system, make_substantial_modification) :-
    modification_status(substantial),
    risk_class(high).

% atom_id: a57842fb74492f7e | chunk: c76f45f84c729f0e | strength: statutory
obligated(commission, none, establish_scientific_panel).

% atom_id: 78ba50cf2fc2ca2b | chunk: c76f45f84c729f0e | strength: statutory
obligated(commission, none, make_provisions).

% atom_id: 69e50bda354f9c21 | chunk: c7c828a43250c0bb | strength: statutory
obligated(commission, none, facilitate_experience_exchange).

% atom_id: 62a951c5348e62d5 | chunk: c8d1b6be34611106 | strength: statutory
obligated(provider, none, take_corrective_action) :-
    time_period(period_referred_to_in_paragraph_2).

% atom_id: a46d9b73c0a0aa0d | chunk: c8ec1bc4f5ab328e | strength: statutory
obligated(provider, certificates, assess_impact).

% atom_id: 4b076f6589a7002f | chunk: c90038e83a3474d2 | strength: statutory
prohibited(provider, ai_system, non_compliance_with_requirements_or_obligations).

% atom_id: 61ba57ad8c7cdb0d | chunk: c91f872f9fa1120b | strength: statutory
obligated(concerned_conformity_assessment_body, notifying_authority, provide_documentary_evidence).

% atom_id: 335c63919d9b62ca | chunk: c9bc3c8dbf81a8ba | strength: statutory
obligated(provider, ai_system, be_resilient) :-
    risk_class(high).

% atom_id: 5c19c973d432e305 | chunk: c9bc3c8dbf81a8ba | strength: statutory
obligated(provider, ai_system, take_technical_and_organizational_measures) :-
    risk_class(high).

% atom_id: 684b349594dd2862 | chunk: c9bc3c8dbf81a8ba | strength: statutory
obligated(provider, ai_system, develop_with_technical_redundancy_solutions) :-
    risk_class(high),
    system_status(continuing_learning).

% atom_id: 7234df48d2af0353 | chunk: c9bc3c8dbf81a8ba | strength: statutory
obligated(provider, ai_system, eliminate_or_reduce_biased_outputs_risk) :-
    risk_class(high),
    system_status(continuing_learning).

% atom_id: 506c5685a49d0389 | chunk: c9bc3c8dbf81a8ba | strength: statutory
obligated(provider, ai_system, address_feedback_loops_with_mitigation_measures) :-
    risk_class(high),
    system_status(continuing_learning).

% atom_id: 186280c6ad1bd845 | chunk: ca074ae25d884280 | strength: statutory
obligated(commission, none, communicate_decision).

% atom_id: 2d9281887ea42b12 | chunk: ca074ae25d884280 | strength: statutory
obligated(commission, none, inform_other_member_states).

% atom_id: 956d2b1d5bd8c26c | chunk: ca8c0ee4ba03afa2 | strength: statutory
obligated(provider, ai_system, develop_on_basis_of_quality_data_sets) :-
    risk_class(high),
    techniques_involving_training(yes).

% atom_id: 3252558530451d4e | chunk: caeb60d9ede5be1c | strength: statutory
obligated(member_state, none, identify_public_authorities).

% atom_id: 3416c5ee9dab9ada | chunk: caeb60d9ede5be1c | strength: statutory
obligated(member_state, none, make_list_publicly_available).

% atom_id: 43b5bdbc81350841 | chunk: caeb60d9ede5be1c | strength: statutory
obligated(member_state, none, notify_list_to_commission_and_other_member_states).

% atom_id: 819cdea61252bbc3 | chunk: caeb60d9ede5be1c | strength: statutory
obligated(member_state, none, keep_list_up_to_date).

% atom_id: 539af1d9e290fa0b | chunk: cb26e7a9916caa55 | strength: statutory
obligated(provider, vulnerable_persons_or_groups_of_vulnerable_persons, assess_and_prevent_negative_impact) :-
    impact_category(accessibility_for_persons_with_a_disability_gender_equality).

% atom_id: 619a0fb560288232 | chunk: cb9477d84a078740 | strength: statutory
obligated(deployer, natural_persons, inform_of_system_operation).

% atom_id: f4a6ca2e55f0b068 | chunk: cb9477d84a078740 | strength: statutory
permitted(ai_system, none, detect_prevent_investigate_criminal_offences) :-
    system_type(emotion_recognition_system_biometric_categorisation_system).

% atom_id: 1b8cafcc00b24618 | chunk: cbbcd5c303745790 | strength: statutory
obligated(national_competent_authorities, none, design_and_implement_sandboxes_for_cross_border_cooperation) :-
    context(relevant).

% atom_id: c738f34996c1b453 | chunk: cbca68ed0c7288a7 | strength: statutory
permitted(commission_and_board, exit_reports, access_and_consider) :-
    confidentiality_provisions(in_article_78),
    agreement(provider_or_prospective_provider).

% atom_id: f0498baf8da2be86 | chunk: cbca68ed0c7288a7 | strength: statutory
permitted(commission_and_board, exit_reports, make_publicly_available) :-
    agreement(provider_or_prospective_provider),
    national_competent_authority(explicit_agreement).

% atom_id: 906213906ee25cb8 | chunk: cc4e771723a21f27 | strength: statutory
permitted(provider, none, submit_application).

% atom_id: 7182f64fceab5ca1 | chunk: cc4e771723a21f27 | strength: statutory
permitted(prospective_provider, none, submit_application).

% atom_id: f08358356beb7542 | chunk: cc4e771723a21f27 | strength: statutory
permitted(deployer, none, participate_in_sandbox).

% atom_id: de1acc40d87f3bbe | chunk: cc4e771723a21f27 | strength: statutory
permitted(third_party, none, participate_in_sandbox).

% atom_id: c2a97111c7d03945 | chunk: cd846930709d2792 | strength: statutory
obligated(provider, logs, keep_logs) :-
    risk_class(high).

% atom_id: 255f1309aa9da828 | chunk: cd846930709d2792 | strength: statutory
obligated(provider, logs, keep_logs_duration) :-
    risk_class(high).

% atom_id: d4fa99e6151d9f80 | chunk: cde9609a013e1f20 | strength: statutory
obligated(provider, high_risk_ai_system, put_name_or_trademark_on_system) :-
    system_status(already_placed_on_market_or_put_into_service),
    risk_class(high).

% atom_id: 1d694887547417e4 | chunk: cebe892166638fdb | strength: statutory
obligated(provider, none, make_report) :-
    causal_link_established(true),
    awareness_of_incident(true).

% atom_id: fab32995d0744965 | chunk: cebe892166638fdb | strength: statutory
obligated(deployer, none, make_report) :-
    causal_link_established(true),
    awareness_of_incident(true).

% atom_id: f871a236f125edb6 | chunk: cec70d44945aa1df | strength: statutory
obligated(importer, high_risk_ai_system, ensure_compliance_storage_transport) :-
    responsibility(under_importers).

% atom_id: fe08ae8e540a58a7 | chunk: cecb65bd98410767 | strength: statutory
obligated(competent_authorities, none, provide_guidance_supervision_and_support) :-
    context(ai_regulatory_sandbox).

% atom_id: af20fcec90b826bd | chunk: cf2aa106ecaa772a | strength: statutory
obligated(provider, deployer, provide_interpretative_information) :-
    risk_class(high).

% atom_id: c7062708809c3f20 | chunk: cf946f32de84ed96 | strength: statutory
obligated(provider_deployer, high_risk_ai_system, comply_with_requirements_obligations) :-
    date(n2_august_2030).

% atom_id: c78597202de6e400 | chunk: cf946f32de84ed96 | strength: statutory
obligated(provider_deployer, high_risk_ai_system, subject_to_significant_changes) :-
    date(n2_august_2026).

% atom_id: bc51e858ba2c6231 | chunk: d11113a060207ed4 | strength: statutory
obligated(provider, ai_system, test_for_risk_management) :-
    risk_class(high).

% atom_id: ee73f816bf910d5e | chunk: d11113a060207ed4 | strength: statutory
obligated(provider, ai_system, ensure_consistent_performance) :-
    risk_class(high).

% atom_id: 127fda42b575ec2f | chunk: d11113a060207ed4 | strength: statutory
obligated(provider, ai_system, comply_with_requirements) :-
    risk_class(high).

% atom_id: fa3d05a44b3bed38 | chunk: d1640a8fafaa58e7 | strength: statutory
obligated(provider, subject_of_testing_or_their_legal_representative, receive_informed_consent_document).

% atom_id: fa98bd3b2bcadbb0 | chunk: d1d6001b5ddb002b | strength: statutory
permitted(provider, none, subcontract_activities) :-
    activity_type(activities).

% atom_id: d7aabc8c3c152840 | chunk: d1d6001b5ddb002b | strength: statutory
permitted(provider, subsidiary, carry_out_activities) :-
    activity_type(activities),
    agreement_status(with_agreement).

% atom_id: 8ec10c1efea746f2 | chunk: d1d6001b5ddb002b | strength: statutory
obligated(notified_bodies, none, make_list_publicly_available) :-
    entity_type(subsidiaries).

% atom_id: 5b65e78f0ded6c24 | chunk: d3ca691d48b46e4d | strength: statutory
obligated(commission, provider_of_generalpurpose_ai_model, communicate_preliminary_findings_and_give_opportunity_to_be).

% atom_id: fcf7dccbedaf2968 | chunk: d3cdedfe11337546 | strength: statutory
permitted(provider, special_categories_of_personal_data, process) :-
    purpose(bias_detection_and_correction),
    risk_class(high).

% atom_id: 27325feee326c7c9 | chunk: d6bda1bca8ee3071 | strength: statutory
obligated(member_state, ai_system, ensure_restrictive_measures) :-
    commission_decision(justified).

% atom_id: 4b8a23e591e0a645 | chunk: d6bda1bca8ee3071 | strength: statutory
obligated(member_state, ai_system, withdraw_ai_system_market) :-
    commission_decision(justified).

% atom_id: 3ea61c8a0ef87071 | chunk: d6bda1bca8ee3071 | strength: statutory
obligated(member_state, national_measure, withdraw_national_measure) :-
    commission_decision(unjustified).

% atom_id: 67d39bd503b07f29 | chunk: d6c52d0937d9d973 | strength: statutory
permitted(national_competent_authorities, none, provide_guidance_and_advice) :-
    regulation(this).

% atom_id: 7153fa2e92d441f9 | chunk: d6c52d0937d9d973 | strength: statutory
permitted(national_competent_authorities, none, provide_guidance_and_advice) :-
    target(sme_including_start_ups).

% atom_id: c9c6f84929c086d6 | chunk: d6c52d0937d9d973 | strength: statutory
obligated(national_competent_authorities, union_law_affected_authorities, consult) :-
    area(areas_covered_by_other_union_law).

% atom_id: f3fd73e639fb0c74 | chunk: d768dc2c71b088f8 | strength: statutory
obligated(notifying_authorities, information, safeguard_confidentiality).

% atom_id: 52743e36bfd780e5 | chunk: d76f97492aabaada | strength: statutory
obligated(parties_concerned, none, respect_rights_of_defence).

% atom_id: fb3f2e7f16ffcaea | chunk: d76f97492aabaada | strength: statutory
permitted(parties_concerned, european_data_protection_supervisor, grant_access_to_file) :-
    legitimate_interest(individuals_undertakings).

% atom_id: d9d8de4226a64aa7 | chunk: d896e008005fdd0c | strength: statutory
permitted(subjects_of_testing, personal_data, withdraw_from_testing) :-
    testing_status(in_real_world_conditions).

% atom_id: 9d2a9b31278118c5 | chunk: d896e008005fdd0c | strength: statutory
permitted(subjects_of_testing, personal_data, request_deletion) :-
    testing_status(in_real_world_conditions).

% atom_id: f80cfdff4f94b146 | chunk: d896e008005fdd0c | strength: statutory
obligated(data_controller, personal_data, delete_immediately_and_permanently) :-
    testing_status(in_real_world_conditions),
    request_action(withdrawal_of_informed_consent).

% atom_id: beaa717e023edffd | chunk: d896e008005fdd0c | strength: statutory
obligated(data_controller, activities, not_affect_activities_already_carried_out) :-
    testing_status(in_real_world_conditions),
    request_action(withdrawal_of_informed_consent).

% atom_id: 6d9b6d91e12c58e4 | chunk: d8c788a3089a96c1 | strength: statutory
obligated(provider, ai_system, assess_and_minimize_environmental_impact).

% atom_id: 122d26b4cbdc2c81 | chunk: d8df7ccbf9e7942e | strength: statutory
obligated(deployer, high_risk_ai_system, use_in_accordance_with_instructions) :-
    risk_class(high).

% atom_id: c6cda30b4857b993 | chunk: d94310e59feed201 | strength: statutory
obligated(market_surveillance_authority, market_surveillance_authorities_of_other_member_states, communicate_grounds) :-
    decision_taken(referred_to_in_paragraph_3),
    ai_system_tested(testing_plan).

% atom_id: 09d9fa0b1a002569 | chunk: d9ba227733eedd1f | strength: statutory
obligated(market_surveillance_authority, ai_system, take_provisional_measures) :-
    operator_action(does_not_take_adequate_corrective_action),
    time_period(within_the_period_referred_to_in_paragraph_2).

% atom_id: 39f2721116f30f8e | chunk: da11298061123faa | strength: statutory
obligated(market_surveillance_authorities, testing_in_real_world_conditions, ensure_compliance_with_regulation).

% atom_id: dd49c3f0ea237e80 | chunk: daa138f90e2707af | strength: statutory
prohibited(provider, ai_system, exploit_vulnerabilities) :-
    vulnerability_type(age_disability_social_or_economic_situation).

% atom_id: 50698fa62c328778 | chunk: dad819658f8d1eb6 | strength: statutory
obligated(provider, natural_persons_or_groups_of_persons, provide_information_on_risks) :-
    specific_risk(harm).

% atom_id: 427ec385a5c7a69e | chunk: dae844895c80e213 | strength: statutory
obligated(provider, risk_management_system, establish_implement_document_maintain) :-
    risk_class(high).

% atom_id: 89bd7c701f38b419 | chunk: dc7f53dda628807b | strength: statutory
obligated(notifying_authority, bodies_notified, participation_in_group_work).

% atom_id: e56fe6332cf8db40 | chunk: ddbe16b42e24b2d4 | strength: statutory
obligated(provider, ai_model, classify_as_general_purpose_with_systemic_risk) :-
    risk_class(general_purpose_with_systemic_risk).

% atom_id: 76e24f95d68c0695 | chunk: ddf33ddf8545c876 | strength: statutory
prohibited(deployer, person_or_group_of_persons, use_subliminal_techniques) :-
    technique_type(subliminal),
    technique_effect(manipulative_or_deceptive).

% atom_id: 2a66dd48520cdcc2 | chunk: ddf33ddf8545c876 | strength: statutory
prohibited(deployer, person_or_group_of_persons, materially_distort_behavior) :-
    decision_impairment(appreciable),
    decision_outcome(informed).

% atom_id: 08b3c9767f642aa5 | chunk: ddf33ddf8545c876 | strength: statutory
prohibited(deployer, person_or_group_of_persons, cause_significant_harm) :-
    harm_type(significant).

% atom_id: 127bd82c983fb7bf | chunk: deaf354ad811be4c | strength: statutory
obligated(market_surveillance_authority_of_a_member_state, provider, require_end_of_non_compliance) :-
    findings_made(finding_1_finding_2_finding_3).

% atom_id: e5a416d8e7230c9a | chunk: e0287eca4f36607f | strength: statutory
obligated(provider, high_risk_ai_system, comply_with_cybersecurity_requirements) :-
    certification_status(certified_or_conformity_statement),
    cybersecurity_scheme(regulation_2019881),
    publication_in_official_journal(published).

% atom_id: f4d438592f99d558 | chunk: e06944c78520ac0c | strength: statutory
obligated(provider, commission_and_other_member_states, submit_report) :-
    time_since_notification(three_months).

% atom_id: 74edf7903ab8f839 | chunk: e0780baa55be8046 | strength: statutory
prohibited(commission_member_states_and_authorities_notified_bodies, none, affect_information_exchange_or_dissemination_of_warnings).

% atom_id: fcc2d17c480d7abf | chunk: e0780baa55be8046 | strength: statutory
prohibited(parties_concerned, none, affect_obligations_to_provide_information_under_criminal_law).

% atom_id: 23f267bbb6ad6157 | chunk: e108cfa1295614a0 | strength: statutory
obligated(notified_bodies, none, satisfy_requirements).

% atom_id: ef1d097df67ee95d | chunk: e149c3c0886c5dbe | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    evidence(concrete_and_reliable).

% atom_id: 14f8d2b4c1167bb5 | chunk: e1af309163ff1e2d | strength: statutory
obligated(distributor, competent_authorities, cooperate_with_authorities) :-
    risk_class(high).

% atom_id: 12300893dca7b8b9 | chunk: e22063da8311c578 | strength: statutory
obligated(provider, none, put_in_place_quality_management_system) :-
    financial_institution(true),
    subject_to_requirements(true).

% atom_id: 3da05376ea0b601c | chunk: e22063da8311c578 | strength: statutory
obligated(provider, none, comply_with_rules_on_internal_governance) :-
    financial_institution(true),
    subject_to_requirements(true).

% atom_id: ecdc823cd0353a9f | chunk: e269b275b46b8ab3 | strength: statutory
obligated(commission, none, provide_support).

% atom_id: f487e7a1635ec834 | chunk: e269b275b46b8ab3 | strength: statutory
obligated(commission, providers_prospective_providers_deployers, receive_support).

% atom_id: 91c3ac1416e3e374 | chunk: e37f8f237da48dbb | strength: statutory
obligated(board, none, safeguard_objectivity_and_impartiality).

% atom_id: 2efaec78ff5493f2 | chunk: e58774002e01f121 | strength: statutory
obligated(importer, competent_authorities, cooperate_with_authorities) :-
    risk_class(high).

% atom_id: 9646fcc6f06528cf | chunk: e61c7fdfebd6fe29 | strength: statutory
obligated(commission, none, develop_expertise_and_capabilities).

% atom_id: 2a6ff6908351fd22 | chunk: e71403f25aede5ec | strength: statutory
permitted(market_surveillance_authorities, none, perform_checks).

% atom_id: 9f4f08bea73e6335 | chunk: e8f7a999b314aa94 | strength: statutory
obligated(importer, high_risk_ai_system, not_place_on_market) :-
    conformity(not_conforming),
    falsification(falsified_accompanied_by_falsified_documentation).

% atom_id: 6704b8b76af4a1dd | chunk: e8f7a999b314aa94 | strength: statutory
obligated(importer, provider_of_system, inform) :-
    risk(within_meaning_of_article_791).

% atom_id: be6a046df6a9e330 | chunk: e8f7a999b314aa94 | strength: statutory
obligated(importer, authorised_representative, inform) :-
    risk(within_meaning_of_article_791).

% atom_id: f2738942280c72e8 | chunk: e8f7a999b314aa94 | strength: statutory
obligated(importer, market_surveillance_authorities, inform) :-
    risk(within_meaning_of_article_791).

% atom_id: cac50c87ddb1a43a | chunk: e910f2bff95ccaed | strength: statutory
obligated(commission, none, assess_harmonised_standard) :-
    harmonised_standard(adopted_by_european_standardisation_organisation).

% atom_id: 1c6801e0e4578ab7 | chunk: e910f2bff95ccaed | strength: statutory
obligated(commission, none, repeal_implementing_acts) :-
    reference_to_harmonised_standard(published_in_official_journal).

% atom_id: c851f80852bbc00e | chunk: e9156c4761ba8712 | strength: statutory
prohibited(provider, ai_system, deploy_without_adequate_protection) :-
    risk_of_harm(high_risk),
    fundamental_rights_impact(adverse).

% atom_id: dec7305c9c0f9a60 | chunk: e92a527779b4de71 | strength: statutory
obligated(distributor, high_risk_ai_system, verify_marking_and_documents) :-
    risk_class(high).

% atom_id: a6f850dd63152275 | chunk: e92a5c643a5132fc | strength: statutory
obligated(deployer, natural_persons, inform_of_ai_system_use) :-
    risk_class(high),
    decision_making_context(related_to_natural_persons).

% atom_id: 059b4c3ce0f1b9fd | chunk: e92a5c643a5132fc | strength: statutory
obligated(deployer, natural_persons, inform_of_ai_system_use) :-
    risk_class(high),
    decision_making_context(for_law_enforcement_purposes).

% atom_id: 5f4039bd7be80aeb | chunk: e97a6d6c03b72fdf | strength: statutory
obligated(provider, ai_system, examine_for_biases) :-
    data_outputs(inputs_for_future_operations).

% atom_id: 0f30d9e765aac4fd | chunk: e97a6d6c03b72fdf | strength: statutory
prohibited(provider, ai_system, produce_biases) :-
    biases(health_and_safety_of_persons_negative_impact_on_fundamental).

% atom_id: f785dc32847b724f | chunk: e9ccad4fc882f370 | strength: statutory
permitted(member_states, none, pay_fees).

% atom_id: ed16cca1a78b887a | chunk: ea0f0872ef5f1ea6 | strength: statutory
obligated(members_of_advisory_forum, none, serve_in_office).

% atom_id: db358b3c24dab9ad | chunk: ea0f0872ef5f1ea6 | strength: statutory
obligated(members_of_advisory_forum, none, extend_term_of_office) :-
    current_term(two_years).

% atom_id: a6ec8e24a86bf3c5 | chunk: ebb7e4ed89db7444 | strength: statutory
obligated(provider_deployer, staff_other_persons, ensure_ai_literacy) :-
    technical_knowledge(their_technical_knowledge_experience_education_training),
    context(the_context_the_ai_systems_are_to_be_used_in),
    persons_groups_of_persons(the_persons_or_groups_of_persons_on_which_the_ai_systems_are).

% atom_id: aa8969ef2cd904e8 | chunk: ece210a9a245c59c | strength: statutory
obligated(competent_authority, none, treat_information_confidentially).

% atom_id: 611f9ab927a90d7d | chunk: ecfdc5e87047d4b2 | strength: statutory
obligated(authorities, none, establish_advisory_forum).

% atom_id: a9e82b1ae5e5c1f5 | chunk: ecfdc5e87047d4b2 | strength: statutory
obligated(authorities, board_and_commission, receive_advice).

% atom_id: 2835e9b037989b09 | chunk: ecfdc5e87047d4b2 | strength: statutory
obligated(authorities, regulation_tasks, contribute_to_tasks).

% atom_id: ab0d7c53007c2c2e | chunk: ed380eb68b11085d | strength: statutory
obligated(deployer, high_risk_ai_system, update_information) :-
    change_or_outdated(true).

% atom_id: ca89a267278e483f | chunk: ed380eb68b11085d | strength: statutory
permitted(deployer, none, rely_on_existing_assessments) :-
    similar_cases(true).

% atom_id: b9421fdc4a21658f | chunk: eecd9853d49dab99 | strength: statutory
obligated(designated_representatives_of_member_states, none, adopt_board_rules_of_procedure) :-
    majority(two_thirds).

% atom_id: e9c042323ed3a454 | chunk: ef206ba59845110b | strength: statutory
obligated(deployer, ai_office_and_competent_authorities, cooperate) :-
    request_reasoned(true).

% atom_id: 59b542c71fa99408 | chunk: ef730923dae61d20 | strength: statutory
obligated(provider, none, implement_mitigation_measures) :-
    risk_status(cannot_be_eliminated).

% atom_id: 0495185787554a05 | chunk: efdea54b6a51caad | strength: statutory
obligated(provider, deployer, provide_information).

% atom_id: e07ea5c3a4a0fe2f | chunk: efdea54b6a51caad | strength: statutory
obligated(provider, deployer, provide_training) :-
    appropriateness(where_appropriate).

% atom_id: 23d90cc3edcf0616 | chunk: f04b15a261a678de | strength: statutory
obligated(provider, ai_system, draw_up_single_declaration) :-
    risk_class(high).

% atom_id: c14ce5cae7bb4c25 | chunk: f052c920f168af73 | strength: statutory
obligated(employer, workers_representatives_and_workers, be_informed_of_high_risk_ai_system_use) :-
    risk_class(high),
    context(workplace).

% atom_id: 6dbbdbaca96ba531 | chunk: f0e913dcee3b05d7 | strength: statutory
obligated(distributor, high_risk_ai_system, take_corrective_actions) :-
    conformity(not_conforming),
    information_in_possession(consideration_of_high_risk_ai_system).

% atom_id: 386bb4878fd83302 | chunk: f0e913dcee3b05d7 | strength: statutory
obligated(distributor, high_risk_ai_system, withdraw_or_recall) :-
    conformity(not_conforming),
    information_in_possession(consideration_of_high_risk_ai_system).

% atom_id: f0281de086b25ff6 | chunk: f0e913dcee3b05d7 | strength: statutory
obligated(distributor, provider_or_importer, take_corrective_actions) :-
    conformity(not_conforming),
    information_in_possession(consideration_of_high_risk_ai_system).

% atom_id: 0638ff1cba589e88 | chunk: f0e913dcee3b05d7 | strength: statutory
obligated(distributor, relevant_authorities, inform) :-
    risk_within_meaning_of_article_79(true).

% atom_id: 6319a8dc54ddae0c | chunk: f1c211489413434d | strength: statutory
obligated(provider, training_validation_and_testing_data_sets, be_relevant_and_representative).

% atom_id: d1da7bd64992a65a | chunk: f1c211489413434d | strength: statutory
obligated(provider, training_validation_and_testing_data_sets, be_free_of_errors_and_complete).

% atom_id: cc0f0ae867722896 | chunk: f1c211489413434d | strength: statutory
obligated(provider, training_validation_and_testing_data_sets, have_appropriate_statistical_properties) :-
    intended_use(persons_or_groups_of_persons).

% atom_id: 4d27c3c3fdf80d21 | chunk: f291a5fefa15d054 | strength: statutory
obligated(requestor, none, state_legal_basis_and_purpose).

% atom_id: 458c2d2d2a9103cf | chunk: f291a5fefa15d054 | strength: statutory
obligated(requestor, none, set_access_period).

% atom_id: 55508b51f5b33814 | chunk: f291a5fefa15d054 | strength: statutory
prohibited(provider, none, fail_to_provide_access).

% atom_id: 9ec10752aebc3fec | chunk: f29bb44d41e0baad | strength: statutory
permitted(public_authority_or_body, market_surveillance_authority, make_reasoned_request_for_testing) :-
    documentation_sufficiency(insufficient).

% atom_id: 38a454113aed8e9a | chunk: f29bb44d41e0baad | strength: statutory
obligated(market_surveillance_authority, high_risk_ai_system, organize_testing) :-
    request_received(true).

% atom_id: 060acf5e8c42248f | chunk: f39bf69a32223907 | strength: statutory
obligated(competent_authorities, website, publish_summary) :-
    project_status(developed_in_sandbox).

% atom_id: 09273b58afbf0e40 | chunk: f39bf69a32223907 | strength: statutory
prohibited(competent_authorities, summary, include_sensitive_data) :-
    data_type(sensitive_operational),
    authorities(law_enforcement_border_control_immigration_asylum).

% atom_id: 7d6ff9a223632119 | chunk: f3f0f2f86415ac9f | strength: statutory
obligated(member_states, market_surveillance_authorities, confer_powers).

% atom_id: 8a3348235315af89 | chunk: f3f0f2f86415ac9f | strength: statutory
obligated(market_surveillance_authorities, providers_and_prospective_providers, provide_information).

% atom_id: 95fb3b0a42702886 | chunk: f3f0f2f86415ac9f | strength: statutory
obligated(market_surveillance_authorities, providers_and_prospective_providers, carry_out_unannounced_remote_or_on_site_inspections).

% atom_id: cd2638d930be5287 | chunk: f3f0f2f86415ac9f | strength: statutory
obligated(market_surveillance_authorities, high_risk_ai_systems, perform_checks_on_testing_in_real_world_conditions).

% atom_id: 61c31a877bc50fdd | chunk: f534ed1daab0be59 | strength: statutory
obligated(provider, ai_system, be_used_as_safety_component) :-
    intended_use(safety_component_of_product).

% atom_id: a133449d2ff51647 | chunk: f534ed1daab0be59 | strength: statutory
obligated(provider, ai_system, be_product_covered_by_legislation) :-
    intended_use(product).

% atom_id: cf1b8d242b9f02f0 | chunk: f548d27c5de05554 | strength: statutory
obligated(authority, public, access_information) :-
    database(eu_database_registered_according_to_article_49).

% atom_id: 30507b37aa7c0b4b | chunk: f5cd26fe3593c36d | strength: statutory
obligated(regulation, none, enter_into_force) :-
    date(twentieth_day_following_publication_in_official_journal_of_t).

% atom_id: e288aa9d66c53857 | chunk: f5cd26fe3593c36d | strength: statutory
obligated(regulation, none, apply) :-
    date(n2_august_2026).

% atom_id: 1e1e09851ee9780c | chunk: f5cd26fe3593c36d | strength: statutory
obligated(regulation, none, apply) :-
    date(n2_february_2025).

% atom_id: 671dbe8bc14a62b7 | chunk: f5cd26fe3593c36d | strength: statutory
obligated(regulation, none, apply) :-
    date(n2_august_2025).

% atom_id: a56e1dbb3215cbf2 | chunk: f5cd26fe3593c36d | strength: statutory
obligated(regulation, none, apply) :-
    date(n2_august_2027).

% atom_id: 8ce246224463a935 | chunk: f60917995d9b9a7f | strength: statutory
obligated(provider, national_competent_authorities, keep_information_disposable) :-
    time_period(n10_years_after_market_entry_or_service_start).

% atom_id: d0fcb69938406795 | chunk: f663ecc32bfd5ec8 | strength: statutory
obligated(ai_office_and_member_states, none, take_into_account_interests_needs_smes) :-
    entity_type(sme).

% atom_id: 46a31eaa5c44495e | chunk: f7a0da7d2a55d2d9 | strength: statutory
obligated(european_parliament_or_council, none, express_objection) :-
    act_type(article_66_or_7_article_71_or_3_article_113_article_435_or_6).

% atom_id: 27b4a8593bc2ac41 | chunk: f7a0da7d2a55d2d9 | strength: statutory
obligated(european_parliament_or_council, none, inform_no_objection) :-
    act_type(article_66_or_7_article_71_or_3_article_113_article_435_or_6).

% atom_id: 506e3c2a6349f6b1 | chunk: f7cfbaaa88ee3a86 | strength: statutory
obligated(provider, none, appoint_authorised_representative) :-
    risk_class(high).

% atom_id: 203e2dea5151ca2f | chunk: f897a24269dd4123 | strength: statutory
obligated(provider, ai_system, ensure_transparency) :-
    risk_class(high).

% atom_id: d59504df25086569 | chunk: f897a24269dd4123 | strength: statutory
obligated(deployer, ai_system_output, interpret_and_use_appropriately) :-
    risk_class(high).

% atom_id: dd1bdd47619152fe | chunk: f918275f5bb0a8d9 | strength: statutory
obligated(commission, none, develop_interface).

% atom_id: 41f6d92d83cab187 | chunk: f918275f5bb0a8d9 | strength: statutory
obligated(commission, stakeholders, interact_with_interface).

% atom_id: 2e0afe0ceae0b437 | chunk: f918275f5bb0a8d9 | strength: statutory
obligated(commission, stakeholders, raise_enquiries).

% atom_id: c04ccc958467c58e | chunk: f918275f5bb0a8d9 | strength: statutory
obligated(commission, competent_authorities, coordinate_proactively).

% atom_id: 01281e81957b07ef | chunk: f96523bd41467880 | strength: statutory
obligated(provider, commission_and_national_competent_authorities, cooperate).

% atom_id: d4025b111cac0228 | chunk: f975fb44e0f0c1c7 | strength: statutory
obligated(provider, none, deliver_harmonised_standards) :-
    time(deadline).

% atom_id: bfb3b9a2a7889938 | chunk: f9bad1cfb469b8ed | strength: statutory
obligated(importer, high_risk_ai_system, ensure_conformity).

% atom_id: a1b887cb8c7ea13b | chunk: fa7cf663667a74fd | strength: statutory
permitted(public_authority, market_surveillance_authority, be_informed_of_requests) :-
    type_of_authority(national_public_authorities_or_bodies),
    jurisdiction_limit(their_jurisdiction).

% atom_id: ecd72ff3f75e5cdc | chunk: fa7cf663667a74fd | strength: statutory
obligated(public_authority, ai_system_provider, request_and_access_documentation) :-
    risk_class(high),
    type_of_ai_system(ai_systems_referred_in_annex_iii).

% atom_id: 03a47930bcbeaeea | chunk: fb97b4caa7ff9e14 | strength: statutory
obligated(member_states, market_surveillance_authorities, designate_authority) :-
    risk_class(high),
    use_case(law_enforcement_border_management_justice_and_democracy).

% atom_id: 973042d18196bc52 | chunk: fb97b4caa7ff9e14 | strength: statutory
obligated(member_states, market_surveillance_authorities, designate_authority) :-
    risk_class(high),
    use_case(points_6_7_8_of_annex).

% atom_id: ef9e7b4d0b4f429f | chunk: fb97b4caa7ff9e14 | strength: statutory
prohibited(market_surveillance_authorities, judicial_authorities, affect_independence_or_interfere_activities).

% atom_id: 532c21cf3f9df16a | chunk: fc304a730ff53ac8 | strength: statutory
obligated(provider, ai_system, comply_with_requirements) :-
    risk_class(high),
    training_data(reflects_specific_setting).

% atom_id: 2ae91fb88ec4a963 | chunk: fc5282c5e09f6881 | strength: statutory
obligated(member_state, national_competent_authorities, determine_conditions) :-
    provider_status(bankruptcy_or_cessation_of_activity).

% atom_id: da7096ab7cb76e1d | chunk: fce782b406bf1370 | strength: statutory
obligated(ai_office, none, develop_template_questionnaire).

% atom_id: 1bdb492dd1d3bafa | chunk: fdd519845212b972 | strength: statutory
obligated(provider, ai_system, automatically_record_events) :-
    risk_class(high).

% atom_id: 8366345ff1c69273 | chunk: fe923155b2829c20 | strength: statutory
permitted(market_surveillance_authorities, none, exercise_powers_remotely) :-
    context(ensuring_effective_enforcement_of_this_regulation).

% atom_id: f0e69768f86f5881 | chunk: fea002432146ad63 | strength: statutory
obligated(provider, generalpurpose_ai_model, comply_with_additional_obligations) :-
    risk_class(systemic).

% atom_id: 576996a98331ad99 | chunk: feee430d2c542ef5 | strength: statutory
obligated(provider, none, register_system) :-
    risk_class(not_high_risk).

% atom_id: 9590cbe17aa9fc92 | chunk: feee430d2c542ef5 | strength: statutory
obligated(provider, none, register_in_eu_database) :-
    risk_class(not_high_risk).

% atom_id: 96f569a6b496e23a | chunk: feee430d2c542ef5 | strength: statutory
obligated(authorised_representative, none, register_system) :-
    risk_class(not_high_risk).

% atom_id: 3cba40ee93942b0f | chunk: feee430d2c542ef5 | strength: statutory
obligated(authorised_representative, none, register_in_eu_database) :-
    risk_class(not_high_risk).

% atom_id: efcda3ed48ab5154 | chunk: ff4547167f24076d | strength: statutory
obligated(commission, notified_body, assign_identification_number).

% atom_id: ac83b9474a3712be | chunk: ff75e24788538ad2 | strength: statutory
obligated(commission, none, submit_report) :-
    date(n2_august_2028),
    frequency(every_four_years_thereafter).