% atom_id: 17b6f8da36478e47 | chunk: 62111f4bf7937977 | strength: constitutional
obligated(congress, none, remove_disability) :-
    person(engaged_in_insurrection_or_rebellion),
    person(unknown).

% atom_id: 5ee234c5be4cc461 | chunk: ace65ec70e3452c2 | strength: constitutional
obligated(state, representatives_apportionment, be_apportioned) :-
    persons_count(whole_number_of_persons),
    indians_exclusion(not_taxed_indians).

% atom_id: 647bb7fa6e647600 | chunk: ace65ec70e3452c2 | strength: constitutional
prohibited(state, voting_rights, deny_voting_right) :-
    gender(male),
    age(21),
    citizenship(us_citizen).

% atom_id: c83721ae9aeb4d52 | chunk: ace65ec70e3452c2 | strength: constitutional
prohibited(state, voting_rights, abridge_voting_right) :-
    gender(male),
    age(21),
    citizenship(us_citizen).

% atom_id: 9ee0e9f71def75dd | chunk: ace65ec70e3452c2 | strength: constitutional
permitted(state, voting_rights, allow_voting_right) :-
    gender(male),
    age(21),
    citizenship(us_citizen).