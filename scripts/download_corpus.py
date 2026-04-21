"""
Q-FENG Corpus Downloader
=========================
Downloads normative documents for all three regimes (Brasil, USA, EU)
into the corpora/ directory structure.

Usage:
    cd C:\\Workspace\\pessoal\\qfeng_validacao
    python scripts/download_corpus.py

Requirements:
    pip install requests beautifulsoup4 lxml
"""

import os
import sys
import time
import hashlib
import json
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# ── Configuration ──────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent / "corpora"
LOG_FILE = BASE_DIR / "download_log.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

DELAY_BETWEEN_REQUESTS = 2  # seconds — be polite


# ── Corpus definition ─────────────────────────────────────────────
# Each entry: (regime/tier/filename, url, format, description)

CORPUS = [
    # ================================================================
    # CASO A — BRASIL (SUS / Saúde Pública)
    # ================================================================

    # --- Constitucional ---
    (
        "brasil/constitucional/CF88_completa.htm",
        "https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm",
        "html",
        "CF/88 texto compilado — extrair Arts. 3, 5, 6, 196-200",
    ),

    # --- Legislação ordinária ---
    (
        "brasil/legislacao/lei_8080_1990.htm",
        "https://www.planalto.gov.br/ccivil_03/leis/l8080.htm",
        "html",
        "Lei Orgânica da Saúde — princípios e diretrizes do SUS",
    ),
    (
        "brasil/legislacao/lei_8142_1990.htm",
        "https://www.planalto.gov.br/ccivil_03/leis/l8142.htm",
        "html",
        "Participação da comunidade e transferências SUS",
    ),
    (
        "brasil/legislacao/lei_8689_1993.htm",
        "https://www.planalto.gov.br/ccivil_03/leis/L8689.htm",
        "html",
        "Extinção do INAMPS — contexto de municipalização",
    ),

    # --- Regulamentação ---
    (
        "brasil/regulamentacao/portaria_consolidacao_2_2017.htm",
        "https://bvsms.saude.gov.br/bvs/saudelegis/gm/2017/prc0002_03_10_2017.html",
        "html",
        "Portaria de Consolidação nº 2 — Políticas Nacionais de Saúde",
    ),
    (
        "brasil/regulamentacao/portaria_consolidacao_5_2017.htm",
        "https://bvsms.saude.gov.br/bvs/saudelegis/gm/2017/prc0005_03_10_2017.html",
        "html",
        "Portaria de Consolidação nº 5 — Ações e Serviços de Saúde",
    ),
    (
        "brasil/regulamentacao/portaria_1631_2015.htm",
        "https://bvsms.saude.gov.br/bvs/saudelegis/gm/2015/prt1631_01_10_2015.html",
        "html",
        "Critérios e Parâmetros Assistenciais para planejamento SUS",
    ),

    # --- Portarias COVID/Manaus (caso empírico) ---
    (
        "brasil/regulamentacao/portarias_manaus_2021/portaria_188_2020_ESPIN.htm",
        "https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt0188_04_02_2020.html",
        "html",
        "Portaria 188/2020 — Declara ESPIN, cria COE-nCoV",
    ),
    (
        "brasil/regulamentacao/portarias_manaus_2021/portaria_356_2020.htm",
        "https://planalto.gov.br/ccivil_03/Portaria/PRT/Portaria%20n%C2%BA%20356-20-MS.htm",
        "html",
        "Portaria 356/2020 — Regulamenta medidas de enfrentamento COVID",
    ),
    (
        "brasil/regulamentacao/portarias_manaus_2021/portaria_454_2020.htm",
        "http://www.planalto.gov.br/CCIVIL_03/Portaria/prt454-20-ms.htm",
        "html",
        "Portaria 454/2020 — Declara transmissão comunitária nacional",
    ),
    (
        "brasil/regulamentacao/portarias_manaus_2021/lei_13979_2020.htm",
        "https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l13979.htm",
        "html",
        "Lei 13.979/2020 — Medidas de enfrentamento de emergência de saúde",
    ),
    (
        "brasil/regulamentacao/portarias_manaus_2021/portaria_913_2022_fim_ESPIN.htm",
        "https://bvsms.saude.gov.br/bvs/saudelegis/gm/2022/prt0913_22_04_2022.html",
        "html",
        "Portaria 913/2022 — Encerra ESPIN, revoga Portaria 188",
    ),

    # ================================================================
    # CASO B — EUA (Medicaid / Obermeyer)
    # ================================================================

    # --- Constitutional ---
    (
        "usa/constitutional/14th_amendment.htm",
        "https://www.law.cornell.edu/constitution/amendmentxiv",
        "html",
        "14th Amendment — Equal Protection Clause (via Cornell LII)",
    ),

    # --- Statutory ---
    (
        "usa/statutory/ssa_title_xix_1901.htm",
        "https://www.law.cornell.edu/uscode/text/42/1396",
        "html",
        "42 USC §1396 — Medicaid appropriations (via Cornell LII)",
    ),
    (
        "usa/statutory/ssa_title_xix_1902.htm",
        "https://www.law.cornell.edu/uscode/text/42/1396a",
        "html",
        "42 USC §1396a — State plan requirements (core) (via Cornell LII)",
    ),
    (
        "usa/statutory/ssa_title_xix_1903.htm",
        "https://www.law.cornell.edu/uscode/text/42/1396b",
        "html",
        "42 USC §1396b — Payment to States (via Cornell LII)",
    ),
    (
        "usa/statutory/ssa_title_xix_1905.htm",
        "https://www.law.cornell.edu/uscode/text/42/1396d",
        "html",
        "42 USC §1396d — Definitions (medical assistance, etc.) (via Cornell LII)",
    ),
    (
        "usa/statutory/civil_rights_act_title_vi.htm",
        "https://www.justice.gov/crt/fcs/TitleVI",
        "html",
        "Civil Rights Act Title VI — Non-discrimination in federal programs",
    ),

    # --- Regulatory ---
    (
        "usa/regulatory/42_cfr_part_430.htm",
        "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-430",
        "html",
        "42 CFR Part 430 — General Medicaid provisions",
    ),
    (
        "usa/regulatory/42_cfr_part_435.htm",
        "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435",
        "html",
        "42 CFR Part 435 — Eligibility (core regulatory)",
    ),
    (
        "usa/regulatory/42_cfr_part_440.htm",
        "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-440",
        "html",
        "42 CFR Part 440 — Services: definitions and scope",
    ),

    # ================================================================
    # CASO C — UE (EU AI Act / Regulação de IA)
    # ================================================================

    # --- Treaties ---
    (
        "eu/treaties/carta_direitos_fundamentais_ue.htm",
        "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT",
        "html",
        "Charter of Fundamental Rights of the EU",
    ),

    # --- Regulation ---
    (
        "eu/regulation/eu_ai_act_2024_1689.htm",
        "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689",
        "html",
        "EU AI Act — Regulation (EU) 2024/1689 (full text)",
    ),
    (
        "eu/regulation/gdpr_full.htm",
        "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679",
        "html",
        "GDPR — Regulation (EU) 2016/679 (full text, extract Arts. 22, 35)",
    ),

    # --- Comparative ---
    (
        "eu/comparative/pl_2338_2023.htm",
        "https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=2583654&filename=PL%202338/2023",
        "html",
        "PL 2338/2023 — Marco Legal da IA brasileira",
    ),
]


# ── Download engine ────────────────────────────────────────────────

def load_log() -> dict:
    """Load download log to avoid re-downloading."""
    if LOG_FILE.exists():
        log = json.loads(LOG_FILE.read_text(encoding="utf-8"))
        # Remove failed entries so they get retried
        return {k: v for k, v in log.items() if v.get("status") != "failed"}
    return {}


def save_log(log: dict) -> None:
    LOG_FILE.write_text(
        json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def sha256_of(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def clean_html(raw_html: str) -> str:
    """Extract meaningful text-bearing HTML, remove scripts/styles."""
    soup = BeautifulSoup(raw_html, "lxml")
    for tag in soup.find_all(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return str(soup)


def download_one(rel_path: str, url: str, fmt: str, desc: str, log: dict) -> bool:
    """Download a single document. Returns True if downloaded, False if skipped."""
    target = BASE_DIR / rel_path

    # Skip if already downloaded and file exists
    if rel_path in log and target.exists():
        print(f"  [SKIP] {rel_path} (already downloaded)")
        return False

    print(f"  [GET]  {rel_path}")
    print(f"         {url}")

    try:
        resp = requests.get(url, headers=HEADERS, timeout=60, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  [FAIL] {rel_path}: {e}")
        log[rel_path] = {
            "status": "failed",
            "error": str(e),
            "url": url,
            "attempted_at": datetime.now().isoformat(),
        }
        return False

    # Ensure directory exists
    target.parent.mkdir(parents=True, exist_ok=True)

    # Process content
    raw = resp.content
    if fmt == "html":
        # Detect encoding
        encoding = resp.encoding or "utf-8"
        try:
            text = raw.decode(encoding)
        except (UnicodeDecodeError, LookupError):
            text = raw.decode("utf-8", errors="replace")
        cleaned = clean_html(text)
        target.write_text(cleaned, encoding="utf-8")
    else:
        # Binary (PDF, etc.)
        target.write_bytes(raw)

    # Log success
    content_for_hash = target.read_bytes()
    log[rel_path] = {
        "status": "ok",
        "url": url,
        "description": desc,
        "sha256": sha256_of(content_for_hash),
        "size_bytes": len(content_for_hash),
        "downloaded_at": datetime.now().isoformat(),
    }
    print(f"  [OK]   {len(content_for_hash):,} bytes")
    return True


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Q-FENG Corpus Normativo — Downloader")
    print(f"Target: {BASE_DIR}")
    print(f"Documents: {len(CORPUS)}")
    print("=" * 60)

    log = load_log()
    downloaded = 0
    skipped = 0
    failed = 0

    for rel_path, url, fmt, desc in CORPUS:
        result = download_one(rel_path, url, fmt, desc, log)
        if result:
            downloaded += 1
            time.sleep(DELAY_BETWEEN_REQUESTS)
        elif rel_path in log and log[rel_path].get("status") == "failed":
            failed += 1
        else:
            skipped += 1

    save_log(log)

    print()
    print("=" * 60)
    print(f"Done. Downloaded: {downloaded} | Skipped: {skipped} | Failed: {failed}")
    print(f"Log saved to: {LOG_FILE}")
    print("=" * 60)

    # Report any failures
    failures = [k for k, v in log.items() if v.get("status") == "failed"]
    if failures:
        print()
        print("⚠ FAILED downloads (require manual retrieval):")
        for f in failures:
            print(f"  - {f}: {log[f].get('error', 'unknown')}")
            print(f"    URL: {log[f].get('url', '?')}")


    # Report documents that need manual work
    print()
    print("📋 AÇÃO MANUAL NECESSÁRIA:")
    print("  1. PPA 2024-2027 (Programa Saúde):")
    print("     → Baixar de: https://www.gov.br/planejamento/")
    print("     → Salvar em: corpora/brasil/operacional/ppa_2024_2027_saude.pdf")
    print()
    print("  2. Plano Nacional de Saúde 2024-2027:")
    print("     → Baixar de: https://bvsms.saude.gov.br/")
    print("     → Salvar em: corpora/brasil/operacional/pns_2024_2027.pdf")
    print()
    print("  3. CMS Managed Care Final Rule 2024:")
    print("     → Baixar de: https://www.cms.gov/newsroom/fact-sheets/")
    print("     → Salvar em: corpora/usa/regulatory/cms_managed_care_2024.pdf")
    print()
    print("  4. Obermeyer et al. (2019):")
    print("     → Já referenciado no WP; artigo em Science, acesso institucional")
    print("     → Salvar em: corpora/usa/empirical/obermeyer_2019_science.pdf")


if __name__ == "__main__":
    main()
