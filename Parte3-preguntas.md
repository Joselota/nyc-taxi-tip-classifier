Parte 3: Evaluación Mensual del Modelo

1. Carga y Evaluación del Modelo en Múltiples Meses
Para evaluar la estabilidad del modelo entrenado, se seleccionaron tres meses distintos: febrero, marzo y abril de 2020.
El modelo se entrenó con datos de enero y luego se evaluó con cada uno de los meses posteriores por separado. Esto permitió analizar su desempeño temporal con datos no vistos.

El script utilizado para esta evaluación fue: src/modeling/evaluate_by_month.py
Este archivo carga el modelo entrenado (random_forest_2020_01.joblib) y evalúa automáticamente su rendimiento sobre los archivos:
features_2020-02.csv
features_2020-03.csv
features_2020-04.csv

Cada evaluación entrega el F1-score y el número de ejemplos considerados.

2. Automatización de la Evaluación
Se desarrolló una función que automatiza la evaluación del modelo sobre distintos conjuntos mensuales, entregando como resultado una tabla estructurada con las siguientes columnas:
mes: período evaluado
n: cantidad de registros utilizados en la evaluación
f1_score: métrica de desempeño principal
El resultado se guarda en: data/processed/evaluacion_mensual.csv
Esto permite reutilizar fácilmente la lógica para más meses o futuros modelos.


3. Visualización y Análisis (opcional pero realizado)
Se generaron dos visualizaciones para facilitar el análisis del comportamiento mensual del modelo:
* Gráfico de F1-score por mes, para observar posibles caídas de desempeño.
* Gráfico de volumen de datos por mes, para verificar si la cantidad de datos influye en la métrica.

Ambos gráficos fueron generados con el script:
src/visualization/run_plots.py
Y guardados en: figures/f1_score_by_month.png  
                figures/volume_by_month.png
Estas visualizaciones se incorporaron al README.md junto con un análisis crítico y recomendaciones para mejorar la robustez del modelo.


¿El modelo mantiene un rendimiento consistente?
No completamente. El modelo muestra un rendimiento razonablemente estable durante los meses de febrero (F1: 0.617) y marzo (F1: 0.638), pero sufre una caída significativa en abril (F1: 0.561).

¿Qué factores podrían explicar la variación en el desempeño?
Algunos posibles factores:
* Cambios estacionales o de comportamiento en los usuarios de taxis en NYC.
* Impacto del COVID-19: en abril de 2020 comienzan las restricciones fuertes en la ciudad, lo que pudo cambiar la naturaleza de los viajes.
* Cambios en la distribución de las clases (propinas generosas vs. no generosas) y de las variables predictoras.
* Ausencia de variables temporales o contextuales en el modelo.

¿Qué acciones recomendarías para mejorar la robustez del modelo en el tiempo?
* Reentrenar el modelo de forma mensual o trimestral para adaptarse a los cambios de distribución.
* Agregar nuevas features relevantes como condiciones climáticas, día del mes o eventos especiales.
* Evaluar un modelo más robusto o adaptable (por ejemplo, XGBoost, LightGBM).
* Implementar una validación temporal (TimeSeriesSplit) en lugar de una validación aleatoria.