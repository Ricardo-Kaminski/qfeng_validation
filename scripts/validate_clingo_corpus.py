"""
Valida o corpus Clingo executando cada cenário ativo.

Cada cenário é executado com os arquivos normativos relevantes carregados
em conjunto. Reporta SAT/UNSAT/UNKNOWN e detecta regressões introduzidas
pelas correções aplicadas em 26/abr/2026.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent / "corpora_clingo"

# Mapeamento canônico cenário -> conjunto de arquivos
SCENARIOS = {
    "C2_Manaus": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/saude/sus_direito_saude.lp",
        "brasil/emergencia_manaus/emergencia_sanitaria.lp",
        "scenarios/c2_manaus_facts.lp",
    ],
    "C3_Concentracao": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/saude/sus_direito_saude.lp",
        "scenarios/c3_concentracao_facts.lp",
    ],
    "C7_Obermeyer": [
        "usa/civil_rights/civil_rights_14th.lp",
        "usa/medicaid/medicaid_access.lp",
        "scenarios/c7_obermeyer_facts.lp",
    ],
    "T_CLT_01_Mata_Avianca": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_01_facts.lp",
    ],
    "T_CLT_02_Sumula85_Distorcida": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_02_facts.lp",
    ],
    "T_CLT_03_Banco_Horas_CCT": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_03_facts.lp",
    ],
    "T_CLT_04_Citacao_Fundamentada": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_04_facts.lp",
    ],
}

# Resultado esperado por cenário
EXPECTED = {
    "C2_Manaus": "UNSAT",
    "C3_Concentracao": "UNSAT",
    "C7_Obermeyer": "UNSAT",
    "T_CLT_01_Mata_Avianca": "UNSAT",
    "T_CLT_02_Sumula85_Distorcida": "UNSAT",
    "T_CLT_03_Banco_Horas_CCT": "SAT",
    "T_CLT_04_Citacao_Fundamentada": "SAT",
}

PYTHON = sys.executable


def run_clingo(files: list[str]) -> str:
    cmd = [PYTHON, "-m", "clingo", "--mode=clingo", "0"] + [
        str(ROOT / f) for f in files
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        out = (result.stdout + result.stderr).lower()
        if "unsatisfiable" in out:
            return "UNSAT"
        if "satisfiable" in out:
            return "SAT"
        if "unknown" in out:
            return "UNKNOWN"
        return f"PARSE_ERROR: {result.stdout[:300]}"
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"


def main() -> None:
    print("=" * 72)
    print("VALIDAÇÃO INTEGRADA DO CORPUS CLINGO Q-FENG — 26/abr/2026")
    print("=" * 72)
    print()

    results: dict[str, tuple[str, str, str]] = {}
    for scenario, files in SCENARIOS.items():
        actual = run_clingo(files)
        expected = EXPECTED[scenario]
        status = "OK" if actual == expected else "FAIL"
        results[scenario] = (actual, expected, status)
        print(f"[{status:4}] {scenario}: {actual} (esperado: {expected})")

    print()
    print("=" * 72)
    failures = [s for s, (_, _, st) in results.items() if st == "FAIL"]
    if failures:
        print(f"FALHAS DETECTADAS ({len(failures)}/{len(SCENARIOS)}):")
        for f in failures:
            a, e, _ = results[f]
            print(f"  - {f}: obtido {a}, esperado {e}")
        print("\nReportar ao chat para análise.")
        sys.exit(1)
    else:
        print(f"TODOS OS {len(SCENARIOS)} CENÁRIOS VALIDADOS COM SUCESSO.")
    print("=" * 72)


if __name__ == "__main__":
    main()
