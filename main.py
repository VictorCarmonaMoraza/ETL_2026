import numpy as np
import pandas as pd
from prefect import flow, task

# devuelve un rango de fechas diarias entre dos fechas dadas
dias = pd.date_range('2021-10-01', '2021-10-10', freq='d')

## SECCION de Valor 1
# genera 10 valores aleatorios entre 10 y 200
valor_1_cierre = np.random.uniform(low=10, high=200, size=10)

# genera 10 valores aleatorios entre 10 y 2000
valor_1_diferencia = np.random.uniform(low=10, high=2000, size=10)

# genera 10 valores aleatorios de '+' o '-' con igual probabilidad
# np.random.choice() -->Genera una muestra aleatoria de valores
# a=('-', '+') -->Los valores posibles son '+' y '-'
# p=(0.5, 0.5) -->Probabilidad igual para ambos (50%)
# size=10 -->Se generan 10 valores aleatorios
valor_1_tendencia = np.random.choice(a=('-', '+'), p=(0.5, 0.5), size=10)
valor_1_rango = np.random.uniform(low=10, high=2000, size=10)

#Seccion de Valor 2
valor_2_cierre = np.random.uniform(low=10, high=2000, size=10)
valor_2_diferencia = np.random.uniform(low=10, high=2000, size=10)
valor_2_tendencia = np.random.choice(a=('-', '+'), p=(0.5, 0.5), size=10)
valor_2_rango = np.random.uniform(low=10, high=20000, size=10)

# Secion de Valor_BITCOIN
valor_bitcoin = np.random.uniform(low=10, high=20000, size=10)

#Creacion de dataframe con los datos generados
#index=dias -->Esto es clave 👉 le da una etiqueta temporal (fecha) a cada fila.
df_valores = pd.DataFrame({
    'VALOR_1_CIERRE': valor_1_cierre,
    'VALOR_1_DIFERENCIA': valor_1_diferencia,
    'VALOR_1_TENDENCIA': valor_1_tendencia,
    'VALOR_1_RANGO': valor_1_rango,
    'VALOR_2_CIERRE': valor_2_cierre,
    'VALOR_2_DIFERENCIA': valor_2_diferencia,
    'VALOR_2_TENDENCIA': valor_2_tendencia,
    'VALOR_2_RANGO': valor_2_rango,
    'VALOR_BITCOIN': valor_bitcoin}, index=dias)


print(df_valores.head(10))

#****EXTRACCION DE DATOS CON PREFECT****
import yfinance as yf

# Crear un objeto Ticker para la acción de Amazon
# yf es el alias de la librería yfinance, que sirve para obtener datos de acciones desde Yahoo Finance
tk = yf.Ticker("AMZN")
#.history(period="1d") -->Obtiene el historial de precios de esa acción durante el último día.
#pd.DataFrame() -->Convierte los datos obtenidos en un DataFrame de pandas para facilitar su manipulación y análisis.
raw_df = pd.DataFrame(tk.history(period="1d"))

#Filtramos el Dataframe para quedarnos solo con las columnas que nos interesan
raw_df = raw_df[['Open', 'High', 'Low', 'Close']]

print(raw_df)
