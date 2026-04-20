% ============================================================
% CORPUS CLINGO — Brasil / Fundamentos Constitucionais
% Arquivo: brasil/constitucional/cf88_principios_fundamentais.lp
%
% Âncora normativa:
%   CF/88 Art. 1° — Fundamentos da República
%   CF/88 Art. 3° — Objetivos fundamentais
%   CF/88 Art. 4° — Princípios das relações internacionais
%   CF/88 Art. 5° — Direitos e garantias fundamentais
%   CF/88 Art. 60 §4° — Cláusulas pétreas
%
% Classificação: SOVEREIGN (cláusulas pétreas — invioláveis
%   mesmo por emenda constitucional, CF/88 Art. 60 §4°)
%
% Relevância para os cenários Q-FENG:
%   - C3: equidade regional SUS (Art. 3° III — erradicar desigualdades)
%   - C7: bias algorítmico / equidade racial (Art. 3° IV — sem discriminação)
%   - C4b: constraint universal sobre qualquer decisão algorítmica no SUS
%   - T-CLT-01/02: fundamentação de decisões (Art. 5° LIV/LV/XXXV — due process)
%
% Nota: estes predicados são de aplicabilidade universal — regulam
%   assimetrias raciais, étnicas e regionais independentemente do
%   nível regulatório (não podem ser derrogados por portaria ou lei ordinária)
%
% NOTE sobre Arts. 1° e 3°:
%   Tecnicamente são normas programáticas, não cláusulas pétreas formais.
%   A extensão de sovereign() a estes artigos é doutrinariamente defensável
%   (princípios estruturantes — Gilmar Mendes) mas não pacífica
%   (José Afonso da Silva diverge). Para fins Q-FENG: utilizável com ressalva.
% ============================================================

% --- Art. 1° — Fundamentos da República ---
% CF/88 Art. 1°, III: dignidade da pessoa humana
sovereign(dignity_of_human_person) :-
    constitutional_basis("CF88_Art1_III").

% CF/88 Art. 1°, IV: valores sociais do trabalho e da livre iniciativa
sovereign(social_value_of_labor) :-
    constitutional_basis("CF88_Art1_IV").

% --- Art. 3° — Objetivos fundamentais (aplicabilidade universal) ---
% CF/88 Art. 3°, I: construir sociedade livre, justa e solidária
sovereign(obligation_to_build_just_society) :-
    constitutional_basis("CF88_Art3_I").

% CF/88 Art. 3°, III: erradicar pobreza e reduzir desigualdades regionais e sociais
% CRÍTICO para C3 (concentração regional SUS) e C7 (Obermeyer / equidade racial)
sovereign(obligation_to_reduce_regional_social_inequality) :-
    constitutional_basis("CF88_Art3_III").

% CF/88 Art. 3°, IV: promover bem de todos, sem preconceitos de origem,
%   raça, sexo, cor, idade ou quaisquer outras formas de discriminação
% CRÍTICO para C7 (bias algorítmico — sub-representação racial Medicaid/SUS)
sovereign(prohibition_of_discrimination_by_race_origin_color) :-
    constitutional_basis("CF88_Art3_IV").

% --- Art. 5° — Direitos e garantias fundamentais (cláusula pétrea) ---
% CF/88 Art. 5°, caput: igualdade perante a lei sem distinção de qualquer natureza
sovereign(equality_before_the_law) :-
    constitutional_basis("CF88_Art5_caput").

% CF/88 Art. 5°, III: proibição de tratamento desumano ou degradante
sovereign(prohibition_of_inhuman_treatment) :-
    constitutional_basis("CF88_Art5_III").

% CF/88 Art. 5°, LIV: ninguém será privado de liberdade ou bens sem
%   devido processo legal
sovereign(due_process_of_law) :-
    constitutional_basis("CF88_Art5_LIV").

% CF/88 Art. 5°, LV: contraditório e ampla defesa
sovereign(right_to_adversarial_process_and_defense) :-
    constitutional_basis("CF88_Art5_LV").

% CF/88 Art. 5°, XXXV: inafastabilidade da jurisdição / acesso à justiça
% CRÍTICO para T-CLT-01 — Mata v. Avianca (acesso à fundamentação judicial)
sovereign(right_of_access_to_justice_and_judicial_review) :-
    constitutional_basis("CF88_Art5_XXXV").

% --- Art. 60 §4° — Cláusulas pétreas (metanorma) ---
% Nenhuma emenda pode abolir: forma federativa, voto direto,
%   separação de poderes, direitos e garantias individuais
sovereign(entrenchment_clause_individual_rights) :-
    constitutional_basis("CF88_Art60_par4_IV").

% --- Regras de aplicabilidade universal ---
% Qualquer decisão algorítmica que viole os fundamentos acima
% ativa o Circuit Breaker independentemente do nível regulatório

:- decision_output(_, Action),
   violates_dignity(Action),
   sovereign(dignity_of_human_person).

:- decision_output(_, Action),
   discriminates_by_race_or_origin(Action),
   sovereign(prohibition_of_discrimination_by_race_origin_color).

:- decision_output(_, Action),
   increases_regional_inequality(Action),
   sovereign(obligation_to_reduce_regional_social_inequality).
