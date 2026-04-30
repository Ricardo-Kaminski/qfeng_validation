% Extracao Q-FENG (passthrough manual) para T-CLT-04-002
% Tipo: T-CLT-04
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: TRT decide acao sobre adicional noturno
legal_decision_issued(acordao_trt_adicional_noturno_sumula60).
% span: citando Sumula TST 60 (adicional noturno - regime de revezamento)
cita_precedente(acordao_trt_adicional_noturno_sumula60, sumula_60_tst).
% span: Sumula TST 60 - precedente real
precedente_existe(sumula_60_tst).
% span: Sumula TST 60 (numero+corte identificados)
precedente_identificado_completo(acordao_trt_adicional_noturno_sumula60, sumula_60_tst).
% span: identifica a ratio (o revezamento noturno integra o adicional a remuneracao)
identifica_ratio_decidendi(acordao_trt_adicional_noturno_sumula60, sumula_60_tst).
% span: A distincao com casos de turno fixo nao noturno e explicitada
analisa_distinguishing(acordao_trt_adicional_noturno_sumula60).
% span: empregado em regime 12x36 com periodos noturnos fixos
regime_jornada(empresa_revezamento_12x36, 12x36).
% span: regime 12x36 com periodos noturnos fixos
trabalho_noturno_realizado(empresa_revezamento_12x36).
