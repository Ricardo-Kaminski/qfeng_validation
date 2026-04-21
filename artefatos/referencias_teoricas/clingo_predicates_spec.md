# Especificação de Predicados Clingo — Referência para E3
## Baseado no WP Q-FENG e nas definições de schemas.py

---

## Estrutura geral dos predicados

O Q-FENG usa Clingo ASP (Answer Set Programming) como motor simbólico.
Predicados são gerados pelo E3 a partir de DeonticAtoms produzidos pelo E2.

### Tipos deônticos e templates

**OBLIGATION (obrigação)**
```prolog
% Template geral
obrigacao(AGENT, ACTION, OBJECT) :- CONDITIONS.

% Exemplo — Art. 196 CF/88 (universalidade SUS)
obrigacao(estado, garantir, acesso_saude) :- populacao(P), residente_brasil(P).

% Com qualificador de soberania (SOVEREIGN)
:- not obrigacao(estado, garantir, acesso_saude).
```

**PROHIBITION (proibição)**
```prolog
% Template geral
proibicao(AGENT, ACTION) :- CONDITIONS.

% Exemplo — discriminação por critério racial (Medicaid / equidade)
proibicao(algoritmo, priorizar_por, custo_historico_racial) :-
    proxy_racial(custo_historico_racial).

% Com soberania
:- proibicao(A, AC), decisao(A, AC).
```

**PERMISSION (permissão)**
```prolog
% Template geral
permissao(AGENT, ACTION) :- CONDITIONS.

% Exemplo — EU AI Act, Art. 9: uso de sistema alto risco se gestão implementada
permissao(provider, deploy_high_risk_system) :-
    sistema_alto_risco(S), gestao_risco_implementada(S), avaliacao_conformidade(S).
```

**META-FATOS de concorrência (gerados pelo runner E3 a partir do concurrency_map)**
```prolog
% Dois chunks normativos com obrigações potencialmente conflitantes
concurrent(chunk_id_a, chunk_id_b).

% Resolução por PRECEDÊNCIA (definida no E4 HITL)
:- obrigacao_ativa(chunk_id_b), not suspensa_por_precedencia(chunk_id_b, chunk_id_a).

% Resolução por COEXISTÊNCIA (disjunção — definida no E4 HITL)
aplica_norma_a(X) | aplica_norma_b(X) :- concurrent(id_a, id_b), caso(X).
```

---

## Soberania Ontológica

Predicados SOVEREIGN recebem constraints fortes que tornam sua violação
logicamente impossível no answer set:

```prolog
% Declaração de soberania
soberano(equidade_racial_verificada).

% Constraint: qualquer decisão de alocação requer equidade verificada
:- decisao_alocacao(P, _), not equidade_racial_verificada(P).

% Se o predicado soberano estiver ausente, o constraint nunca é satisfeito
% → CONSTITUTIONAL_FAILURE no E5
```

Predicados ELASTIC não recebem constraint forte — são satisfeitos por default
mas podem ser sobrescritos por contexto:

```prolog
% Predicado elástico — satisfeito por default, sobrescrito por exceção
prioridade_padrao(P) :- paciente(P), not excecao_urgencia(P).
```

---

## Convenções de nomenclatura

| Elemento | Convenção | Exemplo |
|----------|-----------|---------|
| Agentes | snake_case singular | `estado`, `provider`, `algoritmo` |
| Ações | infinitivo snake_case | `garantir`, `deploy`, `priorizar` |
| Objetos | snake_case descritivo | `acesso_saude`, `high_risk_system` |
| Chunk IDs | sha256[:16] entre aspas | `chunk("a3f2b1c4d5e6f7a8")` |
| Regime | prefixo | `br_`, `us_`, `eu_` |

---

## Validação sintática obrigatória (E3 validator.py)

```python
import clingo

def validate_lp(lp_text: str) -> bool:
    """Valida sintaxe Clingo sem resolver — lança ClingoValidationError se inválido."""
    ctl = clingo.Control()
    try:
        ctl.add("base", [], lp_text)
        ctl.ground([("base", [])])
        return True
    except RuntimeError as e:
        raise ClingoValidationError(f"Predicado inválido: {e}") from e
```

**NUNCA salvar um predicado que não passe nessa validação.**

---

## Cenários de teste E5 — exemplos mínimos

```prolog
% tests/scenarios/brasil_execucao.lp
% Cenário: alerta gerado mas não escalado → EXECUTION_FAILURE esperado

% Fatos do caso Manaus 2021
consumo_oxigenio(manaus, 2021_jan_08, critico).
capacidade_hospitalar(manaus, 2021_jan_08, esgotada).

% Predicados Q-FENG carregados de outputs/e4_validated/brasil.lp
#include "outputs/e4_validated/brasil.lp".

% Query: esperamos que alerta seja gerado
#show alerta_gerado/3.
% Query: esperamos que resposta_escalada NÃO exista → execução falhou
#show resposta_escalada/3.
```

```prolog
% tests/scenarios/usa_constitucional.lp
% Cenário: predicado soberano ausente → CONSTITUTIONAL_FAILURE esperado

% Fatos do caso Obermeyer 2019
paciente(p001). raca(p001, negra). custo_historico(p001, baixo).
necessidade_clinica(p001, alta).  % necessidade real vs. custo histórico

% Predicados Q-FENG SEM equidade_racial_verificada (simular ausência)
#include "outputs/e4_validated/usa_sem_soberania.lp".

% Query: esperamos que alerta_equidade NÃO exista → falha constitucional
#show alerta_equidade/2.
```
