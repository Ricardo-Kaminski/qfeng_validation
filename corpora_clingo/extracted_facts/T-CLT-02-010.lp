% Extracao Q-FENG (passthrough manual) para T-CLT-02-010
% Tipo: T-CLT-02
% Confianca: 0.950
% Extractor: claude-opus-4-7-passthrough
% Supervisor: Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)
% Sessao: passthrough-2026-04-29-sessao-01

% span: Empresa de tecnologia firmou ACT com sindicato dos trabalhadores em informatica
banco_horas_implementado(empresa_tecnologia).
% span: firmou ACT com sindicato
tem_act(empresa_tecnologia).
% span: prazo maximo de 5 meses
prazo_compensacao_meses(empresa_tecnologia, 5).
% span: limitado a 40h mensais de acumulo
acumulo_maximo_horas(empresa_tecnologia, 40).
% span: ACT com sindicato dos trabalhadores em informatica
participacao_sindical_categoria(empresa_tecnologia, categoria_informatica).
% span: ACT foi devidamente registrada
cct_registrada_srte(empresa_tecnologia).
% span: O extrato do banco e fornecido mensalmente a cada trabalhador
extrato_mensal_entregue(empresa_tecnologia).
% span: Todos os saldos sao compensados dentro do prazo estabelecido
compensacao_realizada_no_prazo(empresa_tecnologia).
% span: Nao ha horas extras acima de 2h/dia (8h normais + 2h max)
jornada_diaria_horas(empresa_tecnologia, 10).
