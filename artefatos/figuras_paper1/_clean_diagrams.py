"""
_clean_diagrams.py
==================
Auditor + cleaner de SVGs do Q-FENG Paper 1.

Tarefas:
1. Substituir 'dPASP' -> 'Clingo (ASP)' em todos os SVGs.
2. Remover textos de TÍTULO no topo (class="title" ou "section-head").
3. Remover textos de CAPTION no rodapé (class="caption").
4. Salvar versão limpa em <nome>_clean.svg, preservando original.

Uso: python _clean_diagrams.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1")

def clean_svg(text: str) -> tuple[str, dict]:
    stats = {"dpasp_replaced": 0, "title_removed": 0, "caption_removed": 0,
             "section_head_removed": 0, "figure_text_removed": 0}

    # 1. dPASP -> Clingo (ASP)
    new = text.replace("dPASP solver (Clingo)", "Clingo (ASP) solver")
    new = new.replace("dPASP solver", "Clingo (ASP) solver")
    new = new.replace("dPASP", "Clingo (ASP)")
    stats["dpasp_replaced"] = (text.count("dPASP") - new.count("dPASP"))

    # 2. Remover <text class="title">...</text> (e variantes)
    pattern_title = re.compile(
        r'<text[^>]*class\s*=\s*["\']title["\'][^>]*>.*?</text>\s*',
        re.DOTALL | re.IGNORECASE
    )
    matches_title = pattern_title.findall(new)
    stats["title_removed"] = len(matches_title)
    new = pattern_title.sub("", new)

    # 3. Remover <text class="caption">...</text>
    pattern_caption = re.compile(
        r'<text[^>]*class\s*=\s*["\']caption["\'][^>]*>.*?</text>\s*',
        re.DOTALL | re.IGNORECASE
    )
    matches_caption = pattern_caption.findall(new)
    stats["caption_removed"] = len(matches_caption)
    new = pattern_caption.sub("", new)

    # 4. Remover <text class="section-head">...</text>
    pattern_sh = re.compile(
        r'<text[^>]*class\s*=\s*["\']section-head["\'][^>]*>.*?</text>\s*',
        re.DOTALL | re.IGNORECASE
    )
    matches_sh = pattern_sh.findall(new)
    stats["section_head_removed"] = len(matches_sh)
    new = pattern_sh.sub("", new)

    # 5. Remover qualquer <text> que comece com "Figure N." ou "Figura N."
    #    (independentemente da classe — captura títulos não classificados)
    pattern_fig = re.compile(
        r'<text[^>]*>\s*(?:Figure|Figura)\s+\d+[^<]*</text>\s*',
        re.IGNORECASE
    )
    matches_fig = pattern_fig.findall(new)
    stats["figure_text_removed"] = len(matches_fig)
    new = pattern_fig.sub("", new)

    return new, stats


def main():
    svgs = sorted(ROOT.rglob("*.svg"))
    print(f"[scan] {len(svgs)} SVG files under {ROOT}")
    summary = []
    for src in svgs:
        # Skip já-limpos (_clean.svg) para não criar _clean_clean.svg
        if src.stem.endswith("_clean"):
            continue
        try:
            txt = src.read_text(encoding="utf-8")
        except Exception as e:
            print(f"[skip] {src.name}: read error {e}")
            continue
        new_txt, stats = clean_svg(txt)
        if any(v > 0 for v in stats.values()):
            dst = src.with_name(src.stem + "_clean.svg")
            dst.write_text(new_txt, encoding="utf-8")
            rel = src.relative_to(ROOT)
            summary.append((str(rel), stats, dst.name))
            print(f"[OK] {rel}")
            for k, v in stats.items():
                if v > 0:
                    print(f"      {k}: {v}")
        else:
            print(f"[--] {src.relative_to(ROOT)} (no changes needed)")

    print("\n=== SUMMARY ===")
    print(f"Files modified: {len(summary)}")
    for rel, stats, dst in summary:
        print(f"  {rel} -> {dst}")
        print(f"    {stats}")


if __name__ == "__main__":
    main()
