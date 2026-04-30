% Extracao Q-FENG (passthrough manual) para T-CLT-02-004
% Tipo: T-CLT-02
% Confianca: 0.950
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Empresa de vigilancia ... saldo positivo de 80h no banco de horas
banco_horas_implementado(empresa_vigilancia).
% span: banco de horas estabelecido por CCT
tem_cct(empresa_vigilancia).
% span: compensacao semestral
prazo_compensacao_meses(empresa_vigilancia, 6).
% span: saldo positivo de 80h
acumulo_real_horas(empresa_vigilancia, 80).
% span: demitiu empregado sem justa causa
dispensa_sem_justa_causa(trabalhador_vigilancia).
