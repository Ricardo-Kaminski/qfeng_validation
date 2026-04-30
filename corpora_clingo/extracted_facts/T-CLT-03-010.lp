% Extracao Q-FENG (passthrough manual) para T-CLT-03-010
% Tipo: T-CLT-03
% Confianca: 0.960
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: CCT previa banco de horas
banco_horas_implementado(empresa_acumulo_excede).
% span: CCT previa
tem_cct(empresa_acumulo_excede).
% span: acumulo maximo de 80h
acumulo_maximo_horas(empresa_acumulo_excede, 80).
% span: A empresa permitiu que um operador acumulasse 200h
acumulo_real_horas(empresa_acumulo_excede, 200).
% span: 200h acumuladas vs limite previsto de 80h sem nova negociacao
acumulo_acima_do_limite_instrumento(empresa_acumulo_excede).
