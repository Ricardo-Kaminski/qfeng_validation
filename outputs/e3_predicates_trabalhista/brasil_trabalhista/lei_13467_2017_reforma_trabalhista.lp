% atom_id: 8bababbe7941cb35 | chunk: 10bbde8f0ddadf47 | strength: statutory
prohibited(employer, worker, deduct_salary_without_explicit_consent) :-
    consent_given(false),
    agreement_type(collective_bargaining_agreement_collective_convention).

% atom_id: 49c79ddb3670d60f | chunk: 2b742effbc9e079f | strength: statutory
obligated(employer, worker, participate_in_company_profits_or_results).

% atom_id: 56e42f08da73a469 | chunk: 3361af3c111d8d43 | strength: statutory
prohibited(employer, worker_with_disability, discriminate_salary_criteria_admission).

% atom_id: ea2ecbe16b1cc678 | chunk: 52a8a79a624dadc3 | strength: statutory
obligated(employer, worker, comply_with_health_safety_regulations).

% atom_id: ea48341329f69f7c | chunk: 57d62afb8c643636 | strength: statutory
permitted(worker, none, decide_on_strike_opportunity).

% atom_id: 654ab1bda74315dc | chunk: 57d62afb8c643636 | strength: statutory
permitted(worker, none, defend_interests_through_strike).

% atom_id: 0c601b41e5899f05 | chunk: 64c564a13da29ded | strength: statutory
obligated(state, public, define_essential_services_and_activities).

% atom_id: aa168964867a62f4 | chunk: 64c564a13da29ded | strength: statutory
obligated(state, public, ensure_unavoidable_needs_during_strike).

% atom_id: 2d86a33054323a74 | chunk: 72c5fa1fcd59b5b2 | strength: statutory
obligated(employer, worker, ensure_equal_rights_worker_avulso).

% atom_id: f6d3aa7697119432 | chunk: 8347ffb0f026623b | strength: statutory
obligated(employer, worker, provide_additional_compensation_for_dangerous_work) :-
    work_condition(penoso_insalubre_ou_perigoso).

% atom_id: cbf4c213a91f41e3 | chunk: 86f8035f451865c2 | strength: statutory
obligated(state, child, provide_legal_protection).

% atom_id: ba8a3ed66b468155 | chunk: 880d2444e05ae06c | strength: statutory
prohibited(employer, child, employ_for_nightwork) :-
    age(dezoito).

% atom_id: 120d79283a74e302 | chunk: 880d2444e05ae06c | strength: statutory
prohibited(employer, child, employ) :-
    age(dezesseis).

% atom_id: 12835c6b05b59558 | chunk: 880d2444e05ae06c | strength: statutory
permitted(employer, child, employ_as_apprentice) :-
    age(quatorze).

% atom_id: 58580f20bbc2b3b1 | chunk: 8f2084047cb6a95d | strength: statutory
obligated(employer, worker, provide_proportional_notice_period).

% atom_id: 5bf343d12473fe15 | chunk: 939fae5cd226fedf | strength: statutory
obligated(employer, worker, provide_accident_insurance).

% atom_id: f52eb36c075f0d12 | chunk: 9531b9a9db6d82de | strength: statutory
permitted(employer, worker, grant_incentive_prizes).

% atom_id: cff5888307f6ba63 | chunk: 997878d73763d084 | strength: statutory
obligated(employer, worker, monitor_labor_laws_compliance).

% atom_id: 7263d4bd85248e56 | chunk: 997878d73763d084 | strength: statutory
obligated(employer, worker, monitor_social_security_laws_compliance).

% atom_id: 14a91779d04d479e | chunk: 997878d73763d084 | strength: statutory
obligated(employer, worker, monitor_collective_conventions_compliance).

% atom_id: 4040b6398835b81c | chunk: 997878d73763d084 | strength: statutory
obligated(employer, worker, monitor_collective_agreements_compliance).

% atom_id: 0acaaeeb833bf660 | chunk: 9a1965aef8235377 | strength: statutory
permitted(worker, none, change_clothes_outside_company) :-
    obligation_to_change_in_company(false).

% atom_id: a709293d0f7d4732 | chunk: 9a3f62c235e2fced | strength: statutory
obligated(employer, worker, make_effort_to_minimize_injury).

% atom_id: 7bf8f80589fddebb | chunk: e676e80894d4feaf | strength: statutory
obligated(employer, worker, classify_insalubrity_level).

% atom_id: 37f976e280aae51a | chunk: ff114df33ee0ce81 | strength: statutory
prohibited(employer, worker, extend_working_hours_in_hazardous_environments_without_licen).