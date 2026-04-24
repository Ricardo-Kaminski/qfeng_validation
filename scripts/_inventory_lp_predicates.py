"""Lista todos os nomes de predicados Clingo distintos encontrados nos .lp
e conta suas ocorrencias, para identificar o mapeamento real modality <-> predicate.
"""
import re
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIRS = [
    PROJECT_ROOT / "outputs" / "e3_predicates",
    PROJECT_ROOT / "outputs" / "e3_predicates_trabalhista",
]

PRED_RE = re.compile(r"^([a-z_][a-z0-9_]*)\s*\(", re.IGNORECASE)


def main():
    print("=" * 72)
    print("INVENTARIO DE PREDICADOS Clingo em e3_predicates*")
    print("=" * 72)

    counter_by_track = {}
    all_counter = Counter()

    for root in DIRS:
        track = root.name
        counter_by_track[track] = Counter()
        for lp in root.rglob("*.lp"):
            with lp.open(encoding="utf-8", errors="replace") as f:
                for line in f:
                    s = line.strip()
                    if not s or s.startswith("%"):
                        continue
                    m = PRED_RE.match(s)
                    if m:
                        name = m.group(1).lower()
                        counter_by_track[track][name] += 1
                        all_counter[name] += 1

    print(f"\n=== Agregado (ambas trilhas) ===")
    print(f"{'predicate':<30} {'count':>8}")
    for name, n in all_counter.most_common():
        print(f"  {name:<28} {n:>8,}")

    for track, cnt in counter_by_track.items():
        print(f"\n=== {track} ===")
        for name, n in cnt.most_common():
            print(f"  {name:<28} {n:>8,}")


if __name__ == "__main__":
    main()
