# Análisis de la serie The Simpsons

## El Atlas de Springfield: Un viaje por la geografía y el éxito global

**Descripción del proyecto:**
Este análisis explora cómo la dimensión geográfica de *The Simpsons* ha permitido que la serie trascienda fronteras. Analizaremos la ubicuidad de "Springfield", los viajes internacionales de la familia y el origen diverso de sus personajes, examinando cómo estos elementos, sumados a un doblaje extensivo, han construido un fenómeno cultural universal.

---

## 2. Objetivo del análisis

* **Objetivos principales:**
    * Evaluar la importancia de la representación geográfica en la serie.
    * Analizar cómo la geografía ha influido en su conexión emocional con la audiencia global.
* **Preguntas específicas:**
    * ¿Cómo contribuye la multiplicidad de ciudades llamadas "Springfield" a la sensación de cercanía del espectador?
    * ¿Qué regiones del mundo han sido más visitadas por los Simpson y cómo refleja esto su impacto internacional?
    * ¿Cuál es la diversidad real en el origen de los personajes secundarios?
    * ¿A cuántos idiomas se ha traducido la serie para mantener su relevancia local?

---

## 3. Enfoque y metodología

El análisis se lleva a cabo siguiendo estos pasos:
1.  **Generación y Limpieza:** Uso de IA para recopilar información geográfica (Springfields, viajes, orígenes, doblaje) y estructurarla en datasets limpios.
2.  **Transformación:** Preparación de los datos para asegurar la compatibilidad con herramientas de visualización.
3.  **Análisis Exploratorio:** Verificación de la coherencia de los datos generados.
4.  **Visualización:** Creación de mapas y gráficos interactivos en Tableau para identificar patrones geográficos.

---

## 4. Datasets utilizados

| Archivo | Descripción | Columnas Relevantes |
| :--- | :--- | :--- |
| `Springfields.csv` | Listado de ubicaciones con el nombre Springfield en la realidad. | `Ciudad`, `Estado/País`, `Latitud`, `Longitud` |
| `Simpson_travel_countries_2.csv` | Registro de los países visitados por la familia. | `País`, `Continente`, `Temporada`, `Episodio` |
| `Origin_characters_all.csv` | Origen geográfico o étnico de los personajes. | `Nombre`, `Origen`, |
| `Dubbing_simpsons.csv` | Idiomas y regiones donde se dobla la serie. | `Idioma`, `Región` |

---

## 5. Requisitos y tecnologías

* **Python (Pandas):** Para la carga y exploración inicial de los datos.
* **Tableau:** Herramienta principal para el análisis visual y cartográfico.
* **Jupyter Notebook:** Entorno de documentación y ejecución de código.

---

## 6. Tareas del proyecto

- [x] **Exploración:** Identificación de variables geográficas clave.
- [x] **Limpieza:** Generación de datos sintéticos coherentes mediante IA.
- [x] **Análisis:** Cruce de datos entre países visitados y éxito de la serie.
- [x] **Visualización:** Desarrollo de dashboards en Tableau.
- [x] **Documentación:** Redacción de hallazgos finales en este Readme.

---
