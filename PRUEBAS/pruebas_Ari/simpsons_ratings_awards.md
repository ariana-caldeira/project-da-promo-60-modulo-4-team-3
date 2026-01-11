# 📺 Análisis de la serie *The Simpsons*
## Audiencia, ratings y premios

### Descripción del proyecto
Este proyecto analiza la evolución del éxito de la serie *The Simpsons* a lo largo de más de 35 años de emisión, utilizando métricas de audiencia en Estados Unidos, valoraciones de IMDb y datos históricos de premios y nominaciones. El objetivo es comprender cómo ha cambiado la recepción de la serie con el tiempo y qué temporadas, episodios o años han sido más destacados.

---

## 🎯 Objetivo del análisis

### Objetivos principales
- Analizar la evolución del éxito de *The Simpsons* a lo largo del tiempo.
- Evaluar tendencias de audiencia y ratings de IMDb.
- Identificar temporadas y periodos más exitosos.
- Analizar premios ganados y categorías más relevantes.

> ✍️ Aquí puedes añadir o ajustar los objetivos si lo necesitas.

### Preguntas específicas
- ¿Cómo ha evolucionado el rating promedio de IMDb a lo largo de los años?
- ¿Cómo ha cambiado la audiencia (millones de espectadores en USA) con el tiempo?
- ¿Qué temporadas han sido las más exitosas según audiencia y ratings?
- ¿Qué premios ha ganado la serie y en qué categorías?
- ¿Existen periodos con mayor concentración de premios?

---

## 🧭 Enfoque y metodología

1. **Carga de datos**
   - Importación de los datasets de ratings y premios.
   - Revisión inicial de estructura y tipos de datos.

2. **Exploración inicial**
   - Visualización de las primeras filas.
   - Identificación de valores nulos y posibles inconsistencias.

3. **Limpieza y transformación**
   - Conversión de fechas a formatos adecuados.
   - Normalización de columnas.
   - Filtrado de registros relevantes.

4. **Enriquecimiento del dataset (si aplica)**
   - Agregaciones por año o temporada.
   - Cálculo de métricas agregadas.

5. **Creación del dataset final**
   - Preparación de tablas limpias.
   - Exportación para Tableau.

6. **Análisis exploratorio**
   - Tendencias de audiencia y ratings.
   - Comparación entre temporadas.

7. **Visualización**
   - Gráficos temporales y rankings.
   - Dashboards externos en Tableau.

---

## 📂 Datasets utilizados

### simpsons_awards.csv
**Descripción:**  
Contiene información sobre nominaciones y premios ganados por *The Simpsons*.

| Columna | Descripción |
|------|------------|
| year | Año del premio o nominación |
| award | Nombre del premio |
| award_category | Categoría del premio |
| result | Resultado (ganado / nominado) |
| episode_id | Identificador del episodio |

---

### simpsons_ratings.csv
**Descripción:**  
Contiene información sobre episodios, temporadas, audiencia y ratings IMDb.

| Columna | Descripción |
|------|------------|
| title | Título del episodio |
| air_date | Fecha de emisión |
| directed_by | Director del episodio |
| written_by | Guionista |
| season | Número de temporada |
| episode | Número de episodio |
| us__million_viewers | Audiencia en millones (USA) |
| imdb_rating | Rating IMDb |

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
- Tableau

---

## ✅ Tareas del proyecto

- [ ] Carga y exploración de datos  
- [ ] Limpieza y transformación  
- [ ] Análisis de audiencia  
- [ ] Análisis de ratings IMDb  
- [ ] Análisis de premios  
- [ ] Visualización  
- [ ] Exportación para Tableau  
- [ ] Documentación de hallazgos  

---

## 💻 Código de ejemplo

### Importar librerías
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Cargar datasets

df_awards = pd.read_csv("simpsons_awards.csv")
df_ratings = pd.read_csv("simpsons_ratings.csv")
