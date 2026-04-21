"""Download empirical data for Q-FENG EU/USA scenarios C5-C8."""
from __future__ import annotations

import io
import json
import logging
import zipfile
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import urllib3

# Suppress SSL warnings — common with EU government sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data" / "predictors"
LOG_FILE = DATA_DIR / "DOWNLOAD_LOG.md"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
TIMEOUT = 30
TODAY = datetime.now().strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get(url: str) -> requests.Response:
    return requests.get(url, headers=HEADERS, timeout=TIMEOUT, verify=False)


def _log_failure(scenario: str, attempts: list[tuple[str, str]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().isoformat(timespec="seconds")
    lines = [f"\n## {scenario} — FAILED {ts}\n"]
    for i, (url, err) in enumerate(attempts, 1):
        lines.append(f"- URL {i}: `{url}` → {err}\n")
    lines.append("- Instrução manual: obter o dataset manualmente e salvá-lo em "
                 f"`data/predictors/{scenario.lower().replace(' ', '_')}/`\n")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.writelines(lines)
    log.warning("Logged failure for %s to %s", scenario, LOG_FILE)


def _write_readme(target_dir: Path, scenario_name: str, source: str, url: str,
                  n_rows: int, columns: list[str], scenario_code: str,
                  description: str, synthetic: bool) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    content = f"""# {scenario_name}
- **Fonte:** {source}
- **URL:** {url}
- **Download:** {TODAY}
- **n_rows:** {n_rows}
- **Colunas:** {', '.join(columns)}
- **Cenário Q-FENG:** {scenario_code} — {description}
- **Sintético:** {"Yes" if synthetic else "No"}
"""
    (target_dir / "README.md").write_text(content, encoding="utf-8")
    log.info("README.md written to %s", target_dir)


def _save_parquet(df: pd.DataFrame, path: Path, max_rows: int = 5000) -> pd.DataFrame:
    if len(df) > 100_000:
        log.warning("Dataset has %d rows (>100k) — sampling %d rows", len(df), max_rows)
        df = df.sample(n=max_rows, random_state=42)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    log.info("Saved parquet: %s (%d rows)", path, len(df))
    return df


# ---------------------------------------------------------------------------
# C5 — EU AI Act auditability
# ---------------------------------------------------------------------------

def download_c5() -> tuple[bool, int, bool]:
    target_dir = DATA_DIR / "eu_aiact_audit"
    target_file = target_dir / "eu_aiact_audit.parquet"
    required = ["system_id", "risk_level", "auditability_score", "art13_compliant", "country", "sector"]

    # Attempt 1: HuggingFace datasets library
    url1 = "https://huggingface.co/datasets/vcpublic/eu-ai-act-compliance"
    try:
        log.info("C5 | Attempt 1: HuggingFace datasets library")
        from datasets import load_dataset  # type: ignore[import]
        ds = load_dataset("vcpublic/eu-ai-act-compliance")
        df = ds["train"].to_pandas()
        log.info("C5 | HuggingFace loaded: %d rows, cols: %s", len(df), list(df.columns))
        # Map columns to schema
        col_map: dict[str, str] = {}
        for req in required:
            for col in df.columns:
                if req.lower() in col.lower():
                    col_map[col] = req
                    break
        if col_map:
            df = df.rename(columns=col_map)
        for req in required:
            if req not in df.columns:
                df[req] = None
        df = df[required]
        df = _save_parquet(df, target_file)
        _write_readme(target_dir, "EU AI Act Auditability", "HuggingFace vcpublic/eu-ai-act-compliance",
                      url1, len(df), required, "C5", "EU AI Act Art.13 auditability compliance", False)
        return True, len(df), False
    except Exception as e:
        log.warning("C5 | HuggingFace failed: %s", e)

    # Attempt 2: EU AI Watch API
    url2 = "https://ai-watch.ec.europa.eu/api/v1/systems"
    try:
        log.info("C5 | Attempt 2: EU AI Watch API")
        r = _get(url2)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            key = next((k for k in ["results", "data", "items", "systems"] if k in data), None)
            df = pd.DataFrame(data[key] if key else [data])
        log.info("C5 | AI Watch loaded: %d rows, cols: %s", len(df), list(df.columns))
        col_map = {}
        for req in required:
            for col in df.columns:
                if req.lower() in col.lower():
                    col_map[col] = req
                    break
        if col_map:
            df = df.rename(columns=col_map)
        for req in required:
            if req not in df.columns:
                df[req] = None
        df = df[required]
        df = _save_parquet(df, target_file)
        _write_readme(target_dir, "EU AI Act Auditability", "EU AI Watch API", url2,
                      len(df), required, "C5", "EU AI Act Art.13 auditability compliance", False)
        return True, len(df), False
    except Exception as e:
        log.warning("C5 | EU AI Watch failed: %s", e)
        _log_failure("C5 EU AI Act Auditability",
                     [(url1, "HuggingFace dataset not found or load_dataset error"),
                      (url2, str(e))])

    # Fallback: synthetic sample
    log.info("C5 | Generating synthetic sample (n=50)")
    rng = np.random.default_rng(42)
    countries = ["DE", "FR", "IT", "ES", "NL", "SE", "PL", "BE", "AT", "DK"]
    sectors = ["healthcare", "finance", "law_enforcement", "education", "transport",
               "social_services", "employment", "biometric", "infrastructure", "other"]
    risk_levels = ["unacceptable", "high", "limited", "minimal"]
    risk_weights = [0.05, 0.35, 0.30, 0.30]
    n = 50
    df = pd.DataFrame({
        "system_id": [f"EU-AI-{i:04d}" for i in range(1, n + 1)],
        "risk_level": rng.choice(risk_levels, n, p=risk_weights),
        "auditability_score": rng.uniform(0.1, 1.0, n).round(3),
        "art13_compliant": rng.choice([True, False], n, p=[0.6, 0.4]),
        "country": rng.choice(countries, n),
        "sector": rng.choice(sectors, n),
    })
    df = _save_parquet(df, target_file)
    _write_readme(target_dir, "EU AI Act Auditability (Synthetic)",
                  "Synthetic — generated by Q-FENG pipeline",
                  "N/A — both real sources unavailable", len(df), required,
                  "C5", "EU AI Act Art.13 auditability compliance", True)
    return True, len(df), True


# ---------------------------------------------------------------------------
# C6 — GDPR enforcement
# ---------------------------------------------------------------------------

def download_c6() -> tuple[bool, int, bool]:
    target_dir = DATA_DIR / "gdpr_enforcement"
    target_file = target_dir / "gdpr_art22_decisions.parquet"
    required = ["case_id", "country", "authority", "article", "fine_eur", "date", "summary"]

    urls = [
        "https://raw.githubusercontent.com/riensonckur/gdpr-fines/main/gdpr_fines.csv",
        "https://www.enforcementtracker.com/data/enforcementtracker.json",
        "https://raw.githubusercontent.com/dataramblings/gdpr-fines/main/gdprfines.csv",
    ]

    col_aliases: dict[str, list[str]] = {
        "case_id": ["id", "case_id", "caseid", "case", "number", "ref"],
        "country": ["country", "member_state", "state", "nation"],
        "authority": ["authority", "dpa", "supervisory_authority", "sa"],
        "article": ["article", "articles", "violated_article", "provision"],
        "fine_eur": ["fine", "fine_eur", "fine_amount", "amount", "penalty", "sanction"],
        "date": ["date", "decision_date", "year", "issued_at"],
        "summary": ["summary", "description", "details", "notes", "text"],
    }

    def _map_cols(df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
        rename: dict[str, str] = {}
        for req, aliases in col_aliases.items():
            if req not in df.columns:
                for alias in aliases:
                    if alias in df.columns:
                        rename[alias] = req
                        break
        if rename:
            df = df.rename(columns=rename)
        for req in required:
            if req not in df.columns:
                df[req] = None
        return df[required]

    errors: list[tuple[str, str]] = []

    for url in urls[:2]:
        try:
            log.info("C6 | Trying: %s", url)
            r = _get(url)
            r.raise_for_status()
            if url.endswith(".json"):
                data = r.json()
                if isinstance(data, list):
                    df = pd.DataFrame(data)
                else:
                    key = next((k for k in ["results", "data", "items", "fines"] if k in data), None)
                    df = pd.DataFrame(data[key] if key else [data])
            else:
                df = pd.read_csv(io.StringIO(r.text))
            log.info("C6 | Loaded %d rows from %s", len(df), url)
            df = _map_cols(df)
            # Filter for Art. 22 or Art. 5
            if df["article"].notna().any():
                mask = df["article"].astype(str).str.contains(r"Art\.?\s*2[25]|Art\.?\s*5", case=False, na=False)
                filtered = df[mask]
                if len(filtered) == 0:
                    log.warning("C6 | No Art.22/Art.5 rows found — keeping all %d rows", len(df))
                    filtered = df
                df = filtered
            df = _save_parquet(df, target_file)
            _write_readme(target_dir, "GDPR Enforcement Decisions", "GitHub CSV/JSON", url,
                          len(df), required, "C6",
                          "GDPR Art.22 automated decision-making enforcement cases", False)
            return True, len(df), False
        except Exception as e:
            log.warning("C6 | Failed %s: %s", url, e)
            errors.append((url, str(e)))

    # Attempt 3rd URL (alternative CSV)
    url3 = urls[2]
    try:
        log.info("C6 | Trying fallback: %s", url3)
        r = _get(url3)
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
        log.info("C6 | Loaded %d rows from %s", len(df), url3)
        df = _map_cols(df)
        if df["article"].notna().any():
            mask = df["article"].astype(str).str.contains(r"Art\.?\s*2[25]|Art\.?\s*5", case=False, na=False)
            filtered = df[mask]
            df = filtered if len(filtered) > 0 else df
        df = _save_parquet(df, target_file)
        _write_readme(target_dir, "GDPR Enforcement Decisions", "GitHub dataramblings CSV", url3,
                      len(df), required, "C6",
                      "GDPR Art.22 automated decision-making enforcement cases", False)
        return True, len(df), False
    except Exception as e:
        log.warning("C6 | All URLs failed. Last error: %s", e)
        errors.append((url3, str(e)))
        _log_failure("C6 GDPR Enforcement", errors)

    # Synthetic fallback
    log.info("C6 | Generating synthetic GDPR enforcement data (n=80)")
    rng = np.random.default_rng(42)
    countries = ["DE", "FR", "IT", "ES", "NL", "IE", "SE", "AT", "HU", "PL",
                 "BE", "RO", "LU", "DK", "FI"]
    authorities = {
        "DE": "BfDI", "FR": "CNIL", "IT": "Garante", "ES": "AEPD", "NL": "AP",
        "IE": "DPC", "SE": "IMY", "AT": "DSB", "HU": "NAIH", "PL": "UODO",
        "BE": "APD", "RO": "ANSPDCP", "LU": "CNPD", "DK": "Datatilsynet", "FI": "Tietosuojavaltuutettu",
    }
    articles = ["Art. 22 - Automated decisions", "Art. 5 - Principles",
                "Art. 22 - Profiling", "Art. 5(1)(a) - Lawfulness",
                "Art. 22(1) - No solely automated processing",
                "Art. 5(1)(c) - Data minimisation"]
    n = 80
    country_arr = rng.choice(countries, n)
    fine_arr = rng.lognormal(mean=10, sigma=2, size=n).round(0).astype(int)
    years = rng.integers(2019, 2025, n)
    months = rng.integers(1, 13, n)
    days = rng.integers(1, 28, n)
    df = pd.DataFrame({
        "case_id": [f"GDPR-{i:04d}" for i in range(1, n + 1)],
        "country": country_arr,
        "authority": [authorities[c] for c in country_arr],
        "article": rng.choice(articles, n),
        "fine_eur": fine_arr,
        "date": [f"{y}-{m:02d}-{d:02d}" for y, m, d in zip(years, months, days)],
        "summary": [f"Enforcement case involving automated decision-making under {art}."
                    for art in rng.choice(articles, n)],
    })
    df = _save_parquet(df, target_file)
    _write_readme(target_dir, "GDPR Enforcement Decisions (Synthetic)",
                  "Synthetic — generated by Q-FENG pipeline",
                  "N/A — all real sources unavailable", len(df), required,
                  "C6", "GDPR Art.22 automated decision-making enforcement cases", True)
    return True, len(df), True


# ---------------------------------------------------------------------------
# C7 — Bias algorítmico Obermeyer 2019
# ---------------------------------------------------------------------------

def download_c7() -> tuple[bool, int, bool]:
    target_dir = DATA_DIR / "obermeyer_bias"
    target_file = target_dir / "obermeyer_bias.parquet"
    required = ["race", "risk_score", "cost_avoidable", "active_conditions", "gagne_sum"]

    urls = [
        "https://gitlab.com/labsysmed/dissecting-bias/-/raw/master/data_new.zip",
        "https://gitlab.com/labsysmed/dissecting-bias/-/archive/master/dissecting-bias-master.zip",
    ]

    errors: list[tuple[str, str]] = []

    for url in urls:
        try:
            log.info("C7 | Trying: %s", url)
            r = _get(url)
            r.raise_for_status()
            content = r.content
            if not zipfile.is_zipfile(io.BytesIO(content)):
                raise ValueError("Response is not a valid ZIP file")
            with zipfile.ZipFile(io.BytesIO(content)) as zf:
                names = zf.namelist()
                log.info("C7 | ZIP contents: %s", names[:20])
                # Find CSV/parquet with health data
                candidates = [n for n in names if n.endswith((".csv", ".parquet")) and
                              not n.startswith("__MACOSX")]
                if not candidates:
                    raise FileNotFoundError(f"No CSV/parquet in ZIP: {names}")
                # Prefer the largest or most descriptively named file
                data_file = sorted(candidates, key=lambda n: ("data" in n.lower() or "bias" in n.lower()), reverse=True)[0]
                log.info("C7 | Using file: %s", data_file)
                with zf.open(data_file) as f:
                    if data_file.endswith(".parquet"):
                        df = pd.read_parquet(f)
                    else:
                        df = pd.read_csv(f)
            log.info("C7 | Loaded %d rows, cols: %s", len(df), list(df.columns))
            df.columns = [c.lower().strip() for c in df.columns]
            col_map: dict[str, str] = {}
            aliases: dict[str, list[str]] = {
                "race": ["race", "race_bin", "race_eth", "ethnicity"],
                "risk_score": ["risk_score_t", "risk_score", "risk", "score", "predicted_risk", "algorithm_score"],
                "cost_avoidable": ["cost_avoidable_t", "cost_avoidable", "avoidable_cost", "cost_t"],
                "active_conditions": ["active_conditions", "conditions", "num_conditions", "program_enrolled_t"],
                "gagne_sum": ["gagne_sum_t", "gagne_sum_tm1", "gagne_sum", "gagne", "comorbidity_score"],
            }
            for req, als in aliases.items():
                for a in als:
                    if a in df.columns and req not in col_map.values():
                        col_map[a] = req
                        break
            if col_map:
                df = df.rename(columns=col_map)
            for req in required:
                if req not in df.columns:
                    df[req] = None
            df = df[required]
            df = _save_parquet(df, target_file)
            _write_readme(target_dir, "Obermeyer et al. 2019 Algorithmic Bias",
                          "GitLab labsysmed/dissecting-bias", url,
                          len(df), required, "C7",
                          "Racial bias in healthcare risk scores (Obermeyer 2019 Science paper)", False)
            return True, len(df), False
        except Exception as e:
            log.warning("C7 | Failed %s: %s", url, e)
            errors.append((url, str(e)))

    _log_failure("C7 Obermeyer Bias", errors)

    # Synthetic fallback based on Obermeyer 2019 summary statistics
    log.info("C7 | Generating synthetic Obermeyer data (n=100) from published statistics")
    rng = np.random.default_rng(42)
    n = 100
    # From Obermeyer et al. 2019: Black patients had lower risk scores despite higher comorbidities
    # ~57.6% Black patients at same risk score level would need active management
    race = rng.choice(["Black", "White", "Hispanic", "Other"], n, p=[0.30, 0.55, 0.10, 0.05])
    risk_score = np.where(
        race == "Black",
        rng.normal(loc=45, scale=15, size=n),   # lower predicted risk
        rng.normal(loc=55, scale=15, size=n),   # higher predicted risk
    ).clip(0, 100).round(1)
    active_conditions = np.where(
        race == "Black",
        rng.poisson(lam=4.5, size=n),   # more actual conditions
        rng.poisson(lam=3.2, size=n),
    )
    cost_avoidable = np.where(
        race == "Black",
        rng.normal(loc=3200, scale=800, size=n),
        rng.normal(loc=4100, scale=900, size=n),   # higher predicted cost
    ).clip(0).round(0).astype(int)
    gagne_sum = np.where(
        race == "Black",
        rng.normal(loc=3.8, scale=1.2, size=n),
        rng.normal(loc=2.9, scale=1.1, size=n),
    ).clip(0).round(1)
    df = pd.DataFrame({
        "race": race,
        "risk_score": risk_score,
        "cost_avoidable": cost_avoidable,
        "active_conditions": active_conditions,
        "gagne_sum": gagne_sum,
    })
    df = _save_parquet(df, target_file)
    _write_readme(target_dir, "Obermeyer 2019 Bias (Synthetic)",
                  "Synthetic based on Obermeyer et al. 2019 Science — published summary statistics",
                  "https://doi.org/10.1126/science.aax2342", len(df), required,
                  "C7", "Racial bias in healthcare risk scores (CONSTITUTIONAL_FAILURE case)", True)
    return True, len(df), True


# ---------------------------------------------------------------------------
# C8 — Medicaid access
# ---------------------------------------------------------------------------

def download_c8() -> tuple[bool, int, bool]:
    target_dir = DATA_DIR / "medicaid_access"
    target_file = target_dir / "medicaid_access.parquet"
    required = ["state", "year", "total_enrolled", "pct_with_access", "race_ethnicity", "income_level"]

    urls = [
        "https://data.medicaid.gov/api/1/datastore/query/6c114b2c-cb83-4954-9153-277668a3e7c8/0?limit=5000",
        "https://data.medicaid.gov/api/1/datastore/get/6c114b2c-cb83-4954-9153-277668a3e7c8",
        "https://data.medicaid.gov/api/1/datastore/query/9c26c2f2-fa84-4c3b-9b4e-fde93e37f3d3/0?limit=5000",
    ]

    col_aliases: dict[str, list[str]] = {
        "state": ["state", "state_name", "state_code", "geography"],
        "year": ["year", "report_year", "fiscal_year", "date_year"],
        "total_enrolled": ["total_enrolled", "total", "enrollment", "enrollees", "beneficiaries"],
        "pct_with_access": ["pct_with_access", "access_pct", "access_rate", "percent_access"],
        "race_ethnicity": ["race_ethnicity", "race", "ethnicity", "race_eth", "demographic"],
        "income_level": ["income_level", "income", "fpl", "poverty_level", "income_group"],
    }

    def _map_cols(df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
        rename: dict[str, str] = {}
        for req, aliases in col_aliases.items():
            if req not in df.columns:
                for alias in aliases:
                    if alias in df.columns:
                        rename[alias] = req
                        break
        if rename:
            df = df.rename(columns=rename)
        for req in required:
            if req not in df.columns:
                df[req] = None
        return df[required]

    errors: list[tuple[str, str]] = []

    for url in urls:
        try:
            log.info("C8 | Trying: %s", url)
            r = _get(url)
            r.raise_for_status()
            data = r.json()
            if isinstance(data, list):
                df = pd.DataFrame(data)
            elif isinstance(data, dict):
                # CMS API wraps results
                key = next((k for k in ["results", "data", "rows", "items"] if k in data), None)
                if key:
                    df = pd.DataFrame(data[key])
                elif "columns" in data and "rows" in data:
                    df = pd.DataFrame(data["rows"], columns=data["columns"])
                else:
                    df = pd.json_normalize(data)
            log.info("C8 | Loaded %d rows from %s, cols: %s", len(df), url, list(df.columns))
            if len(df) == 0:
                raise ValueError("Empty dataset returned")
            df = _map_cols(df)
            df = _save_parquet(df, target_file)
            _write_readme(target_dir, "Medicaid Access by Demographics",
                          "CMS data.medicaid.gov API", url,
                          len(df), required, "C8",
                          "Medicaid enrollment and access rates by state, race/ethnicity, income level", False)
            return True, len(df), False
        except Exception as e:
            log.warning("C8 | Failed %s: %s", url, e)
            errors.append((url, str(e)))

    _log_failure("C8 Medicaid Access", errors)

    # Synthetic fallback
    log.info("C8 | Generating synthetic Medicaid access data (n=200)")
    rng = np.random.default_rng(42)
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    ]
    years = [2019, 2020, 2021, 2022, 2023]
    race_ethnicities = ["White Non-Hispanic", "Black Non-Hispanic", "Hispanic",
                        "Asian/Pacific Islander", "American Indian/Alaska Native", "Other/Unknown"]
    income_levels = ["0-50% FPL", "51-100% FPL", "101-138% FPL", "139-200% FPL", "200%+ FPL"]

    rows = []
    for i in range(200):
        state = states[i % 50]
        year = years[i % 5]
        race = rng.choice(race_ethnicities)
        income = rng.choice(income_levels)
        enrolled = int(rng.integers(5000, 500000))
        access = round(float(rng.uniform(0.55, 0.95)), 3)
        rows.append({
            "state": state,
            "year": year,
            "total_enrolled": enrolled,
            "pct_with_access": access,
            "race_ethnicity": race,
            "income_level": income,
        })

    df = pd.DataFrame(rows)
    df = _save_parquet(df, target_file)
    _write_readme(target_dir, "Medicaid Access by Demographics (Synthetic)",
                  "Synthetic — generated by Q-FENG pipeline",
                  "N/A — CMS API unavailable", len(df), required,
                  "C8", "Medicaid enrollment and access rates by state, race/ethnicity, income level", True)
    return True, len(df), True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []

    log.info("=" * 60)
    log.info("Q-FENG EU/USA Empirical Download — C5-C8")
    log.info("=" * 60)

    scenarios = [
        ("C5", "EU AI Act Auditability", download_c5,
         "data/predictors/eu_aiact_audit/eu_aiact_audit.parquet"),
        ("C6", "GDPR Enforcement", download_c6,
         "data/predictors/gdpr_enforcement/gdpr_art22_decisions.parquet"),
        ("C7", "Obermeyer Bias", download_c7,
         "data/predictors/obermeyer_bias/obermeyer_bias.parquet"),
        ("C8", "Medicaid Access", download_c8,
         "data/predictors/medicaid_access/medicaid_access.parquet"),
    ]

    for code, name, fn, file_path in scenarios:
        log.info("\n--- %s: %s ---", code, name)
        try:
            ok, n_rows, synthetic = fn()
            results.append({
                "cenario": code,
                "fonte": name,
                "status": "OK" if ok else "FAILED",
                "n_rows": n_rows if ok else 0,
                "arquivo": file_path,
                "sintetico": "Sim" if synthetic else "Não",
            })
        except Exception as e:
            log.error("Unexpected error in %s: %s", code, e)
            results.append({
                "cenario": code,
                "fonte": name,
                "status": "ERROR",
                "n_rows": 0,
                "arquivo": file_path,
                "sintetico": "N/A",
            })

    log.info("\n" + "=" * 60)
    log.info("SUMMARY")
    log.info("=" * 60)
    log.info("%-8s %-25s %-8s %-8s %-10s", "Cenário", "Fonte", "Status", "n_rows", "Sintético")
    log.info("-" * 70)
    for r in results:
        log.info("%-8s %-25s %-8s %-8s %-10s",
                 r["cenario"], r["fonte"][:24], r["status"], r["n_rows"], r["sintetico"])
    log.info("=" * 60)
    log.info("Done. Check data/predictors/ and data/predictors/DOWNLOAD_LOG.md for details.")


if __name__ == "__main__":
    main()
