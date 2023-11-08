"""
Usando el módulo “random” genera dos listas de N y M números enteros aleatorios entre 1 y 10 e
implementa una función que devuelva una tercera lista que represente la intersección de las dos
primeras. Los valores deben estar ordenados en orden ascendente. Solicitar N y M por teclado y
mostrar el resultado por pantalla.
"""

import random


def interseccion(lista1, lista2):
    """Devuelve una lista con los elementos comunes de dos listas.
    lista1: list
    lista2: list
    return: list"""
    lista3 = []
    for i in lista1:
        if i in lista2 and i not in lista3:
            lista3.append(i)
    return lista3


N = int(input("Introduzca el número de elementos de la primera lista: "))
M = int(input("Introduzca el número de elementos de la segunda lista: "))

lista1 = []
lista2 = []

for i in range(N):
    lista1.append(random.randint(1, 10))
for i in range(M):
    lista2.append(random.randint(1, 10))

print("La primera lista es:", lista1)
print("La segunda lista es:", lista2)

print("La intersección de las dos listas es:", interseccion(lista1, lista2))

# Otra forma de hacerlo:
def interseccion2(lista1, lista2):
     """Devuelve una lista con los elementos comunes de dos listas.
     lista1: list
     lista2: list
     return: list"""
     lista3 = []
     for i in lista1:
        if i in lista2:
            lista3.append(i)
        return sorted(set(lista3))


N = int(input("Introduzca el número de elementos de la primera lista: "))
M = int(input("Introduzca el número de elementos de la segunda lista: "))

lista1 = []
lista2 = []

for i in range(N):
    lista1.append(random.randint(1, 10))
for i in range(M):
    lista2.append(random.randint(1, 10))

print("La primera lista es:", lista1)
print("La segunda lista es:", lista2)

print("La intersección de las dos listas es:", interseccion(lista1, lista2))
