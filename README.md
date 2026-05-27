# Análisis Financiero Automatizado

Proyecto desarrollado en Python para realizar análisis financiero automatizado sobre distintos activos.

## Funcionalidades

- Descarga de precios históricos desde Yahoo Finance.
- Cálculo de retornos diarios.
- Cálculo de estadísticos descriptivos.
- Visualización de retornos mediante gráficos.

## Activos analizados

- AAPL
- JPM
- TSLA

## Periodo analizado

Desde el 2021-01-01 hasta el 2024-01-01.

## Librerías utilizadas

- yfinance
- pandas
- matplotlib

## Cómo ejecutar el proyecto

Instalar las librerías:

```bash
pip install -r requirements.txt

## Respuestas del análisis

### ¿Cuál es el activo con mayor riesgo según volatilidad?

El activo con mayor riesgo es TSLA, ya que presenta la mayor volatilidad entre los activos analizados.

### ¿Algún activo presenta distribución de retornos no simétrica o con colas pesadas?

Sí, TSLA presenta una distribución con mayor kurtosis y señales de colas pesadas, lo que indica mayor presencia de movimientos extremos.

### ¿Qué diferencias observas entre TSLA y JPM respecto a riesgo?

TSLA presenta un nivel de riesgo más alto que JPM, ya que sus retornos son más volátiles y muestran variaciones más extremas. JPM, en cambio, presenta un comportamiento más estable.
