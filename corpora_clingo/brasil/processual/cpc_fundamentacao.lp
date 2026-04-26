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

% --- CPC Art. 489 §1° I-IV — outros critérios de decisão não fundamentada ---
%
% §1°, I: decisão não fundamentada quando se limita à indicação,
%   à reprodução ou à paráfrase de ato normativo, sem explicar sua
%   relação com a causa ou a questão decidida.
sovereign(prohibition_of_normative_act_paraphrase_without_explanation) :-
    statutory_basis("CPC_Art489_par1_I").

% §1°, II: decisão não fundamentada quando emprega conceitos jurídicos
%   indeterminados, sem explicar o motivo concreto de sua incidência.
sovereign(prohibition_of_indeterminate_legal_concepts_without_grounding) :-
    statutory_basis("CPC_Art489_par1_II").

% §1°, III: decisão não fundamentada quando invoca motivos que se
%   prestariam a justificar qualquer outra decisão (motivação genérica
%   / boilerplate). CRÍTICO para auditoria de decisões algorítmicas
%   geradas por LLM, que tendem precisamente a esse tipo de motivação.
sovereign(prohibition_of_generic_template_motivation) :-
    statutory_basis("CPC_Art489_par1_III").

% §1°, IV: decisão não fundamentada quando não enfrenta os argumentos
%   deduzidos no processo capazes de, em tese, infirmar a conclusão
%   adotada pelo julgador.
% NOTE: §1° IV e VI são frequentemente confundidos. IV trata de
%   "argumentos deduzidos no processo"; VI trata da regra geral de
%   enfrentamento. A jurisprudência os trata em conjunto, mas
%   desdobramos para fidelidade textual.
sovereign(prohibition_of_ignoring_deduced_arguments) :-
    statutory_basis("CPC_Art489_par1_IV").

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
% CONSTRAINT REMOVIDA (audit C-3): decision_grounded_in_identified_precedent/1 não é
% definida nem fornecida por nenhum facts-file. Em Clingo closed-world, `not P` com P
% indefinido é sempre verdadeiro, tornando a constraint espuriamente restritiva e
% capaz de gerar UNSAT em T-CLT-04 (controle positivo). A falsificabilidade é
% preservada pela constraint de citação inexistente abaixo.

% Citação de precedente inexistente viola Art. 489 §1°, V (caso Mata v. Avianca)
:- legal_citation_used(Citation),
   not legal_citation_exists(Citation),
   sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi).

% Citação de precedente real, mas sem identificação de ratio decidendi,
% também viola CPC Art. 489 §1° V (precedent-mining sem fundamentação).
% Esta constraint complementa a anterior (citação fantasma stricto sensu)
% para cobrir a tipologia completa de violação do inciso V.
%
% NOTE: ratio_decidendi_identified/1 não é definida em facts-files atuais.
% Esta constraint só dispara se algum cenário futuro definir explicitamente
% a ausência de identificação de ratio. Em closed-world (default Clingo),
% a ausência de definição faz a constraint não disparar — isto é o
% comportamento desejado: a constraint é "armada" mas só ativa quando
% um cenário fornece o fato negativo.
:- legal_citation_used(Citation),
   legal_citation_exists(Citation),
   not ratio_decidendi_identified(Citation),
   ratio_decidendi_required(Citation),
   sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi).
