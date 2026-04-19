"""E3 — Clingo rule templates and condition translation."""
from __future__ import annotations

import re
import unicodedata

from qfeng.core.schemas import DeonticCondition, DeonticModality

_PREDICATE_NAME: dict[DeonticModality, str] = {
    DeonticModality.OBLIGATION:  "obligated",
    DeonticModality.PROHIBITION: "prohibited",
    DeonticModality.PERMISSION:  "permitted",
    DeonticModality.FACULTY:     "permitted",
}


def _normalize(s: str) -> str:
    """Normalize ASCII string to Clingo-safe snake_case atom."""
    return s.lower().replace("-", "_").replace(" ", "_")


def sanitize_clingo_id(s: str) -> str:
    """Convert any string to a valid Clingo lowercase atom identifier.

    Handles PT-BR/EN diacritics (ã→a, ç→c, é→e, ú→u …), apostrophes,
    brackets, and other special chars. Truncates to 60 chars.
    Result always starts with a letter.
    """
    # Transliterate: NFKD decomposes accented chars → strip combining marks
    nfkd = unicodedata.normalize("NFKD", str(s))
    s2 = nfkd.encode("ascii", "ignore").decode("ascii")
    # lowercase + replace common delimiters with underscore
    s2 = s2.lower().replace("-", "_").replace(" ", "_")
    # remove anything not alphanumeric or underscore
    s2 = re.sub(r"[^a-z0-9_]", "", s2)
    # collapse multiple underscores and strip from ends
    s2 = re.sub(r"_+", "_", s2).strip("_")
    # Clingo atoms can't start with a digit
    if s2 and s2[0].isdigit():
        s2 = "n" + s2
    # truncate
    s2 = s2[:60].rstrip("_")
    return s2 or "unknown"


def modality_to_predicate_name(modality: DeonticModality) -> str:
    return _PREDICATE_NAME[modality]


def _extract_numeric(v: str) -> str | None:
    """Extract leading int/float from strings like '80%', '138%FPL', '2.5 anos'."""
    m = re.match(r"^(-?\d+(?:\.\d+)?)", v.strip())
    return m.group(1) if m else None


def condition_to_clingo(cond: DeonticCondition, idx: int) -> str:
    """Translate a DeonticCondition to Clingo literal(s).

    ==  + string  : variable(value)
    ==  + numeric : variable(N)          e.g. count(5)
    ==  + 'not X' : not variable(X)      negation-as-failure
    >/</>=/<=/ != : variable(X_i), X_i op N   (numeric extracted from value)
    """
    var = sanitize_clingo_id(cond.variable)
    op = cond.operator
    val = cond.value.strip()

    # Fix #3 — negation: value like "not active" with == operator
    if op == "==" and val.lower().startswith("not "):
        pos_val = sanitize_clingo_id(val[4:].strip())
        return f"not {var}({pos_val})"

    if op == "==":
        num = _extract_numeric(val)
        # purely numeric: "5", "42", "3.14"
        if num is not None and re.fullmatch(r"-?\d+(?:\.\d+)?", val):
            return f"{var}({num})"
        return f"{var}({sanitize_clingo_id(val)})"

    # Fix #2 — comparison ops: always use arithmetic variable form
    # Extract numeric part from values like "80%", "138%FPL", "2 anos"
    x = f"X_{idx}"
    num = _extract_numeric(val)
    if num is not None:
        return f"{var}({x}), {x} {op} {num}"
    # Non-numeric value with comparison op: fall back to ground predicate
    return f"{var}({sanitize_clingo_id(val)})"


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
