% Extracao Q-FENG (passthrough manual) para T-CLT-02-008
% Tipo: T-CLT-02
% Confianca: 0.940
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Banco de horas estabelecido por ACT
banco_horas_implementado(empresa_act_7meses_demissao).
% span: estabelecido por ACT com compensacao em 7 meses
tem_act(empresa_act_7meses_demissao).
% span: compensacao em 7 meses
prazo_compensacao_meses(empresa_act_7meses_demissao, 7).
% span: saldo positivo de 60h
acumulo_real_horas(empresa_act_7meses_demissao, 60).
