# -*- coding: utf-8 -*-

"""DESVIACIÓN TÍPICA"""

import math

print("Introduzca el primer número:")
numero1 = float(input())

print("Introduzca el segundo número:")
numero2 = float(input())

print("Introduzca el tercer número:")
numero3 = float(input())

media = (numero1 + numero2 + numero3) / 3

desviacion_tipica = math.sqrt(((numero1 - media) ** 2 + (numero2 - media) ** 2 + (numero3 - media) ** 2) / 3)

print("La desviación típica es: ", desviacion_tipica)