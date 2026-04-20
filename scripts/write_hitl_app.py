"""Bootstrap: writes the HITL app.py with navigation support."""
import pathlib

APP = pathlib.Path(__file__).parents[1] / "src" / "qfeng" / "c1_digestion" / "hitl" / "app.py"

CONTENT = '''\
"""E4 HITL — Streamlit UI for SOVEREIGN/ELASTIC classification."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

from qfeng.c1_digestion.hitl.classifier import DecisionCache, HITLDecision

BASE = Path(__file__).parents[4]
SAMPLES_DIR = BASE / "data" / "hitl" / "samples"
CACHE_DIR = BASE / "data" / "hitl" / "hitl_cache"

st.set_page_config(page_title="Q-FENG E4 HITL", layout="wide")
st.title("Q-FENG E4 — Classificação SOVEREIGN / ELASTIC")

_default_corpus = "sus_validacao"
for _arg in sys.argv:
    if _arg.startswith("--corpus="):
        _default_corpus = _arg.split("=", 1)[1]
        break

corpus = st.sidebar.selectbox(
    "Corpus",
    ["sus_validacao", "advocacia_trabalhista"],
    index=["sus_validacao", "advocacia_trabalhista"].index(_default_corpus)
    if _default_corpus in ["sus_validacao", "advocacia_trabalhista"]
    else 0,
)

sample_path = SAMPLES_DIR / f"{corpus}_sample.json"
if not sample_path.exists():
    st.warning(
        "Amostra não encontrada. Execute:\\n\\n"
        f"```bash\\npython -m qfeng.c1_digestion.hitl --action sample --corpus {corpus}\\n```"
    )
    st.stop()

sample: list[dict] = json.loads(sample_path.read_text(encoding="utf-8"))
sample_by_id: dict[str, dict] = {p["id"]: p for p in sample}

if "editing_id" not in st.session_state:
    st.session_state.editing_id = None

cache = DecisionCache(CACHE_DIR / f"{corpus}_decisions.json")
stats = cache.stats()
completed = cache.completed_ids()

total = len(sample)
done = len(completed)

# ── Sidebar: métricas ──────────────────────────────────────────────────────
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Corpus:** `{corpus}`")
st.sidebar.metric("Total", total)
st.sidebar.metric("Revisados", done)
st.sidebar.metric("Restantes", total - done)
st.sidebar.progress(done / total if total else 0)
st.sidebar.metric("SOVEREIGN", stats["sovereign"])
st.sidebar.metric("ELASTIC", stats["elastic"])
st.sidebar.metric("Pulados", stats["skipped"])

# ── Sidebar: histórico com botão Corrigir ──────────────────────────────────
recent = cache.last_decisions(n=15)
if recent:
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Revisões recentes** _(Fix para corrigir)_")
    for pred_id, dec in recent:
        pred_meta = sample_by_id.get(pred_id, {})
        label = pred_meta.get("source_doc", pred_id[:10])
        cls = dec["classification"]
        badge = "[S]" if cls == "SOVEREIGN" else ("[E]" if cls == "ELASTIC" else "[~]")
        col_label, col_btn = st.sidebar.columns([3, 1])
        col_label.caption(f"{badge} {label[:28]}")
        if col_btn.button("Fix", key=f"edit_{pred_id}", help=f"Corrigir: {cls}"):
            st.session_state.editing_id = pred_id
            st.rerun()

# ── Determinar predicado atual ─────────────────────────────────────────────
editing_id = st.session_state.editing_id

if editing_id and editing_id in sample_by_id:
    pred = sample_by_id[editing_id]
    current_decision = cache.get(editing_id)
    cls_atual = current_decision["classification"] if current_decision else "—"
    st.info(f"✏️ **Modo correção** — decisão atual: **{cls_atual}**")
    if st.button("❌ Cancelar correção"):
        st.session_state.editing_id = None
        st.rerun()
else:
    pending = sorted(
        [p for p in sample if p["id"] not in completed],
        key=lambda p: p.get("alhedonic_score", 0.0),
        reverse=True,
    )
    if not pending:
        st.success("Revisão completa!")
        st.balloons()
        st.code(
            f"python -m qfeng.c1_digestion.hitl --action export --corpus {corpus}",
            language="bash",
        )
        st.stop()
    pred = pending[0]

# ── Card ───────────────────────────────────────────────────────────────────
signal: float = pred.get("alhedonic_score", 0.0)
n_reviewed = done + 1

if signal > 0.5:
    st.warning(f"Conflito normativo detectado — Sinal Alhedônico: {signal:.2f}")
else:
    st.info(f"Sinal Alhedônico: {signal:.2f}")

st.subheader(f"Predicado #{n_reviewed} / {total}")

col_rule, col_meta = st.columns([2, 1])

chunk_text = pred.get("chunk_text", "")
chunk_hierarchy = pred.get("chunk_hierarchy", [])
chunk_source_label = pred.get("chunk_source_label", "")

with col_rule:
    st.code(pred["rule"], language="prolog")
    if chunk_text:
        hierarchy_str = " > ".join(chunk_hierarchy) if chunk_hierarchy else "—"
        with st.expander(f"⚖️ Texto normativo original — {hierarchy_str}", expanded=True):
            if chunk_source_label:
                st.caption(f"📌 {chunk_source_label}")
            display = chunk_text[:1500] + ("..." if len(chunk_text) > 1500 else "")
            st.markdown("> " + display)
    else:
        st.caption("Texto original não disponível — regenere com --action sample")

with col_meta:
    st.subheader("Metadados")
    st.write("**Corpus:** " + str(pred.get("corpus", "?")))
    st.write("**Documento:** " + str(pred.get("source_doc", "?")))
    if chunk_hierarchy:
        st.write("**Hierarquia:** " + " > ".join(chunk_hierarchy))
    st.write("**Modalidade:** " + str(pred.get("modality", "?")))
    st.write("**Strength:** " + str(pred.get("strength", "?")))
    st.write("**atom_id:** `" + pred["id"][:12] + "…`")
    chunk_id_short = str(pred.get("chunk_id", "?"))[:12]
    st.write("**chunk_id:** `" + chunk_id_short + "…`")
    n_concurrent = len(pred.get("concurrent_chunks", []))
    st.write(f"**Concorrentes:** {n_concurrent}")

st.divider()

# ── Decisão ────────────────────────────────────────────────────────────────
_note_key = "note_" + pred["id"]
if editing_id == pred["id"] and _note_key not in st.session_state:
    _prev_dec = cache.get(pred["id"])
    if _prev_dec:
        st.session_state[_note_key] = _prev_dec.get("reviewer_note", "")
note = st.text_input("Nota do revisor (opcional)", key=_note_key, placeholder="Observação sobre este predicado específico...")
ts = datetime.now(timezone.utc).isoformat()

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("SOVEREIGN", use_container_width=True, type="primary"):
        cache.save(HITLDecision(pred["id"], "SOVEREIGN", signal, note, ts))
        st.session_state.editing_id = None
        st.rerun()

with c2:
    if st.button("ELASTIC", use_container_width=True):
        cache.save(HITLDecision(pred["id"], "ELASTIC", signal, note, ts))
        st.session_state.editing_id = None
        st.rerun()

with c3:
    if st.button("Pular (decidir depois)", use_container_width=True):
        cache.save(HITLDecision(pred["id"], "SKIP", signal, note, ts))
        st.session_state.editing_id = None
        st.rerun()
'''

APP.write_text(CONTENT, encoding="utf-8")
print(f"Written: {APP}")
