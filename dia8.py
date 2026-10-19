# Numpy y Pandas - operaciones con arrays y dataframes
import numpy as np
import pandas as pd

edades = np.array([30, 25, 35]) 
df = pd.DataFrame({'edades': edades})
print(edades * 2) # Imprime los valores de 'edades' multiplicados por 2
print(edades.mean()) # Imprime el promedio de los valores de 'edades'
print(edades + 10) # Imprime los valores de 'edades' sumados por 10
