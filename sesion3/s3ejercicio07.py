"""Escribe una función mayusculas(palabra) que devuelva la palabra pasada a mayúsculas."""
"""NO PUEDE UTILIZARSE .upper() ni similares."""
def mayusculas(palabra):
    palabra_mayusculas = ""
    for letra in palabra:
        if letra >= "a" and letra <= "z":
            palabra_mayusculas += chr(ord(letra) - 32)
        else:
            palabra_mayusculas += letra
    return palabra_mayusculas

"""Segunda versión de la función utilizando .upper()"""
def mayusculas2(palabra):
    palabra_mayusculas = ""
    for letra in palabra:
        if letra.islower():
            palabra_mayusculas += letra.upper()
        else:
            palabra_mayusculas += letra
    return palabra_mayusculas

palabra1 = input("Introduzca una palabra: ")
print(mayusculas(palabra1))
print(mayusculas2(palabra1))