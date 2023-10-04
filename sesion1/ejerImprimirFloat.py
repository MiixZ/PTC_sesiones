#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:35:25 2023

@author: aulas
"""
import math

print("Introduzca el radio de una circunferencia")

radio = float(input())

"Primera manera de imprimir el float"
print("La longitud es: ", 2*math.pi*radio, " y el área: ", math.pi*radio**2)

"Segunda manera de imprimir el float, añadimos las variables que queremos mostrar con 4 decimales."
print("La longitud es: %.4f y el área: %.4f" % (2*math.pi*radio, math.pi*radio**2))

"Tercera manera de imprimir el float con format (función de string), con dos decimales."
print("La longitud es: {0:.2f} y el área: {1:.2f}".format(2*math.pi*radio, math.pi*radio**2))

"Cuarta manera de imprimir el float, con tres decimales íntegramente en el string."
print(f"La longitud es: {2*math.pi*radio:.3f} y el área: {math.pi*radio**2:.3f}")