% Extracao Q-FENG (passthrough manual) para T-CLT-03-001
% Tipo: T-CLT-03
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Empresa do setor alimenticio firmou CCT prevendo banco de horas anual
banco_horas_implementado(empresa_alimenticio).
% span: firmou CCT prevendo banco de horas anual
tem_cct(empresa_alimenticio).
% span: prazo de 12 meses estabelecido na CCT
prazo_compensacao_meses(empresa_alimenticio, 12).
% span: O sindicato homologou a prestacao anual de contas
participacao_sindical_categoria(empresa_alimenticio, categoria_alimenticio).
% span: todas foram compensadas mediante folgas dentro do prazo de 12 meses
compensacao_realizada_no_prazo(empresa_alimenticio).
% span: Os extratos mensais foram entregues
extrato_mensal_entregue(empresa_alimenticio).
% span: A jornada diaria nunca ultrapassou 10h
jornada_diaria_horas(empresa_alimenticio, 10).
