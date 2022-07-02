"""Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


"""

import pandas as pd
import glob

def clean_data():

    ruta = glob.glob(r'data_lake/raw/*.csv')

    lista_data = []
    for file in ruta:
        df = pd.read_csv(file, index_col=None, header=0)
        lista_data.append(df)

    data_completo = pd.concat(lista_data, axis=0, ignore_index=True)
    data_completo = data_completo[data_completo["Fecha"].notnull()]

    archivo = pd.melt(data_completo, id_vars = ["Fecha"])
    archivo = archivo.rename(columns = {"Fecha": "fecha", "variable": "hora", "value": "precio"})
    archivo = archivo[archivo["precio"].notnull()]

    archivo.to_csv("data_lake/cleansed/precios-horarios.csv", index=None, header = True )

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
