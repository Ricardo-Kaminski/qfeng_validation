"""Probe API DEMAS-VEPI — verifica viabilidade de extração para Manaus.

Estima:
  1. Total de registros disponíveis (paginação sequencial)
  2. Proporção de registros de Manaus (AM)
  3. Campos preenchidos para UTI (ocupacaoconfirmadouti, ocupacaohospitalaruti)
  4. Intervalo de datas

Se Manaus < 0.5% do total → fallback: interpolar TOH mensal FVS-AM para semanal.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import sys

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

API_URL = "https://apidadosabertos.saude.gov.br/assistencia-a-saude/registro-de-ocupacao-hospitalar-covid-19"
PAGE_SIZE = 1000
SAMPLE_PAGES = 10  # sondar 10 páginas = 10.000 registros

ROOT = Path(__file__).parents[1]


def fetch_page(offset: int, limit: int = PAGE_SIZE) -> list[dict]:
    resp = requests.get(
        API_URL,
        params={"limit": limit, "offset": offset},
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    key = list(data.keys())[0]
    return data[key]


def main() -> None:
    print(f"Sondando API DEMAS-VEPI ({SAMPLE_PAGES} páginas × {PAGE_SIZE} registros)...")

    total_records = 0
    manaus_records = 0
    uti_fields_filled = 0
    dates_seen: set[str] = set()
    estados_count: dict[str, int] = {}

    for page in range(SAMPLE_PAGES):
        offset = page * PAGE_SIZE
        try:
            records = fetch_page(offset)
        except Exception as e:
            print(f"  Página {page} falhou: {e}")
            break

        if not records:
            print(f"  Página {page}: vazia — fim dos dados (total estimado: {total_records})")
            break

        total_records += len(records)

        for r in records:
            mun = (r.get("municipionotificacao") or r.get("municipio") or "").lower()
            estado = r.get("estadonotificacao") or r.get("estado") or "?"
            estados_count[estado] = estados_count.get(estado, 0) + 1

            if "manaus" in mun:
                manaus_records += 1
                occ_uti = r.get("ocupacaohospitalaruti")
                covid_uti = r.get("ocupacaoconfirmadouti")
                if occ_uti is not None and covid_uti is not None:
                    uti_fields_filled += 1

            dt = r.get("datanotificacao", "")[:10]
            if dt:
                dates_seen.add(dt)

        print(f"  Página {page:2d}: {len(records)} registros | "
              f"Manaus acum: {manaus_records} ({manaus_records/total_records*100:.1f}%)",
              flush=True)

        # Pequena pausa para não sobrecarregar a API
        time.sleep(0.5)

    print(f"\n=== RESULTADO ===")
    print(f"Registros amostrados: {total_records:,}")
    print(f"Registros Manaus: {manaus_records} ({manaus_records/max(total_records,1)*100:.2f}%)")
    print(f"UTI fields preenchidos (Manaus): {uti_fields_filled}")
    if dates_seen:
        print(f"Datas: {min(dates_seen)} → {max(dates_seen)}")
    print(f"\nTop 10 estados:")
    for estado, cnt in sorted(estados_count.items(), key=lambda x: -x[1])[:10]:
        print(f"  {estado}: {cnt}")

    viavel = manaus_records > 50

    if viavel:
        print("\n✅ API viável — Manaus tem registros suficientes para extração completa.")
        print("   Próximo passo: executar download_api_demas_vepi.py com paginação completa.")
    else:
        print("\n⚠️ API DEMAS-VEPI: Manaus tem poucos registros na amostra.")
        print("   Fallback recomendado: interpolar TOH mensal FVS-AM → semanal.")
        print("   O TOH mensal (toh_uti_manaus.parquet) cobre a janela completa.")

    out = {
        "total_amostrado": total_records,
        "manaus_records": manaus_records,
        "manaus_pct": round(manaus_records / max(total_records, 1) * 100, 3),
        "uti_fields_filled": uti_fields_filled,
        "viavel": viavel,
        "dates_range": [min(dates_seen), max(dates_seen)] if dates_seen else [],
        "top_estados": dict(sorted(estados_count.items(), key=lambda x: -x[1])[:10]),
    }
    out_path = ROOT / "outputs/api_demas_vepi_probe.json"
    import json as _json
    with open(out_path, "w", encoding="utf-8") as f:
        _json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Resultado salvo: {out_path}")


if __name__ == "__main__":
    main()
