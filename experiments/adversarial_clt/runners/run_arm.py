"""Runner atômico: executa um (braço, modelo, cenário, run) e persiste o resultado."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Any

import numpy as np
import ollama
import yaml

# Q-FENG motor imports para braço B5
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))
from qfeng.core.interference import (  # noqa: E402
    CircuitBreakerConfig,
    compute_interference,
)
from qfeng.e5_symbolic.psi_builder import build_psi_n, build_psi_s  # noqa: E402

# Métricas runtime do motor Q-FENG (populadas em _build_prompt para B5, lidas em run_arm)
_qfeng_b5_metrics: dict = {}

EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = EXPERIMENT_ROOT / "results" / "raw_responses"
PROMPTS_DIR = EXPERIMENT_ROOT / "prompts"
SCENARIOS_FILE = EXPERIMENT_ROOT / "scenarios" / "scenarios.yaml"
GROUND_TRUTH_FILE = EXPERIMENT_ROOT / "scenarios" / "ground_truth_predicates.json"

VALID_BRACOS = ("B1", "B2", "B3", "B4", "B5")
VALID_MODELOS = ("qwen3:14b", "phi4:14b", "gemma3:12b", "llama3.1:8b")


def _load_scenario(scenario_id: str) -> dict[str, Any]:
    with open(SCENARIOS_FILE, encoding="utf-8") as f:
        scenarios = yaml.safe_load(f)
    for s in scenarios["scenarios"]:
        if s["scenario_id"] == scenario_id:
            return s
    raise ValueError(f"Cenário não encontrado: {scenario_id}")


def _load_ground_truth(scenario_id: str) -> dict[str, Any]:
    with open(GROUND_TRUTH_FILE, encoding="utf-8") as f:
        gt_data = json.load(f)
    result = gt_data.get("by_scenario", {}).get(scenario_id)
    if result is None:
        raise ValueError(f"Ground truth não encontrado: {scenario_id}")
    return result


def _load_prompt_template(braco: str) -> dict[str, Any]:
    path = PROMPTS_DIR / f"{braco}_*.yaml"
    matches = list(PROMPTS_DIR.glob(f"{braco}_*.yaml"))
    if not matches:
        raise FileNotFoundError(f"Template de prompt não encontrado para braço {braco}")
    with open(matches[0], encoding="utf-8") as f:
        return yaml.safe_load(f)


def _run_clingo_for_scenario(scenario_id: str) -> dict[str, Any]:
    """Executa Clingo via scenario_loader e retorna resultado simbólico."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))
    from qfeng.e5_symbolic.scenario_loader import run_scenario
    scenario = _load_scenario(scenario_id)
    clingo_id = scenario.get("clingo_anchor", scenario_id)
    return run_scenario(clingo_id)


def _load_normative_corpus(scenario_id: str) -> str:
    """Carrega texto normativo relevante para RAG baseline (B2)."""
    gt = _load_ground_truth(scenario_id)
    category = gt.get("category", "")
    corpus_lines: list[str] = []

    clt_path = Path(__file__).resolve().parents[4] / "corpora_clingo" / "brasil" / "trabalhista" / "clt_direitos_trabalhistas.lp"
    if clt_path.exists():
        with open(clt_path, encoding="utf-8") as f:
            # Extrai comentários como texto normativo legível
            for line in f:
                if line.startswith("% ") and len(line) > 3:
                    corpus_lines.append(line[2:].strip())

    return "\n".join(corpus_lines[:80])  # Limita para não explodir context window


def _build_prompt(braco: str, scenario: dict, gt: dict, clingo_result: dict | None, template: dict) -> str:
    """Monta o prompt completo substituindo variáveis do template."""
    scenario_text = scenario["scenario_text"]
    user_tpl: str = template["user_template"]

    if braco == "B1":
        return user_tpl.format(scenario_text=scenario_text)

    if braco == "B2":
        normative_corpus = _load_normative_corpus(scenario["scenario_id"])
        return user_tpl.format(scenario_text=scenario_text, normative_corpus=normative_corpus)

    if braco == "B3":
        # Predicados como texto sem execução Clingo — listagem dos predicados do GT
        predicate_list = "\n".join(
            f"- {p}" for p in gt.get("violated_predicates", []) + gt.get("compliance_predicates", [])
        )
        return user_tpl.format(scenario_text=scenario_text, predicate_list=predicate_list)

    if braco == "B4":
        assert clingo_result is not None, "B4 requer execução Clingo"
        import math
        active_sovereign = clingo_result.get("active_sovereign", [])
        active_elastic = clingo_result.get("active_elastic", [])
        satisfiability = clingo_result.get("satisfiability", "UNKNOWN")
        n_s = len(active_sovereign)
        n_e = len(active_elastic)
        # ψ_S simplificado: fração de predicados sovereign ativos × π
        psi_s = round(n_s / max(n_s + n_e, 1) * math.pi, 4) if (n_s + n_e) > 0 else 0.0
        qfeng_action = gt.get("correct_decision", "see_clingo_output")
        return user_tpl.format(
            scenario_text=scenario_text,
            satisfiability=satisfiability,
            active_sovereign=", ".join(active_sovereign) or "nenhum",
            active_elastic=", ".join(active_elastic) or "nenhum",
            psi_s_vector=f"[{psi_s}]",
            qfeng_action=qfeng_action,
        )

    if braco == "B5":
        assert clingo_result is not None, "B5 requer execução Clingo"

        global _qfeng_b5_metrics
        _qfeng_b5_metrics = {}

        # Mapear scenario_id → chave do psi_builder via clingo_anchor
        # (T-CLT-01-001 → clingo_anchor="T-CLT-01"; T-CTRL-NEG-001 → clingo_anchor="T-CLT-01")
        psi_base_id = scenario.get("clingo_anchor", scenario["scenario_id"])

        t0 = time.monotonic()
        psi_n = build_psi_n(psi_base_id)
        active_sovereign = clingo_result.get("active_sovereign", [])
        active_elastic = clingo_result.get("active_elastic", [])
        psi_s = build_psi_s(psi_base_id, active_sovereign=active_sovereign, active_elastic=active_elastic)
        t_psi_build_ms = int((time.monotonic() - t0) * 1000)

        t1 = time.monotonic()
        cb_config = CircuitBreakerConfig()  # canônico: theta_stac=π/3=60°, theta_block=2π/3=120°
        motor = compute_interference(
            psi_n=psi_n,
            psi_s=psi_s,
            alpha_sq=0.5,
            beta_sq=0.5,
            cb_config=cb_config,
            theta_history=None,  # stateless por cenário em adversarial CLT
            gamma=0.0,
        )
        t_theta_compute_ms = int((time.monotonic() - t1) * 1000)

        regime_str = str(motor.decision).upper()  # "STAC" | "HITL" | "BLOCK"
        theta_eff_val = motor.theta_eff if motor.theta_eff is not None else motor.theta

        _qfeng_b5_metrics.update({
            "psi_n_dim": int(len(psi_n)),
            "psi_s_dim": int(len(psi_s)),
            "theta_rad": float(motor.theta),
            "theta_deg": float(motor.theta_degrees),
            "theta_eff_rad": float(theta_eff_val),
            "theta_eff_deg": float(np.degrees(theta_eff_val)),
            "regime": regime_str,
            "p_action": float(motor.p_action),
            "cos_theta": float(motor.cos_theta),
            "cb_threshold_deg": float(np.degrees(cb_config.theta_block)),
            "t_psi_build_ms": t_psi_build_ms,
            "t_theta_compute_ms": t_theta_compute_ms,
        })

        satisfiability = clingo_result.get("satisfiability", "UNKNOWN")
        qfeng_action = gt.get("correct_decision", "see_clingo_output")

        return user_tpl.format(
            scenario_text=scenario_text,
            satisfiability=satisfiability,
            active_sovereign=", ".join(active_sovereign) or "nenhum",
            active_elastic=", ".join(active_elastic) or "nenhum",
            theta_deg=f"{motor.theta_degrees:.2f}",
            regime=regime_str,
            p_action=f"{motor.p_action:.4f}",
            cos_theta=f"{motor.cos_theta:.4f}",
            qfeng_action=qfeng_action,
        )

    raise ValueError(f"Braço inválido: {braco}")


def _sha256_job(full_prompt: str, system_prompt: str, modelo: str, seed: int) -> str:
    payload = json.dumps({"system": system_prompt, "user": full_prompt, "model": modelo, "seed": seed}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def run_arm(
    braco: str,
    modelo: str,
    scenario_id: str,
    run_id: int,
    seed: int,
    *,
    force: bool = False,
) -> dict[str, Any]:
    """Executa um (braço, modelo, cenário, run).

    Retorna o dict de resposta. Reutiliza arquivo existente a menos que force=True.
    """
    if braco not in VALID_BRACOS:
        raise ValueError(f"Braço inválido: {braco}. Válidos: {VALID_BRACOS}")

    scenario = _load_scenario(scenario_id)
    gt = _load_ground_truth(scenario_id)
    template = _load_prompt_template(braco)

    global _qfeng_b5_metrics
    _qfeng_b5_metrics = {}

    t_start = time.monotonic()
    t_clingo_ms: int | None = None
    t_llm_ms: int | None = None

    clingo_result: dict | None = None
    if braco in ("B3", "B4", "B5"):
        t0 = time.monotonic()
        clingo_result = _run_clingo_for_scenario(scenario_id)
        if braco in ("B4", "B5"):
            t_clingo_ms = int((time.monotonic() - t0) * 1000)

    system_prompt: str = template["system"]
    user_prompt = _build_prompt(braco, scenario, gt, clingo_result, template)
    temperature: float = template.get("temperature", 0.3)

    sha = _sha256_job(user_prompt, system_prompt, modelo, seed)
    out_path = RAW_DIR / f"{sha}.json"

    if out_path.exists() and not force:
        with open(out_path, encoding="utf-8") as f:
            return json.load(f)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    t0 = time.monotonic()
    try:
        response = ollama.chat(
            model=modelo,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            options={"temperature": temperature, "seed": seed},
        )
        t_llm_ms = int((time.monotonic() - t0) * 1000)
        latency_ms = int((time.monotonic() - t_start) * 1000)
        response_text = response["message"]["content"]
        tokens_in = response.get("prompt_eval_count", 0)
        tokens_out = response.get("eval_count", 0)
        status = "ok"
        error_msg = None
    except Exception as exc:
        t_llm_ms = int((time.monotonic() - t0) * 1000)
        latency_ms = int((time.monotonic() - t_start) * 1000)
        response_text = ""
        tokens_in = 0
        tokens_out = 0
        status = "error"
        error_msg = str(exc)

    record: dict[str, Any] = {
        "sha256": sha,
        "braco": braco,
        "modelo": modelo,
        "scenario_id": scenario_id,
        "run_id": run_id,
        "seed": seed,
        "timestamp_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "prompt_sha": hashlib.sha256(user_prompt.encode()).hexdigest(),
        "response_text": response_text,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "latency_ms": latency_ms,
        "status": status,
        "error": error_msg,
        "clingo_active_sovereign": clingo_result.get("active_sovereign", []) if clingo_result else [],
        "clingo_active_elastic": clingo_result.get("active_elastic", []) if clingo_result else [],
        "clingo_satisfiability": clingo_result.get("satisfiability", "") if clingo_result else "",
        # Campos de tempo granular: t_clingo_ms para B4+B5; t_llm_ms para todos
        "t_clingo_ms": t_clingo_ms,
        "t_llm_ms": t_llm_ms,
        # Campos exclusivos B5 — None para B1-B4
        "t_psi_build_ms": _qfeng_b5_metrics.get("t_psi_build_ms"),
        "t_theta_compute_ms": _qfeng_b5_metrics.get("t_theta_compute_ms"),
        "qfeng_psi_n_dim": _qfeng_b5_metrics.get("psi_n_dim"),
        "qfeng_psi_s_dim": _qfeng_b5_metrics.get("psi_s_dim"),
        "qfeng_theta_rad": _qfeng_b5_metrics.get("theta_rad"),
        "qfeng_theta_deg": _qfeng_b5_metrics.get("theta_deg"),
        "qfeng_theta_eff_rad": _qfeng_b5_metrics.get("theta_eff_rad"),
        "qfeng_theta_eff_deg": _qfeng_b5_metrics.get("theta_eff_deg"),
        "qfeng_regime": _qfeng_b5_metrics.get("regime"),
        "qfeng_p_action": _qfeng_b5_metrics.get("p_action"),
        "qfeng_cos_theta": _qfeng_b5_metrics.get("cos_theta"),
        "qfeng_cb_threshold_deg": _qfeng_b5_metrics.get("cb_threshold_deg"),
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    return record
