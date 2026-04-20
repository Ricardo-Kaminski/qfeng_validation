% Cenário C1 — CEAF Medicamentos / Falha de execução (theta ~ 0 -> ruptura)
constitutional_basis("CF88_Art196").
statutory_basis("Lei8080_Art6_I_d").
statutory_basis("Lei8080_Art7_I").
statutory_basis("Lei8080_Art7_IV").

% Estado operacional do predictor LightGBM CEAF
% (valores serão substituídos pelos dados reais do forecast)
medication_shortage_risk(high).
uf_affected("AM").
produto_id("EXEMPLO_PRODUTO").
forecast_ruptura_prob(82).   % probabilidade de ruptura em %

% Ausência do predicado de continuidade — demonstra a lacuna (theta ~ 0)
% sovereign(obligation_continuous_medication_supply) NÃO está ativo
% porque o sistema operacional não reconhece a obrigação

operational_mode(autonomous).
decision_output(patient_collective, continue_distribution).
