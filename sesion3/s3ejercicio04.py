"""Escribe una función buscar(palabra, sub) que devuelva la posición en la que se puede encontrar sub dentro de palabra o -1 en caso de que no esté."""

def buscar(palabra, sub):
    """Devuelve la posición en la que se puede encontrar sub dentro de palabra o -1 en caso de que no esté.
    palabra: str
    sub: str
    return: int"""
    posicion = -1
    for i in range(len(palabra)):
        if palabra[i:i+len(sub)] == sub:
            posicion = i
    return posicion

"""Segunda versión de la función utilizando .find"""
def buscar2(palabra, sub):
    """Devuelve la posición en la que se puede encontrar sub dentro de palabra o -1 en caso de que no esté.
    palabra: str
    sub: str
    return: int"""
    return palabra.find(sub)

palabra1 = input("Introduzca una palabra: ")
sub1 = input("Introduzca una subcadena: ")

print("La subcadena", sub1, "se encuentra en la posición", buscar(palabra1, sub1), "de la palabra", palabra1)
print("La subcadena", sub1, "se encuentra en la posición", buscar2(palabra1, sub1), "de la palabra", palabra1)
