### Condicionales y ciclos, bucles
contador_adultos = 0
for i in range(5):
    edad = int(input(f"Edad {i+1}: "))
    if edad >= 18:
        contador_adultos += 1

print(f"Pueden entrar {contador_adultos} personas")

niños = 0
adolescentes = 0
adultos = 0

for i in range(5):
    edad = int(input(f"Edad {i+1}: "))
    if edad < 13:
        niños += 1
    elif edad < 18:
        adolescentes += 1
    else:
        adultos += 1

print(f"Niños: {niños}, Adolescentes: {adolescentes}, Adultos: {adultos}")