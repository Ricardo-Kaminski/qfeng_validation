% atom_id: 503b591d4a2017a7 | chunk: 020985954a62af18 | strength: statutory
obligated(state_medicaid_agency, child, arrange_for_corrective_treatment) :-
    need_disclosed(true).

% atom_id: 484162a54dd22ebd | chunk: 0ea1c8bccadd2459 | strength: regulatory
prohibited(state, hospital, immediately_jeopardize_health_and_safety_of_patients).

% atom_id: 19c5d52e98de83ed | chunk: 03dffe0b28eb4fca | strength: statutory
obligated(state, individual, deliver_services).

% atom_id: 0541b6c3191be84b | chunk: 0654a77d146da195 | strength: regulatory
obligated(secretary, none, establish_a_system).

% atom_id: f077279d7d4dcdf6 | chunk: 0654a77d146da195 | strength: regulatory
obligated(secretary_and_states, individual, prevent_simultaneous_enrollment).

% atom_id: 0197c2fd72d6d631 | chunk: 0657c771743176ec | strength: regulatory
obligated(state_authority, none, include_descriptions) :-
    plan_kinds(professional_medical_personnel_supporting_staff).

% atom_id: de4b7b90e1428a17 | chunk: 0657c771743176ec | strength: regulatory
obligated(state_authority, none, utilize_standards) :-
    institution_type(private_institutions_public_institutions).

% atom_id: 595de6b9fbeaed8a | chunk: 0657c771743176ec | strength: regulatory
obligated(state_authority, none, enter_into_arrangements) :-
    agencies(state_health_agencies_state_vocational_rehabilitation_agenci).

% atom_id: 889f479565206629 | chunk: 0657c771743176ec | strength: regulatory
obligated(state_authority, none, use_standards_and_methods) :-
    quality_assurance(high_quality).

% atom_id: d6a44e3d086ab2d3 | chunk: 08820b64fc822496 | strength: regulatory
obligated(clearinghouse_or_other_alternate_payee, none, register_with_state_and_secretary) :-
    submitting_claims(true).

% atom_id: da112a69c4a7346a | chunk: 089609fc1fe57d48 | strength: statutory
obligated(state, none, comply_with_eligibility_verification_requirements) :-
    geography(n50_states_district_of_columbia).

% atom_id: 1481e9983423686d | chunk: 08ca41f7aff46b7d | strength: statutory
permitted(secretary, none, continue_payments) :-
    time_period(X_0), X_0 <= 6,
    date(the_date_the_hospital_is_found_to_be_out_of_compliance_with).

% atom_id: 462a2128b51ed057 | chunk: 0a39680cd97e688e | strength: regulatory
obligated(state, annual_report, include_information).

% atom_id: 8762a4350b8efa43 | chunk: 0a40b2924adf64a9 | strength: regulatory
obligated(state, center_or_clinic, provide_payment_for_services) :-
    service_date(january_1_2001),
    fiscal_year(2001).

% atom_id: 3fe84202d4ad8678 | chunk: 0a55f95b669ef914 | strength: statutory
obligated(state, none, provide_financial_participation) :-
    non_federal_share(n40_per_centum).

% atom_id: 0ae8db6b849c0817 | chunk: 0a55f95b669ef914 | strength: statutory
obligated(state, none, provide_financial_participation) :-
    non_federal_share(n100_per_centum),
    effective_date(july_1_1969).

% atom_id: 705a0a2c7e187f42 | chunk: 0a55f95b669ef914 | strength: statutory
obligated(state, none, provide_distribution_of_funds) :-
    effective_date(july_1_1969).

% atom_id: 22ca250c696f9cf8 | chunk: 0beba21d0d409edf | strength: statutory
obligated(state, none, submit_plan_and_timetable_for_corrective_action).

% atom_id: 42f18a7f2ce39590 | chunk: 0beba21d0d409edf | strength: statutory
obligated(secretary, none, approve_plan_of_corrective_action).

% atom_id: 1468d4fd13db34f2 | chunk: 0d640aa4f5cd7ff8 | strength: statutory
obligated(state, none, submit_a_report).

% atom_id: 6d4fab146a4a5f2c | chunk: 0dbbd654a37005c2 | strength: regulatory
obligated(state_agency, specified_individual_or_entity, exclude_from_participation) :-
    required_by_secretary(yes).

% atom_id: 5d187caa00dd6f71 | chunk: 0dbbd654a37005c2 | strength: regulatory
obligated(state_agency, individual_or_entity, terminate_participation) :-
    termination_under_subchapter_xviii(yes),
    termination_included_in_database(yes).

% atom_id: 23212adb46708817 | chunk: 0dbbd654a37005c2 | strength: regulatory
obligated(state_agency, no_payment, not_make_payment) :-
    item_or_service_furnished(yes),
    during_exclusion_period(yes).

% atom_id: 0d6ec8d95dea232f | chunk: 0fa8821dee6ed40a | strength: statutory
prohibited(state_authority, resource_standard_or_methodology, be_more_restrictive) :-
    individual(none).

% atom_id: 6f6d8eb0e34595bb | chunk: 0fee87b1038cb50c | strength: statutory
prohibited(state, individual, include_costs_in_income_determination).

% atom_id: a754d10b285180ee | chunk: 12067e215af72d97 | strength: statutory
obligated(state, child_born_to_eligible_mother, deem_application_and_eligibility) :-
    mother_eligibility(true),
    date_of_birth(date_of_mothers_eligibility).

% atom_id: 4a500f49f361a686 | chunk: 12067e215af72d97 | strength: statutory
obligated(state, child_born_to_eligible_mother, use_mothers_identification_number) :-
    mother_eligibility(true),
    date_of_birth(date_of_mothers_eligibility).

% atom_id: 62cb3e0927ebd054 | chunk: 12067e215af72d97 | strength: statutory
obligated(state, child_born_to_eligible_mother, submit_and_pay_claims) :-
    mother_eligibility(true),
    date_of_birth(date_of_mothers_eligibility).

% atom_id: f5c67bb06f58a842 | chunk: 12067e215af72d97 | strength: statutory
obligated(state, child_born_to_eligible_mother, issue_separate_identification_number) :-
    mother_is_alien(true),
    medical_assistance_available(true).

% atom_id: 45fe07bbdaa79c30 | chunk: 12d24b363282a9b4 | strength: statutory
obligated(state_authority, anyone_receiving_payment, make_no_payment) :-
    recipient(individual_or_provider).

% atom_id: 90ffb4fe0a0ec423 | chunk: 12f97228ddf0fd67 | strength: regulatory
obligated(state, provider, enroll_with_state_agency_and_provide_identifying_information) :-
    date(X_0), X_0 >= 2017,
    payment_method(fee_for_service),
    state_plan_or_waiver(pursuant_to).

% atom_id: a366d9b845676053 | chunk: 142fbe8272e72fe6 | strength: regulatory
obligated(state_medicaid_agency, disabled_individual, provide_medical_assistance) :-
    income(maximum_amount).

% atom_id: 30bf20c3a37f97d1 | chunk: 1438b99125325898 | strength: regulatory
obligated(state_medicaid_agency, none, provide_services_to_encourage_drug_intake).

% atom_id: 19465b964c0b939c | chunk: 14f48c6efe32f056 | strength: regulatory
obligated(state_not_eligible_to_participate_in_state_plan_program_esta, aged_blind_or_disabled_individual, provide_medical_assistance) :-
    is_qualified_disabled_or_working_individual(false),
    is_qualified_medicare_beneficiary(false),
    is_qualified_severely_impaired_individual(false).

% atom_id: e868e998280aab8d | chunk: 14f48c6efe32f056 | strength: regulatory
obligated(state_not_eligible_to_participate_in_state_plan_program_esta, aged_blind_or_disabled_individual, provide_medical_assistance) :-
    is_qualified_disabled_or_working_individual(false),
    is_qualified_medicare_beneficiary(false),
    is_qualified_severely_impaired_individual(false).