% atom_id: 32eff2c62d37f269 | chunk: 1b563ee8e7fea45f | strength: regulatory
obligated(state_medicaid_agency, individual, determine_eligibility_for_medicaid) :-
    income_reduction(income_standard),
    health_care_expenses_deduction(X_1), X_1 > 0.

% atom_id: 438c757f16a8d5e2 | chunk: 2c7caaa4c4400354 | strength: regulatory
prohibited(state_of_residence, institutionalized_individual, be_a_state_other_than_the_one_in_which_the_individual_is_phy) :-
    age(X_0), X_0 >= 21,
    incapable_of_indicating_intent(yes),
    placement_made_by_another_state(no).

% atom_id: b29ef7143b0b9880 | chunk: 3db42388a26583ca | strength: regulatory
permitted(state, none, enter_into_interstate_agreement) :-
    agreement_purpose(resolving_cases_of_disputed_residency).

% atom_id: c466d13f4deba79c | chunk: 1ef16b13853a4f10 | strength: regulatory
obligated(state_medicaid_agency, institution, reduce_payment) :-
    individual_status(specified_in_paragraph_b),
    total_income(X_1), X_1 > 0.

% atom_id: caad3b326a61ecca | chunk: 238e8e40bc358238 | strength: regulatory
obligated(state_of_residence, institutionalized_individual, be_the_state_where_living_and_intends_to_reside).

% atom_id: ab5acfc33c066ad2 | chunk: 242753f5c10ca430 | strength: regulatory
obligated(state, none, submit_data) :-
    time_period(july_1_2023_june_30_2024).

% atom_id: ea8025a8f154b396 | chunk: 263d3e6dac537cdf | strength: regulatory
obligated(state_medicaid_agency, individual, exclude_ffp) :-
    institution_type(public_institution_institution_for_tuberculosis_or_mental_di).

% atom_id: 51cd0cd520723e11 | chunk: 2c7caaa4c4400354 | strength: regulatory
obligated(state_of_residence, institutionalized_individual, be_the_state_in_which_the_individual_is_physically_present) :-
    age(X_0), X_0 >= 21,
    incapable_of_indicating_intent(yes).

% atom_id: 54e22fde7c4bc333 | chunk: 34264d673b7cf98d | strength: regulatory
obligated(state_medicaid_agency, none, apply_income_standards) :-
    institutionalization_period(X_0), X_0 >= 30.

% atom_id: 6bd8e926b9c48988 | chunk: 3db42388a26583ca | strength: regulatory
permitted(state, none, enter_into_interstate_agreement) :-
    agreement_purpose(facilitating_administration_of_program).

% atom_id: e5219782b162655f | chunk: 3db42388a26583ca | strength: regulatory
permitted(state, none, enter_into_interstate_agreement) :-
    agreement_purpose(facilitating_placement_and_adoption).

% atom_id: 533ebc10d6365354 | chunk: 3db42388a26583ca | strength: regulatory
obligated(state, individual_pending_resolution_of_case, provide_medicaid_coverage) :-
    agreement_purpose(resolving_cases_of_disputed_residency).

% atom_id: 5961f690e91de832 | chunk: 41b840aeed051c5d | strength: regulatory
obligated(state_medicaid_agency, individual_applying_for_medicaid, accept_medical_records_as_evidence_of_citizenship).

% atom_id: 3dd1b3fa805fae98 | chunk: 49f814b98f43b615 | strength: regulatory
obligated(state_medicaid_agency, individual_eligible_for_medicaid, continue_to_meet_criteria) :-
    month(december_1973),
    criteria(blindness_or_disability).

% atom_id: ca54d50ba7c4ef2a | chunk: 4af2e69e8017323e | strength: regulatory
obligated(state_medicaid_agency, categorically_needy_beneficiaries, provide_medical_assistance).

% atom_id: 36d3459d600b8d10 | chunk: 4af2e69e8017323e | strength: regulatory
obligated(state_medicaid_agency, medically_needy_beneficiaries, provide_medical_assistance).

% atom_id: 2deb751ce204fea7 | chunk: 4af2e69e8017323e | strength: regulatory
obligated(state_medicaid_agency, qualified_medicare_beneficiaries, provide_medical_assistance).

% atom_id: fd35276b1fc6cb73 | chunk: 4dae0aa2859c707a | strength: regulatory
obligated(state_medicaid_agency, individual_institutionalized_with_intellectual_disabilities, use_income_standards_based_on_need) :-
    institution_type(medical_institution_nursing_facility_intermediate_care_facil).

% atom_id: 87291982edc1827d | chunk: 4dae0aa2859c707a | strength: regulatory
obligated(state_medicaid_agency, individual_institutionalized_with_intellectual_disabilities, establish_income_standards_varied_by_factors) :-
    institution_type(medical_institution_nursing_facility_intermediate_care_facil).

% atom_id: 597de38b3159a28b | chunk: 542b6b7ded89a782 | strength: regulatory
permitted(state_medicaid_agency, aged_individuals_in_institutions, provide_medicaid_coverage) :-
    eligibility(afdc_or_ssi_or_state_supplements_except_for_institutional_st),
    status(aged_blind_and_disabled).

% atom_id: 379e1bbaa821ed90 | chunk: 5979cc39199fe119 | strength: regulatory
obligated(state_medicaid_agency, institutionalized_individuals_with_income_below_special_leve, provide_medicaid_coverage) :-
    status(institutionalized),
    income(special_income_level).

% atom_id: 2aa21500548a118f | chunk: 66b2ced091a3b315 | strength: regulatory
obligated(state_medicaid_agency, individual_under_19, ensure_medicaid_cost_equality) :-
    care_setting(outside_an_institution).

% atom_id: 6c81388047fd4db3 | chunk: 6e50d9bcf9f7e6b4 | strength: regulatory
obligated(state, institutionalized_individuals, meet_medicaid_eligibility_requirements) :-
    date(december_1973).

% atom_id: 74219acd28d2d3b0 | chunk: 7c8e082cda84ff62 | strength: regulatory
obligated(state_medicaid_agency, individual, assist_in_locating_institution) :-
    individual_capability(capable_of_indicating_intent),
    individual_decision(independently_decides_to_move).

% atom_id: f3b2430b8b1a98fe | chunk: 8c809885c0990818 | strength: regulatory
obligated(state_medicaid_agency, essential_spouse, continue_to_meet_conditions) :-
    date(december_1973),
    plan(applicable_cash_assistance_plan).

% atom_id: df961537cd23a470 | chunk: 901d4231e9401667 | strength: regulatory
obligated(state_medicaid_agency, group, provide_medicaid_coverage) :-
    institutionalization_status(true).

% atom_id: 41be648a6cf0e8c7 | chunk: 90bdb8a2bf1b21df | strength: regulatory
obligated(state_medicaid_agency, individuals_requesting_coverage_for_long_term_care_services, provide_medicaid_coverage) :-
    request_purpose(evaluation_for_eligibility_group),
    long_term_care_services_and_supports(nursing_facility_services_equivalent_institutional_services).

% atom_id: c4fa9cdc988e5a8a | chunk: 982307d641351f7e | strength: regulatory
obligated(state_medicaid_agency, institution, reduce_payment) :-
    individual_status(specified_in_paragraph_b_of_this_section).

% atom_id: c9ff41ad96ad26b6 | chunk: 998197645cd1e3f8 | strength: regulatory
obligated(agency, institution, deduct_amounts_from_total_income) :-
    income_status(disregarded_in_eligibility).

% atom_id: cd0a2461966c48ac | chunk: 9a2fa0c7cc608519 | strength: regulatory
obligated(state_medicaid_agency, institutionalized_couple, provide_monthly_allowance) :-
    spouse_age(aged_blind_disabled),
    income_considered_available(yes).

% atom_id: ba96b5f3830360d4 | chunk: aee4a5eb73b59833 | strength: regulatory
obligated(state_medicaid_agency, individuals_losing_categorically_needy_eligibility, send_notices_of_potential_eligibility_for_medicaid) :-
    eligibility_loss_reason(loss_of_ssi),
    medically_needy_program_status(without).

% atom_id: 3962d597eadd37ec | chunk: b10c36dc84016c70 | strength: regulatory
obligated(state_medicaid_agency, institutionalized_couple, provide_monthly_allowance) :-
    spouse_age(aged_blind_disabled),
    income_considered_available(yes).

% atom_id: 7e9d778d188f15a8 | chunk: b325c52ba4d7e967 | strength: regulatory
obligated(state_medicaid_agency, individual_under_65_institutionalized_for_mental_diseases, provide_medicaid_coverage) :-
    age(X_0), X_0 < 65,
    institution_type(institution_for_mental_diseases).

% atom_id: aa7b00cec76779ab | chunk: b7bfbd0c57d7824e | strength: regulatory
obligated(medicaid_agency, none, provide_information_consistently) :-
    standards_and_methods(program_objectives),
    standards_and_methods(individual_rights).

% atom_id: 3c0b8fb8b96ede07 | chunk: bedc63dcdc16126d | strength: regulatory
permitted(state_medicaid_agency, children_under_18, provide_medicaid_coverage) :-
    age(X_0), X_0 <= 18,
    eligibility_criteria(qualify_under_section_1614a_of_the_act),
    medical_care_status(receiving_medical_care_at_home).

% atom_id: 807b1b7967da3a84 | chunk: c6645dea8b11949d | strength: regulatory
obligated(state_medicaid_agency, individual_under_19, provide_level_of_care_outside_institution) :-
    age(X_0), X_0 < 19.