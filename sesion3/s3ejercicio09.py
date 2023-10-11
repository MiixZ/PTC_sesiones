"""Escribe una función elimina_vocales(palabra) que elimine todas las vocales que aparecen en la palabra."""

def elimina_vocales(palabra):
    """Elimina las vocales que aparecen en la palabra.
    palabra: str
    return: str"""
    palabra_sin_vocales = ""
    for i in palabra:
        if i not in "aeiouAEIOU":
            palabra_sin_vocales += i
    return palabra_sin_vocales

"""Segunda versión de la función utilizando .replace"""
def elimina_vocales2(palabra):
    """Elimina las vocales que aparecen en la palabra.
    palabra: str
    return: str"""
    for i in "aeiouAEIOU":
        palabra = palabra.replace(i, "")
    return palabra

palabra1 = input("Introduzca una palabra: ")

print("La palabra", palabra1, "sin vocales es", elimina_vocales(palabra1))
print("La palabra", palabra1, "sin vocales es", elimina_vocales2(palabra1))
