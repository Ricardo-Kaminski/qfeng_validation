% Extracao Q-FENG (passthrough manual) para T-CLT-03-007
% Tipo: T-CLT-03
% Confianca: 0.950
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: CCT do setor bancario preve banco de horas anual
banco_horas_implementado(empresa_bancario_compliance).
% span: CCT do setor bancario
tem_cct(empresa_bancario_compliance).
% span: banco de horas anual (12 meses)
prazo_compensacao_meses(empresa_bancario_compliance, 12).
% span: em linha com a jurisprudencia do TST-Ag-RR-868-65.2021
cita_precedente(empresa_bancario_compliance, tst_ag_rr_868_2021).
% span: precedente real, registrado em rastreabilidade
precedente_existe(tst_ag_rr_868_2021).
% span: em linha com o Tema 1046/STF
cita_precedente(empresa_bancario_compliance, tema_1046_stf).
% span: Tema RG real, registrado em rastreabilidade
precedente_existe(tema_1046_stf).
% span: extrato entregue
extrato_mensal_entregue(empresa_bancario_compliance).
% span: compensacao realizada no prazo
compensacao_realizada_no_prazo(empresa_bancario_compliance).
