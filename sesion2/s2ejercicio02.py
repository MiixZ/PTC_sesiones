# -*- coding: utf-8 -*-

"""DESVIACIÓN TÍPICA"""

"""Dados tres números x1, x2, x3, calcular la desviación típica respecto a su media aritmética."""

import math

"Pedimos los números"
numero1 = float(input("Introduzca el primer número:"))

numero2 = float(input("Introduzca el segundo número:"))

numero3 = float(input("Introduzca el tercer número:"))

"Cálculo de la desviación típica"
media = (numero1 + numero2 + numero3) / 3
desviacion_tipica = math.sqrt(((numero1 - media) ** 2 + (numero2 - media) ** 2 + (numero3 - media) ** 2) / 3)

print(f"La desviación típica es: {desviacion_tipica:.2f}")