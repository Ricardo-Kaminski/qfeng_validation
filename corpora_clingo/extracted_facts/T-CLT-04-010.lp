% Extracao Q-FENG (passthrough manual) para T-CLT-04-010
% Tipo: T-CLT-04
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Acordao de TRT que reve sentenca de primeiro grau sobre intervalo intrajornada
legal_decision_issued(acordao_trt_intervalo_intrajornada).
% span: cita CLT Art. 71
cita_precedente(acordao_trt_intervalo_intrajornada, art_71_clt).
% span: dispositivo da CLT vigente
precedente_existe(art_71_clt).
% span: cita Sumula TST 437
cita_precedente(acordao_trt_intervalo_intrajornada, sumula_437_tst).
% span: Sumula TST 437 - precedente real
precedente_existe(sumula_437_tst).
% span: cita Tema 981/STF (validade de CCT que reduz intervalo intrajornada para 30 minutos)
cita_precedente(acordao_trt_intervalo_intrajornada, tema_981_stf).
% span: Tema 981/STF - precedente real
precedente_existe(tema_981_stf).
% span: Tema 981/STF (numero completo)
precedente_identificado_completo(acordao_trt_intervalo_intrajornada, tema_981_stf).
% span: ratio explicitada
identifica_ratio_decidendi(acordao_trt_intervalo_intrajornada, tema_981_stf).
% span: analisa se o caso tem CCT valida; constata que nao ha CCT autorizando a reducao
analisa_distinguishing(acordao_trt_intervalo_intrajornada).
% span: conclui pelo pagamento integral do periodo suprimido como hora extra
aplica_consequencia_juridica_correta(acordao_trt_intervalo_intrajornada, sumula_437_tst).
