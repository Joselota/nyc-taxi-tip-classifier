import pandas as pd
import os

# CONFIG: puedes mover esto a config.py más adelante
RAW_DATA_PATH = "data/raw/yellow_tripdata_2020-01.parquet"
PROCESSED_DATA_PATH = "data/processed/cleaned_2020-01.csv"

def load_parquet(path):
    return pd.read_parquet(path)

def clean_data(df):
    df = df.copy()

    print(f"Filas antes de limpiar: {len(df)}")

    # 1. Eliminar nulos solo en columnas clave
    columnas_clave = ['trip_distance', 'fare_amount', 'tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = df.dropna(subset=columnas_clave)
    print(f"✅ Después de eliminar nulos en columnas clave: {len(df)}")

    # 2. Filtrar valores positivos
    df = df[(df['trip_distance'] > 0) & (df['fare_amount'] > 0)]
    print(f"✅ Después de filtrar distancia/fare > 0: {len(df)}")

    # 3. Crear variable objetivo: tip >= 20% del fare
    df["is_tip_generous"] = (df["tip_amount"] / df["fare_amount"]) >= 0.2
    df["is_tip_generous"] = df["is_tip_generous"].astype(int)

    return df

def save_cleaned_data(df, path):
    df.to_csv(path, index=False)
    print(f"✅ Archivo limpio guardado en: {path}")

def main():
    print("Cargando datos...")
    df = load_parquet(RAW_DATA_PATH)

    print(f"Dataset original: {len(df)} filas")

    df = df.head(100_000)
    print(f"🔍 Usando muestra de 100.000 filas")

    print("Limpiando datos...")
    df_clean = clean_data(df)

    print(f"✅ Filas después de limpiar: {len(df_clean)}")

    print("Guardando datos procesados...")
    save_cleaned_data(df_clean, PROCESSED_DATA_PATH)

if __name__ == "__main__":
    main()
