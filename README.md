# Análisis Financiero Automatizado

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una pequeña librería de análisis financiero automatizado utilizando Python. El objetivo principal es analizar el comportamiento de distintos activos financieros mediante la descarga de datos históricos, cálculo de retornos, análisis estadístico y visualización gráfica.

El proyecto fue desarrollado utilizando datos obtenidos desde Yahoo Finance para los activos AAPL, JPM y TSLA.

---

# Objetivos

- Descargar precios históricos de activos financieros.
- Calcular retornos diarios de los activos.
- Obtener estadísticas descriptivas de los retornos.
- Visualizar el comportamiento de los retornos mediante gráficos.
- Comparar niveles de riesgo entre distintos activos financieros.

---

# Librerías utilizadas

- yfinance
- pandas
- matplotlib

---

# Estructura del proyecto

El proyecto se compone de las siguientes funciones:

## 1. descargar_datos_yf()

Permite descargar precios históricos desde Yahoo Finance.

### Parámetros

- tickers: lista de activos financieros.
- start: fecha de inicio.
- end: fecha de término.

### Retorna

Un DataFrame con precios de cierre.

---

## 2. calcula_retornos()

Calcula los retornos porcentuales diarios utilizando:

```python
df.pct_change().dropna()