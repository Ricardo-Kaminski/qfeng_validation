% Extracao Q-FENG (passthrough manual) para T-CLT-03-004
% Tipo: T-CLT-03
% Confianca: 0.940
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Trabalhadora firmou CCT com banco de horas semestral
banco_horas_implementado(empresa_licenca_maternidade).
% span: firmou CCT
tem_cct(empresa_licenca_maternidade).
% span: banco de horas semestral de 6 meses
prazo_compensacao_meses(empresa_licenca_maternidade, 6).
% span: A empresa suspendeu o computo do banco durante a licenca e reativou ao retorno
prazo_suspenso_por_afastamento(empresa_licenca_maternidade, licenca_maternidade).
% span: A compensacao total ocorreu em 8 meses (contando o periodo util), dentro do prazo acordado na CCT
compensacao_realizada_no_prazo(empresa_licenca_maternidade).
