import matplotlib.pyplot as plt
import seaborn as sns

def plot_f1_by_month(df, save_path=None):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="mes", y="f1_score", palette="viridis")
    plt.title("F1-score por mes")
    plt.ylabel("F1-score")
    plt.xlabel("Mes")
    plt.ylim(0, 1)
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"📸 Gráfico guardado en: {save_path}")
    else:
        plt.show()

def plot_volume_by_month(df, save_path=None):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="mes", y="n", palette="crest")
    plt.title("Cantidad de registros evaluados por mes")
    plt.ylabel("Número de registros")
    plt.xlabel("Mes")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"📸 Gráfico guardado en: {save_path}")
    else:
        plt.show()

