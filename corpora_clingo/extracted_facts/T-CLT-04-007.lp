% Extracao Q-FENG (passthrough manual) para T-CLT-04-007
% Tipo: T-CLT-04
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: TRT ao julgar caso de rescisao de gestante
legal_decision_issued(acordao_estabilidade_gestante).
% span: cita CF/88 Art. 10, II, b (ADCT)
cita_precedente(acordao_estabilidade_gestante, art_10_ii_b_adct).
% span: dispositivo constitucional vigente
precedente_existe(art_10_ii_b_adct).
% span: cita Sumula TST 244
cita_precedente(acordao_estabilidade_gestante, sumula_244_tst).
% span: Sumula TST 244 - precedente real
precedente_existe(sumula_244_tst).
% span: cita OJ 399 da SDI-1
cita_precedente(acordao_estabilidade_gestante, oj_399_sdi1_tst).
% span: OJ 399 SDI-1 - precedente real
precedente_existe(oj_399_sdi1_tst).
% span: menciona expressamente a OJ 399 para afastar a exigencia de comunicacao previa
identifica_ratio_decidendi(acordao_estabilidade_gestante, oj_399_sdi1_tst).
% span: a gravidez ocorreu antes da dispensa (fato provado)
gravidez_anterior_dispensa(trabalhadora_gestante).
% span: nulidade da dispensa e reintegracao
dispensa_durante_estabilidade(trabalhadora_gestante).
