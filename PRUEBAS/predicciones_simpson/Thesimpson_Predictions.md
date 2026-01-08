# 📊 Análisis de la serie *The Simpsons*

## Predicciones, cronovinculación y geografía del oráculo

---

## 📌 Descripción del proyecto

Este proyecto analiza el fenómeno cultural de las denominadas **predicciones de *The Simpsons***, explorando la relación temporal, temática y geográfica entre eventos representados en la serie y sucesos reales ocurridos posteriormente.

El análisis se apoya en un dataset estructurado y normalizado que documenta coincidencias entre ficción y realidad. El objetivo es identificar patrones temporales, categorías dominantes, personajes implicados y la distribución geográfica de estas predicciones, culminando en la creación de visualizaciones interactivas en **Tableau**.

---

## 🎯 Objetivos del análisis

* **Cuantificar la cronovinculación**
  Evaluar el grado de acierto entre la ficción y la realidad analizando el tiempo transcurrido entre la emisión del episodio y el evento real.

* **Mapear la geografía del oráculo**
  Analizar la dimensión global de las predicciones mediante la identificación de regiones y países con mayor densidad de coincidencias.

* **Perfilado de portavoces proféticos**
  Identificar qué personajes de la serie actúan como principales conductores de estas visiones del futuro.

* **Taxonomía de aciertos**
  Clasificar las predicciones por categorías temáticas (Política, Tecnología, Sociedad, etc.) para detectar en qué áreas la serie resulta más visionaria.

* **Ingeniería de datos para visualización**
  Normalizar y optimizar un dataset complejo, resolviendo conflictos de geolocalización y formato, para su explotación interactiva en Tableau.

---

## ❓ Preguntas de investigación

* ¿Cuál es el **epicentro de profecías**?
  ¿Qué países o regiones presentan una mayor densidad de predicciones cumplidas?

* ¿Quién es el **personaje oráculo**?
  ¿Qué personaje aparece con mayor frecuencia en predicciones de alto impacto o viralidad?

* ¿Cuál es la **brecha temporal del futuro**?
  ¿Cuántos años pasan, en promedio, entre la emisión del episodio y el evento real?

* ¿Qué **temas dominan la narrativa predictiva**?
  ¿Predominan las predicciones tecnológicas sobre las políticas y cómo varía esto según el nivel de coincidencia?

* ¿Cómo influye la **viralidad**?
  ¿Existe relación entre el nivel de coincidencia y el número de visualizaciones (*views*)?

---

## 🧠 Metodología

El proyecto se desarrolla siguiendo las siguientes fases:

1. **Exploración inicial del dataset**

   * Revisión de estructura, tipos de datos y valores nulos.
   * Comprensión del esquema de columnas.

2. **Limpieza y normalización**

   * Unificación de formatos de fecha.
   * Normalización de ubicaciones geográficas (países y regiones).
   * Estandarización de identificadores, categorías y métricas numéricas.

3. **Transformación y enriquecimiento**

   * Cálculo de métricas temporales (diferencia de años).
   * Creación de campos auxiliares para análisis geográfico y temático.
   * Preparación del dataset final para visualización.

4. **Análisis exploratorio (EDA)**

   * Distribución temporal de las predicciones.
   * Análisis por categorías, personajes y regiones.
   * Exploración de relaciones entre coincidencia y viralidad.

5. **Visualización**

   * Exportación del dataset limpio para Tableau.
   * Creación de dashboards interactivos (mapas, rankings y gráficos de dispersión).

---

## 📁 Dataset

### Dataset principal

* **Archivo:** `the_simpson_predictions.csv`
* **Formato:** CSV

**Descripción:**
Dataset que documenta predicciones atribuidas a *The Simpsons*, vinculando eventos ficticios con sucesos reales ocurridos posteriormente. El archivo fue generado mediante un proceso híbrido de investigación manual y estructuración asistida por Inteligencia Artificial, y finalmente normalizado y exportado usando **Pandas**.

---

### 🧱 Estructura del dataset

| Columna                 | Descripción                          |
| ----------------------- | ------------------------------------ |
| ID                      | Identificador único de la predicción |
| EPISODIO                | Título completo del episodio         |
| TEMPORADA               | Número de temporada                  |
| EPISODIO_NUM            | Número de episodio                   |
| FECHA_EMISION           | Fecha original de emisión            |
| AÑO_EMISION             | Año de emisión                       |
| CATEGORIA               | Tema principal de la predicción      |
| UBICACION               | Lugar geográfico asociado            |
| DESCRIPCION             | Descripción del evento en la serie   |
| PREDICCION              | Evento ocurrido en la vida real      |
| DIFERENCIA_AÑOS         | Años entre emisión y evento real     |
| NIVEL_COINCIDENCIA      | Baja / Media / Alta                  |
| PERSONAJE *(si aplica)* | Personaje asociado                   |
| VIEWS *(si aplica)*     | Métrica de impacto o viralidad       |

---

## 🧹 Decisiones de limpieza y normalización

* Las decisiones de limpieza y normalización se basan en un proceso híbrido de análisis humano y estructuración asistida por IA.
* Se unificaron formatos de fecha (AAAA-MM-DD) y se estandarizaron identificadores y categorías temáticas.
* Las ubicaciones geográficas fueron normalizadas mediante correcciones manuales para garantizar consistencia internacional.
* Todo el proceso fue gestionado y validado en Python utilizando Pandas, asegurando la coherencia del dataset y su correcta explotación analítica y visual.

---

## 🛠️ Tecnologías utilizadas

* **Python**
  * Pandas
  * NumPy
* **Jupyter Notebook**
  * Análisis exploratorio y preparación de datos
* **Tableau Desktop / Tableau Public**
  * Visualización interactiva final
* **CSV**
  * Formato del dataset principal
* **Geocodificación manual**
  * Corrección y estandarización de ubicaciones

---
## ✅ Estado del proyecto

- [x] Definición del esquema de datos  
- [x] Creación y normalización del dataset  
- [x] Cargar y explorar el dataset  
- [x] Analizar valores nulos y tipos de datos  
- [x] Limpiar y normalizar fechas y ubicaciones  
- [x] Crear métricas temporales y categóricas  
- [x] Analizar distribución por categorías  
- [x] Analizar geografía de predicciones  
- [x] Analizar personajes y niveles de coincidencia  
- [x] Exportar dataset final para Tableau  
- [x] Documentar hallazgos y conclusiones  

---
## 7️⃣ Código de ejemplo (base)

```python
import pandas as pd

# Carga del dataset
df = pd.read_csv("the_simpson_predictions.csv")

# Visualizar primeras filas
df.head()

# -----------------------------
# Identificar y revisar valores nulos
# -----------------------------
filas_con_nulos = df.isnull().any(axis=1)
df_con_nulos = df[filas_con_nulos]
print("Filas con valores nulos:")
df_con_nulos

# -----------------------------
# Rellenar nulos simples
# -----------------------------
# Por ejemplo, trasladar TITLE a TITLE_EPISODES
if 'TITLE' in df.columns:
    df['TITLE_EPISODES'] = df['TITLE_EPISODES'].fillna(df['TITLE'])

# -----------------------------
# Reordenar columnas principales
# -----------------------------
nuevo_orden = [
    'ID', 'TITLE_EPISODES', 'SEASON_EPISODE_NUMERIC', 'NUMBER_IN_SEASON',
    'YEAR', 'PREDICTION CATEGORY', 'GEOGRAPHICAL LOCATION',
    'COINCIDENCE LEVEL', 'DIFFERENCE (YEARS)', 'DESCRIPTION', 'PREDICTION', 'VIEWS'
]
df = df[nuevo_orden].copy()

print("Columnas reordenadas con éxito:")
print(list(df.columns))

---

## 📌 Notas finales

Este repositorio documenta el proceso de análisis y preparación de datos.
Las visualizaciones finales y conclusiones se presentan en Tableau a partir del dataset limpio generado en este proyecto.
