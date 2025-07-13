import pandas as pd
from datetime import datetime

INPUT_PATH = "data/processed/cleaned_2020-01.csv"
OUTPUT_PATH = "data/processed/features_2020-01.csv"

def load_data(path):
    df = pd.read_csv(path)
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"]) 
    return df

def build_features(df):
    df = df.copy()

    # Extraer hora y día de la semana del pick-up
    df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
    df["pickup_weekday"] = df["tpep_pickup_datetime"].dt.weekday

    # Duración del viaje en minutos
    df["trip_duration"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60

    # Eliminar viajes con duración irreal
    df = df[df["trip_duration"] < 120]
    print(f"✅ Filas después del filtrado por duración < 120 min: {len(df)}") 

    # Mantener solo columnas necesarias
    features = [
        "trip_distance",
        "pickup_hour",
        "pickup_weekday",
        "passenger_count",
        "PULocationID",
        "DOLocationID",
        "trip_duration",
        "is_tip_generous"  # target
    ]
    df = df[features]

    return df

def save_features(df, path):
    df.to_csv(path, index=False)
    print(f"✅ Features guardadas en: {path}")

def main():
    print("Cargando dataset limpio...")
    df = load_data(INPUT_PATH)
    print(f"Filas cargadas: {len(df)}") 

    print("Generando variables predictoras...")
    df_feat = build_features(df)

    print("Guardando archivo con features...")
    save_features(df_feat, OUTPUT_PATH)

if __name__ == "__main__":
    main()
