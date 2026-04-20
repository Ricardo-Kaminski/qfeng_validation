% atom_id: d366ff5f36104fca | chunk: 4f66ddf6670d3979 | strength: regulatory
obligated(hemobras, none, obtain_authorization) :-
    plasma_excedente(enviado_para_uso_industrial_no_exterior).

% atom_id: 47f75d820ac65dc2 | chunk: 592faefd67f45e28 | strength: regulatory
permitted(state_manager, none, request_documents_and_information).

% atom_id: fc60323b575f9343 | chunk: 03d8416d53797f20 | strength: regulatory
prohibited(dab_sas_ms, federal_entity, suspend_financial_reimbursement) :-
    consecutive_days_without_regularization_or_update(X_0), X_0 >= 60.

% atom_id: 48e3768558d9cebc | chunk: 00b09e4e0931695f | strength: regulatory
obligated(component_producer, none, produce_irradiated_blood_components) :-
    irradiation_status(occurred),
    minimum_dose(X_1), X_1 >= 2500.

% atom_id: c593da5138e8b4fe | chunk: 00bb2ae93ea72828 | strength: regulatory
obligated(orgaos_de_apoio_do_sinasan, none, realizar_vigilancia_sanitaria_controle_de_qualidade_e_vigila).

% atom_id: 1c2056a0366870d4 | chunk: 01856bcc70363fdf | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, post_documents).

% atom_id: e79925ce4a8b0974 | chunk: 02fd7d1dd1da467c | strength: regulatory
obligated(doctor, candidate, evaluate_recent_medication_history).

% atom_id: 1884f54b04914824 | chunk: 03d8416d53797f20 | strength: regulatory
obligated(health_manager, none, provide_regularization_of_nutrition_or_update_information_in).

% atom_id: 2cf2fbc94a9cd2f7 | chunk: 06fa9bdb38180286 | strength: regulatory
obligated(group_of_workers, none, monitor_development_of_pmaq_ab_program).

% atom_id: 35720f9a95471b76 | chunk: 0872c48168de3806 | strength: regulatory
obligated(secretarias_de_saude_estados_distrito_federal_municipios, none, adopt_providences_for_credentialing_units_centers) :-
    gestao_plena(sistema_municipal_de_saude).

% atom_id: 022b8b41a80ae2e8 | chunk: 0eb86db5a77125c4 | strength: regulatory
obligated(ministry_of_health, none, publish_manual_instructivo_do_pmaq_ceo).

% atom_id: 60df1a7cc3dcea6f | chunk: 0eef670a617d7874 | strength: regulatory
obligated(department_of_basic_attention, none, provide_manual_instructivo).

% atom_id: d085b308c6acecb9 | chunk: 10d2be82663524ab | strength: regulatory
obligated(unidades_de_assistencia_de_alta_complexidade_em_terapia_nutr, pacientes_em_risco_nutricional_ou_desnutridos, providenciar_condicoes_tecnicas_instalacoes_fisicas_equipame).

% atom_id: 030f033caa654311 | chunk: 11bf0f4e88fc2907 | strength: regulatory
permitted(municipality, none, request_emad_type_2_habilitation) :-
    population(X_0), X_0 < 40000.

% atom_id: 4c75fb73e8548eb0 | chunk: 11bf0f4e88fc2907 | strength: regulatory
permitted(municipality, none, request_emad_type_2_habilitation_individually) :-
    population(X_0), X_0 >= 20000,
    population(X_1), X_1 < 40000.

% atom_id: f73eca90777935eb | chunk: 11bf0f4e88fc2907 | strength: regulatory
permitted(municipality, none, request_emad_type_2_habilitation_through_aggregation) :-
    population(X_0), X_0 < 20000.

% atom_id: d63848eedb612659 | chunk: 123d1ca5f376d601 | strength: regulatory
obligated(authorities_of_health, professionals_of_health, disclose_updated_public_data).

% atom_id: 276e1c12a92d9529 | chunk: 123d1ca5f376d601 | strength: regulatory
obligated(authorities_of_health, orgaos_de_controle_social, disclose_updated_public_data).

% atom_id: 37efa78326075735 | chunk: 123d1ca5f376d601 | strength: regulatory
obligated(authorities_of_health, population_in_general, disclose_updated_public_data).

% atom_id: 6688b7906f95b401 | chunk: 124bc0b825c92691 | strength: regulatory
obligated(municipality, none, develop_or_enhance_social_reintegration_programs) :-
    actions_developed(reintegracao_social_para_pessoas_acometidas_por_transtorno_m),
    residential_services(none),
    health_team_structure(none).

% atom_id: db17ef313376ec79 | chunk: 12a7156284df07ed | strength: regulatory
obligated(ministry_of_health, none, provide_manual_instructivo_with_normatizations).

% atom_id: ac4bb3eca8f17f65 | chunk: 14651242993339fc | strength: regulatory
obligated(ip_ict, ministry_of_health, encourage_report_transfer_and_internalization).

% atom_id: 5356fdb539584691 | chunk: 1655532b2bd0a89d | strength: regulatory
obligated(deployer, none, consult_ministry_of_health).

% atom_id: c353988659adb8c2 | chunk: 187dfd101f6b2bbd | strength: regulatory
obligated(department_of_specialized_attention_and_thematic_care, none, organize_contingency_of_samples).

% atom_id: 2f47d3a658576c08 | chunk: 1f889687d36b1ee1 | strength: regulatory
obligated(institution, none, follow_written_protocols) :-
    concentrated_hemoglobin_type(rhd_negativo_c_ou_e_positivos).

% atom_id: 030d6fd5a12c5c77 | chunk: 1f889687d36b1ee1 | strength: regulatory
obligated(technical_responsible, none, adhere_to_criteria) :-
    concentrated_hemoglobin_type(rhd_negativo_c_ou_e_positivos).

% atom_id: 267a8e8ce706401b | chunk: 20f9c79e2c4219dc | strength: regulatory
obligated(ministry_of_health, none, monitor_nuclei_of_telessaude).

% atom_id: 2d654a38d64a8223 | chunk: 20f9c79e2c4219dc | strength: regulatory
obligated(ministry_of_health, none, evaluate_information_for_incentive_financing).

% atom_id: 3940a83e31e05383 | chunk: 2131911e4a9be652 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, articular_com_outras_secretarias).

% atom_id: 0f06306c0c503bd9 | chunk: 2131911e4a9be652 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, implementar_programa_e_plano_operacional).

% atom_id: 81a148867abfd9eb | chunk: 2131911e4a9be652 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, atuar_em_areas_especificas).

% atom_id: 6dc0d9e93f65d20d | chunk: 217af196f7b553d1 | strength: regulatory
obligated(state, population, monitor_impact_of_sodium_iodide_addition).

% atom_id: d04eda778f1412a2 | chunk: 21b5e77ce54a22a3 | strength: regulatory
obligated(state, none, implement_and_monitor_technical_operational_protocols).

% atom_id: 54bea61a5fa2ed02 | chunk: 21c08b3a67751e66 | strength: regulatory
obligated(credenciado_establishment, none, receive_login_and_password).