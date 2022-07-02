import pandas as pd

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    for fec in range(1995, 2022):

        if fec in range(2016, 2018):
            datos_csv = pd.read_excel('data_lake/landing/{}.xls'.format(fec), header=2)
            datos_csv = datos_csv.iloc[:, 0:25]
            datos_csv.columns = ['Fecha', 'H00', 'H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09', 'H10','H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23']
            datos_csv.to_csv ('data_lake/raw/{}.csv'.format(fec), index=None)

        else:
            datos_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(fec), header=2)
            datos_csv = datos_csv.iloc[:, 0:25]
            datos_csv.columns = ['Fecha', 'H00', 'H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09', 'H10','H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23']
            datos_csv.to_csv ('data_lake/raw/{}.csv'.format(fec), index=None)
    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
