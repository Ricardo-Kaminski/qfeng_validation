"""
Diagnostico para F7: identificar por que 2114 atoms (41%) ficaram orfaos
no cruzamento cache <-> E1. Hipoteses a testar em ordem.
"""
import json
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = PROJECT_ROOT / "outputs" / "deontic_cache"
E1_DIR = PROJECT_ROOT / "outputs" / "e1_chunks"


def build_e1_index():
    """Retorna (set of chunk_ids em E1, dict regime->count, dict {id: source_law})."""
    ids = set()
    per_regime = Counter()
    id_to_source = {}
    for regime_dir in E1_DIR.iterdir():
        if not regime_dir.is_dir():
            continue
        regime = regime_dir.name
        for law_file in regime_dir.glob("*.json"):
            with law_file.open(encoding="utf-8") as f:
                chunks = json.load(f)
            for ch in chunks:
                cid = ch.get("id")
                if cid:
                    ids.add(cid)
                    per_regime[regime] += 1
                    id_to_source[cid] = (regime, ch.get("source"), law_file.name)
    return ids, per_regime, id_to_source


def scan_cache():
    """Retorna lista de (cache_filename_stem, source_chunk_id_within_atom)."""
    records = []
    empty_files = 0
    total_atoms = 0
    for cache_file in CACHE_DIR.glob("*.json"):
        stem = cache_file.stem
        with cache_file.open(encoding="utf-8") as f:
            atoms = json.load(f)
        if not isinstance(atoms, list) or len(atoms) == 0:
            empty_files += 1
            continue
        for atom in atoms:
            total_atoms += 1
            records.append((stem, atom.get("source_chunk_id")))
    return records, empty_files, total_atoms


def main():
    print("=" * 70)
    print("DIAGNOSTICO F7 - Orfaos no cruzamento cache <-> E1")
    print("=" * 70)

    e1_ids, e1_per_regime, e1_id_to_source = build_e1_index()
    print(f"\nE1: {len(e1_ids):,} chunk IDs unicos")
    for r, n in e1_per_regime.items():
        print(f"  {r}: {n:,}")

    records, empty_files, total_atoms = scan_cache()
    print(f"\nCACHE: {len(list(CACHE_DIR.glob('*.json'))):,} arquivos JSON")
    print(f"  Arquivos vazios (zero atoms): {empty_files:,}")
    print(f"  Total de atoms: {total_atoms:,}")

    # Hipotese 1: o nome do arquivo == source_chunk_id?
    stem_equal_src = sum(1 for s, sc in records if s == sc)
    stem_neq_src = sum(1 for s, sc in records if s != sc)
    print(f"\n[H1] filename_stem == atom.source_chunk_id?")
    print(f"  iguais   : {stem_equal_src:,}")
    print(f"  diferentes: {stem_neq_src:,}")
    if stem_neq_src > 0:
        sample = [(s, sc) for s, sc in records if s != sc][:5]
        print(f"  exemplos de diferentes (primeiros 5):")
        for s, sc in sample:
            print(f"    stem={s}  src={sc}")

    # Hipotese 2: stems do cache estao em E1?
    stems = set(r[0] for r in records)
    stem_in_e1 = sum(1 for s in stems if s in e1_ids)
    stem_notin_e1 = sum(1 for s in stems if s not in e1_ids)
    print(f"\n[H2] Stems do cache (unicos) encontrados em E1?")
    print(f"  cache stems unicos totais: {len(stems):,}")
    print(f"  em E1   : {stem_in_e1:,}")
    print(f"  fora E1 : {stem_notin_e1:,}")
    if stem_notin_e1 > 0:
        sample = [s for s in stems if s not in e1_ids][:5]
        print(f"  exemplos (primeiros 5): {sample}")

    # Hipotese 3: source_chunk_id dos atoms estao em E1?
    src_ids = set(r[1] for r in records if r[1])
    src_in_e1 = sum(1 for s in src_ids if s in e1_ids)
    src_notin_e1 = sum(1 for s in src_ids if s not in e1_ids)
    print(f"\n[H3] source_chunk_id dos atoms encontrados em E1?")
    print(f"  source_chunk_ids unicos: {len(src_ids):,}")
    print(f"  em E1   : {src_in_e1:,}")
    print(f"  fora E1 : {src_notin_e1:,}")

    # Contagem por resolucao final:
    # - via src (o que o script F7 faz)
    # - via stem (fallback alternativo)
    atoms_resolved_via_src = sum(1 for s, sc in records if sc in e1_ids)
    atoms_resolved_via_stem = sum(1 for s, sc in records if s in e1_ids)
    atoms_resolved_either = sum(1 for s, sc in records
                                if sc in e1_ids or s in e1_ids)
    print(f"\n[RESOLUCAO]")
    print(f"  atoms resolviveis via atom.source_chunk_id: {atoms_resolved_via_src:,}")
    print(f"  atoms resolviveis via filename_stem       : {atoms_resolved_via_stem:,}")
    print(f"  atoms resolviveis por QUALQUER            : {atoms_resolved_either:,}")
    print(f"  total de atoms                             : {total_atoms:,}")
    print(f"  orfaos (nenhuma resolucao)                 : {total_atoms - atoms_resolved_either:,}")


if __name__ == "__main__":
    main()
