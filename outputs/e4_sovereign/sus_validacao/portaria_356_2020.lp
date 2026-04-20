% atom_id: 32732051e31f5e13 | chunk: 29f484745f7485d7 | strength: regulatory
permitted(medical_prescriber_or_epidemiological_agent, none, determine_isolation_measure).

% atom_id: d6cdf308082854f5 | chunk: 2d3b2836c83b96d3 | strength: regulatory
prohibited(authority, none, determine_or_maintain_quarantine_measure) :-
    end_of_emergency_declaration(encerramento).

% atom_id: b4d41cb1b6b54012 | chunk: 889aa8d9aafc1fac | strength: regulatory
obligated(secretary_of_health, none, adopt_measures) :-
    unidade_da_federacao(sem_agente_de_vigilancia_epidemiologica).

% atom_id: 2171f48c4fac8e48 | chunk: e06a4df7af559184 | strength: regulatory
obligated(agente_de_vigilancia_epidemiologica, none, recommend_isolation).

% atom_id: 2b2f922b4848eb63 | chunk: e06a4df7af559184 | strength: regulatory
obligated(caso_de_contactantes_proximos_a_pessoas_sintomaticas_ou_port, none, undergo_isolation) :-
    relacao_com_pessoa_sintomatica(contactante_proximo).