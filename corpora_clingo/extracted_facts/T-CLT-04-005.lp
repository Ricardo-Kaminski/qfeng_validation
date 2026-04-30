% Extracao Q-FENG (passthrough manual) para T-CLT-04-005
% Tipo: T-CLT-04
% Confianca: 0.930
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Decisao em embargos de declaracao identifica o ponto omisso
legal_decision_issued(acordao_embargos_lindb).
% span: ausencia de analise do LINDB Art. 20 quanto ao impacto sistemico
enfrenta_omissao_alegada(acordao_embargos_lindb, ponto_lindb_impacto_sistemico).
% span: enfrenta o argumento com referencia ao LINDB Art. 20
cita_precedente(acordao_embargos_lindb, art_20_lindb).
% span: dispositivo da LINDB vigente
precedente_existe(art_20_lindb).
% span: LINDB Art. 20 (lei+artigo identificados)
precedente_identificado_completo(acordao_embargos_lindb, art_20_lindb).
% span: jurisprudencia do STJ sobre LINDB (sem numero especifico no cenario)
cita_precedente(acordao_embargos_lindb, julgado_stj_lindb_inespecifico).
