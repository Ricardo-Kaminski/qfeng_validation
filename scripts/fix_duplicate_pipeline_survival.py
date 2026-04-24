#!/usr/bin/env python3
"""
Remove a duplicacao do paragrafo 'Pipeline survival E2' no Paper 1.

O paragrafo aparece duas vezes identicas (provavelmente porque o script
apply_4_4_e3_survival_sentence.py foi executado duas vezes sem checar
idempotencia). Este script detecta e remove a segunda ocorrencia.

Uso:
    python scripts/fix_duplicate_pipeline_survival.py docs/papers/PAPER1_QFENG_VALIDATION.md
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

    text = path.read_text(encoding="utf-8")

    marker = "**Pipeline survival E2"
    count = text.count(marker)
    print(f"Ocorrencias de '{marker}': {count}")

    if count == 1:
        print("Ja esta OK (apenas uma ocorrencia). Nada a fazer.")
        return
    if count == 0:
        print("ERRO: o paragrafo nao esta presente. Rodar "
              "apply_4_4_e3_survival_sentence.py antes.")
        sys.exit(1)
    if count != 2:
        print(f"ERRO: esperava 1 ou 2 ocorrencias, encontrou {count}. Abortando.")
        sys.exit(1)

    # Localiza as duas ocorrencias
    first = text.find(marker)
    second = text.find(marker, first + 1)
    # O paragrafo termina em "discussed in Section 7.4.\n\n". Vou procurar esse delimitador.
    end_marker = "discussed in Section 7.4."
    # Fim do primeiro paragrafo
    first_end = text.find(end_marker, first) + len(end_marker)
    # Fim do segundo paragrafo
    second_end = text.find(end_marker, second) + len(end_marker)

    # Verificar que os dois paragrafos sao textualmente identicos
    p1 = text[first:first_end]
    p2 = text[second:second_end]
    if p1 != p2:
        print("ERRO: as duas ocorrencias nao sao identicas. Inspecionar manualmente.")
        print(f"--- p1 ---\n{p1[:300]}...")
        print(f"--- p2 ---\n{p2[:300]}...")
        sys.exit(1)

    # Remover a segunda ocorrencia inteira, incluindo o '\n\n' que a separa do primeiro
    # Entre first_end e second: deve ter '\n\n' (separador de paragrafos em markdown)
    between = text[first_end:second]
    print(f"Separador entre as duas ocorrencias: {repr(between)}")

    # Remover [first_end .. second_end]
    new_text = text[:first_end] + text[second_end:]
    # Limpeza: garantir que so exista um '\n\n' apos o paragrafo unico
    # (isto e, remover '\n\n' extras que possam ter ficado)

    backup = path.with_suffix(path.suffix + ".bak2")
    shutil.copy2(path, backup)
    print(f"\nBackup criado: {backup}")

    path.write_text(new_text, encoding="utf-8")

    size_before = len(text)
    size_after = len(new_text)
    print(f"Deduplicacao aplicada.")
    print(f"Tamanho antes : {size_before:,} chars")
    print(f"Tamanho depois: {size_after:,} chars")
    print(f"Delta         : {size_after - size_before:,} chars")

    # Pos-verificacao
    count_after = new_text.count(marker)
    status = "[OK]" if count_after == 1 else "[!!]"
    print(f"\n{status} ocorrencias de '{marker}' apos deduplicacao: {count_after}")


if __name__ == "__main__":
    main()
