from pathlib import Path
t = Path("docs/papers/PAPER1_QFENG_VALIDATION.md").read_text(encoding="utf-8")
print("Pipeline survival count:", t.count("Pipeline survival E2"))
print("Single-HITL count:", t.count("Single HITL reviewer"))
print("Limitations heading count:", t.count("### 7.4 Limitations"))
