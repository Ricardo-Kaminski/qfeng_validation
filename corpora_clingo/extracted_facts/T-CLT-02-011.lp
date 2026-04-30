% Extracao Q-FENG (passthrough manual) para T-CLT-02-011
% Tipo: T-CLT-02
% Confianca: 0.970
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Transportadora firmou CCT com banco de horas semestral
banco_horas_implementado(transportadora_x).
% span: firmou CCT
tem_cct(transportadora_x).
% span: banco de horas semestral
prazo_compensacao_meses(transportadora_x, 6).
% span: O sindicato dos trabalhadores assinou a CCT
participacao_sindical_categoria(transportadora_x, categoria_transporte).
% span: empregador exigiu que os trabalhadores abrissem mao do direito ao adicional de horas extras
clausula_renuncia_adicional(transportadora_x).
