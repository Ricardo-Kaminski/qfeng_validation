% Cenário T-CLT-01 — Mata v. Avianca / Citação fantasma (theta ~ pi)
constitutional_basis("CF88_Art93_IX").
constitutional_basis("CF88_Art5_XXXV").
statutory_basis("CPC_Art489_par1_V").
statutory_basis("CPC_Art489_par1_VI").
statutory_basis("LINDB_Art20").

% Fatos do caso
legal_decision_issued(decisao_tst_mata_avianca).
legal_citation_used("precedente_inexistente_123456").

% O precedente citado NÃO existe na base jurisprudencial
% legal_citation_exists/1 NÃO será derivado — ativa o constraint
