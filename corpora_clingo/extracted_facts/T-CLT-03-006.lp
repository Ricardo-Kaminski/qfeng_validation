% Extracao Q-FENG (passthrough manual) para T-CLT-03-006
% Tipo: T-CLT-03
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: CCT do setor de varejo preve banco de horas
banco_horas_implementado(empresa_varejo_compliance).
% span: CCT do setor de varejo
tem_cct(empresa_varejo_compliance).
% span: compensacao em ate 12 meses
prazo_compensacao_meses(empresa_varejo_compliance, 12).
% span: Toda compensacao ocorreu dentro do prazo
compensacao_realizada_no_prazo(empresa_varejo_compliance).
% span: com extrato mensal entregue
extrato_mensal_entregue(empresa_varejo_compliance).
% span: A jornada extra nunca superou 2h/dia (8h normais + 2h max = 10h)
jornada_diaria_horas(empresa_varejo_compliance, 10).
