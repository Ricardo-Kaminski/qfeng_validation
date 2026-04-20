% atom_id: e8113f6c7df6775d | chunk: 0d3d6d64378056d5 | strength: statutory
permitted(state, individual_of_child_bearing_age, furnish_family_planning_services_and_supplies) :-
    age(child_bearing),
    eligibility(yes).

% atom_id: 94faa5359b0ad96d | chunk: 0d3d6d64378056d5 | strength: statutory
obligated(state, individual_21_or_older, provide_nursing_facility_services) :-
    age(X_0), X_0 >= 21.

% atom_id: f3e7d57005c4713e | chunk: 4c1bdc0bc0db3776 | strength: statutory
prohibited(state, none, be_considered_expansion_state) :-
    population(parents_only_nonpregnant_childless_adults_only).

% atom_id: 08758614a40dcd8c | chunk: 0d3d6d64378056d5 | strength: statutory
obligated(state, individual_under_21_eligible, provide_early_and_periodic_screening_diagnostic_and_treatmen) :-
    age(X_0), X_0 < 21,
    eligibility(yes).

% atom_id: 6595461fd4276a18 | chunk: 0d3d6d64378056d5 | strength: statutory
obligated(state, pregnant_woman_diagnosed_with_or_presumed_to_have_covid_19, provide_treatment_of_condition_that_may_seriously_complicate) :-
    diagnosis(covid_19),
    eligibility(yes).

% atom_id: a1f7ba3f177b8e65 | chunk: 0d3d6d64378056d5 | strength: statutory
obligated(state, individual_diagnosed_with_or_presumed_to_have_covid_19, provide_testing_and_treatment_for_covid_19) :-
    diagnosis(covid_19),
    eligibility(yes).

% atom_id: 19581413e5584adb | chunk: 0d3d6d64378056d5 | strength: statutory
obligated(state, individual_during_period_of_covid_19_vaccine_administration, provide_covid_19_vaccine_and_administration) :-
    period(n2021_2022).

% atom_id: 8a83a887c077bd15 | chunk: 1220d194966b3ef7 | strength: statutory
obligated(state, individual_not_65_years_old, provide_payments_for_care_or_services) :-
    age(X_0), X_0 < 65.

% atom_id: e688e15cdd989601 | chunk: 4c1bdc0bc0db3776 | strength: statutory
obligated(state, none, offer_health_benefits_coverage) :-
    date(march_23_2010),
    population(parents_nonpregnant_childless_adults),
    income_threshold(X_2), X_2 >= 100,
    services_included(inpatient_hospital_services),
    dependency_on_employer_coverage(false),
    employment_dependency(false),
    limited_to_premium_assistance(false),
    hospital_only_benefits(false),
    high_deductible_health_plan(false),
    alternative_benefits(false).

% atom_id: d4e4ae5bbdf12cfd | chunk: 6ec025e7dc390a88 | strength: statutory
obligated(state, individual, authorize_personal_care_services) :-
    service_type(not_an_inpatient_or_resident_of_a_hospital_nursing_facility),
    authorization_source(a_physician_in_accordance_with_a_plan_of_treatment_a_service).

% atom_id: b53d85da5d6afbf6 | chunk: 6ec025e7dc390a88 | strength: statutory
obligated(state, qualified_individual, provide_personal_care_services) :-
    service_type(not_an_inpatient_or_resident_of_a_hospital_nursing_facility),
    family_relationship(member_of_the_individuals_family).

% atom_id: cb5b3859bcb17fa8 | chunk: 6ec025e7dc390a88 | strength: statutory
obligated(state, home_or_other_location, furnish_services) :-
    service_type(not_an_inpatient_or_resident_of_a_hospital_nursing_facility).

% atom_id: 90d377f24b6c894e | chunk: 890bd001a536c39f | strength: statutory
obligated(state, individual_65_years_or_over_institution_for_mental_diseases, provide_inpatient_hospital_services_and_nursing_facility_ser).

% atom_id: b40ef0ceca27ddb6 | chunk: ca9f2330eac4fe88 | strength: statutory
prohibited(state, political_subdivision, require_greater_percentage_of_non_federal_share) :-
    non_federal_share(current_required_percentage).

% atom_id: 8377ef0481ff8860 | chunk: ca9f2330eac4fe88 | strength: statutory
permitted(state, political_subdivision, make_voluntary_contributions).

% atom_id: 7209ad16539e9877 | chunk: ce62d36139c2c245 | strength: statutory
obligated(institution, mentally_retarded_individuals, provide_health_or_rehabilitative_services).

% atom_id: b2106e036279c7d0 | chunk: e2dff93de4663f37 | strength: statutory
obligated(state_or_political_subdivision, public_institution, ensure_non_federal_expenditures_not_reduced_below_average) :-
    calendar_quarter(january_1_1975),
    services_furnished_to_patients(institution_or_distinct_part).