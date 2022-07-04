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

    #Generar todos los archivos csv
    ruta = glob.glob(r'data_lake/raw/*.csv')

    #Unir los archivos csv
    lista_data = []
    for file in ruta:
        df = pd.read_csv(file, index_col=None, header=0)
        lista_data.append(df)

    #Limpiar los campos nulos
    data_completo = pd.concat(lista_data, axis=0, ignore_index=True)
    data_completo = data_completo[data_completo["Fecha"].notnull()]

    #Transformar los datos
    archivo = pd.melt(data_completo, id_vars = ["Fecha"])
    archivo = archivo.rename(columns = {"Fecha": "fecha", "variable": "hora", "value": "precio"})
    archivo = archivo[archivo["precio"].notnull()]

    #Generar un nuevo archivo csv con todos los datos y guardar en la ruta especificada
    archivo.to_csv("data_lake/cleansed/precios-horarios.csv", index=None, header = True )

    #raise NotImplementedError("Implementar esta función")

    #Generar test de creación de columnas

def test_columns():

    read_file = pd.read_csv(
                'data_lake/cleansed/precios-horarios.csv')
    assert ["fecha","hora","precio"] == list(read_file.columns.values)


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()

    clean_data()
