"""
Escribir una función que recibe una cadena de caracteres con al menos 10 palabras (que pueden repetirse)
y devuelva un diccionario en la que figuren cada palabra y la cantidad en que aparece en la cadena de entrada.
Por ejemplo si la entrada es: “me gusta programar pero me gusta más programar en python” debe devolver:
{'me': 2, 'gusta':2, 'programar':2, 'pero':1,..}
"""

# -*- coding: utf-8 -*-

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

cadena = input("Introduce una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de las palabras: ", resultado)