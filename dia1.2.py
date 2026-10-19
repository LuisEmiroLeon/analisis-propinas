nombre = "Luis"
edad = 30 
print(f"Hola, soy {nombre} y tengo {edad} años")
def saludar(nombre_persona, edad_persona):
    return f"¡Hola, {nombre_persona}! Veo que tienes {edad_persona} años."
mensaje = saludar(nombre, edad)
print(mensaje)
print(saludar("Ana", 25))
