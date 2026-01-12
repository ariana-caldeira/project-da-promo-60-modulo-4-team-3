# 📺 Análisis de la serie *The Simpsons*

## Audiencia, ratings y premios

---

### Descripción del proyecto
Este proyecto analiza la evolución del éxito de la serie *The Simpsons* a lo largo de más de 35 años de emisión, utilizando métricas de audiencia en Estados Unidos, valoraciones de IMDb y datos históricos de premios y nominaciones. El objetivo es comprender cómo ha cambiado la recepción de la serie con el tiempo y qué temporadas, episodios o años han sido más destacados, culminando en la creación de visualizaciones interactivas en **Tableau**.

---

## 🎯 Objetivo del análisis

- Analizar la evolución del éxito de *The Simpsons* a lo largo del tiempo.
- Evaluar tendencias de audiencia y ratings de IMDb.
- Identificar temporadas y periodos más exitosos.
- Analizar premios ganados y categorías más relevantes.


### ❓ Preguntas de investigación
- ¿Cómo ha evolucionado el rating promedio de IMDb a lo largo de los años?
- ¿Cómo ha cambiado la audiencia (millones de espectadores en USA) con el tiempo?
- ¿Qué temporadas han sido las más exitosas según audiencia y ratings?
- ¿Qué premios ha ganado la serie y en qué categorías?
- ¿Existen periodos con mayor concentración de premios?

---

## 🧠 Metodología y enfoque

1. **Carga de datos**
   - Importación de los datasets de ratings y premios.
   - Revisión inicial de estructura y tipos de datos.

2. **Exploración inicial**
   - Visualización de las primeras filas.
   - Identificación de valores nulos y posibles inconsistencias.

3. **Limpieza y transformación**
   - Conversión de fechas y otros datos a formatos.
   - Eliminación de nulos y columnas sin utilidad.
   - Normalización, organización y renombre de columnas.
   - Unión de tablas para crear un dataset más completo.

4. **Creación del dataset final**
   - Preparación de tablas limpias.
   - Exportación en .csv limpios a ser usados en Tableau.

5. **Análisis exploratorio**
   - Tendencias de audiencia, ratings y premios.
   - Comparación entre temporadas y años.

6. **Visualización**
   - Gráficos temporales y rankings.
   - Dashboards externos en Tableau.

---

## 📂 Datasets utilizados

### simpsons_awards.csv
**Descripción:**  
Contiene información sobre episodios, temporadas, nominaciones y premios ganados por *The Simpsons*.

| Columna        | Descripción                                        |
| -------------- | -------------------------------------------------- |
| award_id       | Identificador único del premio o nominación        |
| organization   | Organización que otorga el premio                  |
| year           | Año en que se otorgó o nominó el premio            |
| award_category | Categoría del premio                               |
| award          | Nombre del premio                                  |
| result         | Resultado (ej. Ganado / Nominado)                  |
| person         | Nombre de la persona asociada al premio            |
| role           | Rol desempeñado por la persona                     |
| character      | Personaje vinculado al premio (si aplica)          |
| episode_id     | Identificador del episodio relacionado (si aplica) |
| season         | Número de temporada del episodio relacionado       |
| episode        | Número del episodio relacionado                    |


---

### simpsons_ratings.csv
**Descripción:**  
Contiene información sobre episodios, temporadas, audiencia y ratings IMDb.

| Columna             | Descripción                                |
| ------------------- | ------------------------------------------ |
| title               | Título del episodio                        |
| description         | Breve descripción del episodio             |
| air_date            | Fecha de emisión del episodio              |
| directed_by         | Nombre del director del episodio           |
| written_by          | Nombre del guionista del episodio          |
| season              | Número de temporada                        |
| episode             | Número del episodio dentro de la temporada |
| us__million_viewers | Audiencia en millones en Estados Unidos    |
| imdb_rating         | Rating del episodio en IMDb                |
| tmdb_rating         | Rating del episodio en TMDb                |
| tmdb_vote_count     | Cantidad de votos en TMDb                  |


---

## 🛠️ Requisitos y tecnologías

### Lenguaje
- Python

### Librerías
- pandas
- numpy
- matplotlib
- seaborn

### Herramientas
- Jupyter Notebook
- Tableau Desktop / Tableau Public

### Formato de datasets
- CSV


---

## ✅ Tareas del proyecto

- [x] Definición del alcance del análisis y de las métricas clave (audiencia, ratings y premios).
- [x] Creación de una carpeta `src` con un archivo de soporte que contiene funciones para la exploración EDA.
- [x] Carga y exploración inicial de los datasets de ratings, audiencias, premios y episodios.
- [x] Revisión y tratamiento de valores nulos.
- [x] Conversión y validación de tipos de datos (fechas, numéricos, categóricos).
- [x] Eliminación de columnas innecesarias para el análisis.
- [x] Unión e integración de los distintos datasets en una estructura coherente.
- [x] Exportación de los dos datasets limpios: ratings y awards.
- [x] Análisis exploratorio de audiencia y ratings de IMDb por temporada y año.
- [x] Análisis de premios y nominaciones, incluyendo categorías y periodos más destacados.
- [x] Visualizaciones de datos con pandas y Matplotlib/Seaborn.
- [x] Exportación de los datasets para Tableau.


---


## 📑 Documento de soporte EDA (`src/eda_support.py`)

Este archivo contiene funciones y configuraciones útiles para la exploración y limpieza de los datasets:

### Contenido principal
- Librerías de visualización (`matplotlib`, `seaborn`)
- Funciones de imputación de nulos (`SimpleImputer`, `IterativeImputer`, `KNNImputer`)
- Configuración para mostrar todas las columnas de un DataFrame
- Función `open_csv(ruta)`:
  - Carga un CSV
  - Reintenta con codificación `latin1` si falla
  - Devuelve un DataFrame o un DataFrame vacío si hay error
- Función `eda_1(df: pd.DataFrame)`:
  - Exploración rápida de un dataset
  - Muestra dimensiones, tipos de datos, duplicados, porcentaje de nulos y valores únicos

### Ejemplo de uso
```python
from src import eda_soporte as eda_sp
```

# Cargar dataset
df_ratings = pd.read_csv("./datasets/simpsons_ratings_episodes.csv", index_col=0)

# Exploración rápida
eda_sp.eda_1(df_ratings)


---


## 💻 Código de ejemplo

### Importar librerías
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Importar documento de soporte
```python
from src import eda_soporte as eda_sp
```

### Cargar datasets
df_award = eda_sp.open_csv("./datasets/award.csv")
df_character_award = eda_sp.open_csv("./datasets/character_award.csv")
df_credit = eda_sp.open_csv("./datasets/credit.csv")
df_episode = eda_sp.open_csv("./datasets/episode.csv")
df_ratings = pd.read_csv("./datasets/simpsons_ratings_episodes.csv", index_col=0)

### Visualizar primeras filas
df_award.head()
df_episode.head()
df_ratings.head()

### Primera exploración EDA
eda_sp.eda_1(df_award)
eda_sp.eda_1(df_episode)
eda_sp.eda_1(df_ratings)

### Limpiar duplicados 
df_credit = df_credit.drop_duplicates()
df_award = df_award.drop_duplicates()

### Eliminar 4 columnas
df_episode = df_episode.drop(columns=['season', 'episode', 'number_in_series', 'episode_image'])

### Ordenar columnas
cols = ['award_id', 'organization', 'year', 'award_category', 'award', 'result', 
        'person', 'role', 'character',
        'episode_id', 'season', 'episode']

df_award = df_award[cols]

### Renombrar columnas
df_ratings = df_ratings.rename(columns={'original_air_date': 'air_date', 'number_in_season': 'episode', 'us_viewers_in_millions': 'us__million_viewers'})

### Unión de datasets
df_award = df_award.merge(df_credit[['episode_id', 'person', 'role']],
            on=['episode_id', 'person'],
            how='left')

### Exportación de datasets limpios
df_award.to_csv("./final_data/simpsons_awards.csv", index=False)
df_ratings.to_csv("./final_data/simpsons_ratings.csv", index=False)

---

## 📈 Visualizaciones

### Customización de colores 
```python
#Custom Colors
class clr:
    S = '\033[1m' + '\033[96m'
    E = '\033[0m'
    
my_colors = ["#2f64d6", "#f8db27", "#9c5b01", "#f0f0f0", "#ff81c1"]
```
![Colores](images/python_colors.png)

### Evolución de los premios por año
![Premios por año](images/premios_ano.png)



## 📌 Notas finales
Este repositorio documenta el proceso de análisis y preparación de datos.
Las visualizaciones finales y conclusiones se presentan en Tableau a partir del dataset limpio generado en este proyecto.
