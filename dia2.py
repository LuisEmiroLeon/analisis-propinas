## Condicionales
edad = int(input("Tu edad: "))
if edad >= 18:
    print("Puedes entrar a ver una película de 18+")
else:
    print("No puedes entrar a ver una película de 18+")

# Condicionales con elif, varias condiciones
edad = int(input("Tu edad: "))
if edad < 13:
    print("Puedes entrar a ver una película de infantil")

elif edad < 18:
    print("Puedes ver PG-13 con adulto")

else:
    print("puedes entrar a ver una película de 18+")