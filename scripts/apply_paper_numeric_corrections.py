#!/usr/bin/env python3
"""
Aplica as 4 correcoes cirurgicas no paper Q-FENG para converter 98.4%/420/4 failures
para os valores corretos 97.96%/245/5 failures derivados do parquet threshold_robustness.parquet.

Uso:
    python apply_paper_numeric_corrections.py <caminho_para_PAPER1_QFENG_VALIDATION.md>

Exemplo:
    python scripts/apply_paper_numeric_corrections.py docs/papers/PAPER1_QFENG_VALIDATION.md

Valida que cada old_str aparece exatamente uma vez antes de aplicar.
Salva backup .bak antes de sobrescrever.
"""
import sys
import shutil
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <caminho_md>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERRO: arquivo nao encontrado: {path}")
        sys.exit(1)

    text = path.read_text(encoding='utf-8')
    original_len = len(text)

    edits = [
        # Edit 1 - Abstract
        (
            "Abstract",
            "Threshold robustness analysis across 420 parameter combinations confirmed 98.6% regime stability.",
            "Threshold robustness analysis across 245 evaluations (5 \u00d7 7 threshold combinations \u00d7 7 scenarios) confirmed 97.96% regime stability, with all five failures concentrated exclusively at \u03b8_block = 130\u00b0 for scenario T-CLT-02 (\u03b8 = 127.81\u00b0) and 100% stability at \u03b8_block \u2264 125\u00b0."
        ),
        # Edit 2 - Secao 6.1 narrative
        (
            "6.1 narrative",
            "Results: 241 of 245 evaluations (98.4%) produced the same regime classification as the paper-reported values (\u03b8_stac = 30\u00b0, \u03b8_block = 120\u00b0). The four failures occurred exclusively at \u03b8_block = 130\u00b0 for scenario T-CLT-02 (\u03b8 = 127.81\u00b0), which is the only scenario within 3\u00b0 of any tested threshold boundary. No failures occurred at the paper-reported thresholds or for any scenario other than T-CLT-02. This confirms that the CB classification is stable for all scenarios except T-CLT-02 at the extreme boundary of the tested range.",
            "Results: 240 of 245 evaluations (97.96%) produced the same regime classification as the paper-reported values (\u03b8_stac = 30\u00b0, \u03b8_block = 120\u00b0). The five failures occurred exclusively at \u03b8_block = 130\u00b0 for scenario T-CLT-02 (\u03b8 = 127.81\u00b0), which is 2.19\u00b0 below this boundary \u2014 the only scenario whose \u03b8 falls between any tested CB threshold pair. No failures occurred at the paper-reported thresholds or for any scenario other than T-CLT-02; at \u03b8_block \u2264 125\u00b0 the correctness rate is 100% (210/210). This confirms that the CB classification is stable for all scenarios except T-CLT-02 at the extreme upper end of the tested \u03b8_block range."
        ),
        # Edit 3 - Tabela 6 linha T-CLT-02
        (
            "Tabela 6 T-CLT-02",
            "| T-CLT-02 | 127.81 | 88.6% | 100% | 4/35 | \u03b8_block = 130\u00b0 |",
            "| T-CLT-02 | 127.81 | 85.71% | 100% | 5/35 | \u03b8_block = 130\u00b0 |"
        ),
        # Edit 4 - Tabela 6 Overall
        (
            "Tabela 6 Overall",
            "| **Overall** | \u2014 | **98.4%** | **100%** | **4/245** | \u2014 |",
            "| **Overall** | \u2014 | **97.96%** | **100%** | **5/245** | \u2014 |"
        ),
    ]

    # Validar
    print("=" * 70)
    print("VALIDACAO: cada old_str deve aparecer exatamente 1x")
    print("=" * 70)
    all_ok = True
    for name, old, new in edits:
        count = text.count(old)
        status = "OK" if count == 1 else f"FAIL (count={count})"
        print(f"  [{status}] {name}")
        if count != 1:
            all_ok = False

    if not all_ok:
        print("\nABORTANDO. Nenhuma mudanca aplicada.")
        sys.exit(1)

    # Backup
    backup_path = path.with_suffix(path.suffix + '.bak')
    shutil.copy2(path, backup_path)
    print(f"\nBackup criado: {backup_path}")

    # Aplicar
    for name, old, new in edits:
        text = text.replace(old, new, 1)

    # Gravar
    path.write_text(text, encoding='utf-8')
    new_len = len(text)

    print(f"\nCorrecoes aplicadas com sucesso.")
    print(f"Tamanho antes : {original_len} chars")
    print(f"Tamanho depois: {new_len} chars")
    print(f"Delta         : {new_len - original_len:+d} chars")

    # Verificar ausencia de valores antigos
    print("\n=== Pos-verificacao (valores antigos devem ter sumido) ===")
    old_markers = ["420 parameter combinations", "98.6%", "241 of 245", "98.4%", "88.6%", "4/245", "The four failures"]
    for m in old_markers:
        cnt = text.count(m)
        status = "OK" if cnt == 0 else f"AINDA PRESENTE ({cnt}x)"
        print(f"  [{status}] '{m}'")


if __name__ == '__main__':
    main()
