# -*- coding: utf-8 -*-

"""Realizar un programa que pida un valor X de porcentaje de alcohol de una marca de cerveza y
que según dicho porcentaje calcule cuantos tercios de esa marca de cerveza (333cc) puedo tomar si
no quiero ingerir más de 50 cc de alcohol. Dar el resultado en valor entero."""

print("Introduzca el porcentaje de alcohol de la cerveza:")
porcentaje_alcohol = float(input())

cantidad_alcohol = 333 * porcentaje_alcohol / 100
tercios = 50 / cantidad_alcohol

if tercios > 0:
    print("Puedes tomar ", int(tercios), " tercios de cerveza.")
else:
    print("No puedes tomar cerveza.")