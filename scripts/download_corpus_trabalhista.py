"""
download_corpus_trabalhista.py
==============================
Download do corpus normativo trabalhista para o Q-FENG Paper 2.

Fontes: planalto.gov.br (CLT, Lei 13.467, CF/88) + tst.jus.br (Súmulas)
Saída:  corpora/brasil_trabalhista/{constitucional,legislacao,jurisprudencia}/

Uso:
    python scripts/download_corpus_trabalhista.py

Dependências:
    pip install requests beautifulsoup4 lxml
"""
from __future__ import annotations

import logging
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent / "corpora" / "brasil_trabalhista"

DOCUMENTOS = [
    # ── Constitucional ──────────────────────────────────────────────────
    {
        "destino": BASE_DIR / "constitucional" / "CF88_art7_xiii_xvi.htm",
        "url": "https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm",
        "descricao": "CF/88 Art. 7º — Direitos dos Trabalhadores",
        "seccao": "art_7",   # para extração futura de seção específica
    },
    # ── Legislação ───────────────────────────────────────────────────────
    {
        "destino": BASE_DIR / "legislacao" / "clt_completa.htm",
        "url": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm",
        "descricao": "CLT — Consolidação das Leis do Trabalho (completa)",
    },
    {
        "destino": BASE_DIR / "legislacao" / "lei_13467_2017_reforma_trabalhista.htm",
        "url": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm",
        "descricao": "Lei 13.467/2017 — Reforma Trabalhista",
    },
    # ── Jurisprudência TST ───────────────────────────────────────────────
    # Portal TST usa JavaScript — PDF canônico substitui scraping HTML
    # Contém: súmulas + OJs SDI-1 + SDI-2 + SDC (completo e oficial)
    {
        "destino": BASE_DIR / "jurisprudencia" / "livro_jurisprudencia_tst.pdf",
        "url": "https://www.tst.jus.br/documents/10157/63003/Livro-Internet.pdf",
        "descricao": "Livro de Jurisprudência TST — Súmulas + OJs SDI-1/SDI-2/SDC",
        "tipo": "pdf",
    },
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "pt-BR,pt;q=0.9",
}


def baixar(url: str, destino: Path, descricao: str, tipo: str = "html") -> bool:
    """Baixa uma URL e salva no destino. Suporta HTML e PDF."""
    if destino.exists():
        log.info(f"  Já existe: {destino.name} — pulando")
        return True

    destino.parent.mkdir(parents=True, exist_ok=True)

    log.info(f"Baixando: {descricao}")
    log.info(f"  URL: {url}")

    try:
        resp = requests.get(url, headers=HEADERS, timeout=120)
        resp.raise_for_status()

        if tipo == "pdf":
            destino.write_bytes(resp.content)
            tamanho_kb = destino.stat().st_size / 1024
            log.info(f"  Salvo: {destino.name} ({tamanho_kb:.1f} KB)")
            if destino.stat().st_size < 1_000_000:
                log.warning(f"  ALERTA: arquivo menor que 1 MB — verificar conteúdo")
                return False
        else:
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "lxml")
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            destino.write_text(str(soup), encoding="utf-8")
            tamanho_kb = destino.stat().st_size / 1024
            log.info(f"  Salvo: {destino.name} ({tamanho_kb:.1f} KB)")

        return True

    except requests.RequestException as e:
        log.error(f"  Erro ao baixar {url}: {e}")
        return False


def main() -> None:
    log.info("Iniciando download do corpus trabalhista Q-FENG Paper 2")
    log.info(f"Destino: {BASE_DIR}")

    sucesso = 0
    falha = 0

    for doc in DOCUMENTOS:
        ok = baixar(
            url=doc["url"],
            destino=doc["destino"],
            descricao=doc["descricao"],
            tipo=doc.get("tipo", "html"),
        )
        if ok:
            sucesso += 1
        else:
            falha += 1
        # Pausa entre requests para não sobrecarregar os servidores
        time.sleep(2)

    log.info(f"\nConcluído: {sucesso} OK, {falha} falhas")

    if falha > 0:
        log.warning("Alguns documentos falharam — verificar URLs acima.")

    # Verificar o que foi baixado
    log.info("\nArquivos disponíveis:")
    for subdir in ["constitucional", "legislacao", "jurisprudencia"]:
        pasta = BASE_DIR / subdir
        if pasta.exists():
            arquivos = [f for f in pasta.iterdir() if f.suffix in {".htm", ".html", ".pdf"}]
            log.info(f"  {subdir}/: {len(arquivos)} arquivo(s)")
            for f in sorted(arquivos):
                log.info(f"    {f.name} ({f.stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
