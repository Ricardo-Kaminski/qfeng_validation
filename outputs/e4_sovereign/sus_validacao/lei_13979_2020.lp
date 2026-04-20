% atom_id: 7e2267ddfcfff855 | chunk: 0b4b7026c74c9b1f | strength: statutory
obligated(executive_power, none, regulate_obligations).

% atom_id: d3979e30f45b208f | chunk: 96effb09fa4548ed | strength: statutory
permitted(orgao_ou_entidade, none, utilizar_sistema_de_registro_de_precos) :-
    dispensa_de_licitacao(sim),
    compra_ou_contratacao_por_mais_de_um_orgao_ou_entidade(sim).

% atom_id: 366c823162a09640 | chunk: d5f9ce9796098f43 | strength: statutory
prohibited(concessionaria_e_empresa_de_transporte_publico, passageiro, enter_terminals_and_transport_means_in_disobedience_to_estab).

% atom_id: 476e7693020da2fe | chunk: 3114d98f011b4601 | strength: statutory
obligated(state, healthcare_actions_and_services, utilize_funds_from_fines).

% atom_id: 8bc471ce98ae06ea | chunk: 4f8bc49ae83a2e09 | strength: statutory
obligated(executive_power, none, establish_regulations_for_mask_wearing).

% atom_id: 8af4626aef38e967 | chunk: 4f8bc49ae83a2e09 | strength: statutory
obligated(public, none, wear_mask_in_public_spaces) :-
    location(public_spaces_via_publica_transportes_publicos_coletivos).

% atom_id: c0e4d6ce3b12ff4e | chunk: 6880044d6c2c8cba | strength: statutory
obligated(state, person, guarantee_obligation) :-
    medical_declaration(true),
    age(X_1), X_1 < 3.

% atom_id: 219ea33598e67624 | chunk: b76728f45218d034 | strength: statutory
obligated(executive_power, none, establish_authorities_for_fiscalization_and_collection).

% atom_id: 5e01f5dcbc7b1b1d | chunk: d5f9ce9796098f43 | strength: statutory
obligated(concessionaria_e_empresa_de_transporte_publico, none, act_in_collaboration_with_poder_publico).

% atom_id: 611d2bd2b3e9d06a | chunk: e301b38009d0431a | strength: statutory
obligated(establishment, none, provide_alcohol_based_hand_rub_70_percent) :-
    functioning_during_pandemic(covid_19).