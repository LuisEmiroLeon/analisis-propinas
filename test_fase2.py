
import pandas as pd

datos = {"nombre": ["Luis", "Ana", "Carlos"], "edad": [30, 17, 40]}
df = pd.DataFrame(datos)
print(df)
print(f"\nPromedio edad: {df['edad'].mean()}")
