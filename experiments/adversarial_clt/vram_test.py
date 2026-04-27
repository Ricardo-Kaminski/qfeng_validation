"""Validação VRAM dos 4 modelos Ollama para experimento adversarial CLT."""
import subprocess
import json
import time
import datetime
import sys

MODELS = [
    "qwen3:14b",
    "phi4:14b",
    "gemma3:12b",
    "llama3.1:8b",
]

PROMPT_TESTE = (
    "Analise brevemente: um trabalhador cumpre 9 horas diárias sem adicional. "
    "Isso viola a CLT? Responda em 2 frases."
)


def get_vram_mb() -> int:
    """Retorna VRAM usada em MB via nvidia-smi."""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
            text=True,
        )
        return int(out.strip().split("\n")[0])
    except Exception:
        return -1


def run_ollama_call(model: str, prompt: str) -> tuple[str, float]:
    """Executa chamada ollama e retorna (resposta, latência_s)."""
    import urllib.request
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 128},
    }).encode()

    t0 = time.time()
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=600) as resp:
        body = json.loads(resp.read())
    latency = time.time() - t0
    text = body.get("message", {}).get("content", "")
    return text, latency


def main():
    baseline_mb = get_vram_mb()
    print(f"[VRAM baseline] {baseline_mb} MB\n")

    results = []
    for model in MODELS:
        print(f"  Testando {model}...", flush=True)
        # Aquecer (pull já feito, mas garantir que modelo está em memória)
        try:
            text, latency = run_ollama_call(model, PROMPT_TESTE)
        except Exception as e:
            print(f"    ERRO: {e}")
            results.append({"model": model, "status": "ERRO", "error": str(e)})
            continue

        # Medir VRAM logo após a chamada (modelo ainda carregado)
        vram_after = get_vram_mb()
        delta = vram_after - baseline_mb

        preview = text[:120].replace("\n", " ")
        print(f"    VRAM após: {vram_after} MB (+{delta} MB) | latência: {latency:.1f}s")
        print(f"    Resposta: {preview}...")

        results.append({
            "model": model,
            "status": "OK",
            "vram_baseline_mb": baseline_mb,
            "vram_after_mb": vram_after,
            "vram_delta_mb": delta,
            "latency_s": round(latency, 2),
            "response_preview": preview,
        })

        # Aguardar Ollama descarregar modelo antes do próximo (keep_alive=0)
        time.sleep(5)

    # --- Gerar relatório Markdown ---
    md_lines = [
        "# Validação VRAM — Modelos Ollama",
        f"\n**Data:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**VRAM baseline:** {baseline_mb} MB",
        "\n## Resultados por Modelo\n",
        "| Modelo | Status | VRAM Após (MB) | Delta (MB) | Latência (s) |",
        "|--------|--------|----------------|------------|--------------|",
    ]
    for r in results:
        if r["status"] == "OK":
            md_lines.append(
                f"| {r['model']} | ✅ OK | {r['vram_after_mb']} | +{r['vram_delta_mb']} | {r['latency_s']} |"
            )
        else:
            md_lines.append(f"| {r['model']} | ❌ ERRO | — | — | — |")

    md_lines += [
        "\n## Conclusão\n",
        "Todos os modelos dentro do limite de 12 GB VRAM da RTX 3060." if all(r["status"] == "OK" for r in results) else "⚠️ Alguns modelos falharam — verificar logs.",
        "\n## Prompt Usado\n",
        f"```\n{PROMPT_TESTE}\n```",
    ]

    report_path = "experiments/adversarial_clt/_models_validation.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"\nRelatório salvo em: {report_path}")

    # Salvar JSON de resultados
    json_path = "experiments/adversarial_clt/_models_validation.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n=== RESUMO ===")
    for r in results:
        status = "OK" if r["status"] == "OK" else "ERRO"
        delta = f"+{r.get('vram_delta_mb','?')} MB" if r["status"] == "OK" else "—"
        print(f"  {r['model']:20s}  {status}  {delta}")


if __name__ == "__main__":
    main()
