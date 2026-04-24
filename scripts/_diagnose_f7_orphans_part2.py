"""
Diagnostico complementar F7:
1. Contar atoms em deontic_cache_trabalhista/
2. Checar se existem parquets/pickles de atoms em outros lugares
3. Verificar timestamp de e2_report.md vs. ultimo arquivo do cache
"""
import json
from collections import Counter
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = PROJECT_ROOT / "outputs"


def scan_cache(cache_dir: Path):
    n_files = 0
    n_empty = 0
    n_atoms = 0
    modality_counter = Counter()
    for cache_file in cache_dir.glob("*.json"):
        n_files += 1
        with cache_file.open(encoding="utf-8") as f:
            atoms = json.load(f)
        if not isinstance(atoms, list) or len(atoms) == 0:
            n_empty += 1
            continue
        for atom in atoms:
            n_atoms += 1
            mod = atom.get("modality")
            if mod:
                modality_counter[mod] += 1
    return n_files, n_empty, n_atoms, modality_counter


def scan_e1_chunks(e1_dir: Path):
    """Retorna {chunk_id: regime} a partir de diretorios agrupados por regime."""
    mapping = {}
    per_regime = Counter()
    for regime_dir in e1_dir.iterdir():
        if not regime_dir.is_dir():
            continue
        regime = regime_dir.name
        for law_file in regime_dir.glob("*.json"):
            with law_file.open(encoding="utf-8") as f:
                chunks = json.load(f)
            for ch in chunks:
                cid = ch.get("id")
                if cid:
                    mapping[cid] = regime
                    per_regime[regime] += 1
    return mapping, per_regime


def scan_e1_chunks_flat(e1_dir: Path):
    """Para diretorios que nao sao por-regime (como e1_chunks_scoped)."""
    mapping = {}
    per_regime = Counter()
    for law_file in e1_dir.rglob("*.json"):
        try:
            with law_file.open(encoding="utf-8") as f:
                chunks = json.load(f)
        except Exception:
            continue
        if not isinstance(chunks, list):
            continue
        for ch in chunks:
            if not isinstance(ch, dict):
                continue
            cid = ch.get("id")
            reg = ch.get("regime", "unknown")
            if cid:
                mapping[cid] = reg
                per_regime[reg] += 1
    return mapping, per_regime


def find_parquets_and_pickles():
    """Procura por arquivos *.parquet, *.pkl, *.pickle em outputs/"""
    return (
        sorted(OUTPUTS.rglob("*.parquet"))
        + sorted(OUTPUTS.rglob("*.pkl"))
        + sorted(OUTPUTS.rglob("*.pickle"))
    )


def main():
    print("=" * 72)
    print("DIAGNOSTICO F7 - PARTE 2")
    print("=" * 72)

    # ---- Cache saude ----
    print("\n[1] deontic_cache/ (saude)")
    cache = OUTPUTS / "deontic_cache"
    n_files, n_empty, n_atoms, mod_counter = scan_cache(cache)
    print(f"  arquivos: {n_files:,}   vazios: {n_empty:,}   atoms: {n_atoms:,}")
    for m, n in sorted(mod_counter.items(), key=lambda x: -x[1]):
        print(f"    {m:<12}: {n:>6,}")

    # ---- Cache trabalhista ----
    print("\n[2] deontic_cache_trabalhista/")
    cache_t = OUTPUTS / "deontic_cache_trabalhista"
    n_files_t, n_empty_t, n_atoms_t, mod_counter_t = scan_cache(cache_t)
    print(f"  arquivos: {n_files_t:,}   vazios: {n_empty_t:,}   atoms: {n_atoms_t:,}")
    for m, n in sorted(mod_counter_t.items(), key=lambda x: -x[1]):
        print(f"    {m:<12}: {n:>6,}")

    # ---- Cruzar trabalhista com seu E1 ----
    print("\n[3] e1_chunks_trabalhista/")
    e1_t = OUTPUTS / "e1_chunks_trabalhista"
    if e1_t.exists():
        # trabalhista pode ser flat (nao separado por regime) ou hierarquico
        subdirs = [p for p in e1_t.iterdir() if p.is_dir()]
        if subdirs:
            print(f"  estrutura: hierarquica ({len(subdirs)} subdiretorios)")
            map_t, per_reg_t = scan_e1_chunks(e1_t)
        else:
            print(f"  estrutura: flat (arquivos diretos)")
            map_t, per_reg_t = scan_e1_chunks_flat(e1_t)
        print(f"  chunks indexados: {len(map_t):,}")
        for r, n in per_reg_t.items():
            print(f"    {r}: {n:,}")
    else:
        print("  DIRETORIO NAO EXISTE")

    # ---- e1_chunks_scoped ----
    print("\n[4] e1_chunks_scoped/")
    e1_s = OUTPUTS / "e1_chunks_scoped"
    if e1_s.exists():
        subdirs = [p for p in e1_s.iterdir() if p.is_dir()]
        if subdirs:
            print(f"  estrutura: hierarquica ({len(subdirs)} subdiretorios)")
            for sd in subdirs:
                n_f = len(list(sd.glob("*.json")))
                print(f"    {sd.name}: {n_f} arquivos")
        else:
            n_f = len(list(e1_s.glob("*.json")))
            print(f"  estrutura: flat ({n_f} arquivos)")
        map_s, per_reg_s = scan_e1_chunks_flat(e1_s)
        print(f"  chunks indexados (total): {len(map_s):,}")
        for r, n in per_reg_s.items():
            print(f"    {r}: {n:,}")
    else:
        print("  DIRETORIO NAO EXISTE")

    # ---- Parquets / Pickles ----
    print("\n[5] Arquivos .parquet / .pkl / .pickle em outputs/")
    pqs = find_parquets_and_pickles()
    for p in pqs:
        rel = p.relative_to(OUTPUTS)
        size_kb = p.stat().st_size / 1024
        print(f"    {rel}  ({size_kb:,.1f} KB)")

    # ---- Timestamps ----
    print("\n[6] Timestamps: e2_report.md vs ultimo JSON no cache")
    report = OUTPUTS / "e2_report.md"
    cache_files = sorted(cache.glob("*.json"), key=lambda p: p.stat().st_mtime)
    if report.exists() and cache_files:
        t_report = datetime.fromtimestamp(report.stat().st_mtime)
        t_first = datetime.fromtimestamp(cache_files[0].stat().st_mtime)
        t_last = datetime.fromtimestamp(cache_files[-1].stat().st_mtime)
        print(f"  e2_report.md      : {t_report}")
        print(f"  cache primeiro    : {t_first}")
        print(f"  cache ultimo      : {t_last}")
        if t_report < t_last:
            print(f"  !! CACHE foi modificado APOS e2_report (pode estar dessincronizado)")
        elif t_report > t_last:
            print(f"  !! REPORT e mais recente que todo o cache saude "
                  f"(pode ter sido gerado de outra fonte, ex. parquet)")
        else:
            print("  (sincronizados)")


if __name__ == "__main__":
    main()
