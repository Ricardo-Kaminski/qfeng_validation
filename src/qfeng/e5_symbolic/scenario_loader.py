"""Clingo scenario loader for E5 Symbolic Testing.

Uses the Clingo Python API (binary not on PATH).
Runs twice per scenario:
  1. Full program (with constraints) → SAT/UNSAT
  2. Relaxed program (constraints stripped) → active sovereign/elastic atoms
     (needed to populate psi_S even when full program is UNSAT)
"""

from __future__ import annotations

import pathlib
import re

import clingo

CORPUS_DIR = pathlib.Path("C:/Workspace/academico/qfeng_validacao/corpora_clingo")

# ── Registry of scenarios ─────────────────────────────────────────

SCENARIO_REGISTRY: dict[str, dict] = {
    "C2": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/saude/sus_direito_saude.lp",
            "brasil/emergencia_manaus/emergencia_sanitaria.lp",
        ],
        "facts": "scenarios/c2_manaus_facts.lp",
        "expected": "UNSAT",
        "regime": "brasil",
        "domain": "saude",
        "predictor_type": "TimeSeries",
        "n_observations": 1526,
        "data_source": "real_primary",
        "outcome_description": "Colapso hospitalar Manaus jan/2021 — O2 crítico",
        # Obrigacoes de insumos criticos (Lei 8.080/1990 Art. 15; CF/88 Art. 196)
        # existiam mas a cadeia institucional de distribuicao de O2 nao estava
        # constituida como agenciamento sociotecnico operante — predicado existe,
        # canal ausente. (Portaria GM/MS 69/2021 = registro de vacinas; nao usar
        # como ancora para obrigacao de insumos hospitalares.)
        "failure_type": "execution_absent_channel",
    },
    "C3": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/saude/sus_direito_saude.lp",
        ],
        "facts": "scenarios/c3_concentracao_facts.lp",
        "expected": "UNSAT",
        "regime": "brasil",
        "domain": "saude",
        "predictor_type": "LightGBM",
        "n_observations": 27,
        "data_source": "real_normative",
        "outcome_description": "Concentração regional SUS viola equidade constitucional",
        # O predicado de equidade (obligation_to_reduce_regional_inequality) está
        # ausente do Sistema 5 do modelo de alocação — nenhum sinal algédônico
        # pode ser gerado mesmo com dados disponíveis.
        "failure_type": "constitutional",
    },
    "C7": {
        "corpus": [
            "usa/civil_rights/civil_rights_14th.lp",
            "usa/medicaid/medicaid_access.lp",
        ],
        "facts": "scenarios/c7_obermeyer_facts.lp",
        "expected": "UNSAT",
        "regime": "usa",
        "domain": "saude",
        "predictor_type": "Statistical",
        "n_observations": 48784,
        "data_source": "real_primary",
        "outcome_description": "Bias racial Obermeyer 2019 — gap 34pp sub-representação",
        # prohibition_disparate_impact nunca foi inscrito no Sistema 5 do
        # algoritmo de alocação de risco — ausência constitucional pré-implantação.
        "failure_type": "constitutional",
    },
    "T-CLT-01": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
            "brasil/processual/cpc_fundamentacao.lp",
        ],
        "facts": "scenarios/t_clt_01_facts.lp",
        "expected": "UNSAT",
        "regime": "brasil",
        "domain": "trabalhista",
        "predictor_type": "ASP",
        "n_observations": 1,
        "data_source": "real_normative",
        "outcome_description": "Citação fantasma Mata v. Avianca — precedente inexistente",
        # obligation_to_ground_decision existe no corpus (CPC 489), mas o LLM
        # não consultou a cadeia de precedentes antes de gerar a citação —
        # inércia epistêmica: predicado existe, actante não respondeu.
        "failure_type": "execution_inertia",
    },
    "T-CLT-02": {
        "corpus": [
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        ],
        "facts": "scenarios/t_clt_02_facts.lp",
        "expected": "UNSAT",
        "regime": "brasil",
        "domain": "trabalhista",
        "predictor_type": "ASP",
        "n_observations": 1,
        "data_source": "real_normative",
        "outcome_description": "Banco de horas 8 meses sem CCT — Súmula TST 85 distorcida",
        # Requisito soberano (CCT para banco > 6 meses) estruturalmente ausente
        # da configuração contratual — falha constitucional antes da implantação.
        "failure_type": "constitutional",
    },
    "T-CLT-03": {
        "corpus": [
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        ],
        "facts": "scenarios/t_clt_03_facts.lp",
        "expected": "SAT",
        "regime": "brasil",
        "domain": "trabalhista",
        "predictor_type": "ASP",
        "n_observations": 1,
        "data_source": "real_normative",
        "outcome_description": "Banco de horas 10 meses com CCT — caso correto (STAC)",
        # SAT — sem falha: todos os predicados soberanos satisfeitos pela CCT válida.
        "failure_type": None,
    },
    "T-CLT-04": {
        "corpus": [
            "brasil/constitucional/cf88_principios_fundamentais.lp",
            "brasil/trabalhista/clt_direitos_trabalhistas.lp",
            "brasil/processual/cpc_fundamentacao.lp",
        ],
        "facts": "scenarios/t_clt_04_facts.lp",
        "expected": "SAT",
        "regime": "brasil",
        "domain": "trabalhista",
        "predictor_type": "ASP",
        "n_observations": 1,
        "data_source": "real_normative",
        "outcome_description": "Citação fundamentada TST-RR-000200-50.2019 — controle positivo (STAC)",
        # SAT — controle positivo para T-CLT-01: mesma obrigação de fundamentação,
        # precedente real verificado → constraint não dispara.
        "failure_type": None,
    },
}


# ── Clingo execution helpers ──────────────────────────────────────


def _load_combined(files: list[pathlib.Path]) -> str:
    return "\n".join(p.read_text(encoding="utf-8") for p in files)


def _strip_constraints(src: str) -> str:
    """Remove integrity constraints (:- body.) to get relaxed program.

    Handles multi-line constraints: once a line starts with ':-' (integrity
    constraint, no head), all continuation lines until the closing '.' are
    also commented out.
    """
    lines = []
    in_constraint = False
    for line in src.splitlines():
        stripped = line.strip()
        # Detect start of integrity constraint (no head before :-)
        if not in_constraint and stripped.startswith(":-"):
            in_constraint = True
        if in_constraint:
            lines.append(f"% [relaxed] {line}")
            # Constraint ends when the line contains a terminating period
            # (not inside a string — simple heuristic sufficient for our corpus)
            code_part = stripped.split("%")[0]  # strip inline comments
            if code_part.rstrip().endswith("."):
                in_constraint = False
        else:
            lines.append(line)
    return "\n".join(lines)


def _extract_atoms(model: clingo.Model, prefix: str) -> list[str]:
    atoms = []
    for atom in model.symbols(shown=True):
        name = str(atom)
        if name.startswith(prefix):
            atoms.append(name)
    return atoms


def run_scenario(scenario_id: str) -> dict:
    """Run a scenario and return full results dict.

    Returns:
        satisfiable: bool
        active_sovereign: list[str]   — from relaxed run
        active_elastic:  list[str]    — from relaxed run
        n_sovereign_active: int
        n_elastic_active:   int
    """
    cfg = SCENARIO_REGISTRY[scenario_id]
    corpus_paths = [CORPUS_DIR / f for f in cfg["corpus"]]
    facts_path = CORPUS_DIR / cfg["facts"]

    all_files = corpus_paths + [facts_path]
    src = _load_combined(all_files)

    # 1. Full run — get SAT/UNSAT
    ctl_full = clingo.Control(["--models=0"])
    ctl_full.add("base", [], src)
    ctl_full.ground([("base", [])])
    result_full = ctl_full.solve()
    satisfiable = bool(result_full.satisfiable)

    # 2. Relaxed run — get active atoms even when UNSAT
    src_relaxed = _strip_constraints(src)
    ctl_relax = clingo.Control(["--models=1"])
    ctl_relax.add("base", [], src_relaxed)
    ctl_relax.ground([("base", [])])

    active_sovereign: list[str] = []
    active_elastic: list[str] = []

    with ctl_relax.solve(yield_=True) as handle:
        for model in handle:
            active_sovereign = _extract_atoms(model, "sovereign(")
            active_elastic = _extract_atoms(model, "elastic(")
            break

    return {
        "satisfiable": satisfiable,
        "active_sovereign": active_sovereign,
        "active_elastic": active_elastic,
        "n_sovereign_active": len(active_sovereign),
        "n_elastic_active": len(active_elastic),
    }


def run_scenario_with_occupancy(scenario_id: str, occupancy_pct: int) -> dict:
    """Run scenario with dynamically injected hospital_occupancy_rate_pct.

    Replaces the hard-coded occupancy fact in the facts file with the
    provided value. Used to implement time-varying psi_S across the 12-month
    Manaus series: CB emerges naturally when occupancy exceeds the 85% threshold
    defined in emergencia_sanitaria.lp, without manual weight calibration.
    """
    cfg = SCENARIO_REGISTRY[scenario_id]
    corpus_paths = [CORPUS_DIR / f for f in cfg["corpus"]]
    facts_path = CORPUS_DIR / cfg["facts"]

    facts_src = facts_path.read_text(encoding="utf-8")
    facts_src = re.sub(
        r"hospital_occupancy_rate_pct\(\d+\)\.",
        f"hospital_occupancy_rate_pct({occupancy_pct}).",
        facts_src,
    )

    corpus_src = "\n".join(p.read_text(encoding="utf-8") for p in corpus_paths)
    src = corpus_src + "\n" + facts_src

    ctl_full = clingo.Control(["--models=0"])
    ctl_full.add("base", [], src)
    ctl_full.ground([("base", [])])
    satisfiable = bool(ctl_full.solve().satisfiable)

    src_relaxed = _strip_constraints(src)
    ctl_relax = clingo.Control(["--models=1"])
    ctl_relax.add("base", [], src_relaxed)
    ctl_relax.ground([("base", [])])

    active_sovereign: list[str] = []
    active_elastic: list[str] = []
    with ctl_relax.solve(yield_=True) as handle:
        for model in handle:
            active_sovereign = _extract_atoms(model, "sovereign(")
            active_elastic = _extract_atoms(model, "elastic(")
            break

    return {
        "satisfiable": satisfiable,
        "active_sovereign": active_sovereign,
        "active_elastic": active_elastic,
        "n_sovereign_active": len(active_sovereign),
        "n_elastic_active": len(active_elastic),
    }
