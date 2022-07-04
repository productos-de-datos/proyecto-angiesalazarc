"""Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl

"""

def train_daily_model():

    import pandas as pd
    import pickle
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import RandomForestRegressor

#Realizar lectura de datos

    df = pd.read_csv("data_lake/business/features/precios-diarios.csv", encoding = 'utf-8', sep=',')

#Generar variables de estudio para el modelo

    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y%m%d')
    X_fecha = np.array(df['fecha']).reshape(-1,1)
    y_precio = np.array(df['precio']).reshape(-1,1)

#Dividir los datos de entrenamiento y prueba, con un tamaño de muestra de entrenamiento del 80%.
    (X_train, X_test, y_train, y_test,) = train_test_split(X_fecha, y_precio, test_size=0.2, random_state=123456,)

#Crear una instancia del modelo de regresión lineal
    inst_model = RandomForestRegressor(n_estimators=100, max_features='sqrt', n_jobs=-1, oob_score = True, random_state = 123456)

#Entrenar el clasificador
    inst_model.fit(X_train,y_train)

#Guardar el modelo entrenado generado en la ruta especificada
    pickle.dump(inst_model, open('src/models/precios-diarios.pickle', 'wb'))


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    train_daily_model()


