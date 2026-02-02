import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class EDAHelper:
    """
    Clase auxiliar para realizar un EDA básico y reutilizable sobre un DataFrame de pandas.
    Pensada para usarse como documento accesorio en notebooks de análisis.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    # -------------------------
    # Información general
    # -------------------------
    def overview(self):
        """Muestra información general del DataFrame."""
        print("Shape del DataFrame:")
        print(self.df.shape)
        print("\nTipos de datos:")
        print(self.df.dtypes)
        print("\nPrimeras filas:")
        display(self.df.head())

    def missing_values(self, percentage: bool = True, decimals: int = 2):
        """
        Devuelve nulos por columna.
        percentage=True devuelve el porcentaje.
        """
        nulls = self.df.isnull().sum()
        if percentage:
            nulls = (nulls / len(self.df) * 100).round(decimals)
            return nulls.sort_values(ascending=False)
        return nulls.sort_values(ascending=False)

    # -------------------------
    # Estadística descriptiva
    # -------------------------
    def numeric_summary(self):
        """Resumen estadístico de columnas numéricas."""
        return self.df.describe().T

    def categorical_summary(self):
        """Resumen de columnas categóricas."""
        cat_cols = self.df.select_dtypes(include="object").columns
        summary = {}
        for col in cat_cols:
            summary[col] = self.df[col].value_counts().head(10)
        return summary

    # -------------------------
    # Visualizaciones
    # -------------------------
    def hist(self, column, bins=30):
        """Histograma de una columna numérica."""
        plt.figure(figsize=(6, 4))
        sns.histplot(self.df[column].dropna(), bins=bins, kde=True)
        plt.title(f"Distribución de {column}")
        plt.show()

    def boxplot(self, column):
        """Boxplot para detección de outliers."""
        plt.figure(figsize=(6, 2))
        sns.boxplot(x=self.df[column])
        plt.title(f"Boxplot de {column}")
        plt.show()

    def countplot(self, column, top_n=10):
        """Countplot para variables categóricas."""
        data = self.df[column].value_counts().head(top_n)
        plt.figure(figsize=(6, 4))
        sns.barplot(x=data.values, y=data.index)
        plt.title(f"Top {top_n} valores de {column}")
        plt.show()

    def correlation_matrix(self):
        """Matriz de correlación para variables numéricas."""
        corr = self.df.select_dtypes(include=np.number).corr()
        plt.figure(figsize=(10, 6))
        sns.heatmap(corr, annot=False, cmap="coolwarm")
        plt.title("Matriz de correlación")
        plt.show()

    # -------------------------
    # Utilidades
    # -------------------------
    def unique_values(self, column):
        """Valores únicos y su conteo."""
        return self.df[column].value_counts()

    def outliers_iqr(self, column):
        """Detecta outliers usando el método IQR."""
        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return self.df[(self.df[column] < lower) | (self.df[column] > upper)]

# Ejemplo de uso:
# eda = EDAHelper(df)
# eda.overview()
# eda.missing_values()
# eda.hist("age")
