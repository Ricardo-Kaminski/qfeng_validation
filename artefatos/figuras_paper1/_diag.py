from pathlib import Path
p = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1\Diagram2_QFENG_Engineering_v2.svg")
b = p.read_bytes()
print("size:", len(b), "bytes")
print("first 80 bytes (hex):", b[:80].hex())
print("first 80 bytes (repr):", repr(b[:80]))
print("---")
print("first 200 chars (utf-8):")
print(b[:200].decode("utf-8", errors="replace"))
