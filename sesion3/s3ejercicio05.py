"""Escribe una función num_vocales(palabra) que devuelva el número de vocales que aparece en la palabra."""

def num_vocales(palabra):
    """Cuenta el número de vocales que aparece en la palabra.
    palabra: str
    return: int"""
    contador = 0
    for i in palabra:
        if i in "aeiouAEIOU":
            contador += 1
    return contador

"""Segunda versión de la función utilizando .count"""
def num_vocales2(palabra):
    """Cuenta el número de vocales que aparece en la palabra.
    palabra: str
    return: int"""
    return (palabra.count("a") + palabra.count("e") + palabra.count("i") + palabra.count("o") + palabra.count("u")
            + palabra.count("A") + palabra.count("E") + palabra.count("I") + palabra.count("O") + palabra.count("U"))

palabra1 = input("Introduzca una palabra: ")

print("La palabra", palabra1, "tiene", num_vocales(palabra1), "vocales")
print("La palabra", palabra1, "tiene", num_vocales2(palabra1), "vocales")
