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

% atom_id: fc60323b575f9343 | chunk: 03d8416d53797f20 | strength: regulatory
prohibited(dab_sas_ms, federal_entity, suspend_financial_reimbursement) :-
    consecutive_days_without_regularization_or_update(X_0), X_0 >= 60.

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

% atom_id: 81bf6bbe94d87ab5 | chunk: 2324bbc92a121a39 | strength: regulatory
permitted(group_of_workers, none, expedite_reports_recommendations_manuals).

% atom_id: 606c2f9c74143544 | chunk: 2324bbc92a121a39 | strength: regulatory
permitted(group_of_workers, none, request_meetings_for_discussion).

% atom_id: 0d432ce996613796 | chunk: 2455ad614e2c9537 | strength: regulatory
obligated(gestor_estadual_e_municipal, none, effectuate_monitoring_and_control).

% atom_id: ebda830b7f7463e0 | chunk: 2455ad614e2c9537 | strength: regulatory
obligated(gestor_estadual_e_municipal, none, perform_evaluation_and_audit).

% atom_id: d81dc0f277310fe4 | chunk: 2455ad614e2c9537 | strength: regulatory
obligated(gestor_estadual_e_municipal, none, ensure_compliance_with_program_rules).

% atom_id: b71af434e8d26795 | chunk: 25483fe11647fd8c | strength: regulatory
obligated(service_of_hemotherapy, none, inform_authority_of_vigilance) :-
    use_of_blood_components(none).

% atom_id: c74d20191be7058e | chunk: 275df89f3045e065 | strength: regulatory
obligated(professional, none, comply_with_course_requirements) :-
    course_type(specific),
    course_provider(secretaria_de_vigilancia_em_saude).

% atom_id: 925c4df30f626923 | chunk: 294d74c0126dcfba | strength: regulatory
obligated(secretaria_de_vigilancia_sanitaria_do_ministerio_da_saude, none, register_painels_of_serums_and_hemoglobins).

% atom_id: 89027e1c8364074a | chunk: 2a1a04690a8184b3 | strength: regulatory
obligated(secretaria_de_vigilanca_em_saude, none, establish_and_publish_rules_for_episus_program).

% atom_id: 22245e2566b8c563 | chunk: 2bbd6c9a5409eda7 | strength: regulatory
obligated(federated_entity, none, insert_monitoring_data_into_sismob).

% atom_id: 67badc99d83d4d3c | chunk: 2bbd6c9a5409eda7 | strength: regulatory
obligated(health_manager, none, permanently_and_continuously_update_data).

% atom_id: 036073221b731114 | chunk: 2bbd6c9a5409eda7 | strength: regulatory
obligated(health_manager, none, ensure_data_veracity_and_quality).

% atom_id: 2b817de3850bdb34 | chunk: 2c3dcacf6a97b9e0 | strength: regulatory
obligated(authority, patient, register_tdic_in_clinical_record).

% atom_id: b45de5d50922be9f | chunk: 2c8fd1b850aea803 | strength: regulatory
obligated(servicos_de_atencao_especializada, none, cumprir_estabelecido_na_pactuacao).

% atom_id: 9019e236df5f9da0 | chunk: 2cadd14dc3380b44 | strength: regulatory
obligated(sinasan, none, fomentar_qualification_of_plasma_production).

% atom_id: 48a5a628bcb238c7 | chunk: 2d4a1124c62a5573 | strength: regulatory
obligated(health_manager, none, provide_regularization_of_nutrition_or_update_information_in) :-
    consecutive_days_without_action(X_0), X_0 >= 60.

% atom_id: f0f8f6d16478e8e7 | chunk: 2d4a1124c62a5573 | strength: regulatory
prohibited(ministry_of_health, federal_entity, transfer_financial_resources) :-
    irregularity_status(unsanitized).

% atom_id: e3f51574b837f6ca | chunk: 2db2f4645d342acd | strength: regulatory
obligated(svs_ms_secretarias_saude_estados_distrito_federal_municipios, none, divulgar_informacao_notificacao_compulsoria).

% atom_id: be195f9223868635 | chunk: 2e169da7e3f23eee | strength: regulatory
permitted(establishment, none, utilize_material_publicitario_and_campaign) :-
    sales_status(initiating_sales).

% atom_id: 65ecfa6e8be04e94 | chunk: 2e169da7e3f23eee | strength: regulatory
obligated(establishment, none, follow_manual_directives) :-
    sales_status(initiating_sales).

% atom_id: 699e9ed9bcd6329e | chunk: 2f7602111e607a9d | strength: regulatory
obligated(ministry_of_health, hospital_establishment, provide_technical_support).

% atom_id: abd9a5ef224357b8 | chunk: 2fceab4f7a48ba72 | strength: regulatory
obligated(department_of_emergencies_in_public_health, none, manage_and_certify_courses).

% atom_id: 012aec33a8aeb0f4 | chunk: 31eb048fc2f449c0 | strength: regulatory
obligated(daet_sas_ms, none, schedule_and_conduct_regular_meetings).

% atom_id: d691f40a28bd6b4d | chunk: 32c32b9a71a43600 | strength: regulatory
obligated(secretaria_de_vigilanca_em_saude, none, editar_normas_especificas).

% atom_id: 05c7c936b89f9fa3 | chunk: 335a164aa6d34dcf | strength: regulatory
obligated(unit_of_blood_component, none, be_labeled_with_autologous_donation).

% atom_id: bc5dd332df7b0e1d | chunk: 335a164aa6d34dcf | strength: regulatory
obligated(unit_of_blood_component, none, be_segregated_and_used_only_for_autologous_transfusion).

% atom_id: 75f1209e992ed1bc | chunk: 34a346014ed6dff5 | strength: regulatory
obligated(responsavel_tecnico, vigilancia_epidemiologica_e_sanitaria_do_estado_municipio_ou, notificar_por_escrito) :-
    gravacao(none).

% atom_id: 7fccd2a8e4c305c8 | chunk: 355e6d1e66d33dd4 | strength: regulatory
obligated(secretary_executive, none, organize_accompany_and_forward_deliberations).

% atom_id: d4bc57c1e1c2dc5f | chunk: 35bce5dd24f82d2b | strength: regulatory
obligated(institution_of_healthcare, public, fill_cid_fields_in_aih).

% atom_id: d8957e8f89cb806b | chunk: 37b1db51758d4683 | strength: regulatory
obligated(titular_or_suplente, none, attend_consecutive_meetings) :-
    number_of_absences(X_0), X_0 >= 2,
    consecutiveness(two).

% atom_id: 09a0ad0dfc359e93 | chunk: 37b1db51758d4683 | strength: regulatory
prohibited(titular_or_suplente, none, provide_justification) :-
    number_of_absences(X_0), X_0 >= 2,
    consecutiveness(two).

% atom_id: 06b585c76d0a94a2 | chunk: 38b2f8096a02a4d1 | strength: regulatory
obligated(secretaria_de_ciencia_tecnologia_inovacao_e_complexo_da_saud, none, exercise_secretariat_executive_of_cpceis).

% atom_id: edffb681ad938cf4 | chunk: 38b2f8096a02a4d1 | strength: regulatory
obligated(secretaria_de_ciencia_tecnologia_inovacao_e_complexo_da_saud, none, coordinate_activities_of_cpceis).

% atom_id: e20531b468810e88 | chunk: 3907f94cc164659a | strength: regulatory
obligated(provider, none, report_project_execution).

% atom_id: bab58bfcafe25ee3 | chunk: 3a2211da6d96d797 | strength: regulatory
obligated(health_entity_of_recognized_excellence, none, observe_economic_criteria_and_rational_use_of_public_resourc).

% atom_id: fb786e655901db9d | chunk: 3c6bf1721ada4484 | strength: regulatory
permitted(secretary_of_vigilance_in_health, none, edit_regulatory_norms).

% atom_id: b5fd0531a00fe334 | chunk: 3d1db34ad3e8f6d6 | strength: regulatory
permitted(secretary_of_vigilance_in_health, none, edit_regulatory_norms).

% atom_id: 36430993787222c8 | chunk: 3d3b3a95c86011b4 | strength: regulatory
obligated(drac_sas_ms, establishments_of_specialized_health_care, evaluate).

% atom_id: aea78632061f27f4 | chunk: 3d96de49983b4871 | strength: regulatory
obligated(federative_entity, none, be_disabled_from_svo_actions_and_services) :-
    notified_deaths(X_0), X_0 < 0.

% atom_id: 9219aac1f847595a | chunk: 3e19271dd0975658 | strength: regulatory
obligated(authority, none, follow_chlorine_residue_guidelines).

% atom_id: a391a18a16e1937b | chunk: 3f1ebae12831774e | strength: regulatory
permitted(secretary_of_vigilance_in_health, none, delegate_authority_to_alter_and_issue_regulations).

% atom_id: dece69c55faad781 | chunk: 3f6b9be9d48802f8 | strength: regulatory
obligated(state, blood_receptor, perform_blood_compatibility_test).

% atom_id: 8f6015519a4884ae | chunk: 3f6bc93259cd7cb1 | strength: regulatory
obligated(municipal_managers_and_state_managers, none, create_conditions_for_telessaude).

% atom_id: aa89d854cee166f1 | chunk: 3f6bc93259cd7cb1 | strength: regulatory
obligated(higher_education_institutions_managers, none, create_conditions_for_telessaude).

% atom_id: b82b40b21e893bc0 | chunk: 3f6bc93259cd7cb1 | strength: regulatory
obligated(research_institutions_managers, none, create_conditions_for_telessaude).

% atom_id: 65d386c59b4c5444 | chunk: 3f6bc93259cd7cb1 | strength: regulatory
obligated(institutes_technology_managers, none, create_conditions_for_telessaude).

% atom_id: 1e3ca2b54f04d669 | chunk: 405a7223085621ca | strength: regulatory
obligated(state, none, articulate_with_other_health_services).

% atom_id: ddf1152149144a76 | chunk: 42b1bc571c901e0e | strength: regulatory
obligated(coordenacao_geral_de_gestao_de_sistemas_de_informacoes_em_sa, none, adopt_providences_for_adaptations).

% atom_id: 08dc63b507375454 | chunk: 43739fb3e2c0fef8 | strength: regulatory
obligated(servico_de_atencao, none, realizar_notificacao_compulsoria).

% atom_id: 39e6f9d372acbca6 | chunk: 43a7430294a7ae2a | strength: regulatory
obligated(component_producer, none, reintegrate_components_into_stock) :-
    transport_and_storage_conditions(known_and_adapted).

% atom_id: 57adc200f94cdd19 | chunk: 43a7430294a7ae2a | strength: regulatory
obligated(component_producer, none, submit_to_visual_inspection) :-
    before_reintegration(true).

% atom_id: 7ea2a99e4d592067 | chunk: 44866a12ff19a3b4 | strength: regulatory
obligated(coordenador_executivo, none, plan_and_organize_activities).

% atom_id: 8ac080fc6cd78355 | chunk: 44b1705677258f2e | strength: regulatory
obligated(secretaria_executiva, none, inform_institution_of_repayment_duty).

% atom_id: fcfa8313bc002c03 | chunk: 44b1705677258f2e | strength: regulatory
obligated(instituition, none, replenish_irregularly_applied_funds).

% atom_id: f9de9046527b0fa3 | chunk: 45f8e0b92025e4b4 | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude, none, define_structure_for_program_operation).

% atom_id: 76f53a332193027a | chunk: 45f8e0b92025e4b4 | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude, none, organize_operational_structure).

% atom_id: 88df954758c3cc80 | chunk: 45f8e0b92025e4b4 | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude, none, take_necessary_provisions).

% atom_id: 0110b49fcf09a37c | chunk: 4624d59458df6ed1 | strength: regulatory
obligated(emap, none, ensure_minimum_composition_of_professionals).

% atom_id: 97a787447907aae9 | chunk: 47e8b01120560b66 | strength: regulatory
obligated(authority, none, conduct_technical_visits_and_audits).

% atom_id: 48927c79992c5e9d | chunk: 487f77f40537f962 | strength: regulatory
obligated(deployer, none, verify_technology_internalization).

% atom_id: 7e12cb75f066e40f | chunk: 49811e15d9156810 | strength: regulatory
obligated(state, users_of_alcohol_and_other_drugs, offer_hospital_support) :-
    resolutividade_extra_hospitalares(X_0), X_0 < 1,
    necessidade_imediata_intervencao(true).

% atom_id: a54591f991f158aa | chunk: 4a74b5e2abed6d53 | strength: regulatory
obligated(municipality, none, implement_samu_192_service).

% atom_id: a81ef469c8dd2365 | chunk: 4b1b5377790fef98 | strength: regulatory
obligated(group_of_work_health_care_cit, none, monitor_development_pmaq_ceo).

% atom_id: 52af26e2be942cc1 | chunk: 4babc9bc38dd64fa | strength: regulatory
obligated(state, none, utilize_concentrated_hemocytes) :-
    time_since_irradiation(X_0), X_0 <= 24,
    days_after_collection(X_1), X_1 <= 5.

% atom_id: 503f90a43606769d | chunk: 4c4049029a82d3aa | strength: regulatory
obligated(authority, non_state_actors, investigate_discrepancies) :-
    discrepance_results(present).

% atom_id: 6e5ee73c50711052 | chunk: 4d3a100e6fcd87a4 | strength: regulatory
obligated(industry_producer, none, obtain_authorization_for_export) :-
    plasma_transfer(for_processing_abroad).

% atom_id: d366ff5f36104fca | chunk: 4f66ddf6670d3979 | strength: regulatory
obligated(hemobras, none, obtain_authorization) :-
    plasma_excedente(enviado_para_uso_industrial_no_exterior).

% atom_id: d0405c23524b6503 | chunk: 50ea8a784e5d7d20 | strength: regulatory
permitted(svs_ms, none, edit_norms_and_adopt_measures).

% atom_id: 9a477fe6804d9a76 | chunk: 514aa25a3ffc7e8f | strength: regulatory
obligated(ministry_of_health, municipalities_and_distrito_federal, monitor_and_evaluate_data_quality).

% atom_id: 957ae4d9c6786771 | chunk: 514aa25a3ffc7e8f | strength: regulatory
obligated(secretary_of_health_municipalities_and_distrito_federal, none, be_informed_about_monitoring_plan).

% atom_id: fbe9c54a6b288d5e | chunk: 514aa25a3ffc7e8f | strength: regulatory
obligated(secretary_of_primary_healthcare, none, publish_monitoring_plan_on_internet).

% atom_id: 1bb6357fb9c8ba7c | chunk: 528c8685faa4e930 | strength: regulatory
obligated(ministry_of_health, none, monitoring).

% atom_id: 3d2bd3ef52c3bc7a | chunk: 528c8685faa4e930 | strength: regulatory
obligated(health_establishment, none, submit_reports).

% atom_id: ed246007cc6599e5 | chunk: 528c8685faa4e930 | strength: regulatory
obligated(cgcansaes, none, conduct_technical_visits).

% atom_id: 038697499fffb3bc | chunk: 52b8601359c24bab | strength: regulatory
obligated(coordenacao_geral_de_inovacao_e_informatica_em_saude, none, provide_technical_logistical_and_administrative_support).

% atom_id: 1f68439abb350b69 | chunk: 55425486654d0e9e | strength: regulatory
permitted(institution, none, present_retification_to_audit_report).

% atom_id: 1918801a8d43a7f1 | chunk: 55e4299b061bce33 | strength: regulatory
obligated(drac_sas_ms, none, coordinate_and_monitor_pnass).

% atom_id: b42d5c4c8f6a33fa | chunk: 55e9cb273fec8651 | strength: regulatory
permitted(credenciado_estabelecimento, none, utilize_material_publicitario_e_fazer_campanha_publicitaria) :-
    acesso_ao_ambiente_de_producao(sim).

% atom_id: de83dd3eedebdc0b | chunk: 55e9cb273fec8651 | strength: regulatory
obligated(credenciado_estabelecimento, none, seguir_diretrizes_definidas_pelo_ministerio_da_saude_no_manu) :-
    acesso_ao_ambiente_de_producao(sim).

% atom_id: 69ca846a320c73f7 | chunk: 5876ccb686c56998 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, send_supplement_of_vitamin_a).

% atom_id: 2546a4564688fd7d | chunk: 5876ccb686c56998 | strength: regulatory
obligated(secretaria_de_ciencia_tecnologia_e_insumos_estrategicos, none, send_supplement_of_vitamin_a).

% atom_id: 47f75d820ac65dc2 | chunk: 592faefd67f45e28 | strength: regulatory
permitted(state_manager, none, request_documents_and_information).

% atom_id: be314fe0e965ba13 | chunk: 592faefd67f45e28 | strength: regulatory
permitted(state_manager, none, conduct_in_person_or_remote_inspection).

% atom_id: 20ce8724faff61fc | chunk: 59da0effbd5b40e0 | strength: regulatory
obligated(sgtes, none, monitoring_of_compliance_with_commitments_in_tenders).

% atom_id: 0c7f0ad4123725ad | chunk: 5a45c04de00cfa2e | strength: regulatory
obligated(sad, patient, ensure_continuity_of_care).

% atom_id: 213790775b7268bb | chunk: 5a45c04de00cfa2e | strength: regulatory
obligated(ras_points, patient, provide_integral_care).

% atom_id: 8132253e09727bfe | chunk: 5ab06da5fbe7eef0 | strength: regulatory
obligated(service_of_hemotherapy, none, perform_immunohematological_exams_for_donor_qualification).

% atom_id: 296f44f442fe7b33 | chunk: 5bb8e7df2fb4132f | strength: regulatory
obligated(authority, none, insert_program_academia_da_saude).

% atom_id: d629de67b0120604 | chunk: 5dc345a23d6401f4 | strength: regulatory
obligated(state, medical_practitioner, utilize_criterially_blood_transfusion).

% atom_id: db4b34e7317a22da | chunk: 5e58e0bf6b4db062 | strength: regulatory
obligated(state, portadores_de_diabetes_mellitus, disponibilizar_medicamentos_e_insumos).

% atom_id: 2a5c388a21d87bf8 | chunk: 5e703e1c72180b35 | strength: regulatory
obligated(group_executive, ministry_of_health, coordinate_pnpmf_program).

% atom_id: 0c724f56dcb1f5c6 | chunk: 5e76c4700c4db3bf | strength: regulatory
obligated(sctie_ms, none, monitor_technical_capacitation_activities).

% atom_id: 3d45b84b3bbacad9 | chunk: 5e76c4700c4db3bf | strength: regulatory
obligated(sctie_ms, none, monitor_project_executive_and_cronogram).

% atom_id: 58aa7b2baf666f17 | chunk: 5e76c4700c4db3bf | strength: regulatory
obligated(sctie_ms, none, monitor_technology_transfer_process).

% atom_id: 6a3e0d166f41f75b | chunk: 5e76c4700c4db3bf | strength: regulatory
obligated(sctie_ms, none, monitor_institutional_capacities_development).

% atom_id: b7594c45974a5860 | chunk: 5e76c4700c4db3bf | strength: regulatory
obligated(ctr, none, participate_in_monitoring_activities).

% atom_id: b2651a421d6c3fcf | chunk: 5f295173c03ef366 | strength: regulatory
obligated(state, healthcare_provider, use_equipment_free_of_pyrogens_and_disposables_with_filter).

% atom_id: 9e03a50d9a4506cd | chunk: 5f5491e64cab993f | strength: regulatory
prohibited(industria_nacional_ou_internacional, none, enviar_sangue_componentes_e_derivados) :-
    utilizacao_na_producao_de_reagentes_de_diagnostico_ou_painel(true),
    para_industria_nacional_ou_internacional(true),
    natureza_publica_ou_privada(true).

% atom_id: 0e5172fd7d14f85a | chunk: 5f5491e64cab993f | strength: regulatory
prohibited(laboratorio, none, enviar_sangue_componentes_e_derivados) :-
    utilizacao_na_producao_de_reagentes_de_diagnostico_ou_painel(true).

% atom_id: a0ddeb6cc76ae6e9 | chunk: 6052954ac41dae13 | strength: regulatory
obligated(state, woman_and_newborn, elaborate_singulate_therapeutic_project).

% atom_id: 814eb0979d14bd94 | chunk: 6439543bf5e32cfa | strength: regulatory
obligated(state, none, qualify_equipment_prior_to_use).

% atom_id: e9fed616b755a3e9 | chunk: 6439543bf5e32cfa | strength: regulatory
obligated(state, none, operate_equipment_according_to_manufacturer_specifications).

% atom_id: 8a384740fd639f87 | chunk: 64cc8e8f026d40ca | strength: regulatory
obligated(secretaria_de_vigilanca_em_saude, none, orientar_estados_e_municipios).

% atom_id: 5bd909cb3e7c645b | chunk: 64cc8e8f026d40ca | strength: regulatory
obligated(estados_e_municipios, none, instituir_comites_estaduais_e_municipais_de_mobilizacao_cont).

% atom_id: 6a64d8e17769da39 | chunk: 64e698437f9d3b95 | strength: regulatory
obligated(state, none, enhance_basic_healthcare_services).

% atom_id: 0306e55a509a8010 | chunk: 670e879217558062 | strength: regulatory
obligated(health_institution, none, establish_at_least_one_transfusion_agency) :-
    type_of_intervention(interventions_cirurgicas_grande_porte_atendimentos_de_urgenc),
    monthly_transfusions(X_1), X_1 >= 60.

% atom_id: 3af2094a8267015b | chunk: 67137dce42e6aeba | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude_secretaria_de_atencao_a_sa, none, adopt_measures).

% atom_id: f8ecaa7cef7c4ec0 | chunk: 6753591a9926c444 | strength: regulatory
obligated(sctie_ms, pdp_project, suspend_project) :-
    project_status(em_desacordo_com_requisitos_em_desacordo_com_criterios_em_de).

% atom_id: 50bbb47a58d8743b | chunk: 6753591a9926c444 | strength: regulatory
obligated(technical_evaluation_committees, pdp_project, analyze_project) :-
    project_status(em_desacordo_com_requisitos_em_desacordo_com_criterios_em_de).

% atom_id: 31c4a97daf17e128 | chunk: 6753591a9926c444 | strength: regulatory
obligated(deliberative_committee, pdp_project, make_decision) :-
    project_status(em_desacordo_com_requisitos_em_desacordo_com_criterios_em_de).

% atom_id: acf9c972fc1b8441 | chunk: 677b4f9ccdbcfd42 | strength: regulatory
obligated(secretaria_finalistica_do_ministerio_da_saude, none, realizar_analise_das_atividades_executadas_e_emissao_de_pare).

% atom_id: 6cd21d648362c25f | chunk: 6aacee3d337215c7 | strength: regulatory
obligated(se_ms, none, provide_administrative_support_and_necessary_means).

% atom_id: 9b2607e08ebed955 | chunk: 70047f3da96e8536 | strength: regulatory
obligated(coordinator_of_sinasan, none, define_usage_of_excess_plasma).

% atom_id: fdd6d6aaf7c2a7ef | chunk: 707988cfb5b1ff6d | strength: regulatory
obligated(laboratorios_oficiais_de_controle_de_qualidade, none, execute_reference_analysis).

% atom_id: 0a5e5805654ab96b | chunk: 70ee3e019b9ce15a | strength: regulatory
permitted(pfc_provider, none, store_pfc_below_neg18c).

% atom_id: e705a7a02bea0199 | chunk: 70ee3e019b9ce15a | strength: regulatory
obligated(pfc_provider, none, maintain_pfc_validity).

% atom_id: 8586d65640f3d761 | chunk: 71af9f74e61af05e | strength: regulatory
obligated(state, none, reinforce_health_event_monitoring).

% atom_id: 0f1d7c5dde53b2bb | chunk: 72e8897cb529719e | strength: regulatory
permitted(secretary_of_vigilance_in_health, none, edit_complementary_rules_for_execution).

% atom_id: ffa335bef534d158 | chunk: 73a4146d3070ac29 | strength: regulatory
obligated(medical_doctor, hemotherapy_doctor, concur_with_therapeutic_apheresis) :-
    solicitation(written_request_from_patients_doctor).

% atom_id: f44cbd1e59c4115b | chunk: 73a4146d3070ac29 | strength: regulatory
obligated(medical_doctor, patient, request_therapeutic_apheresis).

% atom_id: 778ffd48006c5529 | chunk: 73aa433fe3b7d1b8 | strength: regulatory
obligated(ministry_of_health, none, instaurate_audit) :-
    irregularities_or_non_compliance(present).

% atom_id: 7a9da1264dbffc95 | chunk: 73aa433fe3b7d1b8 | strength: regulatory
obligated(ministry_of_health, none, offer_denunciation) :-
    irregularities_or_non_compliance(present).

% atom_id: 4b85d338df40c00b | chunk: 73bd0384a04df31f | strength: regulatory
obligated(state_or_distrito_federal, none, enable_sentinel_health_unit) :-
    location(capital).

% atom_id: e8d97b3b4bee0d18 | chunk: 73bd0384a04df31f | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude, none, select_sentinel_health_units) :-
    location(capital),
    compliance(art_335_m_information).

% atom_id: 63eb13f825f312d3 | chunk: 7420ffebff5bb8f7 | strength: regulatory
obligated(federative_entity, none, provide_evidence_of_program_implementation).

% atom_id: af410f89182999f5 | chunk: 748285f3d1db0aa8 | strength: regulatory
obligated(state, hospital, fill_aih_form) :-
    case_type(accident_disease),
    work_related(true).

% atom_id: db45b270635d960f | chunk: 772a6da511042620 | strength: regulatory
obligated(federative_entities, none, submit_documentation).

% atom_id: d86c2ac8295b7ed4 | chunk: 77e4a2bde13f6f21 | strength: regulatory
obligated(cnpmmfi, none, reunir_em_caracter_ordinario).

% atom_id: 1339729a0d20a96d | chunk: 77e4a2bde13f6f21 | strength: regulatory
obligated(cnpmmfi, none, reunir_em_caracter_extraordinario) :-
    secretaria_executiva_do_comite(none),
    presidencia(none).

% atom_id: 3d89eba446d3fd1a | chunk: 7852dbecbc424582 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, establish_clinical_protocol_and_therapeutic_guidelines).

% atom_id: 3c57f77d1d96afb3 | chunk: 7852dbecbc424582 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, include_medications_in_rol_of_exceptional_drugs).

% atom_id: 12310d93bbdc0720 | chunk: 7852dbecbc424582 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, adopt_other_measures_for_fidelity_to_disposition).

% atom_id: 60be960d12084393 | chunk: 7a63e5521f5b90d9 | strength: regulatory
obligated(ministry_of_health, none, promote_professional_capacitation_and_training).

% atom_id: 844d52bd94f84eb1 | chunk: 7a63e5521f5b90d9 | strength: regulatory
obligated(ministry_of_health, none, participate_in_technology_offering_and_infrastructure_provis).

% atom_id: 66ca0a754b8f9515 | chunk: 7ab4baa428a5eaa3 | strength: regulatory
obligated(project_executer, none, submit_financial_reports_with_independent_audit_opinion).

% atom_id: f8049e88b78c02b0 | chunk: 7ae7e3da337af43c | strength: regulatory
obligated(candidate_for_blood_donation, none, interrompere_activities_risking_health) :-
    activity_type(ocupacoes_hobbies_esportes).

% atom_id: 1512e00b07906ceb | chunk: 7ae7e3da337af43c | strength: regulatory
obligated(candidate_for_blood_donation, none, interrompere_activities_risking_health_duration) :-
    activity_type(ocupacoes_hobbies_esportes).

% atom_id: ec0cad962cc1e977 | chunk: 7b8a0301beae90bf | strength: regulatory
permitted(instituicao, none, apresentar_proposta_de_remanejamento) :-
    beneficio_fiscal(atendido).

% atom_id: 55e4ba96c2283a4d | chunk: 7bda0941854f7461 | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, adopt_measures_for_implementing_dispositions).

% atom_id: 90a9f3ad7caf5c8a | chunk: 7bda0941854f7461 | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude, none, adopt_measures_for_implementing_dispositions).

% atom_id: 11ff73cea05574bb | chunk: 7bee1621244da2c4 | strength: regulatory
obligated(authority, none, evaluate_and_monitor_pnqm).

% atom_id: 4f3209395cc2b856 | chunk: 7d4d29e3c6909bc1 | strength: regulatory
obligated(responsible_party, none, monitor_cyanobacteria_cells) :-
    source_of_water(surface_waters).

% atom_id: 427aef5cdfa9f749 | chunk: 7e19335ee8536110 | strength: regulatory
obligated(orgao_ou_entidade, none, promover_adecuacoes_necessarias).

% atom_id: 39633561e3681bba | chunk: 8106c4e12c075e2a | strength: regulatory
obligated(deployer, none, accept_process_and_monitoring_methods).

% atom_id: 6ca9dbf07b8a31d3 | chunk: 81b6719d41044afa | strength: regulatory
permitted(municipality_or_distrito_federal, none, utilize_difference_in_value_of_resources) :-
    custo_final_da_construcao_do_estabelecimento(incentivo_repassado_pelo_ministerio_da_saude).

% atom_id: e85a8a3d5677f82f | chunk: 81eb2ca2f07d2f6f | strength: regulatory
obligated(titular_or_suplente, none, attend_consecutive_meetings) :-
    justificativa(sem_justificativa),
    reunioes(X_1), X_1 >= 2.

% atom_id: 8684ac5524b600f5 | chunk: 84eff399f5847c81 | strength: regulatory
obligated(authority, none, register_monitoring_and_evaluation_reports).

% atom_id: a38409ed87959885 | chunk: 84eff399f5847c81 | strength: regulatory
obligated(authority, none, conduct_preventive_and_corrective_monitoring_and_evaluation).

% atom_id: d88c8aaf940a0b11 | chunk: 85351a1b2b2bbd36 | strength: regulatory
obligated(gestor_local_sus, none, establish_limit_internations_psiquiatria_and_control_entry_i).

% atom_id: 325d2aa35c0d6eed | chunk: 85351a1b2b2bbd36 | strength: regulatory
obligated(gestor_local_sus, none, establish_instruments_and_mechanisms_specific_resolutivos_at).

% atom_id: df07ff135b723673 | chunk: 86b6a2ede31ae157 | strength: regulatory
obligated(comissao_de_monitoramento_e_avaliacao, none, formalize_meetings_in_minutes).

% atom_id: eafd406f0765bbfa | chunk: 8a8add5e6c725a42 | strength: regulatory
permitted(institution, none, realize_procedures_with_regulation) :-
    proposals(actions_and_services_constant_of_the_relation_of_procedures).

% atom_id: d6d1dc8cc17f8acd | chunk: 8a8add5e6c725a42 | strength: regulatory
obligated(institution, none, observe_vigence_and_requirements) :-
    credenciamento_or_habilitacao(specific_to_the_pronon_or_pronas_pcd).

% atom_id: 1bf8ddc47b1f928b | chunk: 8b1cab230753ba56 | strength: regulatory
obligated(secretaria_de_atencao_primaria_a_saude_do_ministerio_da_saud, none, monitoramento_dos_servicos_habilitados).

% atom_id: 60c2000f8f0e11d2 | chunk: 8b6c175bace3ef59 | strength: regulatory
obligated(institutions, none, accompany_monitor_and_assess_compliance).

% atom_id: 7be5539094c62dfc | chunk: 8b7944bb04600778 | strength: regulatory
permitted(institution_public_or_ict, none, propose_new_pdp).

% atom_id: 0060ac63088dbc18 | chunk: 8b7944bb04600778 | strength: regulatory
obligated(institution_public_or_ict, society, ensure_sus_product_offer).

% atom_id: db50d442cf5e9506 | chunk: 8b7944bb04600778 | strength: regulatory
obligated(institution_public_or_ict, society, rationalize_investments).

% atom_id: cac2dae8f0563dff | chunk: 8c4e12c13fa4c8e1 | strength: regulatory
obligated(secretaria_de_atencao_especializada_a_saude, none, publish_manual_tecnico_do_pntn).

% atom_id: aeafdf4876385e09 | chunk: 8c67044b35d38024 | strength: regulatory
obligated(financial_institution, none, automatically_apply_financial_resources).

% atom_id: 71ecbac449a2fcf7 | chunk: 8e786c7ec70306c0 | strength: regulatory
obligated(credenciado_estabelecimento, none, provide_login_and_password).

% atom_id: 028bf9379ccb6739 | chunk: 8f0c175b33c951c1 | strength: regulatory
obligated(dsei, indigenous_communities, maintain_water_supply_infrastructure).

% atom_id: fa1e544dfe9766e5 | chunk: 8f0c175b33c951c1 | strength: regulatory
obligated(dsei, indigenous_communities, avoid_discontinuity_of_water_supply).

% atom_id: ab7e57af0a72d2c1 | chunk: 8f2caf6411a2c7a7 | strength: regulatory
obligated(secretarias_de_saude_estados_df_municipios, none, monitoramento_e_avaliacao_programas_residencia_medica).

% atom_id: c479d34b9e0a1a67 | chunk: 8fe463edd14b2ade | strength: regulatory
obligated(svs_ms, none, competence_to_perform_tasks).

% atom_id: f86c5b5f9fb40c92 | chunk: 912e12f2331c622a | strength: regulatory
obligated(specialized_attention_points, people_with_disabilities, act_as_reference_point_for_diagnosis_and_rehabilitation) :-
    pntn(none).

% atom_id: f4b27b18c9316d40 | chunk: 9189c36854f98581 | strength: regulatory
obligated(state, none, describe_fluoridation_techniques).

% atom_id: e6d6eae2fdf57a19 | chunk: 91c994d92ca279de | strength: regulatory
permitted(executive_committee, none, invite_professional_entities).

% atom_id: 79147aa32f584b4b | chunk: 9202b584600d1772 | strength: regulatory
obligated(secretaria_de_ciencia_tecnologia_e_insumos_estrategicos_do_m, none, execute_program_integrated_and_coordinated).

% atom_id: f6e5cd6f61182140 | chunk: 93700e63e91e3db7 | strength: regulatory
obligated(company, none, verify_transactions).

% atom_id: 256428e73cabb9a1 | chunk: 96ea2b5c306e6b38 | strength: regulatory
obligated(sgtes, none, monitor_courses).

% atom_id: 78bf9b67c488982c | chunk: 9824bf4c74383398 | strength: regulatory
permitted(municipality, none, request_habilitation_of_emap_r) :-
    population(X_0), X_0 <= 20000.

% atom_id: 2aa14385043be428 | chunk: 9824bf4c74383398 | strength: regulatory
obligated(emap_r, none, work_integrated_with_ras).

% atom_id: 7b24f050d5c953c8 | chunk: 9a7cc30cbc455f80 | strength: regulatory
obligated(area_finalistica, none, produce_monitoring_and_evaluation_reports).

% atom_id: 28a9802b753feecf | chunk: 9a7cc30cbc455f80 | strength: regulatory
obligated(area_finalistica, comissao_de_monitoramento_e_avaliacao_de_projetos, receive_and_validate_reports).

% atom_id: abc77da2dd9b843c | chunk: 9eb537c5e0942ffc | strength: regulatory
obligated(comissao_gestora, none, reunir_se).

% atom_id: a608477bd8c580c8 | chunk: 9eb537c5e0942ffc | strength: regulatory
obligated(comite_executivo, none, reunir_se).

% atom_id: 2f2d0b4218dca9e4 | chunk: a02116ce579669b6 | strength: regulatory
obligated(members_of_commission_gestora_and_executivo_committee, none, perform_services_publicly).

% atom_id: 15406f0594e1970a | chunk: a06fde4011ef9836 | strength: regulatory
obligated(secretaria_de_atencao_primaria_a_saude_do_ministerio_da_saud, none, analyze_solicitations_for_habilitation).

% atom_id: 2a6bdf3d414f03d2 | chunk: a0fbd915d3592ef3 | strength: regulatory
obligated(state, none, monitor_cysts_giardia_and_oocysts_cryptosporidium) :-
    moving_geometric_mean_of_e_coli(X_0), X_0 >= 1000.

% atom_id: 0905afe9f7a2a267 | chunk: a3647fdb2a2203bd | strength: regulatory
obligated(authority, none, monitor_proposals_for_academia_da_saude_poles).

% atom_id: 99c3170ca1d031ab | chunk: a3cbb56210f5e31e | strength: regulatory
obligated(institution, none, utilize_method_of_evaluation_for_assuring_materials_equipmen).

% atom_id: 3ee0ec30831845ec | chunk: a6f9b9329649a4cf | strength: regulatory
obligated(manufacturer, none, provide_anticoagulants) :-
    bolsa(coleta_de_sangue).

% atom_id: 6884ec9fb69804a0 | chunk: a6f9b9329649a4cf | strength: regulatory
obligated(manufacturer, none, prescribe_anticoagulant_quantities) :-
    bolsa(coleta_de_sangue).

% atom_id: 3bb66fb4b28ed143 | chunk: a6f9b9329649a4cf | strength: regulatory
obligated(manufacturer, none, consider_sangue_volume) :-
    bolsa(coleta_de_sangue).

% atom_id: ea3c5319131a9cda | chunk: a9795a5392ca433b | strength: regulatory
permitted(provider, none, use_platform_transferegov_or_alternative).

% atom_id: 11c6042c9982b4b7 | chunk: a9b516997c96f5dd | strength: regulatory
obligated(ministry_of_health, none, monitor_strategic_public_health_actions_services).

% atom_id: 844c843b9b6177f4 | chunk: a9da9438e3c7d75f | strength: regulatory
obligated(ministry_of_health, none, publish_manual_instructivo_do_pmaq_ab).

% atom_id: c1f99fec13549cd2 | chunk: aa479c97035ed6fc | strength: regulatory
prohibited(indicated_person, none, integrate_monitoring_and_assessment_committee) :-
    time_since_institution_of_committee(X_0), X_0 < 5.

% atom_id: 77e91984ee974e75 | chunk: aa56e9e5384a6fc8 | strength: regulatory
obligated(comissao_de_acompanhamento_ou_grupo_condutor_regional_da_rap, none, define_e_desenvolve_strategias_avaliacao_monitoramento).

% atom_id: acbff4569be3d4bf | chunk: ab2a0f29ece77e17 | strength: statutory
obligated(states, none, finance_healthcare_services).

% atom_id: 58f8a428f9ef5392 | chunk: ab5e3d42e1840368 | strength: regulatory
obligated(state, none, stimulate_innovative_alternatives).

% atom_id: 0006ddbdf97f1fdd | chunk: abd524bfa7e72d07 | strength: regulatory
obligated(state, none, detail_strategic_health_vigilance_actions_and_services).

% atom_id: b52a73b2a12fb27c | chunk: ae21f3c27461941c | strength: regulatory
obligated(secretaria_executiva_da_cpceis, none, elaborate_annual_report).

% atom_id: 0783c392b5bad68f | chunk: ae21f3c27461941c | strength: regulatory
obligated(secretaria_executiva_da_cpceis, none, transmit_report_to_secretaria_executiva_and_gabinete_do_mini).

% atom_id: 612e7de88684bb1d | chunk: ae9dfb3b4c2f5853 | strength: regulatory
permitted(service_of_hemotherapy, none, produce_and_use_reagents_for_immunohematological_tests) :-
    authorization(anvisa).

% atom_id: bd8969efcdd0bfb2 | chunk: aeb385c76f0fc235 | strength: regulatory
obligated(federative_entity, none, comply_with_sentinel_vigilance_goals) :-
    metas_estabelecidas(cumpridas).

% atom_id: 97b492d29b6adfeb | chunk: af2843dcd539c45f | strength: regulatory
obligated(ministry_of_health, none, publish_manual_instructivo).

% atom_id: 80c54566e4e339e7 | chunk: b0b2f1a409740abc | strength: regulatory
obligated(secretario_de_vigilancia_em_saude, none, editar_normas_regulamentadoras_do_comite_nacional_de_mobiliz).

% atom_id: 4ded42674cc58dbb | chunk: b1b43ba5f486e2aa | strength: regulatory
obligated(state, pharmacy_service_provider, coordinate_pharmaceutical_supplies).

% atom_id: e8797b75b5ba7731 | chunk: b27cc5e36eb8be51 | strength: regulatory
obligated(service_of_hemotherapy, none, maintain_control_and_qualification_system).

% atom_id: f43fda9b39c4bf4c | chunk: b27cc5e36eb8be51 | strength: regulatory
obligated(service_of_hemotherapy, none, inspect_products_on_receiving_and_usage).

% atom_id: f7a6361459cebb7c | chunk: b27cc5e36eb8be51 | strength: regulatory
obligated(service_of_hemotherapy, none, monitor_results_obtained_with_input).

% atom_id: 74d7ff847e0d38c2 | chunk: b2beeb3df4cfe620 | strength: regulatory
obligated(department_of_emergencies_in_public_health_secretariat_of_vi, none, conduct_monitoring_and_assessment_of_profesp).

% atom_id: 1a61f37c3c3bb461 | chunk: b42f93c19acd737f | strength: regulatory
permitted(ministry_of_health, none, launch_calls_for_proposals).

% atom_id: ff9085e474c216fd | chunk: b7ddec3dc18cf8f3 | strength: regulatory
obligated(state, person_with_mental_suffering_or_disorder, ensure_integral_care_through_substitutive_strategies).

% atom_id: 1e3344bdc14e4700 | chunk: b7e471069e6e11e7 | strength: regulatory
obligated(coordenador_do_sinasan, none, define_utilizacao_plasma_congelado).

% atom_id: e5de9a46ee387238 | chunk: b8679c1c97832023 | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude_do_ministerio_da_saude, none, manage_vigidesastres).

% atom_id: 0599f315f4704a67 | chunk: b965b7581de2ea58 | strength: regulatory
obligated(secretary_of_vigilance_in_health, none, define_composition_of_technical_committee_and_technical_boar).

% atom_id: 172a17a2fb5ad5ae | chunk: ba6f43595fcde479 | strength: regulatory
obligated(ministry_of_health, none, provide_security_solution).

% atom_id: 13f7d1af44eaec0a | chunk: ba6f43595fcde479 | strength: regulatory
prohibited(entity, none, use_non_provided_security_solution).

% atom_id: d9c694ad1c27adac | chunk: bb9fccc38467b12c | strength: regulatory
obligated(ministry_of_health, none, provide_security_solution) :-
    process_phase(first).

% atom_id: fda0439d6e8476fb | chunk: bb9fccc38467b12c | strength: regulatory
prohibited(entity, none, use_non_provided_security_solution) :-
    process_phase(first).

% atom_id: b5bcce3c412e4eea | chunk: bbd74848891688f5 | strength: regulatory
obligated(authority, none, conduct_quality_control).

% atom_id: 40fe32904825b50e | chunk: bc29fbde3351ab72 | strength: regulatory
obligated(secretaria_especial_de_saude_indigena, none, elaborate_raa).

% atom_id: 9e35a2c34189a8fd | chunk: bc29fbde3351ab72 | strength: regulatory
obligated(secretaria_especial_de_saude_indigena, none, verify_compliance_with_program_metas).

% atom_id: 0a24f4c763797e87 | chunk: bdbaf27b963b6628 | strength: regulatory
obligated(gestor_municipal_estadual_distrito_federal, none, solicitacao_formal_rnsvo) :-
    gestao_svo(gestao_municipal_gestao_estadual_gestao_distrito_federal).

% atom_id: 9e922a0d9f607043 | chunk: beda63bd8da8de52 | strength: regulatory
obligated(secretaria_de_vigilanca_em_saude, none, offer_episus_intermediario).

% atom_id: 0fb4edf4314b880d | chunk: c11474df8ed01df6 | strength: regulatory
obligated(ente_federativo, none, doar_medicamentos_e_material_medico_hospitalar).

% atom_id: c68e20a036ef5846 | chunk: c21efd3b081951f7 | strength: regulatory
obligated(health_authority, data_subject, guarantee_confidentiality_of_personal_information).

% atom_id: 4c596f632f6c937f | chunk: c3784f8627bd46bc | strength: regulatory
obligated(commission_of_evaluation_of_excellence_of_health_entities, entity_under_evaluation, supervise_and_monitor).

% atom_id: 22eef048b3e4136e | chunk: c3784f8627bd46bc | strength: regulatory
obligated(commission_of_evaluation_of_excellence_of_health_entities, entity_under_evaluation, request_information_and_documents).

% atom_id: 26ab9dbb50d69767 | chunk: c3784f8627bd46bc | strength: regulatory
obligated(commission_of_evaluation_of_excellence_of_health_entities, entity_under_evaluation, conduct_on_site_visits).

% atom_id: 1d0f826ac5956b55 | chunk: c3784f8627bd46bc | strength: regulatory
obligated(commission_of_evaluation_of_excellence_of_health_entities, entity_under_evaluation, perform_audits).

% atom_id: 3a74839b6f37d0b0 | chunk: c3784f8627bd46bc | strength: regulatory
obligated(commission_of_evaluation_of_excellence_of_health_entities, entity_under_evaluation, comply_with_investigations).

% atom_id: 1000793c0e9d19db | chunk: c4269786fbd23247 | strength: regulatory
obligated(unidades_organizacionais_do_ministerio_da_saude, none, implementar_executar_avaliar_e_monitorar_atividades).

% atom_id: 5343eba179fdf96d | chunk: c43bac459834a763 | strength: regulatory
obligated(federative_entity, none, provide_evidence_of_fund_application).

% atom_id: 3a98f35367402959 | chunk: c4e4d00a505d04a1 | strength: regulatory
obligated(federative_entity, none, comply_with_rag_reporting) :-
    incentive_funding(perceived).

% atom_id: 8d9f1e1031b902de | chunk: c573cc0aa59e242a | strength: regulatory
obligated(authority, sus_manager, evaluate_technologies).

% atom_id: 12d506504a492d8c | chunk: c57eeb96d8f31ce3 | strength: regulatory
obligated(employer, worker_exposed_to_asbestos, encourage_sus_notification) :-
    diagnosis_or_suspicion_of_disease(asbestosisamianto).

% atom_id: 819a9308a210200c | chunk: c5a3d2723dbdb3d0 | strength: regulatory
obligated(ministry_of_health, none, allocate_funding).

% atom_id: f52023c7a16eba3d | chunk: c6cd98150f80c152 | strength: regulatory
obligated(authority, none, execute_health_surveillance_actions).

% atom_id: 326fa63c080f85d9 | chunk: c861d68fbb28ef3e | strength: regulatory
obligated(beneficiary_entity, none, prove_application_of_funds).

% atom_id: 46e1449d51af78f8 | chunk: c8deb56631d8c632 | strength: regulatory
obligated(state, citizen, promote_access_and_rational_use_of_medications).

% atom_id: 02341686c9800ec2 | chunk: c8efad873365da23 | strength: regulatory
obligated(federative_entity, none, provide_evidence_of_revenue_application).

% atom_id: 531f0f59171b8778 | chunk: c928a5d83cd3d29e | strength: regulatory
obligated(mnp_sus, none, homologate_agreements).

% atom_id: 300edf3833412dc2 | chunk: c928a5d83cd3d29e | strength: regulatory
obligated(secretariat_executive, none, facilitate_enclosures).

% atom_id: 7967d791a2fbaefe | chunk: cb79db7fbcb9a0c8 | strength: regulatory
obligated(ministry_of_health_and_state_and_municipal_secretaries_of_he, none, monitor_and_evaluate_violence_sexual_services).

% atom_id: c65ec47a561cbb74 | chunk: cc3e777bf63f597e | strength: regulatory
obligated(ms, none, authorize_pharmacy_adhesion) :-
    farmacias_e_drogarias(os_siguientes_atos).

% atom_id: 90a40aab0a578692 | chunk: cc5702287297d89f | strength: regulatory
obligated(health_establishment, none, detect_diseases_and_aggravations).

% atom_id: 936d9f56c069b2c1 | chunk: cc8cfd569cf6f0b8 | strength: regulatory
permitted(group_executive, none, invite_other_representatives) :-
    collaboration_necessity(ministerio_da_saude_entidades_vinculadas_ao_setor_publico_e).

% atom_id: 3553f8cb5ab80c30 | chunk: cd62e693deddf37e | strength: regulatory
obligated(entity, none, submit_request_for_excellence_recognition).

% atom_id: a2b78f99b7150a96 | chunk: ce0699eb127d45b4 | strength: regulatory
obligated(deployer, none, utilize_sisab_for_data_submission).

% atom_id: 3a923af62d3c3c75 | chunk: d1e17deefce8b9dd | strength: regulatory
obligated(federative_entity, none, insert_monitoring_information_into_sismob).

% atom_id: 44b2cf02e827c7df | chunk: d1e17deefce8b9dd | strength: regulatory
obligated(health_manager, none, permanently_and_continuously_update_data).

% atom_id: c1cc339657d1464f | chunk: d2f391310f176aef | strength: regulatory
obligated(authority, none, perform_hemolysin_test_for_plasma_transfusions).

% atom_id: a0a69055b89aab80 | chunk: d3313aedb57c5072 | strength: regulatory
obligated(svs_ms, none, adopt_measures_for_plenary_functioning_of_rnsvo).

% atom_id: 014fe0f9a5e32185 | chunk: d45f4c9ad58b05b4 | strength: regulatory
obligated(state, healthcare_provider, use_suitable_blood_component) :-
    blood_collection_days(X_0), X_0 < 5.

% atom_id: b214ee364391aa55 | chunk: d54e94beec8330b9 | strength: regulatory
obligated(participant, none, not_earn_compensation).

% atom_id: 3cc4018846343742 | chunk: d54e94beec8330b9 | strength: regulatory
obligated(participant, none, perform_relevant_public_service).

% atom_id: b8119a52ce41b582 | chunk: d93abd8b90ffd14f | strength: regulatory
obligated(union_states_df_municipalities, none, acquire_distribute_dispense_financiate_pharmaceuticals).

% atom_id: 17993b8afcbf1244 | chunk: d967ffcaa1c2efde | strength: regulatory
obligated(estabelecimentos_responsaveis_vigilancia_zoonoses_sus, none, inscricao_no_scnes).

% atom_id: b7657f99e96feb56 | chunk: d967ffcaa1c2efde | strength: regulatory
obligated(servicos_vigilancia_prevencao_controle_zoonoses_acidentes, none, inscricao_no_scnes).

% atom_id: 7489d810550c07cf | chunk: db295e8b69a07e47 | strength: regulatory
obligated(ministry_of_health_sas_ms_secretaria_de_vigilancia_em_saude, none, monitoring_and_assessment_of_program_academia_da_saude_activ).

% atom_id: 2415aaa8432cd54c | chunk: dbe391e5b0d12c82 | strength: regulatory
obligated(state, healthcare_facility, support_visa_t_investigation).

% atom_id: 09f2d38c52d7ba14 | chunk: dc3cb2505aba579c | strength: regulatory
obligated(ministry_of_health, none, apply_direct_contracting) :-
    project_character(emergencia_em_saude_publica_justificada_singularidade_priori).

% atom_id: 990f0341b5df85b8 | chunk: dd7516a25be09206 | strength: regulatory
obligated(authority, none, approve_diagnostic_kits).

% atom_id: d1caed2f9a7ef981 | chunk: df26d3114afd979e | strength: regulatory
obligated(technical_area_responsible_for_funding_research, none, monitor_and_assess_project_results).

% atom_id: 73765246d5b915a5 | chunk: e064b4a2f5836787 | strength: regulatory
obligated(professional, none, complete_training_program).

% atom_id: 7405fdd0060c444a | chunk: e070f1fb77e12dcb | strength: regulatory
obligated(authority, none, institute_mechanisms_for_organization_and_implantation_of_hi).

% atom_id: 74c57c008dde3bbf | chunk: e0f05b10cdd669e3 | strength: regulatory
obligated(sctie_ms, none, implement_monitoring_assessment_and_follow_up_of_procis).

% atom_id: 315708e1b2d8b02a | chunk: e2371ec603dcfa1c | strength: regulatory
obligated(state, families_assisted_by_program, monitor_families_through_vigilance).

% atom_id: 0d792aea1d54a323 | chunk: e2804f288ffeb424 | strength: regulatory
obligated(ministry_of_health, healthcare_establishments, apply_pnass_periodically).

% atom_id: d3d24f8da01d31eb | chunk: e546eb6c38e4c5d1 | strength: regulatory
obligated(orgaos_de_controle_interno, none, monitorar_aplicacao_correta_dos_recursos).

% atom_id: 6264524171c9379c | chunk: e7bedb3fdf57cc9f | strength: regulatory
obligated(system_operator, water_body, monitor_e_coli) :-
    source_type(superficial).

% atom_id: 064d0d91fff44ec5 | chunk: e807a7bade6c5a39 | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude_do_ministerio_da_saude, none, coordinate_comite_tecnico).

% atom_id: 220e10a31c44c82e | chunk: e90ad3736b89b279 | strength: regulatory
obligated(municipal_authority, health_team, evaluate_request).

% atom_id: 85709341b14b436c | chunk: ea4a14bedf010af6 | strength: regulatory
obligated(departamento_de_emergencias_em_saude_publica_secretaria_de_v, none, manage_and_coordinate_episus_program).

% atom_id: eabe77eafdfeaec9 | chunk: ea541f555c296b71 | strength: regulatory
obligated(professional, none, wear_protection_clothing_and_shoes).

% atom_id: 4f01ff8e7774679a | chunk: eaaf7e9d5590274b | strength: statutory
obligated(government, public, ensure_access_and_quality_in_oral_health_services).

% atom_id: 69acd2db3353bffa | chunk: eab01de7b154c134 | strength: regulatory
obligated(orgao_de_controle_interno, none, monitorar_aplicacao_correta_recursos_financeiros).

% atom_id: f43edc04df696756 | chunk: ebb50733462e1798 | strength: regulatory
obligated(hospital, none, be_automaticallycalibrated_as_center_of_reference_for_chroni) :-
    hospital(registered_as_high_complexity_cancer_center).

% atom_id: c4b8857d4d3b7c51 | chunk: ee527d2e26f638e6 | strength: regulatory
obligated(institution, none, send_revised_work_plan_to_secretariat) :-
    percentage_of_funds_raised(X_0), X_0 >= 60.

% atom_id: f22282196c0d9689 | chunk: f0e133aae57ae1f7 | strength: regulatory
permitted(state, none, use_same_cold_room_for_reagents_and_samples).

% atom_id: 705a2951489193b5 | chunk: f152419f5b9a05ce | strength: regulatory
obligated(authority, none, perform_calibration_and_preventive_maintenance).

% atom_id: 4c5c6497657865e4 | chunk: f2b8b4f90b556eac | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, establish_clinical_protocols_and_therapeutic_guidelines).

% atom_id: 2c8ad5b9466f2f13 | chunk: f2b8b4f90b556eac | strength: regulatory
obligated(secretaria_de_atencao_a_saude, none, implement_measures_for_disposition_implementation).

% atom_id: 57cb4b646af3c1bf | chunk: f49d71b9c6042e94 | strength: regulatory
obligated(unidade_sentinela, none, comply_with_obligations) :-
    justificado(false).

% atom_id: 8bc62f7d8be42170 | chunk: f49d71b9c6042e94 | strength: regulatory
obligated(unidade_sentinela, none, disable_from_actions) :-
    meses_consecutivos(X_0), X_0 >= 4.

% atom_id: a60d2b5505caa5de | chunk: f56b0847e64a96b9 | strength: regulatory
obligated(authority, unidade, control_labeling_by_two_different_people) :-
    technology_used(codigo_de_barras_outra_forma_eletronica_validada).

% atom_id: ea319e95d95064a6 | chunk: f6472d36312f02ed | strength: regulatory
obligated(ministry_of_health, none, allocate_financial_resources).

% atom_id: 9d601552b27f367c | chunk: f67d4f35e28a17a3 | strength: statutory
obligated(state, population, contribute_to_expansion_and_valuation_of_public_recreation_s).

% atom_id: da2653fc8f484a1d | chunk: f7b92a9d34034893 | strength: regulatory
obligated(authority, provider, confirm_data_consistency).

% atom_id: 9810f8f951d92524 | chunk: f7d0c90281f91e90 | strength: regulatory
obligated(orgaos_e_entidades, none, manifestar_interesse_de_participar_do_fas) :-
    incisos_do_art_3o(pelo_menos_um).

% atom_id: 73a39c5c4b0b4351 | chunk: f899d373e6891a79 | strength: regulatory
obligated(sas_ms, none, conduct_evaluation_and_monitoring_of_pnqm).

% atom_id: 0dcdc60c5dba2296 | chunk: f899d373e6891a79 | strength: regulatory
obligated(anvisa_and_inca_sas_ms, none, conduct_evaluation_and_monitoring_of_pnqm).

% atom_id: 85483db4f434c95b | chunk: fd0e631522543a4e | strength: regulatory
obligated(institution, none, issue_receipts_to_donors_and_maintain_documentary_control_of).

% atom_id: 5c5c9eafe5ce3167 | chunk: fd0e631522543a4e | strength: regulatory
obligated(institution, ministry_of_health_and_authorities, keep_records_available_for_inspection) :-
    request(instado_a_apresenta_las).

% atom_id: acd248e8a4966552 | chunk: fd39729f65382ca7 | strength: regulatory
obligated(institution, none, accompany_funds).

% atom_id: 28a31476dc41e48c | chunk: fd39729f65382ca7 | strength: regulatory
obligated(institution, none, provide_accounts).

% atom_id: 1a1a4bc6790afdd0 | chunk: fd39729f65382ca7 | strength: regulatory
obligated(institution, none, technical_evaluation).

% atom_id: 755e831aea02b8f8 | chunk: fda8a9cf57c88ffb | strength: regulatory
obligated(sad, none, provide_minimum_12_hours_daily_functioning).

% atom_id: 3d5b10c4602182c8 | chunk: fda8a9cf57c88ffb | strength: regulatory
obligated(sad, none, ensure_continuity_of_healthcare).

% atom_id: b90233c1b952c9ca | chunk: fda8a9cf57c88ffb | strength: regulatory
permitted(sad, none, utilize_plantao_regime).

% atom_id: 26fd4b384c2b4d7c | chunk: fe0226141d061b39 | strength: regulatory
obligated(program, none, coordinate_national_epidemiological_actions).

% atom_id: d63aadcda0ea3614 | chunk: fe84289670ab98bc | strength: regulatory
obligated(secretaria_de_vigilancia_em_saude, none, coordinate_comite_nacional).

% atom_id: 63334bee43e9bc43 | chunk: ff02e228cf418eef | strength: regulatory
obligated(se_ms, entities_of_health_with_recognized_excellence, issue_certification_for_annual_executed_value).