![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/github/license/Joselota/nyc-taxi-tip-classifier)
![Repo size](https://img.shields.io/github/repo-size/Joselota/nyc-taxi-tip-classifier)

# NYC Taxi Tip Classifier 🗽🚕

Este proyecto implementa un clasificador de propinas basado en viajes de taxi en Nueva York durante el año 2020. Utiliza técnicas de aprendizaje automático y buenas prácticas de ingeniería de software para transformar un notebook exploratorio en un proyecto modular, reproducible y mantenible.

## 📌 Objetivo

Predecir si un viaje de taxi tendrá una propina generosa (mayor al 20%) utilizando características como distancia del viaje, hora del día, ubicación de recogida y bajada, entre otros.

Además, se analiza el rendimiento del modelo a lo largo del tiempo (meses del año) para detectar posibles variaciones estacionales.

---

## 📁 Estructura del Proyecto

```text
├── README.md               <- Este archivo.
├── requirements.txt        <- Dependencias necesarias.
├── data/
│   ├── raw/                <- Datos originales descargados.
│   └── processed/          <- Datos limpios y preparados.
├── models/                 <- Modelos entrenados serializados (.joblib).
├── notebooks/              <- Notebooks exploratorios y de validación.
├── src/
│   ├── __init__.py
│   ├── config.py           <- Parámetros globales y rutas.
│   ├── data/
│   │   └── dataset.py      <- Carga y limpieza de datos.
│   ├── features/
│   │   └── build_features.py <- Generación de variables predictoras.
│   ├── modeling/
│   │   ├── train.py        <- Entrenamiento del modelo.
│   │   └── predict.py      <- Evaluación y predicción.
│   └── visualization/
│       └── plots.py        <- Gráficas de resultados.
```
----
## 📥 Descarga de Datos

Puedes descargar los datos originales desde el sitio oficial de NYC Taxi & Limousine Commission:

👉 [https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

Para este proyecto se utilizó el dataset de **Yellow Taxi - Enero 2020** (`yellow_tripdata_2020-01.parquet`), aunque puedes probar con otros meses.

Guarda los archivos descargados en la carpeta: `data/raw/`.

## 📦 Ejecución rápida
from src.modeling.predict import predict_for_month

model = load_model("models/random_forest_january.joblib")
df = pd.read_parquet("data/processed/february.parquet")
f1 = predict_for_month(model, df)
print(f"F1-score febrero: {f1}")

## 🤝 Cómo contribuir

¿Tienes ideas para mejorar este proyecto? ¡Contribuciones son bienvenidas!

1. Haz un fork del repositorio.
2. Crea una rama con tu mejora: `git checkout -b mejora-nueva`.
3. Haz commit de tus cambios: `git commit -m 'Agrega nueva funcionalidad'`.
4. Haz push a tu rama: `git push origin mejora-nueva`.
5. Abre un Pull Request.



