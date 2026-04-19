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

    conc_map = {
        "003bd71d0f5d3a8c": ["0097db893574abbe"],
        "0097db893574abbe": ["003bd71d0f5d3a8c"],
    }
    conc_path = e1_dir / "concurrency_map.json"
    conc_path.write_text(json.dumps(conc_map), encoding="utf-8")

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
        assert result.total_predicates == 3
        assert result.syntax_invalid == 3
        assert len(result.warnings) > 0
