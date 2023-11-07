"""
Usando el módulo "random" genera dos listas de N y M números
enteros aleatoros entre 1 y 10 e implementa una función que
devuelva una tercera lista que contenga los números de las dos
primeras listas en orden ascendente sin contener valores repetidos.
Solicitar N y M por teclado y mostrar el resultado por pantalla.
"""

import random


def lista_aleatoria(longitud):
    """Devuelve una lista de longitud "longitud" con números aleatorios entre 1 y 10.
    longitud: int
    return: list"""
    lista = []
    for i in range(longitud):
        lista.append(random.randint(1, 10))
    return lista


def lista_sin_repetir(primera_lista, segunda_lista):
    """Devuelve una lista con los valores de dos listas ordenados de menor a mayor sin repetir.
    lista1: list
    lista2: list
    return: list"""
    lista = []
    for i in primera_lista:
        if i not in lista:
            lista.append(i)
    for i in segunda_lista:
        if i not in lista:
            lista.append(i)
    return lista


def minimo_en_lista(lista_a_comprobar):
    """Devuelve el mínimo de una lista.
    lista: list
    return: int"""
    minimo = lista_a_comprobar[0]
    for i in lista_a_comprobar:
        if i < minimo:
            minimo = i
    return minimo


def ordenar_lista(lista_a_ordenar):
    """Devuelve una lista ordenada de menor a mayor.
    lista: list
    return: list"""
    lista_ordenada = []

    while lista_a_ordenar:
        minimo = minimo_en_lista(lista_a_ordenar)
        lista_ordenada.append(minimo)
        lista_a_ordenar.remove(minimo)
    return lista_ordenada


N = int(input("Introduzca un número: "))
M = int(input("Introduzca otro número: "))
lista1 = lista_aleatoria(N)
lista2 = lista_aleatoria(M)
print("La lista 1 es", lista1)
print("La lista 2 es", lista2)

lista3 = lista_sin_repetir(lista1, lista2)
print("La lista 3 es", lista3)

lista3_ordenada = ordenar_lista(lista3)
print("La lista 3 ordenada es", lista3_ordenada)


# Segunda versión usando set()
def lista_sin_repetir2(primera_lista, segunda_lista):
    """Devuelve una lista con los valores de dos listas ordenados de menor a mayor sin repetir.
    lista1: list
    lista2: list
    return: list"""
    lista = list(set(primera_lista + segunda_lista))
    return lista


def ordenar_lista2(lista_a_ordenar):
    """Devuelve una lista ordenada de menor a mayor.
    lista: list
    return: list"""
    lista_ordenada = sorted(lista_a_ordenar)
    return lista_ordenada


N = int(input("Introduzca un número: "))
M = int(input("Introduzca otro número: "))
lista1 = lista_aleatoria(N)
lista2 = lista_aleatoria(M)
print("La lista 1 es", lista1)
print("La lista 2 es", lista2)

lista3 = lista_sin_repetir2(lista1, lista2)
print("La lista 3 es", lista3)

lista3_ordenada = ordenar_lista2(lista3)
print("La lista 3 ordenada es", lista3_ordenada)