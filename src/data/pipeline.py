"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices
import luigi

from luigi import Task, LocalTarget

#Se genera tarea para correr las funciones realizadas anteriormente (ingesta, transformación y limpieza de datos).
#para luego guardar el archivo en la ruta especificada.

class IngestTransformClean(Task):
    def output(self):
        return LocalTarget("data_lake/cleansed/precios-horarios.csv")

    def run(self):
        ingest_data.ingest_data()
        transform_data.transform_data()
        clean_data.clean_data()

#Se genera tarea para correr las funciones realizadas para computar los precios pormedios diarios y mensuales,
#tomando el resultado de la tarea anterior, y especificando la ruta donde debe guardar los archivos resultado.

class Computes(Task):
    def requires(self):
        return IngestTransformClean()

    def output(self):
        return LocalTarget(
            [
                "data_lake/business/precios-diarios.csv",
                "data_lake/business/precios-mensuales.csv"
            ]
        )

    def run(self):
        compute_daily_prices.compute_daily_prices()
        compute_monthly_prices.compute_monthly_prices()


    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    luigi.run(["Computes", "--local-scheduler"])
