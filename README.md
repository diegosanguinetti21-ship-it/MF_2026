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

# Funciones implementadas

## 1. descargar_datos_yf()

Permite descargar precios históricos desde Yahoo Finance y retornar un DataFrame con precios de cierre.

---

## 2. calcula_retornos()

Calcula los retornos porcentuales diarios utilizando:

```python
df.pct_change().dropna()
```

---

## 3. resumen_estadistico_retornos()

Calcula las siguientes medidas estadísticas:

- Media
- Volatilidad
- Asimetría
- Kurtosis
- Máximo
- Mínimo

---

## 4. plot_retornos()

Genera gráficos de:
- Series de tiempo
- Histogramas
- Boxplot

mediante subplots.

---

# Activos analizados

```python
tickers = ['AAPL', 'JPM', 'TSLA']
periodo = ('2021-01-01', '2024-01-01')
```

---

# Ejecución del proyecto

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar programa

```bash
python main.py
```

---

# Resultados del análisis

## ¿Cuál es el activo con mayor riesgo según volatilidad?

El activo con mayor riesgo es TSLA, ya que presenta la mayor volatilidad entre los activos analizados.

---

## ¿Algún activo presenta distribución de retornos no simétrica o con colas pesadas?

Sí. TSLA presenta una distribución de retornos con alta kurtosis y asimetría, lo que indica presencia de colas pesadas y movimientos extremos.

---

## ¿Qué diferencias observas entre TSLA y JPM respecto a riesgo?

TSLA presenta un comportamiento considerablemente más volátil y riesgoso que JPM. En cambio, JPM presenta un comportamiento más estable y conservador.

---

# Conclusiones

El análisis permitió identificar diferencias importantes de riesgo entre los activos estudiados. TSLA presentó mayor volatilidad y movimientos extremos, mientras que JPM mostró un comportamiento más estable. El uso de Python facilita la automatización de análisis financieros y la visualización de datos.