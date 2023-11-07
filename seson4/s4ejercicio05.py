"""
Partiendo de una lista que contiene a su vez N listas de M enteros, si la consideramos como una
matriz de dimensión NxM, implementar una función que nos devuelva la matriz traspuesta MxN
(intercambiando filas y columnas) que contedrá M listas de N enteros. Solicitar N y M por teclado y
mostrar el resultado por pantalla.
"""

import random


def matriz_traps(matriz_a_trasponer):
    """Devuelve la matriz traspuesta de una matriz.
    matriz: list
    return: list"""
    matriz_resultado = []
    for fila in range(len(matriz_a_trasponer[0])):
        matriz_resultado.append([])
        for columna in range(len(matriz_a_trasponer)):
            matriz_resultado[fila].append(matriz_a_trasponer[columna][fila])
    return matriz_resultado


def imprimir_matriz(matriz_a_imprimir):
    """Imprime una matriz.
    matriz: list"""
    for fila in matriz_a_imprimir:
        print(fila)


N = int(input("Introduzca el número de filas: "))
M = int(input("Introduzca el número de columnas: "))

matriz = []
for i in range(N):
    matriz.append([])
    for j in range(M):
        matriz[i].append(random.randint(1, 10))

print("La matriz traspuesta de la matriz")
imprimir_matriz(matriz)
print("es")
imprimir_matriz(matriz_traps(matriz))
