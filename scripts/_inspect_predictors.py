"""Inspect predictor data for all remaining scenarios."""
import sys, json
sys.path.insert(0, "C:/Workspace/academico/qfeng_validacao/src")
import pandas as pd

BASE = "C:/Workspace/academico/qfeng_validacao/data/predictors/"

for name, path in [
    ("obermeyer_bias", BASE + "obermeyer_bias/obermeyer_bias.parquet"),
    ("medicaid_access", BASE + "medicaid_access/medicaid_access.parquet"),
    ("eu_aiact_audit", BASE + "eu_aiact_audit/eu_aiact_audit.parquet"),
]:
    df = pd.read_parquet(path)
    print(f"\n{'='*50}")
    print(f"{name}: shape={df.shape}")
    print(f"cols: {list(df.columns)}")
    print(df.head(3).to_string())

print(f"\n{'='*50}")
print("advocacia_trabalhista_decisions.json:")
with open("C:/Workspace/academico/qfeng_validacao/data/hitl/hitl_cache/advocacia_trabalhista_decisions.json") as f:
    d = json.load(f)
print(f"type={type(d)}, keys/len={list(d.keys()) if isinstance(d, dict) else len(d)}")
if isinstance(d, dict):
    for k, v in list(d.items())[:3]:
        print(f"  {k}: {str(v)[:200]}")
elif isinstance(d, list):
    for item in d[:3]:
        print(f"  {str(item)[:200]}")
