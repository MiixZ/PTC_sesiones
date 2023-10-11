"""Escribe una función eliminar_letras(palabra, letra) que devuelva una versión de palabra que no contiene el carácter letra ninguna vez."""

def eliminar_letras(palabra, letra):
    """Elimina las letras de una palabra.
    palabra: str
    letra: str
    return: str"""
    nuevaPalabra = ""
    for i in palabra:
        if i != letra:
            nuevaPalabra += i
    return nuevaPalabra

"""Segunda versión de la función utilizando .replace"""
def eliminar_letras2(palabra, letra):
    """Elimina las letras de una palabra.
    palabra: str
    letra: str
    return: str"""
    return palabra.replace(letra, "")

palabra1 = input("Introduzca una palabra: ")
letra1 = input("Introduzca una letra: ")

print("La palabra", palabra1, "sin la letra", letra1, "es", eliminar_letras(palabra1, letra1))
print("La palabra", palabra1, "sin la letra", letra1, "es", eliminar_letras2(palabra1, letra1))