import pandas as pd
import os
import argparse
from datetime import datetime

from src.data.dataset import clean_data
from src.features.build_features import build_features

def run_pipeline(month_str):
    raw_file = f"data/raw/yellow_tripdata_2020-{month_str}.parquet"
    cleaned_file = f"data/processed/cleaned_2020-{month_str}.csv"
    features_file = f"data/processed/features_2020-{month_str}.csv"

    if not os.path.exists(raw_file):
        print(f"❌ Archivo no encontrado: {raw_file}")
        return

    print(f"📥 Cargando archivo: {raw_file}")
    df = pd.read_parquet(raw_file)
    df = df.head(100_000)  # Opcional: usar muestra para pruebas

    print("🧼 Limpiando datos...")
    df_clean = clean_data(df)
    df_clean.to_csv(cleaned_file, index=False)
    print(f"✅ Guardado: {cleaned_file}")

    print("🛠️ Generando features...")
    df_clean["tpep_pickup_datetime"] = pd.to_datetime(df_clean["tpep_pickup_datetime"])
    df_clean["tpep_dropoff_datetime"] = pd.to_datetime(df_clean["tpep_dropoff_datetime"])
    df_feat = build_features(df_clean)
    df_feat.to_csv(features_file, index=False)
    print(f"✅ Guardado: {features_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline de procesamiento mensual")
    parser.add_argument("--mes", type=str, required=True, help="Mes en formato 02, 03, 04, etc.")
    args = parser.parse_args()

    run_pipeline(args.mes)
