# 📊 Proyecto ETL con Prefect, NumPy, Pandas y Yahoo Finance

Este proyecto combina **generación de datos simulados** con **extracción de datos bursátiles reales** mediante la API de **Yahoo Finance**, utilizando herramientas de **Python** como `NumPy`, `Pandas`, y `Prefect`.

El objetivo es construir un flujo de datos reproducible que genere valores financieros de ejemplo y obtenga información real de la acción de **Amazon (AMZN)**.

---

## 🚀 Descripción del proyecto

El script realiza dos partes principales:

### 1️⃣ Generación de datos simulados
Crea un **DataFrame (`df_valores`)** con información ficticia de dos valores financieros y el precio de Bitcoin, simulando métricas como:
- Cierre (`Cierre`)
- Diferencia (`Diferencia`)
- Tendencia (`Tendencia`)
- Rango (`Rango`)

Para ello utiliza:
- `numpy.random.uniform()` → genera números aleatorios dentro de un rango definido.
- `numpy.random.choice()` → elige símbolos `'+'` o `'-'` aleatoriamente con igual probabilidad.
- `pandas.date_range()` → genera un rango de fechas diarias (del 1 al 10 de octubre de 2021).

🔹 El resultado es un **DataFrame indexado por fechas** que podría representar la evolución diaria de valores financieros simulados.

---

### 2️⃣ Extracción de datos reales con Yahoo Finance

Utilizando la librería `yfinance`, se conecta con la API pública de **Yahoo Finance** para descargar el **historial diario** de precios de la acción de **Amazon (AMZN)**:

- Se crea un objeto `Ticker` con:
  ```python
  tk = yf.Ticker("AMZN")
