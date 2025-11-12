# Importar librerias necesarias y definciono de entornos

from prefect import task, flow

from data import tickers, today
from extract import extractData


# 1-Extraccion: yfinance + API Coinbase
@task
def extract_data(tickers, today):
    raw_dfs =extractData(tickers, today)
    return raw_dfs


# 2-Trandformacion: limpieza y agregacion
@task
def transform_data():
    pass


# 3-Carga
@task
def load():
    pass


# 4-FLOW
@flow(name="ETL Caso")
def etl_caso():
    raw_df = extract_data(tickers, today)
    # tablon = transform_data(raw_df)
    # load(tablon)
    pass


# 🚀 Ejecución (Prefect 2+)
if __name__ == "__main__":
    etl_caso()
