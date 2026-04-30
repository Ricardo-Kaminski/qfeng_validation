% Extracao Q-FENG (passthrough manual) para T-CLT-03-002
% Tipo: T-CLT-03
% Confianca: 0.930
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: CCT do setor farmaceutico preve banco de horas anual
banco_horas_implementado(empresa_farmaceutico).
% span: CCT do setor farmaceutico
tem_cct(empresa_farmaceutico).
% span: 12 meses + 3 meses adicionais por clausula de renovacao automatica sem nova negociacao
prazo_compensacao_meses(empresa_farmaceutico, 15).
% span: O sindicato dos trabalhadores contesta
participacao_sindical_categoria(empresa_farmaceutico, categoria_farmaceutico).
