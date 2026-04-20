% ============================================================
% CORPUS CLINGO — Brasil / Direito Processual
% Arquivo: brasil/processual/cpc_fundamentacao.lp
%
% Âncora normativa:
%   CF/88 Art. 93, IX — fundamentação obrigatória de decisões judiciais
%   CF/88 Art. 5°, XXXV — inafastabilidade da jurisdição (via cf88 layer)
%   CPC Art. 489 §1° — decisão não fundamentada (critérios)
%   LINDB Art. 20 (Lei 13.655/2018) — motivação de consequências práticas
%
% Classificação: SOVEREIGN
%   (garantia constitucional de fundamentação — CF/88 Art. 93 IX,
%    não pode ser afastada por lei ordinária ou regulamento)
%
% Relevância para os cenários Q-FENG:
%   - T-CLT-01: Mata v. Avianca — citação fantasma / ratio decidendi ausente
%   - T-CLT-02/03: decisões sobre banco de horas devem identificar âncora
%   - Paper 2 (AI & Law / JURIX): raciocínio jurídico assistido por LLM
% ============================================================

% --- CF/88 Art. 93, IX — Fundamentação obrigatória ---
% Âncora constitucional do dever de fundamentar todas as decisões judiciais
sovereign(constitutional_obligation_to_state_reasons_for_decisions) :-
    constitutional_basis("CF88_Art93_IX").

% --- CPC Art. 489 §1° — Critérios de decisão não fundamentada ---
% §1°, V: decisão não fundamentada quando cita precedente sem identificar
%   fundamento determinante (ratio decidendi) nem demonstra aplicabilidade
% CRÍTICO para T-CLT-01 — Mata v. Avianca (citação fantasma)
sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi) :-
    statutory_basis("CPC_Art489_par1_V").

% §1°, VI: decisão não fundamentada quando não enfrenta todos os argumentos
%   capazes de infirmar a conclusão adotada pelo julgador
sovereign(obligation_to_address_all_legal_arguments) :-
    statutory_basis("CPC_Art489_par1_VI").

% §1°, V-VI combinados: proibição de enunciados genéricos e citação sem ratio
sovereign(prohibition_of_generic_precedent_citation) :-
    statutory_basis("CPC_Art489_par1_V"),
    statutory_basis("CPC_Art489_par1_VI").

% --- LINDB Art. 20 (Lei 13.655/2018) ---
% Vedação de decisão que não considere as consequências práticas
% Relevante para JURIX: decisão algorítmica deve explicitar impactos
sovereign(obligation_to_state_practical_consequences_of_decision) :-
    statutory_basis("LINDB_Art20").

% --- Constraints derivados ---
% Decisão judicial emitida sem fundamentação em precedente identificado viola CF/88 Art. 93 IX
:- legal_decision_issued(Decision),
   not decision_grounded_in_identified_precedent(Decision),
   sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi).

% Citação de precedente inexistente viola Art. 489 §1°, V (caso Mata v. Avianca)
:- legal_citation_used(Citation),
   not legal_citation_exists(Citation),
   sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi).
