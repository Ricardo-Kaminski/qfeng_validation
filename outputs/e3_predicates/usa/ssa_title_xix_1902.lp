% atom_id: e48cb0d724de7036 | chunk: 019800cbc2e5ddd5 | strength: statutory
permitted(state, hospital_nursing_facility_intermediate_care_facility, provide_continuous_stay).

% atom_id: 503b591d4a2017a7 | chunk: 020985954a62af18 | strength: statutory
obligated(state_medicaid_agency, child, arrange_for_corrective_treatment) :-
    need_disclosed(true).

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

% atom_id: 484162a54dd22ebd | chunk: 0ea1c8bccadd2459 | strength: regulatory
prohibited(state, hospital, immediately_jeopardize_health_and_safety_of_patients).

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

% atom_id: a2c43afc974a5607 | chunk: 15bcf4d73ccad42c | strength: regulatory
obligated(state_medicaid_agency, none, provide_administration_methods) :-
    methods(administration_personnel_standards_on_a_merit_basis_excludin).

% atom_id: 4eb13faa942f9b97 | chunk: 15bcf4d73ccad42c | strength: regulatory
obligated(state_medicaid_agency, none, train_and_use_subprofessional_staff) :-
    emphasis(full_time_or_part_time_employment_of_recipients_and_other_pe).

% atom_id: 9bbb926dee8e39ce | chunk: 15bcf4d73ccad42c | strength: regulatory
prohibited(state_or_local_officer_employee_independent_contractor, none, commit_prohibited_acts) :-
    activity(any_activity_under_the_plan),
    prohibition_source(section_207_or_208_of_title_18_united_states_government).

% atom_id: dd42bb242c853c7a | chunk: 15bcf4d73ccad42c | strength: regulatory
obligated(state_or_local_officer_employee_independent_contractor, none, adhere_to_safeguards_against_conflicts_of_interest) :-
    activity(selecting_awarding_or_otherwise_obtaining_items_and_services).

% atom_id: b288a24623b1efc2 | chunk: 18dc865b3bd35b65 | strength: regulatory
obligated(state, provider_or_supplier, conduct_check_of_death_master_file) :-
    date(january_1_2028),
    event(enrollment_reenrollment_or_revalidation).

% atom_id: 1b09d26f7f49cceb | chunk: 18dc865b3bd35b65 | strength: regulatory
obligated(state, provider_or_supplier, conduct_check_of_death_master_file) :-
    date(january_1_2028),
    frequency(quarterly).

% atom_id: d696dfb9e6c1754b | chunk: 197f8b21ddef8874 | strength: regulatory
obligated(state, none, solicit_advice) :-
    plan_amendments(any),
    waiver_requests(any),
    demonstration_projects(any).

% atom_id: b723839c52105933 | chunk: 19c302906694a0e0 | strength: regulatory
obligated(nursing_facility, none, satisfy_requirements).

% atom_id: 6a8e7861c6be4347 | chunk: 1b90c7aafaa2b54b | strength: statutory
obligated(state, federally_qualified_health_center_or_rural_health_clinic, provide_supplemental_payment) :-
    service_provider(federally_qualified_health_center_or_rural_health_clinic),
    contract_exists(true).

% atom_id: 1eb3bee39934da9a | chunk: 1b97ccc41ba3f0c4 | strength: statutory
prohibited(state_medicaid_agency, resource_standard_or_methodology, be_more_restrictive) :-
    individual(subparagraph_b_subparagraph_c_subparagraph_d).

% atom_id: 142a20a5b0a32f3f | chunk: 1c4a23f2f48ebe4a | strength: statutory
obligated(hospice_program, individual, provide_initial_receipt_of_hospice_care).

% atom_id: 3837810e8f4cb4cc | chunk: 1c7153d6ea1305f6 | strength: statutory
prohibited(state, none, waive_provisions).

% atom_id: 0c37572d02d60e25 | chunk: 1f317bd8133db35e | strength: regulatory
permitted(state, individual_who_is_pregnant_and_eligible_for_medical_assistan, provide_medical_assistance) :-
    pregnancy_status(pregnant),
    eligibility_status(eligible_for_medical_assistance).

% atom_id: bb0d489f4300245a | chunk: 1f317bd8133db35e | strength: regulatory
obligated(state, individual_who_is_pregnant_and_eligible_for_medical_assistan, remain_eligible_for_medical_assistance) :-
    pregnancy_status(pregnant),
    eligibility_status(eligible_for_medical_assistance).

% atom_id: 07dc159f3507530d | chunk: 201fdc76e8e09d42 | strength: statutory
obligated(state_medicaid_agency, eligible_individual_without_permanent_dwelling, provide_method_of_making_cards_evidencing_eligibility) :-
    residence_status(does_not_reside_in_apermanent_dwelling_or_does_not_have_a_fi).

% atom_id: 19a5c12546f5347e | chunk: 2032039dee82ee45 | strength: statutory
obligated(state, federal_government, repay_payments) :-
    corrective_action(none),
    approved_plan_and_timetable(none).

% atom_id: 8661ebf07298e408 | chunk: 22dbcc279eccade0 | strength: statutory
obligated(provider, individual, refer_to_state_agency).

% atom_id: 840726ccce551467 | chunk: 24ffec2fef89afc1 | strength: statutory
permitted(state, none, elect_to_provide_medical_assistance) :-
    date(april_1_2010),
    date(january_1_2014).

% atom_id: f129652b5c293de6 | chunk: 24ffec2fef89afc1 | strength: statutory
permitted(state, none, phase_in_extension_of_eligibility) :-
    date(april_1_2010),
    date(january_1_2014).

% atom_id: 1ccdcd9353370618 | chunk: 24ffec2fef89afc1 | strength: statutory
obligated(state, individuals_described_in_subclause_viii, ensure_extension_of_eligibility) :-
    income(lower_income).

% atom_id: 293679497bc78f16 | chunk: 28036bdfb6a12983 | strength: regulatory
obligated(puerto_rico, administrator_of_the_centers_for_medicare_and_medicaid_servi, submit_report) :-
    quarter(puerto_rico_is_required_under_subparagraph_a).

% atom_id: cf9fd9161e115cbf | chunk: 284db9bda9557838 | strength: statutory
obligated(state, none, make_election_under_section_1902_e_16_c) :-
    election(child_health_assistance_for_targeted_low_income_children_who).

% atom_id: f2a3ee7694a22291 | chunk: 285ea9d15599930a | strength: statutory
permitted(state, none, engage_in_provider_and_supplier_screening_or_oversight).

% atom_id: 0e6cdbb9ce9e20b8 | chunk: 28c83284673be3da | strength: statutory
obligated(state, none, establish_or_designate_authority).

% atom_id: fc0e0f9baeb4a78c | chunk: 28c83284673be3da | strength: statutory
obligated(state_authority, none, establish_and_maintain_standards) :-
    standards_scope(health).

% atom_id: cd1c54e7d6c6e2cf | chunk: 296055b1d46ea1dd | strength: statutory
obligated(hospital_nursing_facility_provider_home_health_care_or_perso, none, comply_with_requirements_subsection_w).

% atom_id: 307a0546e20d135e | chunk: 29bfa4057035c463 | strength: statutory
prohibited(state_authority, individual_eligible_for_medical_assistance, treat_as_enrolled_in_federal_health_care_program) :-
    eligibility_status(eligible_for_medical_assistance_under_subsection_a_10_a_ii_x),
    minimum_essential_coverage(not_eligible_under_section_5000a_f_1_of_the_internal_revenue).

% atom_id: ee5a1c759a426026 | chunk: 29bfa4057035c463 | strength: statutory
prohibited(state_authority, individual_eligible_for_medical_assistance, treat_as_enrolled_in_federal_health_care_program) :-
    eligibility_status(described_in_subsection_l_1_a_and_eligible_only_because_of_s),
    eligibility_limitation(limited_by_the_state_under_clause_vii_in_the_matter_followin).

% atom_id: bb1294448735b943 | chunk: 2cac5c038dce1363 | strength: statutory
obligated(state, individual_newly_enrolled_in_state_plan, submit_name_and_social_security_number_to_commissioner) :-
    enrollment_status(newly_enrolled_in_the_state_plan_under_this_subchapter),
    month(that_month),
    citizenship_status(united_states_citizen_or_national).

% atom_id: 246c5ac4bc436d4f | chunk: 2f5a9df17ba689d1 | strength: statutory
prohibited(state, none, apply_assets_or_resources_test).

% atom_id: 371a42cc25043446 | chunk: 2f99ab7851a258e7 | strength: statutory
obligated(state, provider_or_supplier, impose_enrollment_moratoria_or_numerical_caps) :-
    risk_level(high_risk_for_fraud_high_risk_for_waste_high_risk_for_abuse).

% atom_id: 275a4c914e7030ae | chunk: 2f99ab7851a258e7 | strength: statutory
obligated(state, beneficiaries, ensure_access_to_medical_assistance) :-
    impact(adverse).

% atom_id: 64fecc3fca9cedeb | chunk: 3291fd8e625088e6 | strength: statutory
obligated(state, patient_receiving_services_in_intermediate_care_facility_for, provide_written_plan_of_care_prior_to_admission_or_authoriza).

% atom_id: 7878a3df2c3d707d | chunk: 3291fd8e625088e6 | strength: statutory
obligated(state, patient_receiving_services_in_intermediate_care_facility_for, conduct_regular_program_of_independent_professional_review_i).

% atom_id: 8afc476c4a80f26c | chunk: 33ea0e8a035f1483 | strength: regulatory
prohibited(state_authority, none, exceed_income_limit) :-
    income_level(X_0), X_0 > 100.

% atom_id: 753cb4e53280c101 | chunk: 3413638a9e217a14 | strength: statutory
obligated(state, individual_in_medical_institution, provide_medical_assistance) :-
    location(medical_institution).

% atom_id: 978a6e19454c2136 | chunk: 3746794618d92a3b | strength: regulatory
permitted(state, none, provide_payment) :-
    medical_assistance_furnished(medicare_cost_sharing_respecting_the_furnishing_of_a_service),
    service_or_item(the_sum_of_such_payment_amount_and_any_amount_of_payment_mad).

% atom_id: 56c21764aa94254c | chunk: 37fb635f5cde4981 | strength: regulatory
obligated(state_medicaid_agency, individual_described_in_subclause_viii_of_a10ai, provide_medical_assistance) :-
    is_individual(subclause_viii_of_subsection_a10ai).

% atom_id: a1aacecdeb5c5563 | chunk: 37fb635f5cde4981 | strength: regulatory
obligated(state_medicaid_agency, individual_described_in_subclause_viii_of_a10ai, provide_benchmark_coverage_or_equivalent) :-
    is_individual(subclause_viii_of_subsection_a10ai).

% atom_id: 8140643b8b7a9fa7 | chunk: 37fb635f5cde4981 | strength: regulatory
obligated(state_medicaid_agency, individual_described_in_subclause_viii_of_a10ai, provide_medical_assistance_subject_to_requirements) :-
    is_individual(subclause_viii_of_subsection_a10ai).

% atom_id: ae266dd221e719ae | chunk: 3942a6eb4aa9bbb4 | strength: regulatory
obligated(state_authority, individuals_in_state_who_are_eligible_for_medical_assistance, notify_of_availability_of_benefits) :-
    eligibility_status(eligible),
    pregnancy_status(pregnant_women_breastfeeding_or_postpartum_women_children_be).

% atom_id: eb2b9fdf12abdb12 | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, none, enter_into_agreements_or_arrangements).

% atom_id: 0f8c8e91630b1b38 | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, state_authorities_concerned_with_mental_diseases, enter_into_agreements_or_arrangements).

% atom_id: 90b1a4621ad06cde | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, institutions, enter_into_agreements_or_arrangements).

% atom_id: e420b20a13748c1d | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, individuals_under_alternate_plans_of_care, ensure_immediate_readmittance_to_institutions).

% atom_id: 74cecdb9b071e98f | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, patients_and_facilities, ensure_access).

% atom_id: f1984ae39ee4ee69 | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, individuals_under_alternate_plans_of_care, furnish_information).

% atom_id: cda5788aac2c6f9c | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, individuals_under_alternate_plans_of_care, make_reports).

% atom_id: 2586f8a9312aaa18 | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, none, engage_in_joint_planning).

% atom_id: 27ca7f9e8d025762 | chunk: 39ef0392c0198bb2 | strength: regulatory
obligated(state_authorities, none, develop_alternate_methods_of_care).

% atom_id: b839286215efc711 | chunk: 3b397361c5015751 | strength: statutory
permitted(state, none, not_meet_requirement) :-
    state(non_50_states_district_of_columbia).

% atom_id: 5eeccfd5ecc267e2 | chunk: 3b397361c5015751 | strength: statutory
permitted(state, none, substitute_percentage) :-
    state(non_50_states_district_of_columbia).

% atom_id: e1c33fd6dd94aeab | chunk: 3b7344fc1adaced9 | strength: regulatory
prohibited(state, facility, immediately_jeopardize_health_and_safety_of_patients).

% atom_id: b39433a473c40371 | chunk: 3b7344fc1adaced9 | strength: regulatory
permitted(state, facility, establish_alternative_remedies) :-
    alternative_remedies_effectiveness(effective_in_detering_noncompliance_correcting_deficiencies).

% atom_id: 3e35e3d6f3dc906a | chunk: 3cc936124d834f62 | strength: statutory
permitted(state, none, use_resource_level) :-
    medical_assistance(true),
    state_option(yes).

% atom_id: fe98b1b35f8b60b4 | chunk: 3da876c0772f6143 | strength: regulatory
obligated(state, none, comply_with_requirements).

% atom_id: dc54d75f0058fa49 | chunk: 3ee5f9e07c1c8baa | strength: regulatory
obligated(state, public, publish_searchable_directory) :-
    plan_type(fee_for_service_basis_primary_care_case_management_system_de).

% atom_id: a12b6707417fea90 | chunk: 3ee5f9e07c1c8baa | strength: regulatory
obligated(state, public, update_directory_quarterly) :-
    plan_type(fee_for_service_basis_primary_care_case_management_system_de).

% atom_id: 5351e2f7722c44e0 | chunk: 3ee5f9e07c1c8baa | strength: regulatory
obligated(state, public, make_paper_directories_available) :-
    plan_type(fee_for_service_basis_primary_care_case_management_system_de).

% atom_id: bb7b0e64b481e1d7 | chunk: 3f02c962b0e99116 | strength: statutory
obligated(state, individual, disregard_compensation) :-
    compensation_type(stipend).

% atom_id: e9ca86f59f386b07 | chunk: 3f25d2269f724452 | strength: statutory
obligated(state_authority, individual, conduct_eye_examination) :-
    condition(blind).

% atom_id: 92b1af1c8f1b7aed | chunk: 3fd2c0431d233c65 | strength: regulatory
obligated(entity_furnishing_items_or_services, secretary_or_state_agency, supply_information) :-
    request(specifically_addressed_to_entity_by_secretary_or_state_agenc).

% atom_id: aa3c8231304abfb5 | chunk: 4004312dbae1d714 | strength: statutory
obligated(state, none, implement_asset_verification_program).

% atom_id: 6c812541241d0808 | chunk: 40dad45b5be9a5d7 | strength: statutory
permitted(state, individual_or_entity, exclude_from_participation) :-
    reason(section_1320a_7_section_1320a_7a_section_1395ccb2).

% atom_id: 663978b05d248cf2 | chunk: 41b71372742ac585 | strength: statutory
obligated(northern_mariana_islands, none, implement_requirements).

% atom_id: b76f9d3a7534cf34 | chunk: 41b71372742ac585 | strength: statutory
obligated(american_samoa, none, implement_requirements).

% atom_id: 0624d59ae9be73ea | chunk: 41b71372742ac585 | strength: statutory
obligated(guam, none, implement_requirements).

% atom_id: 9569feb4ed76d538 | chunk: 41ee3c2d1b415740 | strength: regulatory
obligated(secretary, state, waive_drug_review_and_utilization_requirements) :-
    event_type(natural_disasters_similar_situations),
    service_type(emergency_services).

% atom_id: 52d3341887fdd8a1 | chunk: 43180d42d9299e8f | strength: regulatory
obligated(state_agency_administering_state_plan, none, provide_assurances_to_secretary) :-
    compliance_with_subparagraphs(a_b_c).

% atom_id: ba2bbc6e36c4c0a3 | chunk: 44386e79230e162e | strength: regulatory
obligated(state, none, demonstrate_operation_of_medicaid_fraud_and_abuse_control_un) :-
    fraud_and_abuse_unit_description(section_1396bq),
    effective_functions_requirements(section_1396bq).

% atom_id: 5780e311a24350d9 | chunk: 44386e79230e162e | strength: regulatory
obligated(state, none, demonstrate_cost_effectiveness_or_protection_of_beneficiarie) :-
    minimal_fraud_existence(true),
    beneficiary_protection(true).

% atom_id: 11150d1d5c694f89 | chunk: 44e1d2c8b091a10f | strength: statutory
obligated(state, individual, not_condition_provision_of_care).

% atom_id: 5caa0f9a1ad91e5d | chunk: 44e1d2c8b091a10f | strength: statutory
obligated(state, individual, not_discriminate_against_individual).

% atom_id: 16edce8e8fe7ff2f | chunk: 44ef6995dfbc651b | strength: regulatory
obligated(state, individuals_described_in_subparagraph_d_of_paragraph_1, establish_income_level) :-
    income_level(n100_percent_or_133_percent_of_fpl).

% atom_id: 45826016bb22b3a5 | chunk: 46fcc43ad68f5919 | strength: statutory
obligated(state_authority, individual_eligible_for_medical_assistance, provide_medical_assistance) :-
    status(inmate_of_public_institution).

% atom_id: 87831a087d355b23 | chunk: 47ee0ea39e1abf20 | strength: regulatory
obligated(secretary, none, not_authorize_limitations).

% atom_id: db77bf8efeba1faf | chunk: 484216b9c65d162d | strength: regulatory
obligated(state, adult_individual, provide_written_information).

% atom_id: a13181bd3a86fa84 | chunk: 4a6ff71f07bbef6f | strength: statutory
obligated(state, hospitals, provide_payments_for_inpatient_services) :-
    age_of_infant(X_0), X_0 < 1,
    age_of_child(X_1), X_1 < 6,
    hospital_type(proportionate_share_hospital).

% atom_id: 47575fada7cccabf | chunk: 4b4cbeb448f0a18c | strength: statutory
prohibited(state, individual_child_or_pregnant_woman, deny_medical_assistance) :-
    eligibility(eligible_for_assistance_under_this_subchapter).

% atom_id: efcc63260aa6a683 | chunk: 4beeef5400816370 | strength: statutory
obligated(individual, none, complete_community_service).

% atom_id: fa2554c10bf7baf4 | chunk: 4d72e2784a24b35f | strength: statutory
permitted(state, none, provide_for_making_determinations_of_disability_or_blindness).

% atom_id: 12b5a247dd240c92 | chunk: 4d72e2784a24b35f | strength: statutory
obligated(state, individual, apply_definitions_of_disability_and_blindness).

% atom_id: 19eca42f582a31f1 | chunk: 4f8a03af8532b296 | strength: statutory
obligated(state, nursing_home_administrator, be_licensed).

% atom_id: ab8d5589b99596bb | chunk: 500543fdcc7584e7 | strength: statutory
obligated(state, individual_with_medicaid_managed_care_organization, deem_eligible_for_medicaid_benefits) :-
    enrollment_status(medicaid_managed_care_organization),
    primary_care_case_manager(true),
    eligible_organization_contract(true),
    would_lose_eligibility(true),
    minimum_enrollment_period(end_of_current_period).

% atom_id: dfafe21a19790260 | chunk: 56fb28145cf4adea | strength: regulatory
obligated(state, disabled_individual, provide_medical_assistance) :-
    resources(maximum_amount).

% atom_id: 1d5dfa140ead1e29 | chunk: 585339ad11c64817 | strength: statutory
obligated(healthcare_provider, individual, document_in_medical_record) :-
    advance_directive_status(executed).

% atom_id: 5c8a93846e723bc3 | chunk: 585339ad11c64817 | strength: statutory
obligated(healthcare_provider, individual, document_in_medical_record) :-
    advance_directive_status(not_executed).

% atom_id: b0ec584fef90b33d | chunk: 585e657fe08b2ade | strength: statutory
prohibited(state, eligible_juvenile, terminate_eligibility_for_medical_assistance) :-
    juvenile_status(eligible_juvenile),
    institution_status(inmate_of_public_institution).

% atom_id: 39cd1a014065e2c5 | chunk: 585e657fe08b2ade | strength: statutory
permitted(state, eligible_juvenile, suspend_coverage) :-
    juvenile_status(eligible_juvenile),
    institution_status(inmate_of_public_institution).

% atom_id: 7000a63bfb5b38c4 | chunk: 589b1b1a5e785f81 | strength: regulatory
obligated(physician_or_collaborating_nurse_practitioner, individual_admitted_to_facility, certify_service_requirements) :-
    service_type(skilled_nursing_facility_services_intermediate_care_facility).

% atom_id: 367e6e0a4d14af20 | chunk: 589b1b1a5e785f81 | strength: regulatory
obligated(physician_or_collaborating_nurse_practitioner, individual_admitted_to_facility, recertify_service_requirements) :-
    service_type(skilled_nursing_facility_services_intermediate_care_facility),
    services_furnished_periodically(true).

% atom_id: bbfed7fba0de957d | chunk: 58d7b2b8797fe285 | strength: regulatory
obligated(state, none, ensure_coverage) :-
    ownership_interests(items_not_covered_by_paragraphs_1_through_3),
    significance_or_rights(unique_religious_spiritual_traditional_cultural_significance).

% atom_id: 24551cf2e94f4c60 | chunk: 595950e2712554a7 | strength: regulatory
permitted(state, individual, deem_continued_eligibility) :-
    enrollment_status(group_health_plan),
    eligibility_loss(before_end_of_minimum_enrollment_period),
    minimum_enrollment_period(defined_in_subparagraph_b).

% atom_id: c18491a9139544fe | chunk: 5a7a7dc3c0618707 | strength: regulatory
obligated(state, qualified_medicare_beneficiary, apply_determination_to_services) :-
    determination_status(qualified_medicare_beneficiary).

% atom_id: d25285703897583e | chunk: 5a7a7dc3c0618707 | strength: regulatory
obligated(state, qualified_medicare_beneficiary, consider_determination_valid_for_period_of_12_months) :-
    determination_status(qualified_medicare_beneficiary).

% atom_id: d300c9dce9e8445b | chunk: 5a7a7dc3c0618707 | strength: regulatory
permitted(state, none, provide_for_more_frequent_determinations) :-
    determination_status(qualified_medicare_beneficiary).

% atom_id: ef41717e548372f0 | chunk: 5ac6609f1db3e91f | strength: regulatory
obligated(state, data_collected_under_state_plan, meet_requirements).

% atom_id: 9551572cda81844e | chunk: 5ad74dedfc12fec7 | strength: statutory
obligated(state, none, comply_with_drug_review_and_utilization_requirements).

% atom_id: f59830d37d80d4a0 | chunk: 5af9847f470c4108 | strength: regulatory
obligated(state_medicaid_agency, individual_wishing_to_make_application, have_opportunity_to_make_application).

% atom_id: b1949b006ef7fb35 | chunk: 5af9847f470c4108 | strength: regulatory
obligated(state_medicaid_agency, eligible_individual, furnish_medical_assistance).

% atom_id: e0891eed1089bf41 | chunk: 5f79d11e0d834cbd | strength: regulatory
obligated(state, entity_meeting_requirements, delegating_authority_to_conduct_review_activities) :-
    contract(meets_requirements_of_section_1320c_1),
    determination_by_secretary(none),
    contract_with_peer_review_organization(has_contract_with_secretary_under_part_b_of_subchapter_xi).

% atom_id: 2ce0ac78713a23c2 | chunk: 6026ddf3635dad7a | strength: statutory
obligated(state, none, develop_a_written_description).

% atom_id: deb7e6ed560112d8 | chunk: 6037eca0d4ba0e73 | strength: statutory
obligated(entity_participating_in_the_plan_and_providing_services, none, have_records_audited) :-
    audit_determination(necessary_to_insure_proper_payments).

% atom_id: 090a93229277cb28 | chunk: 61d5c5ba156a8f92 | strength: statutory
obligated(state, institutionalized_individuals_and_couples, provide_monthly_personal_needs_allowance).

% atom_id: 4d55e8c65ecf379b | chunk: 62011fb29f9ee1fc | strength: statutory
prohibited(state, state, permit_eligibility_determination_without_application_of_limi).

% atom_id: 08f9a7d440cf0463 | chunk: 62cf8356e25aa65c | strength: statutory
obligated(individual_driver, none, have_valid_drivers_license).

% atom_id: 68ba2882fed401ed | chunk: 6487047cddf18565 | strength: regulatory
obligated(participating_provider, pace_provider, not_require_to_pay_more_than_state_plan_amount) :-
    service_coverage(state_plan),
    individual_status(pace_program_eligible_individual),
    provider_participation(participating_under_state_plan).

% atom_id: 4ec2353f88eef0fe | chunk: 65ba68470e966dbe | strength: statutory
obligated(state, individual_or_child_or_pregnant_woman, not_discontinue_medical_assistance) :-
    aid_status(receiving_aid_under_part_a_of_subchapter_iv),
    termination_reason(terminated_pursuant_to_section_602a43_of_this_title).

% atom_id: 3e89fd79bcbbdba5 | chunk: 6785dbe6ced42127 | strength: statutory
obligated(state, pregnant_women, make_ambulatory_prenatal_care_available) :-
    period(presumptive_eligibility).

% atom_id: 38d190f1c5bc98bd | chunk: 6785dbe6ced42127 | strength: statutory
obligated(state, children, make_medical_assistance_available) :-
    period(presumptive_eligibility),
    items_and_services(section_1396r_1a).

% atom_id: 9f5f83a14bc840b0 | chunk: 6785dbe6ced42127 | strength: statutory
obligated(state, individuals, make_medical_assistance_available) :-
    period(presumptive_eligibility),
    description(section_1396r_1b).

% atom_id: d0447335677de0ad | chunk: 6785dbe6ced42127 | strength: statutory
obligated(state, individuals, make_medical_assistance_available) :-
    period(presumptive_eligibility),
    description(section_1396r_1c).

% atom_id: 474c35ddbac107b1 | chunk: 68466ede3d03da05 | strength: regulatory
obligated(state, individual_required_to_submit_social_security_number, provide_reasonable_opportunity_to_present_satisfactory_docum) :-
    required_to_submit_social_security_number(none).

% atom_id: cc828acd8fdb3d79 | chunk: 687f85b88c5c81be | strength: regulatory
obligated(state, none, establish_processes_and_use_reliable_information) :-
    purpose(verifying_community_engagement),
    paragraphs(n1_3_9aii).

% atom_id: 709792b566cc6b32 | chunk: 688d2b0ae4ba0db4 | strength: regulatory
obligated(state, third_party_with_legal_liability, consider_state_as_holder_of_individuals_rights_to_payment) :-
    payment_made_under_state_plan(none),
    third_party_has_legal_liability(none).

% atom_id: 56ba7a7b97cbde7d | chunk: 6b5b13caf5ceb49e | strength: regulatory
obligated(state, pregnant_woman, establish_income_eligibility_level).

% atom_id: 803affa2c4dfc4b3 | chunk: 6b6d42f6c188092d | strength: regulatory
obligated(state, applicable_individual, demonstrate_community_engagement) :-
    date(first_day_of_first_quarter_after_2026),
    waiver_or_demonstration_project(yes).

% atom_id: 4f7c013171b5533a | chunk: 6b6d42f6c188092d | strength: regulatory
obligated(state, applicable_individual, demonstrate_community_engagement) :-
    date(first_day_of_first_quarter_after_2026),
    waiver_or_demonstration_project(no).

% atom_id: b757eccaeb6d19b9 | chunk: 6bc41ce204050fc0 | strength: regulatory
obligated(state, state, demonstrate_progress) :-
    method_collection_reporting(satisfactory_to_secretary).

% atom_id: 34029d6a2c429f9f | chunk: 6c2bdde753482702 | strength: statutory
obligated(state, institutionalized_individual, provide_minimum_monthly_personal_needs_allowance).

% atom_id: 145b5bd6cf35d812 | chunk: 6c2bdde753482702 | strength: statutory
obligated(state, institutionalized_couple, provide_minimum_monthly_personal_needs_allowance) :-
    age(aged_blind_or_disabled),
    income_consideration(available_to_each_other).

% atom_id: d33f5eadfd1e9267 | chunk: 6e82bca1492f9b72 | strength: regulatory
obligated(state_medicaid_agency, individual_screened_for_cancer, provide_treatment_for_cancer) :-
    screening_status(screened_for_breast_or_cervical_cancer),
    cancer_status(need_treatment).

% atom_id: 778821d0a91621d3 | chunk: 6efcf4f9214617ef | strength: regulatory
obligated(state_medicaid_agency, individual_65_or_older_or_disabled, provide_medicaid_coverage) :-
    age(X_0), X_0 >= 65,
    disabled_status(true).

% atom_id: 4dd27191d1760dbf | chunk: 6f0b95facb648bb1 | strength: regulatory
obligated(secretary, information_submitted_under_system, establish_standards).

% atom_id: 2753abffc9ce6624 | chunk: 6f0b95facb648bb1 | strength: regulatory
obligated(secretary, privacy_of_information, protect).

% atom_id: 8b901f976597c91c | chunk: 6f0b95facb648bb1 | strength: regulatory
obligated(secretary, privacy_of_information, ensure).

% atom_id: 2ad4f7f3c25f2973 | chunk: 6f236ee79f3844eb | strength: statutory
obligated(secretary, none, submit_report).

% atom_id: 7845cfc191f72e9c | chunk: 6fb3396f539b6b09 | strength: regulatory
obligated(state, secretary, receive_report_submission) :-
    time_period_start(april_1_2023),
    time_period_end(june_30_2024).

% atom_id: b89902e3339f5205 | chunk: 6fb3396f539b6b09 | strength: regulatory
obligated(state, public, receive_publicly_available_information) :-
    time_period_start(april_1_2023),
    time_period_end(june_30_2024).

% atom_id: 0c23c1a2c0733253 | chunk: 7013073133846eb5 | strength: regulatory
obligated(state_agency, none, develop_alternate_plans_of_care) :-
    recipient_age(X_0), X_0 >= 65,
    recipient_need(would_otherwise_need_care_in_such_institutions).

% atom_id: fd908c1f4b9b9b0f | chunk: 7013073133846eb5 | strength: regulatory
obligated(state_agency, none, utilize_available_resources_maximally) :-
    recipient_age(X_0), X_0 >= 65,
    recipient_need(would_otherwise_need_care_in_such_institutions).

% atom_id: 60d2ce9c5f2e4259 | chunk: 7013073133846eb5 | strength: regulatory
obligated(state_agency, none, provide_services) :-
    recipient_age(X_0), X_0 >= 65,
    service_type(section_303a4ai_and_ii_section_1383a4ai_and_ii).

% atom_id: 2934773cea5af0be | chunk: 7013073133846eb5 | strength: regulatory
obligated(state_agency, none, implement_methods_of_administration) :-
    recipient_age(X_0), X_0 >= 65,
    recipient_need(would_otherwise_need_care_in_such_institutions).

% atom_id: f9b6c9016988cf41 | chunk: 70d51bc7393677cb | strength: statutory
prohibited(state, citizen_of_the_united_states, exclude_from_medicaid_program).

% atom_id: ef2b52b4241d081d | chunk: 717f21620a2ef55b | strength: regulatory
obligated(provider, none, include_in_description).

% atom_id: d2acbc379993efde | chunk: 71d59c2c50a8ee9c | strength: regulatory
obligated(state_or_local_agency, institutions_and_agencies, determine_participation_requirements) :-
    section_1395aa_a(first_sentence).

% atom_id: 4768489eb8ccfb7a | chunk: 71d59c2c50a8ee9c | strength: regulatory
obligated(state_or_local_agency, institutions_and_agencies, perform_function_of_determining_participation_requirements) :-
    section_1395aa_a(first_sentence).

% atom_id: a6ff5d8c6a01ce84 | chunk: 71d59c2c50a8ee9c | strength: regulatory
permitted(secretary, individual_institutions_and_agencies, validate_state_determinations) :-
    section_1396r_g(cause_to_question).

% atom_id: d58890ca8d65a8ec | chunk: 71d59c2c50a8ee9c | strength: regulatory
obligated(secretary, individual_institutions_and_agencies, make_independent_and_binding_determinations) :-
    section_1396r_g(cause_to_question).

% atom_id: 60679aebd735d17c | chunk: 746d6db881332081 | strength: regulatory
obligated(state, health_care_practitioner_and_provider, provide_information_access).

% atom_id: e10ce71b929e829a | chunk: 7535eee99afa13a7 | strength: statutory
obligated(state_authority, applicant_or_recipient, determine_eligibility_and_extents_of_medical_assistance) :-
    subchapter(i_x_xiv_xvi_iv_a).

% atom_id: 803690612465f032 | chunk: 7535eee99afa13a7 | strength: statutory
obligated(state_authority, applicant_or_recipient, consider_only_available_income_and_resources) :-
    subchapter(i_x_xiv_xvi_iv_a).

% atom_id: 410dbd00baa7c65c | chunk: 7535eee99afa13a7 | strength: statutory
obligated(state_authority, applicant_or_recipient, evaluate_income_or_resources_reasonably) :-
    subchapter(i_x_xiv_xvi_iv_a).

% atom_id: 78e38b21e5aa388c | chunk: 7535eee99afa13a7 | strength: statutory
obligated(state_authority, applicant_or_recipient, not_consider_financial_responsibility_except_spouse_or_child) :-
    subchapter(i_x_xiv_xvi_iv_a).

% atom_id: 36364c57252d617b | chunk: 7535eee99afa13a7 | strength: statutory
obligated(state_authority, applicant_or_recipient, provide_flexibility_in_applying_eligibility_standards) :-
    subchapter(i_x_xiv_xvi_iv_a).

% atom_id: bd9be1cba0444319 | chunk: 75c85693dbaad991 | strength: statutory
obligated(ordering_or_referring_physician_or_other_professional, none, specify_npi_on_claim).

% atom_id: e7a6ded43f85864b | chunk: 77a40b73b2ff0ea8 | strength: regulatory
permitted(state_agency, applicant, provide_signature) :-
    eligibility_element(medical_assistance_child_health_assistance).

% atom_id: 7b2981b155e4adeb | chunk: 77a40b73b2ff0ea8 | strength: regulatory
permitted(state_agency, applicant, use_electronic_signature) :-
    application_type(medical_assistance).

% atom_id: 5feca420505a9d11 | chunk: 79230eb4bfa39824 | strength: regulatory
obligated(state, none, implement_payment_models) :-
    payment_models(section_1315ac),
    nationwide_basis(true).

% atom_id: c5a02d565cbfe8a8 | chunk: 79230eb4bfa39824 | strength: regulatory
prohibited(state, none, implement_payment_models) :-
    payment_models(section_1315ac),
    nationwide_basis(false),
    administrative_feasibility(threshold).

% atom_id: f564e3743de13316 | chunk: 7acfa95ad4157949 | strength: statutory
obligated(state, pregnant_woman, continue_to_be_eligible_for_medical_assistance) :-
    eligibility_status(eligible_and_received_medical_assistance),
    application_status(applied_for).

% atom_id: ca4045dde57a7065 | chunk: 7cf047f83d037029 | strength: regulatory
obligated(pr_state, administrator_of_the_centers_for_medicare_and_medicaid_servi, submit_documentation) :-
    request_received(true).

% atom_id: a751b877ca3beb1c | chunk: 7e17db878de446e6 | strength: statutory
obligated(state, hospital, take_alternative_action).

% atom_id: f77a65e37119038c | chunk: 7ef247e12b8e2baf | strength: statutory
prohibited(state, none, application_of_subparagraphs_a_and_b) :-
    agreement_status(in_effect_as_of_close_of_fiscal_year),
    agreement_description(agreement_in_paragraph_2b).

% atom_id: 4915bb385b9e2270 | chunk: 7fdebf366674eb68 | strength: statutory
obligated(individual, none, enroll_in_educational_program) :-
    enrollment_status(half_time).

% atom_id: d9a23fdd969d7fe5 | chunk: 800a2d58fc1bbd85 | strength: regulatory
obligated(state_agency, none, make_reports) :-
    requirement(secretary).

% atom_id: d38b22842539a6da | chunk: 800a2d58fc1bbd85 | strength: regulatory
obligated(state_agency, none, comply_with_provisions) :-
    requirement(secretary).

% atom_id: 29783b3390c23148 | chunk: 8020e1a5707739c9 | strength: statutory
obligated(state, none, not_apply_expense_block_or_income_disregard).

% atom_id: 42acc55000908e60 | chunk: 8036ea6f95070448 | strength: statutory
prohibited(secretary, none, waive_compliance) :-
    requirements_of_this_paragraph(none).

% atom_id: 7b2c6bcf7017af76 | chunk: 803dde804bfb9c9c | strength: regulatory
obligated(state_medicaid_agency, none, enter_into_cooperative_arrangements) :-
    responsible_for_administration_or_supervision_of_health_serv(true),
    responsible_for_administration_or_supervision_of_vocational(true).

% atom_id: cf43ec99aeaf9de9 | chunk: 803dde804bfb9c9c | strength: regulatory
obligated(state_medicaid_agency, none, enter_into_agreements) :-
    receiving_payments_under_subchapter_v(true).

% atom_id: 868e63da956d4dbb | chunk: 803dde804bfb9c9c | strength: regulatory
obligated(state_medicaid_agency, none, utilize_agencies_in_furnishing_care_and_services) :-
    receiving_payments_under_subchapter_v(true),
    care_and_services_included_in_state_plan(true).

% atom_id: 62933b32f1b3f8a1 | chunk: 803dde804bfb9c9c | strength: regulatory
obligated(state_medicaid_agency, none, reimburse_agencies_for_cost_of_care_and_services) :-
    receiving_payments_under_subchapter_v(true),
    individual_for_which_payment_would_otherwise_be_made_to_stat(true).

% atom_id: 34ef5e9b99750fbd | chunk: 803dde804bfb9c9c | strength: regulatory
obligated(state_medicaid_agency, none, coordinate_operations_with_state_programs) :-
    operations_under_this_subchapter(true),
    state_operations_under_special_supplemental_nutrition_progra(true).

% atom_id: a90546c970d1f797 | chunk: 8097165d63222382 | strength: regulatory
obligated(state_authority, individual_who_has_attained_19_years_of_age, disregard_first_2000_received_as_compensation_for_participat) :-
    age(19),
    compensation_amount(2000),
    clinical_trial_requirements(section_1382ab26).

% atom_id: d09b65c8f1d2e36d | chunk: 82e65c8e9b6fba62 | strength: statutory
obligated(state, none, establish_or_designate_single_state_agency).

% atom_id: 26fde60af90c43cf | chunk: 82e65c8e9b6fba62 | strength: statutory
obligated(state, none, administer_or_supervise_administration_of_plan).

% atom_id: 3de9b6e2e671ba1a | chunk: 82e65c8e9b6fba62 | strength: statutory
obligated(state_or_local_agency_administering_state_plan, individual, determine_eligibility_for_medical_assistance) :-
    subchapter(i),
    eligibility(true).

% atom_id: bb93e5585ee2ce06 | chunk: 82e65c8e9b6fba62 | strength: statutory
obligated(agency_or_agencies_administering_supplemental_security_incom, individual, determine_eligibility_for_medical_assistance) :-
    subchapter(xvi).

% atom_id: b923bd7b8cb2f846 | chunk: 82e65c8e9b6fba62 | strength: statutory
obligated(agency_or_agencies_administering_state_plan_approved_under_p, individual, determine_eligibility_for_medical_assistance) :-
    subchapter(xvi),
    eligibility(false).

% atom_id: 3f6a1f814d233bac | chunk: 8356560b83d40b02 | strength: regulatory
prohibited(state_medicaid_agency, individual, include_costs_in_income_determination).

% atom_id: 6a09c7e5a1df9f8e | chunk: 83a4306771793a59 | strength: regulatory
obligated(physician_submitting_claim, none, receive_payment) :-
    service_period(X_0), X_0 <= 14,
    arrangement_type(informal_reciprocal_arrangement).

% atom_id: 739cdec00d335647 | chunk: 83a4306771793a59 | strength: regulatory
obligated(physician_submitting_claim, none, receive_payment) :-
    service_period(X_0), X_0 <= 90,
    arrangement_type(per_diem_or_other_fee_for_time_compensation).

% atom_id: a1d689e81f2adf2c | chunk: 83a4306771793a59 | strength: regulatory
obligated(physician_furnishing_services, none, be_identified_in_claim) :-
    service_period(X_0), X_0 <= 14,
    arrangement_type(informal_reciprocal_arrangement).

% atom_id: 8f1d6db82a7563c5 | chunk: 83a4306771793a59 | strength: regulatory
obligated(physician_furnishing_services, none, be_identified_in_claim) :-
    service_period(X_0), X_0 <= 90,
    arrangement_type(per_diem_or_other_fee_for_time_compensation).

% atom_id: 56cece905cbe584d | chunk: 8571e931672e4e91 | strength: statutory
prohibited(health_insurer, none, consider_eligibility_for_medicaid) :-
    individual_is_eligible(true),
    individual_receives_medical_assistance(true).

% atom_id: 91c0477d123aa824 | chunk: 85e00789d905fd84 | strength: statutory
obligated(state_agencies, hospitals_nursing_facilities_home_health_agencies_clinics_la, provide_consultative_services) :-
    date(july_1_1969).

% atom_id: d041729bb3efe14f | chunk: 8855e0b5fd5c97d1 | strength: statutory
obligated(state_or_local_agency, none, seek_reimbursement) :-
    legal_liability_exists(none),
    reimbursement_amount(costs_of_recovery).

% atom_id: 81adf08b3d3995c4 | chunk: 889e57089d6616c7 | strength: regulatory
obligated(secretary, none, deem_satisfactory_progress) :-
    territory_description(paragraph_1),
    good_faith_effort(true).

% atom_id: bc182379d88f5415 | chunk: 897dea2b02196bbc | strength: regulatory
obligated(state, federally_qualified_health_center, provide_payment_for_services) :-
    fiscal_year(X_0), X_0 >= 2001,
    service_start_date(X_1), X_1 >= 2001.

% atom_id: beb5db61d1869bf6 | chunk: 897dea2b02196bbc | strength: regulatory
obligated(state, rural_health_clinic, provide_payment_for_services) :-
    fiscal_year(X_0), X_0 >= 2001,
    service_start_date(X_1), X_1 >= 2001.

% atom_id: d3d6fc4f7e3f18c0 | chunk: 8b23f3a262f21e82 | strength: statutory
permitted(state, none, provide_payment_to_federally_qualified_health_center_or_rura) :-
    service_type(section_1396d_a_2_c_services_section_1396d_a_2_b_services).

% atom_id: 06d32a5796b09bfe | chunk: 8cc2ee09c8f4a372 | strength: regulatory
obligated(state, pregnant_woman, deem_to_continue_being_described_in_subsection_a10) :-
    is_pregnant(true),
    family_income_change(true),
    previously_described_in_subsection_a10(true).

% atom_id: bad24100eac1522f | chunk: 8cc2ee09c8f4a372 | strength: regulatory
prohibited(state, pregnant_woman, apply_change_of_income) :-
    is_pregnant(true),
    family_income_change(true),
    previously_described_in_subsection_a10(true).

% atom_id: 026c8ebad63e4a3b | chunk: 8cc2ee09c8f4a372 | strength: regulatory
permitted(state, pregnant_woman, provide_ambulatory_prenatal_care) :-
    is_pregnant(true),
    has_presumptive_eligibility(true).

% atom_id: 2ce468c883f085c5 | chunk: 8cc2ee09c8f4a372 | strength: regulatory
prohibited(state, pregnant_woman, determine_ineligible_for_medical_assistance) :-
    is_pregnant(true),
    has_presumptive_eligibility(true),
    determined_ineligible(true).

% atom_id: 585b557d65d87987 | chunk: 8e6e993afd7f8b70 | strength: statutory
obligated(government_authority, center_or_clinic, pay_amount).

% atom_id: e531f1b3015e3824 | chunk: 8f8aa7b9e7672598 | strength: statutory
obligated(individual, none, earn_income) :-
    monthly_income(applicable_minimum_wage_80_hours).

% atom_id: 0a82efb16b9684be | chunk: 90338f0f1dbb60c5 | strength: statutory
obligated(state_authority, individual, be_deemed_eligible_for_minimum_essential_coverage) :-
    eligibility_for_medical_assistance(none),
    failure_to_meet_community_engagement_requirement(none).

% atom_id: 76abe6590a3e76cc | chunk: 91445045b74674d4 | strength: statutory
obligated(state, individual_misidentified_as_deceased, re_enroll_under_state_plan) :-
    misidentification_status(deceased),
    disenrollment_reason(death_master_file),
    disenrollment_action(medical_assistance).

% atom_id: 5083a8a3e6c1b81a | chunk: 91c5efe7b6e9d066 | strength: statutory
obligated(disclosing_entity, none, comply_with_requirements).

% atom_id: ab7fb6827cff5ad2 | chunk: 9217de04962020fc | strength: regulatory
obligated(state, federally_qualified_health_center_or_rural_health_clinic, provide_payment_for_services) :-
    qualification_date(X_0), X_0 > 2000.

% atom_id: 868a5fb80d4d0983 | chunk: 9217de04962020fc | strength: regulatory
obligated(state, federally_qualified_health_center_or_rural_health_clinic, calculate_payment_amount) :-
    qualification_date(X_0), X_0 > 2000.

% atom_id: 384e038809834a1b | chunk: 9217de04962020fc | strength: regulatory
obligated(state, federally_qualified_health_center_or_rural_health_clinic, provide_payment_for_services) :-
    qualification_date(X_0), X_0 > 2000.

% atom_id: a79dc182976af99f | chunk: 9217de04962020fc | strength: regulatory
obligated(state, federally_qualified_health_center_or_rural_health_clinic, provide_payment_for_services) :-
    qualification_date(X_0), X_0 > 2000.

% atom_id: 2fad3bcc7467c6d2 | chunk: 935a84f531bac0b5 | strength: statutory
obligated(secretary, none, establish_a_system).

% atom_id: 17e37ebff6818962 | chunk: 93a0d80f4245f4ea | strength: regulatory
obligated(state, public_and_facility, receive_notice).

% atom_id: bc4f395b07220dac | chunk: 93a0d80f4245f4ea | strength: regulatory
obligated(state, facility, terminate_payment_denial_effectiveness) :-
    state_findings(substantial_compliance),
    good_faith_efforts(true).

% atom_id: 36702fbc6ddafa39 | chunk: 93a0d80f4245f4ea | strength: regulatory
obligated(state, facility, terminate_payment_denial_effectiveness) :-
    paragraph_1_b_case(true),
    eleventh_month_after_effective_date(true).

% atom_id: da82a64662c6141c | chunk: 93a0d80f4245f4ea | strength: regulatory
obligated(state, facility, terminate_facility_certification) :-
    clause_b_applicability(true),
    failure_to_substantially_meet_provisions(true).

% atom_id: 4bfaa972da78a8fe | chunk: 93d2ba5d7f4af057 | strength: statutory
permitted(state, none, impose_charges) :-
    type_of_charge(enrollment_fees_premiums_similar_charges_deductions_cost_sha).

% atom_id: c81e9ae55d72c27d | chunk: 93d2ba5d7f4af057 | strength: statutory
obligated(state, none, impose_deductions_cost_sharing) :-
    type_of_individual(specified_individuals),
    care_items_or_services(furnished).

% atom_id: 676fe096bd3dda11 | chunk: 93dd74038086a49c | strength: statutory
permitted(state_medicaid_agency, individual_eligible_for_medical_assistance, obtain_medical_assistance) :-
    eligibility_status(eligible_for_medical_assistance).

% atom_id: 202e21e9234bc0e4 | chunk: 93dd74038086a49c | strength: statutory
permitted(qualified_institution_or_person, individual_eligible_for_medical_assistance, provide_services) :-
    eligibility_status(eligible_for_medical_assistance).

% atom_id: ac0948b9977b4b23 | chunk: 93dd74038086a49c | strength: statutory
prohibited(medicaid_managed_care_organization_or_similar_entity, individual_eligible_for_medical_assistance, restrict_choice_of_provider) :-
    eligibility_status(eligible_for_medical_assistance),
    enrollment_status(enrolled_in_primary_care_case_management_system_or_medicare).

% atom_id: 9b2e2a619b68eb13 | chunk: 93dd74038086a49c | strength: statutory
prohibited(state_medicaid_agency, individual_eligible_for_medical_assistance, require_medicaid_coverage_for_convicted_persons) :-
    conviction_status(convicted_of_felony),
    state_agency_determination(inconsistent_with_best_interests_of_beneficiaries).

% atom_id: 347020c523d845e5 | chunk: 93dd74038086a49c | strength: statutory
prohibited(state_medicaid_agency, provider_or_supplier_with_moratorium, require_medicaid_coverage) :-
    moratorium_status(under_moratorium).

% atom_id: 9d5a831b47a4a3eb | chunk: 9713b65bc9b0ba80 | strength: regulatory
obligated(state_medicaid_agency, individual_eligible_for_medical_assistance, provide_medicaid_coverage) :-
    eligibility_determination(true),
    application_month(X_1), X_1 <= 3.

% atom_id: 2be45bfd7b125e86 | chunk: 995efa9989b276f5 | strength: statutory
obligated(state, recipients_of_medical_support, assign_rights_of_payment).

% atom_id: 8ca7c4c85ac220f1 | chunk: 9c547d2ef23c3138 | strength: statutory
obligated(state, individual_who_is_an_indian, disregard_property_from_resources).

% atom_id: 73f4f45e700b8663 | chunk: 9da8579175d984bc | strength: regulatory
obligated(state, none, not_required_to_provide_payment) :-
    service(deductibles_coinsurance_or_copayments_for_medicare_cost_shar),
    payment_exceeds(payment_amount_under_subchapter_xviii).

% atom_id: 4d2722251950df85 | chunk: 9dd040fbe06f81cc | strength: statutory
obligated(state, physician, maintain_a_list) :-
    update_frequency(monthly).

% atom_id: 40984615190337d3 | chunk: 9dd040fbe06f81cc | strength: statutory
obligated(state, physician, contain_each_physicians_unique_identifier) :-
    identifier_source(system_established_under_subsection_x).

% atom_id: 2775463fff2b0511 | chunk: 9dd040fbe06f81cc | strength: statutory
obligated(state, physician, list_all_physicians_certified_to_participate) :-
    certification_status(certified).

% atom_id: b3b3a326c22dfcec | chunk: 9e8f6556a46ca0bb | strength: regulatory
obligated(state, individual_and_family, use_modified_adjusted_gross_income) :-
    family_size(X_0), X_0 > 1.

% atom_id: 0937ed6fcb566135 | chunk: 9e8f6556a46ca0bb | strength: regulatory
obligated(state, individual_and_family, use_household_income) :-
    family_size(X_0), X_0 > 1.

% atom_id: de73cfaa20415b7c | chunk: 9e8f6556a46ca0bb | strength: regulatory
obligated(state, population_eligible_for_medical_assistance, establish_income_eligibility_thresholds) :-
    date(march_23_2010).

% atom_id: a129459044d5dfda | chunk: 9e8f6556a46ca0bb | strength: regulatory
obligated(state, individual_eligible_for_medical_assistance_on_march_23_2010, ensure_continued_coverage) :-
    date(march_23_2010).

% atom_id: 2797bc349e3d94de | chunk: 9e8f6556a46ca0bb | strength: regulatory
obligated(secretary, states, waive_provisions) :-
    purpose(ensure_income_and_eligibility_systems).

% atom_id: dcbff067be695b36 | chunk: 9f08a003b2311313 | strength: statutory
permitted(secretary, none, include_transportation_options).

% atom_id: c13676b904daf105 | chunk: 9f7e740f14247ad0 | strength: statutory
permitted(state, parent, provide_payment_for_medical_assistance) :-
    subparagraph_applies(a_applies).

% atom_id: c2bd90ff42dbfbff | chunk: a01fd97bf529183e | strength: regulatory
permitted(hospital, none, elect_to_be_a_qualified_entity) :-
    is_participating_provider(true).

% atom_id: a0bb5949b278d8d8 | chunk: a1c106d651f0e039 | strength: regulatory
obligated(secretary, state, require_state_to_provide_medical_assistance) :-
    state_status(providing_medical_assistance_to_residents_under_a_waiver_gra).

% atom_id: cd94f7b8d28145b0 | chunk: a555bac772deb5ec | strength: regulatory
obligated(puerto_rico, centers_for_medicare_and_medicaid_services_administrator, report_on_selected_measures) :-
    date(X_0), X_0 >= 12.

% atom_id: 8e70a0252d30a657 | chunk: a77486da946d421e | strength: regulatory
obligated(state, family, determine_income).

% atom_id: f55f10f223519e51 | chunk: a77486da946d421e | strength: regulatory
prohibited(state, medical_care_provider, consider_costs) :-
    care_type(medical_or_remedial).

% atom_id: e78b2182cc0e014b | chunk: a9320d21792c99da | strength: statutory
prohibited(beneficiary, none, have_legal_liability_to_make_payment).

% atom_id: 118b9655fe7a499f | chunk: abb0c3b6b6086f8f | strength: statutory
obligated(state, facility, terminate_certification) :-
    immediate_jeopardy(none).

% atom_id: 660fa93ea2808dcb | chunk: abb0c3b6b6086f8f | strength: statutory
permitted(state, state, provide) :-
    immediate_jeopardy(none).

% atom_id: c936d910b7d2651f | chunk: abb57b887cdf5011 | strength: statutory
prohibited(state_medicaid_agency, individual, include_costs_in_income_determination) :-
    type_of_care(medical),
    type_of_care(remedial).

% atom_id: 5319742e6c73539b | chunk: ad8d3cd9d40aa0d9 | strength: regulatory
obligated(state_authority, none, provide_safeguards).

% atom_id: 3cbed2e7737572fa | chunk: ad8d3cd9d40aa0d9 | strength: regulatory
obligated(state_authority, recipients, determine_eligibility_for_care_and_services).

% atom_id: 39a2ad85d8a79046 | chunk: ad8d3cd9d40aa0d9 | strength: regulatory
obligated(state_authority, recipients, provide_care_and_services).

% atom_id: afedd84540f1b214 | chunk: ae4c1fd1126acfe5 | strength: statutory
obligated(secretary, none, not_authorize_denial_or_limitation_of_payments).

% atom_id: 463485a11113803b | chunk: af2623a889c77236 | strength: regulatory
obligated(state, individuals, establish_income_level) :-
    income_level(n133_percent_of_fpl).

% atom_id: c9d2185353985761 | chunk: b0ba65d779f1e067 | strength: statutory
obligated(state, individual_enrolled_for_medical_assistance, review_death_master_file_or_successor_system) :-
    frequency(quarterly).

% atom_id: f9854998f8ea04cc | chunk: b12edf1b89ad4617 | strength: statutory
obligated(state, none, provide_education).

% atom_id: da273d536e3f4d28 | chunk: b2aa4a1be5bfece8 | strength: statutory
obligated(entity_receiving_or_making_payments, none, comply_with_conditions) :-
    annual_payment_amount(n5000000).

% atom_id: 7c79a378b8e5c687 | chunk: b3b0801ab5145eaa | strength: regulatory
obligated(state_medicaid_agency, individual_receiving_hospice_care, provide_payment_for_hospice_care) :-
    care_type(hospice_care).

% atom_id: 841c00ab89295f3d | chunk: b3b0801ab5145eaa | strength: regulatory
obligated(state_medicaid_agency, individual_receiving_hospice_care_in_nursing_facility_or_int, provide_additional_payment_to_account_for_room_and_board) :-
    care_type(hospice_care),
    residency_status(nursing_facility_or_intermediate_care_facility_for_the_menta),
    eligibility_for_nursing_facility_services(would_be_eligible_if_not_receiving_hospice_care).

% atom_id: 3e760ae5ab98eaac | chunk: b46a130785bfcf56 | strength: regulatory
obligated(state, information, request_and_exchange).

% atom_id: 31b699b59faee00c | chunk: b56cc9821e9d7927 | strength: regulatory
obligated(state_agency, none, provide_assurances).

% atom_id: 931bf2dec3c1ad71 | chunk: b5826f3caa642a7c | strength: regulatory
obligated(state, national_system, report_criminal_and_civil_convictions_sanctions_negative_lic).

% atom_id: 932c8c564dbe1d4c | chunk: b682d043116e46ed | strength: statutory
obligated(secretary, none, require_data_reporting).

% atom_id: 5768ef4ad1dcc31a | chunk: b682d043116e46ed | strength: statutory
obligated(state_or_waiver_authority, individual_eligible_for_medical_assistance, report_data) :-
    data_reporting_determined_necessary(true).

% atom_id: 5abf96246bb09be9 | chunk: b70e51339b769624 | strength: statutory
obligated(state_health_agency_or_other_appropriate_state_medical_agenc, private_or_public_institutions, establish_and_maintain_health_standards).

% atom_id: bfae806a603a83ec | chunk: b71c97e852ee572b | strength: statutory
obligated(state, hospital, provide_no_payment) :-
    date(X_0), X_0 after 3,
    admission_date(end_of_3_month_period).

% atom_id: 2a8bbd7e5d810d6f | chunk: b78ed34208078215 | strength: statutory
obligated(individual, none, participate_in_work_program).

% atom_id: 44392a008bc005cf | chunk: b7ddcd3148767a5e | strength: statutory
obligated(state, supplier_of_medical_assistance, issue_provider_numbers) :-
    type_of_suppliers(durable_medical_equipment).

% atom_id: 271b9068c190cfad | chunk: b7ddcd3148767a5e | strength: statutory
prohibited(state, supplier_of_medical_assistance, issue_or_renew_provider_numbers) :-
    type_of_suppliers(durable_medical_equipment),
    condition_met(true).

% atom_id: ae3199b8411a438b | chunk: b922102006713e7b | strength: statutory
obligated(state, none, submit_state_plan_for_medical_assistance).

% atom_id: 76fb3a15743e52e1 | chunk: bd8f3b3660ca50b0 | strength: statutory
permitted(state, none, elect_to_phase_in_extension_of_eligibility) :-
    categorical_group(nonpregnant_childless_adults),
    income(any).

% atom_id: ab8878892609bae9 | chunk: bd8f3b3660ca50b0 | strength: statutory
prohibited(state, individuals_with_higher_income, extend_eligibility_before_lower_income_individuals) :-
    income(lower_income).

% atom_id: 71573400b2b0157d | chunk: becbcf42f2719d48 | strength: regulatory
obligated(state_medicaid_agency, program_registered_providers, distribute_pediatric_vaccines).

% atom_id: 016e361231e5613c | chunk: becbcf42f2719d48 | strength: regulatory
obligated(program_registered_providers, vaccine_eligible_children, immunize_with_vaccines).

% atom_id: 60f98e9ee211ad14 | chunk: bfa564551c49fb64 | strength: statutory
prohibited(person_furnishing_service, individual_or_financially_responsible_relative_or_representa, seek_to_collect_payment) :-
    total_liabilities_of_third_parties(amount_payable_for_service_under_plan_disregarding_1396o),
    amount_to_be_collected(variable_lesser_of_operator_i_value_amount_may_be_collected).

% atom_id: f35547a0d7c2c0ff | chunk: c0ed1123b9bbbc9e | strength: statutory
obligated(state, eligibility_standards_methodologies_or_procedures, not_have_in_effect) :-
    period_start(march_23_2010),
    period_end(none),
    exchange_status(exchange_established_by_state).

% atom_id: 87b844bc5a7ed21a | chunk: c17374e692a63117 | strength: regulatory
obligated(state, none, determine_savings_exceedance) :-
    enrollment(cobra_continuation_coverage).

% atom_id: a0ff55149ed6b759 | chunk: c6487c732b49d545 | strength: regulatory
obligated(state_medicaid_agency, none, ensure_compliance) :-
    requirement_source(state_law_statutory_or_as_recognized_by_the_courts_of_the_st).

% atom_id: 7f15a5ab9c80d718 | chunk: c7df98236b476658 | strength: regulatory
obligated(state, person_or_institution_providing_services, keep_records).

% atom_id: e921eeeacd3c2896 | chunk: c7df98236b476658 | strength: regulatory
obligated(state, person_or_institution_providing_services, furnish_information).

% atom_id: 376dd2b2f5680eda | chunk: c7fc83c482efb791 | strength: statutory
prohibited(state, nonpregnant_nondisabled_adults_eligible_for_medical_assistan, apply_requirement_under_paragraph_1) :-
    income(X_0), X_0 > 133,
    certification_date(december_312010),
    state_fiscal_year_deficit_status(budget_deficit_projected_budget_deficit).

% atom_id: 156ce7496e281d78 | chunk: c9e42aba9ce16359 | strength: statutory
permitted(state, none, consider_only_income_of_applicant_or_recipient).

% atom_id: 07f022a0b49881f4 | chunk: cabcfa9493f7bc72 | strength: regulatory
obligated(state, individual_65_or_older_in_public_institution_for_mental_dise, provide_medical_assistance) :-
    age(X_0), X_0 >= 65,
    location(public_institution_for_mental_diseases).

% atom_id: d536b0d579c8a102 | chunk: cabcfa9493f7bc72 | strength: regulatory
obligated(state, public, develop_and_implement_comprehensive_mental_health_program) :-
    age(X_0), X_0 >= 65,
    location(public_institution_for_mental_diseases).

% atom_id: c9c7dea456daa22b | chunk: cb3f8cf93f3308d4 | strength: regulatory
obligated(state, none, satisfy_requirements) :-
    fiscal_quarter(july_1_2023_june_30_2024).

% atom_id: d8ca9fbc7ded139c | chunk: cd8df9c359ddb5d1 | strength: statutory
obligated(state, providers_and_suppliers, comply_with_disclosure_requirements).

% atom_id: c0c9a73b4e8becb7 | chunk: ce02710ae0e6dbf6 | strength: regulatory
obligated(state, children_enrolled_under_state_plan_or_waiver, monitor_and_manage_appropriate_use_of_antipsychotic_medicati) :-
    age(X_0), X_0 <= 18.

% atom_id: 9f310959d6ea1b90 | chunk: ce02710ae0e6dbf6 | strength: regulatory
obligated(state, children_in_foster_care, monitor_and_manage_appropriate_use_of_antipsychotic_medicati) :-
    age(X_0), X_0 <= 18.

% atom_id: 899326ba16d360c0 | chunk: cfd453dcb7c69203 | strength: regulatory
prohibited(hospital, none, provide_services_as_substitute).

% atom_id: daae513f4738e92e | chunk: d0085b425bb43c94 | strength: statutory
obligated(government_authority, provider_or_organization, impose_sanction) :-
    charge(excess).

% atom_id: 2be334bd5b3826b3 | chunk: d05c08df83f2cc73 | strength: regulatory
obligated(state, federally_qualified_health_center_or_rural_health_clinic, agree_to_payment_schedule).

% atom_id: 265bde377c6a77ba | chunk: d05c08df83f2cc73 | strength: regulatory
obligated(state_and_federally_qualified_health_center_or_rural_health, none, make_supplemental_payment) :-
    frequency(every_4_months).

% atom_id: 3ba3f1044a4b76a8 | chunk: d144d2c9b0e49bd0 | strength: regulatory
obligated(state, providers_and_suppliers, establish_compliance_program) :-
    status(under_state_plan_under_waiver_of_plan).

% atom_id: 3eb4a959be33df58 | chunk: d15b9d54514776aa | strength: statutory
prohibited(state, financial_institution_or_entity, provide_payments_for_items_or_services) :-
    location(united_states).

% atom_id: 517c1ad0061eb960 | chunk: d2827b4dedcafd60 | strength: statutory
obligated(state, provider_or_individual_driver_of_nonemergency_transportation, provide_mechanism_for_attestation) :-
    service_type(nonemergency_transportation),
    recipient_of_service(medically_necessary_services).

% atom_id: c6dae672022a7ee0 | chunk: d2cc92a27ae720e0 | strength: regulatory
obligated(secretary, none, review_termination) :-
    provider_participation_terminated(true),
    notification_received(true).

% atom_id: 79e113bbd7c0ae29 | chunk: d34629a7b47730d3 | strength: regulatory
obligated(state, none, provide_payment_for_services) :-
    fiscal_year(n2002_or_a_succeeding_fiscal_year).

% atom_id: 27d65c1fd9ff77ac | chunk: d3b7589db899e84b | strength: statutory
permitted(state, none, appoint_advisory_committee_and_designee).

% atom_id: 61e08d84579777ac | chunk: d4da92c2d3c917bb | strength: statutory
obligated(state, none, ensure_effectiveness_in_all_political_subdivisions).

% atom_id: 5bd6c60582a2963d | chunk: d4da92c2d3c917bb | strength: statutory
obligated(political_subdivision, none, comply_with_mandatory_requirements).

% atom_id: 51d8eed7491f7ff1 | chunk: d6ab6ccea32f1dca | strength: regulatory
obligated(state_medicaid_agency, none, comply_with_provisions).

% atom_id: aca5dacd8e80847c | chunk: d9c2f58c81f6589e | strength: regulatory
prohibited(secretary, state, approve_state_plan_for_medical_assistance) :-
    individuals(l1),
    requirement(apply_for_assistance_under_the_state_program_funded_under_pa).

% atom_id: 3fc5bd14e74ee24a | chunk: daf0496974fd21fd | strength: statutory
prohibited(state, individual, affect_rights_to_appeal_disenrollment).

% atom_id: b6480278b8154d99 | chunk: dbed7da0bb0d0223 | strength: regulatory
obligated(state, consumer, maintain_consumer_oriented_website).

% atom_id: c952599eca85a57f | chunk: dbed7da0bb0d0223 | strength: regulatory
obligated(state, skilled_nursing_facility_and_nursing_facility, provide_information).

% atom_id: 614f04613171dec8 | chunk: dc0c9fb56175dae0 | strength: regulatory
permitted(state, none, make_payment_directly_to_vaccine_manufacturer) :-
    vaccine_administration_date(X_0), X_0 < 1994,
    individual_status(entitled_to_medical_assistance).

% atom_id: 378561ed84c8ce30 | chunk: ddb64898c0330017 | strength: regulatory
obligated(state, individual_65_or_older_institution_for_mental_diseases, include_medical_assistance) :-
    age(X_0), X_0 >= 65,
    institution_type(institutions_for_mental_diseases).

% atom_id: c1b9d4164e113950 | chunk: ddd6788a205c5723 | strength: statutory
permitted(state, state, provide_for_reduction_of_payment_amount) :-
    person_furnishing_services(subsection_a25c).

% atom_id: facba5f2371cec14 | chunk: de6aa03232782838 | strength: regulatory
obligated(state_authority, persons_under_21_eligible_for_medical_assistance, inform_of_availability_and_need) :-
    age(X_0), X_0 < 21,
    eligibility_status(eligible_for_medical_assistance).

% atom_id: 790bb42e738e4bf5 | chunk: dee8bedfdfea44c1 | strength: statutory
permitted(residential_pediatric_recovery_center, mothers_of_infants_receiving_treatment, offer_counseling_and_other_services) :-
    services_coverage(state_plan_waiver).

% atom_id: eff98f0d3f09fd6a | chunk: df179ec135e3c4f4 | strength: statutory
obligated(state, individual_entitled_to_nursing_facility_services, include_home_health_services).

% atom_id: 5d537d8d0f245c5a | chunk: df4d155553481fe2 | strength: statutory
obligated(state, hospital, terminate_participation) :-
    health_and_safety_jeopardy(none).

% atom_id: 019cb6ac3016c187 | chunk: e02559bcbae0053c | strength: statutory
obligated(state_agency, health_care_facility_laboratory_clinic_organization, make_public_survey_findings) :-
    survey_completion(X_0), X_0 > 90.

% atom_id: 96362275f8f41a30 | chunk: e08f5956413e96c0 | strength: statutory
obligated(state, none, provide_mechanism_to_receive_reports).

% atom_id: cab595c5dfad9d16 | chunk: e09fd52a46fd6465 | strength: statutory
obligated(state, none, comply_with_screening_overseeing_and_reporting_requirements).

% atom_id: c757699b5d5005a1 | chunk: e0c6eb66c6f28afe | strength: regulatory
obligated(state_medicaid_agency, individual_not_attained_first_birthday, deliver_medicaid_services) :-
    age(X_0), X_0 < 1.

% atom_id: d129ad02bceee2b6 | chunk: e0eb2dbb4dbc7cc1 | strength: regulatory
obligated(state_medicaid_agency, individual_under_18_and_disabled, provide_medicaid_coverage) :-
    age(X_0), X_0 <= 18,
    disabled_status(true).

% atom_id: c6be3e5c6de1f502 | chunk: e0f48d0898c5dc85 | strength: regulatory
obligated(laboratory_provider, none, provide_laboratory_services) :-
    service_type(section_1395x_e_9_paragraphs_16_and_17_of_section_1395x_s_se).

% atom_id: 417070e139795f58 | chunk: e24d6acf564ea131 | strength: regulatory
obligated(state_medicaid_agency, individual_eligible_for_medical_assistance, provide_medicaid_coverage) :-
    eligibility_criteria(a10aiiv_a10aivi_a10aivii_a10aiiix).

% atom_id: 1df7b18c1ac90ad4 | chunk: e25d71d699a0ab5d | strength: regulatory
obligated(state_agency, secretary_and_state_medical_licensing_board, notify_of_sanction) :-
    termination_or_suspension(true).

% atom_id: 7d2c51322d73ff77 | chunk: e33916c732a5eaaa | strength: statutory
obligated(state, nursing_facility_services, include_specified_items_and_services).

% atom_id: 2d266a9a0c3162be | chunk: e33916c732a5eaaa | strength: statutory
obligated(state, nursing_facility_services, make_description_available_upon_request).

% atom_id: f730ab9aa8034a39 | chunk: e3dbf7676fd0435b | strength: statutory
obligated(federal_authority, state, transmit_information) :-
    frequency(once_each_month).

% atom_id: 449d3c8bd6bdd2b1 | chunk: e3dbf7676fd0435b | strength: statutory
obligated(federal_authority, state, allow_transmission_of_information) :-
    frequency(once_each_month).

% atom_id: 13fa819111dd48a2 | chunk: e4aa2111db7a462a | strength: statutory
obligated(state, federally_qualified_health_center, allow_contractual_relationships).

% atom_id: 1af03ee2df684509 | chunk: e55ccceef39a1e71 | strength: statutory
obligated(state, none, provide_adjusted_payments_for_inpatient_hospital_services).

% atom_id: 0e6ec2164a00b547 | chunk: e5d6893e1a461861 | strength: statutory
permitted(governmental_agency_or_entity, none, make_payment_according_to_assignment) :-
    assignment_source(person_or_institution_providing_care_or_service),
    recipient(governmental_agency_or_entity).

% atom_id: 05fbca7e479d313f | chunk: e5d6893e1a461861 | strength: statutory
permitted(agent_of_person_or_institution_providing_care_or_service, none, receive_payment_pursuant_to_agreement) :-
    agreement_type(agency_agreement),
    compensation_relationship(unrelated_to_payment_amount_or_billing).

% atom_id: 27fd5453d4e5b222 | chunk: e8ebf8822c97a52b | strength: regulatory
obligated(state_health_agency_or_other_appropriate_state_medical_agenc, none, establish_a_plan).

% atom_id: 3d79982f4c63952c | chunk: e8ebf8822c97a52b | strength: regulatory
obligated(state_health_agency_or_other_appropriate_state_medical_agenc, appropriate_professional_health_personnel, review_the_appropriateness_and_quality_of_care_and_services).

% atom_id: 80e3a5985d71ad8c | chunk: e8ebf8822c97a52b | strength: regulatory
obligated(state_health_agency_or_other_appropriate_state_medical_agenc, state_agency_established_or_designated_pursuant_to_paragraph, provide_guidance_with_respect_to_the_review_of_care_and_serv).

% atom_id: 4943f275a54dd2c1 | chunk: ea5598600f34876e | strength: regulatory
permitted(secretary, none, waive_or_modify_requirements) :-
    location(american_samoa_northern_mariana_islands).

% atom_id: 822df97404a6ff03 | chunk: ea58457d4dc61c5d | strength: statutory
obligated(health_services_facility_or_organization_receiving_payments, none, make_reports_to_secretary) :-
    receives_payments_under_plan(true),
    type_of_facility_or_organization(uniform_reporting_system_established).

% atom_id: 7b7a7c1b95f56f37 | chunk: ea73d90ed531ad98 | strength: statutory
prohibited(state_law_applicator, none, construing_the_section_to_prohibit).

% atom_id: 317b55ae717af0c3 | chunk: ea73d90ed531ad98 | strength: statutory
permitted(health_care_provider, health_care_provider_agent, objecting_on_conscience_basis).

% atom_id: 01c4c99ba30a1b4a | chunk: ea73d90ed531ad98 | strength: statutory
permitted(health_care_provider_agent, implementing_an_advance_directive, not_implementing).

% atom_id: ee02f47e4a5cb6ae | chunk: eb0d60ba5a80f9ae | strength: regulatory
obligated(state, organization_or_entity, exclude_from_participation) :-
    type(medicaid_managed_care_organization_entity_furnishing_service).

% atom_id: 8e0bfe1f44f9a3b1 | chunk: eb2a60615b6b219d | strength: regulatory
obligated(state_medicaid_agency, none, provide_or_arrange_for_the_provision_of_screening_services).

% atom_id: 8a3c4a55e5d9f442 | chunk: ec2e9e992ced4aab | strength: statutory
obligated(state, individual_resident_absent_from_state, provide_medical_assistance_inclusion) :-
    residency_status(resident_of_state),
    absence_status(absent_from_state).

% atom_id: c002b70acc6da57e | chunk: ed24a65a09123371 | strength: statutory
obligated(state, child_under_19, determine_eligibility_for_medical_assistance) :-
    age(X_0), X_0 <= 19,
    family_income_poverty_line_pct(X_1), X_1 <= 300.

% atom_id: 0cece2b39f43e2f8 | chunk: eeb6eb2421ae586e | strength: regulatory
obligated(entity_and_its_employees_management_contractors_agents, none, establish_written_policies).

% atom_id: 5a682fd3232012a5 | chunk: ef7ac937f41f95ce | strength: statutory
obligated(state_authority, none, exclude_individuals_based_on_residence).

% atom_id: 2353be23a3ce5567 | chunk: f0bec77e9ea83845 | strength: statutory
permitted(secretary, state, waive_payment) :-
    allowable_error_rate(reached),
    good_faith_effort(made).

% atom_id: 193d34703bc169e7 | chunk: f1e9ccaf0bb11502 | strength: statutory
prohibited(provider, individual_entitled_to_payment, refuse_to_furnish_services) :-
    third_party_liability(potential).

% atom_id: f5991f2c3f5eae5b | chunk: f2352090adf33cc5 | strength: statutory
obligated(ordering_or_referring_physicians, none, be_enrolled_under_state_plan_or_waiver).

% atom_id: 17a9e3b5551eb25a | chunk: f3a31d99c5d0e765 | strength: statutory
permitted(state, provider, include_any_provider).

% atom_id: 7cdae4b7730f4ede | chunk: f5e5e5953406055a | strength: regulatory
obligated(state, individual_under_19_eligible_for_benefits, remain_eligible_for_benefits) :-
    age(X_0), X_0 < 19,
    eligibility_determination(eligible).

% atom_id: 69ca22c0fd16a9f3 | chunk: f7fbc9eb5ff6c689 | strength: statutory
obligated(individual, none, work).

% atom_id: 52765fd73f9079f2 | chunk: f987ee95d2fe23a8 | strength: statutory
obligated(state, hospital, provide_outlier_adjustment) :-
    payment_basis(prospective).

% atom_id: 18b0ba20764a3ea1 | chunk: fa2e0df89fec1038 | strength: statutory
prohibited(state, individual_determined_ineligible_for_medical_assistance, be_treated_as_not_providing_medical_assistance) :-
    ineligibility_reason(failure_to_meet_community_engagement_requirement).

% atom_id: fb0e0ec1bc06e605 | chunk: fa6dc06da707770e | strength: statutory
obligated(state, individual, provide_supplemental_security_income_benefits) :-
    benefit_reason(subparagraph_e_subparagraph_g_of_section_1382e1).

% atom_id: 74f3086eb8ef2589 | chunk: fa99ace192086bb9 | strength: regulatory
obligated(secretary, plan, approve) :-
    fulfills_conditions(subsection_a).

% atom_id: 06169cb52bb5435f | chunk: fa99ace192086bb9 | strength: regulatory
prohibited(secretary, plan, approve) :-
    imposes_eligibility_condition(medical_assistance).

% atom_id: af09a74f52da4b21 | chunk: fae8ef274269f5fb | strength: statutory
prohibited(state, none, apply_paragraph) :-
    date(september_30_2029).

% atom_id: de36d6e3aea9f905 | chunk: fb7b05983eabb7ab | strength: statutory
obligated(state, service_provider, provide_payment_for_services).

% atom_id: 78d9317d583dadca | chunk: fd5d79c38d33cfab | strength: regulatory
obligated(provider_or_organization, adult_individuals_receiving_medical_care, maintain_written_policies_and_procedures).

% atom_id: a619c7b931761adb | chunk: fe1069cbe3f6c4db | strength: statutory
obligated(state_authority, hospital, find_compliance) :-
    date(X_0), X_0 > 6,
    compliance_status(in_compliance).

% atom_id: 4240eb5b7085c2dd | chunk: fe4063f7ba87caaa | strength: regulatory
permitted(state, employer_of_physician_dentist_or_practitioner, receive_payment) :-
    employment_condition(turn_over_fee_to_employer).

% atom_id: 4cf9aaf6d3e0103d | chunk: fe4063f7ba87caaa | strength: regulatory
permitted(state, facility_in_which_care_or_service_was_provided, receive_payment) :-
    contractual_arrangement(submit_bill_for_care_or_service).

% atom_id: 69585c966132cc28 | chunk: febdf66e428f503a | strength: statutory
obligated(state, individual_enrolled_under_state_plan_or_waiver, provide_address_information) :-
    enrollment_status(under_state_plan_or_waiver).

% atom_id: be28298dd294b94d | chunk: febdf66e428f503a | strength: statutory
obligated(state, process_to_obtain_address_information, obtain_from_reliable_data_sources) :-
    enrollment_status(under_state_plan_or_waiver).

% atom_id: 7f3b66778e732c15 | chunk: febdf66e428f503a | strength: statutory
obligated(state, process_to_obtain_address_information, take_actions_specified_by_secretary) :-
    enrollment_status(under_state_plan_or_waiver).