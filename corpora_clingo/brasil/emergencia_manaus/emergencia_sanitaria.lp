% ============================================================
% CORPUS CLINGO — Brasil / Emergência Sanitária Manaus 2021
% Arquivo: brasil/emergencia_manaus/emergencia_sanitaria.lp
%
% Âncora normativa:
%   Lei 13.979/2020 Art. 3° — Medidas de enfrentamento COVID-19
%   Portaria GM/MS 188/2020 — Declaração de ESPIN
%   Portaria GM/MS 356/2020 — Regulamentação Lei 13.979
%   Portaria GM/MS 454/2020 — Transmissão comunitária
%   Portaria GM/MS 69/2021 — Situação Manaus (jan/2021)
%   Portaria GM/MS 197/2021 — Renovação ESPIN
%   Portaria GM/MS 268/2021 — Medidas adicionais Manaus
%   CF/88 Art. 196 (via sus_direito_saude.lp)
%
% Classificação: SOVEREIGN (emergência — aplicabilidade imediata)
%
% NOTE sobre sovereign() para portarias (Camada 3):
%   Portarias são atos administrativos revogaréis por portaria posterior.
%   A classificação sovereign() aqui tem sentido TEMPORAL E OPERACIONAL:
%   durante a vigência da ESPIN (2020-02-03 a 2022-04-22) as obrigações
%   têm eficácia plena e imediata. O mecanismo period_within/2 já garante
%   que estes predicados só são derivados dentro do período relevante.
%   Fora do período: historicamente corretos, operacionalmente inativos.
%
% Relevância: Cenário C2 — Manaus 2021 / colapso hospitalar
%   Demonstra theta > 120° (Circuit Breaker) quando capacidade
%   hospitalar colapsa e o sistema não aciona resposta normativa
% ============================================================

% --- Lei 13.979/2020 Art. 3° — Medidas compulsórias ---
% Autoridade sanitária pode determinar isolamento e quarentena
sovereign(authority_to_determine_isolation) :-
    statutory_basis("Lei13979_Art3_I").

% Autoridade pode determinar realização compulsória de exames
sovereign(authority_to_require_medical_exams) :-
    statutory_basis("Lei13979_Art3_II").

% Requisição de bens e serviços de pessoas jurídicas em emergência
% CRÍTICO C2: requisição de cilindros de oxigênio em Manaus
sovereign(authority_to_requisition_goods_in_emergency) :-
    statutory_basis("Lei13979_Art3_VII"),
    health_emergency_declared.

% Autorização para importação de insumos sem registro prévio
% Art. 3°, VIII: importação e distribuição de produtos sem registro prévio
% (Art. 3°, IX trata de fabricação/distribuição excepcional — distinto)
% Para crise de oxigênio Manaus: Art. 3°, VII (requisição) + Art. 3°, VIII
sovereign(authorization_to_import_without_prior_registration) :-
    statutory_basis("Lei13979_Art3_VIII"),
    health_emergency_declared.

% --- Portaria 188/2020 — ESPIN ---
% Declaração de Emergência em Saúde Pública de Importância Nacional
sovereign(espin_declaration_active) :-
    regulatory_basis("Portaria188_2020"),
    period_within("2020-02-03", "2022-04-22").

% --- Portaria 356/2020 — Regulamentação ---
% Obrigação de notificação imediata de casos suspeitos
sovereign(obligation_immediate_notification_suspected_cases) :-
    regulatory_basis("Portaria356_2020"),
    espin_declaration_active.

% Obrigação de adotar medidas de contenção
sovereign(obligation_to_adopt_containment_measures) :-
    regulatory_basis("Portaria356_2020"),
    espin_declaration_active.

% --- Portaria 454/2020 — Transmissão comunitária ---
% Reconhecimento de transmissão comunitária em todo território nacional
sovereign(community_transmission_declared_nationwide) :-
    regulatory_basis("Portaria454_2020").

% --- Portaria 69/2021 — Situação Manaus ---
% Reconhecimento da situação crítica do sistema de saúde em Manaus
sovereign(critical_health_system_situation_manaus) :-
    regulatory_basis("Portaria69_2021"),
    municipality("Manaus").

% Obrigação de reforço imediato de insumos críticos — oxigênio
% PREDICADO CENTRAL DO CENÁRIO C2
sovereign(obligation_immediate_supply_critical_inputs_oxygen) :-
    regulatory_basis("Portaria69_2021"),
    sovereign(critical_health_system_situation_manaus),
    input_type("oxygen").

% --- Portaria 197/2021 — Renovação ESPIN ---
sovereign(espin_renewed_jan2021) :-
    regulatory_basis("Portaria197_2021").

% --- Portaria 268/2021 — Medidas adicionais ---
% Determinação de medidas adicionais de resposta
sovereign(obligation_additional_response_measures) :-
    regulatory_basis("Portaria268_2021"),
    espin_renewed_jan2021.

% --- Predicados de estado operacional para C2 ---
% Estados do sistema hospitalar Manaus (alimentados pelo predictor TimeSeries)
% NOTE: Clingo usa inteiros — R em percentual (0-100), limiar 85%
hospital_capacity_critical :-
    hospital_occupancy_rate_pct(R), R > 85.

oxygen_supply_critical :-
    oxygen_days_remaining(D), D < 3.

% --- Constraints centrais do cenário C2 ---
% Sistema não pode continuar operação autônoma com capacidade crítica
:- operational_mode(autonomous),
   hospital_capacity_critical,
   sovereign(obligation_immediate_supply_critical_inputs_oxygen).

% Sistema não pode aprovar alta hospitalar com oxigênio crítico
:- decision_output(_, approve_discharge),
   oxygen_supply_critical,
   sovereign(obligation_immediate_supply_critical_inputs_oxygen).

% Sistema deve acionar COES quando capacidade crítica e ESPIN ativa
sovereign(obligation_to_activate_coes) :-
    hospital_capacity_critical,
    espin_declaration_active.
