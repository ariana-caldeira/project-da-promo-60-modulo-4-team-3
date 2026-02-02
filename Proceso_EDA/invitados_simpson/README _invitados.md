# Análisis exploratorio de Invitados de Los Simpsons

### 📋 1. Descripción y Objetivos
Este proyecto busca descifrar el ADN de Los Simpsons cruzando dos fuentes de datos principales. Queremos entender quiénes son los invitados y de qué sectores vienen.

### 🎯 Preguntas Clave:
**Invitados**: ¿Cómo es el recuento por temporada y qué sectores (música, cine, etc.) predominan?

### 🛠️ 2. Tecnologías y Metodología
**Stack**: Pandas, Numpy, Matplotlib, Seaborn.

**Destino**: Limpieza y pre-procesamiento para visualización final en Tableau.

**Flujo**: Carga ➡️ Limpieza Manual ➡️ Cruce de Tablas (Merging) ➡️ EDA ➡️ Exportación.

### 📂 3. Inventario de Datasets

simpsonguest1.csv:	Estrellas invitadas, roles y sectores.

simpsons_episodes.csv:	Datos técnicos, temporadas y ratings.


### 🚀 4. Hoja de Ruta: Procesamiento de Datos de Los Simpsons
Este apartado describe la lógica de ejecución del análisis, desde la preparación del entorno hasta la generación de archivos listos para Tableau.

**🛠️ Fase 1: Configuración e Ingesta**

**Preparación del Entorno**: Importar las librerías base (Pandas, Numpy) y configurar las herramientas de visualización (Matplotlib, Seaborn) con una estética acorde a la serie.

**Carga de Datos**: Importación de los cuatro archivos fundamentales:

simpsonguest1.csv (Invitados)

simpsons_episodes.csv (Episodios)


**🔍 Fase 2: Auditoría y Limpieza (EDA Manual)**
**Inspección de Integridad**: Revisión manual de las dimensiones de cada tabla y detección de valores nulos (especialmente en nombres de invitados y sectores a los que pertenecen).

**📊 Fase 3: Análisis y Visualización**
**Identificación de Sectores**: Análisis de frecuencia para determinar si Springfield recibe más músicos, actores o deportistas.

**Validación Visual**: Generación de gráficos de barras y líneas para confirmar tendencias antes de la exportación final.

**📤 Fase 5: Preparación para Tableau**
**Consolidación**: Selección de columnas clave (Temporada, Invitado, Rating, Género, Palabra).

**Exportación**: Exportación de los archivos para trabajar con ellos en Tableau.



