import pandas as pd
from joblib import load
from sklearn.metrics import f1_score

MODEL_PATH = "models/random_forest_2020_01.joblib"
MONTHS = ["02", "03", "04"]  # Puedes extender esta lista
BASE_PATH = "data/processed/"

def load_model(path):
    return load(path)

def evaluate_for_month(model, month):
    file_path = f"{BASE_PATH}features_2020-{month}.csv"
    try:
        df = pd.read_csv(file_path)
        X = df.drop(columns=["is_tip_generous"])
        y = df["is_tip_generous"]
        y_pred = model.predict(X)
        f1 = f1_score(y, y_pred)
        return {"mes": f"2020-{month}", "f1_score": f1, "n": len(df)}
    except FileNotFoundError:
        print(f"⚠️ Archivo no encontrado: {file_path}")
        return {"mes": f"2020-{month}", "f1_score": None, "n": 0}

def main():
    print("📦 Cargando modelo entrenado en enero...")
    model = load_model(MODEL_PATH)

    resultados = []
    for mes in MONTHS:
        print(f"📊 Evaluando mes: 2020-{mes}")
        resultado = evaluate_for_month(model, mes)
        resultados.append(resultado)

    df_resultados = pd.DataFrame(resultados)
    print("\n🧾 Resultados por mes:")
    print(df_resultados)

    # Opcional: guardar resultados
    df_resultados.to_csv("data/processed/evaluacion_mensual.csv", index=False)
    print("✅ Resultados guardados en: data/processed/evaluacion_mensual.csv")

if __name__ == "__main__":
    main()
