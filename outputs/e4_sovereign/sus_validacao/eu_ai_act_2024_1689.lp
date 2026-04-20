% atom_id: 5b7194434043d835 | chunk: 0097db893574abbe | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    use_cases(high_risk_ai_systems),
    conditions_fulfilled(both).

% atom_id: 1933fa9b65355f5f | chunk: 00f886be50778ea7 | strength: statutory
obligated(authority, information_or_documentation, treat_with_confidentiality) :-
    source(this_article).

% atom_id: 50d4c7e5456406d3 | chunk: 04928b44712bad29 | strength: statutory
prohibited(national_competent_authority, information, disclose_confidentially_exchanged_information) :-
    context(high_risk_ai_systems_used_by_law_enforcement),
    context(high_risk_ai_systems_used_by_border_control),
    context(high_risk_ai_systems_used_by_immigration_authorities),
    context(high_risk_ai_systems_used_by_asylum_authorities),
    context(disclosure_would_jeopardise_public_and_national_security_int).

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