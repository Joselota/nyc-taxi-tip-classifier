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

## 🚀 Instalación y ejecución desde cero

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Joselota/nyc-taxi-tip-classifier.git
   cd nyc-taxi-tip-classifier
   ```

2. **Crea un entorno virtual (opcional pero muy recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Mac/Linux
   # .\venv\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Descarga los datos y colócalos en `data/raw/`**  
   (Ver sección anterior para el enlace de descarga).

5. **Ejecuta el pipeline de procesamiento y entrenamiento:**  
   Por ejemplo:
   ```bash
   python src/data/dataset.py
   python src/features/build_features.py
   python src/modeling/train.py
   ```

6. **Haz predicciones:**
   ```bash
   python src/modeling/predict.py
   ```

> Si usas Anaconda, puedes crear el entorno con:
> ```bash
> conda create -n taxi-tip python=3.11
> conda activate taxi-tip
> pip install -r requirements.txt
> ```

---

Esto permitirá que cualquier persona pueda reproducir tu proyecto fácilmente.  
¿Quieres que lo agregue al README por ti?## 🚀 Instalación y ejecución desde cero

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Joselota/nyc-taxi-tip-classifier.git
   cd nyc-taxi-tip-classifier
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Mac/Linux
   # .\venv\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Descarga los datos y colócalos en `data/raw/`**  
   (Ver sección anterior para el enlace de descarga).

5. **Ejecuta el pipeline de procesamiento y entrenamiento:**  
   Por ejemplo:
   ```bash
   python src/data/dataset.py
   python src/features/build_features.py
   python src/modeling/train.py
   ```

6. **Haz predicciones:**
   ```bash
   python src/modeling/predict.py
   ```

> Si usas Anaconda, puedes crear el entorno con:
> ```bash
> conda create -n taxi-tip python=3.11
> conda activate taxi-tip
> pip install -r requirements.txt
> ```


