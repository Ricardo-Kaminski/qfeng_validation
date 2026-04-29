"""Smoke test para upsert por sha256 em _append_to_parquet (B5.7.3).

Valida que a função é idempotente: chamadas repetidas com o mesmo sha256
resultam em 1 linha, não em duplicatas.

Uso: python -m experiments.adversarial_clt.runners._smoke_test_upsert_parquet
"""
from __future__ import annotations

import sys
import json
from pathlib import Path
from datetime import datetime

# Garante import correto
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"
TEST_PARQUET = RESULTS_PATH / "_test_upsert.parquet"

# Monkey-patch RESULTS_PARQUET para apontar ao arquivo de teste
import experiments.adversarial_clt.runners.run_full_experiment as rfe
_ORIGINAL_PARQUET = rfe.RESULTS_PARQUET
rfe.RESULTS_PARQUET = TEST_PARQUET

from experiments.adversarial_clt.runners.run_full_experiment import _append_to_parquet
import pandas as pd


def _make_record(sha: str, latency: int = 1000, arm: str = "B1") -> dict:
    return {
        "sha256": sha,
        "braco": arm,
        "modelo": "qwen3:14b",
        "scenario_id": "T-CLT-01-001",
        "run_id": 1,
        "seed": 42,
        "timestamp_iso": datetime.utcnow().isoformat() + "Z",
        "response_text": f"resposta de teste sha={sha}",
        "tokens_in": 100,
        "tokens_out": 200,
        "latency_ms": latency,
        "status": "ok",
        "error": None,
        "clingo_satisfiability": "SAT",
        "clingo_active_sovereign": ["r1"],
        "clingo_active_elastic": [],
        "friccao_categoria": "derivacional",
        "t_clingo_ms": None, "t_llm_ms": None,
        "t_psi_build_ms": None, "t_theta_compute_ms": None,
        "qfeng_theta_deg": None, "qfeng_theta_eff_deg": None,
        "qfeng_regime": None, "qfeng_p_action": None,
        "qfeng_cos_theta": None, "qfeng_psi_n_dim": None, "qfeng_psi_s_dim": None,
    }


passed = 0
failed = 0


def check(condition: bool, msg: str) -> None:
    global passed, failed
    if condition:
        print(f"  PASS: {msg}")
        passed += 1
    else:
        print(f"  FAIL: {msg}")
        failed += 1


def run_smoke_tests() -> bool:
    # Limpar teste anterior
    if TEST_PARQUET.exists():
        TEST_PARQUET.unlink()

    print("=== Smoke test upsert _append_to_parquet ===\n")

    # Test 1: primeira inserção cria parquet com 1 linha
    rec_a = _make_record("aaa111", latency=1000)
    _append_to_parquet(rec_a)
    df = pd.read_parquet(TEST_PARQUET)
    check(len(df) == 1, f"1 linha após 1ª inserção (obtido: {len(df)})")
    check(df.iloc[0]["sha256"] == "aaa111", "sha256 correto na linha 1")

    # Test 2: inserção com mesmo sha256 substitui (não duplica)
    rec_a2 = _make_record("aaa111", latency=9999)
    _append_to_parquet(rec_a2)
    df = pd.read_parquet(TEST_PARQUET)
    check(len(df) == 1, f"Ainda 1 linha após upsert com mesmo sha256 (obtido: {len(df)})")
    check(int(df.iloc[0]["latency_ms"]) == 9999, f"latency_ms atualizado para 9999 (obtido: {df.iloc[0]['latency_ms']})")

    # Test 3: inserção com sha256 diferente adiciona nova linha
    rec_b = _make_record("bbb222", latency=2000)
    _append_to_parquet(rec_b)
    df = pd.read_parquet(TEST_PARQUET)
    check(len(df) == 2, f"2 linhas após inserção de sha256 distinto (obtido: {len(df)})")
    check(df["sha256"].nunique() == 2, "2 SHAs únicos no parquet")

    # Test 4: terceira inserção de sha256 distinto
    rec_c = _make_record("ccc333", latency=3000, arm="B3")
    _append_to_parquet(rec_c)
    df = pd.read_parquet(TEST_PARQUET)
    check(len(df) == 3, f"3 linhas após 3ª inserção (obtido: {len(df)})")

    # Test 5: re-upsert do sha "bbb222" não aumenta cardinalidade
    rec_b2 = _make_record("bbb222", latency=8888)
    _append_to_parquet(rec_b2)
    df = pd.read_parquet(TEST_PARQUET)
    check(len(df) == 3, f"Ainda 3 linhas após re-upsert de bbb222 (obtido: {len(df)})")
    row_b = df[df["sha256"] == "bbb222"]
    check(int(row_b.iloc[0]["latency_ms"]) == 8888, f"bbb222 atualizado para 8888 (obtido: {row_b.iloc[0]['latency_ms']})")

    # Test 6: sha256 é único no parquet final
    check(df["sha256"].is_unique, "sha256 único em todas as linhas")

    # Test 7: status='ok' em todas as linhas
    check((df["status"] == "ok").all(), "status='ok' em todas as linhas")

    # Test 8: campos None preservados para B1-B4
    check(df["qfeng_theta_deg"].isna().all(), "qfeng_theta_deg None para todos os registros de teste")

    # Cleanup
    if TEST_PARQUET.exists():
        TEST_PARQUET.unlink()
    rfe.RESULTS_PARQUET = _ORIGINAL_PARQUET

    print(f"\n=== Resultado: {passed} PASSED, {failed} FAILED ===")
    return failed == 0


if __name__ == "__main__":
    ok = run_smoke_tests()
    sys.exit(0 if ok else 1)
