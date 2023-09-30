# -*- coding: utf-8 -*-

""" CALCULAR EL TIEMPO CONVENCIONAL DADOS VALORES ARBITRARIOS"""

"""Realizar un programa que lea una cantidad de horas, minutos y segundos con valores arbitrarios,
y los transforme en una expresion de tiempo convencional en la que los minutos y segundos dentro
del rango [0,59]. Por ejemplo, dadas 10 horas, 119 minutos y 280 segundos, debera dar como
resultado 12 horas, 3 minutos y 40 segundos."""

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