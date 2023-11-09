"""
Crea una lista con los valores enteros de 1 a N e implementa una función que reciba dicha lista y
nos devuelva la suma de dichos valores. Solicitar N por teclado y mostrar el resultado por pantalla.
"""


def suma_lista(lista_a_sumar):
    """Suma los valores de una lista.
    lista: list
    return: int"""
    suma = 0
    for i in lista_a_sumar:
        suma += i
    return suma


N = int(input("Introduzca un número: "))
lista = list(range(1, N + 1))

print("La suma de los valores de la lista", lista, "es", suma_lista(lista))


# Segunda versión usando sum()
def suma_lista2(lista_a_sumar):
    """Suma los valores de una lista.
    lista: list
    return: int"""
    return sum(lista_a_sumar)


N = int(input("Introduzca un número: "))
lista = list(range(1, N + 1))

print("La suma de los valores de la lista", lista, "es", suma_lista2(lista))