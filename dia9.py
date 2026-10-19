# CSV reales
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df.head()) # Imprime las primeras filas del DataFrame
print(df.info()) # Imprime información sobre el DataFrame
print(df.head(10)) # Imprime las primeras 10 filas del DataFrame
print(df['total_bill'].mean()) # Imprime el promedio de la columna 'total_bill'
print(df['total_bill'].std()) # Imprime la desviación estándar de la columna 'total_bill'
print(df.info()) # Imprime información sobre el DataFrame
print(df.describe()) # Imprime estadísticas descriptivas del DataFrame
