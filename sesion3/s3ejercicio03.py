"""Escribe una función mayusculas_minusculas(palabra) que devuelva una cadena en la que las mayúsculas y las minúsculas estén al contrario."""

"""Función sin usar métodos de cadenas ni .lower, .upper, etc. Ord convierte el caracter que representa a un entero.
Chr convierte el entero en el carácter que representa."""
def mayusculas_minusculas(palabra):
    """Devuelve una cadena en la que las mayúsculas y las minúsculas estén al contrario.
    palabra: str
    return: str"""
    nuevaPalabra = ""
    for i in palabra:
        if 'A' < i < 'Z':
            nuevaPalabra += chr(ord(i)-ord('A')+ord('a'))
        else:
            nuevaPalabra += chr(ord(i)-ord('a')+ord('A'))
    return nuevaPalabra

"""Segunda versión de la función utilizando .swapcase"""
def mayusculas_minusculas2(palabra):
    """Devuelve una cadena en la que las mayúsculas y las minúsculas estén al contrario.
    palabra: str
    return: str"""
    return palabra.swapcase()

palabra1 = input("Introduzca una palabra: ")

print("La palabra", palabra1, "con las mayúsculas y las minúsculas al contrario es", mayusculas_minusculas(palabra1))
print("La palabra", palabra1, "con las mayúsculas y las minúsculas al contrario es", mayusculas_minusculas2(palabra1))
