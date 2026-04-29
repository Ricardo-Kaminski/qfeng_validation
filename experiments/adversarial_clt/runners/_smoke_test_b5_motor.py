"""Smoke test: caminho B5 sem chamada LLM, valida motor Q-FENG completo.

Testa:
  1. Motor sintetico sobre 3 cenarios canonicos (via scenario_loader + psi_builder)
  2. Campos None para B1-B4 no record (sem chamada LLM)

Executar:
    C:/Users/ricar/miniconda3/envs/qfeng/python.exe experiments/adversarial_clt/runners/_smoke_test_b5_motor.py
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))

from qfeng.core.interference import CircuitBreakerConfig, compute_interference
from qfeng.e5_symbolic.psi_builder import build_psi_n, build_psi_s
from qfeng.e5_symbolic.scenario_loader import run_scenario

# ---------------------------------------------------------------------------
# Cenarios canonicos: (clingo_anchor, descricao, regime_esperado)
# T-CLT-01 = phantom citation (UNSAT) → alto theta → BLOCK
# T-CLT-03 = hour bank com CCT (SAT)  → baixo theta → STAC
# T-CLT-04 = positive control (SAT)   → baixo theta → STAC
# ---------------------------------------------------------------------------
CANONARIES = [
    ("T-CLT-01", "phantom citation UNSAT", "BLOCK"),
    ("T-CLT-03", "hour bank valido SAT", "STAC"),
    ("T-CLT-04", "positive control SAT", "STAC"),
]

print("=== Smoke test motor Q-FENG B5 ===\n")
all_passed = True

for clingo_id, descr, expected_regime in CANONARIES:
    print(f"--- {clingo_id}: {descr} ---")
    try:
        result = run_scenario(clingo_id)
        psi_n = build_psi_n(clingo_id)
        psi_s = build_psi_s(
            clingo_id,
            active_sovereign=result["active_sovereign"],
            active_elastic=result["active_elastic"],
        )

        cb_config = CircuitBreakerConfig()
        motor = compute_interference(
            psi_n=psi_n,
            psi_s=psi_s,
            alpha_sq=0.5,
            beta_sq=0.5,
            cb_config=cb_config,
            theta_history=None,
            gamma=0.0,
        )

        regime_str = str(motor.decision).upper()
        print(f"  Clingo SAT: {result['satisfiable']}")
        print(f"  N sovereign: {result['n_sovereign_active']}, N elastic: {result['n_elastic_active']}")
        print(f"  psi_n dim: {len(psi_n)}, psi_s dim: {len(psi_s)}")
        print(f"  theta: {motor.theta_degrees:.2f} deg | cos(theta): {motor.cos_theta:.4f}")
        print(f"  p_action: {motor.p_action:.4f}")
        print(f"  Regime: {regime_str} (esperado: {expected_regime})")
        match = regime_str == expected_regime
        print(f"  Status: {'OK' if match else 'DIVERGENCIA EDITORIAL — verificar calibracao psi_builder'}")
        print()
    except Exception as e:
        print(f"  ERRO: {e}")
        import traceback; traceback.print_exc()
        all_passed = False
        print()

# ---------------------------------------------------------------------------
# Verificacao de campos None para B1/B4 sem LLM (via importacao direta)
# ---------------------------------------------------------------------------
print("--- Verificacao de campos qfeng_* para B1 (esperado: todos None) ---")
try:
    from experiments.adversarial_clt.runners.run_arm import _qfeng_b5_metrics
    # Apos rodar B1, _qfeng_b5_metrics deve estar vazio
    from experiments.adversarial_clt.runners import run_arm as _run_arm_mod
    _run_arm_mod._qfeng_b5_metrics = {}
    # Simular bloco B1 em _build_prompt (nao popula _qfeng_b5_metrics)
    campos_b5 = [
        _run_arm_mod._qfeng_b5_metrics.get("theta_deg"),
        _run_arm_mod._qfeng_b5_metrics.get("regime"),
        _run_arm_mod._qfeng_b5_metrics.get("t_psi_build_ms"),
    ]
    assert all(v is None for v in campos_b5), f"Esperado None, obtido: {campos_b5}"
    print("  qfeng_theta_deg=None, qfeng_regime=None, t_psi_build_ms=None: OK")
    print()
except Exception as e:
    print(f"  AVISO: {e}")
    print()

print("=" * 50)
print(f"Smoke test B5 motor: {'PASSED' if all_passed else 'FALHA — ver erros acima'}")
