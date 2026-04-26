% ============================================================
% DEPRECATED — CENÁRIO NÃO COMPÕE PIPELINE E5 ATIVO
%
% Este arquivo foi movido para corpora_clingo/_deprecated/ em 26/abr/2026.
% O cenário C1 (CEAF Medicamentos via predictor LightGBM) foi descartado
% como caso de validação simbólica do Q-FENG durante a consolidação do
% conjunto canônico de cenários ativos.
%
% Razão da deprecation:
%   - O preditor LightGBM CEAF foi explorado como possibilidade de cenário
%     em fases anteriores da PoC, mas não foi adotado como caso de
%     validação simbólica na arquitetura final do Q-FENG.
%   - O preditor permanece como artefato de engenharia (pipeline de ML
%     funcional), mas não alimenta o motor simbólico Clingo.
%
% Conjunto canônico de cenários ativos (após decisão de 26/abr/2026):
%   - C2: Manaus 2021 (colapso hospitalar, theta > 120°)
%   - C3: Concentração regional SUS (theta ~ pi)
%   - C7: Obermeyer 2019 / bias algorítmico Medicaid (theta ~ pi)
%   - T-CLT-01: Mata v. Avianca / citação fantasma (theta ~ pi)
%   - T-CLT-02: Súmula TST 85 distorcida (theta > 120°)
%   - T-CLT-03: Banco de horas com CCT (controle, theta < 30°)
%   - T-CLT-04: Citação fundamentada (controle positivo)
%
% Cobertura normativa preservada:
%   Os predicados Lei 8080 Art. 6° I d (assistência farmacêutica integral),
%   Art. 7° I (universalidade) e Art. 7° IV (igualdade) permanecem em
%   sus_direito_saude.lp como cobertura normativa do SUS — eles não
%   dependem de C1 e continuam relevantes para C2 e C3.
%
% Arquivo preservado para rastro histórico e eventual menção como
% caminho não-adotado em notas metodológicas do paper.
% ============================================================

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
