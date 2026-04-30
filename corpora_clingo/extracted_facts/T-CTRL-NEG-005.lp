% Extracao Q-FENG (passthrough manual) para T-CTRL-NEG-005
% Tipo: T-CTRL-NEG
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: motoristas que trabalham entre 22h e 5h
trabalho_noturno_realizado(empresa_transporte_noturno).
% span: Empresa de transporte recolhe adicionais noturnos de 20%
adicional_noturno_pago_percentual(empresa_transporte_noturno, 20).
% span: calcula a hora noturna como 52 minutos e 30 segundos
hora_noturna_reduzida_aplicada(empresa_transporte_noturno).
% span: motoristas em turno noturno entre 22h e 5h
regime_jornada(empresa_transporte_noturno, turno_fixo_noturno).
% span: Nenhuma hora extra e realizada alem das 8h diarias
jornada_diaria_horas(empresa_transporte_noturno, 8).
% span: registra os periodos em sistema eletronico
registro_ponto_eletronico(empresa_transporte_noturno).
