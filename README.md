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

4. **Descargar los datos crudos**  
   Debes descargar manualmente los archivos Parquet desde el sitio oficial de NYC Taxi & Limousine Commission: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
    
    Guárdalos en la carpeta data/raw/ con los siguientes nombres:
    * yellow_tripdata_2020-01.parquet
    * yellow_tripdata_2020-02.parquet
    * yellow_tripdata_2020-03.parquet
    * yellow_tripdata_2020-04.parquet

5. **Procesar datos y entrenar modelo base (enero):**  
   Por ejemplo:
   ```bash
        python -m src.pipeline_mes --mes 01
        python -m src.modeling.train
   ```

6. **Evaluar el modelo base:**
   ```bash
   python -m src.modeling.predict
   ```

7. **Evaluación mensual del modelo:**
    ```bash
    python -m src.modeling.evaluate_by_month
    ```
    Esto generará una tabla con el F1-score por mes y cantidad de registros evaluados.

8. **Visualización de resultados**
    ```bash
    python -m src.visualization.run_plots
    ```
    Se guardarán los gráficos en la carpeta figures/.

---

## ⚠️ Requisitos previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Anaconda/Miniconda para gestión de entornos

> ⚠️ **Nota:** El procesamiento de los archivos Parquet puede requerir varios GB de RAM y algo de tiempo, dependiendo de tu equipo.

## 🛠️ Soporte

¿Tienes dudas o encontraste un bug?  
Abre un issue en [GitHub Issues](https://github.com/Joselota/nyc-taxi-tip-classifier/issues) o contacta a Ingrid Solis(Joselota).

## 📚 Créditos

- Datos originales: [NYC Taxi & Limousine Commission](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- Inspirado en prácticas de ingeniería de datos y ciencia de datos reproducible.

---


