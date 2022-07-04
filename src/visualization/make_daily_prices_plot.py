"""Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

"""
import pandas as pd
import matplotlib.pyplot as plt

def make_daily_prices_plot():

#Realizar lectura de datos y especificar los ejes del gráfico.

    data = r'data_lake/business/precios-diarios.csv'
    datos = pd.read_csv(data, index_col=None, sep=',', header=0)
    datos["fecha"] = pd.to_datetime(datos["fecha"])

    x=datos.fecha
    y=datos.precio

#Especificar características del gráfico.

    plt.figure(figsize=(15, 6))
    plt.plot(x, y, 'b', label='Promedio diario')
    plt.title('Promedio diario')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.xticks(rotation="vertical")
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    make_daily_prices_plot()
