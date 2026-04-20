% Cenário C3 — Concentração regional SUS (theta ~ pi)
constitutional_basis("CF88_Art196").
constitutional_basis("CF88_Art198").
constitutional_basis("CF88_Art3_III").
statutory_basis("Lei8080_Art7_I").
statutory_basis("Lei8080_Art7_IV").

% Estado operacional — distribuição desigual de recursos
regional_resource_concentration(high).
uf_benefited("SP").
uf_disadvantaged("AM").
resource_allocation_gap_pct(45).    % diferença percentual de recursos

operational_mode(autonomous).
decision_output(allocation_system, maintain_current_allocation).
increases_regional_inequality(maintain_current_allocation).
