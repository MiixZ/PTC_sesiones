"""Escribe una función vocales(palabra) que devuelva las vocales que aparecen en la palabra."""
def vocales(palabra):
    """Devuelve las vocales que aparecen en la palabra.
    palabra: str
    return: str"""
    vocales = ""
    for i in palabra:
        if i in "aeiouAEIOU":
            vocales += i
    return vocales

"""Segunda versión de la función utilizando .count"""
def vocales2(palabra):
    """Devuelve las vocales que aparecen en la palabra.
    palabra: str
    return: str"""
    vocales = ""
    for i in "aeiouAEIOU":
        if palabra.count(i) > 0:
            vocales += i
    return vocales

palabra1 = input("Introduzca una palabra: ")

print("La palabra", palabra1, "tiene las vocales", vocales(palabra1))
print("La palabra", palabra1, "tiene las vocales", vocales2(palabra1))
