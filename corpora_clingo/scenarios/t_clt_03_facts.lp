% Cenário T-CLT-03 — Banco de horas COM CCT (theta < 30° — caso correto)
constitutional_basis("CF88_Art7_XIII").
constitutional_basis("CF88_Art7_XXVI").
statutory_basis("CLT_Art59_par2").
statutory_basis("CLT_Art611A_I").
statutory_basis("CLT_Art611A_II").

% Fatos do caso — banco de horas com CCT dentro do limite de 1 ano
hour_bank_period(10).
collective_bargaining_agreement_active.
weekly_hours_contracted(44).

% hour_bank_valid_with_cct será derivado — STAC ativo (theta < 30°)
