"""B5.9.1 — Constrói dataset derivado para análises confirmatórias H1-H6.

Lê snapshot frozen B1-B4, extrai hallucination_flag e coverage_score,
persiste como results_b1_b4_derivado.parquet.

Uso: python -m experiments.adversarial_clt.analysis.build_derived_dataset
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from experiments.adversarial_clt.analysis._extract_hallucination import (
    ANCHOR_SATISFIABLE,
    GROUND_TRUTH,
    extract_coverage_score,
    extract_hallucination_flag,
)

RESULTS = Path(__file__).resolve().parents[1] / "results"
SNAPSHOT = RESULTS / "results_b1_b4_para_analise_29abr2026.parquet"
OUTPUT = RESULTS / "results_b1_b4_derivado.parquet"
NOTES_DIR = Path(__file__).resolve().parents[3] / "artefatos" / "notas_metodologicas"


def main() -> None:
    print(f"\n{'='*60}")
    print("B5.9.1 — Dataset Derivado B1-B4")
    print(f"Timestamp UTC-3: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    # 1. Carregar snapshot
    print(f"Carregando snapshot: {SNAPSHOT.name}")
    df = pd.read_parquet(SNAPSHOT)
    assert len(df) == 2400, f"Esperado 2400 linhas, encontrou {len(df)}"
    assert df["sha256"].nunique() == 2400, "SHA256 não único no snapshot"
    print(f"OK: {len(df)} linhas | {df['sha256'].nunique()} SHAs únicos")

    # 2. Verificar cobertura ground truth
    gts_present = set(df["scenario_id"].unique())
    gts_covered = {sid for sid in gts_present if sid in GROUND_TRUTH}
    print(f"\nGround truth: {len(gts_covered)}/{len(gts_present)} scenarios cobertos")
    missing_gt = gts_present - set(GROUND_TRUTH.keys())
    if missing_gt:
        print(f"  AVISO: sem ground truth para: {sorted(missing_gt)}")

    # 3. Extrair variáveis derivadas
    print(f"\nExtraindo hallucination_flag e coverage_score para {len(df)} registros...")
    hall_flags: list[int] = []
    cov_scores: list[int] = []
    clingo_satisfiable: list[bool | None] = []

    import yaml
    scenarios_file = Path(__file__).resolve().parents[1] / "scenarios" / "scenarios.yaml"
    scen_data = yaml.safe_load(scenarios_file.read_text(encoding="utf-8"))
    scenario_anchor = {s["scenario_id"]: s.get("clingo_anchor", "") for s in scen_data["scenarios"]}

    for _, row in df.iterrows():
        hall_flags.append(extract_hallucination_flag(row["scenario_id"], row["response_text"] or ""))
        cov_scores.append(extract_coverage_score(row["response_text"] or ""))
        anchor = scenario_anchor.get(row["scenario_id"], "")
        clingo_satisfiable.append(ANCHOR_SATISFIABLE.get(anchor, None))

    df["hallucination_flag"] = hall_flags
    df["coverage_score"] = cov_scores
    df["clingo_satisfiable"] = clingo_satisfiable  # metadata derivado
    df["correct_decision"] = df["scenario_id"].map(GROUND_TRUTH)

    # 4. Sanity checks
    assert df["hallucination_flag"].isin([0, 1]).all(), "hallucination_flag fora de {0,1}"
    assert df["coverage_score"].between(0, 3).all(), "coverage_score fora de [0,3]"

    # 5. Relatório de distribuições
    print(f"\nDistribuição hallucination_flag por braço:")
    hall_by_arm = df.groupby("braco")["hallucination_flag"].agg(["sum", "mean", "count"]).rename(
        columns={"sum": "n_hall", "mean": "rate_hall", "count": "n_total"}
    )
    hall_by_arm["rate_hall"] = hall_by_arm["rate_hall"].map("{:.3f}".format)
    print(hall_by_arm.to_string())

    print(f"\nDistribuição hallucination_flag por (braço, modelo):")
    print(df.groupby(["braco", "modelo"])["hallucination_flag"].mean().unstack().round(3).to_string())

    print(f"\nDistribuição coverage_score por braço (média):")
    print(df.groupby("braco")["coverage_score"].mean().round(3).to_string())

    print(f"\nDistribuição friccao_categoria:")
    print(df["friccao_categoria"].value_counts().to_string())

    print(f"\nDistribuição correct_decision:")
    print(df["correct_decision"].value_counts().to_string())

    # Sanidade B1 vs B3 (predição H1: B3 < B1)
    b1_rate = df[df["braco"] == "B1"]["hallucination_flag"].mean()
    b3_rate = df[df["braco"] == "B3"]["hallucination_flag"].mean()
    print(f"\n[Pré-verificação H1] B1 hall_rate={b1_rate:.3f} | B3 hall_rate={b3_rate:.3f}")
    if b3_rate < b1_rate:
        print("  ✓ Direção esperada: B3 < B1")
    else:
        print(f"  ⚠ Direção INESPERADA: B3 ({b3_rate:.3f}) ≥ B1 ({b1_rate:.3f}) — verificar extração")

    # 6. Gravar parquet derivado
    df.to_parquet(OUTPUT, index=False)
    sha_output = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    sha_snapshot = hashlib.sha256(SNAPSHOT.read_bytes()).hexdigest()
    print(f"\nGravado: {OUTPUT.name}")
    print(f"Linhas: {len(df)} | SHA256: {sha_output[:32]}...")

    # 7. Nota metodológica
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    note = f"""# B5.9.1 — Auditoria Snapshot e Dataset Derivado B1-B4

**Data:** {datetime.now().strftime('%d/%abr/%Y %H:%M')}
**Branch:** `caminho2`

## Snapshot Input

- Arquivo: `results_b1_b4_para_analise_29abr2026.parquet`
- Linhas: 2.400 | SHAs únicos: 2.400
- SHA256: `{sha_snapshot[:32]}...`

## Dataset Derivado Output

- Arquivo: `results_b1_b4_derivado.parquet`
- Linhas: {len(df)} | SHA256: `{sha_output[:32]}...`
- Colunas adicionadas: `hallucination_flag`, `coverage_score`, `clingo_satisfiable`, `correct_decision`

## Nota Metodológica: clingo_satisfiability

O campo `clingo_satisfiability` está vazio em todos os braços (B1-B4) devido a bug de
mismatch de chave no `run_arm.py`: a função `run_scenario()` retorna `satisfiable` (bool),
mas o código persiste `record["clingo_satisfiability"] = clingo_result.get("satisfiability", "")`.
A satisfiability dos 4 anchors foi re-derivada via re-execução de `run_scenario()`:

| Anchor | Satisfiável | Categoria |
|--------|------------|-----------|
| T-CLT-01 | False (UNSAT) | derivacional |
| T-CLT-02 | False (UNSAT) | procedural |
| T-CLT-03 | True (SAT) | controle_positivo |
| T-CLT-04 | True (SAT) | controle_negativo |

## Definição Operacional Adaptada: hallucination_flag

**Critério:** `hallucination_flag = 1` se `correct_decision='VIOLACAO'` E resposta do LLM
não identifica a violação (sem menção textual a violação, nulidade, irregularidade etc.).

Ground truth source: `scenarios.yaml` campo `correct_decision`.

## Distribuição por Braço

{hall_by_arm.to_string()}

## Distribuição por (Braço, Modelo)

{df.groupby(["braco", "modelo"])["hallucination_flag"].mean().unstack().round(3).to_string()}

## Distribuição coverage_score (média)

{df.groupby("braco")["coverage_score"].mean().round(3).to_string()}

## Distribuição friccao_categoria

{df["friccao_categoria"].value_counts().to_string()}

## Status

**B5.9.1: PASSED** — dataset derivado pronto para análises H1-H6.
"""
    note_path = NOTES_DIR / "B5_9_1_auditoria_snapshot.md"
    note_path.write_text(note, encoding="utf-8")
    print(f"Nota: {note_path.name}")
    print(f"\n{'='*60}")
    print("B5.9.1 CONCLUÍDO")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
