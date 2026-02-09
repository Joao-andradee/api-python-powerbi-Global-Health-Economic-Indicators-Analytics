# ================= Libraries ==================
from __future__ import annotations

import os
import time
from typing import Dict, List

import pandas as pd
import requests

#=======================================================

# Base World Bank API endpoint
BASE_URL = "https://api.worldbank.org/v2/country/all/indicator/{indicator}"

# Common parameters for all API calls
PARAMS = {"format": "json", "per_page": 20000}

# Indicators we want to extract
INDICATORS = {
    "SP.DYN.LE00.IN": "life_expectancy",
    "SH.XPD.CHEX.PC.CD": "health_spend_pc",
    "NY.GDP.PCAP.CD": "gdp_pc",
}

# Folder where CSVs will be saved
OUT_DIR = os.path.join(os.getcwd(), "wb_exports")

#=======================================================

def fetch_indicator(indicator_code: str, value_name: str, retries: int = 3) -> pd.DataFrame:
    """
    Extract a single World Bank indicator and return a tidy DataFrame.
    """

    # Build API URL
    url = BASE_URL.format(indicator=indicator_code)

    last_err = None

    # Retry logic in case of temporary failures
    for attempt in range(1, retries + 1):
        try:
            # Call API
            r = requests.get(url, params=PARAMS, timeout=60)
            r.raise_for_status()

            # Convert response to JSON
            payload = r.json()

            # payload[1] contains the actual data
            rows = payload[1]
            out: List[Dict] = []

            # Loop through each observation
            for x in rows:
                if not x:
                    continue

                country = x.get("country") or {}
                indicator = x.get("indicator") or {}

                year = x.get("date")
                if year is None:
                    continue

                # Build clean row
                out.append(
                    {
                        "country_iso3": x.get("countryiso3code"),
                        "country_name": country.get("value"),
                        "year": int(year),
                        value_name: x.get("value"),
                        "indicator_code": indicator.get("id"),
                        "indicator_name": indicator.get("value"),
                    }
                )

            # Convert to DataFrame
            df = pd.DataFrame(out)

            # Basic cleaning
            df = df.dropna(subset=["country_iso3", "country_name", "year"])
            df[value_name] = pd.to_numeric(df[value_name], errors="coerce")

            return df

        except Exception as e:
            last_err = e
            time.sleep(1.5 * attempt)

    # If all retries fail
    raise RuntimeError(f"Failed to fetch {indicator_code}: {last_err}")

#=======================================================

def main() -> None:
    # Create export folder if it doesn't exist
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Export folder:", OUT_DIR)

    # Loop through each indicator
    for code, value_name in INDICATORS.items():
        print(f"Fetching {code} -> {value_name} ...")

        # Extract data from API
        df = fetch_indicator(code, value_name=value_name)

        # Optional: limit to modern data range
        df = df[(df["year"] >= 2000) & (df["year"] <= 2023)]

        # Save CSV file
        out_path = os.path.join(OUT_DIR, f"{value_name}.csv")
        df.to_csv(out_path, index=False)

        print(f"Saved: {out_path} ({len(df):,} rows)")

    print("\nAll indicators exported successfully.")

#=======================================================

if __name__ == "__main__":
    main()

