% ============================================================
% CORPUS CLINGO — Brasil / Emergência Sanitária Manaus 2021
% Arquivo: brasil/emergencia_manaus/emergencia_sanitaria.lp
%
% Âncora normativa:
%   Lei 13.979/2020 Art. 3° — Medidas de enfrentamento COVID-19
%   Portaria GM/MS 188/2020 — Declaração de ESPIN
%   Portaria GM/MS 356/2020 — Regulamentação Lei 13.979
%   Portaria GM/MS 454/2020 — Transmissão comunitária
%   Portaria GM/MS 197/2021 — Renovação ESPIN
%   Portaria GM/MS 79/2021 — Ampliação vagas Mais Médicos para Manaus (18/jan/2021)
%   Lei 13.979/2020 Art. 10 — Coordenação federativa resposta COVID-19
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

% --- Lei 13.979/2020 Art. 3° §7° — Dispensa de licitação emergencial ---
% Autoriza dispensa de licitação para aquisição de bens, serviços e
% insumos relacionados ao enfrentamento da emergência de saúde pública.
% Completa a cadeia jurídica do C2: Estado pode requisitar (Art. 3° VII)
% e adquirir sem licitação (Art. 3° §7°), garantindo base legal completa
% para a obrigação de fornecimento imediato de O₂.
sovereign(authorization_to_dispense_bidding_in_emergency) :-
    statutory_basis("Lei13979_Art3_par7"),
    health_emergency_declared.

% --- Portaria 188/2020 — ESPIN ---
% Declaração de Emergência em Saúde Pública de Importância Nacional
sovereign(espin_declaration_active) :-
    regulatory_basis("Portaria188_2020"),
    period_within("2020-02-03", "2022-04-22").
% Átomo plano derivado do wrapper — necessário para regras dependentes (audit C-1)
espin_declaration_active :- sovereign(espin_declaration_active).

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

% --- Colapso UTI Manaus — FVS-AM Boletim 16/jan/2021 + Decretos AM ---
% Situação crítica documentada: FVS-AM Boletim 16/jan/2021 (103.69% UTI pública)
% Base normativa: Decreto AM 43.303/2021 (23/jan — calamidade pública estadual)
% NOTA (audit C-4): Portaria GM/MS 69/2021 NÃO se aplica — trata de registro de
% vacinas no SI-PNI. Âncora correta: Decreto AM 43.303/2021 + hospital_capacity_critical.
sovereign(critical_health_system_situation_manaus) :-
    regulatory_basis("DecretoAM43303_2021"),
    municipality("Manaus"),
    hospital_capacity_critical.

% Obrigação de reforço imediato de insumos críticos — oxigênio
% Base: Lei 13.979/2020 Art. 3° VIII (requisição de bens) + Lei 8.080/1990 Art. 15 I
% PREDICADO CENTRAL DO CENÁRIO C2
sovereign(obligation_immediate_supply_critical_inputs_oxygen) :-
    statutory_basis("Lei13979_Art3_VIII"),
    statutory_basis("Lei8080_1990_Art15_I"),
    sovereign(critical_health_system_situation_manaus),
    input_type("oxygen").

% --- Portaria 197/2021 — Renovação ESPIN ---
sovereign(espin_renewed_jan2021) :-
    regulatory_basis("Portaria197_2021").
% Átomo plano derivado do wrapper — necessário para regras dependentes (audit C-1)
espin_renewed_jan2021 :- sovereign(espin_renewed_jan2021).

% --- Portaria GM/MS 79/2021 + Lei 13.979/2020 Art. 10 — Força de trabalho médica Manaus ---
% Portaria 79/2021 (18/jan): ampliação emergencial vagas Mais Médicos para Manaus
% âncora correta: regulação de FORÇA DE TRABALHO médica emergencial, não medidas genéricas.
% Art. 10 Lei 13.979/2020: competência federal de coordenação federativa na crise sanitária.
% (audit LAW-BR-04): predicado renomeado de obligation_additional_response_measures para
% refletir o escopo real da Portaria 79/2021 e evitar generalização indevida do normativo.
sovereign(obligation_expand_medical_workforce_manaus_pandemic) :-
    regulatory_basis("Portaria79_2021"),
    statutory_basis("Lei13979_Art10"),
    espin_renewed_jan2021.
% Átomo plano — padrão audit C-1 para regras dependentes futuras
obligation_expand_medical_workforce_manaus_pandemic :- sovereign(obligation_expand_medical_workforce_manaus_pandemic).

% --- Predicados de estado operacional para C2 ---
% Estados do sistema hospitalar Manaus (alimentados pelo predictor TimeSeries).
% NOTE: Clingo usa inteiros — R em percentual (0-100).
%
% Limiar de TOH > 85%: âncora institucional na Ficha Técnica de Indicadores
% da Atenção Hospitalar do MS (Taxa de Ocupação Hospitalar de UTI), elaborada
% pela Coordenação-Geral de Atenção Hospitalar/DAHU/SAES/MS, com base na
% literatura crítica brasileira (AMIB — Associação de Medicina Intensiva
% Brasileira) que classifica TOH > 85% como "saturação operacional" — estado
% em que o tempo de espera por leito UTI cresce não-linearmente e a
% mortalidade por priorização inadequada aumenta significativamente.
%
% Limiar de oxigênio: ver oxygen_critical_threshold_days/1 abaixo (configurável).
%
hospital_capacity_critical :-
    hospital_occupancy_rate_pct(R), R > 85.

% Limiar de cobertura de oxigênio crítico: 3 dias.
% Critério operacional baseado no precedente Manaus 2021: White Martins
% comunicou ao MS em 14/jan/2021 que não conseguiria repor estoque em
% até 24-48h, configurando ponto de não-retorno operacional. O limiar
% de 3 dias é uma janela de antecedência mínima para acionamento de
% requisição emergencial (Lei 13.979/2020 Art. 3° VII) ou reorganização
% logística (transporte aéreo, redirecionamento de pacientes).
oxygen_critical_threshold_days(3).

oxygen_supply_critical :-
    oxygen_days_remaining(D),
    oxygen_critical_threshold_days(T),
    D < T.

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
