% Extracao Q-FENG (passthrough manual) para T-CLT-04-006
% Tipo: T-CLT-04
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Acordao cita corretamente Tema 1046/STF e TST-Ag-RR-868
legal_decision_issued(acordao_tema1046_ratio_invertida).
% span: cita corretamente Tema 1046/STF
cita_precedente(acordao_tema1046_ratio_invertida, tema_1046_stf).
% span: precedente real
precedente_existe(tema_1046_stf).
% span: Tema 1046/STF identificado
precedente_identificado_completo(acordao_tema1046_ratio_invertida, tema_1046_stf).
% span: cita corretamente TST-Ag-RR-868-65.2021
cita_precedente(acordao_tema1046_ratio_invertida, tst_ag_rr_868_2021).
% span: precedente real
precedente_existe(tst_ag_rr_868_2021).
% span: usa a tese de validade de CCT bancaria para justificar validade de banco SEM qualquer CCT
aplica_ratio_invertida(acordao_tema1046_ratio_invertida, tema_1046_stf).
% span: o tribunal nao reconheceu que o precedente pressupoe CCT existente, invertendo a ratio
aplica_ratio_invertida(acordao_tema1046_ratio_invertida, tst_ag_rr_868_2021).
