cadena = input("Introduzca una cadena:")

# Elimina las A mayúsculas de la cadena
i = 0
for letra in cadena:
    if letra == "A":
        cadena = cadena[:i] + cadena[i + 1:]
    else:
        i += 1

print("La cadena sin las A en mayúscula es: ", cadena)
