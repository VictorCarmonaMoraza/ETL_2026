import numpy as np
import pandas as pd
from prefect import flow, task

# devuelve un rango de fechas diarias entre dos fechas dadas
dias = pd.date_range('2021-10-01','2021-10-10', freq='d')

# genera 10 valores aleatorios entre 10 y 200
valor_1_cierre = np.random.uniform(low=10, high=200, size=10)

print(dias)
print(valor_1_cierre)