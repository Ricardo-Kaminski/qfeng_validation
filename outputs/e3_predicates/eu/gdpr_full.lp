% atom_id: 699bd695396d8414 | chunk: 1251d12a78979828 | strength: statutory
obligated(authority, none, issue_opinions) :-
    request_source(national_parliament),
    request_source(member_state_government),
    request_source(other_institutions_and_bodies).

% atom_id: c3f73f7690c2cc50 | chunk: 1ab8a2ff83d75f1f | strength: statutory
obligated(member, none, end_duties) :-
    event(expiry_of_term_of_office),
    event(resignation),
    event(compulsory_retirement).

% atom_id: 60da1e32ee61eec0 | chunk: 1acc9f6b7f9f889d | strength: statutory
obligated(authority, none, advise_in_accordance_with_member_state_law) :-
    context(legislative_and_administrative_measures).

% atom_id: dd83cad14bd22bca | chunk: 2744a8153c3f423a | strength: statutory
obligated(european_data_protection_supervisor, none, have_voting_rights) :-
    decision_topic(principles_and_rules),
    context(union_institutions_bodies_offices_agencies).

% atom_id: 4d7385dbcdc848ec | chunk: 347e667802a550cc | strength: statutory
obligated(authority, none, prevent_investigate_detect_and_prosecute).

% atom_id: b5387ecd49b2a897 | chunk: 46a24bcfd6f32663 | strength: statutory
obligated(supervisory_authority_member_or_staff, none, comply_with_obligations).

% atom_id: 1dc8ec0e2f3b3515 | chunk: 46a24bcfd6f32663 | strength: statutory
prohibited(supervisory_authority_member_or_staff, none, engage_in_incompatible_actions).

% atom_id: a24dd4840377a0b1 | chunk: 4eb5a9f6e93cdd0f | strength: statutory
obligated(controllers, controllers, determine_responsibilities) :-
    number_of_controllers(two_or_more),
    joint_determination(purposes_and_means).

% atom_id: 4d1d54060c6ebf73 | chunk: 4eb5a9f6e93cdd0f | strength: statutory
obligated(controllers, data_subjects, exercise_rights) :-
    number_of_controllers(two_or_more),
    joint_determination(purposes_and_means).

% atom_id: a2df8b1a6b38070c | chunk: 4eb5a9f6e93cdd0f | strength: statutory
obligated(controllers, controllers, provide_information) :-
    number_of_controllers(two_or_more),
    joint_determination(purposes_and_means).

% atom_id: ed3dc0b31b4e1abb | chunk: 4eb5a9f6e93cdd0f | strength: statutory
obligated(controllers, controllers, designate_contact_point) :-
    number_of_controllers(two_or_more),
    joint_determination(purposes_and_means).

% atom_id: f647eb161ff44cfa | chunk: 8a423986c551fc21 | strength: statutory
obligated(member, none, have_qualifications_experience_and_skills).

% atom_id: c6d47ecafa7eef8b | chunk: 913bfec60ae9fa84 | strength: statutory
obligated(member, none, be_dismissed) :-
    misconduct(serious),
    performance_conditions(fulfilled).

% atom_id: 1e65b287670daf48 | chunk: afd64d0092d62fa5 | strength: statutory
permitted(data_protection_officer, none, fulfill_other_tasks_and_duties).

% atom_id: 50f2c13096888a56 | chunk: afd64d0092d62fa5 | strength: statutory
obligated(controller_or_processor, none, ensure_no_conflict_of_interests) :-
    tasks_and_duties(conflict_of_interest).

% atom_id: aa8beb3e49686ada | chunk: bb1b3d2841843313 | strength: statutory
obligated(commission, none, submit_legislative_proposals) :-
    appropriateness(appropriate).

% atom_id: cf224eeedd45d11d | chunk: bb1b3d2841843313 | strength: statutory
obligated(commission, none, amend_other_union_legal_acts) :-
    legislative_proposals(submitted).

% atom_id: 3cb9731fb8b447ae | chunk: c132845fc8c49742 | strength: statutory
obligated(supervisory_authority, none, refrain_from_incompatible_actions).

% atom_id: bc4f9dabef6361ff | chunk: c132845fc8c49742 | strength: statutory
obligated(supervisory_authority, none, not_engage_in_incompatible_occupation).

% atom_id: 8e75acca62df5c5f | chunk: ccc324e9df5fd147 | strength: statutory
obligated(authority, none, prevent_and_investigate_crimes).

% atom_id: ebdbe6266d383e9c | chunk: ccc324e9df5fd147 | strength: statutory
obligated(authority, none, detect_crimes).

% atom_id: 3ed56de0ec9c462a | chunk: ccc324e9df5fd147 | strength: statutory
obligated(authority, none, prosecute_crimes).

% atom_id: a8749fd8b377a0d1 | chunk: ccc324e9df5fd147 | strength: statutory
obligated(authority, none, safeguard_public_security).