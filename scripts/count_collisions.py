"""Count chunk_id collisions in an E1 output directory."""
import json
import pathlib
import sys
from collections import Counter

e1_dir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("outputs/e1_chunks_scoped")

id_counter: Counter = Counter()
total_chunks = 0
for jf in e1_dir.rglob("*.json"):
    if "concurrency_map" in jf.name:
        continue
    try:
        chunks = json.loads(jf.read_text(encoding="utf-8", errors="replace"))
        for c in chunks:
            cid = c.get("id", "")
            if cid:
                id_counter[cid] += 1
                total_chunks += 1
    except Exception as e:
        print(f"SKIP {jf.name}: {e}")

collisions = {k: v for k, v in id_counter.items() if v > 1}
print(f"Total chunks: {total_chunks}")
print(f"Total IDs unicos: {len(id_counter)}")
print(f"IDs com colisao (>1): {len(collisions)}")
print(f"Chunks afetados: {sum(collisions.values())}")
collision_rate = 100 * len(collisions) / len(id_counter) if id_counter else 0
print(f"Taxa de colisao: {collision_rate:.1f}%")
if collisions:
    top5 = sorted(collisions.items(), key=lambda x: -x[1])[:5]
    print("Top 5 colisoes:", top5)
