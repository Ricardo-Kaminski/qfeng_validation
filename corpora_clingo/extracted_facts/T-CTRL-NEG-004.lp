% Extracao Q-FENG (passthrough manual) para T-CTRL-NEG-004
% Tipo: T-CTRL-NEG
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Empresa e sindicato celebraram CCT com banco de horas de 6 meses
banco_horas_implementado(empresa_ctrl_neg_004).
% span: Empresa e sindicato celebraram CCT
tem_cct(empresa_ctrl_neg_004).
% span: banco de horas de 6 meses
prazo_compensacao_meses(empresa_ctrl_neg_004, 6).
% span: acumulo maximo de 60h mensais
acumulo_maximo_horas(empresa_ctrl_neg_004, 60).
% span: extrato entregue mensalmente
extrato_mensal_entregue(empresa_ctrl_neg_004).
% span: todas as horas foram compensadas em folgas previamente comunicadas
compensacao_realizada_no_prazo(empresa_ctrl_neg_004).
% span: A CCT foi registrada na SRTE
cct_registrada_srte(empresa_ctrl_neg_004).
