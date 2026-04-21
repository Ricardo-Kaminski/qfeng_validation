% atom_id: 7b7e203cf3b73f43 | chunk: 0436cfe6e8767f1b | strength: statutory
obligated(state, none, employ_and_fix_compensation).

% atom_id: 5927052dcaa5fea3 | chunk: 51f3ec7b72bc200d | strength: regulatory
permitted(member_of_macpac, none, receive_compensation) :-
    serving_on_business(macpac_including_travel_time).

% atom_id: cc600ffc55d522b3 | chunk: 51f3ec7b72bc200d | strength: regulatory
permitted(member_of_macpac, none, receive_travel_expenses) :-
    serving_away_from_home_and_regular_place_of_business(while_serving_on_the_business_of_macpac).

% atom_id: b4465bed66e4be52 | chunk: 51f3ec7b72bc200d | strength: regulatory
permitted(physician_personnel_of_macpac, none, receive_physician_comparability_allowance) :-
    serving_as_personnel_of_macpac(macpac).

% atom_id: d96c92e906faa542 | chunk: 51f3ec7b72bc200d | strength: regulatory
obligated(macpac, personnel_of_macpac, treat_as_employees_of_us_senate) :-
    pay_and_benefits(other_than_pay_of_members_of_macpac).

% atom_id: 0242391ef293abcc | chunk: 784f4ea3e4b57466 | strength: regulatory
obligated(macpac, none, consult_with_medpac) :-
    duty(carrying_out_duties).

% atom_id: 90992fe627380376 | chunk: 784f4ea3e4b57466 | strength: regulatory
obligated(medpac, none, analyze_and_recommend_changes_to_medicare_policy) :-
    responsibility(analysis_of_and_recommendations).

% atom_id: fb5a1351e85ecd0a | chunk: 78c842cb9b1d9d5a | strength: regulatory
obligated(state_medicaid_agency, none, seek_assistance_and_support).

% atom_id: 3d0a06a344e21490 | chunk: a2905fe5429e4dd8 | strength: regulatory
obligated(macpac, states, consult_regularly).

% atom_id: a2f10c3a565f77f1 | chunk: a2905fe5429e4dd8 | strength: regulatory
obligated(macpac, states, ensure_input_included).

% atom_id: f8de226318cb441e | chunk: de625ef8be6fb830 | strength: regulatory
obligated(agency, none, utilize_information) :-
    information_type(published_unpublished).

% atom_id: fdbe11faa7bfc076 | chunk: de625ef8be6fb830 | strength: regulatory
obligated(agency, none, collect_and_assess_information) :-
    source(own_staff_other_arrangements).