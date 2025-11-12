import pandas as pd
import yfinance as yf
import requests

def extractData(tickers, today):
    """
    Extrae datos de los tickers de Yahoo Finance y del valor actual del Bitcoin desde Coinbase.
    Devuelve un diccionario de DataFrames con los datos de cada activo.
    """

    # DataFrames vacíos para almacenar los datos crudos de cada empresa
    raw_dataframes = {}

    # 1️⃣ Iteramos sobre cada ticker para extraer sus datos desde Yahoo Finance
    for ticker in tickers:
        tk = yf.Ticker(ticker)
        raw_df = tk.history(period="1d")[['Open', 'High', 'Low', 'Close']]
        raw_df.columns = raw_df.columns.str.lower()  # columnas en minúsculas
        raw_dataframes[ticker] = raw_df

    # 2️⃣ Datos BTC desde Coinbase API
    url_btc = "https://api.coinbase.com/v2/prices/BTC-USD/spot?currency=USD"
    valor_btc = requests.get(url_btc).json()

    # Extraemos el valor como float y lo convertimos a entero
    btc_convertido = int(float(valor_btc['data']['amount']))

    # 3️⃣ Creamos un índice basado en la fecha actual
    btc_index = pd.to_datetime([today])

    # 4️⃣ Creamos un DataFrame con el valor de BTC
    btc_dataframe = pd.DataFrame({'btc_usd': [btc_convertido]}, index=btc_index)

    # 5️⃣ Añadimos el DataFrame de BTC al diccionario
    raw_dataframes['BTC_USD'] = btc_dataframe

    # 6️⃣ (Opcional) Mostrar resultados
    for ticker, df in raw_dataframes.items():
        print(f"\n🔹 {ticker}")
        print(df)

    # 7️⃣ Devolver el diccionario completo
    return raw_dataframes
