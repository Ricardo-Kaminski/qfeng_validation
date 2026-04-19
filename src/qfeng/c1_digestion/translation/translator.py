"""E3 — DeonticAtom → ClingoPredicate translation."""
from __future__ import annotations

import clingo

from qfeng.c1_digestion.translation.templates import (
    _normalize,
    build_rule,
    condition_to_clingo,
    modality_to_predicate_name,
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
