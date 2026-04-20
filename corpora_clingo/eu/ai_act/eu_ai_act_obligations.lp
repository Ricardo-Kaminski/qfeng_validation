% ============================================================
% CORPUS CLINGO — União Europeia / EU AI Act
% Arquivo: eu/ai_act/eu_ai_act_obligations.lp
%
% Âncora normativa:
%   EU AI Act (Regulation 2024/1689)
%   Art. 6° — Classificação de sistemas de IA de alto risco
%   Art. 9° — Sistema de gestão de riscos
%   Art. 10° — Dados e governança de dados
%   Art. 13° — Transparência e fornecimento de informações
%   Art. 14° — Supervisão humana
%   Art. 17° — Sistema de gestão de qualidade
%   Art. 62° — Obrigações de notificação para incidentes graves
%   Annex III — Lista de sistemas de alto risco
%
% Classificação: SOVEREIGN / ELASTIC conforme artigo
%
% NOTE: sovereign() aqui = não derrogável pelo deployer/operador individual
% Sentido operacional, não hierárquico-constitucional.
% Regulamento EU pode ser emendado por atos delegados (Art. 97 EU AI Act)
% e por revisão legislativa ordinária — diferente de cláusula pétrea CF/88.
%
% Relevância: Cenário C5 — Auditabilidade EU AI Act (theta ~ pi)
% ============================================================

% --- Art. 6° — Sistemas de alto risco ---
% Sistemas de IA em infraestrutura crítica de saúde = alto risco
% Annex III, pt. 5: acesso a serviços públicos essenciais / prestações sociais
% (mais preciso que "health_critical_infrastructure" para evitar questionamento em peer review)
% NOTE: maps to EU AI Act Annex III, point 5 (access to essential services)
% or point 1 (critical infrastructure) depending on deployment context
sovereign(health_ai_classified_as_high_risk) :-
    regulatory_basis("EUAIA_Art6"),
    annex_iii_category("essential_public_services_health").

% Sistemas de IA em acesso a serviços públicos essenciais = alto risco
sovereign(public_services_ai_classified_as_high_risk) :-
    regulatory_basis("EUAIA_Art6"),
    annex_iii_category("access_to_essential_services").

% --- Art. 9° — Gestão de riscos (SOVEREIGN) ---
% Sistemas de alto risco devem ter sistema de gestão de riscos
sovereign(obligation_risk_management_system_high_risk_ai) :-
    regulatory_basis("EUAIA_Art9"),
    sovereign(health_ai_classified_as_high_risk).

% Identificação e análise de riscos conhecidos e razoavelmente previsíveis
sovereign(obligation_risk_identification_and_analysis) :-
    regulatory_basis("EUAIA_Art9_II").

% --- Art. 10° — Dados e governança ---
% Práticas de governança e gestão de dados adequadas
sovereign(obligation_data_governance_practices) :-
    regulatory_basis("EUAIA_Art10_I").

% Dados de treinamento livres de erros e completos — na medida do possível
sovereign(obligation_training_data_quality) :-
    regulatory_basis("EUAIA_Art10_III").

% Exame de possíveis vieses nos dados
% CRÍTICO para C5: auditabilidade requer detecção de bias
sovereign(obligation_bias_examination_in_training_data) :-
    regulatory_basis("EUAIA_Art10_V").

% --- Art. 13° — Transparência (SOVEREIGN para alto risco) ---
% Sistema deve ser suficientemente transparente para permitir interpretação
sovereign(transparency_obligation_high_risk_ai) :-
    regulatory_basis("EUAIA_Art13_I"),
    sovereign(health_ai_classified_as_high_risk).

% Instruções de uso devem incluir características, capacidades e limitações
sovereign(obligation_to_disclose_capabilities_and_limitations) :-
    regulatory_basis("EUAIA_Art13_III").

% Nível de precisão, robustez e cibersegurança deve ser informado
sovereign(obligation_to_disclose_accuracy_and_robustness) :-
    regulatory_basis("EUAIA_Art13_III_b").

% --- Art. 14° — Supervisão humana (SOVEREIGN) ---
% Sistemas de alto risco devem permitir supervisão humana efetiva
sovereign(obligation_effective_human_oversight) :-
    regulatory_basis("EUAIA_Art14_I"),
    sovereign(health_ai_classified_as_high_risk).

% Capacidade de intervenção e anulação por humanos
sovereign(obligation_human_override_capability) :-
    regulatory_basis("EUAIA_Art14_IV_e").

% --- Art. 17° — Sistema de gestão de qualidade (QMS) ---
sovereign(obligation_quality_management_system) :-
    regulatory_basis("EUAIA_Art17_I"),
    sovereign(health_ai_classified_as_high_risk).

% --- Art. 62° — Notificação de incidentes graves (SOVEREIGN) ---
% Incidentes graves devem ser notificados à autoridade nacional competente
sovereign(obligation_serious_incident_notification) :-
    regulatory_basis("EUAIA_Art62_I").

% Notificação imediata — sem demora injustificada
sovereign(obligation_immediate_incident_notification) :-
    regulatory_basis("EUAIA_Art62_I"),
    incident_classified_as_serious.

% --- Predicados ELASTIC (moduláveis por implementação) ---
% Formato específico das instruções de uso
elastic(format_of_user_instructions) :-
    regulatory_basis("EUAIA_Art13_III").

% Método específico de logging de eventos
elastic(logging_method_selection) :-
    regulatory_basis("EUAIA_Art12").

% --- Constraints para cenário C5 ---
% Sistema de IA de alto risco sem auditabilidade viola Art. 13°
:- ai_system_deployed(System),
   sovereign(health_ai_classified_as_high_risk),
   not system_provides_audit_trail(System),
   sovereign(transparency_obligation_high_risk_ai).

% Sistema sem supervisão humana viola Art. 14°
:- operational_mode(fully_autonomous),
   sovereign(health_ai_classified_as_high_risk),
   sovereign(obligation_effective_human_oversight).
