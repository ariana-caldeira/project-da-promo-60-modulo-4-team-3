
# DOCUMENTO DE SOPORTE A ANALISIS EDA

import pandas as pd
import numpy as np

# Imputación de nulos
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
import seaborn as sns
import matplotlib.pyplot as plt

# Visualizar todas las columnas de los DataFrames
pd.set_option('display.max_columns', None)



#__________________________________________________
# FUNCIÓN .READ CSV
def open_csv(ruta):   
    """
    Intenta cargar un archivo CSV. Si falla por codificación, 
    intenta de nuevo con 'latin1'.
    """
    try:
        df = pd.read_csv(ruta)
        print("Archivo cargado con éxito")
        return df
    except Exception:
         try:
            df = pd.read_csv(ruta, encoding='latin1')
            print("Archivo cargado con éxito (latin1)")
            return df
         except Exception as e:
            print(f"❌ No se pudo cargar el archivo. ERROR: {e}")
            return pd.DataFrame()



#____________________________________________________
# PRIMERA EXPLORACIÓN EDA - Resumen
def eda_1(df: pd.DataFrame):

    print("🔍 EXPLORACIÓN RÁPIDA EDA")

    # 1. Dimensiones del dataframe
    print("\n____ DIMENSIONES ____")
    print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")

    # 2. Mostrar Tipos de Datos de cada columna
    print("\n____ TIPO DE DATOS ____")
    print(df.dtypes)

    # 3. Filas Duplicadas
    print("\n____ DUPLICADOS ____")
    print(df.duplicated().sum())

    # 4. Mostrar el Porcentaje de Nulos (isna().sum()/len(df)*100)
    print("\n____ % DE NULOS ____")
    null_percentages = round((df.isna().sum() / len(df)) * 100, 2)
    print(null_percentages)

    # 5. Buscar si hay columnas con valores únicos
    print("\n____ VALORES ÚNICOS ____")
    print(df.nunique())

    print("\n--- ✅ Inspección EDA terminada ---")

