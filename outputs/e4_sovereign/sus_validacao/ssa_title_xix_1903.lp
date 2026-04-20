% atom_id: 2ee2e93e567ca5fb | chunk: 09774d791f8aefb1 | strength: statutory
obligated(state, family, exclude_medical_costs_from_income) :-
    cost_type(medical_care_remedial_care).

% atom_id: a36d5df4ecc547eb | chunk: 6a25e322f258028f | strength: regulatory
permitted(hospital_clinic_or_similar_entity, none, expend_funds_for_training_and_materials) :-
    purpose(determining_eligibility_of_individuals_for_medical_assistanc),
    purpose(providing_outreach_services).

% atom_id: d705495d93c6f9be | chunk: 870da70da7402c4d | strength: statutory
prohibited(state, provider_of_personal_care_service_and_home_health_care_servi, require_utilization_of_specific_evv_system) :-
    evv_system_operated(not_state_or_contractor).

% atom_id: 641cf6587d60732a | chunk: 09774d791f8aefb1 | strength: statutory
obligated(state, family, exclude_amount_paid_to_state) :-
    amount_paid(medical_care_remedial_care).

% atom_id: 335008ad35bebdaa | chunk: 0ce3fcca6ec64846 | strength: statutory
obligated(state_medicaid_agency, individual, provide_medicaid_coverage) :-
    is_paid_or_eligible(true),
    income_ssi_pct(X_1), X_1 <= 300.

% atom_id: eee7ad4b7fa5f820 | chunk: 157ecf4d61874b10 | strength: regulatory
obligated(secretary, none, integrate_duties_and_functions) :-
    determinations(making_determinations_as_to_whether_an_organization_is_a_med).

% atom_id: c67b50b52d5351b1 | chunk: 1b3d63cb0a510a4a | strength: regulatory
obligated(state_medicaid_agency, individual_eligible_for_medicaid, provide_medicaid_aid_or_assistance) :-
    eligibility_status(eligible),
    current_status(not_receiving_aid_or_assistance).

% atom_id: 4a7030085bb4a6cb | chunk: 1b3d63cb0a510a4a | strength: regulatory
obligated(state_medicaid_agency, individual_eligible_for_medicaid, provide_medicaid_aid_or_assistance) :-
    eligibility_status(would_be_eligible),
    current_status(in_a_medical_institution).

% atom_id: 8b9f933e8c243c0e | chunk: 2eb2a4f3d36c864a | strength: regulatory
obligated(state_authority, none, conduct_adequate_over_oversight_of_the_program).

% atom_id: 8d25557c1f411396 | chunk: 5d2c7016694088aa | strength: regulatory
obligated(secretary, private_and_public_institutions, conduct_timely_sample_onsite_surveys).

% atom_id: 433a40e91f08d71d | chunk: 5d2c7016694088aa | strength: regulatory
obligated(secretary, public, make_findings_available_for_public_inspection).

% atom_id: f1a15f0882df3c1e | chunk: 74275f2764d7d380 | strength: statutory
obligated(provider, none, submit_utilization_data_and_coding) :-
    covered_outpatient_drugs(section_1396r_8a7).

% atom_id: 1ed176ebc9e9f8d0 | chunk: 7a38faef637a4a7f | strength: regulatory
obligated(secretary, medicaid_provider, calculate_medicaid_share) :-
    period(none).

% atom_id: 2ecb944483019579 | chunk: 7a38faef637a4a7f | strength: regulatory
obligated(secretary, inpatient_bed_days, take_into_account) :-
    enrollment_status(none).

% atom_id: 92adf752d4d9c972 | chunk: 86341f93e2a35690 | strength: regulatory
obligated(state, federal_medicaid_program, reduce_federal_medical_assistance_percentage) :-
    unsatisfactory_or_invalid_showing(true),
    type_of_facility_or_institutional_services(type_of_facilities_or_services).

% atom_id: 989564d762ffb989 | chunk: 8a7c8cd5374d078f | strength: regulatory
obligated(state, none, reduce_expenditures_on_covered_outpatient_drugs) :-
    drug_category(categories_of_greatest_utilization).

% atom_id: bb0f73e262dc37b1 | chunk: 8a7c8cd5374d078f | strength: regulatory
obligated(state, none, increase_utilization_of_generic_drugs).

% atom_id: 2223105ca9f330ce | chunk: 8a7c8cd5374d078f | strength: regulatory
obligated(state, none, implement_education_programs_and_incentives).

% atom_id: 093606fdbd0fc88f | chunk: ce7713d86e95f046 | strength: regulatory
obligated(secretary, medicaid_provider, establish_overall_hospital_ehr_amount) :-
    eligibility(eligible_for_payments_under_paragraph_1b).

% atom_id: fd38177fdd259063 | chunk: d522323c86a22469 | strength: regulatory
obligated(secretary, none, study_average_costs).

% atom_id: 7359af975e645a77 | chunk: d522323c86a22469 | strength: regulatory
permitted(secretary, none, utilize_studies).

% atom_id: 383a82c6863d8c4e | chunk: d534d120ef11a2db | strength: regulatory
obligated(secretary, state, pay_to_state) :-
    service_provider(personal_care_service_and_home_health_care_service_providers),
    system_utilization(electronic_visit_verification_system_operated_by_state_or_co).

% atom_id: fd2c1579acbe70a9 | chunk: df9d3b40b2e9a36a | strength: regulatory
obligated(state_agency, individual, make_a_showing_satisfactory_to_secretary) :-
    calendar_quarter(each),
    request_for_payment(full_federal_medical_assistance_percentage).

% atom_id: 6dd57f9ed156db2f | chunk: df9d3b40b2e9a36a | strength: regulatory
prohibited(state_agency, individual, count_days_with_payments_made_on_behalf_of_individual).

% atom_id: 8cacf5d718c2e420 | chunk: df9d3b40b2e9a36a | strength: regulatory
obligated(state_agency, patients_in_mental_hospitals_and_intermediate_care_facilitie, have_professional_management_reviewed_and_evaluated_annually) :-
    calendar_quarter(each).

% atom_id: 9e6a990060a29d2a | chunk: ed70c6be1ed4622a | strength: statutory
obligated(state, provider_of_medical_assistance, conduct_investigation_and_pursue_prosecution) :-
    violation(fraud).

% atom_id: c4872200899c47fe | chunk: ed70c6be1ed4622a | strength: statutory
obligated(state, provider_of_health_care_services, conduct_investigation_and_pursue_prosecution) :-
    violation(fraud),
    approval(inspector_general_of_relevant_federal_agency).