# E3 Translation — Design Spec
**Data:** 2026-04-19
**Status:** Aprovado pelo usuário
**Módulo:** `src/qfeng/c1_digestion/translation/`
**Contexto:** E0/E1/E2 aprovados. E3 transforma DeonticAtoms do cache E2 em ClingoPredicates (.lp), incluindo meta-fatos de concorrência do concurrency_map.json.

---

## 1. Objetivo

Implementar o módulo E3 que:

1. Lê DeonticAtoms do cache E2 (`outputs/deontic_cache/*.json`)
2. Traduz cada atom em um ClingoPredicate com regra .lp (template-based)
3. Traduz condições estruturadas em corpo de regra Clingo (opção B)
4. Gera meta-fatos `concurrent(A, B).` dos pares do `concurrency_map.json`
5. Valida sintaxe via API Python do clingo 5.8.0
6. Salva outputs por regime + relatório E3

---

## 2. Decisões de design

| Decisão | Escolha | Razão |
|---------|---------|-------|
| Abordagem de tradução | Template-based (sem LLM) | Determinístico, auditável, preserva primazia simbólica |
| Condições | Predicados Clingo no corpo da regra | Captura semântica, testável em E5 |
| Validação de sintaxe | `clingo.Control().add()` Python API | clingo 5.8.0 disponível; parse error = syntax_valid=False |
| Output por regime | `outputs/e3_predicates/{regime}/{source}.lp` | Consistente com E1/E2 |
| Concorrências | `outputs/e3_predicates/concurrent_facts.lp` | Arquivo separado — carregado pelo solver em E5 |
| `patient=None` | Mantido como átomo `none` na aridade 3 | Consistência de aridade para E5 pattern matching |
| Traceabilidade | Comments com atom_id e chunk_id em cada regra | Auditoria E4 HITL |

---

## 3. Estrutura de arquivos

```
src/qfeng/c1_digestion/translation/
  __init__.py           ← exporta: atom_to_predicate, run_e3_batch, E3BatchResult
  translator.py         ← atom_to_predicate(DeonticAtom) → ClingoPredicate
  templates.py          ← templates Clingo por DeonticModality + condition translation
  runner.py             ← run_e3_batch: carrega E2 cache → outputs + relatório
  __main__.py           ← CLI: --scope, --deontic-dir, --output-dir

outputs/e3_predicates/
  brasil/
    lei_8080_1990.lp
    ...
  eu/
    eu_ai_act_2024_1689.lp
    ...
  usa/
    ssa_title_xix_1902.lp
    ...
  concurrent_facts.lp   ← 329 concurrent(A, B). meta-fatos

tests/test_e3/
  __init__.py           (já existe)
  test_translator.py    ← unit tests atom_to_predicate
  test_runner.py        ← integration tests batch
  test_syntax.py        ← clingo syntax validation em regras geradas
```

---

## 4. API pública

### 4.1 `templates.py`

```python
from qfeng.core.schemas import DeonticAtom, DeonticModality

_PREDICATE_NAME: dict[str, str] = {
    DeonticModality.OBLIGATION:  "obligated",
    DeonticModality.PROHIBITION: "prohibited",
    DeonticModality.PERMISSION:  "permitted",
    DeonticModality.FACULTY:     "permitted",
}

def modality_to_predicate_name(modality: DeonticModality) -> str:
    return _PREDICATE_NAME[modality]

def condition_to_clingo(cond: dict) -> str:
    """Converte DeonticCondition para literal Clingo.

    Exemplos:
      {variable: use_cases, operator: ==, value: high_risk_ai_systems}
        → "use_cases(high_risk_ai_systems)"
      {variable: inconsistent_submissions, operator: >, value: 0}
        → "inconsistent_submissions(X_0), X_0 > 0"
    """
    ...

def build_rule(name: str, agent: str, patient: str, action: str,
               conditions: list[str]) -> str:
    """Monta regra Clingo completa.

    Sem condições: "obligated(agent, patient, action)."
    Com condições: "obligated(agent, patient, action) :-\n    cond1,\n    cond2."
    """
    ...
```

### 4.2 `translator.py`

```python
from qfeng.core.schemas import ClingoPredicate, DeonticAtom

def atom_to_predicate(atom: DeonticAtom) -> ClingoPredicate:
    """Transforma um DeonticAtom em ClingoPredicate com regra .lp validada.

    Returns:
        ClingoPredicate com syntax_valid=True/False segundo parse clingo.
    """
    ...
```

### 4.3 `runner.py`

```python
from qfeng.c1_digestion.scope.config import ScopeConfig

def run_e3_batch(
    deontic_dir: Path,
    output_dir: Path,
    scope: ScopeConfig,
    concurrency_map_path: Path,
) -> E3BatchResult:
    """Traduz todos os DeonticAtoms do cache E2 filtrado pelo scope.

    Args:
        deontic_dir: outputs/deontic_cache/
        output_dir: outputs/e3_predicates/
        scope: ScopeConfig para filtrar por regime
        concurrency_map_path: outputs/e1_chunks_scoped/concurrency_map.json
    """
    ...
```

### 4.4 `E3BatchResult` (dataclass)

```python
@dataclass
class E3BatchResult:
    total_atoms: int = 0
    total_predicates: int = 0
    syntax_valid: int = 0
    syntax_invalid: int = 0
    predicates_per_regime: dict[str, int] = field(default_factory=dict)
    concurrent_facts: int = 0
    warnings: list[str] = field(default_factory=list)
```

---

## 5. Templates Clingo por modalidade

### 5.1 Sem condições (fato ground)
```prolog
% atom_id: ea9646908e4d3ea2 | chunk: 003bd71d0f5d3a8c | strength: statutory
permitted(municipality, none, organize_sus_in_districts).
```

### 5.2 Com condições string (== operator)
```prolog
% atom_id: 5b7194434043d835 | chunk: 0097db893574abbe | strength: statutory
permitted(commission, none, adopt_delegated_acts) :-
    use_cases(high_risk_ai_systems),
    conditions_fulfilled(both).
```

### 5.3 Com condições numéricas (>, <, >=, <=)
```prolog
% atom_id: cf1cf23cfc71002a | chunk: 00915e1cbfff5699 | strength: regulatory
obligated(state_agency, state_agency, provide_information) :-
    inconsistent_submissions(X_0), X_0 > 0.
```

### 5.4 Meta-fatos de concorrência
```prolog
% concurrent_facts.lp — gerado do concurrency_map.json
concurrent(ea9646908e4d3ea2, 5b7194434043d835).
concurrent(cf1cf23cfc71002a, ea9646908e4d3ea2).
...
```

**Regra de normalização:** nomes de valores/variáveis são normalizados para snake_case:
- `"high-risk_ai_systems"` → `high_risk_ai_systems`
- `"state_agency"` → `state_agency` (já ok)
- valores numéricos → mantidos como literais Clingo

---

## 6. Condition translation rules

| Operator E2 | Clingo gerado | Exemplo |
|-------------|--------------|---------|
| `==` + string value | `variable(value)` | `use_cases(high_risk_ai_systems)` |
| `==` + numeric | `variable(N)` | `count(5)` |
| `>` | `variable(X_i), X_i > N` | `submissions(X_0), X_0 > 0` |
| `<` | `variable(X_i), X_i < N` | `rate(X_0), X_0 < 80` |
| `>=` | `variable(X_i), X_i >= N` | `coverage(X_0), X_0 >= 138` |
| `<=` | `variable(X_i), X_i <= N` | `bed_ratio(X_0), X_0 <= 2` |
| `!=` | `variable(X_i), X_i != N` | `inconsistencies(X_0), X_0 != 0` |

`X_i` é variável Clingo única por condição (X_0, X_1, ...) para evitar colisão.

---

## 7. Validação de sintaxe

```python
import clingo

def validate_syntax(rule: str) -> bool:
    """Retorna True se clingo parseia a regra sem erro."""
    ctl = clingo.Control()
    try:
        ctl.add("base", [], rule)
        return True
    except RuntimeError:
        return False
```

Atoms com `syntax_valid=False` são incluídos no output com flag de aviso — não bloqueiam o batch. E4 HITL os revisará.

---

## 8. Filtro de regime no runner

O runner carrega os atoms do cache E2 e filtra pelo scope:
1. Para cada arquivo `.json` em `deontic_dir/`
2. Obtém `source_chunk_id` de cada atom
3. Verifica o regime do chunk via lookup no E1 output JSON
4. Inclui apenas atoms cujo regime está em `scope.regimes`

**Alternativa mais simples (MVP):** processar TODOS os atoms do cache E2 sem filtro de regime, agrupando por chunk_id → regime via E1 JSONs. Scope é aplicado apenas no nível de quais regimes geram arquivos .lp separados.

---

## 9. Testes

### `test_translator.py` — 12 casos

| Caso | Input | Esperado |
|------|-------|---------|
| obligation sem condições | modality=obligation, conditions=[] | `obligated(A, P, V).` |
| obligation com condição `>` | conditions=[{var, >, 0}] | `obligated(...) :- var(X), X > 0.` |
| faculty sem condições | modality=faculty | `permitted(A, P, V).` |
| permission com condição `==` string | conditions=[{var, ==, str}] | `permitted(...) :- var(str).` |
| prohibition | modality=prohibition | `prohibited(A, P, V).` |
| patient=None | patient="None" | `obligated(A, none, V).` |
| múltiplas condições | conditions=[c1, c2] | body com 2 literais |
| snake_case normalização | value="high-risk_ai_systems" | `high_risk_ai_systems` |
| syntax_valid=True | regra válida | clingo parse OK |
| syntax_valid=False | regra inválida (injetada) | syntax_valid=False |
| traceabilidade | qualquer atom | comment com atom_id + chunk_id |
| strength no comment | strength=statutory | `% strength: statutory` |

### `test_runner.py` — 5 casos

| Caso | Esperado |
|------|---------|
| Batch com 3 atoms fixture | 3 ClingoPredicate gerados, arquivos .lp criados |
| concurrent_facts.lp gerado | N linhas = len(concurrency_map pairs) |
| Regime correto por arquivo | brasil atoms em `brasil/` |
| E3BatchResult correto | total_atoms, syntax_valid contados |
| atoms com syntax_invalid | incluídos em output com warning |

### `test_syntax.py` — 3 casos

| Caso | Esperado |
|------|---------|
| Regra obrigação válida | `validate_syntax()` → True |
| Regra com erro de sintaxe | `validate_syntax()` → False |
| Regra com variável Clingo livre | `validate_syntax()` → True |

---

## 10. Critérios de aprovação (Fase A → B)

### Fase A (pytest)
- `pytest tests/test_e3/ -v` — todos verdes
- `ruff check src/qfeng/c1_digestion/translation/` — sem erros
- `mypy src/qfeng/c1_digestion/translation/` — sem erros (strict)

### Fase B (corpus real)
```bash
python -m qfeng.c1_digestion.translation \
    --deontic-dir outputs/deontic_cache/ \
    --scope configs/sus_validacao.yaml \
    --concurrency-map outputs/e1_chunks_scoped/concurrency_map.json \
    --output-dir outputs/e3_predicates/
```

Critérios:
- [ ] ≥ 5.000 predicados gerados (dos 5.136 atoms do E2)
- [ ] syntax_valid ≥ 95% dos predicados
- [ ] concurrent_facts.lp com 329 fatos
- [ ] Amostra de 3 predicados por regime revisada e aprovada pelo usuário
- [ ] Usuário diz **"pode avançar"**

---

## 11. O que NÃO está no escopo deste módulo

- Classificação SOVEREIGN/ELASTIC (responsabilidade do E4 HITL)
- `validated_by` e `validated_at` (campos do E4)
- Resolução de concorrências (E4)
- Execução Clingo / consultas ASP (E5)
- Predicados agnósticos de anti-alucinação jurídica (Paper 2 — E3 futuro)
