## Listas 
edades = [10, 15, 20, 12, 18, 25, 8]

def contar_adultos(lista_edades):
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

print(contar_adultos(edades))

edades = [10, 15, 20, 12, 18, 25, 8]

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
print(f"Niños: {ninos}, Adolescentes: {adols}, Adultos: {aduls}")