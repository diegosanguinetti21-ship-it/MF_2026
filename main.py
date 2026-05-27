# ==========================================
# LIBRERIAS
# ==========================================

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# FUNCION DESCARGA DE DATOS
# ==========================================

def descargar_datos_yf(tickers, start, end):

    datos = yf.download(
        tickers,
        start=start,
        end=end
    )["Close"]

    return datos

# ==========================================
# FUNCION CALCULO DE RETORNOS
# ==========================================

def calcula_retornos(df):

    retornos = df.pct_change().dropna()

    return retornos

# ==========================================
# FUNCION RESUMEN ESTADISTICO
# ==========================================

def resumen_estadistico_retornos(df):

    resumen = pd.DataFrame({
        "Media": df.mean(),
        "Volatilidad": df.std(),
        "Asimetria": df.skew(),
        "Kurtosis": df.kurt(),
        "Maximo": df.max(),
        "Minimo": df.min()
    })

    return resumen

# ==========================================
# FUNCION GRAFICOS
# ==========================================

def plot_retornos(df):

    fig, axes = plt.subplots(3, 1, figsize=(12, 14))

    # Serie de tiempo
    df.plot(ax=axes[0])
    axes[0].set_title("Series de Tiempo de Retornos")

    # Histograma
    df.hist(ax=axes[1])
    axes[1].set_title("Histogramas de Retornos")

    # Boxplot
    df.boxplot(ax=axes[2])
    axes[2].set_title("Boxplot de Retornos")

    plt.tight_layout()
    plt.show()

# ==========================================
# PIPELINE
# ==========================================

tickers = ['AAPL', 'JPM', 'TSLA']
periodo = ('2021-01-01', '2024-01-01')

# Descargar datos
precios = descargar_datos_yf(
    tickers,
    periodo[0],
    periodo[1]
)

# Calcular retornos
retornos = calcula_retornos(precios)

# Resumen estadistico
resumen = resumen_estadistico_retornos(retornos)

print("\nRESUMEN ESTADISTICO")
print(resumen)

# Graficos
plot_retornos(retornos)
