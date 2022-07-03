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



if __name__ == "__main__":

    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
