"""E3 — DeonticAtom → ClingoPredicate translation."""
from __future__ import annotations

from qfeng.core.schemas import ClingoPredicate, DeonticAtom


def validate_syntax(rule: str) -> bool:
    raise NotImplementedError


def atom_to_predicate(atom: DeonticAtom) -> ClingoPredicate:
    raise NotImplementedError
