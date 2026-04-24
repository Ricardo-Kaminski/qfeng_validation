"""
Diagnostico F7 - PARTE 3
Ler os arquivos .lp em e3_predicates/ e e3_predicates_trabalhista/,
parsear os cabecalhos '% atom_id: ... | chunk: ... | strength: ...'
e os predicados para inferir modality.

Isto e a fonte de verdade real dos DeonticAtoms usados no experimento Clingo,
incluindo tanto os extraidos por LLM quanto os curados (camada 2 da tese).
"""
import re
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
E3_SAUDE = PROJECT_ROOT / "outputs" / "e3_predicates"
E3_TRAB = PROJECT_ROOT / "outputs" / "e3_predicates_trabalhista"

# Mapeamento nome-de-predicado Clingo -> modality
# Ampliar se encontrarmos outros nomes no parse
PRED_TO_MODALITY = {
    "obligated": "obligation",
    "obliged": "obligation",
    "required": "obligation",
    "shall": "obligation",
    "must": "obligation",
    "permitted": "permission",
    "allowed": "permission",
    "may": "permission",
    "prohibited": "prohibition",
    "forbidden": "prohibition",
    "not_allowed": "prohibition",
    "faculty": "faculty",
    "optional": "faculty",
    "entitled": "faculty",
}

HEADER_RE = re.compile(
    r"^%\s*atom_id:\s*([0-9a-f]+)\s*\|\s*chunk:\s*([0-9a-fA-F_]+)"
    r"(?:\s*\|\s*strength:\s*([a-z_]+))?",
    re.IGNORECASE,
)
PRED_RE = re.compile(r"^([a-z_][a-z0-9_]*)\s*\(", re.IGNORECASE)


def parse_lp_file(lp_path: Path):
    """Retorna lista de dicts {atom_id, chunk, strength, predicate, modality}."""
    atoms = []
    current_header = None
    with lp_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip()
            if not line:
                continue
            m = HEADER_RE.match(line)
            if m:
                current_header = {
                    "atom_id": m.group(1),
                    "chunk": m.group(2),
                    "strength": m.group(3) or "",
                }
                continue
            if current_header is not None and not line.startswith("%"):
                pm = PRED_RE.match(line.lstrip())
                if pm:
                    pred_name = pm.group(1).lower()
                    modality = PRED_TO_MODALITY.get(pred_name, f"UNKNOWN:{pred_name}")
                    atoms.append({
                        **current_header,
                        "predicate": pred_name,
                        "modality": modality,
                    })
                    current_header = None  # consumido
    return atoms


def scan_track(e3_dir: Path, label: str):
    print(f"\n[{label}] {e3_dir.relative_to(PROJECT_ROOT)}")
    if not e3_dir.exists():
        print("  DIRETORIO NAO EXISTE")
        return

    subdirs = [p for p in e3_dir.iterdir() if p.is_dir()]
    per_regime_modality = {}
    per_regime_total = Counter()
    unknown_preds = Counter()

    if subdirs:
        # Hierarquico por regime (saude)
        for regime_dir in sorted(subdirs):
            regime = regime_dir.name
            per_regime_modality[regime] = Counter()
            for lp in sorted(regime_dir.glob("*.lp")):
                atoms = parse_lp_file(lp)
                for a in atoms:
                    if a["modality"].startswith("UNKNOWN:"):
                        unknown_preds[a["modality"]] += 1
                    else:
                        per_regime_modality[regime][a["modality"]] += 1
                        per_regime_total[regime] += 1
    else:
        # Flat (possivel caso trabalhista)
        per_regime_modality["brasil"] = Counter()
        for lp in sorted(e3_dir.glob("*.lp")):
            atoms = parse_lp_file(lp)
            for a in atoms:
                if a["modality"].startswith("UNKNOWN:"):
                    unknown_preds[a["modality"]] += 1
                else:
                    per_regime_modality["brasil"][a["modality"]] += 1
                    per_regime_total["brasil"] += 1

    total_all = sum(per_regime_total.values())
    print(f"  Total atoms (predicados reconhecidos): {total_all:,}")
    for r, tot in per_regime_total.items():
        print(f"    {r}: {tot:,}")
        for m in ["obligation", "permission", "prohibition", "faculty"]:
            n = per_regime_modality[r].get(m, 0)
            print(f"      {m:<12}: {n:>5,}")

    if unknown_preds:
        print(f"\n  Predicados nao mapeados (top 10):")
        for pred, n in unknown_preds.most_common(10):
            print(f"    {pred}: {n}")

    return per_regime_modality, per_regime_total, unknown_preds


def main():
    print("=" * 72)
    print("DIAGNOSTICO F7 - PARTE 3  (fonte: e3_predicates/*.lp)")
    print("=" * 72)

    saude = scan_track(E3_SAUDE, "SAUDE")
    trab = scan_track(E3_TRAB, "TRABALHISTA")

    print("\n" + "=" * 72)
    print("RESUMO AGREGADO")
    print("=" * 72)

    total = 0
    if saude:
        _, totals, _ = saude
        print("\nSaude por regime:")
        for r, n in totals.items():
            print(f"  {r}: {n:,}")
            total += n
    if trab:
        _, totals, _ = trab
        print("\nTrabalhista por regime:")
        for r, n in totals.items():
            print(f"  {r}: {n:,}")
            total += n

    print(f"\nGrande total: {total:,}")
    print(f"Referencias esperadas:")
    print(f"  e2_report.md (saude)     : 5,136")
    print(f"  e2_report_trab (trabalhista): 5,006")
    print(f"  soma esperada            : 10,142")


if __name__ == "__main__":
    main()
