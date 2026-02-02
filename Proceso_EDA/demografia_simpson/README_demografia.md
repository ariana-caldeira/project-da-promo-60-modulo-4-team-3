# Análisis Exploratorio de Guiones de Los Simpsons

Este notebook  realiza un análisis exploratorio de datos (EDA) sobre un csv que contiene las líneas de guion de la serie de televisión "Los Simpsons" y otro que contiene los datos de los personajes, como género, nombre, etc. 

## 📜 Descripción del Notebook

El propósito principal de este notebook es llevar a cabo una investigación inicial de los datasets para entender su estructura, identificar patrones, detectar anomalías y extraer insights preliminares. Para facilitar este proceso, se utiliza una clase de ayuda personalizada (`EDAHelper`) ubicada en el directorio `src`.

## 📊 Datasets

**Dataset `simpsons_script_lines.csv`**
Columnas:
- id: Identificador único de la línea de guion.
- episode_id: Identificador del episodio.
- number: Orden secuencial de la línea dentro del episodio.
- raw_tex: Texto original del guion, incluyendo nombre del personaje y acotaciones.
- timestamp_in_ms: Marca temporal de la línea dentro del episodio.
- speaking_line: Indica si la línea corresponde a diálogo hablado. Es clave para filtrar acotaciones.
- character_id: Identificador del personaje que pronuncia la línea. Permite relacionar el diálogo con los personajes.
- location_id: Identificador numérico de la localización.
- raw_character_text: Nombre del personaje tal como aparece en el guion.
- raw_location_text: Localización textual donde ocurre la línea.
- spoken_words: Texto hablado sin acotaciones narrativas.
- normalized_text: Versión normalizada del texto hablado.
- word_count: Número de palabras del diálogo.
Se convierte a numérico para el análisis.

**Dataset `simpsons_characters.csv`:**
Columnas:
- id: Identificador único del personaje.
- name: Nombre del personaje.
- normalized_name: Versión normalizada del nombre del personaje.
- gender: Género asignado al personaje.


## ⚙️ Estructura del Análisis

El notebook sigue los siguientes pasos:

1.  **Importación de Librerías:**
    -   Se importan las librerías estándar para el análisis de datos como `pandas`, `numpy`, `matplotlib` y `seaborn`.
    -   Se añade la ruta al directorio `src` para importar la clase de ayuda `EDAHelper`.

2.  **Carga de Datos:**
    -   Se carga el archivo `simpsons_script_lines.csv` en un DataFrame de pandas.

3.  **Análisis Exploratorio con `EDAHelper`:**
    -   **`overview()`**: Muestra una vista general del DataFrame, incluyendo sus dimensiones, los tipos de datos de cada columna y las primeras filas.
    -   **`missing_values()`**: Calcula y muestra el porcentaje de valores nulos por columna para identificar datos faltantes.
    -   **`numeric_summary()`**: Proporciona un resumen estadístico (media, desviación estándar, etc.) de las columnas numéricas.
    -   **`categorical_summary()`**: Analiza las columnas categóricas, mostrando los valores más frecuentes (por ejemplo, los personajes con más diálogos o las frases más repetidas).
    -   **`countplot("episode_id")`**: Genera una visualización que muestra la cantidad de líneas de diálogo por episodio, ayudando a identificar los episodios con más actividad.

## 🚀 Cómo Utilizar

Para ejecutar este notebook:

1.  Asegúrate de tener instaladas todas las dependencias (`pandas`, `numpy`, `matplotlib`, `seaborn`).
2.  Verifica que el archivo `simpsons_script_lines.csv` se encuentre en la carpeta `data`.
3.  Asegúrate de que el módulo `soporte_eda.py` esté en la carpeta `src`.
4.  Ejecuta las celdas del notebook en orden.
