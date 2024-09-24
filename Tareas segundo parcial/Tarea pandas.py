# Ejercicio 1. Mediante teclado especificar los siguiente:
# - Numero de columnas que tendrá el dataframe
# - Una vez que se especifique, preguntar por los datos que tendra esa Serie
# - Preguntar por los nombres de las columnas que tendrá el dataframe
# - Preguntar por los nombres de las filas que tendrá el dataframe
# - Una vez introducidos los datos, crear el dataframe que contenga esa información
# - Mostrar el dataframe
import pandas as pd

num_columnas = 3
columnas = [
    [5,6,7,8],
    [1,2,3,4],
    [10,20,30,40]
]

nombres_col = ["columna 1","columna 2","columna 3","columna 4"]
filas = ["a","b","c"]

df = pd.DataFrame(columnas,index=filas, columns=nombres_col)
print(df)
