% atom_id: 795d01bdbdfef297 | chunk: 00074de1a9582b83 | strength: constitutional
permitted(provider, worker, establish_private_pension_scheme).

% atom_id: 619ad1100099da7d | chunk: 00074de1a9582b83 | strength: constitutional
obligated(authority, provider, regulate_private_pension_scheme).

% atom_id: dc1cfb2e236d7712 | chunk: 00158639bee6d562 | strength: constitutional
permitted(public, none, peaceful_assembly_in_public_places_without_weapons) :-
    frustrate_previous_meeting(false).

% atom_id: cd778ed2fcb9cf7e | chunk: 00158639bee6d562 | strength: constitutional
obligated(authority, public, prior_notice_of_assembly).

% atom_id: 9700c6be82f9b711 | chunk: 0071c6d0c9d37ca3 | strength: constitutional
obligated(state, public_land, align_land_destination_with_agricultural_policy).

% atom_id: f3e24f4394922905 | chunk: 0071c6d0c9d37ca3 | strength: constitutional
obligated(state, public_land, align_land_destination_with_national_rural_reform_plan).

% atom_id: f0c8e42c855e1d2e | chunk: 01052f6d90ae31d3 | strength: constitutional
obligated(state, society, promote_cultural_policies).

% atom_id: 64c4d9ed37fd939a | chunk: 024815abf27cde6b | strength: constitutional
obligated(state, workplace, organize_labor_inspection).

% atom_id: b97291033d23649e | chunk: 027e6c0ce765b833 | strength: constitutional
permitted(union, none, institute_taxes).

% atom_id: 91e17a669d065dcf | chunk: 027e6c0ce765b833 | strength: constitutional
permitted(state, none, institute_taxes).

% atom_id: 1574e705dab49d43 | chunk: 027e6c0ce765b833 | strength: constitutional
permitted(district_federal, none, institute_taxes).

% atom_id: 2ed029ec9714a55f | chunk: 027e6c0ce765b833 | strength: constitutional
permitted(municipality, none, institute_taxes).

% atom_id: 48bb09f810270484 | chunk: 02bec8fff4337c38 | strength: constitutional
obligated(state, citizen, guarantee_property_rights).

% atom_id: 260f50892fdbce64 | chunk: 033f4905d06af6fc | strength: constitutional
prohibited(collective, none, form_paramilitary_association).

% atom_id: 9c82fa48b5b60236 | chunk: 034264b6c618305a | strength: constitutional
obligated(citizen, chamber_of_deputies, elect_representatives_proportionally).

% atom_id: 13b58bc54414f0a7 | chunk: 0382ed693240c60a | strength: constitutional
obligated(state, citizen, conduct_election_for_governor_and_vice_governor).

% atom_id: d8e29b70ec8875b7 | chunk: 0382ed693240c60a | strength: constitutional
obligated(state, citizen, take_office_on_january_6th).

% atom_id: 862c1d6502b49e29 | chunk: 03892d6110c6ca23 | strength: constitutional
obligated(state, public, establish_national_education_plan).

% atom_id: 31ef8729de70db34 | chunk: 05348b6308051f9f | strength: constitutional
obligated(union, public_service, regulate_public_consortiums_and_cooperation_agreements).

% atom_id: a47662a15bf9ef3d | chunk: 05348b6308051f9f | strength: constitutional
permitted(union, public_service, authorize_associated_management_of_public_services).

% atom_id: 7d0720df01c10ee7 | chunk: 05348b6308051f9f | strength: constitutional
permitted(union, public_service, transfer_total_or_partial_charges_services_personnel_and_ess).

% atom_id: 4e1566e2050a8911 | chunk: 062459975f7a4368 | strength: constitutional
obligated(state, public, conduct_fiscal_policies_to_sustain_public_debt_levels).

% atom_id: f9de16045faf0bfd | chunk: 067ea6b95eaeac3c | strength: constitutional
prohibited(authority, communication, violate_communication_secrecy) :-
    type_of_communication(telephone).

% atom_id: 2a5efb389efc53cd | chunk: 067ea6b95eaeac3c | strength: constitutional
permitted(judiciary_authority, communication, authorize_communication_interception) :-
    type_of_investigation(criminal),
    legal_procedure(processual_penal).

% atom_id: 76a120dc1d884222 | chunk: 0716c4b73eae29a5 | strength: constitutional
obligated(state, public_servant, remunerate_according_to_article_39_paragraph_4).

% atom_id: 8c29df3cc21f7f90 | chunk: 07d3fa20cf98b71c | strength: constitutional
permitted(municipality, public, institute_contribution_for_public_services) :-
    law_form(respecting_local_legislation).

% atom_id: b35ac87dc49b3ae7 | chunk: 07d3fa20cf98b71c | strength: constitutional
permitted(distrito_federal, public, institute_contribution_for_public_services) :-
    law_form(respecting_local_legislation).

% atom_id: 85d47a143bf1a1ee | chunk: 093ffd38449abac4 | strength: constitutional
obligated(state, public_finance, observe_financial_rules) :-
    national_emergency_status(active),
    financial_exercise_period(emergency_period).

% atom_id: 3f4fab6bd21d0b9e | chunk: 09888509c38baf18 | strength: constitutional
obligated(state, data_subject, protect_personal_data_including_digital_media).

% atom_id: 6ddd0201fa4983ae | chunk: 0b55574d8202be99 | strength: constitutional
obligated(union, indigenous_people, demarcate_tribal_lands).

% atom_id: 4d020e047d0355ab | chunk: 0b55574d8202be99 | strength: constitutional
obligated(union, indigenous_people, protect_cultural_rights).

% atom_id: b6c8247b3e3aec93 | chunk: 0b55574d8202be99 | strength: constitutional
obligated(union, indigenous_people, ensure_rights_respected).

% atom_id: c286c3a848eefd9f | chunk: 0c0571ab090f3c13 | strength: constitutional
obligated(state, none, institute_tax_on_goods_and_services).

% atom_id: d123f2f99afc13c5 | chunk: 0c06926e470257fd | strength: constitutional
prohibited(state, municipality, intervene_in_municipalities) :-
    territory_type(regular).

% atom_id: 3aad013ddee43251 | chunk: 0c06926e470257fd | strength: constitutional
prohibited(federal_government, municipality, intervene_in_municipalities) :-
    territory_type(territorial_federation).

% atom_id: 7cf72f16c4527fdb | chunk: 0d63044de16e35a7 | strength: constitutional
permitted(executive_power, none, apply_fiscal_adjustment_mechanism) :-
    debt_ratio(X_0), X_0 > 95,
    duration(n12_months).

% atom_id: 7e1129abc38512a9 | chunk: 0d63044de16e35a7 | strength: constitutional
permitted(legislative_power, none, apply_fiscal_adjustment_mechanism) :-
    debt_ratio(X_0), X_0 > 95,
    duration(n12_months).

% atom_id: 70fc7b1b4f3c14ac | chunk: 0d63044de16e35a7 | strength: constitutional
permitted(judiciary_power, none, apply_fiscal_adjustment_mechanism) :-
    debt_ratio(X_0), X_0 > 95,
    duration(n12_months).

% atom_id: e3c47e223604fc5b | chunk: 0d63044de16e35a7 | strength: constitutional
permitted(public_prosecutor_office, none, apply_fiscal_adjustment_mechanism) :-
    debt_ratio(X_0), X_0 > 95,
    duration(n12_months).

% atom_id: 4dfebb7f1520d43d | chunk: 0d63044de16e35a7 | strength: constitutional
permitted(audit_court, none, apply_fiscal_adjustment_mechanism) :-
    debt_ratio(X_0), X_0 > 95,
    duration(n12_months).

% atom_id: 2fed4d00a83cf566 | chunk: 0d63044de16e35a7 | strength: constitutional
permitted(public_defender_office, none, apply_fiscal_adjustment_mechanism) :-
    debt_ratio(X_0), X_0 > 95,
    duration(n12_months).

% atom_id: 4d409c5f50d32710 | chunk: 0ec7b00c7327f7ff | strength: constitutional
obligated(state, citizen, guarantee_education).

% atom_id: 19bc2c3aa178d67e | chunk: 0ff5afe834b31093 | strength: constitutional
obligated(society, public_finance, finance_social_security).

% atom_id: ce223e0175035096 | chunk: 1296a4a2a044e651 | strength: constitutional
obligated(federal_judge, none, process_and_judge_cases).

% atom_id: 321bc11fb89ab681 | chunk: 1340202d598da46d | strength: constitutional
permitted(indian_community, none, file_lawsuit_in_defense_of_rights).

% atom_id: 9700eb16953107a4 | chunk: 1340202d598da46d | strength: constitutional
permitted(public_ministry, none, intervene_in_legal_proceedings).

% atom_id: da44df406a3ac3ba | chunk: 13a284daa8292796 | strength: constitutional
prohibited(state, distrito_federal, divide_into_municipalities).

% atom_id: 13cf5098f0459ded | chunk: 13a284daa8292796 | strength: constitutional
obligated(state, distrito_federal, regulate_by_organic_law) :-
    voting_rounds(2),
    minimum_interval_days(X_1), X_1 >= 10.

% atom_id: 23d7f76dc30390bd | chunk: 13a284daa8292796 | strength: constitutional
obligated(chamber_of_deputies, organic_law, approve_with_two_thirds_majority).

% atom_id: f69160ef9c34cdf3 | chunk: 13a284daa8292796 | strength: constitutional
permitted(chamber_of_deputies, organic_law, promulgate).

% atom_id: a6016dd75b3e80d1 | chunk: 1841b7bc18aef19b | strength: constitutional
prohibited(non_state_actors, individual, enter_house_without_consent).

% atom_id: 7c642519bda674ff | chunk: 1841b7bc18aef19b | strength: constitutional
permitted(non_state_actors, individual, enter_house_without_consent) :-
    circumstance(flagrant_crime).

% atom_id: 617e0ebeececf15b | chunk: 1841b7bc18aef19b | strength: constitutional
permitted(non_state_actors, individual, enter_house_without_consent) :-
    circumstance(disaster).

% atom_id: 8e70d62f3e29d6a6 | chunk: 1841b7bc18aef19b | strength: constitutional
permitted(non_state_actors, individual, enter_house_without_consent) :-
    circumstance(render_assistance).

% atom_id: 5d0831a5e42a898d | chunk: 1841b7bc18aef19b | strength: constitutional
permitted(judiciary_authority, individual, enter_house_without_consent) :-
    time_of_day(day).

% atom_id: 635a8f3d1da73721 | chunk: 187d180c95d30b24 | strength: constitutional
obligated(state, public_finance, review_distribution_criteria) :-
    time_since_initial_application(n6_years).

% atom_id: bccd5f5c21aadb23 | chunk: 187d180c95d30b24 | strength: constitutional
obligated(state, public_finance, review_distribution_criteria) :-
    time_since_initial_review(n10_years).

% atom_id: a729f64e94824bff | chunk: 190bd6f04e8e096a | strength: constitutional
prohibited(state, condemned_person, impose_penalty_on_successor).

% atom_id: 3ac9569093a3861e | chunk: 190bd6f04e8e096a | strength: constitutional
obligated(state, condemned_person, extend_obligation_to_repair_damage_to_successors).

% atom_id: 667545e27b18d02b | chunk: 190bd6f04e8e096a | strength: constitutional
obligated(state, condemned_person, execute_penalty_against_successors_within_limit_of_transferr).

% atom_id: 288c1a1c5a305746 | chunk: 191071165737b53e | strength: constitutional
obligated(legislature, judicial_organ, regulate_constitution_investment_jurisdiction_competence_gua).

% atom_id: 4a0369d011d87157 | chunk: 1a4bcf1be590d116 | strength: constitutional
obligated(state, senator, be_elected_under_majority_principle).

% atom_id: 7ed9b93eb78d8a9c | chunk: 1be83c9c6cbe7b72 | strength: constitutional
permitted(person, none, freedom_of_movement_within_national_territory).

% atom_id: 24377ca840ec175e | chunk: 1d62b8323ab32f4c | strength: constitutional
obligated(president_of_the_republic, tribunal_judges, nominate_tribunal_judges) :-
    judge_age(X_0), X_0 >= 30,
    judge_age(X_1), X_1 <= 70.

% atom_id: c9e7829c623abcaa | chunk: 1daac06bd1705849 | strength: constitutional
obligated(authority, person, ensure_privacy_rights).

% atom_id: dd1e84c8367d9e14 | chunk: 1e1e1a318c7dac88 | strength: constitutional
obligated(supremo_tribunal_federal, none, guard_constitution).

% atom_id: 18122717f19efc88 | chunk: 1eefabe4704853dd | strength: constitutional
obligated(president_of_the_republic, senate_federal, nominate_military_ministers) :-
    number_of_nominees(15),
    military_branch(navy_army_air_force).

% atom_id: 1ea43279dbec432b | chunk: 1eefabe4704853dd | strength: constitutional
obligated(senate_federal, president_of_the_republic, approve_nomination_military_ministers) :-
    number_of_approvals(15),
    military_branch(navy_army_air_force).

% atom_id: 966a2d72ea7c5049 | chunk: 1f1ed681a6e6f5ed | strength: constitutional
obligated(state, worker, organize_social_security_system).

% atom_id: 2631bb8d90d7fc83 | chunk: 1f1ed681a6e6f5ed | strength: constitutional
obligated(worker, state, participate_in_social_security_system).

% atom_id: ee063caacb7b051e | chunk: 1fa267f1969d31ed | strength: constitutional
prohibited(state, none, exceed_personal_expense_limits).

% atom_id: d8bc4f15aed45a0f | chunk: 22ae072802dbda37 | strength: constitutional
obligated(state, public_servant, participate_in_contributive_pension_system).

% atom_id: e648b66be3ca87ce | chunk: 22ae072802dbda37 | strength: constitutional
obligated(state, retired_public_servant, participate_in_contributive_pension_system).

% atom_id: 2081e2871fc84d6f | chunk: 22ae072802dbda37 | strength: constitutional
obligated(state, public_servant_beneficiary, participate_in_contributive_pension_system).

% atom_id: b18a31e6c31f8e5c | chunk: 22ae072802dbda37 | strength: constitutional
obligated(state, pension_beneficiary, participate_in_contributive_pension_system).

% atom_id: f6c206666ffa8ea2 | chunk: 23e05f912fd8582b | strength: constitutional
obligated(state, rubber_tappers, provide_compensation).

% atom_id: 918e1f5ded82c010 | chunk: 241ff6a3cc1cc22b | strength: constitutional
obligated(tribunal_of_accounts_uni, public, exercise_attributions).

% atom_id: d45053901b1a617e | chunk: 24e000691c37a721 | strength: constitutional
prohibited(authority, civilly_identified_person, submit_to_criminal_identification) :-
    legal_provisions(false).

% atom_id: 32ceaeea521ac93a | chunk: 265f900706274d00 | strength: constitutional
obligated(state, public, repudiate_terrorism_and_racism).

% atom_id: 8aa650545bd4665c | chunk: 267e2f368038ba55 | strength: constitutional
permitted(state, school, direct_public_funds_to_community_confessional_or_charitable) :-
    type_of_school(community_confessional_or_charitable).

% atom_id: 66699f5aeb8abdd9 | chunk: 26f43223521727a6 | strength: constitutional
obligated(authority, citizen, provide_information_to_public) :-
    interest_type(personal),
    interest_type(collective_or_general).

% atom_id: 0159c8ecb3dc9d66 | chunk: 26f43223521727a6 | strength: constitutional
prohibited(authority, public_information, disclose_information_without_legal_basis) :-
    security_impact(high).

% atom_id: 3a1f09ebeb8bd631 | chunk: 27205a635f15807a | strength: constitutional
obligated(state, none, conduct_election) :-
    vacant_positions(president_vice_president).

% atom_id: f1d202c68331cb4c | chunk: 27b618a8793cbecf | strength: constitutional
obligated(collective, none, approve_laws_complementary_majority_absolute).

% atom_id: 26943b3c9c51b2bb | chunk: 284ded093bba27d1 | strength: constitutional
obligated(state, needy_person, provide_legal_orientation).

% atom_id: 32e655a8dcc5901d | chunk: 284ded093bba27d1 | strength: constitutional
obligated(state, human_rights, promote_human_rights).

% atom_id: 6522d09ffb14e7c4 | chunk: 284ded093bba27d1 | strength: constitutional
obligated(state, needy_person, defend_legal_rights).

% atom_id: 7b734ada2f1c44fc | chunk: 28ac878b9c71b961 | strength: constitutional
obligated(public_procurator, state, defend_legal_order).

% atom_id: 333cb304b8229d0e | chunk: 28ac878b9c71b961 | strength: constitutional
obligated(public_procurator, state, defend_democratic_regime).

% atom_id: e1559d7836a7ad49 | chunk: 28ac878b9c71b961 | strength: constitutional
obligated(public_procurator, citizen, defend_individual_interests) :-
    interest_type(indisponivel).

% atom_id: 378ffb7b68fb510d | chunk: 28ac878b9c71b961 | strength: constitutional
obligated(public_procurator, society, defend_social_interests) :-
    interest_type(indisponivel).

% atom_id: c4c2d642cb951094 | chunk: 29a4918d6a2dd6d4 | strength: constitutional
prohibited(union, none, unspecified_action).

% atom_id: e0df669925205aae | chunk: 29a4918d6a2dd6d4 | strength: constitutional
prohibited(state, none, unspecified_action).

% atom_id: 1e2403e004eb64f4 | chunk: 29a4918d6a2dd6d4 | strength: constitutional
prohibited(district_federal, none, unspecified_action).

% atom_id: 358400adc71764d2 | chunk: 29a4918d6a2dd6d4 | strength: constitutional
prohibited(municipality, none, unspecified_action).

% atom_id: 6b5db6ec2f04f2cf | chunk: 2b1d7e37d659a193 | strength: constitutional
obligated(collective, public, organize_national_system_of_science_technology_and_innovatio).

% atom_id: e8e0e1d79fd08ddc | chunk: 2b69fed7b3528ade | strength: constitutional
permitted(citizen, authority, request_writ_of_mandamus) :-
    right_status(liquid_and_certain),
    protected_right(habeas_corpus_habeas_data).

% atom_id: 0e058e1dcaa82e5f | chunk: 2b69fed7b3528ade | strength: constitutional
obligated(authority, citizen, protect_right_through_mandamus) :-
    right_status(liquid_and_certain),
    protected_right(habeas_corpus_habeas_data).

% atom_id: 9b3f394001a9dd3c | chunk: 2b6da17a0fe6e34e | strength: constitutional
obligated(state, public, institute_administration_policy_and_remuneration_council).

% atom_id: 799ee674ceb35ef7 | chunk: 2c9ea2b1d774cdab | strength: constitutional
prohibited(authority, individual, detain_without_pretrial_release) :-
    legal_provision(pretrial_release).

% atom_id: 438516af844a536e | chunk: 2cc66f17cc14d22d | strength: constitutional
obligated(congressional_majority, none, appoint_commission_members) :-
    constitution_promulgation(true).

% atom_id: df982a5b48089856 | chunk: 2cc66f17cc14d22d | strength: constitutional
obligated(executive_power, none, appoint_commission_members) :-
    constitution_promulgation(true).

% atom_id: 068a7140607f9343 | chunk: 2cc66f17cc14d22d | strength: constitutional
obligated(commission_of_territorial_studies, none, present_territorial_study_reports) :-
    constitution_promulgation(true),
    time_since_constitution_promulgation(X_1), X_1 <= 90.

% atom_id: 5e13c45d1bbf3c50 | chunk: 2e47413c1b15a579 | strength: constitutional
permitted(union, none, firm_cooperation_instruments) :-
    entity_type(public_org),
    entity_type(private_entity).

% atom_id: 573786e417aa2acc | chunk: 2e47413c1b15a579 | strength: constitutional
permitted(state, none, firm_cooperation_instruments) :-
    entity_type(public_org),
    entity_type(private_entity).

% atom_id: d7392c7796db5375 | chunk: 2e47413c1b15a579 | strength: constitutional
permitted(district_federal, none, firm_cooperation_instruments) :-
    entity_type(public_org),
    entity_type(private_entity).

% atom_id: ddc97d55b0807abd | chunk: 2e47413c1b15a579 | strength: constitutional
permitted(municipality, none, firm_cooperation_instruments) :-
    entity_type(public_org),
    entity_type(private_entity).

% atom_id: 306520829f9dca88 | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(union, public_org_private_entity, share_specialized_human_resources) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: 7369b4cf78a8bc60 | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(state, public_org_private_entity, share_specialized_human_resources) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: 3daf31f9d298fec5 | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(district_federal, public_org_private_entity, share_specialized_human_resources) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: 089f0f45b8c6bad9 | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(municipality, public_org_private_entity, share_specialized_human_resources) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: eed7990e889fdd2b | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(union, beneficiary_entity, provide_counterpart_financial_or_nonfinancial) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: 2df362c60547941f | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(state, beneficiary_entity, provide_counterpart_financial_or_nonfinancial) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: 4dbefe5d5b7d4983 | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(district_federal, beneficiary_entity, provide_counterpart_financial_or_nonfinancial) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: fb940e42c58fa556 | chunk: 2e47413c1b15a579 | strength: constitutional
obligated(municipality, beneficiary_entity, provide_counterpart_financial_or_nonfinancial) :-
    project_type(research),
    project_type(scientific_technological_development),
    project_type(innovation).

% atom_id: 5c80b624a3b3075d | chunk: 2e4802ed41ce5aa0 | strength: constitutional
obligated(union, none, maintain_independent_harmonious_powers).

% atom_id: 0c54ca143f350e0a | chunk: 2edcf3898e6ea3ce | strength: constitutional
obligated(executive_power, none, establish_laws).

% atom_id: 60f613c515142497 | chunk: 2f069eb965802d4d | strength: constitutional
permitted(executive_power, none, grant_concession_permission_authorization_radiodiffusion_ser).

% atom_id: 1e28a23f3ac27425 | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, criminalize_crimes_without_bail_or_pardon) :-
    crime_type(torture).

% atom_id: 2f118c76e6310e1a | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, criminalize_crimes_without_bail_or_pardon) :-
    crime_type(illicit_drug_trafficking).

% atom_id: ed4e59976168b7e9 | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, criminalize_crimes_without_bail_or_pardon) :-
    crime_type(terrorism).

% atom_id: 460aea5c145c7ff5 | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, criminalize_crimes_without_bail_or_pardon) :-
    crime_type(heinous_crime).

% atom_id: 16efc2f674c9fc5f | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, hold_responsible_for_heinous_crimes) :-
    crime_type(heinous_crime),
    role_in_crime(mandator).

% atom_id: dedb0950929aecf4 | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, hold_responsible_for_heinous_crimes) :-
    crime_type(heinous_crime),
    role_in_crime(executor).

% atom_id: b486fdb92cf995e8 | chunk: 31425fe0bd3e8067 | strength: constitutional
obligated(state, public, hold_responsible_for_heinous_crimes) :-
    crime_type(heinous_crime),
    role_in_crime(omitter).

% atom_id: 350b4edb9821e7ed | chunk: 315f8b8385ac3257 | strength: constitutional
permitted(authority, public, use_private_property_in_emergency) :-
    emergency_risk(imminent_public_danger).

% atom_id: fd7cbb4d95a8bad9 | chunk: 32d49caca6c73330 | strength: constitutional
prohibited(authority, none, adopt_interim_measures_for_constitutional_articles_regulatio) :-
    emend_date(X_0), X_0 >= 1995,
    emend_date(X_1), X_1 <= 2001.

% atom_id: 81895f09e1a9bda7 | chunk: 32dd576e4b1c5929 | strength: constitutional
obligated(state, public, publish_tax_collection_amounts).

% atom_id: 939958fb1e53d7cb | chunk: 3468abf3803b9aec | strength: constitutional
obligated(state, stranger_property, regulate_stranger_succession_benefiting_brz_spouse_or_childr) :-
    more_favorable_personal_law_of_deceased(false).

% atom_id: 00f5866a996987f3 | chunk: 34c225a24eedeaa5 | strength: constitutional
obligated(state, tribunal_of_accounts, apply_norms_to_organization_and_composition).

% atom_id: 7b8bea51ad7d97fb | chunk: 34c225a24eedeaa5 | strength: constitutional
obligated(state, tribunal_of_accounts, apply_norms_to_fiscalization).

% atom_id: 81da232515699e07 | chunk: 35d4a70eb3e096d4 | strength: constitutional
prohibited(union, state_or_district_federal, intervene) :-
    reason_for_intervention(none).

% atom_id: 219a57ce6c313480 | chunk: 36738dec96f080d6 | strength: constitutional
obligated(authority, none, declare_intervention).

% atom_id: fa92c76609d5bffd | chunk: 3887310b2f47c13b | strength: constitutional
obligated(state, none, observe_normative_basics) :-
    creation_year_of_state(X_0), X_0 <= 10.

% atom_id: c416bf15ce510615 | chunk: 39976166f2dbb16e | strength: constitutional
obligated(authority, worker_and_employer, ensure_participation_in_councils).

% atom_id: 857354b2f7a2c1f8 | chunk: 3b0cea3debb3e234 | strength: constitutional
obligated(state, public, disseminate_financial_information).

% atom_id: 5a102f5927e18866 | chunk: 3d0f3871bb1ff253 | strength: constitutional
obligated(supremo_tribunal_federal, none, initiate_complementary_law).

% atom_id: e1b5ba5288961bb5 | chunk: 3d0f3871bb1ff253 | strength: constitutional
obligated(legislature, none, enact_complementary_law_on_judges_statute).

% atom_id: 82ef942968fe6bf0 | chunk: 3e512f833226047e | strength: constitutional
prohibited(employer, state, contribute_to_private_entities).

% atom_id: 86a551ec29164965 | chunk: 3ee4ed63e8c7fb99 | strength: constitutional
prohibited(state, none, prejudice_acquired_right).

% atom_id: 3994d0fc6400e827 | chunk: 3ee4ed63e8c7fb99 | strength: constitutional
prohibited(state, none, prejudice_perfect_legal_act).

% atom_id: cef433fc9bc4a093 | chunk: 3ee4ed63e8c7fb99 | strength: constitutional
prohibited(state, none, prejudice_judicial_settlement).

% atom_id: f96e71e4d2ec00e8 | chunk: 3faf1f593447f334 | strength: constitutional
obligated(state, public_sector, exercise_regulatory_functions).

% atom_id: 05d253f68591b546 | chunk: 3faf1f593447f334 | strength: constitutional
obligated(state, private_sector, exercise_regulatory_functions).

% atom_id: 627f379c06350e12 | chunk: 40a4a4c3a5eb84e9 | strength: constitutional
obligated(state, executor_or_agent_of_defense_state, assume_responsibility_for_illicit_actions) :-
    status(post_emergency).

% atom_id: 5b83321e951d8ec4 | chunk: 43ff2e692fee93a0 | strength: constitutional
obligated(authority, judge_with_temporary_investment, grant_stability) :-
    admission_method(public_concours),
    status_date(constitution_promulgation_date).

% atom_id: c52941d3e8565fe3 | chunk: 43ff2e692fee93a0 | strength: constitutional
obligated(authority, judge_with_temporary_investment, maintain_competences_prerogatives_restrictions) :-
    admission_method(public_concours),
    status_date(constitution_promulgation_date).

% atom_id: 80d6feb9d4f1b7f9 | chunk: 43ff2e692fee93a0 | strength: constitutional
obligated(authority, judge_with_temporary_investment, observe_probatory_stage) :-
    admission_method(public_concours),
    status_date(constitution_promulgation_date).

% atom_id: f07d9594996a1e79 | chunk: 43ff2e692fee93a0 | strength: constitutional
obligated(authority, judge_with_temporary_investment, maintain_quadro_extinction) :-
    admission_method(public_concours),
    status_date(constitution_promulgation_date).

% atom_id: 248fdff93318e64f | chunk: 44a1107dfa70b7fe | strength: constitutional
obligated(authority, territory, organize_administrative_and_judicial_system).

% atom_id: bdb53f670d434c97 | chunk: 463efc561f8a5355 | strength: constitutional
obligated(president_of_the_republic, none, elaborate_delegated_laws) :-
    delegation_request(requested_from_congress).

% atom_id: 67cc485a0b659055 | chunk: 463efc561f8a5355 | strength: constitutional
obligated(president_of_the_republic, none, request_delegation_from_congress).

% atom_id: ae27c0ae3b888847 | chunk: 49671474f32796f7 | strength: constitutional
permitted(individual, none, acquire_ownership_of_land) :-
    land_area(n250_square_meters),
    possession_duration(five_years),
    continuous_possession(true),
    opposition(false),
    usage(residential).

% atom_id: 9ff107e0ac17b758 | chunk: 49ca4eaf13f641b5 | strength: constitutional
obligated(state, public, promote_tourism).

% atom_id: cf5ae14f9d504c33 | chunk: 49ca4eaf13f641b5 | strength: constitutional
obligated(state, public, encourage_tourism_development).

% atom_id: d2bfc97e1c48330c | chunk: 4a77c088f02e57d8 | strength: constitutional
prohibited(state, person, take_measures_against_people) :-
    state_of_siege_declaration_reason(art137_i).

% atom_id: 96a4eaed92715f37 | chunk: 4aa6018f206b9e13 | strength: constitutional
prohibited(authority, rural_small_property, penhor_rural_property_for_productive_debts) :-
    property_type(small_rural),
    work_by_family(true).

% atom_id: ecf75b8f37b5e41b | chunk: 4aa6018f206b9e13 | strength: constitutional
permitted(state, rural_small_property_owner, finance_rural_development) :-
    property_type(small_rural),
    work_by_family(true).

% atom_id: b6e9ce5d12207225 | chunk: 4b43656c1992d106 | strength: constitutional
obligated(ministry_of_finance, public, exercise_customs_control_on_foreign_trade).

% atom_id: 0a831b752051abcd | chunk: 4bd8f19861027ecd | strength: constitutional
permitted(legislature, none, establish_special_tax_criteria).

% atom_id: e0ef35994485b1b4 | chunk: 4d1f7247d1650712 | strength: constitutional
prohibited(authority, brasilian_naturalized_citizen, extradite_individual) :-
    crime_type(common_crime),
    time_of_naturalization(time_of_crime).

% atom_id: 28d68501c379edb0 | chunk: 4d1f7247d1650712 | strength: constitutional
prohibited(authority, brasilian_naturalized_citizen, extradite_individual) :-
    crime_type(illicit_drug_trafficking).

% atom_id: 6e84451583ed2688 | chunk: 4f121c1dfc93b934 | strength: constitutional
obligated(citizen, none, perform_mandatory_military_service).

% atom_id: a9559730b33589fc | chunk: 501bea28aae81ff5 | strength: constitutional
obligated(state, prisoner_mother, ensure_conditions_for_breastfeeding).

% atom_id: 71bbc65575909d58 | chunk: 503a5a03ee66c771 | strength: constitutional
permitted(non_state_actors, land, acquire_property_right) :-
    ownership_duration(five_years),
    opposition(none),
    land_area(fifty_hectares),
    zone_type(rural),
    productivity(true).

% atom_id: 601a12b40621cf80 | chunk: 503f3217d2c6f89b | strength: constitutional
obligated(state, public, allocate_resources_for_basic_education_and_teacher_salary).

% atom_id: a9e5621ae508393b | chunk: 503f3217d2c6f89b | strength: constitutional
obligated(municipality, public, allocate_resources_for_basic_education_and_teacher_salary).

% atom_id: 19642a42bf6a4b8b | chunk: 536f7f1486111c1a | strength: constitutional
permitted(president_of_the_republic, none, request_authorization_to_declare_state_of_siege) :-
    situation(cases_defined_by_law).

% atom_id: ae1467bb89667851 | chunk: 5489dcc1e481ddf4 | strength: constitutional
obligated(state, public, provide_public_services).

% atom_id: ef1d069d875d9e11 | chunk: 54b831600011bbaa | strength: constitutional
obligated(judiciary_authority, labor_dispute_cases, exercise_jurisdiction_uniquely).

% atom_id: e5b551d2b1e9c4a4 | chunk: 553819c8459e2ba6 | strength: constitutional
obligated(authority, individual, process_only_through_competent_authority).

% atom_id: 31469abcb8e011f5 | chunk: 5558da52c273fbeb | strength: constitutional
obligated(state, public_finance, set_legal_limit_on_judicial_payments) :-
    year(X_0), X_0 <= 2026.

% atom_id: bc7e61ef389743a7 | chunk: 5558da52c273fbeb | strength: constitutional
obligated(state, public_finance, allocate_budget_for_social_programs_and_security) :-
    year(X_0), X_0 >= 2017.

% atom_id: 4b1dd580ce158f56 | chunk: 561de608591f627f | strength: constitutional
obligated(armed_forces, country, defend_the_homeland).

% atom_id: 2c5df7e4924ad34d | chunk: 561de608591f627f | strength: constitutional
obligated(armed_forces, state_institutions, guarantee_constitutional_powers).

% atom_id: 32e27de666a7a2cc | chunk: 561de608591f627f | strength: constitutional
obligated(armed_forces, country, maintain_law_and_order) :-
    initiative_source(constitutional_power).

% atom_id: e14d6bd32f4ff320 | chunk: 57d989518c2066ba | strength: constitutional
prohibited(state, none, designate_cases_or_persons_in_budget_allocations).

% atom_id: 64c65c464662eec3 | chunk: 582ebcc9bfb9219f | strength: constitutional
obligated(state, environment, defend_environmental_balance).

% atom_id: 5a08bab6d0e1c052 | chunk: 582ebcc9bfb9219f | strength: constitutional
obligated(collective, environment, preserve_environment_for_future_generations).

% atom_id: 67d05c88b36e3d1e | chunk: 591e4bed11673878 | strength: constitutional
obligated(state, public, exercise_integrated_administrative_competence_ibpt).

% atom_id: 8d5ebe48adc976ab | chunk: 591e4bed11673878 | strength: constitutional
obligated(municipality, public, exercise_integrated_administrative_competence_ibpt).

% atom_id: 188d82b223e7d891 | chunk: 592ba1193d6b7eec | strength: constitutional
prohibited(deputy_or_senator, none, hold_office).

% atom_id: 8a52346f1f60de4a | chunk: 5a2fc699e5cc873f | strength: constitutional
obligated(collective, humanity, cooperate_for_human_progress).

% atom_id: 5f334cc3cbc20041 | chunk: 5a8065c7e5fc1ef2 | strength: constitutional
prohibited(municipality, public, establish_tax_differences_based_on_origin_or_destination).

% atom_id: cf677e225ca74dfa | chunk: 5a8065c7e5fc1ef2 | strength: constitutional
prohibited(state, public, establish_tax_differences_based_on_origin_or_destination).

% atom_id: 5f1bf760f9c2cab0 | chunk: 5a8065c7e5fc1ef2 | strength: constitutional
prohibited(distrito_federal, public, establish_tax_differences_based_on_origin_or_destination).

% atom_id: c1daca9a81d15ad6 | chunk: 5af93f481d8a73eb | strength: constitutional
obligated(state, public, organize_justice_system).

% atom_id: 4634816b5f6126e2 | chunk: 5b36c1a0e884bb2b | strength: constitutional
obligated(state, public, regulate_fuel_sales_and_resales).

% atom_id: fb259ef60bc9f92d | chunk: 5bdff3485924e175 | strength: constitutional
obligated(authority, none, process_and_judge_military_crimes).

% atom_id: 767df452c732fe35 | chunk: 5c4c2722c4256309 | strength: constitutional
obligated(tribunal, law_or_normative_act, declare_unconstitutionality) :-
    vote_count(majority_absolute).

% atom_id: a1c4226ab4b6e8e8 | chunk: 5d2244571564a558 | strength: constitutional
obligated(universities, none, adhere_to_principle_of_indissociability).

% atom_id: 91debd7deea08c99 | chunk: 5dc2f119b11c63b3 | strength: constitutional
permitted(state, public_finance, link_revenues_to_pay_debts_or_provide_guarantees).

% atom_id: c955b450b9542a89 | chunk: 5de7462093759b0f | strength: constitutional
obligated(state, public, ensure_information_access).

% atom_id: 52698e96630f0075 | chunk: 5de7462093759b0f | strength: constitutional
permitted(journalist, source, protect_source_confidentiality) :-
    necessity(professional_exercise).

% atom_id: 85da36c9289c34d1 | chunk: 5e3261907452c86c | strength: constitutional
obligated(state, public, incentivize_internal_market_development).

% atom_id: 7083c3818114fd1d | chunk: 5eb9431f9e26c241 | strength: constitutional
obligated(owner, property, fulfill_social_function_of_property).

% atom_id: ba9dc6fe74b93d9f | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(member_of_chamber_of_deputies, none, initiate_complementary_laws).

% atom_id: d04a80149c0b6712 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(member_of_chamber_of_deputies, none, initiate_ordinary_laws).

% atom_id: 8c9e8bc148c12f46 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(committee_of_chamber_of_deputies, none, initiate_complementary_laws).

% atom_id: c6c93704299fd5bc | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(committee_of_chamber_of_deputies, none, initiate_ordinary_laws).

% atom_id: e42fbeb3e10e38b1 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(senate_member, none, initiate_complementary_laws).

% atom_id: 331be7664a06243d | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(senate_member, none, initiate_ordinary_laws).

% atom_id: c26a8bd462a5e87c | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(national_congress, none, initiate_complementary_laws).

% atom_id: 63e1a0ba3713c464 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(national_congress, none, initiate_ordinary_laws).

% atom_id: 12e9df99111d25b9 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(president_of_the_republic, none, initiate_complementary_laws).

% atom_id: 180687e1776370e8 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(president_of_the_republic, none, initiate_ordinary_laws).

% atom_id: 369abae862bcf534 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(supreme_court_of_brazil, none, initiate_complementary_laws).

% atom_id: e75bde02d50cbf4c | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(supreme_court_of_brazil, none, initiate_ordinary_laws).

% atom_id: 548f8dc53b9b21ec | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(superior_courts, none, initiate_complementary_laws).

% atom_id: 1885fb6df172c8be | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(superior_courts, none, initiate_ordinary_laws).

% atom_id: 45c955a235995827 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(procurator_general_of_the_republic, none, initiate_complementary_laws).

% atom_id: 6b53508e4c335059 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(procurator_general_of_the_republic, none, initiate_ordinary_laws).

% atom_id: 8651b55b88937d88 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(citizen, none, initiate_complementary_laws).

% atom_id: 20c2f5c24b1877c8 | chunk: 5f8aa5d4c52fea48 | strength: constitutional
permitted(citizen, none, initiate_ordinary_laws).

% atom_id: ba59d8d8952c6371 | chunk: 5fc7bb5a4e38fbf4 | strength: constitutional
prohibited(collective, public_finance, increase_budgeted_expenditure).

% atom_id: 456d525a52095a15 | chunk: 5fed8a1bf068e11e | strength: constitutional
obligated(authority, individual, issue_writing_order_for_arrest) :-
    type_of_crime(non_military),
    flagrante_delito(false).

% atom_id: 89b9cdd63f5626a0 | chunk: 5fed8a1bf068e11e | strength: constitutional
prohibited(authority, individual, arrest_without_order_or_flagrante_delito) :-
    type_of_crime(non_military).

% atom_id: beaaa3b21958a371 | chunk: 5fed8a1bf068e11e | strength: constitutional
obligated(authority, individual, arrest_in_flagrante_delito) :-
    type_of_crime(non_military).

% atom_id: 60f6c1f9666d916b | chunk: 5fed8a1bf068e11e | strength: constitutional
obligated(authority, individual, arrest_in_military_cases) :-
    type_of_crime(military).

% atom_id: 458f0188ca8aa818 | chunk: 60c6507f09144ea6 | strength: constitutional
obligated(congressional_bureau, none, appoint_committee_to_monitor_emergency_measures) :-
    emergency_state(defense_or_siege).

% atom_id: 1b66b74f27e2a360 | chunk: 6288b8b6a4cee267 | strength: constitutional
obligated(president_of_the_republic, project_of_law, sanction_project_of_law) :-
    president_approval(true).

% atom_id: ffd78b78eb7d45a3 | chunk: 64176a15f51d0533 | strength: constitutional
obligated(state, public, regulate_public_health_actions_and_services).

% atom_id: 59864e898b9f10a0 | chunk: 64176a15f51d0533 | strength: constitutional
obligated(state, public, fiscalize_public_health_actions_and_services).

% atom_id: 7dbc3e4c009072d3 | chunk: 64176a15f51d0533 | strength: constitutional
obligated(state, public, control_public_health_actions_and_services).

% atom_id: 28af359f3120693c | chunk: 64176a15f51d0533 | strength: constitutional
obligated(state, public, execute_public_health_actions_and_services_directly_or_throu).

% atom_id: 2f25b7907819b8b8 | chunk: 64176a15f51d0533 | strength: constitutional
obligated(state, public, execute_public_health_actions_and_services_through_private_e).

% atom_id: 63cf88e323e97b2c | chunk: 64f502aa50789fd6 | strength: constitutional
obligated(state, consumer, defend_consumer_rights).

% atom_id: 2c90c26232bbbfc6 | chunk: 655c47e82a0acbf4 | strength: constitutional
obligated(state, public, exercise_public_security).

% atom_id: 3017079d667b4f25 | chunk: 658b1d3151333dfa | strength: constitutional
obligated(state, citizen, define_attributes_of_unique_healthcare_system).

% atom_id: 425aa5532a85c267 | chunk: 65b984e3521b767b | strength: constitutional
obligated(state, dependent_heir, provide_assistance_to_carente_dependents) :-
    crime_type(doloso),
    economic_status(carente).

% atom_id: 96c3d7cc39770466 | chunk: 676b042ae29c1224 | strength: constitutional
obligated(state, public, obey_legal_principles).

% atom_id: 79ad8e04abd5822c | chunk: 68845abb8b7d5384 | strength: constitutional
obligated(authority, individual, release_immediately_from_unlawful_detention).

% atom_id: 4b00065547bfba8f | chunk: 699eee9084f8fb27 | strength: constitutional
permitted(private_entity, none, provide_healthcare_assistance).

% atom_id: b1c8b8a6b22d6816 | chunk: 6a00369caa02b1ec | strength: constitutional
permitted(associative_entities, none, represent_members_judicially_or_extrajudicially) :-
    authorization(express).

% atom_id: 8ff4bbb2b23c6633 | chunk: 6baed9e2527813b3 | strength: constitutional
obligated(authority, tribunal, appoint_public_ministry_members_to_tribunals) :-
    public_ministry_career_years(X_0), X_0 >= 10.

% atom_id: 58209ad3b76e8f46 | chunk: 6baed9e2527813b3 | strength: constitutional
obligated(authority, tribunal, appoint_lawyers_to_tribunals) :-
    lawyer_professional_years(X_0), X_0 >= 10,
    lawyer_reputation(notorio_saber_juridico_e_ilibada).

% atom_id: 4776b88dfa9ea25f | chunk: 6baed9e2527813b3 | strength: constitutional
obligated(representative_organs_of_classes, tribunal, submit_sextuple_list_for_tribunal_appointments).

% atom_id: d7a5b07bd2006a1a | chunk: 6e06a0c138070852 | strength: constitutional
obligated(state, citizen, establish_minimum_curriculum_for_basic_education).

% atom_id: be403ab7dd8aad16 | chunk: 6fafe401a2f2e342 | strength: constitutional
obligated(legislative_power, none, exercise_legislative_power).

% atom_id: 63e546e7d9f5f5cb | chunk: 6fb43120c2b8e95a | strength: constitutional
obligated(state, citizen, guarantee_full_exercise_of_cultural_rights).

% atom_id: c5cb1911e815a5fe | chunk: 6fb43120c2b8e95a | strength: constitutional
obligated(state, citizen, support_access_to_national_cultural_sources).

% atom_id: 06d603d473eb6c5f | chunk: 6fb43120c2b8e95a | strength: constitutional
obligated(state, cultural_manifestations, promote_and_incentivize_cultural_expressions).

% atom_id: 4ef59ed5e320c1bd | chunk: 6fb82c9edcb67725 | strength: constitutional
prohibited(authority, foreigner, grant_extradition_for_political_crime_or_opinion).

% atom_id: e216870b5be9dacb | chunk: 6fc3ff142da1023a | strength: constitutional
obligated(state, public, create_national_learning_service_rural).

% atom_id: 96bfa06aec9f91ff | chunk: 6fda3e75ca615690 | strength: constitutional
obligated(congressional_authority, none, establish_social_communication_council).

% atom_id: e35403c3e35722f8 | chunk: 7068bebc5af426d0 | strength: constitutional
obligated(state, public, guarantee_national_development).

% atom_id: 18350b4832b18c8c | chunk: 70e2966a51e5a02f | strength: constitutional
prohibited(state, educational_institution, apply_principle_of_article_206_iv) :-
    institution_type(official),
    creation_method(state_or_municipal_legislation),
    existence_date(constitution_promulgation_date).

% atom_id: 6f8d77f7b380f662 | chunk: 71f0afd1a9bad4ee | strength: constitutional
obligated(authority, benefit_recipient, observe_benefit_limits) :-
    benefit_type(previdencia_social).

% atom_id: 2dc089ae925bf9f8 | chunk: 727970efda113a38 | strength: constitutional
obligated(president_of_the_republic, public, designate_executor_and_areas_for_special_measures) :-
    state_of_siege_declaration(published).

% atom_id: d603c058d81782c5 | chunk: 72c2adb3b458e6f7 | strength: constitutional
obligated(state, worker, respect_professional_association_rights).

% atom_id: f534045f6c2d54ef | chunk: 733547e4a05ab7d4 | strength: constitutional
permitted(worker, none, decide_on_strike_opportunity).

% atom_id: 7c67915a5640ed3e | chunk: 733547e4a05ab7d4 | strength: constitutional
permitted(worker, none, defend_interests_through_strike).

% atom_id: 5ca53aec524db8ec | chunk: 74911adc43107e7a | strength: constitutional
obligated(state, public, finance_unemployment_insurance_program).

% atom_id: a401dfc7b4ebaa14 | chunk: 74911adc43107e7a | strength: constitutional
obligated(state, public, finance_social_security_actions).

% atom_id: fb28728495c3c10b | chunk: 74911adc43107e7a | strength: constitutional
obligated(state, public, finance_abono_salary_bonus).

% atom_id: fac9f50ca873898e | chunk: 75e2bab11f436eb3 | strength: constitutional
prohibited(employer, worker, discriminate_in_salary_or_position) :-
    reason(sex_age_race_marital_status).

% atom_id: 66db3230626bd0ee | chunk: 77420c1aeca9932d | strength: constitutional
obligated(state, author, grant_exclusive_rights_to_works).

% atom_id: 72afb84163f8403a | chunk: 77c5d92b135a6dfa | strength: constitutional
obligated(state, citizen, foster_sports_practices).

% atom_id: a97de5a9f04be61f | chunk: 782fd1f28b85c274 | strength: constitutional
obligated(state, public, promote_scientific_development).

% atom_id: 737ffe8eb1fa7da6 | chunk: 782fd1f28b85c274 | strength: constitutional
obligated(state, public, encourage_research).

% atom_id: 481f536c3eb322e1 | chunk: 782fd1f28b85c274 | strength: constitutional
obligated(state, public, promote_scientific_and_technological_capacity_building).

% atom_id: 6e350d493a6c6cfb | chunk: 782fd1f28b85c274 | strength: constitutional
obligated(state, public, promote_innovation).

% atom_id: ecbf9e234018798c | chunk: 78ac34501a6bfc89 | strength: constitutional
prohibited(state, public_funds, retain_or_restrict_delivery_and_use_of_resources).

% atom_id: 129fe9cd2d7886fe | chunk: 79ac56f4854d182c | strength: constitutional
prohibited(authority, individual, consider_guilty_before_final_judgment).

% atom_id: de4d7454ae22299a | chunk: 7a204f29159ff304 | strength: constitutional
prohibited(state, public, restrict_publicity_of_procedural_acts) :-
    interest(defesa_da_intimidade),
    interest(interesse_social).

% atom_id: a335c96f8ca79a3a | chunk: 7a968c33ed125f88 | strength: constitutional
obligated(union, mineral_resources, own_mineral_rights).

% atom_id: af3785fedbf11baf | chunk: 7a968c33ed125f88 | strength: constitutional
permitted(union, mineral_resources, grant_exploration_rights).

% atom_id: e62a982ead4c81e9 | chunk: 7a968c33ed125f88 | strength: constitutional
obligated(concessionaire, mineral_production, own_product_of_exploration).

% atom_id: 0e4f41b1c52d1d47 | chunk: 7ada64270c67e018 | strength: constitutional
obligated(executive_power, none, exercise_executive_power).

% atom_id: 586d0e1474809bf4 | chunk: 7c2eff379d5837d2 | strength: constitutional
permitted(private_individual, none, exercise_notarial_and_registration_services) :-
    delegation_status(from_state_authority).

% atom_id: d7000368f55ea3cf | chunk: 7d82ca6c1ebd2ea5 | strength: constitutional
prohibited(state, citizen, apply_retroactive_penal_law).

% atom_id: bb975973d2e9a403 | chunk: 7e12b4fc097d45b6 | strength: constitutional
prohibited(authority, none, establish_exceptional_judiciary).

% atom_id: 812e0fd211fd545e | chunk: 7e552c5273b86929 | strength: constitutional
obligated(congressional_houses, none, constitute_commissions).

% atom_id: 2b7bddf10eb78b02 | chunk: 7fe956fc6a6c29b8 | strength: constitutional
permitted(supremo_tribunal_federal, none, approve_syllogism_with_effect_vinculante) :-
    decision_threshold(two_thirds_of_members),
    repeated_decisions(X_1), X_1 >= 1.

% atom_id: 6e6f2c17d8d577e9 | chunk: 7fe956fc6a6c29b8 | strength: constitutional
obligated(other_judicial_organs_and_public_administration, none, follow_syllogism_effect_vinculante) :-
    syllogism_publication(official_press).

% atom_id: 93353219245f0d92 | chunk: 7fe956fc6a6c29b8 | strength: constitutional
permitted(supremo_tribunal_federal, none, revisit_or_cancel_syllogism) :-
    legal_procedure(established_by_law).

% atom_id: 59bb4f5fc7783104 | chunk: 80bfc55d1c45b0a1 | strength: constitutional
obligated(family, child, ensure_child_rights).

% atom_id: d0920df0fe1011aa | chunk: 80bfc55d1c45b0a1 | strength: constitutional
obligated(society, child, ensure_child_rights).

% atom_id: bb489e437122af0e | chunk: 80bfc55d1c45b0a1 | strength: constitutional
obligated(state, child, ensure_child_rights).

% atom_id: a5576aed44fad50f | chunk: 810f07ee47763ab6 | strength: constitutional
obligated(state, public, legislate_transport_ordering).

% atom_id: 9681921fe20ce5a7 | chunk: 810f07ee47763ab6 | strength: constitutional
obligated(state, public, respect_reciprocity_principle_international_transport).

% atom_id: 7b4bd29d2237b196 | chunk: 812819375155bf76 | strength: constitutional
obligated(state, citizen, provide_free_legal_assistance) :-
    income(minimum_wage).

% atom_id: a00dbb243ea8fca0 | chunk: 840cbea838688a31 | strength: constitutional
obligated(municipality, public, authorize_parcelment_funding) :-
    date(X_0), X_0 <= 2026.

% atom_id: f8c2f53b78eac461 | chunk: 840cbea838688a31 | strength: constitutional
obligated(municipality, public, formalize_parcelment) :-
    date(X_0), X_0 <= 2026,
    authorization_status(approved).

% atom_id: 4bceecaf539419f1 | chunk: 86e7d93715593be7 | strength: constitutional
prohibited(president_and_vice_president, none, absent_from_country_without_congress_license) :-
    duration_of_absence(X_0), X_0 > 15.

% atom_id: 7462fb91282a8efb | chunk: 873d6c1b4a96a217 | strength: constitutional
permitted(union, none, institute_compulsory_loans) :-
    law_type(complementary).

% atom_id: a51c8376afa0f411 | chunk: 87fe2d6852486b5e | strength: constitutional
obligated(state, inventor, grant_patent_privilege).

% atom_id: 950f462404989ad6 | chunk: 87fe2d6852486b5e | strength: constitutional
obligated(state, industrial_creator, protect_industrial_creativity).

% atom_id: cffe85a11f9aa07b | chunk: 87fe2d6852486b5e | strength: constitutional
obligated(state, brand_owner, protect_brand_property).

% atom_id: c2f50b9252f8c935 | chunk: 87fe2d6852486b5e | strength: constitutional
obligated(state, company_name_holder, protect_company_names).

% atom_id: 26e6bec100815f7e | chunk: 87fe2d6852486b5e | strength: constitutional
obligated(state, distinctive_sign_holder, protect_distinctive_signs).

% atom_id: 5aadc1c6507b30a3 | chunk: 888c0e522daa3c06 | strength: constitutional
obligated(legislature, public, create_and_extinguish_ministries_and_organs).

% atom_id: cd37fd6b6bde603b | chunk: 8e981a25ab5903cb | strength: constitutional
obligated(state, organs_of_legislative_and_judicial_powers_public_ministry_de, deliver_budgetary_allocations_by_the_20th_day_of_each_month).

% atom_id: 6a854e146587d1cd | chunk: 8f20aa2097c4047f | strength: constitutional
obligated(authority, detainee, identify_responsible_authorities).

% atom_id: f36ba405b714408c | chunk: 8f447b3e1cf1dc82 | strength: constitutional
permitted(union, none, coordinate_actions_in_geoeconomic_complex).

% atom_id: 6399e0797b7f910f | chunk: 8f8cf5eac9cbe0c6 | strength: constitutional
permitted(citizen, none, propose_popular_action) :-
    act_harm(public_patrimony),
    act_harm(administrative_morality),
    act_harm(environment),
    act_harm(historical_cultural_patrimony).

% atom_id: 5ba688994aa06bf7 | chunk: 8f8cf5eac9cbe0c6 | strength: constitutional
permitted(court, citizen, exempt_from_costs) :-
    good_faith(true).

% atom_id: 77a1a71644903544 | chunk: 8ffe71bf7fd10939 | strength: constitutional
permitted(union, none, constitute_funds_for_pension_payment).

% atom_id: 3c668c84e5ec84f3 | chunk: 8ffe71bf7fd10939 | strength: constitutional
permitted(state, none, constitute_funds_for_pension_payment).

% atom_id: 240cc10e41a199c1 | chunk: 8ffe71bf7fd10939 | strength: constitutional
permitted(district_federal, none, constitute_funds_for_pension_payment).

% atom_id: f79a7edf96b97134 | chunk: 8ffe71bf7fd10939 | strength: constitutional
permitted(municipality, none, constitute_funds_for_pension_payment).

% atom_id: d582fdc74f4b58a9 | chunk: 9036fe12aae251d0 | strength: constitutional
obligated(state, public, constitute_judicial_section).

% atom_id: 89fcbf63d4b42288 | chunk: 9133350083529518 | strength: constitutional
obligated(authority, none, regulate_foreign_land_acquisition).

% atom_id: 65db5ca401124137 | chunk: 9133350083529518 | strength: constitutional
obligated(authority, none, establish_congressional_authorization_cases).

% atom_id: 307a406d2c2cf970 | chunk: 931cad5bf139a4d0 | strength: constitutional
obligated(congress_national, union_administration_entities, exercise_external_control).

% atom_id: d9370ca43c412848 | chunk: 931cad5bf139a4d0 | strength: constitutional
obligated(each_power_internal_system, union_administration_entities, exercise_internal_control).

% atom_id: 3705474392e680da | chunk: 9a61c96973bee574 | strength: constitutional
prohibited(union, contributor, levy_tax_without_guarantees).

% atom_id: ed940852f5ef71b4 | chunk: 9a61c96973bee574 | strength: constitutional
prohibited(state, contributor, levy_tax_without_guarantees).

% atom_id: 181e69b2552c6b24 | chunk: 9a61c96973bee574 | strength: constitutional
prohibited(district_of_federal_politics, contributor, levy_tax_without_guarantees).

% atom_id: a7dce96bf454c5b6 | chunk: 9a61c96973bee574 | strength: constitutional
prohibited(municipality, contributor, levy_tax_without_guarantees).

% atom_id: 6c7dec112887ec55 | chunk: 9a896bad8acac514 | strength: constitutional
obligated(state, person, provide_religious_assistance_in_entities) :-
    entity_type(civil_or_military_internment_entity).

% atom_id: 80bad28248a29571 | chunk: 9a940f52a84e0bfb | strength: constitutional
obligated(union, public, organize_education_systems).

% atom_id: 1383eb5730949bc3 | chunk: 9a940f52a84e0bfb | strength: constitutional
obligated(state, public, organize_education_systems).

% atom_id: 79b60cc0f948506a | chunk: 9a940f52a84e0bfb | strength: constitutional
obligated(district_federal, public, organize_education_systems).

% atom_id: f56f29254d4d41f8 | chunk: 9a940f52a84e0bfb | strength: constitutional
obligated(municipality, public, organize_education_systems).

% atom_id: dc1cc63bcb49a884 | chunk: 9aa054826617f5cf | strength: constitutional
prohibited(state, child, impose_penal_sanctions) :-
    age(X_0), X_0 < 18.

% atom_id: 10452b3e6fa3f1c8 | chunk: 9acdf70f92bf5bec | strength: constitutional
obligated(authority, citizen, review_legal_infringement).

% atom_id: 28f9a143808ff03d | chunk: 9b0262c5366929f8 | strength: constitutional
obligated(state, citizen, implement_healthcare_reforms) :-
    year(2027).

% atom_id: e47d828df07a0d01 | chunk: 9b0aaebf4ffa58cf | strength: constitutional
obligated(collective, society, build_free_just_and_solidary_society).

% atom_id: 6ec10d0fdb3d02e7 | chunk: 9c86ef6c93db67d4 | strength: constitutional
obligated(state, public, implement_measures_during_national_emergency) :-
    emergency_status(national_calamity).

% atom_id: d78714ae93062a1b | chunk: 9e0a70ee452b96b2 | strength: constitutional
obligated(union, public, create_institutions).

% atom_id: dd9129eb5a704f6c | chunk: 9e0a70ee452b96b2 | strength: constitutional
obligated(state, public, create_institutions).

% atom_id: 900ce95f399d1e7d | chunk: 9e189ea2d72e5e18 | strength: constitutional
obligated(advocacia_geral_da_uniao, uniao, represent_union_judicially_and_extrajudicially).

% atom_id: 6bedd06fcce6594e | chunk: 9e189ea2d72e5e18 | strength: constitutional
obligated(advocacia_geral_da_uniao, executive_power, provide_legal_advice_and_assistance).

% atom_id: 08375422a27a2452 | chunk: 9ebe10c5ff84f005 | strength: constitutional
obligated(union, rural_property_owner, desappropriate_for_social_interest) :-
    property_function(not_complying_with_social_function).

% atom_id: 605f0f5661993a1e | chunk: 9ebe10c5ff84f005 | strength: constitutional
obligated(union, rural_property_owner, provide_just_compensation) :-
    property_function(not_complying_with_social_function).

% atom_id: 4d4c9cf9e149da47 | chunk: 9ebe10c5ff84f005 | strength: constitutional
obligated(legislature, resettlement_instruments, define_usage_of_resettlement_instruments).

% atom_id: ab6438c401c3208a | chunk: 9ed0645ab13bc659 | strength: constitutional
obligated(state, none, plan_and_execute_agricultural_policy).

% atom_id: 7601d9d6a51386db | chunk: 9ed5d251d52fc081 | strength: constitutional
obligated(state, municipality, convalidate_municipal_creation_acts) :-
    publication_date(X_0), X_0 <= 31,
    legislation_at_time_of_creation(state_legislation).

% atom_id: 886b00a7e088925d | chunk: 9ff03317448728ce | strength: constitutional
obligated(legislative_executive_judiciary, public, maintain_integrated_internal_control_system).

% atom_id: c00955e01743049f | chunk: a0a32fdeb1a4d6d9 | strength: constitutional
permitted(executive_power_federal, none, adopt_simplified_contracting_processes) :-
    calamity_state(true).

% atom_id: 3c7e8651d422b842 | chunk: a0a32fdeb1a4d6d9 | strength: constitutional
obligated(executive_power_federal, none, ensure_competition_and_equality_conditions) :-
    calamity_state(true).

% atom_id: e46b57a486d7cc36 | chunk: a0a32fdeb1a4d6d9 | strength: constitutional
prohibited(executive_power_federal, none, observe_article_169_section_1) :-
    calamity_state(true),
    contract_type(temporary_and_emergency_contracting).

% atom_id: 73e74e942f386c76 | chunk: a0a32fdeb1a4d6d9 | strength: constitutional
obligated(executive_power_federal, none, limit_dispensation_to_situations_in_article_37_inciso_ix) :-
    calamity_state(true).

% atom_id: 6d8df1d4fc943c8c | chunk: a0a32fdeb1a4d6d9 | strength: constitutional
obligated(competent_authorities, none, exercise_control_over_contractions) :-
    calamity_state(true).

% atom_id: f6453e42dee54439 | chunk: a0baf6d2bd1f2f18 | strength: constitutional
obligated(house_member, none, vote_majority_presence) :-
    constitutional_disposition(false).

% atom_id: 5767d260a1ee8322 | chunk: a2d9903980e054ef | strength: constitutional
prohibited(state, association_or_cooperative, interfere_in_functioning).

% atom_id: 6335aecab81e59eb | chunk: a94efe2aab2ebd82 | strength: constitutional
obligated(broadcast_provider, public, adhere_to_programming_principles).

% atom_id: 86c86ae2572febf7 | chunk: aaa9f7b701601193 | strength: constitutional
obligated(authority, supremo_tribunal_federal, compose_of_eleven_ministers).

% atom_id: 584f2e21092f9225 | chunk: aaa9f7b701601193 | strength: constitutional
obligated(authority, ministers_of_supremo_tribunal_federal, be_selected_from_citizens_with_age_between_35_and_70).

% atom_id: 4aeb9e1fc14d746d | chunk: aaa9f7b701601193 | strength: constitutional
obligated(authority, ministers_of_supremo_tribunal_federal, have_notable_legal_knowledge_and_unblemished_reputation).

% atom_id: 29e5c2f02211e5f8 | chunk: ac393016841a0619 | strength: constitutional
obligated(president_of_the_republic, tribunal_judges, nominate_tribunal_judges) :-
    judge_age(X_0), X_0 >= 30,
    judge_age(X_1), X_1 <= 70.

% atom_id: 799b194b0d077d02 | chunk: ac393016841a0619 | strength: constitutional
obligated(president_of_the_republic, tribunal_judges, recruit_tribunal_judges_locally) :-
    feasibility(possible).

% atom_id: 84edd7c2b822e573 | chunk: adc716241a3c172d | strength: constitutional
permitted(individual, none, exercise_profession) :-
    professional_qualifications(law_established).

% atom_id: 9dc747ae8fe759f1 | chunk: ae4bffab2af83f9a | strength: constitutional
obligated(congressional_body, state, exercise_external_control).

% atom_id: bb62385308fa8c57 | chunk: ae4bffab2af83f9a | strength: constitutional
obligated(court_of_audits, state, assist_in_external_control).

% atom_id: d482e47dc33a9dde | chunk: aef23c2d2a9173a1 | strength: constitutional
obligated(state, public_finance, allocate_percentage_of_revenue_to_unspecified_purposes) :-
    date(X_0), X_0 <= 31.

% atom_id: dd3289dbfad097c2 | chunk: af321192e4d665d8 | strength: constitutional
permitted(president_of_the_republic, public, declare_defense_state) :-
    threat_level(grave_and_imminent_institutional_instability),
    impact(calamities_of_large_proportions_nature).

% atom_id: 3c1f5bef12a0917e | chunk: afc48a1f61139800 | strength: constitutional
obligated(state, citizen, exercise_sovereignty_through_universal_suffrage).

% atom_id: 845325cebe5635c1 | chunk: b0721ec7a66ea5f2 | strength: constitutional
permitted(chamber_of_deputies_or_senate_committee, minister_of_state_or_head_of_presidential_office_or_cgces_ch, convocate_for_information_session).

% atom_id: 1d2ffaece34e1a89 | chunk: b0e218c7f772592b | strength: constitutional
prohibited(collective, state, armed_action_against_constitutional_order).

% atom_id: 1edddff033dd6f1f | chunk: b2d6cfd4dc3e862f | strength: constitutional
obligated(state, citizen, ensure_freedom_of_conscience_and_belief).

% atom_id: 62f7ab5d2fbd7ba3 | chunk: b2d6cfd4dc3e862f | strength: constitutional
obligated(state, religious_institution, protect_religious_sites_and_practices).

% atom_id: 499ef3e29fb3d52f | chunk: b59c4d7bb12e8e83 | strength: constitutional
obligated(authority, jury_institution, organize_jury_system).

% atom_id: 2bfda352dcac6854 | chunk: b7a010d73ae661a2 | strength: constitutional
obligated(congress_national, none, legislate_on_unions_matters) :-
    sanction_required(false).

% atom_id: 5607d9b4dfd59859 | chunk: b7a010d73ae661a2 | strength: constitutional
obligated(president_republic, none, sanction_legislation_congress_national) :-
    exception_articles(n49_51_52).

% atom_id: f9b9740b919dfca8 | chunk: b94058933a3a4153 | strength: constitutional
obligated(authority, individual, prosecute_racism_crime).

% atom_id: 242fd97ffb9dec29 | chunk: bafea39f2c68342f | strength: constitutional
obligated(employer, worker, ensure_election_of_worker_representative) :-
    number_of_employees(X_0), X_0 >= 200.

% atom_id: d4a2f724c21eae1e | chunk: bba3b8bedf17208e | strength: constitutional
prohibited(union, none, apply_financial_restrictions) :-
    calamity_status(public_emergency).

% atom_id: f45a6b78c09af506 | chunk: bbfacec0c4468d89 | strength: constitutional
obligated(state, poor_person, provide_free_services_and_benefits) :-
    poverty_status(reconhecido).

% atom_id: 5f84ec0b91a4f908 | chunk: bed00fe40b505c21 | strength: constitutional
obligated(state, municipality, liquidate_preexisting_contributions_debts) :-
    debt_date(X_0), X_0 <= 1988,
    request_parcelment(true),
    start_payment_within(X_2), X_2 <= 180.

% atom_id: c1930a8695e9cb99 | chunk: bed00fe40b505c21 | strength: constitutional
prohibited(state, municipality, apply_interests_and_fines_on_parcelment_debts) :-
    debt_date(X_0), X_0 <= 1988,
    request_parcelment(true).

% atom_id: af999f974bf8cffb | chunk: bed00fe40b505c21 | strength: constitutional
permitted(municipality, state, request_parcelment_of_contributions_debts) :-
    debt_date(X_0), X_0 <= 1988.

% atom_id: 483b26f7faeeab45 | chunk: bed00fe40b505c21 | strength: constitutional
obligated(municipality, state, initiate_payment_of_contributions_debts_within_180_days) :-
    debt_date(X_0), X_0 <= 1988,
    request_parcelment(true).

% atom_id: ac49a6dcc4653b7f | chunk: bed00fe40b505c21 | strength: constitutional
permitted(municipality, state, pay_contributions_debts_in_120_monthly_installments) :-
    debt_date(X_0), X_0 <= 1988,
    request_parcelment(true).

% atom_id: 01e098447dc81b5c | chunk: bfcef4fe7657daef | strength: constitutional
permitted(legislature, none, create_labor_courts).

% atom_id: 20c8f16b4f5145a7 | chunk: bfcef4fe7657daef | strength: constitutional
permitted(legislature, none, assign_labor_jurisdiction_to_regular_judges) :-
    comarca(labor_courts_jurisdiction).

% atom_id: 6a07d34538d9f36c | chunk: c07fc3d59b88718d | strength: constitutional
obligated(state, legal_system, ensure_advocate_necessity_in_justice_administration).

% atom_id: 6781f4ea39254486 | chunk: c07fc3d59b88718d | strength: constitutional
prohibited(authority, advocate, violate_advocate_rights).

% atom_id: c7c574472d6b9443 | chunk: c0e47312bb39d1aa | strength: constitutional
obligated(state, citizen, ensure_legal_equality).

% atom_id: c65410d822d3df8e | chunk: c0e47312bb39d1aa | strength: constitutional
obligated(state, citizen, protect_right_to_life).

% atom_id: b89e771241022fa0 | chunk: c0e47312bb39d1aa | strength: constitutional
obligated(state, citizen, protect_right_to_freedom).

% atom_id: 155b427640c5cfd9 | chunk: c0e47312bb39d1aa | strength: constitutional
obligated(state, citizen, protect_right_to_equality).

% atom_id: cfe798868c2ac82e | chunk: c0e47312bb39d1aa | strength: constitutional
obligated(state, citizen, protect_right_to_security).

% atom_id: 237964ae014e8333 | chunk: c0e47312bb39d1aa | strength: constitutional
obligated(state, citizen, protect_right_to_property).

% atom_id: 3654604fd85503e4 | chunk: c14c1314d5308cc7 | strength: constitutional
obligated(authority, individual, ensure_right_of_reply).

% atom_id: f3e81b243bd9ac7f | chunk: c2513ec06010cf2f | strength: constitutional
obligated(authority, project_of_law, review_project_of_law).

% atom_id: fe4d7b617ca26b4b | chunk: c2513ec06010cf2f | strength: constitutional
obligated(authority, project_of_law, send_to_sancion_or_promulgate) :-
    approval_status(approved).

% atom_id: 19630c0089430e38 | chunk: c2513ec06010cf2f | strength: constitutional
obligated(authority, project_of_law, archive_project_of_law) :-
    approval_status(rejected).

% atom_id: c9ad28ecf529151b | chunk: c2984e5a7a06b2a6 | strength: constitutional
permitted(executive_power, none, enact_legislation_to_address_calamity) :-
    purpose_of_action(addressing_calamity_and_its_consequences),
    duration_of_effect(limited_to_duration_of_calamity).

% atom_id: 993862043652be5f | chunk: c2984e5a7a06b2a6 | strength: constitutional
permitted(executive_power, none, expand_government_action_without_budgetary_limitations) :-
    purpose_of_action(addressing_calamity_and_its_consequences),
    duration_of_effect(limited_to_duration_of_calamity).

% atom_id: c650dded8f6416e3 | chunk: c2984e5a7a06b2a6 | strength: constitutional
permitted(executive_power, none, grant_tax_incentives_without_budgetary_limitations) :-
    purpose_of_action(addressing_calamity_and_its_consequences),
    duration_of_effect(limited_to_duration_of_calamity).

% atom_id: ae00cf941ccab51a | chunk: c2a14aad854916ab | strength: constitutional
obligated(state, public, use_portuguese_as_official_language).

% atom_id: 41c998663195fec4 | chunk: c2fbf384d0782cbe | strength: constitutional
obligated(state, property_owner, expropriate_illegal_property) :-
    illegal_activity(cultivation_of_psychotropic_plants).

% atom_id: 54acbd0826b691cc | chunk: c2fbf384d0782cbe | strength: constitutional
obligated(state, property_owner, expropriate_illegal_property) :-
    illegal_activity(forced_labor).

% atom_id: 6c7d8780783555ab | chunk: c2fbf384d0782cbe | strength: constitutional
obligated(state, property_owner, allocate_property_for_social_programs) :-
    expropriated_property(true).

% atom_id: 8bdcbaa0ada09faf | chunk: c2fbf384d0782cbe | strength: constitutional
prohibited(property_owner, none, claim_indemnity_for_expropriated_property) :-
    expropriation_reason(illegal_activity).

% atom_id: 601919599dd24623 | chunk: c5bd425286e5ef94 | strength: constitutional
obligated(authority, judiciary_power, ensure_autonomy_administrative_and_financial).

% atom_id: 8d208b2b82ef2b2f | chunk: c6543122cfd5dcff | strength: constitutional
obligated(state, cultural_good, protect_cultural_assets).

% atom_id: ac4db9655ba85895 | chunk: c6852491d9d53252 | strength: constitutional
obligated(authority, person, communicate_arrest_to_judge).

% atom_id: c22c50b873875411 | chunk: c6852491d9d53252 | strength: constitutional
obligated(authority, person, communicate_arrest_to_family_or_designee).

% atom_id: fb464a4ff9bbfe79 | chunk: c7583c262098770d | strength: constitutional
obligated(state, public, institute_taxes).

% atom_id: 0623964be091faba | chunk: c7d8167e0568eb0d | strength: constitutional
obligated(state, public, establish_regional_electoral_court).

% atom_id: e502ee93c21c229d | chunk: c988f495940df0d5 | strength: constitutional
prohibited(authority, association, compulsorily_dissolve_association) :-
    judicial_decision(false).

% atom_id: 5f0f585d1f8de589 | chunk: c988f495940df0d5 | strength: constitutional
prohibited(authority, association, suspend_association_activities) :-
    judicial_decision(false).

% atom_id: ddb7d27341e689d9 | chunk: c988f495940df0d5 | strength: constitutional
obligated(judiciary, association, compulsorily_dissolve_association) :-
    judicial_decision(true).

% atom_id: b00340958715875d | chunk: c988f495940df0d5 | strength: constitutional
obligated(judiciary, association, suspend_association_activities) :-
    judicial_decision(true).

% atom_id: 9315ff69aaf9cf41 | chunk: c988f495940df0d5 | strength: constitutional
obligated(judiciary, association, await_final_judgment) :-
    judicial_decision(true),
    final_judgment(false).

% atom_id: ecf2c836ddb284f1 | chunk: cc177fada05d048b | strength: constitutional
obligated(state, public, organize_and_regulate_by_constitution_and_laws).

% atom_id: 03d2b54af910de28 | chunk: ccfef852d97435bc | strength: constitutional
obligated(chamber_of_deputies, president_of_the_republic, submit_to_judgment_common_crimes) :-
    vote_percentage(X_0), X_0 >= 2.

% atom_id: 13157123eaa1b295 | chunk: ccfef852d97435bc | strength: constitutional
obligated(senate, president_of_the_republic, submit_to_judgment_crimes_of_responsibility) :-
    vote_percentage(X_0), X_0 >= 2.

% atom_id: cb0b725c4a316ec3 | chunk: cd374cb5093bfa1d | strength: constitutional
prohibited(president_of_the_republic, none, act_contrary_to_constitution).

% atom_id: 4f813f08cd12a27d | chunk: ce13a56e4e32e33a | strength: constitutional
obligated(state, citizen, ensure_social_security).

% atom_id: e8383c33a9b37691 | chunk: cef65ba5f6f45c94 | strength: constitutional
obligated(authority, inmate, respect_physical_and_moral_integrity).

% atom_id: b654651fe8c26b72 | chunk: cef65dba119ea3fb | strength: constitutional
obligated(state, condemned_person, indemnify_for_judicial_error).

% atom_id: b06d4f48e0dc9fbd | chunk: cef65dba119ea3fb | strength: constitutional
obligated(state, detainee, compensate_for_unauthorized_detention).

% atom_id: 5a1d10b67ff23223 | chunk: cfaac262bba7f577 | strength: constitutional
obligated(authority, citizen, grant_mandado_de_injuncao) :-
    lack_of_regulatory_norm(true),
    inviability_of_exercising_rights(true).

% atom_id: 96aab2566b003acb | chunk: d204402a93d8ad5e | strength: constitutional
obligated(authority, individual, grant_habeas_corpus) :-
    violation_of_rights(true).

% atom_id: c4416284455e53ec | chunk: d33ae5a52b52c540 | strength: constitutional
obligated(state, citizen, promote_and_incentivize_education).

% atom_id: 555a99353af1ac76 | chunk: d33ae5a52b52c540 | strength: constitutional
obligated(family, citizen, promote_and_incentivize_education).

% atom_id: c116b6ee2b562149 | chunk: d33ae5a52b52c540 | strength: constitutional
permitted(society, none, collaborate_in_education_promotion).

% atom_id: 2ea9db0f29fdcb55 | chunk: d3d7bde417a329bd | strength: constitutional
prohibited(state, citizen, define_crime_retroactively).

% atom_id: 6d85d9bc7073ac57 | chunk: d3d7bde417a329bd | strength: constitutional
prohibited(state, citizen, impose_penalty_without_legal_precedence).

% atom_id: 5ead5390c55ccb74 | chunk: d4c8853b1feae561 | strength: constitutional
obligated(legislature, none, organize_and_determine_competence_of_tribunals_judges_and_el).

% atom_id: 62bd8f284a0c9a2f | chunk: d4ceaa734cee156e | strength: constitutional
prohibited(collective, public, discriminate_against_fundamental_rights).

% atom_id: 15289b97f7eaa7bc | chunk: d58588500387e21d | strength: constitutional
obligated(union, public, adopt_extraordinary_fiscal_regime) :-
    state_of_emergency(national).

% atom_id: 382cc32e20bc4717 | chunk: d6029ac232e20d32 | strength: constitutional
obligated(private_entity, public, provide_education) :-
    initiative_type(private).

% atom_id: e6f643097e308698 | chunk: d725a9b143077f32 | strength: constitutional
prohibited(deputy_and_senator, none, perform_prohibited_actions).

% atom_id: 8ff6c075ba67cd86 | chunk: d8bac802c4cedc6a | strength: constitutional
obligated(union, territory, collect_state_taxes) :-
    is_divided_into_municipalities(false).

% atom_id: f782ec48fdab1f00 | chunk: d8bac802c4cedc6a | strength: constitutional
obligated(union, territory, collect_municipal_taxes) :-
    is_divided_into_municipalities(false).

% atom_id: 62d0701364ecd4d7 | chunk: d8bac802c4cedc6a | strength: constitutional
obligated(federal_district, territory, collect_municipal_taxes).

% atom_id: 126965741ef431a4 | chunk: d92294e26345319f | strength: constitutional
obligated(state, citizen, guarantee_social_rights).

% atom_id: d93032b7f25fc31e | chunk: da66044da335439e | strength: constitutional
obligated(union, none, exercise_currency_emission_exclusively).

% atom_id: 0fe63144e437e930 | chunk: db1aa7a627ce8b42 | strength: constitutional
obligated(congress_member, legislation, propose_new_project_same_session) :-
    project_status(rejected),
    proposal_support(majority_absolute).

% atom_id: 661960efd5c5fe70 | chunk: db975c4877e1ccc3 | strength: constitutional
obligated(state, citizen, ensure_dignified_existence).

% atom_id: e40d0bac633704d6 | chunk: db975c4877e1ccc3 | strength: constitutional
obligated(state, citizen, promote_social_justice_principles).

% atom_id: 6f733c45b69be142 | chunk: dc1876d55c5adbc8 | strength: constitutional
obligated(state, citizen, provide_social_assistance).

% atom_id: 275ab496834ae3f6 | chunk: dc59a2ef4725ff25 | strength: constitutional
obligated(state, foreign_investor, regulate_foreign_capital_investment).

% atom_id: d92d83d6622c50f1 | chunk: dc59a2ef4725ff25 | strength: constitutional
obligated(state, foreign_investor, encourage_reinvestment).

% atom_id: c1ec7e4c75e9a477 | chunk: dc59a2ef4725ff25 | strength: constitutional
obligated(state, foreign_investor, regulate_profit_reinvestment).

% atom_id: 36c09d377053b2f2 | chunk: dcb9334de8b64dd9 | strength: constitutional
obligated(authority, detainee, inform_rights).

% atom_id: 5ec384330c44e0e2 | chunk: dcb9334de8b64dd9 | strength: constitutional
obligated(authority, detainee, ensure_family_assistance).

% atom_id: 8debd16953784144 | chunk: dcb9334de8b64dd9 | strength: constitutional
obligated(authority, detainee, ensure_legal_counsel_assistance).

% atom_id: ab06752cb2235acf | chunk: de5816d0f319ed17 | strength: constitutional
permitted(collective, none, propose_constitutional_amendment).

% atom_id: ac5d50c8bfdeccaf | chunk: e0052040b44aadad | strength: constitutional
obligated(state, none, determine_assembly_deputies_number) :-
    deputy_representation_in_chamber(triple),
    current_number_of_deputies(X_1), X_1 >= 36.

% atom_id: 16628c0834b019bd | chunk: e02ab1fb8ada23b2 | strength: constitutional
prohibited(authority, deputy_senator, criminal_or_civil_law_action_against_opinions_words_votes).

% atom_id: aa3449cefc18ac52 | chunk: e04f5fa5ae83b0ce | strength: constitutional
obligated(state, citizen, ensure_free_access_to_services).

% atom_id: 46894d87af59d3e8 | chunk: e05e00eaace2889c | strength: constitutional
prohibited(authority, citizen, cassate_political_rights).

% atom_id: 4ef130cc78e472db | chunk: e0aa064f1d71aaf8 | strength: constitutional
obligated(chamber_of_deputies, none, begin_discussion_and_vote_on_projects).

% atom_id: 739613ab39b71e70 | chunk: e437a494acf5920d | strength: constitutional
obligated(parent, minor_child, assist_create_educate_minor_children).

% atom_id: 597ecb5bae7ee58d | chunk: e437a494acf5920d | strength: constitutional
obligated(major_child, parent, help_support_parents_in_old_age_or_need) :-
    condition(old_age),
    condition(need),
    condition(illness).

% atom_id: ca422d7a556be926 | chunk: e4d6bb56c4458c83 | strength: constitutional
obligated(authority, public_finance, destine_tax_revenue_to_contracting_entity).

% atom_id: 081bf7ca87749b86 | chunk: e5b42c2e123fae22 | strength: constitutional
obligated(union, public, allocate_minimal_percentage_of_tax_revenue_for_education).

% atom_id: 88020f2607bc2166 | chunk: e5b42c2e123fae22 | strength: constitutional
obligated(state, public, allocate_minimal_percentage_of_tax_revenue_for_education).

% atom_id: a225d8f06452dad9 | chunk: e5b42c2e123fae22 | strength: constitutional
obligated(federal_district, public, allocate_minimal_percentage_of_tax_revenue_for_education).

% atom_id: 1986c91320eb2acc | chunk: e5b42c2e123fae22 | strength: constitutional
obligated(municipality, public, allocate_minimal_percentage_of_tax_revenue_for_education).

% atom_id: f9321639d7981baf | chunk: e69b13cc20539e0b | strength: constitutional
obligated(state, public, eradicate_poverty_and_marginalization).

% atom_id: cc704f62e05d13b2 | chunk: e69b13cc20539e0b | strength: constitutional
obligated(state, public, reduce_social_and_regional_inequalities).

% atom_id: 7d757e9528062d89 | chunk: ea2622bfbfd64229 | strength: constitutional
obligated(union, none, institute_social_contributions).

% atom_id: 5872c1743f3aaf9e | chunk: ea26c0cc125355f6 | strength: constitutional
obligated(state, public, provide_education_based_on_principles).

% atom_id: d4367b001002b53d | chunk: ea4e781c08f95d20 | strength: constitutional
obligated(authority, apenado, segregate_prison_population) :-
    nature_of_crime(specific_nature),
    age(X_1), X_1 >= 18.

% atom_id: 4af3d61e3f244fe9 | chunk: eaad78bd7b66715d | strength: constitutional
obligated(state, microenterprise, provide_differential_legal_treatment) :-
    entity_type(microenterprise).

% atom_id: 87ca2b2ec8c710de | chunk: eaad78bd7b66715d | strength: constitutional
obligated(state, small_business, provide_differential_legal_treatment) :-
    entity_type(small_business).

% atom_id: 9c864a1e29eaf2a4 | chunk: eaad78bd7b66715d | strength: constitutional
obligated(state, microenterprise_small_business, simplify_administrative_obligations) :-
    entity_type(microenterprise),
    entity_type(small_business).

% atom_id: 4dc91e10f0ae5727 | chunk: eaad78bd7b66715d | strength: constitutional
obligated(state, microenterprise_small_business, reduce_legal_obligations) :-
    entity_type(microenterprise),
    entity_type(small_business).

% atom_id: 5cf91eef7adc042f | chunk: eaad78bd7b66715d | strength: constitutional
obligated(state, microenterprise_small_business, eliminate_legal_obligations) :-
    entity_type(microenterprise),
    entity_type(small_business).

% atom_id: cdfc95921a7224c8 | chunk: eaad78bd7b66715d | strength: constitutional
obligated(state, microenterprise_small_business, reduce_legal_obligations_through_legislation) :-
    entity_type(microenterprise),
    entity_type(small_business).

% atom_id: b2e77f420bc957b9 | chunk: eaff98b214456fbd | strength: constitutional
permitted(union, none, constitute_integrated_fund).

% atom_id: 29ae6b1bf72a0370 | chunk: ebd0564da4755594 | strength: constitutional
obligated(ministry_of_public_accountability_member, none, comply_with_dispositions) :-
    disposition_pertinence(rights_restrictions_and_investment_form).

% atom_id: df21720aa8e9b55e | chunk: ed9e35c39b842062 | strength: constitutional
obligated(president_of_the_republic, senate_federal, seek_approval_for_governor_appointment) :-
    article_32_effectiveness(false).

% atom_id: c91d528fb16449de | chunk: ed9e35c39b842062 | strength: constitutional
obligated(president_of_the_republic, distrito_federal, appoint_governor_and_vice_governor) :-
    senate_approval(true),
    article_32_effectiveness(false).

% atom_id: 24aac2810198d2c7 | chunk: f0553f060b240f8c | strength: constitutional
obligated(state, public_finance, retain_tax_amount_for_distribution) :-
    tax_reference_rate(from_art_130),
    retention_mechanism(from_art_131_section_1).

% atom_id: 98c9189814bc3979 | chunk: f0b40b21ab61c3b7 | strength: constitutional
obligated(state, public, adapt_infrastructure_for_disabled_access).

% atom_id: fb38fd36be124a08 | chunk: f1c4b5149e025dde | strength: constitutional
obligated(municipality, public, execute_urban_development_policy).

% atom_id: 1a3ca10aac765478 | chunk: f1c4b5149e025dde | strength: constitutional
obligated(municipality, public, guarantee_wellbeing_of_habitants).

% atom_id: abf9d38de7917372 | chunk: f1ce2cf7185b9245 | strength: constitutional
obligated(state, zona_franca_de_manaus, maintain_differential_competitiveness) :-
    date(n2023_05_31),
    legislation_type(tributos_extintos).

% atom_id: ffc3a359bd5cb785 | chunk: f1ce2cf7185b9245 | strength: constitutional
obligated(state, areas_of_free_trade, maintain_differential_competitiveness) :-
    date(n2023_05_31),
    legislation_type(tributos_extintos).

% atom_id: 879f2e93b9018b80 | chunk: f22f7aa828bcb227 | strength: constitutional
prohibited(individual, none, be_compelled_to_associate).

% atom_id: aae7c964f6e29df9 | chunk: f2fbe0057ac0da0a | strength: constitutional
obligated(state, citizen, provide_free_habeas_corpus_actions).

% atom_id: 7f4841adb2b663ef | chunk: f2fbe0057ac0da0a | strength: constitutional
obligated(state, citizen, provide_free_habeas_data_actions).

% atom_id: ddbb46cf3771666c | chunk: f2fbe0057ac0da0a | strength: constitutional
obligated(state, citizen, provide_free_citizenship_exercise_actions) :-
    legal_form(law).

% atom_id: 8c3bac857a8e2029 | chunk: f30ca349d14656df | strength: constitutional
prohibited(municipal_legislature, none, exceed_budget_percentages) :-
    budget_type(tributary_and_transfers),
    year(previous_year).

% atom_id: f3df6d2864f40ebe | chunk: f33e55b8cd02b50f | strength: constitutional
obligated(vice_president, none, replace_president_during_impediment) :-
    president_status(impedimento).

% atom_id: c2fa5164a08a8a74 | chunk: f33e55b8cd02b50f | strength: constitutional
obligated(vice_president, none, succeed_president_in_vacancy) :-
    president_status(vaga).

% atom_id: 6b0d7e5a6c4c10db | chunk: f3a43c8110765681 | strength: constitutional
obligated(authority, current_peace_judges, maintain_rights_and_attributes).

% atom_id: 614e59b8287673f2 | chunk: f3a43c8110765681 | strength: constitutional
obligated(authority, public, schedule_election) :-
    election_type(peace_judges).

% atom_id: 53c7da56c32ff587 | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, take_office_in_congressional_session).

% atom_id: a429c4cf130bfb08 | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, maintain_constitution).

% atom_id: b527d7538d2f3e2d | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, defend_constitution).

% atom_id: a0eb43fd5d63ee7e | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, comply_with_constitution).

% atom_id: 3f3c20f1b7238598 | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, public, observe_laws).

% atom_id: ae4e4648a1906ca5 | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, public, promote_general_welfare_of_brazilian_people).

% atom_id: 2e1151a5d27816c6 | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, sustain_unification_of_brazil).

% atom_id: 7af8bc0ae9e809bd | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, sustain_integrity_of_brazil).

% atom_id: aa8a68f5f7e340c7 | chunk: f3f193118bb59eb0 | strength: constitutional
obligated(president, none, sustain_independence_of_brazil).

% atom_id: a637c6e86f94a259 | chunk: f41f646628969ceb | strength: constitutional
obligated(president_of_the_republic, senate_majority, nominate_conference_members).

% atom_id: 91bed5c79725b2aa | chunk: f45e2fcfd530ee2d | strength: constitutional
prohibited(authority, debtor, enforce_civil_arrest_for_debt).

% atom_id: b60afedead9b228d | chunk: f45e2fcfd530ee2d | strength: constitutional
prohibited(authority, debtor, enforce_civil_arrest_for_debt) :-
    debt_type(alimenticia),
    inadimplemento_voluntario_inescusavel(true).

% atom_id: ed7407764cd9773e | chunk: f45e2fcfd530ee2d | strength: constitutional
prohibited(authority, debtor, enforce_civil_arrest_for_debt) :-
    debt_type(depositario_infiel).

% atom_id: bcbc34f8072022e7 | chunk: f45f38442b6d6170 | strength: constitutional
permitted(collective, none, create_political_parties) :-
    sovereignty_status(respected),
    regime_type(democratic),
    party_system(pluralistic).

% atom_id: a084f311eef736a0 | chunk: f45f38442b6d6170 | strength: constitutional
obligated(collective, none, respect_fundamental_rights).

% atom_id: 388d2c4beb02903f | chunk: f5940d03d51050ec | strength: constitutional
obligated(authority, resident_entity, require_authorization_for_foreign_request).

% atom_id: a340f0a4b7d27b46 | chunk: f5f6755b16552c6d | strength: constitutional
obligated(authority, servant, grant_stability_after_three_years_of_service) :-
    years_of_service(3),
    recruitment_method(public_concours).

% atom_id: 0059c333ec9af29c | chunk: f7d4d8918a368c71 | strength: constitutional
obligated(state, citizen, guarantee_universal_healthcare_access).

% atom_id: 4b6b8cdf97e587a8 | chunk: f9732fe6613d6f36 | strength: constitutional
obligated(authority, worker, process_and_judge_labor_disputes).

% atom_id: 2c1f4c1829235cbe | chunk: f9a7fa2b7428026a | strength: constitutional
obligated(state, public_servant_retiree, review_rights_and_benefits) :-
    time_since_constitution(unknown).

% atom_id: b7cf5fbe4fe3c3ff | chunk: f9a7fa2b7428026a | strength: constitutional
obligated(state, public_servant_retiree, update_benefits_to_constitutional_standards) :-
    time_since_constitution(unknown).

% atom_id: 0754654359e50b5a | chunk: f9d93552f93d0a8b | strength: constitutional
permitted(collective, none, propose_direct_unconstitutionality_action).

% atom_id: 7b480f34c78fd89a | chunk: f9d93552f93d0a8b | strength: constitutional
permitted(collective, none, propose_declaratory_constitutionality_action).

% atom_id: fb0c174e916dc021 | chunk: fa031e06c4d66aee | strength: constitutional
obligated(municipal_legislative_power, municipality, exercise_external_control_fiscalization).

% atom_id: 2ea896682d6f4ce9 | chunk: fa031e06c4d66aee | strength: constitutional
obligated(municipal_executive_power, municipality, exercise_internal_control_fiscalization).

% atom_id: e5c768ae3021ffe1 | chunk: fa0bacb0c6af70b2 | strength: constitutional
obligated(collective, elderly_person, ensure_participation_and_wellbeing_of_elderly).

% atom_id: d592ab600ef52dac | chunk: fa4c90296df66a94 | strength: constitutional
prohibited(union, public, assume_financial_obligations_from_state_creation) :-
    type_of_expense(retired_personnel_expenses),
    type_of_expense(internal_or_external_debt_amortizations).

% atom_id: 0763ca54bedf0038 | chunk: faa2aba154a8b7d5 | strength: constitutional
obligated(state, public_servant, establish_criteria_for_loss_of_stable_position) :-
    servant_activity(exclusive_state_activities).

% atom_id: 01701af93bc9a763 | chunk: fbe129dabba33b55 | strength: constitutional
obligated(municipality, none, adopt_organic_law_in_two_rounds) :-
    intercession_days(X_0), X_0 >= 10,
    approval_threshold(two_thirds_of_council_members).

% atom_id: d42581e7a06b88ce | chunk: fbe129dabba33b55 | strength: constitutional
obligated(municipality, none, promulgate_organic_law) :-
    approval_threshold(two_thirds_of_council_members).

% atom_id: 563d554680a06779 | chunk: fbe129dabba33b55 | strength: constitutional
obligated(municipality, none, comply_with_constitutional_principles).

% atom_id: 203f41df2581b36b | chunk: fbe129dabba33b55 | strength: constitutional
obligated(municipality, none, comply_with_state_constitution_principles).

% atom_id: fcde634ab19963c8 | chunk: fcf42dd0a13feb1d | strength: constitutional
obligated(state, family, provide_special_protection_to_family).

% atom_id: dcc17b7956af4edc | chunk: fdaccc65d22ca49a | strength: constitutional
permitted(state, none, directly_explore_economic_activity) :-
    national_security_impetus(true),
    collective_interest_significance(relevant).