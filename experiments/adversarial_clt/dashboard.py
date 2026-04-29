"""Dashboard de monitoramento do experimento adversarial CLT.

Uso: C:/Users/ricar/miniconda3/envs/qfeng/python.exe dashboard.py [--port 7860]
"""
import json
import re
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from datetime import datetime
from collections import Counter

BASE     = Path(__file__).parent
MANIFEST = BASE / "results" / "manifest.json"
RUN_LOG  = BASE / "results" / "run_log.txt"
RAW_DIR  = BASE / "results" / "raw_responses"
PARQUET  = BASE / "results" / "results.parquet"

JOBS_PER_ARM = 600
TOTAL_JOBS   = 3000
ARMS         = ("B1", "B2", "B3", "B4", "B5")
MODELS       = ("qwen3:14b", "phi4:14b", "gemma3:12b", "llama3.1:8b")

# Cache para estatísticas do parquet (reconstruído quando o arquivo muda)
_parquet_cache: dict = {"mtime": 0.0, "data": None}
# Cache B5 específico (reconstruído quando n_b5 muda)
_b5_cache: dict = {"n": -1, "data": None}


def _read_manifest() -> dict:
    if not MANIFEST.exists():
        return {}
    try:
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _tail_log(n: int = 60) -> list[str]:
    if not RUN_LOG.exists():
        return []
    return RUN_LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-n:]


def _parquet_stats() -> dict:
    """Lê parquet e retorna estatísticas por braço (latência, contagem). Cache por mtime."""
    global _parquet_cache
    if not PARQUET.exists():
        return {}
    try:
        mtime = PARQUET.stat().st_mtime
        if mtime == _parquet_cache["mtime"] and _parquet_cache["data"] is not None:
            return _parquet_cache["data"]

        import pandas as pd
        df = pd.read_parquet(PARQUET)
        arm_col = "arm" if "arm" in df.columns else "braco"

        result: dict = {}
        for arm in ARMS:
            sub = df[df[arm_col] == arm]
            lat = sub["latency_ms"].dropna()
            result[arm] = {
                "n": len(sub),
                "median_lat_s": round(float(lat.median()) / 1000, 1) if len(lat) else None,
            }

        # B5 motor θ stats from parquet
        b5 = df[df[arm_col] == "B5"]
        if len(b5) and "qfeng_theta_deg" in b5.columns:
            theta = b5["qfeng_theta_deg"].dropna()
            overhead_cols = ["t_clingo_ms", "t_psi_build_ms", "t_theta_compute_ms"]
            overhead = b5[[c for c in overhead_cols if c in b5.columns]].fillna(0).sum(axis=1)
            lat_b5 = b5["latency_ms"].dropna()
            result["_b5_motor"] = {
                "n": len(b5),
                "median_theta": round(float(theta.median()), 2) if len(theta) else None,
                "median_overhead_ms": int(overhead.median()) if len(overhead) else None,
                "median_latency_ms": int(lat_b5.median()) if len(lat_b5) else None,
                "overhead_pct": (
                    round(float(overhead.median()) / float(lat_b5.median()) * 100, 2)
                    if len(overhead) and len(lat_b5) and float(lat_b5.median()) > 0
                    else None
                ),
                "regimes": (
                    b5["qfeng_regime"].value_counts().to_dict()
                    if "qfeng_regime" in b5.columns
                    else {}
                ),
            }

        _parquet_cache = {"mtime": mtime, "data": result}
        return result
    except Exception:
        return {}


def _build_b5_stats_fallback() -> dict | None:
    """Fallback: lê raw_responses para B5 quando parquet não tem dados B5."""
    global _b5_cache
    if not RAW_DIR.exists():
        return None

    manifest = _read_manifest()
    n_b5 = sum(1 for k, v in manifest.items() if k.startswith("B5__") and v == "completed")
    if n_b5 == 0:
        return None
    if n_b5 == _b5_cache["n"] and _b5_cache["data"] is not None:
        return _b5_cache["data"]

    b5_files = []
    try:
        for jf in RAW_DIR.iterdir():
            if jf.suffix != ".json":
                continue
            try:
                d = json.loads(jf.read_text(encoding="utf-8"))
                if d.get("braco") == "B5" and d.get("status") == "ok":
                    b5_files.append(d)
            except Exception:
                continue
    except Exception:
        return None

    if not b5_files:
        return None

    theta_vals = sorted(d["qfeng_theta_deg"] for d in b5_files if d.get("qfeng_theta_deg") is not None)
    overhead_vals = sorted(
        (d.get("t_clingo_ms") or 0) + (d.get("t_psi_build_ms") or 0) + (d.get("t_theta_compute_ms") or 0)
        for d in b5_files if d.get("latency_ms", 0) > 0
    )
    lat_vals = sorted(d["latency_ms"] for d in b5_files if d.get("latency_ms", 0) > 0)

    def med(lst):
        return lst[len(lst) // 2] if lst else None

    median_overhead = med(overhead_vals)
    median_latency = med(lat_vals)
    result = {
        "n": len(b5_files),
        "regimes": dict(Counter(d.get("qfeng_regime", "?") for d in b5_files)),
        "median_theta": round(med(theta_vals), 2) if med(theta_vals) is not None else None,
        "median_overhead_ms": median_overhead,
        "median_latency_ms": median_latency,
        "overhead_pct": (
            round(median_overhead / median_latency * 100, 2)
            if median_overhead and median_latency
            else None
        ),
    }
    _b5_cache = {"n": n_b5, "data": result}
    return result


def _build_stats(manifest: dict) -> dict:
    completed = sum(1 for v in manifest.values() if v == "completed")
    failed    = sum(1 for v in manifest.values() if v == "failed")
    pending   = TOTAL_JOBS - completed - failed

    arms = {b: {"completed": 0, "failed": 0} for b in ARMS}
    for key, status in manifest.items():
        arm = key.split("__")[0] if "__" in key else "?"
        if arm in arms and status in ("completed", "failed"):
            arms[arm][status] += 1

    models = {m: {"completed": 0, "failed": 0} for m in MODELS}
    for key, status in manifest.items():
        parts = key.split("__")
        model = parts[1] if len(parts) > 1 else "?"
        if model not in models:
            models[model] = {"completed": 0, "failed": 0}
        if status in ("completed", "failed"):
            models[model][status] += 1

    eta = lat = "—"
    try:
        for line in reversed(_tail_log(200)):
            m = re.search(r"lat_média=([\d.]+)s.*ETA=([\d.]+)h", line)
            if m:
                lat = f"{float(m.group(1)):.1f}s"
                eta_h = float(m.group(2))
                eta = f"{eta_h:.1f}h" if eta_h > 0 else "< 1h"
                break
    except Exception:
        pass

    return dict(
        total=TOTAL_JOBS, completed=completed, failed=failed, pending=pending,
        pct=round(completed / TOTAL_JOBS * 100, 2),
        arms=arms, models=models, eta=eta, lat=lat,
    )


def _progress_bar(pct: float, color: str = "#4ade80", height: int = 22) -> str:
    pct = min(max(pct, 0), 100)
    return (
        f'<div style="background:#1e293b;border-radius:8px;height:{height}px;width:100%;margin:4px 0">'
        f'<div style="background:{color};width:{pct}%;height:100%;border-radius:8px;'
        f'transition:width .4s;display:flex;align-items:center;padding-left:8px;'
        f'font-size:11px;color:#0f172a;font-weight:700">'
        f'{pct:.1f}%</div></div>'
    )


def _arm_color(arm: str) -> str:
    return {
        "B1": "#60a5fa", "B2": "#a78bfa", "B3": "#34d399",
        "B4": "#fbbf24", "B5": "#f472b6",
    }.get(arm, "#94a3b8")


def _regime_badge(regime: str, count: int) -> str:
    c = {"STAC": "#4ade80", "HITL": "#fbbf24", "BLOCK": "#f87171"}.get(regime, "#94a3b8")
    return (
        f'<span style="background:{c}22;color:{c};border:1px solid {c}55;'
        f'border-radius:4px;padding:2px 8px;font-size:.75rem;margin-right:4px;">'
        f'{regime}: {count}</span>'
    )


def _render_html() -> bytes:
    manifest = _read_manifest()
    st = _build_stats(manifest)
    pq = _parquet_stats()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # B5 stats — preferir parquet, fallback raw_responses
    b5 = pq.get("_b5_motor") or _build_b5_stats_fallback()

    # Log colorido
    colored_lines = []
    for ln in _tail_log(60):
        if "[ERROR]" in ln:
            colored_lines.append(f'<span style="color:#f87171">{ln}</span>')
        elif "[INFO]" in ln and ("Progresso" in ln or "completos" in ln or "concluído" in ln):
            colored_lines.append(f'<span style="color:#34d399">{ln}</span>')
        elif "HTTP Request" in ln:
            colored_lines.append(f'<span style="color:#94a3b8">{ln}</span>')
        else:
            colored_lines.append(f'<span style="color:#cbd5e1">{ln}</span>')
    log_html = "\n".join(colored_lines) or "<em>Log vazio</em>"

    # Tabela por braço
    arms_rows = ""
    for arm in ARMS:
        cnts = st["arms"].get(arm, {"completed": 0, "failed": 0})
        c, f = cnts["completed"], cnts["failed"]
        pct_arm = round(c / JOBS_PER_ARM * 100, 1)
        color = _arm_color(arm)
        bar = _progress_bar(pct_arm, color=color, height=14)
        lat_info = pq.get(arm, {}).get("median_lat_s")
        lat_cell = f'<span style="color:#94a3b8">{lat_info}s</span>' if lat_info else "—"
        b5_badge = (
            ' <span style="background:#f472b622;color:#f472b6;border:1px solid #f472b655;'
            'border-radius:3px;padding:1px 5px;font-size:.7rem">motor θ</span>'
            if arm == "B5" else ""
        )
        arms_rows += (
            f"<tr>"
            f"<td style='color:{color};font-weight:600'>{arm}{b5_badge}</td>"
            f"<td style='color:#4ade80'>{c}</td>"
            f"<td style='color:#f87171'>{f}</td>"
            f"<td>{lat_cell}</td>"
            f"<td style='width:120px'>{bar}</td>"
            f"</tr>"
        )

    # Tabela por modelo
    models_rows = ""
    for model, cnts in sorted(st["models"].items()):
        c, f = cnts["completed"], cnts["failed"]
        models_rows += (
            f"<tr><td>{model}</td>"
            f"<td style='color:#4ade80'>{c}</td>"
            f"<td style='color:#f87171'>{f}</td></tr>"
        )

    # Seção B5 motor θ
    if b5:
        regime_badges = "".join(
            _regime_badge(r, cnt) for r, cnt in sorted(b5.get("regimes", {}).items())
        )
        theta_str = f"{b5['median_theta']:.1f}°" if b5.get("median_theta") is not None else "—"
        overhead_str = f"{b5['median_overhead_ms']}ms" if b5.get("median_overhead_ms") is not None else "—"
        latency_str = (
            f"{round(b5['median_latency_ms']/1000, 1)}s"
            if b5.get("median_latency_ms") is not None else "—"
        )
        h7_color = "#4ade80" if (b5.get("overhead_pct") is not None and b5["overhead_pct"] < 5) else "#f87171"
        h7_str = (
            f"<span style='color:{h7_color};font-weight:700'>{b5['overhead_pct']:.2f}%</span>"
            if b5.get("overhead_pct") is not None else "—"
        )
        b5_section = f"""
  <div class="section" style="border-left:3px solid #f472b6">
    <h2>Motor θ — B5 <span style="color:#f472b6;font-size:.8rem">({b5.get('n', 0)}/{JOBS_PER_ARM} chamadas)</span></h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:12px">
      <div style="background:#0f172a;border-radius:8px;padding:12px">
        <div style="font-size:.7rem;color:#64748b;text-transform:uppercase">θ mediano</div>
        <div style="font-size:1.5rem;font-weight:700;color:#f472b6">{theta_str}</div>
      </div>
      <div style="background:#0f172a;border-radius:8px;padding:12px">
        <div style="font-size:.7rem;color:#64748b;text-transform:uppercase">Overhead Q-FENG</div>
        <div style="font-size:1.5rem;font-weight:700;color:#fbbf24">{overhead_str}</div>
      </div>
      <div style="background:#0f172a;border-radius:8px;padding:12px">
        <div style="font-size:.7rem;color:#64748b;text-transform:uppercase">Latência mediana</div>
        <div style="font-size:1.5rem;font-weight:700;color:#60a5fa">{latency_str}</div>
      </div>
      <div style="background:#0f172a;border-radius:8px;padding:12px">
        <div style="font-size:.7rem;color:#64748b;text-transform:uppercase">H7 overhead/latência</div>
        <div style="font-size:1.5rem;font-weight:700">{h7_str}</div>
      </div>
    </div>
    <div style="margin-top:8px">
      <span style="font-size:.75rem;color:#64748b;margin-right:8px">Regimes:</span>
      {regime_badges or '<span style="color:#475569">aguardando dados...</span>'}
    </div>
  </div>"""
    else:
        b5_section = """
  <div class="section" style="border-left:3px solid #f472b655">
    <h2>Motor θ — B5 <span style="color:#64748b;font-size:.8rem">(aguardando conclusão de B4)</span></h2>
    <div style="color:#475569;font-size:.85rem;padding:8px 0">
      B5 ainda não iniciado. Após B4 concluir (600/600), o runner processará B5 automaticamente.
      Esta seção exibirá θ mediano, distribuição de regimes (STAC/HITL/BLOCK) e overhead Q-FENG (H7).
    </div>
  </div>"""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Adversarial CLT — Monitor</title>
  <style>
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ background:#0f172a; color:#e2e8f0; font-family:'Segoe UI',monospace; padding:24px; }}
    h1 {{ font-size:1.4rem; color:#f8fafc; margin-bottom:4px; }}
    .sub {{ color:#64748b; font-size:.85rem; margin-bottom:24px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:16px; margin-bottom:24px; }}
    .card {{ background:#1e293b; border-radius:12px; padding:16px; }}
    .card .label {{ font-size:.75rem; color:#64748b; text-transform:uppercase; letter-spacing:.05em; }}
    .card .value {{ font-size:2rem; font-weight:700; margin-top:4px; }}
    .green {{ color:#4ade80; }} .red {{ color:#f87171; }} .yellow{{ color:#fbbf24; }}
    .blue  {{ color:#60a5fa; }} .pink  {{ color:#f472b6; }}
    .section {{ background:#1e293b; border-radius:12px; padding:16px; margin-bottom:16px; }}
    .section h2 {{ font-size:.95rem; color:#94a3b8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px; }}
    table {{ width:100%; border-collapse:collapse; font-size:.85rem; }}
    th, td {{ text-align:left; padding:6px 8px; border-bottom:1px solid #0f172a; }}
    th {{ color:#64748b; font-weight:600; }}
    .log {{ font-family:monospace; font-size:.78rem; background:#0f172a; border-radius:8px;
            padding:12px; height:420px; overflow-y:auto; white-space:pre-wrap; line-height:1.5; }}
    .badge {{ display:inline-block; background:#334155; border-radius:4px; padding:2px 8px;
              font-size:.75rem; color:#94a3b8; margin-left:8px; }}
    .refresh {{ color:#475569; font-size:.75rem; text-align:right; margin-top:8px; }}
    .arm-legend {{ display:flex; gap:12px; flex-wrap:wrap; margin-bottom:8px; font-size:.75rem; }}
    .arm-dot {{ display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:4px; }}
  </style>
</head>
<body>
  <h1>🔬 Adversarial CLT <span class="badge">Q-FENG / Paper 2</span> <span class="badge" style="background:#f472b622;color:#f472b6">B5 motor θ</span></h1>
  <div class="sub">5 braços × 4 modelos × 50 cenários × 3 runs = 3.000 jobs &nbsp;·&nbsp; Atualiza a cada 10s &nbsp;·&nbsp; {now}</div>

  <div class="grid">
    <div class="card"><div class="label">Total de Jobs</div><div class="value blue">{st['total']:,}</div></div>
    <div class="card"><div class="label">Completos</div><div class="value green">{st['completed']:,}</div></div>
    <div class="card"><div class="label">Falhas</div><div class="value red">{st['failed']:,}</div></div>
    <div class="card"><div class="label">Pendentes</div><div class="value yellow">{st['pending']:,}</div></div>
    <div class="card"><div class="label">Lat. média</div><div class="value blue">{st['lat']}</div></div>
    <div class="card"><div class="label">ETA restante</div><div class="value yellow">{st['eta']}</div></div>
  </div>

  <div class="section">
    <h2>Progresso geral — {st['completed']} de {st['total']} jobs</h2>
    {_progress_bar(st['pct'])}
    <div class="arm-legend" style="margin-top:10px">
      <span><span class="arm-dot" style="background:#60a5fa"></span>B1 LLM bruto</span>
      <span><span class="arm-dot" style="background:#a78bfa"></span>B2 RAG baseline</span>
      <span><span class="arm-dot" style="background:#34d399"></span>B3 ancoragem dPASP</span>
      <span><span class="arm-dot" style="background:#fbbf24"></span>B4 Q-FENG simbólico</span>
      <span><span class="arm-dot" style="background:#f472b6"></span>B5 motor θ completo</span>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px">
    <div class="section">
      <h2>Por braço (600 jobs cada)</h2>
      <table>
        <tr><th>Braço</th><th>OK</th><th>Erro</th><th>Lat. mediana</th><th>Progresso</th></tr>
        {arms_rows or '<tr><td colspan="5" style="color:#475569">Nenhum dado</td></tr>'}
      </table>
    </div>
    <div class="section">
      <h2>Por modelo</h2>
      <table>
        <tr><th>Modelo</th><th>OK</th><th>Erro</th></tr>
        {models_rows or '<tr><td colspan="3" style="color:#475569">Nenhum dado</td></tr>'}
      </table>
    </div>
  </div>

  {b5_section}

  <div class="section">
    <h2>Log recente (últimas 60 linhas)</h2>
    <div class="log" id="log">{log_html}</div>
  </div>

  <div class="refresh">Próximo refresh em <span id="countdown" style="color:#60a5fa;font-weight:700">10s</span></div>

  <script>
    const log = document.getElementById('log');
    if (log) log.scrollTop = log.scrollHeight;
    let secs = 10;
    const badge = document.getElementById('countdown');
    function tick() {{
      if (secs <= 0) {{ location.reload(); return; }}
      if (badge) badge.textContent = secs + 's';
      secs--;
      setTimeout(tick, 1000);
    }}
    tick();
  </script>
</body>
</html>"""
    return html.encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_response(404); self.end_headers(); return
        body = _render_html()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=7860)
    args = parser.parse_args()
    print(f"Dashboard rodando em http://localhost:{args.port}  (Ctrl+C para parar)")
    HTTPServer(("0.0.0.0", args.port), Handler).serve_forever()
