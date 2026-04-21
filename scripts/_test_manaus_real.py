"""Preview real Manaus series from SIH data."""
import sys
sys.path.insert(0, "C:/Workspace/academico/qfeng_validacao/src")

from qfeng.e5_symbolic.manaus_sih_loader import load_manaus_real_series

series = load_manaus_real_series()

print(f"{'Label':<12} {'Internac':>8} {'Obitos':>7} {'t_mort':>7} {'t_uti':>7} {'t_resp':>7} {'score':>7} {'theta_t':>9}")
print("-" * 75)
for r in series:
    print(f"{r['label']:<12} {r['internacoes']:>8} {r['obitos']:>7} "
          f"{r['taxa_mortalidade']:>7.4f} {r['taxa_uti']:>7.4f} "
          f"{r['taxa_respiratorio']:>7.4f} {r['score_pressao']:>7.4f} "
          f"{r['theta_t']:>9.2f} deg")

print()
thetas = [r['theta_t'] for r in series]
scores = [r['score_pressao'] for r in series]
print("theta range:", min(thetas), "->", max(thetas))
print("jan/2021 theta:", thetas[3], "deg  (target: > 120)")
print("out/2020 theta:", thetas[0], "deg")
