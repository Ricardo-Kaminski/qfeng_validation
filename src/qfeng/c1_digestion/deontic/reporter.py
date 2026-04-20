"""E2 report generator — produces e2_report.md after batch extraction.

Collects statistics on DeonticAtom extraction: modality distribution,
confidence metrics, cache usage, and quality alerts.
"""

from __future__ import annotations

import json
import logging
import statistics
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from qfeng.c1_digestion.ingestion.labels import human_label
from qfeng.core.schemas import DeonticAtom, NormChunk

logger = logging.getLogger(__name__)


@dataclass
class E2BatchResult:
    """Resultado consolidado do batch E2."""

    total_chunks_in_corpus: int = 0
    total_chunks_processed: int = 0
    total_atoms_extracted: int = 0
    cache_hits: int = 0
    llm_calls: int = 0

    atoms_per_regime: dict[str, int] = field(default_factory=dict)
    atoms_per_chunk_type: dict[str, int] = field(default_factory=dict)
    modality_distribution: dict[str, int] = field(default_factory=dict)
    confidence_values: list[float] = field(default_factory=list)

    zero_atom_chunks: list[NormChunk] = field(default_factory=list)
    low_confidence_atoms: list[tuple[DeonticAtom, NormChunk]] = field(
        default_factory=list
    )
    sample_atoms: dict[str, list[tuple[DeonticAtom, NormChunk]]] = field(
        default_factory=dict
    )

    def record_extraction(
        self,
        chunk: NormChunk,
        atoms: list[DeonticAtom],
        from_cache: bool,
    ) -> None:
        """Registra o resultado de uma extração.

        Args:
            chunk: Chunk processado.
            atoms: Atoms extraídos.
            from_cache: Se o resultado veio do cache.
        """
        self.total_chunks_processed += 1
        regime = chunk.regime.value

        if from_cache:
            self.cache_hits += 1
        else:
            self.llm_calls += 1

        if not atoms:
            self.zero_atom_chunks.append(chunk)
            return

        self.total_atoms_extracted += len(atoms)
        self.atoms_per_regime[regime] = (
            self.atoms_per_regime.get(regime, 0) + len(atoms)
        )
        self.atoms_per_chunk_type[chunk.chunk_type] = (
            self.atoms_per_chunk_type.get(chunk.chunk_type, 0) + len(atoms)
        )

        for atom in atoms:
            self.modality_distribution[atom.modality.value] = (
                self.modality_distribution.get(atom.modality.value, 0) + 1
            )
            self.confidence_values.append(atom.confidence)

            if atom.confidence < 0.5:
                self.low_confidence_atoms.append((atom, chunk))

        # Coletar amostras (até 3 por regime)
        if regime not in self.sample_atoms:
            self.sample_atoms[regime] = []
        if len(self.sample_atoms[regime]) < 3:
            self.sample_atoms[regime].append((atoms[0], chunk))


def generate_e2_report(result: E2BatchResult, path: Path) -> None:
    """Gera relatório consolidado do E2 em Markdown.

    Args:
        result: Resultado do batch E2.
        path: Caminho para salvar o relatório.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        "# E2 Deontic Extraction Report",
        "",
        "## Resumo",
        "",
        f"- **Chunks no corpus:** {result.total_chunks_in_corpus}",
        f"- **Chunks processados:** {result.total_chunks_processed}",
        f"- **DeonticAtoms extraídos:** {result.total_atoms_extracted}",
        f"- **Cache hits:** {result.cache_hits}",
        f"- **LLM calls:** {result.llm_calls}",
        f"- **Chunks com 0 atoms:** {len(result.zero_atom_chunks)}",
        f"- **Atoms com confidence < 0.5:** {len(result.low_confidence_atoms)}",
        "",
    ]

    # Atoms por regime
    lines.extend([
        "## DeonticAtoms por Regime",
        "",
        "| Regime | Atoms |",
        "|--------|-------|",
    ])
    for regime, count in sorted(result.atoms_per_regime.items()):
        lines.append(f"| {regime} | {count} |")

    # Atoms por chunk_type
    lines.extend([
        "",
        "## DeonticAtoms por chunk_type",
        "",
        "| chunk_type | Atoms |",
        "|------------|-------|",
    ])
    for ctype, count in sorted(
        result.atoms_per_chunk_type.items(), key=lambda x: x[1], reverse=True
    ):
        lines.append(f"| {ctype} | {count} |")

    # Distribuição de modality
    lines.extend([
        "",
        "## Distribuição de Modality",
        "",
        "| Modality | Quantidade | % |",
        "|----------|-----------|---|",
    ])
    total_atoms = max(result.total_atoms_extracted, 1)
    for mod, count in sorted(
        result.modality_distribution.items(), key=lambda x: x[1], reverse=True
    ):
        pct = 100.0 * count / total_atoms
        lines.append(f"| {mod} | {count} | {pct:.1f}% |")

    # Métricas de confidence
    lines.extend([
        "",
        "## Métricas de Confidence",
        "",
    ])
    if result.confidence_values:
        mean_conf = statistics.mean(result.confidence_values)
        median_conf = statistics.median(result.confidence_values)
        below_07 = sum(1 for c in result.confidence_values if c < 0.7)
        pct_below = 100.0 * below_07 / len(result.confidence_values)
        lines.extend([
            f"- **Média:** {mean_conf:.3f}",
            f"- **Mediana:** {median_conf:.3f}",
            f"- **Abaixo de 0.7:** {below_07} ({pct_below:.1f}%)",
        ])
    else:
        lines.append("- Sem dados de confidence (nenhum atom extraído)")

    # Amostras por regime
    lines.extend([
        "",
        "## Amostras de DeonticAtoms (3 por regime)",
        "",
    ])
    for regime, samples in sorted(result.sample_atoms.items()):
        lines.append(f"### {regime.upper()}")
        lines.append("")
        for atom, chunk in samples:
            lines.append(f"**Chunk:** {human_label(chunk, 60)}")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(
                atom.model_dump(mode="json"),
                ensure_ascii=False,
                indent=2,
            ))
            lines.append("```")
            lines.append("")

    # Chunks com 0 atoms
    if result.zero_atom_chunks:
        lines.extend([
            "## Chunks com 0 DeonticAtoms",
            "",
        ])
        for chunk in result.zero_atom_chunks[:50]:
            lines.append(f"- {human_label(chunk, 60)}")
        if len(result.zero_atom_chunks) > 50:
            lines.append(
                f"\n*... e mais {len(result.zero_atom_chunks) - 50} chunks.*"
            )

    # Alertas: low confidence
    if result.low_confidence_atoms:
        lines.extend([
            "",
            "## Alertas: Atoms com Confidence < 0.5",
            "",
        ])
        for atom, chunk in result.low_confidence_atoms[:30]:
            lines.append(
                f"- **{atom.action}** (conf={atom.confidence:.2f}) "
                f"← {human_label(chunk, 50)}"
            )
        if len(result.low_confidence_atoms) > 30:
            lines.append(
                f"\n*... e mais {len(result.low_confidence_atoms) - 30} alertas.*"
            )

    path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Relatório E2 salvo em %s", path)
