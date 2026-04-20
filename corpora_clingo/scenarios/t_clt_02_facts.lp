% Cenário T-CLT-02 — Súmula TST 85 distorcida (theta > 120°)
constitutional_basis("CF88_Art7_XIII").
constitutional_basis("CF88_Art7_XVI").
statutory_basis("CLT_Art59_par5").
statutory_basis("CLT_Art59_par2").
statutory_basis("CLT_Art611B_IX").
jurisprudential_basis("SumulaTST_85_I").
jurisprudential_basis("SumulaTST_85_V").

% Fatos do caso — banco de horas sem CCT com período de 8 meses
hour_bank_period(8).
% collective_bargaining_agreement_active NÃO está presente
% Ativa constraint: P > 6 sem CCT = violação

weekly_hours_contracted(44).
