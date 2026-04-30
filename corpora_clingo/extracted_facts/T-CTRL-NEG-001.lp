% Extracao Q-FENG (passthrough manual) para T-CTRL-NEG-001
% Tipo: T-CTRL-NEG
% Confianca: 0.970
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: jornada de 8 horas diarias
jornada_diaria_horas(empresa_manufatura_compliance, 8).
% span: 44 horas semanais para todos os empregados
jornada_semanal_horas(empresa_manufatura_compliance, 44).
% span: jornada de 8 horas diarias e 44 horas semanais
regime_jornada(empresa_manufatura_compliance, 8h_diaria).
% span: 1 hora para jornada de 8h
intervalo_intrajornada_concedido_minutos(empresa_manufatura_compliance, 60).
% span: Todos os registros de ponto sao eletronicos e auditaveis
registro_ponto_eletronico(empresa_manufatura_compliance).
