"""
Usando el módulo “random” genera dos listas de N y M números enteros aleatorios entre 1 y 10 e
implementa una función que devuelva una tercera lista con los valores de la primera que NO estén
en la segunda. Los valores deben estar ordenados en orden ascendente. Solicitar N y M por teclado
y mostrar el resultado por pantalla.
"""

# -*- coding: utf-8 -*-

import random

def valores_no_comunes(lista1, lista2):
    return sorted(set([valor for valor in lista1 if valor not in lista2]))

N = int(input("Introduce el valor de N: "))
M = int(input("Introduce el valor de M: "))

lista1 = [random.randint(1, 10) for _ in range(N)]          # _ es una variable que no se va a usar
lista2 = [random.randint(1, 10) for _ in range(M)]

print("La primera lista es:", lista1)
print("La segunda lista es:", lista2)

resultado = valores_no_comunes(lista1, lista2)

print("Los valores de la primera lista que NO están en la segunda lista son: ", resultado)