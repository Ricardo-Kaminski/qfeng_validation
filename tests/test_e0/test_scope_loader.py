"""Testes para ScopeConfig e load_scope."""

from typing import TypedDict

import pytest

from qfeng.c1_digestion.scope.config import ScopeConfig


class _ScopeKwargs(TypedDict):
    name: str
    description: str
    regimes: list[str]
    documents: dict[str, list[str]]
    chunk_types: list[str]
    hierarchy_depth: int
    follow_cross_references: bool
    min_chunk_chars: int
    strength_filter: list[str] | None


def _valid_kwargs() -> _ScopeKwargs:
    return _ScopeKwargs(
        name="test_scope",
        description="Scope de teste",
        regimes=["brasil", "eu"],
        documents={"brasil": ["lei_8080*"], "eu": ["eu_ai_act*"]},
        chunk_types=["obligation", "principle"],
        hierarchy_depth=3,
        follow_cross_references=False,
        min_chunk_chars=40,
        strength_filter=None,
    )


class TestScopeConfigValidation:
    def test_valid_scope_creates_without_error(self) -> None:
        scope = ScopeConfig(**_valid_kwargs())
        assert scope.name == "test_scope"
        assert scope.hierarchy_depth == 3

    def test_unknown_regime_raises_value_error(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["regimes"] = ["brasil", "jupiter"]
        with pytest.raises(ValueError, match="Regimes desconhecidos"):
            ScopeConfig(**kwargs)

    def test_error_message_includes_scope_name(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["regimes"] = ["marte"]
        with pytest.raises(ValueError, match="test_scope"):
            ScopeConfig(**kwargs)

    def test_hierarchy_depth_zero_raises(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 0
        with pytest.raises(ValueError, match="hierarchy_depth"):
            ScopeConfig(**kwargs)

    def test_hierarchy_depth_five_raises(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 5
        with pytest.raises(ValueError, match="hierarchy_depth"):
            ScopeConfig(**kwargs)

    def test_hierarchy_depth_one_is_valid(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 1
        scope = ScopeConfig(**kwargs)
        assert scope.hierarchy_depth == 1

    def test_hierarchy_depth_four_is_valid(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 4
        scope = ScopeConfig(**kwargs)
        assert scope.hierarchy_depth == 4

    def test_negative_min_chunk_chars_raises(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["min_chunk_chars"] = -1
        with pytest.raises(ValueError, match="min_chunk_chars"):
            ScopeConfig(**kwargs)

    def test_zero_min_chunk_chars_is_valid(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["min_chunk_chars"] = 0
        scope = ScopeConfig(**kwargs)
        assert scope.min_chunk_chars == 0

    def test_all_three_regimes_valid(self) -> None:
        kwargs = _valid_kwargs()
        kwargs["regimes"] = ["brasil", "eu", "usa"]
        scope = ScopeConfig(**kwargs)
        assert len(scope.regimes) == 3
