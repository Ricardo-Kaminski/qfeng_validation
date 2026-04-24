#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove stale figure-description paragraphs left over from the old placeholder system.

The old docx had Normal-style paragraphs like:
  "Figure 2. Born-rule vs. classical Bayesian probability..."
  "Figure 3. Manaus theta-efetivo dual-axis time series..."
that described what figures WOULD look like. After the surgery, real captions
(Caption-style) were inserted. The old descriptive texts are now stale and must go.

We only remove paragraphs that:
  - are Normal/FirstParagraph style (not Caption, not Heading)
  - start with "Figure N." where N is 1-7
  - are NOT adjacent to (i.e., immediately after) an image paragraph
"""
from __future__ import annotations

import shutil
import sys
from datetime import datetime
from pathlib import Path

from docx import Document  # type: ignore[import-untyped]

DOCX = Path(
    r"C:\Workspace\academico\qfeng_validacao\docs\papers\PAPER1_QFENG_FINAL_editando.docx"
)

# Exact strings to identify stale paragraphs (match by startswith)
STALE_PREFIXES = [
    "Figure 2. Born-rule vs. classical Bayesian probability",
    "Figure 3. Manaus theta-efetivo dual-axis time series",
]


def _para_has_image(p) -> bool:  # type: ignore[no-untyped-def]
    return "a:blip" in p._p.xml


def main() -> None:
    if not DOCX.exists():
        print(f"ABORT: {DOCX} not found", file=sys.stderr)
        sys.exit(1)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = DOCX.with_name(DOCX.stem + f".pre_cleanup_{ts}.docx")
    shutil.copy2(DOCX, bak)
    print(f"Backup: {bak}", file=sys.stderr)

    doc = Document(DOCX)
    paras = list(doc.paragraphs)
    removed = []

    for i, p in enumerate(paras):
        txt = p.text.strip()
        style_name = p.style.name if p.style else "Normal"

        # Only touch Normal/body paragraphs — never Caption, Heading, etc.
        if "Heading" in style_name or "Caption" in style_name:
            continue

        for prefix in STALE_PREFIXES:
            if txt.startswith(prefix):
                # Extra safety: the previous paragraph should NOT be an image
                # (if it were, this might be a real caption we just re-styled)
                prev_has_img = i > 0 and _para_has_image(paras[i - 1])
                if prev_has_img:
                    print(
                        f"SKIP (adjacent to image): para[{i}] {txt[:60]!r}",
                        file=sys.stderr,
                    )
                    continue
                print(f"REMOVING para[{i}] {txt[:80]!r}", file=sys.stderr)
                p._p.getparent().remove(p._p)
                removed.append(txt[:80])
                break

    if not removed:
        print("Nothing to remove — docx already clean.", file=sys.stderr)
        bak.unlink()
        return

    doc.save(DOCX)
    print(f"\nRemoved {len(removed)} stale paragraph(s). Saved: {DOCX}", file=sys.stderr)
    for t in removed:
        print(f"  - {t!r}", file=sys.stderr)


if __name__ == "__main__":
    main()
