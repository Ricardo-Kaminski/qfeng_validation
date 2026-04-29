"""Deduplicacao one-shot retroativa do results.parquet (B5.7.4).

Mantem keep='last' por sha256 — a versao mais recente de cada SHA, alinhada
com a politica do upsert ativo a partir do commit B5.7.3.

Uso: python -m experiments.adversarial_clt.runners._dedup_parquet_one_shot
"""
from __future__ import annotations

import json
import hashlib
import sys
from pathlib import Path
from datetime import datetime

import pandas as pd

EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
RESULTS = EXPERIMENT_ROOT / "results"
PARQUET = RESULTS / "results.parquet"
RAW = RESULTS / "raw_responses"


def run_dedup() -> dict:
    print(f"\n{'='*60}")
    print("DEDUP ONE-SHOT — results.parquet")
    print(f"Timestamp UTC-3: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    assert PARQUET.exists(), f"PARAR: parquet não encontrado: {PARQUET}"
    assert RAW.exists(), f"PARAR: raw_responses não encontrado: {RAW}"

    # 1. Carrega parquet atual
    df_pre = pd.read_parquet(PARQUET)
    print(f"Pré-dedup: {len(df_pre)} linhas, {df_pre['sha256'].nunique()} SHAs únicos")
    print(f"Duplicatas: {len(df_pre) - df_pre['sha256'].nunique()} linhas extras")

    # 2. Auditoria SHA parquet vs raw_responses
    raw_shas = {f.stem for f in RAW.glob("*.json")}
    parquet_shas = set(df_pre["sha256"].unique())
    ghosts = parquet_shas - raw_shas
    missing = raw_shas - parquet_shas

    print(f"\nAuditoria SHA:")
    print(f"  Raw responses: {len(raw_shas)} SHAs únicos")
    print(f"  Parquet SHAs: {len(parquet_shas)} únicos")
    print(f"  Ghosts (parquet sem raw): {len(ghosts)}")
    print(f"  Missing (raw sem parquet): {len(missing)}")

    assert not ghosts, f"PARAR: SHAs fantasma: {sorted(ghosts)[:5]}"
    assert not missing, f"PARAR: SHAs em raw ausentes do parquet: {sorted(missing)[:5]}"

    # 3. Dedup keep='last' por sha256
    df_post = df_pre.drop_duplicates(subset=["sha256"], keep="last").reset_index(drop=True)
    print(f"\nPós-dedup: {len(df_post)} linhas")

    # 4. Cardinalidade por braço
    print("\nCardinalidade pós-dedup por braço:")
    expected_b1b2b3 = {"B1": 600, "B2": 600, "B3": 600}
    for arm, expected in expected_b1b2b3.items():
        actual = int((df_post["braco"] == arm).sum())
        status = "OK" if actual == expected else "FAIL"
        print(f"  {arm}: {actual}/{expected} [{status}]")
        assert actual == expected, f"PARAR: {arm} esperava {expected}, encontrou {actual}"

    b4_actual = int((df_post["braco"] == "B4").sum())
    b4_pre = int((df_pre["braco"] == "B4").sum())
    b4_ok = 597 <= b4_actual <= 600
    print(f"  B4: {b4_actual} (pré-dedup: {b4_pre}) [{'OK' if b4_ok else 'WARN'}]")
    assert b4_ok, f"PARAR: B4 fora da faixa 597-600: {b4_actual}"

    b5_actual = int((df_post["braco"] == "B5").sum())
    print(f"  B5: {b5_actual} (esperado: 0)")
    assert b5_actual == 0, f"PARAR: B5 não deve existir ainda: {b5_actual}"

    # 5. Invariantes de integridade
    assert df_post["sha256"].is_unique, "PARAR: sha256 não-único após dedup"
    assert (df_post["status"] == "ok").all(), "PARAR: há linhas com status != ok"

    # 6. Q-FENG colunas None para B1-B4
    qfeng_cols = ["qfeng_regime", "qfeng_theta_deg", "qfeng_p_action"]
    for arm in ("B1", "B2", "B3", "B4"):
        sub = df_post[df_post["braco"] == arm]
        for col in qfeng_cols:
            if col in sub.columns:
                n_non_null = sub[col].notna().sum()
                assert n_non_null == 0, f"PARAR: {arm}.{col} tem {n_non_null} valores não-null — bug arquitetônico"
    print("\nQ-FENG colunas: None para B1-B4 ✓")

    # 7. Cardinalidade por (braço, modelo)
    print("\nCardinalidade por (braço, modelo):")
    breakdown = df_post.groupby(["braco", "modelo"]).size().reset_index(name="n")
    for _, row in breakdown.iterrows():
        print(f"  {row['braco']}/{row['modelo']}: {row['n']}")

    # 8. Grava parquet deduplicado
    df_post.to_parquet(PARQUET, index=False)
    sha_post = hashlib.sha256(PARQUET.read_bytes()).hexdigest()
    print(f"\nParquet gravado. SHA256: {sha_post[:32]}...")

    # 9. Relatório JSON
    report = {
        "timestamp_utc3": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pre_dedup_rows": int(len(df_pre)),
        "post_dedup_rows": int(len(df_post)),
        "removed_duplicates": int(len(df_pre) - len(df_post)),
        "unique_shas": int(df_post["sha256"].nunique()),
        "cardinality_by_arm": {arm: int((df_post["braco"] == arm).sum()) for arm in df_post["braco"].unique()},
        "cardinality_by_arm_model": breakdown.to_dict(orient="records"),
        "parquet_sha256_post": sha_post,
        "policy": "keep=last por sha256 (alinhado com upsert ativo)",
    }
    report_path = RESULTS / "_dedup_report_29abr2026.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Relatório: {report_path}")

    print(f"\n{'='*60}")
    print(f"DEDUP CONCLUÍDO: {len(df_pre)} → {len(df_post)} linhas (-{len(df_pre)-len(df_post)})")
    print(f"{'='*60}")

    return report


if __name__ == "__main__":
    run_dedup()
