import pandas as pd
from src.visualization.plots import plot_f1_by_month, plot_volume_by_month

def main():
    df = pd.read_csv("data/processed/evaluacion_mensual.csv")
    
    print("📊 Generando gráfico de F1-score por mes...")
    plot_f1_by_month(df, save_path="figures/f1_score_by_month.png")

    print("📊 Generando gráfico de volumen por mes...")
    plot_volume_by_month(df, save_path="figures/volume_by_month.png")

if __name__ == "__main__":
    main()
