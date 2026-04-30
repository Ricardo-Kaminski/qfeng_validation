% Extracao Q-FENG (passthrough manual) para T-CLT-03-005
% Tipo: T-CLT-03
% Confianca: 0.940
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Empresa do setor quimico com CCT de banco de horas
banco_horas_implementado(empresa_quimico_5x10).
% span: CCT de banco de horas anuais
tem_cct(empresa_quimico_5x10).
% span: banco de horas anuais
prazo_compensacao_meses(empresa_quimico_5x10, 12).
% span: jornada de 10h/dia para compensacao semanal
jornada_diaria_horas(empresa_quimico_5x10, 10).
% span: modelo 5x10 sem previsao especifica na CCT
regime_jornada(empresa_quimico_5x10, 5x10).
