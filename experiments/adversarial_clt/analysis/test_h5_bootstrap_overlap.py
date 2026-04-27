"""H5b — Effect-size overlap across architectures (bootstrap pareado).

Testa se a magnitude do efeito Q-FENG na redução de alucinação (D1) é invariante
entre famílias arquitetônicas de LLM, operacionalizado como SOBREPOSIÇÃO DOS IC95%
BOOTSTRAP da diferença pareada [D1(B1) − D1(B4)] entre todos os pares de modelos.

H₅ᵦ: ICs 95% bootstrap de [D1(B1) − D1(B4)]_modelo_i sobrepostos para >= 5/6 pares (i,j)

Adicionada pela emenda 27/abr/2026 (PRE_REGISTRATION.md §11.2) para alinhar
com a reivindicação editorial de agnosticismo de stack ML (canônico §7.4 nova).

H5 (Levene's test em test_h5_levene_variance.py) é preservada como evidência
complementar, NÃO substituída.

Implementação:
- Para cada modelo m em {qwen3:14b, phi4:14b, gemma3:12b, llama3.1:8b}:
    - Computar delta_m = D1(B1, scenario_i) − D1(B4, scenario_i) para cada cenário i
    - Bootstrap não-paramétrico pareado por cenário, 1000 iterações
    - Derivar IC95% percentile (2.5%, 97.5%) sobre a média dos deltas
- Computar matriz 4×4 de overlap binário entre os ICs dos 4 modelos
- Critério de evidência: ≥ 5 dos 6 pares (i,j) com overlap
"""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd


N_BOOTSTRAP = 1000
RNG_SEED = 42
OVERLAP_THRESHOLD = 5  # de 6 pares possíveis

MODELS = ["qwen3:14b", "phi4:14b", "gemma3:12b", "llama3.1:8b"]


def _compute_paired_delta(df: pd.DataFrame, model: str, arm_base: str = "B1", arm_inter: str = "B4") -> np.ndarray:
    """Diferença pareada D1(B1) - D1(B4) por cenário, para um modelo dado."""
    df_m = df[df["model"] == model]
    pivot = df_m.pivot_table(
        index="scenario_id", columns="arm", values="d1_score", aggfunc="mean"
    )
    if arm_base not in pivot.columns or arm_inter not in pivot.columns:
        return np.array([])
    delta = (pivot[arm_base] - pivot[arm_inter]).dropna().values
    return delta


def _bootstrap_ci(
    delta: np.ndarray,
    n_iter: int = N_BOOTSTRAP,
    seed: int = RNG_SEED,
) -> tuple[float, float, float]:
    """IC95% bootstrap percentile sobre a média dos deltas.

    Returns:
        (point_estimate, ci_low_2.5%, ci_high_97.5%)
    """
    rng = np.random.default_rng(seed)
    n = len(delta)
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    means = np.empty(n_iter)
    for i in range(n_iter):
        sample = rng.choice(delta, size=n, replace=True)
        means[i] = sample.mean()
    return float(delta.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def _intervals_overlap(ci1: tuple[float, float], ci2: tuple[float, float]) -> bool:
    """True se [a1, b1] e [a2, b2] se sobrepõem."""
    a1, b1 = ci1
    a2, b2 = ci2
    return not (b1 < a2 or b2 < a1)


def run_h5b_bootstrap_overlap(
    d1_path: str | Path,
    arm_base: str = "B1",
    arm_inter: str = "B4",
    output_path: str | Path | None = None,
) -> dict:
    """Executa bootstrap overlap test para H5b sobre D1.

    Args:
        d1_path: parquet com colunas scenario_id, arm, model, d1_score
        arm_base: braço baseline (padrão B1)
        arm_inter: braço intervenção (padrão B4)
        output_path: caminho para salvar JSON

    Returns:
        dict com ICs por modelo, matriz de overlap e conclusão H5b
    """
    path = Path(d1_path)
    df = pd.read_parquet(path) if path.suffix == ".parquet" else pd.read_csv(path)

    # Normaliza coluna arm
    if "arm" not in df.columns and "braco" in df.columns:
        df = df.rename(columns={"braco": "arm"})

    cis: dict[str, dict] = {}
    for model in MODELS:
        delta = _compute_paired_delta(df, model, arm_base, arm_inter)
        if len(delta) == 0:
            cis[model] = {"point": None, "ci_low": None, "ci_high": None, "n_scenarios": 0}
            continue
        point, low, high = _bootstrap_ci(delta)
        cis[model] = {
            "point": round(point, 4),
            "ci_low": round(low, 4),
            "ci_high": round(high, 4),
            "n_scenarios": int(len(delta)),
        }
        print(f"  [H5b] {model}: Δ_mean={point:.4f} IC95%=[{low:.4f}, {high:.4f}] n={len(delta)}")

    # Matriz de overlap pareado 4×4
    pairs = list(combinations(MODELS, 2))
    overlap_matrix: dict[str, bool | None] = {}
    n_overlap = 0
    n_total = 0

    for m1, m2 in pairs:
        c1 = cis[m1]
        c2 = cis[m2]
        if c1["ci_low"] is None or c2["ci_low"] is None:
            overlap_matrix[f"{m1}__{m2}"] = None
            continue
        if any(v is None or (isinstance(v, float) and np.isnan(v))
               for v in [c1["ci_low"], c1["ci_high"], c2["ci_low"], c2["ci_high"]]):
            overlap_matrix[f"{m1}__{m2}"] = None
            continue
        overlap = _intervals_overlap((c1["ci_low"], c1["ci_high"]), (c2["ci_low"], c2["ci_high"]))
        overlap_matrix[f"{m1}__{m2}"] = overlap
        n_total += 1
        if overlap:
            n_overlap += 1
        print(f"  [H5b] {m1} vs {m2}: {'overlap ✓' if overlap else 'no overlap ✗'}")

    h5b_supported = (n_total >= 1) and (n_overlap >= OVERLAP_THRESHOLD)

    result = {
        "test": "H5b — Bootstrap effect-size overlap (4 LLM architectures)",
        "n_bootstrap": N_BOOTSTRAP,
        "rng_seed": RNG_SEED,
        "arms_compared": [arm_base, arm_inter],
        "models": MODELS,
        "confidence_intervals": cis,
        "overlap_matrix": overlap_matrix,
        "n_pairs_with_overlap": n_overlap,
        "n_pairs_total": n_total,
        "criterion_threshold": f">= {OVERLAP_THRESHOLD}/6 pairs with overlap",
        "h5b_supported": h5b_supported,
        "conclusion": {
            "h5b_supported": h5b_supported,
            "verdict": (
                f"H5b SUSTENTADA — magnitude do efeito Q-FENG invariante cross-architecture ({n_overlap}/{n_total} pares sobrepostos)"
                if h5b_supported
                else f"H5b FALSIFICADA — efeito Q-FENG varia entre arquiteturas LLM ({n_overlap}/{n_total} pares sobrepostos)"
            ),
        },
    }
    print(f"\n  → {result['conclusion']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H5b salvos em {out}")

    return result


def _smoke_test_with_synthetic_data() -> None:
    """Smoke test: bootstrap sobre dados sintéticos com efeito Q-FENG conhecido e invariante."""
    import tempfile
    rng = np.random.default_rng(42)
    rows = []
    for model in MODELS:
        for scen_id in range(50):
            # B1: D1 ~ N(0.6, 0.1); B4: D1 ~ N(0.3, 0.1) → efeito ~0.3 invariante entre modelos
            for arm, mean in [("B1", 0.6), ("B4", 0.3)]:
                rows.append({
                    "scenario_id": f"S{scen_id:03d}",
                    "arm": arm,
                    "model": model,
                    "d1_score": float(np.clip(rng.normal(mean, 0.1), 0, 1)),
                })
    df = pd.DataFrame(rows)

    with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as tmp:
        tmp_path = tmp.name
    df.to_parquet(tmp_path)

    try:
        result = run_h5b_bootstrap_overlap(tmp_path)
        assert result["h5b_supported"] is True, (
            f"Smoke test falhou: efeito invariante deveria sustentar H5b, "
            f"n_overlap={result['n_pairs_with_overlap']}/{result['n_pairs_total']}"
        )
        print("✓ test_h5b smoke test verified: synthetic invariant effect sustains H5b")
    finally:
        Path(tmp_path).unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bootstrap effect-size overlap H5b")
    parser.add_argument("--d1-path", help="Parquet com colunas: scenario_id, arm, model, d1_score")
    parser.add_argument("--output-path", default=None)
    parser.add_argument("--base-arm", default="B1")
    parser.add_argument("--inter-arm", default="B4")
    parser.add_argument("--smoke-test", action="store_true", help="Roda smoke test com dados sintéticos")
    args = parser.parse_args()

    if args.smoke_test:
        _smoke_test_with_synthetic_data()
    elif args.d1_path:
        result = run_h5b_bootstrap_overlap(
            d1_path=args.d1_path,
            arm_base=args.base_arm,
            arm_inter=args.inter_arm,
            output_path=args.output_path,
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        parser.print_help()
