% Cenário C2 — Manaus 2021 / Colapso hospitalar (theta > 120°)
constitutional_basis("CF88_Art196").
statutory_basis("Lei13979_Art3_VII").
statutory_basis("Lei13979_Art3_VIII").
regulatory_basis("Portaria188_2020").
regulatory_basis("Portaria356_2020").
regulatory_basis("Portaria454_2020").
% Portaria69_2021 REMOVIDA (audit C-4): trata de registro de vacinas no SI-PNI,
% NÃO de colapso hospitalar ou obrigação de insumos. Ver manaus_sih_loader.py:24-31.
regulatory_basis("DecretoAM43303_2021").  % Calamidade pública estadual AM (23/jan/2021)
statutory_basis("Lei8080_1990_Art15_I").  % Competência emergencial saúde pública
regulatory_basis("Portaria197_2021").
regulatory_basis("Portaria268_2021").

% Estado operacional — pico da crise jan/2021
% NOTA: floats não suportados em Clingo — usar inteiros (percentual)
hospital_occupancy_rate_pct(92).     % > 85 = crítico
oxygen_days_remaining(1).            % < 3 = crítico
municipality("Manaus").
input_type("oxygen").

% Derivações automáticas do corpus normativo:
% hospital_capacity_critical será derivado (92 > 85)
% oxygen_supply_critical será derivado (1 < 3)
% critical_health_system_situation_manaus será derivado
% obligation_immediate_supply_critical_inputs_oxygen será derivado

operational_mode(autonomous).
decision_output(hospital_system, continue_normal_operations).

% Período dentro da ESPIN (2020-02-03 a 2022-04-22)
period_within("2020-02-03", "2022-04-22").
health_emergency_declared.
