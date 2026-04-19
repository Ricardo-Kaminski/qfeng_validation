# E3 Translation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement E3 Translation — transforms `DeonticAtom` objects from the E2 cache into Clingo `.lp` predicate files plus `concurrent_facts.lp` meta-facts, with syntax validation via the clingo Python API.

**Architecture:** Template-based translation (no LLM): `templates.py` builds Clingo rule strings from modality/condition data; `translator.py` orchestrates per-atom translation and validates syntax; `runner.py` drives the batch over the E2 deontic cache, resolves chunk→regime, writes per-regime `.lp` files, and generates `concurrent_facts.lp` from `concurrency_map.json`. The E1 output directory is derived from `concurrency_map_path.parent`.

**Tech Stack:** Python 3.11, clingo 5.8.0 (via `import clingo`), Pydantic v2, pytest, ruff, mypy --strict.

---

## File Map

| File | Status | Responsibility |
|------|--------|----------------|
| `src/qfeng/c1_digestion/translation/__init__.py` | Modify | Export public API |
| `src/qfeng/c1_digestion/translation/templates.py` | Create | `_normalize`, `modality_to_predicate_name`, `condition_to_clingo`, `build_rule` |
| `src/qfeng/c1_digestion/translation/translator.py` | Create | `validate_syntax`, `atom_to_predicate` |
| `src/qfeng/c1_digestion/translation/runner.py` | Create | `E3BatchResult`, `run_e3_batch` |
| `src/qfeng/c1_digestion/translation/__main__.py` | Create | CLI entry point |
| `tests/test_e3/__init__.py` | Already exists | — |
| `tests/test_e3/test_translator.py` | Create | Unit tests for `atom_to_predicate` (12 cases) |
| `tests/test_e3/test_runner.py` | Create | Integration tests for `run_e3_batch` (5 cases) |
| `tests/test_e3/test_syntax.py` | Create | Syntax validation tests (3 cases) |

---

## Task 1: Scaffold Stubs

**Files:**
- Modify: `src/qfeng/c1_digestion/translation/__init__.py`
- Create: `src/qfeng/c1_digestion/translation/templates.py`
- Create: `src/qfeng/c1_digestion/translation/translator.py`
- Create: `src/qfeng/c1_digestion/translation/runner.py`
- Create: `src/qfeng/c1_digestion/translation/__main__.py`
- Create: `tests/test_e3/test_translator.py`
- Create: `tests/test_e3/test_runner.py`
- Create: `tests/test_e3/test_syntax.py`

- [ ] **Step 1: Create `templates.py` stub**

```python
"""E3 — Clingo rule templates and condition translation."""
from __future__ import annotations

from qfeng.core.schemas import DeonticCondition, DeonticModality

_PREDICATE_NAME: dict[DeonticModality, str] = {
    DeonticModality.OBLIGATION:  "obligated",
    DeonticModality.PROHIBITION: "prohibited",
    DeonticModality.PERMISSION:  "permitted",
    DeonticModality.FACULTY:     "permitted",
}


def _normalize(s: str) -> str:
    raise NotImplementedError


def modality_to_predicate_name(modality: DeonticModality) -> str:
    raise NotImplementedError


def condition_to_clingo(cond: DeonticCondition, idx: int) -> str:
    raise NotImplementedError


def build_rule(
    name: str,
    agent: str,
    patient: str,
    action: str,
    conditions: list[str],
) -> str:
    raise NotImplementedError
```

- [ ] **Step 2: Create `translator.py` stub**

```python
"""E3 — DeonticAtom → ClingoPredicate translation."""
from __future__ import annotations

from qfeng.core.schemas import ClingoPredicate, DeonticAtom


def validate_syntax(rule: str) -> bool:
    raise NotImplementedError


def atom_to_predicate(atom: DeonticAtom) -> ClingoPredicate:
    raise NotImplementedError
```

- [ ] **Step 3: Create `runner.py` stub**

```python
"""E3 — Batch runner: deontic cache → Clingo .lp files."""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

from qfeng.c1_digestion.scope.config import ScopeConfig

logger = logging.getLogger(__name__)


@dataclass
class E3BatchResult:
    total_atoms: int = 0
    total_predicates: int = 0
    syntax_valid: int = 0
    syntax_invalid: int = 0
    predicates_per_regime: dict[str, int] = field(default_factory=dict)
    concurrent_facts: int = 0
    warnings: list[str] = field(default_factory=list)


def run_e3_batch(
    deontic_dir: Path,
    output_dir: Path,
    scope: ScopeConfig,
    concurrency_map_path: Path,
) -> E3BatchResult:
    raise NotImplementedError
```

- [ ] **Step 4: Create `__main__.py` stub**

```python
"""E3 — CLI entry point."""
from __future__ import annotations


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Create empty test files**

`tests/test_e3/test_translator.py`:
```python
"""Unit tests for E3 translator — atom_to_predicate."""
```

`tests/test_e3/test_runner.py`:
```python
"""Integration tests for E3 runner — run_e3_batch."""
```

`tests/test_e3/test_syntax.py`:
```python
"""Tests for E3 validate_syntax."""
```

- [ ] **Step 6: Update `__init__.py`**

```python
"""E3 — Translation: DeonticAtom → Clingo/dPASP predicates."""
from qfeng.c1_digestion.translation.runner import E3BatchResult, run_e3_batch
from qfeng.c1_digestion.translation.translator import atom_to_predicate, validate_syntax

__all__ = ["atom_to_predicate", "validate_syntax", "run_e3_batch", "E3BatchResult"]
```

- [ ] **Step 7: Verify imports compile**

```bash
cd C:\Workspace\academico\qfeng_validacao
conda activate qfeng
python -c "from qfeng.c1_digestion.translation import atom_to_predicate, run_e3_batch, E3BatchResult, validate_syntax; print('OK')"
```

Expected: `OK`

- [ ] **Step 8: Commit scaffold**

```bash
git add src/qfeng/c1_digestion/translation/ tests/test_e3/
git commit -m "feat(e3): scaffold translation module stubs"
```

---

## Task 2: TDD `_normalize` + `modality_to_predicate_name`

**Files:**
- Modify: `src/qfeng/c1_digestion/translation/templates.py`
- Modify: `tests/test_e3/test_translator.py`

- [ ] **Step 1: Write failing tests**

Add to `tests/test_e3/test_translator.py`:

```python
import pytest
from qfeng.c1_digestion.translation.templates import (
    _normalize,
    modality_to_predicate_name,
)
from qfeng.core.schemas import DeonticModality


class TestNormalize:
    def test_hyphen_to_underscore(self) -> None:
        assert _normalize("high-risk_ai_systems") == "high_risk_ai_systems"

    def test_space_to_underscore(self) -> None:
        assert _normalize("state agency") == "state_agency"

    def test_already_snake(self) -> None:
        assert _normalize("state_agency") == "state_agency"

    def test_lowercase(self) -> None:
        assert _normalize("Municipality") == "municipality"

    def test_mixed(self) -> None:
        assert _normalize("High-Risk AI") == "high_risk_ai"


class TestModalityToPredicateName:
    def test_obligation(self) -> None:
        assert modality_to_predicate_name(DeonticModality.OBLIGATION) == "obligated"

    def test_prohibition(self) -> None:
        assert modality_to_predicate_name(DeonticModality.PROHIBITION) == "prohibited"

    def test_permission(self) -> None:
        assert modality_to_predicate_name(DeonticModality.PERMISSION) == "permitted"

    def test_faculty(self) -> None:
        assert modality_to_predicate_name(DeonticModality.FACULTY) == "permitted"
```

- [ ] **Step 2: Run to verify failure**

```bash
conda activate qfeng && pytest tests/test_e3/test_translator.py::TestNormalize tests/test_e3/test_translator.py::TestModalityToPredicateName -v
```

Expected: FAIL with `NotImplementedError`.

- [ ] **Step 3: Implement `_normalize` and `modality_to_predicate_name`**

In `templates.py`, replace the two `raise NotImplementedError` stubs:

```python
def _normalize(s: str) -> str:
    """Normalize string to Clingo-safe snake_case atom."""
    return s.lower().replace("-", "_").replace(" ", "_")


def modality_to_predicate_name(modality: DeonticModality) -> str:
    return _PREDICATE_NAME[modality]
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
pytest tests/test_e3/test_translator.py::TestNormalize tests/test_e3/test_translator.py::TestModalityToPredicateName -v
```

Expected: 9 PASSED.

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/translation/templates.py tests/test_e3/test_translator.py
git commit -m "feat(e3): implement _normalize and modality_to_predicate_name"
```

---

## Task 3: TDD `condition_to_clingo`

**Files:**
- Modify: `src/qfeng/c1_digestion/translation/templates.py`
- Modify: `tests/test_e3/test_translator.py`

- [ ] **Step 1: Write failing tests**

Add to `tests/test_e3/test_translator.py`:

```python
from qfeng.c1_digestion.translation.templates import condition_to_clingo
from qfeng.core.schemas import DeonticCondition


class TestConditionToClingo:
    def test_eq_string_value(self) -> None:
        cond = DeonticCondition(variable="use_cases", operator="==", value="high_risk_ai_systems")
        assert condition_to_clingo(cond, 0) == "use_cases(high_risk_ai_systems)"

    def test_eq_string_normalizes_value(self) -> None:
        cond = DeonticCondition(variable="use_cases", operator="==", value="high-risk_ai_systems")
        assert condition_to_clingo(cond, 0) == "use_cases(high_risk_ai_systems)"

    def test_gt_numeric(self) -> None:
        cond = DeonticCondition(variable="inconsistent_submissions", operator=">", value="0")
        assert condition_to_clingo(cond, 0) == "inconsistent_submissions(X_0), X_0 > 0"

    def test_lt_numeric(self) -> None:
        cond = DeonticCondition(variable="rate", operator="<", value="80")
        assert condition_to_clingo(cond, 0) == "rate(X_0), X_0 < 80"

    def test_gte_numeric(self) -> None:
        cond = DeonticCondition(variable="coverage", operator=">=", value="138")
        assert condition_to_clingo(cond, 0) == "coverage(X_0), X_0 >= 138"

    def test_lte_numeric(self) -> None:
        cond = DeonticCondition(variable="bed_ratio", operator="<=", value="2")
        assert condition_to_clingo(cond, 0) == "bed_ratio(X_0), X_0 <= 2"

    def test_neq_numeric(self) -> None:
        cond = DeonticCondition(variable="inconsistencies", operator="!=", value="0")
        assert condition_to_clingo(cond, 0) == "inconsistencies(X_0), X_0 != 0"

    def test_variable_index_increments(self) -> None:
        cond = DeonticCondition(variable="count", operator=">", value="5")
        result_idx1 = condition_to_clingo(cond, 1)
        assert "X_1" in result_idx1

    def test_eq_numeric_value(self) -> None:
        cond = DeonticCondition(variable="count", operator="==", value="5")
        assert condition_to_clingo(cond, 0) == "count(5)"
```

- [ ] **Step 2: Run to verify failure**

```bash
pytest tests/test_e3/test_translator.py::TestConditionToClingo -v
```

Expected: FAIL with `NotImplementedError`.

- [ ] **Step 3: Implement `condition_to_clingo`**

In `templates.py`, replace the `condition_to_clingo` stub:

```python
def condition_to_clingo(cond: DeonticCondition, idx: int) -> str:
    """Translate a DeonticCondition to Clingo literal(s).

    For == with string: variable(value)
    For == with numeric: variable(N)
    For comparison ops: variable(X_i), X_i op N
    """
    var = _normalize(cond.variable)
    op = cond.operator
    val = cond.value

    def _is_numeric(v: str) -> bool:
        try:
            float(v)
            return True
        except ValueError:
            return False

    if op == "==":
        if _is_numeric(val):
            return f"{var}({val})"
        return f"{var}({_normalize(val)})"

    # Comparison operator: use Clingo arithmetic variable
    x = f"X_{idx}"
    return f"{var}({x}), {x} {op} {val}"
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
pytest tests/test_e3/test_translator.py::TestConditionToClingo -v
```

Expected: 9 PASSED.

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/translation/templates.py tests/test_e3/test_translator.py
git commit -m "feat(e3): implement condition_to_clingo with all operators"
```

---

## Task 4: TDD `build_rule`

**Files:**
- Modify: `src/qfeng/c1_digestion/translation/templates.py`
- Modify: `tests/test_e3/test_translator.py`

- [ ] **Step 1: Write failing tests**

Add to `tests/test_e3/test_translator.py`:

```python
from qfeng.c1_digestion.translation.templates import build_rule


class TestBuildRule:
    def test_fact_no_conditions(self) -> None:
        result = build_rule("obligated", "state", "citizen", "provide_healthcare", [])
        assert result == "obligated(state, citizen, provide_healthcare)."

    def test_rule_with_one_condition(self) -> None:
        result = build_rule("permitted", "commission", "none", "adopt_acts",
                            ["use_cases(high_risk_ai_systems)"])
        assert result == (
            "permitted(commission, none, adopt_acts) :-\n"
            "    use_cases(high_risk_ai_systems)."
        )

    def test_rule_with_two_conditions(self) -> None:
        result = build_rule("obligated", "state", "citizen", "pay",
                            ["income(X_0), X_0 <= 138", "status(eligible)"])
        assert result == (
            "obligated(state, citizen, pay) :-\n"
            "    income(X_0), X_0 <= 138,\n"
            "    status(eligible)."
        )

    def test_patient_none_atom(self) -> None:
        result = build_rule("permitted", "municipality", "none", "organize_districts", [])
        assert result == "permitted(municipality, none, organize_districts)."
```

- [ ] **Step 2: Run to verify failure**

```bash
pytest tests/test_e3/test_translator.py::TestBuildRule -v
```

Expected: FAIL with `NotImplementedError`.

- [ ] **Step 3: Implement `build_rule`**

In `templates.py`, replace the `build_rule` stub:

```python
def build_rule(
    name: str,
    agent: str,
    patient: str,
    action: str,
    conditions: list[str],
) -> str:
    """Assemble a complete Clingo rule or ground fact."""
    head = f"{name}({agent}, {patient}, {action})"
    if not conditions:
        return f"{head}."
    body = ",\n    ".join(conditions)
    return f"{head} :-\n    {body}."
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
pytest tests/test_e3/test_translator.py::TestBuildRule -v
```

Expected: 4 PASSED.

- [ ] **Step 5: Run all templates tests so far**

```bash
pytest tests/test_e3/test_translator.py -v
```

Expected: all pass (9 normalize/modality + 9 condition + 4 build = 22 PASSED).

- [ ] **Step 6: Commit**

```bash
git add src/qfeng/c1_digestion/translation/templates.py tests/test_e3/test_translator.py
git commit -m "feat(e3): implement build_rule"
```

---

## Task 5: TDD `validate_syntax` + `atom_to_predicate`

**Files:**
- Modify: `src/qfeng/c1_digestion/translation/translator.py`
- Modify: `tests/test_e3/test_translator.py`

- [ ] **Step 1: Write failing tests**

Add to `tests/test_e3/test_translator.py`:

```python
from qfeng.c1_digestion.translation.translator import atom_to_predicate, validate_syntax
from qfeng.core.schemas import (
    DeonticAtom,
    DeonticCondition,
    DeonticModality,
    NormativeStrength,
)


class TestValidateSyntax:
    def test_valid_fact(self) -> None:
        assert validate_syntax("obligated(state, citizen, provide_healthcare).") is True

    def test_valid_rule_with_body(self) -> None:
        rule = "permitted(a, b, c) :-\n    use_cases(high_risk)."
        assert validate_syntax(rule) is True

    def test_invalid_syntax(self) -> None:
        assert validate_syntax("obligated(state, UNCLOSED") is False


class TestAtomToPredicate:
    def _make_atom(
        self,
        *,
        modality: DeonticModality = DeonticModality.OBLIGATION,
        agent: str = "state",
        patient: str = "citizen",
        action: str = "provide_healthcare",
        conditions: list[DeonticCondition] | None = None,
        strength: NormativeStrength = NormativeStrength.STATUTORY,
        atom_id: str = "abc123",
        chunk_id: str = "chunk456",
    ) -> DeonticAtom:
        return DeonticAtom(
            id=atom_id,
            source_chunk_id=chunk_id,
            modality=modality,
            agent=agent,
            patient=patient,
            action=action,
            conditions=conditions or [],
            strength=strength,
            confidence=0.9,
        )

    def test_obligation_no_conditions(self) -> None:
        atom = self._make_atom()
        pred = atom_to_predicate(atom)
        assert "obligated(state, citizen, provide_healthcare)." in pred.rule

    def test_obligation_with_gt_condition(self) -> None:
        atom = self._make_atom(
            conditions=[DeonticCondition(variable="count", operator=">", value="0")]
        )
        pred = atom_to_predicate(atom)
        assert "obligated(state, citizen, provide_healthcare) :-" in pred.rule
        assert "count(X_0), X_0 > 0" in pred.rule

    def test_faculty_maps_to_permitted(self) -> None:
        atom = self._make_atom(modality=DeonticModality.FACULTY)
        pred = atom_to_predicate(atom)
        assert "permitted(" in pred.rule

    def test_permission_with_eq_string_condition(self) -> None:
        atom = self._make_atom(
            modality=DeonticModality.PERMISSION,
            conditions=[DeonticCondition(variable="use_cases", operator="==",
                                         value="high_risk_ai_systems")],
        )
        pred = atom_to_predicate(atom)
        assert "permitted(" in pred.rule
        assert "use_cases(high_risk_ai_systems)" in pred.rule

    def test_prohibition(self) -> None:
        atom = self._make_atom(modality=DeonticModality.PROHIBITION)
        pred = atom_to_predicate(atom)
        assert "prohibited(" in pred.rule

    def test_patient_none_becomes_atom_none(self) -> None:
        atom = self._make_atom(patient="None")
        pred = atom_to_predicate(atom)
        assert ", none, " in pred.rule

    def test_multiple_conditions(self) -> None:
        atom = self._make_atom(conditions=[
            DeonticCondition(variable="rate", operator=">=", value="80"),
            DeonticCondition(variable="status", operator="==", value="active"),
        ])
        pred = atom_to_predicate(atom)
        assert "rate(X_0), X_0 >= 80" in pred.rule
        assert "status(active)" in pred.rule

    def test_traceability_comment_atom_id(self) -> None:
        atom = self._make_atom(atom_id="ea9646908e4d3ea2", chunk_id="003bd71d0f5d3a8c")
        pred = atom_to_predicate(atom)
        assert "% atom_id: ea9646908e4d3ea2" in pred.rule
        assert "chunk: 003bd71d0f5d3a8c" in pred.rule

    def test_strength_in_comment(self) -> None:
        atom = self._make_atom(strength=NormativeStrength.STATUTORY)
        pred = atom_to_predicate(atom)
        assert "strength: statutory" in pred.rule

    def test_syntax_valid_true_for_valid_atom(self) -> None:
        atom = self._make_atom()
        pred = atom_to_predicate(atom)
        assert pred.syntax_valid is True

    def test_source_atom_id_set(self) -> None:
        atom = self._make_atom(atom_id="myatom")
        pred = atom_to_predicate(atom)
        assert pred.source_atom_id == "myatom"
        assert pred.id == "myatom"

    def test_source_chunk_id_set(self) -> None:
        atom = self._make_atom(chunk_id="mychunk")
        pred = atom_to_predicate(atom)
        assert pred.source_chunk_id == "mychunk"
```

- [ ] **Step 2: Run to verify failure**

```bash
pytest tests/test_e3/test_translator.py::TestValidateSyntax tests/test_e3/test_translator.py::TestAtomToPredicate -v
```

Expected: FAIL with `NotImplementedError`.

- [ ] **Step 3: Implement `validate_syntax` and `atom_to_predicate`**

Replace the stubs in `translator.py`:

```python
"""E3 — DeonticAtom → ClingoPredicate translation."""
from __future__ import annotations

import clingo

from qfeng.c1_digestion.translation.templates import (
    build_rule,
    condition_to_clingo,
    modality_to_predicate_name,
    _normalize,
)
from qfeng.core.schemas import ClingoPredicate, DeonticAtom


def validate_syntax(rule: str) -> bool:
    """Return True if clingo parses the rule without error."""
    ctl = clingo.Control()
    try:
        ctl.add("base", [], rule)
        return True
    except RuntimeError:
        return False


def atom_to_predicate(atom: DeonticAtom) -> ClingoPredicate:
    """Transform a DeonticAtom into a ClingoPredicate with validated .lp rule."""
    name = modality_to_predicate_name(atom.modality)
    agent = _normalize(atom.agent)
    patient = "none" if atom.patient.strip().lower() == "none" else _normalize(atom.patient)
    action = _normalize(atom.action)

    clingo_conds = [condition_to_clingo(c, i) for i, c in enumerate(atom.conditions)]
    rule_body = build_rule(name, agent, patient, action, clingo_conds)

    comment = (
        f"% atom_id: {atom.id} | chunk: {atom.source_chunk_id}"
        f" | strength: {atom.strength}\n"
    )
    full_rule = comment + rule_body
    valid = validate_syntax(rule_body)

    return ClingoPredicate(
        id=atom.id,
        rule=full_rule,
        source_atom_id=atom.id,
        source_chunk_id=atom.source_chunk_id,
        syntax_valid=valid,
    )
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
pytest tests/test_e3/test_translator.py -v
```

Expected: all pass (22 templates + 3 validate_syntax + 12 atom_to_predicate = 37 PASSED).

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/translation/translator.py tests/test_e3/test_translator.py
git commit -m "feat(e3): implement validate_syntax and atom_to_predicate"
```

---

## Task 6: TDD `run_e3_batch` + `E3BatchResult`

**Files:**
- Modify: `src/qfeng/c1_digestion/translation/runner.py`
- Modify: `tests/test_e3/test_runner.py`

- [ ] **Step 1: Write failing tests**

Replace `tests/test_e3/test_runner.py` with:

```python
"""Integration tests for E3 runner — run_e3_batch."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from qfeng.c1_digestion.scope.config import ScopeConfig
from qfeng.c1_digestion.translation.runner import E3BatchResult, run_e3_batch
from qfeng.core.schemas import DeonticAtom, DeonticCondition, DeonticModality, NormativeStrength


# ── Fixtures ──────────────────────────────────────────────────────────


@pytest.fixture
def sample_atoms() -> list[DeonticAtom]:
    return [
        DeonticAtom(
            id="ea9646908e4d3ea2",
            source_chunk_id="003bd71d0f5d3a8c",
            modality=DeonticModality.FACULTY,
            agent="municipality",
            patient="None",
            action="organize_sus_in_districts",
            conditions=[],
            strength=NormativeStrength.STATUTORY,
            confidence=0.9,
        ),
        DeonticAtom(
            id="5b7194434043d835",
            source_chunk_id="0097db893574abbe",
            modality=DeonticModality.PERMISSION,
            agent="commission",
            patient="None",
            action="adopt_delegated_acts",
            conditions=[
                DeonticCondition(variable="use_cases", operator="==",
                                 value="high_risk_ai_systems"),
            ],
            strength=NormativeStrength.STATUTORY,
            confidence=0.92,
        ),
        DeonticAtom(
            id="cf1cf23cfc71002a",
            source_chunk_id="00915e1cbfff5699",
            modality=DeonticModality.OBLIGATION,
            agent="state_agency",
            patient="state_agency",
            action="provide_information",
            conditions=[
                DeonticCondition(variable="inconsistent_submissions", operator=">", value="0"),
            ],
            strength=NormativeStrength.REGULATORY,
            confidence=0.88,
        ),
    ]


@pytest.fixture
def runner_env(tmp_path: Path, sample_atoms: list[DeonticAtom]) -> dict:
    """Create a minimal E1+deontic_cache+concurrency_map environment."""
    # E1 scoped output — needed to build chunk_id → (regime, source) lookup
    e1_dir = tmp_path / "e1_chunks_scoped"
    brasil_dir = e1_dir / "brasil"
    brasil_dir.mkdir(parents=True)

    chunks_data = [
        {"id": "003bd71d0f5d3a8c", "source": "lei_8080_1990", "regime": "brasil",
         "hierarchy": ["Art. 1"], "text": "x", "language": "pt-BR",
         "effective_date": None, "cross_references": [], "chunk_type": "obligation"},
        {"id": "0097db893574abbe", "source": "lei_8080_1990", "regime": "brasil",
         "hierarchy": ["Art. 2"], "text": "y", "language": "pt-BR",
         "effective_date": None, "cross_references": [], "chunk_type": "obligation"},
        {"id": "00915e1cbfff5699", "source": "lei_8080_1990", "regime": "brasil",
         "hierarchy": ["Art. 3"], "text": "z", "language": "pt-BR",
         "effective_date": None, "cross_references": [], "chunk_type": "obligation"},
    ]
    (brasil_dir / "lei_8080_1990.json").write_text(
        json.dumps(chunks_data), encoding="utf-8"
    )

    # concurrency_map — one pair
    conc_map = {
        "003bd71d0f5d3a8c": ["0097db893574abbe"],
        "0097db893574abbe": ["003bd71d0f5d3a8c"],
    }
    conc_path = e1_dir / "concurrency_map.json"
    conc_path.write_text(json.dumps(conc_map), encoding="utf-8")

    # deontic_cache — one file per chunk
    deontic_dir = tmp_path / "deontic_cache"
    deontic_dir.mkdir()
    for atom in sample_atoms:
        cache_file = deontic_dir / f"{atom.source_chunk_id}.json"
        cache_file.write_text(
            json.dumps([atom.model_dump(mode="json")]), encoding="utf-8"
        )

    scope = ScopeConfig(
        name="test",
        description="test scope",
        regimes=["brasil"],
        documents={"brasil": ["lei_8080_1990*"]},
        chunk_types=["obligation"],
        hierarchy_depth=3,
        follow_cross_references=False,
        min_chunk_chars=40,
        strength_filter=None,
    )

    output_dir = tmp_path / "e3_predicates"

    return {
        "deontic_dir": deontic_dir,
        "output_dir": output_dir,
        "scope": scope,
        "conc_path": conc_path,
    }


# ── Tests ─────────────────────────────────────────────────────────────


class TestRunE3Batch:
    def test_three_atoms_generate_three_predicates(self, runner_env: dict) -> None:
        result = run_e3_batch(
            runner_env["deontic_dir"],
            runner_env["output_dir"],
            runner_env["scope"],
            runner_env["conc_path"],
        )
        assert result.total_atoms == 3
        assert result.total_predicates == 3

    def test_lp_file_created_for_regime(self, runner_env: dict) -> None:
        run_e3_batch(
            runner_env["deontic_dir"],
            runner_env["output_dir"],
            runner_env["scope"],
            runner_env["conc_path"],
        )
        lp_file = runner_env["output_dir"] / "brasil" / "lei_8080_1990.lp"
        assert lp_file.exists()
        content = lp_file.read_text(encoding="utf-8")
        assert "permitted(municipality, none, organize_sus_in_districts)." in content

    def test_concurrent_facts_file_created(self, runner_env: dict) -> None:
        result = run_e3_batch(
            runner_env["deontic_dir"],
            runner_env["output_dir"],
            runner_env["scope"],
            runner_env["conc_path"],
        )
        conc_lp = runner_env["output_dir"] / "concurrent_facts.lp"
        assert conc_lp.exists()
        assert result.concurrent_facts == 1
        content = conc_lp.read_text(encoding="utf-8")
        assert "concurrent(" in content

    def test_batch_result_counts(self, runner_env: dict) -> None:
        result = run_e3_batch(
            runner_env["deontic_dir"],
            runner_env["output_dir"],
            runner_env["scope"],
            runner_env["conc_path"],
        )
        assert result.syntax_valid + result.syntax_invalid == result.total_predicates
        assert result.predicates_per_regime.get("brasil", 0) == 3

    def test_syntax_invalid_atoms_included_with_warning(
        self, runner_env: dict, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from qfeng.c1_digestion.translation import translator as translator_mod
        monkeypatch.setattr(translator_mod, "validate_syntax", lambda _rule: False)
        result = run_e3_batch(
            runner_env["deontic_dir"],
            runner_env["output_dir"],
            runner_env["scope"],
            runner_env["conc_path"],
        )
        # Atoms still included, but all marked invalid
        assert result.total_predicates == 3
        assert result.syntax_invalid == 3
        assert len(result.warnings) > 0
```

- [ ] **Step 2: Run to verify failure**

```bash
pytest tests/test_e3/test_runner.py -v
```

Expected: FAIL with `NotImplementedError`.

- [ ] **Step 3: Implement `run_e3_batch`**

Replace the `run_e3_batch` stub in `runner.py`:

```python
"""E3 — Batch runner: deontic cache → Clingo .lp files."""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

from qfeng.c1_digestion.scope.config import ScopeConfig
from qfeng.c1_digestion.translation.translator import atom_to_predicate
from qfeng.core.schemas import ClingoPredicate, DeonticAtom

logger = logging.getLogger(__name__)


@dataclass
class E3BatchResult:
    total_atoms: int = 0
    total_predicates: int = 0
    syntax_valid: int = 0
    syntax_invalid: int = 0
    predicates_per_regime: dict[str, int] = field(default_factory=dict)
    concurrent_facts: int = 0
    warnings: list[str] = field(default_factory=list)


def _build_chunk_lookup(e1_dir: Path, scope: ScopeConfig) -> dict[str, tuple[str, str]]:
    """Return {chunk_id: (regime, source_stem)} from E1 output JSONs."""
    lookup: dict[str, tuple[str, str]] = {}
    for regime in scope.regimes:
        regime_dir = e1_dir / regime
        if not regime_dir.exists():
            continue
        for json_file in sorted(regime_dir.glob("*.json")):
            try:
                chunks = json.loads(json_file.read_text(encoding="utf-8"))
            except Exception as exc:
                logger.warning("Falha ao ler E1 JSON %s: %s", json_file.name, exc)
                continue
            for chunk in chunks:
                lookup[chunk["id"]] = (regime, json_file.stem)
    return lookup


def run_e3_batch(
    deontic_dir: Path,
    output_dir: Path,
    scope: ScopeConfig,
    concurrency_map_path: Path,
) -> E3BatchResult:
    """Translate all DeonticAtoms in the E2 cache to ClingoPredicates.

    Args:
        deontic_dir: outputs/deontic_cache/ — each file is {chunk_id}.json
        output_dir: outputs/e3_predicates/ — per-regime .lp files written here
        scope: ScopeConfig — only regimes in scope.regimes are processed
        concurrency_map_path: outputs/e1_chunks_scoped/concurrency_map.json
            The parent directory is used as the E1 output root for chunk lookup.
    """
    result = E3BatchResult()
    e1_dir = concurrency_map_path.parent

    # Build chunk_id → (regime, source_stem) lookup
    chunk_lookup = _build_chunk_lookup(e1_dir, scope)

    # Group predicates by (regime, source_stem) for .lp file output
    by_file: dict[tuple[str, str], list[ClingoPredicate]] = {}

    for cache_file in sorted(deontic_dir.glob("*.json")):
        try:
            raw_atoms = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception as exc:
            msg = f"Falha ao ler cache {cache_file.name}: {exc}"
            logger.warning(msg)
            result.warnings.append(msg)
            continue

        atoms = [DeonticAtom.model_validate(a) for a in raw_atoms]

        for atom in atoms:
            result.total_atoms += 1
            key = chunk_lookup.get(atom.source_chunk_id)
            if key is None:
                # chunk not in scope — skip
                continue
            regime, source_stem = key

            pred = atom_to_predicate(atom)
            result.total_predicates += 1
            if pred.syntax_valid:
                result.syntax_valid += 1
            else:
                result.syntax_invalid += 1
                msg = f"syntax_invalid: atom {atom.id} (chunk {atom.source_chunk_id})"
                logger.warning(msg)
                result.warnings.append(msg)

            result.predicates_per_regime[regime] = (
                result.predicates_per_regime.get(regime, 0) + 1
            )
            by_file.setdefault((regime, source_stem), []).append(pred)

    # Write per-regime .lp files
    output_dir.mkdir(parents=True, exist_ok=True)
    for (regime, source_stem), preds in sorted(by_file.items()):
        regime_dir = output_dir / regime
        regime_dir.mkdir(parents=True, exist_ok=True)
        lp_path = regime_dir / f"{source_stem}.lp"
        lp_path.write_text(
            "\n\n".join(p.rule for p in preds),
            encoding="utf-8",
        )
        logger.info("Escrito: %s (%d predicados)", lp_path, len(preds))

    # Write concurrent_facts.lp
    conc_map: dict[str, list[str]] = json.loads(
        concurrency_map_path.read_text(encoding="utf-8")
    )
    seen: set[frozenset[str]] = set()
    facts: list[str] = []
    for chunk_a, neighbors in conc_map.items():
        for chunk_b in neighbors:
            pair: frozenset[str] = frozenset({chunk_a, chunk_b})
            if pair not in seen:
                seen.add(pair)
                facts.append(f"concurrent({chunk_a}, {chunk_b}).")

    conc_lp = output_dir / "concurrent_facts.lp"
    header = "% concurrent_facts.lp — gerado do concurrency_map.json\n"
    conc_lp.write_text(header + "\n".join(facts), encoding="utf-8")
    result.concurrent_facts = len(facts)
    logger.info("concurrent_facts.lp: %d fatos", result.concurrent_facts)

    logger.info(
        "E3 batch: %d atoms → %d predicados | valid=%d invalid=%d | conc=%d",
        result.total_atoms, result.total_predicates,
        result.syntax_valid, result.syntax_invalid, result.concurrent_facts,
    )
    return result
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
pytest tests/test_e3/test_runner.py -v
```

Expected: 5 PASSED.

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/translation/runner.py tests/test_e3/test_runner.py
git commit -m "feat(e3): implement run_e3_batch and E3BatchResult"
```

---

## Task 7: TDD `test_syntax.py` + CLI `__main__.py`

**Files:**
- Modify: `tests/test_e3/test_syntax.py`
- Modify: `src/qfeng/c1_digestion/translation/__main__.py`

- [ ] **Step 1: Write `test_syntax.py`**

Replace `tests/test_e3/test_syntax.py` with:

```python
"""Tests for E3 validate_syntax — clingo 5.8.0 parse-level validation."""
from qfeng.c1_digestion.translation.translator import validate_syntax


class TestValidateSyntaxStandalone:
    def test_valid_obligation_rule(self) -> None:
        rule = "obligated(state, citizen, provide_healthcare)."
        assert validate_syntax(rule) is True

    def test_invalid_syntax_unclosed_paren(self) -> None:
        rule = "obligated(state, citizen, provide_healthcare"
        assert validate_syntax(rule) is False

    def test_rule_with_free_clingo_variable(self) -> None:
        rule = "obligated(state, citizen, provide_info) :-\n    count(X_0), X_0 > 0."
        assert validate_syntax(rule) is True
```

- [ ] **Step 2: Run test_syntax.py — expect PASS (already implemented)**

```bash
pytest tests/test_e3/test_syntax.py -v
```

Expected: 3 PASSED.

- [ ] **Step 3: Implement `__main__.py`**

Replace `__main__.py` with:

```python
"""E3 — CLI entry point.

Usage:
    python -m qfeng.c1_digestion.translation \\
        --deontic-dir outputs/deontic_cache/ \\
        --scope configs/sus_validacao.yaml \\
        --concurrency-map outputs/e1_chunks_scoped/concurrency_map.json \\
        --output-dir outputs/e3_predicates/
"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path

from qfeng.c1_digestion.scope.config import load_scope
from qfeng.c1_digestion.translation.runner import run_e3_batch

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="E3 — Traduz DeonticAtoms do cache E2 em ClingoPredicates (.lp)"
    )
    parser.add_argument(
        "--deontic-dir",
        type=Path,
        default=Path("outputs/deontic_cache"),
        help="Diretório do cache E2 (default: outputs/deontic_cache/)",
    )
    parser.add_argument(
        "--scope",
        type=Path,
        required=True,
        help="Perfil YAML de escopo (ex: configs/sus_validacao.yaml)",
    )
    parser.add_argument(
        "--concurrency-map",
        type=Path,
        default=Path("outputs/e1_chunks_scoped/concurrency_map.json"),
        help="Mapa de concorrências E1 (default: outputs/e1_chunks_scoped/concurrency_map.json)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/e3_predicates"),
        help="Diretório de saída para arquivos .lp (default: outputs/e3_predicates/)",
    )
    args = parser.parse_args()

    scope = load_scope(args.scope)
    result = run_e3_batch(
        deontic_dir=args.deontic_dir,
        output_dir=args.output_dir,
        scope=scope,
        concurrency_map_path=args.concurrency_map,
    )

    logger.info("E3 concluído:")
    logger.info("  atoms processados:  %d", result.total_atoms)
    logger.info("  predicados gerados: %d", result.total_predicates)
    logger.info("  syntax_valid:       %d", result.syntax_valid)
    logger.info("  syntax_invalid:     %d", result.syntax_invalid)
    logger.info("  concurrent_facts:   %d", result.concurrent_facts)
    if result.warnings:
        logger.warning("  avisos: %d", len(result.warnings))
    for regime, count in sorted(result.predicates_per_regime.items()):
        logger.info("  %s: %d predicados", regime, count)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Test CLI help runs without error**

```bash
conda activate qfeng && python -m qfeng.c1_digestion.translation --help
```

Expected: prints usage with `--deontic-dir`, `--scope`, `--concurrency-map`, `--output-dir`.

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/translation/__main__.py tests/test_e3/test_syntax.py
git commit -m "feat(e3): add CLI __main__.py and test_syntax.py"
```

---

## Task 8: Phase A — Full Validation (pytest + ruff + mypy)

**Files:** No new files — validation only.

- [ ] **Step 1: Run full test suite**

```bash
conda activate qfeng && pytest tests/test_e3/ -v
```

Expected: all pass. Count should be approximately:
- `test_translator.py`: ~37 tests (9 normalize/modality + 9 condition + 4 build + 3 validate_syntax + 12 atom_to_predicate)
- `test_runner.py`: 5 tests
- `test_syntax.py`: 3 tests

- [ ] **Step 2: Run regression — full test suite**

```bash
pytest tests/ -v --tb=short
```

Expected: all 152+ tests still pass (E0/E1/E2 + new E3).

- [ ] **Step 3: Run ruff on translation module**

```bash
ruff check src/qfeng/c1_digestion/translation/
```

Expected: no errors. If issues found, fix them before proceeding.

- [ ] **Step 4: Run mypy on translation module**

```bash
mypy src/qfeng/c1_digestion/translation/ --strict
```

Expected: no errors. Common fixes needed:
- Add `-> None` return types on any function missing them
- Add `from __future__ import annotations` if missing
- Ensure no `Any` without explicit type ignore comments

- [ ] **Step 5: Fix any ruff/mypy issues found and re-run**

After fixing, confirm both pass clean:

```bash
ruff check src/qfeng/c1_digestion/translation/ && mypy src/qfeng/c1_digestion/translation/ --strict
```

Expected: `All checks passed.` / `Success: no issues found`.

- [ ] **Step 6: Commit Phase A completion**

```bash
git add -u
git commit -m "feat(e3): Phase A complete — all tests pass, ruff+mypy clean"
```

---

## Self-Review Checklist (done before saving this plan)

**Spec coverage:**
- ✅ Sec 3 file structure — all files accounted for
- ✅ Sec 4.1 templates API — `modality_to_predicate_name`, `condition_to_clingo`, `build_rule`
- ✅ Sec 4.2 translator — `atom_to_predicate`
- ✅ Sec 4.3 runner — `run_e3_batch` with all 4 params
- ✅ Sec 4.4 `E3BatchResult` — all 7 fields present
- ✅ Sec 5 templates — all 4 modality cases covered, concurrent_facts format
- ✅ Sec 6 condition translation — all 7 operators in tests
- ✅ Sec 7 syntax validation — `clingo.Control().add()` + `syntax_valid=False` doesn't block batch
- ✅ Sec 8 regime filter — via chunk_lookup from E1 output JSONs
- ✅ Sec 9 test cases — 12 atom_to_predicate + 5 runner + 3 syntax = 20 spec cases covered
- ✅ Sec 10 Phase A commands — ruff + mypy + pytest in Task 8
- ✅ `__init__.py` exports — `atom_to_predicate`, `validate_syntax`, `run_e3_batch`, `E3BatchResult`

**Type consistency:**
- `condition_to_clingo(cond: DeonticCondition, idx: int)` — used consistently as `[condition_to_clingo(c, i) for i, c in enumerate(atom.conditions)]`
- `E3BatchResult` fields match across runner.py stub → implementation → test assertions
- `ClingoPredicate` fields (`id`, `rule`, `source_atom_id`, `source_chunk_id`, `syntax_valid`) — all set in `atom_to_predicate`
