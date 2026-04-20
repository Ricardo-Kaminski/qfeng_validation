# Spec: E4 — HITL Classification (SOVEREIGN / ELASTIC)
# ==========================================================
# Data: 2026-04-19
# Status: Aprovado para implementacao
# Modulo: src/qfeng/c1_digestion/hitl/
# Interface: Streamlit app local
# Granularidade: Amostragem estratificada por documento

---

## 1. Objetivo

O E4 e o modulo de revisao humana do pipeline C1. Seu proposito e classificar
cada ClingoPredicate gerado pelo E3 como:

- SOVEREIGN: predicado normativo inviolavel — representa uma restricao
  constitucional ou legal de ordem publica que nao pode ser afastada por
  autonomia privada, instrucao contratual ou decisao algorítmica.
  Gera o vetor |psi_S> no calculo de theta.

- ELASTIC: predicado normativo flexível — pode ser modulado por CCT,
  acordo individual, contexto operacional ou decisao discricionaria
  dentro dos limites legais. Contribui para a Elasticidade Ontologica.

A classificacao alimenta diretamente o E5 (Symbolic Testing):
- predicados SOVEREIGN -> constraints Clingo invioaveis -> |psi_S>
- predicados ELASTIC   -> fatos opcionais -> peso no alinhamento normativo

---

## 2. Decisoes arquiteturais

| Decisao                  | Escolha                                      |
|--------------------------|----------------------------------------------|
| Interface                | Streamlit app local (porta 8501)             |
| Granularidade            | Amostragem estratificada por documento       |
| Persistencia             | JSON incremental (hitl_cache/)               |
| Retomada                 | Checkpoint por predicate_id                  |
| Corpora suportados       | sus_validacao + advocacia_trabalhista        |
| Sinal Alhedonico         | Score de conflito interno (ver secao 5)      |
| Exportacao               | .lp separado por classe (sovereign/elastic/) |


---

## 3. Amostragem estratificada por documento

Em vez de revisar os 4.973 predicados individualmente, o E4 opera sobre uma
amostra representativa por documento-fonte, preservando a distribuicao de
modalidades (obligation / prohibition / permission / faculty).

Parametros:

| Corpus                  | n_per_doc | min_per_modality | seed |
|-------------------------|-----------|------------------|------|
| sus_validacao           | 30        | 5                | 42   |
| advocacia_trabalhista   | 40        | 5                | 42   |

Estimativa de carga de revisao:

| Corpus         | Documentos | n_per_doc | Total amostras |
|----------------|------------|-----------|----------------|
| sus_validacao  | 33         | 30        | ~990           |
| trabalhista    | 4          | 40        | ~160           |
| Total          |            |           | ~1.150         |

---

## 4. Estrutura de arquivos

src/qfeng/c1_digestion/hitl/
    __init__.py
    sampler.py          <- amostragem estratificada
    classifier.py       <- logica SOVEREIGN/ELASTIC + Sinal Alhedonico
    exporter.py         <- gera .lp separados por classe
    app.py              <- Streamlit UI
    __main__.py         <- entry point

data/hitl/
    samples/
        sus_validacao_sample.json
        advocacia_trabalhista_sample.json
    hitl_cache/
        sus_validacao_decisions.json
        advocacia_trabalhista_decisions.json

outputs/
    e4_sovereign/
        brasil/ eu/ usa/
    e4_elastic/
        brasil/ eu/ usa/


---

## 5. Sinal Alhedonico

Score [0.0, 1.0] que sinaliza conflito normativo detectavel automaticamente
antes da revisao humana. Componentes:

| Componente         | Peso | Condicao                                        |
|--------------------|------|-------------------------------------------------|
| concurrent_penalty | +0.4 | chunk_id tem par concorrente no mapa E1          |
| modality_conflict  | +0.3 | obligation vs prohibition no mesmo agent+action  |
| strength_mismatch  | +0.2 | constitutional vs infralegal no mesmo escopo     |
| low_confidence     | +0.1 | confidence E2 < 0.75                             |

Predicados com sinal > 0.5 sao destacados na interface Streamlit com
aviso de conflito normativo detectado e revisados primeiro.

---

## 6. sampler.py

```python
# src/qfeng/c1_digestion/hitl/sampler.py
from __future__ import annotations
import random
from pathlib import Path


def build_stratified_sample(
    e3_dir: Path,
    scope_name: str,
    n_per_doc: int = 30,
    min_per_modality: int = 5,
    seed: int = 42,
) -> list[dict]:
    rng = random.Random(seed)
    sample: list[dict] = []
    for lp_file in sorted(e3_dir.rglob("*.lp")):
        if lp_file.name == "concurrent_facts.lp":
            continue
        predicates = _parse_lp(lp_file)
        if not predicates:
            continue
        by_modality: dict[str, list[dict]] = {}
        for pred in predicates:
            by_modality.setdefault(pred.get("modality", "unknown"), []).append(pred)
        doc_sample: list[dict] = []
        for preds in by_modality.values():
            doc_sample.extend(rng.sample(preds, min(min_per_modality, len(preds))))
        already = {p["id"] for p in doc_sample}
        remaining = [p for p in predicates if p["id"] not in already]
        needed = max(0, n_per_doc - len(doc_sample))
        if needed and remaining:
            doc_sample.extend(rng.sample(remaining, min(needed, len(remaining))))
        for pred in doc_sample:
            pred["source_doc"] = lp_file.stem
            pred["scope"] = scope_name
        sample.extend(doc_sample)
    return sample


def _parse_lp(lp_file: Path) -> list[dict]:
    results = []
    for line in lp_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        if line.startswith("norm("):
            parts = line[5:].rstrip(").").split(",")
            if len(parts) >= 8:
                results.append({
                    "id": parts[0].strip(), "modality": parts[1].strip(),
                    "agent": parts[2].strip(), "patient": parts[3].strip(),
                    "action": parts[4].strip(), "regime": parts[5].strip(),
                    "strength": parts[6].strip(), "confidence": float(parts[7].strip()),
                    "rule": line, "source_doc": lp_file.stem,
                })
    return results
```


---

## 7. classifier.py

```python
# src/qfeng/c1_digestion/hitl/classifier.py
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json


@dataclass
class HITLDecision:
    predicate_id: str
    classification: str       # "SOVEREIGN" | "ELASTIC"
    alhedonic_signal: float
    reviewer_note: str = ""
    session_ts: str = ""


class DecisionCache:
    def __init__(self, cache_path: Path) -> None:
        self.path = cache_path
        self._data: dict[str, dict] = {}
        if cache_path.exists():
            self._data = json.loads(cache_path.read_text(encoding="utf-8"))

    def save(self, decision: HITLDecision) -> None:
        self._data[decision.predicate_id] = {
            "classification": decision.classification,
            "alhedonic_signal": decision.alhedonic_signal,
            "reviewer_note": decision.reviewer_note,
            "session_ts": decision.session_ts,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8")

    def get(self, predicate_id: str) -> dict | None:
        return self._data.get(predicate_id)

    def completed_ids(self) -> set[str]:
        return set(self._data.keys())

    def stats(self) -> dict:
        total = len(self._data)
        sovereign = sum(1 for v in self._data.values() if v["classification"] == "SOVEREIGN")
        return {"total": total, "sovereign": sovereign, "elastic": total - sovereign}
```

---

## 8. app.py — Interface Streamlit

```python
# src/qfeng/c1_digestion/hitl/app.py
import json, streamlit as st
from datetime import datetime
from pathlib import Path
from qfeng.c1_digestion.hitl.classifier import DecisionCache, HITLDecision

BASE        = Path("C:/Workspace/academico/qfeng_validacao")
SAMPLES_DIR = BASE / "data/hitl/samples"
CACHE_DIR   = BASE / "data/hitl/hitl_cache"

st.set_page_config(page_title="Q-FENG E4 HITL", layout="wide")
st.title("Q-FENG E4 — Classificacao SOVEREIGN / ELASTIC")

corpus = st.sidebar.selectbox("Corpus", ["sus_validacao", "advocacia_trabalhista"])
cache  = DecisionCache(CACHE_DIR / f"{corpus}_decisions.json")
stats  = cache.stats()

sample_path = SAMPLES_DIR / f"{corpus}_sample.json"
if not sample_path.exists():
    st.warning(f"Execute: python -m qfeng.c1_digestion.hitl --action sample --corpus {corpus}")
    st.stop()

sample = json.loads(sample_path.read_text(encoding="utf-8"))
total, done = len(sample), len(cache.completed_ids())

st.sidebar.metric("Total", total)
st.sidebar.metric("Revisados", done)
st.sidebar.metric("Restantes", total - done)
st.sidebar.progress(done / total if total else 0)
st.sidebar.metric("SOVEREIGN", stats["sovereign"])
st.sidebar.metric("ELASTIC",   stats["elastic"])

pending = sorted(
    [p for p in sample if p["id"] not in cache.completed_ids()],
    key=lambda p: p.get("alhedonic_signal", 0.0), reverse=True,
)
if not pending:
    st.success("Revisao completa. Execute --action export.")
    st.stop()

pred   = pending[0]
signal = pred.get("alhedonic_signal", 0.0)
if signal > 0.5:
    st.warning(f"Conflito normativo detectado — Sinal Alhedonico: {signal:.2f}")

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Predicado")
    st.code(pred["rule"], language="prolog")
    st.caption(f"Fonte: {pred['source_doc']} | Regime: {pred.get('regime','?')} | Strength: {pred.get('strength','?')}")
with col2:
    st.subheader("Metadados")
    for k in ["modality", "agent", "patient", "action"]:
        st.write(f"**{k.capitalize()}:** {pred.get(k, '?')}")
    st.write(f"**Confidence E2:** {pred.get('confidence', 0):.3f}")

st.divider()
note = st.text_input("Nota do revisor (opcional)")
c1, c2, c3 = st.columns(3)
ts = datetime.now().isoformat()
with c1:
    if st.button("SOVEREIGN", use_container_width=True, type="primary"):
        cache.save(HITLDecision(pred["id"], "SOVEREIGN", signal, note, ts)); st.rerun()
with c2:
    if st.button("ELASTIC", use_container_width=True):
        cache.save(HITLDecision(pred["id"], "ELASTIC",   signal, note, ts)); st.rerun()
with c3:
    if st.button("Pular (decidir depois)", use_container_width=True):
        sample.append(sample.pop(sample.index(pred)))
        sample_path.write_text(json.dumps(sample, ensure_ascii=False, indent=2))
        st.rerun()
```


---

## 9. exporter.py

```python
# src/qfeng/c1_digestion/hitl/exporter.py
from __future__ import annotations
from pathlib import Path
import json


def export_classified_lp(sample_path: Path, cache_path: Path, output_dir: Path) -> dict:
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    cache  = json.loads(cache_path.read_text(encoding="utf-8"))
    by_class: dict[str, dict] = {"sovereign": {}, "elastic": {}}
    for pred in sample:
        dec = cache.get(pred["id"])
        if not dec:
            continue
        cls    = dec["classification"].lower()
        regime = pred.get("regime", "brasil")
        doc    = pred.get("source_doc", "unknown")
        by_class[cls].setdefault(regime, {}).setdefault(doc, []).append(pred["rule"])
    stats = {"sovereign": 0, "elastic": 0}
    for cls, regimes in by_class.items():
        for regime, docs in regimes.items():
            regime_dir = output_dir / cls / regime
            regime_dir.mkdir(parents=True, exist_ok=True)
            for doc, rules in docs.items():
                (regime_dir / f"{doc}.lp").write_text("\n\n".join(rules), encoding="utf-8")
                stats[cls] += len(rules)
    return stats
```

---

## 10. Fluxo de execucao (comandos de uma linha)

Gerar amostra — saude:
python -m qfeng.c1_digestion.hitl --action sample --corpus sus_validacao

Gerar amostra — trabalhista:
python -m qfeng.c1_digestion.hitl --action sample --corpus advocacia_trabalhista

Abrir interface Streamlit:
python -m qfeng.c1_digestion.hitl --action review --corpus sus_validacao

Exportar .lp classificados:
python -m qfeng.c1_digestion.hitl --action export --corpus sus_validacao

---

## 11. Criterios de aprovacao (Fase B)

| Criterio                              | Threshold          |
|---------------------------------------|--------------------|
| Amostra gerada sem erro               | 100%               |
| Cobertura de modalidades por doc      | >= 4 modalities    |
| Interface Streamlit carrega           | OK                 |
| Checkpoint incremental funciona       | Retoma sessao      |
| Export gera sovereign/ e elastic/     | Ambos nao-vazios   |
| Taxa SOVEREIGN corpus saude           | Esperado 60-75%    |
| Taxa SOVEREIGN corpus trabalhista     | Esperado 70-80%    |

---

## 12. Notas para o paper

- A distribuicao SOVEREIGN/ELASTIC por regime (brasil/eu/usa) e dado primario
  do paper 1 — evidencia empirica de Elasticidade Ontologica diferenciada
  entre regimes normativos.
- O Sinal Alhedonico medio por documento e proxy de Friccao Ontologica
  estrutural — documentos com signal alto (ex: portarias Manaus) correspondem
  a zonas de alta tensao normativa empiricamente verificavel.
- Os 6 syntax_invalid do E3 trabalhista (0,25%) sao descartados silenciosamente
  na amostragem — nao afetam a validade estatistica.
- A taxa SOVEREIGN/ELASTIC por regime e o dado comparativo central do paper 1:
  hipotese — regimes com maior densidade constitucional (brasil) apresentam
  theta_efetivo medio mais alto que regimes com maior elasticidade contratual (usa).

---

## 13. O que NAO esta no escopo deste modulo

- Fine-tuning ou aprendizado ativo sobre as decisoes HITL
- Revisao colaborativa multi-anotador simultanea
- Integracao com banco de dados externo (Neo4j, Postgres)
- Calculo de theta ou theta_efetivo (responsabilidade do E5)
- Validacao de concordancia inter-anotador automatica (pode ser adicionado em V2)
