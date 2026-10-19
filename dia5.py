### Diccionarios y listas
persona = {"nombre": "Luis", "edad": 30, "ciudad": "Bogotá"}

def presentar(dic):
    return f"Soy {dic['nombre']} de {dic['ciudad']} y tengo {dic['edad']} años"

print(presentar(persona))

nombres_personas = ["Luis", "Ana", "Carlos", "María", "Pedro"]
edades = [30, 17, 40, 35, 16]


def contar_grupos(lista_edades):
    niños = 0
    adolescentes = 0
    adultos = 0
    for edad in lista_edades:
        if edad < 13:
            niños += 1
        elif edad < 18:
            adolescentes += 1
        else:
            adultos += 1
    return niños, adolescentes, adultos

ninos, adols, aduls = contar_grupos(edades)
print(f"Nombre de personas:{nombres_personas}, Edades: {edades}")
print(f"Niños: {ninos}, Adolescentes: {adols}, Adultos: {aduls}")

personas = [
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Carlos", "edad": 40},
]

def contar_grupos(personas):
    niños = adolescentes = adultos = 0
    for p in personas:
        if p["edad"] < 13:
            niños += 1
        elif p["edad"] < 18:
            adolescentes += 1
        else:
            adultos += 1
    return niños, adolescentes, adultos

print(contar_grupos(personas))