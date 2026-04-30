% Extracao Q-FENG (passthrough manual) para T-CLT-03-011
% Tipo: T-CLT-03
% Confianca: 0.930
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Empresa firmou CCT com banco de horas anual
banco_horas_implementado(empresa_acidente_trabalho).
% span: firmou CCT
tem_cct(empresa_acidente_trabalho).
% span: banco de horas anual
prazo_compensacao_meses(empresa_acidente_trabalho, 12).
% span: A empresa alega que o prazo deveria ser suspenso pelo periodo de afastamento. Fato observado, mesmo sem clausula previa na CCT
prazo_suspenso_por_afastamento(empresa_acidente_trabalho, acidente_trabalho).
