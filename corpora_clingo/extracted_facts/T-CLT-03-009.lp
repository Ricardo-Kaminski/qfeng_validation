% Extracao Q-FENG (passthrough manual) para T-CLT-03-009
% Tipo: T-CLT-03
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Trabalhador com banco de horas por CCT
banco_horas_implementado(empresa_conversao_saldo).
% span: banco de horas por CCT
tem_cct(empresa_conversao_saldo).
% span: prazo 12 meses
prazo_compensacao_meses(empresa_conversao_saldo, 12).
% span: A CCT previa essa possibilidade de conversao
conversao_saldo_em_dinheiro(empresa_conversao_saldo, sim).
% span: as horas convertidas seriam pagas com adicional de 50%
saldo_pago_com_adicional(empresa_conversao_saldo, 50).
