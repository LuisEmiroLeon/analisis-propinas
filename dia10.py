# Limpieza de datos - nulos, duplicados
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df.info()) # Imprime información sobre el DataFrame
print(df.describe()) # Imprime estadísticas descriptivas del DataFrame
print(df.isnull().sum()) # Imprime el número de valores nulos en cada columna
print(df[df.duplicated()]) # Imprime las filas duplicadas en el DataFrame
print(df[df['total_bill'] > 30]) # Imprime las filas donde 'total_bill' es mayor a 30
