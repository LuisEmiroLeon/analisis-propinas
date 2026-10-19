## Pandas - operaciones con dataframes
import pandas as pd

personas = [
    {"nombre": "Luis", "edad": 30, "ciudad": "Bogotá"},
    {"nombre": "Ana", "edad": 17, "ciudad": "Medellín"},
    {"nombre": "Carlos", "edad": 40, "ciudad": "Bogotá"},
    {"nombre": "Sofia", "edad": 15, "ciudad": "Cali"},
]

df = pd.DataFrame(personas)

adultos = df[df['edad'] >= 18].shape[0]
ciudad_origen = df[df['ciudad'] == 'Bogotá'].shape[0]
print(df)
print(f"Adultos: {adultos}")
print(f"Personas de Bogotá: {ciudad_origen}")