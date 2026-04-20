"""C1 — Normative Digestion Pipeline.

Transforms raw normative documents (laws, regulations, protocols)
into executable Clingo/dPASP predicates through five stages:

E1: Ingestion & structural parsing
E2: LLM-powered deontic extraction
E3: Symbolic translation (DeonticAtom → Clingo)
E4: HITL validation & sovereignty classification
E5: Symbolic unit testing
"""
