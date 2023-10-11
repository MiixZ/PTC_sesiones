"""Escribe una función es_inversa(palabra1, palabra2) que determine si una palabra es la misma que la otra pero con los caracteres en orden inverso. Por ejemplo 'absd' y 'dsba'."""

def es_inversa(palabra1, palabra2):
    """Determina si una palabra es la misma que la otra pero con los caracteres en orden inverso.
    palabra1: str
    palabra2: str
    return: bool"""
    return palabra1 == palabra2[::-1]

palabra1 = input("Introduzca una palabra: ")
palabra2 = input("Introduzca otra palabra: ")

if es_inversa(palabra1, palabra2):
    print("Las palabras", palabra1, "y", palabra2, "son inversas.")
else:
    print("Las palabras", palabra1, "y", palabra2, "no son inversas.")
