% Extracao Q-FENG (passthrough manual) para T-CLT-01-009
% Tipo: T-CLT-01
% Confianca: 0.910
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Magistrado trabalhista manteve sentenca de primeiro grau sem acrescimo de fundamentacao
legal_decision_issued(acordao_trt_adota_sentenca).
% span: 'Adoto os fundamentos da sentenca como razoes de decidir'
decisao_adota_fundamentos_sentenca(acordao_trt_adota_sentenca).
% span: A sentenca de origem havia citado precedente posteriormente superado
legal_decision_issued(sentenca_origem_referida).
% span: a sentenca havia citado precedente posteriormente superado
cita_precedente(sentenca_origem_referida, julgado_tst_superado_inespecifico).
% span: precedente posteriormente superado por jurisprudencia mais recente do TST
precedente_superado(julgado_tst_superado_inespecifico).
