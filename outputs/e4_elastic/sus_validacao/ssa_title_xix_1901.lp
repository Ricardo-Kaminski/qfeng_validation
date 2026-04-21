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

% atom_id: fdbe11faa7bfc076 | chunk: de625ef8be6fb830 | strength: regulatory
obligated(agency, none, collect_and_assess_information) :-
    source(own_staff_other_arrangements).