% atom_id: 463ecb3d3d98931e | chunk: 2e11b7cf3312f1f3 | strength: regulatory
obligated(state, pregnant_woman, provide_routine_prenatal_care) :-
    service_included(yes).

% atom_id: 161d089c1824c6a7 | chunk: 2e11b7cf3312f1f3 | strength: regulatory
permitted(state, pregnant_woman, provide_additional_treatment_services) :-
    complicating_condition(yes).

% atom_id: 72a3aa011c44c10c | chunk: 2e11b7cf3312f1f3 | strength: regulatory
obligated(state, pregnant_woman, provide_labor_and_delivery_services) :-
    service_included(yes).

% atom_id: 3ca28ad3658704b0 | chunk: 2e11b7cf3312f1f3 | strength: regulatory
obligated(state, pregnant_woman, provide_routine_post_partum_care) :-
    service_included(yes).

% atom_id: 3bb712ad32291a45 | chunk: 3c85659b55824874 | strength: regulatory
obligated(individual_furnishing_audiology_services, none, meet_one_of_the_following_conditions) :-
    state_license_status(does_not_license_audiologists),
    exemption_status(exempted_from_state_licensure_based_on_practice_in_specific).

% atom_id: 1552978c5e1119c1 | chunk: 3d3a2acb08079f48 | strength: regulatory
obligated(state, none, make_nursing_facility_services_available).

% atom_id: 9c7f73b335446060 | chunk: 5f1bd8e4e86991a1 | strength: regulatory
obligated(state_medicaid_agency, individual_ininstitution, require_individual_to_spend_income_on_medical_care) :-
    location(hospital_nursing_facility_intermediate_care_facility_for_int).

% atom_id: 1062683384260039 | chunk: 63d2d741841b0a19 | strength: regulatory
obligated(state_authority, institution, meet_requirements) :-
    health_and_safety(patients).

% atom_id: 7efaa2c426f896f3 | chunk: 661a01674f8d7da8 | strength: regulatory
obligated(institution, patient, receive_room_board_and_professional_services) :-
    stay_duration(X_0), X_0 >= 24.

% atom_id: b31042883ec2e7c5 | chunk: 71dafad7cf700512 | strength: regulatory
obligated(institution, none, provide_room_board_and_professional_services).

% atom_id: e4c9da7047f5b4a4 | chunk: 7d5b7da1035cc99d | strength: regulatory
obligated(alternative_benefit_plan_provider, beneficiary, include_essential_health_benefits) :-
    state_option(n45_cfr_156100).

% atom_id: bb536f2057ec9333 | chunk: 86a0079dc7f22446 | strength: regulatory
obligated(state_agency, none, provide_other_services).

% atom_id: 8c1dce585c33b0e6 | chunk: 9b32f08758335753 | strength: regulatory
obligated(state_medicaid_agency, beneficiaries_in_institutions_for_mental_diseases, limit_services) :-
    age(X_0), X_0 >= 65.

% atom_id: 163b040d95e172e7 | chunk: b704c191069a1dcb | strength: regulatory
obligated(state, beneficiary, pay_premiums).

% atom_id: 093daa007aab6235 | chunk: e1bef2539e2cee08 | strength: regulatory
obligated(home_health_agency_or_facility_licensed_by_state, none, provide_physical_therapy_or_occupational_therapy_or_speech_p).

% atom_id: dc4aa3681e2cc6de | chunk: efabfe7857071f4d | strength: regulatory
obligated(state_medicaid_agency, ventilator_dependent_individual, ensure_respiratory_care) :-
    days_of_inpatient_stay(X_0), X_0 >= 30.

% atom_id: 53f6a383a4d675c2 | chunk: fed5295698f79de1 | strength: regulatory
obligated(institution, none, conduct_reviews) :-
    committee_members(overall_administration_responsible_individuals_nursing_super).