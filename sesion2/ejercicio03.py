# -*- coding: utf-8 -*-

""" CALCULAR EL TIEMPO CONVENCIONAL DADOS VALORES ARBITRARIOS"""

print("Introduzca las horas:")
horas = int(input())

print("Introduzca los minutos:")
minutos = int(input())

print("Introduzca los segundos:")
segundos = int(input())

"""Divmod devuelve una tupla con el cociente y el resto de la división."""

segs_convencional = divmod(segundos, 60)
minutos += segs_convencional[0]

mins_convencional = divmod(minutos, 60)
horas += mins_convencional[0]

tiempo_convencional = str(horas) + ":" + str(mins_convencional[1]) + ":" + str(segs_convencional[1])
print("El tiempo convencional es: ", tiempo_convencional)