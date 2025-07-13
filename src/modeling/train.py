import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
import os

DATA_PATH = "data/processed/features_2020-01.csv"
MODEL_PATH = "models/random_forest_2020_01.joblib"

def load_data(path):
    return pd.read_csv(path)

def train_model(X_train, y_train):
    clf = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    clf.fit(X_train, y_train)
    return clf

def save_model(model, path):
    dump(model, path)
    print(f"✅ Modelo guardado en: {path}")

def main():
    print("📥 Cargando dataset con features...")
    df = load_data(DATA_PATH)

    print("🔍 Separando X e y...")
    X = df.drop(columns=["is_tip_generous"])
    y = df["is_tip_generous"]

    print("🧠 Entrenando modelo...")
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)

    print("💾 Guardando modelo...")
    save_model(model, MODEL_PATH)

if __name__ == "__main__":
    main()
