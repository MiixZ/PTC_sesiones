"""Escribe una función contar_letras(palabra, letra) que devuelva el número de veces que aparece una letra en una palabra."""

def contar_letras(palabra, letra):
    """Cuenta el número de veces que aparece una letra en una palabra.
    palabra: str
    letra: str
    return: int"""
    contador = 0
    for i in palabra:
        if i == letra:
            contador += 1
    return contador

"""Segunda versión de la función utilizando .count"""
def contar_letras2(palabra, letra):
    """Cuenta el número de veces que aparece una letra en una palabra.
    palabra: str
    letra: str
    return: int"""
    return palabra.count(letra)

palabra1 = input("Introduzca una palabra: ")
letra1 = input("Introduzca una letra: ")

print("La letra", letra1, "aparece", contar_letras(palabra1, letra1), "veces en la palabra", palabra1)
print("La letra", letra1, "aparece", contar_letras2(palabra1, letra1), "veces en la palabra", palabra1)