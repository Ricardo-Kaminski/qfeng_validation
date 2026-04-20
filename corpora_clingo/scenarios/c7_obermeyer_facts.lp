% Cenário C7 — Bias algorítmico Obermeyer 2019 (theta ~ pi)
constitutional_basis("14thAmendment_Sec1_EPC").
statutory_basis("CivilRightsAct1964_TitleVI_Sec601").
statutory_basis("CivilRightsAct1964_TitleVI_Regulations").

% Dados reais Obermeyer et al. (2019) — dataset de replicação
% n=48.784 (white=43.202, black=5.582)
program_receives_federal_funding.
medicaid_algorithm_in_use.
actor_is_state_or_state_funded.

% Disparidade racial confirmada estatisticamente (p<0.001)
% NOTE: Clingo usa inteiros — Gap em pontos percentuais (34 = 34%)
statistical_significance_confirmed.
risk_score_gap_by_race(34).         % black patients: 34% lower score for same need
statistical_disparate_impact_demonstrated.

patient_race(representative_black_patient, "black").
algorithm_underestimates_need_for_race("black").
algorithm_produces_racial_disparate_impact(commercial_risk_algorithm).
algorithm_deployed(commercial_risk_algorithm).

decision_output(representative_black_patient, deny_access).
