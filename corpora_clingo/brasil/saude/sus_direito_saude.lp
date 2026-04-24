% ============================================================
% CORPUS CLINGO — Brasil / Saúde Pública
% Arquivo: brasil/saude/sus_direito_saude.lp
%
% Âncora normativa:
%   CF/88 Art. 196 — Saúde como direito de todos e dever do Estado
%   CF/88 Art. 197 — Relevância pública das ações de saúde
%   CF/88 Art. 198 — Sistema Único de Saúde
%   CF/88 Art. 200 — Competências do SUS
%   Lei 8080/1990 Art. 2° — Direito à saúde
%   Lei 8080/1990 Art. 7° — Princípios do SUS
%   Lei 8080/1990 Art. 9° — Direção do SUS
%
% Classificação: SOVEREIGN
%   (direito social fundamental — CF/88 Art. 6°,
%    não pode ser suprimido por ato administrativo)
%
% Relevância para os cenários Q-FENG:
%   - C1: CEAF — fornecimento contínuo de medicamentos
%   - C2: Manaus — dever do Estado em emergência sanitária
%   - C3: concentração regional — universalidade e equidade
%   - C4a/b: constraint para decisão clínica algorítmica
% ============================================================

% --- CF/88 Art. 196 — Direito à saúde ---
% Saúde é direito de todos e dever do Estado
% garantido mediante políticas sociais e econômicas
sovereign(right_to_health_as_duty_of_state) :-
    constitutional_basis("CF88_Art196").

% Acesso universal e igualitário às ações e serviços de saúde
sovereign(universal_equal_access_to_health_services) :-
    constitutional_basis("CF88_Art196").

% --- CF/88 Art. 197 — Relevância pública ---
% Ações e serviços de saúde são de relevância pública
sovereign(health_services_public_relevance) :-
    constitutional_basis("CF88_Art197").

% --- CF/88 Art. 198 — SUS ---
% Regionalização e hierarquização
sovereign(sus_regionalization_and_hierarchy) :-
    constitutional_basis("CF88_Art198").

% Integralidade do atendimento
sovereign(integrality_of_health_care) :-
    constitutional_basis("CF88_Art198_II").

% Participação da comunidade
sovereign(community_participation_in_health) :-
    constitutional_basis("CF88_Art198_III").

% --- Lei 8080/1990 Art. 6°, I, d — Assistência farmacêutica (CRÍTICO C1 CEAF) ---
% Âncora direta do fornecimento contínuo de medicamentos no SUS
% Sem este predicado o cenário C1 não tem base normativa no corpus
sovereign(right_to_integral_pharmaceutical_assistance) :-
    statutory_basis("Lei8080_Art6_I_d").

sovereign(obligation_continuous_medication_supply) :-
    statutory_basis("Lei8080_Art6_I_d"),
    sovereign(right_to_integral_pharmaceutical_assistance).

% --- Lei 8080/1990 Art. 2° — Direito à saúde ---
% O Estado deve prover condições indispensáveis ao pleno exercício do direito à saúde
sovereign(obligation_to_provide_health_conditions) :-
    statutory_basis("Lei8080_Art2").

% --- Lei 8080/1990 Art. 7° — Princípios do SUS ---
% Universalidade: acesso a todos os níveis de assistência
sovereign(universality_of_access) :-
    statutory_basis("Lei8080_Art7_I").

% Integralidade: conjunto articulado e contínuo das ações e serviços
sovereign(integrality_of_actions_and_services) :-
    statutory_basis("Lei8080_Art7_II").

% Preservação da autonomia das pessoas
sovereign(preservation_of_personal_autonomy) :-
    statutory_basis("Lei8080_Art7_III").

% Igualdade da assistência sem preconceitos ou privilégios
sovereign(equality_of_assistance_without_prejudice) :-
    statutory_basis("Lei8080_Art7_IV").

% Direito à informação sobre saúde
sovereign(right_to_health_information) :-
    statutory_basis("Lei8080_Art7_V").

% Divulgação de informações sobre saúde
sovereign(disclosure_of_health_information) :-
    statutory_basis("Lei8080_Art7_VI").

% Utilização da epidemiologia para estabelecer prioridades
sovereign(epidemiology_based_priority_setting) :-
    statutory_basis("Lei8080_Art7_VII").

% Equidade — CRÍTICO para C3 (concentração regional)
% NOTE: "equity" here encompasses Art. 7° IV (igualdade formal) PLUS
% Art. 3° III (redução de desigualdades regionais — sovereign na camada constitucional)
% Distinção doutrinária: igualdade (Art. 7° IV) ≠ equidade (tratar desigualmente
% os desiguais). Para fins Q-FENG: predicado cobre ambos os sentidos.
sovereign(equity_in_health_assistance) :-
    statutory_basis("Lei8080_Art7_IV").

% --- Predicados ELASTIC (moduláveis por portaria) ---
% Organização de serviços por nível de complexidade
elastic(organization_by_complexity_level) :-
    statutory_basis("Lei8080_Art7_XI").

% Conjugação de recursos financeiros, tecnológicos e humanos
elastic(resource_conjugation_for_health) :-
    statutory_basis("Lei8080_Art7_XII").

% --- Constraints derivados ---
% Nenhum sistema algorítmico pode negar acesso universal
% Guard Lei8080_Art7_I: scopes constraint to SUS/health-access regime (audit H-6)
:- decision_output(_, deny_access),
   sovereign(universality_of_access),
   statutory_basis("Lei8080_Art7_I").

% Nenhum sistema pode produzir desigualdade regional sistêmica
:- decision_output(_, regional_allocation),
   increases_regional_inequality(regional_allocation),
   sovereign(equity_in_health_assistance).
