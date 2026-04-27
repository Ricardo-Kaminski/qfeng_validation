"""H6 — Estratificação por Fricção Ontológica (ANOVA one-way).

Testa se o efeito da ancoragem sobre D1 varia conforme a categoria de
Fricção Ontológica do cenário.

H₆: |Δ_D1(B4−B1)|_derivacional > |Δ_D1(B4−B1)|_procedural
Teste: ANOVA one-way (fator: friccao_categoria [4 níveis]) sobre Δ_D1
Categorias: derivacional (n=23), procedural (n=11), controle_positivo (n=11), controle_negativo (n=5)
Interpretação: exploratória (não confirmatória), α = 0.05

Δ_D1 por cenário = D1(arm=B1, cenário) - D1(arm=B4, cenário)
  Positivo = B4 reduz alucinação (direção esperada pela ancoragem Q-FENG)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


SCENARIOS_FILE = Path(__file__).resolve().parents[1] / "scenarios" / "scenarios.yaml"
VALID_FRICCAO_CATS = ["derivacional", "procedural", "controle_positivo", "controle_negativo"]


def _load_friccao_map() -> dict[str, str]:
    """Carrega mapeamento scenario_id → friccao_categoria do YAML."""
    import yaml
    with open(SCENARIOS_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {s["scenario_id"]: s.get("friccao_categoria", "") for s in data["scenarios"]}


def _compute_delta_d1(
    df: pd.DataFrame,
    arm_base: str = "B1",
    arm_inter: str = "B4",
) -> pd.DataFrame:
    """Calcula Δ_D1 = D1(B1) - D1(B4) por cenário (média entre modelos e runs).

    Retorna DataFrame com scenario_id, delta_d1, friccao_categoria.
    """
    agg = (
        df[df["arm"].isin([arm_base, arm_inter])]
        .dropna(subset=["d1_score"])
        .groupby(["scenario_id", "arm"])["d1_score"]
        .mean()
        .unstack("arm")
        .dropna()
    )

    if arm_base not in agg.columns or arm_inter not in agg.columns:
        return pd.DataFrame(columns=["scenario_id", "delta_d1", "friccao_categoria"])

    agg["delta_d1"] = agg[arm_base] - agg[arm_inter]  # positivo = B4 melhor
    agg = agg.reset_index()[["scenario_id", "delta_d1"]]
    return agg


def run_h6_friccao(
    d1_path: str | Path,
    arm_base: str = "B1",
    arm_inter: str = "B4",
    output_path: str | Path | None = None,
) -> dict:
    """Executa análise H6 por fricção ontológica.

    Args:
        d1_path: parquet com colunas scenario_id, arm, model, run_id, d1_score
        arm_base: braço baseline
        arm_inter: braço intervenção
        output_path: caminho para salvar JSON

    Returns:
        dict com resultados ANOVA e conclusão H6
    """
    path = Path(d1_path)
    if not path.exists():
        raise FileNotFoundError(f"D1 parquet não encontrado: {path}")

    df = pd.read_parquet(path)

    # Garante coluna 'arm' (pode estar como 'braco' no parquet legado)
    if "arm" not in df.columns and "braco" in df.columns:
        df = df.rename(columns={"braco": "arm"})

    delta = _compute_delta_d1(df, arm_base, arm_inter)
    if delta.empty:
        print(f"  [H6] Sem dados para comparar {arm_base} vs {arm_inter}")
        return {"h6": {}, "conclusion": {"h6_corroborated": False}}

    # Adiciona friccao_categoria via YAML (fonte canônica)
    friccao_map = _load_friccao_map()
    delta["friccao_categoria"] = delta["scenario_id"].map(friccao_map).fillna("desconhecida")

    # Estatísticas descritivas por categoria
    desc: dict = {}
    groups_for_anova: list[np.ndarray] = []
    for cat in VALID_FRICCAO_CATS:
        grp = delta[delta["friccao_categoria"] == cat]["delta_d1"].values
        if len(grp) == 0:
            continue
        desc[cat] = {
            "n": int(len(grp)),
            "mean_delta_d1": round(float(grp.mean()), 4),
            "std_delta_d1": round(float(grp.std(ddof=1)), 4) if len(grp) > 1 else 0.0,
            "abs_mean_delta_d1": round(float(np.abs(grp).mean()), 4),
        }
        groups_for_anova.append(grp)
        print(f"  [H6] {cat}: n={len(grp)} Δ_D1_mean={grp.mean():.4f} |Δ|={np.abs(grp).mean():.4f}")

    # ANOVA one-way
    anova_result: dict = {}
    if len(groups_for_anova) >= 2:
        F, p = stats.f_oneway(*groups_for_anova)
        # η² = SS_between / SS_total
        grand_mean = delta["delta_d1"].mean()
        ss_between = sum(
            len(g) * (g.mean() - grand_mean) ** 2 for g in groups_for_anova
        )
        ss_total = sum((delta["delta_d1"] - grand_mean) ** 2)
        eta2 = ss_between / ss_total if ss_total > 0 else 0.0

        anova_result = {
            "F": round(float(F), 4),
            "p": round(float(p), 6),
            "eta2": round(eta2, 4),
            "significant_p05": p < 0.05,
        }
        print(f"  [H6] ANOVA: F={F:.4f} p={p:.4f} η²={eta2:.4f}")
    else:
        print("  [H6] Insuficientes categorias para ANOVA")

    # Teste H6 específico: |Δ|_derivacional > |Δ|_procedural
    h6_direction = False
    if "derivacional" in desc and "procedural" in desc:
        abs_deriv = desc["derivacional"]["abs_mean_delta_d1"]
        abs_proced = desc["procedural"]["abs_mean_delta_d1"]
        h6_direction = abs_deriv > abs_proced
        print(f"  [H6] |Δ|_derivacional={abs_deriv:.4f} vs |Δ|_procedural={abs_proced:.4f} → {'✓' if h6_direction else '✗'}")

    results = {
        "h6": {
            "by_friccao": desc,
            "anova": anova_result,
            "arms_compared": [arm_base, arm_inter],
            "n_scenarios_total": int(len(delta)),
            "h6_direction_correct": h6_direction,
        },
        "conclusion": {
            "h6_corroborated": h6_direction and anova_result.get("significant_p05", False),
            "alpha": 0.05,
            "verdict": (
                "H6 CORROBORADA: efeito da ancoragem significativamente maior em cenários derivacionais"
                if h6_direction and anova_result.get("significant_p05", False)
                else (
                    "H6 PARCIAL: direção correta mas ANOVA não significativa (exploratório)"
                    if h6_direction
                    else "H6 NÃO CORROBORADA: sem diferença de efeito por categoria de fricção"
                )
            ),
        },
    }

    print(f"\n  → {results['conclusion']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H6 salvos em {out}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ANOVA H6 — Fricção Ontológica")
    parser.add_argument("--d1", required=True, help="Parquet com scores D1 por job")
    parser.add_argument("--base-arm", default="B1")
    parser.add_argument("--inter-arm", default="B4")
    parser.add_argument("--output", default="experiments/adversarial_clt/results/h6_friccao.json")
    args = parser.parse_args()

    run_h6_friccao(
        d1_path=args.d1,
        arm_base=args.base_arm,
        arm_inter=args.inter_arm,
        output_path=args.output,
    )
