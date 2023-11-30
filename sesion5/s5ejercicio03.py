"""
Escribe una función que genere 100 números aleatorios entre 1 y 50 y devuelva un diccionario con los valores generados y su frecuencia.
Crear una segunda función para calcular la media aritmética considerando el diccionario como una distribución de frecuencias de cada valor.
"""

# -*- coding: utf-8 -*-

import random

def generar_numeros():
    numeros = [random.randint(1, 50) for _ in range(100)]
    frecuencias = {}
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    return frecuencias

def calcular_media(frecuencias):
    total = sum(num * frec for num, frec in frecuencias.items())
    cantidad = sum(frecuencias.values())
    return total / cantidad

frecuencias = generar_numeros()
media = calcular_media(frecuencias)

print("Numeros: ", frecuencias.keys())

print("Frecuencias: ", frecuencias)
print("Media: ", media)