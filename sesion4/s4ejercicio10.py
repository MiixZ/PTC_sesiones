"""
Leer una frase de teclado e implementar una función que devuelva una lista de pares en la que
debe aparecer cada letra junto a su frecuencia de aparición. Los espacios no se deben tener en
cuenta. Dicha lista debe estar ordenada atendiendo al orden ascendente de las letras. Ejemplo: ante
la entrada “programa” debe dar como salida [('a', 2), ('g', 1), ('m',1), ('o', 1), ('p',1), ('r',2)].
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