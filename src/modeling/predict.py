import pandas as pd
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
from joblib import load

MODEL_PATH = "models/random_forest_2020_01.joblib"
DATA_PATH = "data/processed/features_2020-01.csv"  # puedes cambiar esto para evaluar otros meses

def load_data(path):
    return pd.read_csv(path)

def load_model(path):
    return load(path)

def evaluate(model, X, y):
    y_pred = model.predict(X)
    f1 = f1_score(y, y_pred)
    acc = accuracy_score(y, y_pred)
    cm = confusion_matrix(y, y_pred)

    print("🎯 Evaluación del modelo")
    print(f"F1-score: {f1:.4f}")
    print(f"Accuracy: {acc:.4f}")
    print("Confusion matrix:")
    print(cm)

def main():
    print("📦 Cargando modelo...")
    model = load_model(MODEL_PATH)

    print("📥 Cargando datos de evaluación...")
    df = load_data(DATA_PATH)

    X = df.drop(columns=["is_tip_generous"])
    y = df["is_tip_generous"]

    print("🔍 Evaluando...")
    evaluate(model, X, y)

if __name__ == "__main__":
    main()
