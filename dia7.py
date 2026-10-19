## Pandas estadisticas y visualización de datos
import pandas as pd

personas = [
    {"nombre": "Luis", "edad": 30, "ciudad": "Bogota"},
    {"nombre": "Ana", "edad": 25, "ciudad": "Medellin"},
    {"nombre": "Carlos", "edad": 35, "ciudad": "Bogota"}
]

df = pd.DataFrame(personas)

print(df['edad'].mean())
print(df['edad'].max())
print(df.groupby('ciudad').size())

import matplotlib.pyplot as plt
df.groupby('ciudad').size().plot(kind='bar') # Crea un gráfico de barras con la cantidad de personas por ciudad
plt.title('Personas por Ciudad') # Agrega un título al gráfico
plt.xlabel('Ciudad') # Agrega una etiqueta al eje x
plt.ylabel('Cantidad') # Agrega una etiqueta al eje y
plt.show() # Muestra el gráfico


