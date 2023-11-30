"""
Escribe una función que haga lo mismo que el ejercicio 1 pero ahora con los caracteres que aparecen en una cadena de caracteres,
es decir, recibe como entrada la cadena de texto y nos da el diccionario con cada carácter y las veces que aparece.
"""

# -*- coding: utf-8 -*-

def frecuencia_letras(frase):
    frecuencias = {}
    for letra in frase:
        if letra.isalpha():
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    pares = list(frecuencias.items())
    pares.sort()
    return pares

frase = input("Introduce una frase: ")
resultado = frecuencia_letras(frase)

print("Frecuencia de las letras: ", resultado)