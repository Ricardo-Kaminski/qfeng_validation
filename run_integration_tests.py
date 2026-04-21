import clingo, pathlib, sys

BASE = pathlib.Path("C:/Workspace/academico/qfeng_validacao/corpora_clingo")

def load_files(paths):
    combined = ""
    for p in paths:
        combined += pathlib.Path(BASE / p).read_text(encoding="utf-8") + "\n"
    return combined

def run_test(name, files, expected, show_atoms=None):
    src = load_files(files)
    ctl = clingo.Control(["--models=0"])
    try:
        ctl.add("base", [], src)
        ctl.ground([("base", [])])
    except Exception as e:
        print(f"{name}: PARSE_ERROR: {e}")
        return
    result = ctl.solve()
    sat = result.satisfiable
    status = "SAT" if sat else "UNSAT"
    ok = (status == expected)
    mark = "OK" if ok else "FALHOU"

    active = []
    if sat and show_atoms:
        with ctl.solve(yield_=True) as handle:
            for model in handle:
                for atom in show_atoms:
                    if model.contains(clingo.Function(atom)):
                        active.append(atom)
                break

    print(f"[{mark}] {name}: {status} (esperado: {expected})")
    if active:
        print(f"      Atoms derivados: {active}")
    if not ok:
        print(f"      ATENCAO: resultado diverge do esperado!")

print("=" * 60)
print("TESTES DE INTEGRAÇÃO CLINGO — Q-FENG")
print("=" * 60)
print()

# C2 — Manaus — DEVE ser UNSAT
run_test("C2 Manaus", [
    "brasil/constitucional/cf88_principios_fundamentais.lp",
    "brasil/saude/sus_direito_saude.lp",
    "brasil/emergencia_manaus/emergencia_sanitaria.lp",
    "scenarios/c2_manaus_facts.lp",
], "UNSAT")

# C3 — Concentração regional — DEVE ser UNSAT
run_test("C3 Concentração", [
    "brasil/constitucional/cf88_principios_fundamentais.lp",
    "brasil/saude/sus_direito_saude.lp",
    "scenarios/c3_concentracao_facts.lp",
], "UNSAT")

# C7 — Obermeyer — DEVE ser UNSAT
run_test("C7 Obermeyer", [
    "usa/civil_rights/civil_rights_14th.lp",
    "usa/medicaid/medicaid_access.lp",
    "scenarios/c7_obermeyer_facts.lp",
], "UNSAT")

# T-CLT-01 — Citação fantasma — DEVE ser UNSAT
run_test("T-CLT-01 Mata v Avianca", [
    "brasil/constitucional/cf88_principios_fundamentais.lp",
    "brasil/trabalhista/clt_direitos_trabalhistas.lp",
    "brasil/processual/cpc_fundamentacao.lp",
    "scenarios/t_clt_01_facts.lp",
], "UNSAT")

# T-CLT-02 — Banco de horas sem CCT > 6 meses — DEVE ser UNSAT
run_test("T-CLT-02 Banco de horas sem CCT", [
    "brasil/trabalhista/clt_direitos_trabalhistas.lp",
    "scenarios/t_clt_02_facts.lp",
], "UNSAT")

# T-CLT-03 — Banco de horas COM CCT — DEVE ser SAT
run_test("T-CLT-03 Banco de horas com CCT", [
    "brasil/trabalhista/clt_direitos_trabalhistas.lp",
    "scenarios/t_clt_03_facts.lp",
], "SAT", show_atoms=["hour_bank_valid_with_cct"])

print()

# Contagem final por arquivo
print("=" * 60)
print("SYNTAX-CHECK + CONTAGEM — TODOS OS ARQUIVOS")
print("=" * 60)
import re

all_lp = sorted(BASE.rglob("*.lp"))
for f in all_lp:
    txt = f.read_text(encoding="utf-8")
    ctl2 = clingo.Control()
    try:
        ctl2.add("base", [], txt)
        ctl2.ground([("base", [])])
        syn = "OK"
    except Exception as e:
        syn = f"ERRO"
    s = len(re.findall(r"^sovereign\(", txt, re.MULTILINE))
    e = len(re.findall(r"^elastic\(", txt, re.MULTILINE))
    c = len(re.findall(r"^:-", txt, re.MULTILINE))
    rel = f.relative_to(BASE)
    print(f"{rel}: sovereign={s} elastic={e} constraints={c} | {syn}")
