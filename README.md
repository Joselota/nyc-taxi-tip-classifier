# NYC Taxi Tip Classifier 🗽🚕

Este proyecto implementa un clasificador de propinas basado en viajes de taxi en Nueva York durante el año 2020. Utiliza técnicas de aprendizaje automático y buenas prácticas de ingeniería de software para transformar un notebook exploratorio en un proyecto modular, reproducible y mantenible.

## 📌 Objetivo

Predecir si un viaje de taxi tendrá una propina generosa (mayor al 20%) utilizando características como distancia del viaje, hora del día, ubicación de recogida y bajada, entre otros.

Además, se analiza el rendimiento del modelo a lo largo del tiempo (meses del año) para detectar posibles variaciones estacionales.

---

## 🗂️ Estructura del Proyecto
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



