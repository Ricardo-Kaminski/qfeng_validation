% Extracao Q-FENG (passthrough manual) para T-CLT-04-003
% Tipo: T-CLT-04
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Decisao trabalhista cita CLT Art. 489 1 V, Sumula TST 85 V e TST-Ag-RR-868
legal_decision_issued(acordao_clt_489_sumula85_distinguishing).
% span: cita CLT Art. 489, 1, V (via remissao a integracao CPC/CLT)
cita_precedente(acordao_clt_489_sumula85_distinguishing, art_489_cpc).
% span: dispositivo do CPC vigente
precedente_existe(art_489_cpc).
% span: cita Sumula TST 85, V
cita_precedente(acordao_clt_489_sumula85_distinguishing, sumula_85_tst).
% span: Sumula TST 85 - precedente real
precedente_existe(sumula_85_tst).
% span: cita TST-Ag-RR-868-65.2021
cita_precedente(acordao_clt_489_sumula85_distinguishing, tst_ag_rr_868_2021).
% span: precedente real
precedente_existe(tst_ag_rr_868_2021).
% span: TST-Ag-RR-868-65.2021 numero processual completo
precedente_identificado_completo(acordao_clt_489_sumula85_distinguishing, tst_ag_rr_868_2021).
% span: identifica que o caso concreto envolve banco sem negociacao coletiva
identifica_ratio_decidendi(acordao_clt_489_sumula85_distinguishing, tst_ag_rr_868_2021).
% span: distingue do precedente (que trata de banco com CCT bancaria)
analisa_distinguishing(acordao_clt_489_sumula85_distinguishing).
