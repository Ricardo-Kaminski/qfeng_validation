"""E3 — Translation: DeonticAtom → Clingo/dPASP predicates."""
from qfeng.c1_digestion.translation.runner import E3BatchResult, run_e3_batch
from qfeng.c1_digestion.translation.translator import atom_to_predicate, validate_syntax

__all__ = ["atom_to_predicate", "validate_syntax", "run_e3_batch", "E3BatchResult"]
