"""Orquestrador da análise confirmatória completa (H1–H6).

Etapas:
  1. Avalia D1, D2, D3 sobre results.parquet → salva parquets por métrica
  2. H1 McNemar (D1 binária, B4 vs B1 por modelo, Bonferroni)
  3. H2 Wilcoxon (D2 contínua, B3/B4 vs B1 por modelo)
  4. H3 ANOVA two-way (arm × model, D1/D2/D3)
  5. H4 Wilcoxon (D3 contínua, B4 vs B1 por modelo)
  6. H5 Levene (variância cross-model, B4 vs B1)
  7. H6 ANOVA one-way (Δ_D1 por friccao_categoria)
  8. Consolida em summary.json

Uso:
  python -m experiments.adversarial_clt.analysis.run_confirmatory_analysis
  python -m experiments.adversarial_clt.analysis.run_confirmatory_analysis --results-parquet caminho.parquet
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

# Paths canônicos
_EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
_RESULTS_DIR = _EXPERIMENT_ROOT / "results"
_SCENARIOS_DIR = _EXPERIMENT_ROOT / "scenarios"
_ANALYSIS_DIR = _RESULTS_DIR / "analysis"

RESULTS_PARQUET = _RESULTS_DIR / "results.parquet"
GROUND_TRUTH_JSON = _SCENARIOS_DIR / "ground_truth_predicates.json"


def _eval_metrics(results_parquet: Path) -> dict[str, Path]:
    """Avalia D1, D2, D3 e salva parquets por métrica. Retorna paths."""
    sys.path.insert(0, str(_EXPERIMENT_ROOT.parent.parent))
    from experiments.adversarial_clt.evaluators.eval_d1_alucinacao import eval_d1_scenario
    from experiments.adversarial_clt.evaluators.eval_d2_cobertura import eval_d2_scenario
    from experiments.adversarial_clt.evaluators.d3_specificity import eval_d3_scenario

    import json as _json
    df = pd.read_parquet(results_parquet)
    with open(GROUND_TRUTH_JSON, encoding="utf-8") as f:
        gt_data = _json.load(f)

    arm_col = "arm" if "arm" in df.columns else "braco"
    model_col = "model" if "model" in df.columns else "modelo"

    d1_rows, d2_rows, d3_rows = [], [], []

    for _, row in df.iterrows():
        sid = row.get("scenario_id", "")
        arm = row.get(arm_col, "")
        model = row.get(model_col, "")
        run_id = row.get("run_id", 0)
        friccao = row.get("friccao_categoria", "")
        response = row.get("response_text", "")
        if not response:
            continue

        gt = gt_data.get("by_scenario", {}).get(sid, {})
        base = {"scenario_id": sid, "arm": arm, "model": model, "run_id": run_id, "friccao_categoria": friccao}

        if gt:
            d1_rows.append({**base, **eval_d1_scenario(response, gt)})
            d2_rows.append({**base, **eval_d2_scenario(response, gt)})
        d3_rows.append({**base, **eval_d3_scenario(response)})

    _ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    for name, rows in [("d1", d1_rows), ("d2", d2_rows), ("d3", d3_rows)]:
        if rows:
            out = _ANALYSIS_DIR / f"{name}_scores.parquet"
            pd.DataFrame(rows).to_parquet(out, index=False)
            paths[name] = out
            print(f"  [{name.upper()}] {len(rows)} scores → {out.name}")

    return paths


def run_full_analysis(results_parquet: Path = RESULTS_PARQUET) -> dict:
    """Executa pipeline completo de análise confirmatória."""
    if not results_parquet.exists():
        raise FileNotFoundError(
            f"results.parquet não encontrado: {results_parquet}\n"
            "Execute primeiro o runner LLM (Task F2.5)."
        )

    print(f"\n{'='*60}")
    print("ANÁLISE CONFIRMATÓRIA FRENTE 2 — Q-FENG vs CLT")
    print(f"{'='*60}\n")

    # ── Etapa 1: Métricas D1/D2/D3 ──────────────────────────────────
    print("[ Etapa 1 ] Avaliando D1/D2/D3...")
    metric_paths = _eval_metrics(results_parquet)

    # ── Etapa 2-7: Hipóteses confirmatórias ─────────────────────────
    from experiments.adversarial_clt.analysis.test_h1_mcnemar import run_h1_mcnemar
    from experiments.adversarial_clt.analysis.test_h2_h4_wilcoxon import run_h2_wilcoxon, run_h4_wilcoxon
    from experiments.adversarial_clt.analysis.test_h3_anova_interaction import run_h3_anova
    from experiments.adversarial_clt.analysis.test_h5_levene_variance import run_h5_levene
    from experiments.adversarial_clt.analysis.test_subgroup_friccao import run_h6_friccao

    summary: dict = {}

    print("\n[ H1 ] McNemar — alucinação (D1)...")
    if "d1" in metric_paths:
        summary["h1"] = run_h1_mcnemar(
            d1_path=metric_paths["d1"],
            output_path=_ANALYSIS_DIR / "h1_mcnemar.json",
        )

    print("\n[ H2 ] Wilcoxon — cobertura predicativa (D2)...")
    if "d2" in metric_paths:
        summary["h2"] = run_h2_wilcoxon(
            d2_path=metric_paths["d2"],
            output_path=_ANALYSIS_DIR / "h2_wilcoxon.json",
        )

    print("\n[ H3 ] ANOVA two-way — interação arm×model...")
    summary["h3"] = run_h3_anova(
        results_path=results_parquet,
        d1_path=metric_paths.get("d1"),
        d2_path=metric_paths.get("d2"),
        d3_path=metric_paths.get("d3"),
        output_path=_ANALYSIS_DIR / "h3_anova.json",
    )

    print("\n[ H4 ] Wilcoxon — especificidade de citação (D3)...")
    if "d3" in metric_paths:
        summary["h4"] = run_h4_wilcoxon(
            d3_path=metric_paths["d3"],
            output_path=_ANALYSIS_DIR / "h4_wilcoxon.json",
        )

    print("\n[ H5 ] Levene — consistência cross-architecture...")
    summary["h5"] = run_h5_levene(
        d1_path=metric_paths.get("d1"),
        d2_path=metric_paths.get("d2"),
        output_path=_ANALYSIS_DIR / "h5_levene.json",
    )

    print("\n[ H6 ] ANOVA one-way — estratificação por fricção ontológica...")
    if "d1" in metric_paths:
        summary["h6"] = run_h6_friccao(
            d1_path=metric_paths["d1"],
            output_path=_ANALYSIS_DIR / "h6_friccao.json",
        )

    # ── Sumário consolidado ──────────────────────────────────────────
    conclusions = {
        hyp: data.get("conclusion", data.get(f"conclusion_{hyp}", {}))
        for hyp, data in summary.items()
    }
    summary_path = _ANALYSIS_DIR / "summary_confirmatory.json"
    summary_path.write_text(
        json.dumps({"conclusions": conclusions, "metric_paths": {k: str(v) for k, v in metric_paths.items()}},
                   indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n{'='*60}")
    print("SUMÁRIO FINAL")
    print(f"{'='*60}")
    for hyp, conc in conclusions.items():
        v = conc.get("verdict", "—")
        print(f"  {hyp.upper()}: {v}")
    print(f"\nSumário salvo em {summary_path}")

    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análise confirmatória completa H1-H6")
    parser.add_argument(
        "--results-parquet",
        default=str(RESULTS_PARQUET),
        help="Caminho para results.parquet do experimento",
    )
    args = parser.parse_args()
    run_full_analysis(Path(args.results_parquet))
