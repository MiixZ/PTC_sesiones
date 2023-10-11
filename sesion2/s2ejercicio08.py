# -*- coding: utf-8 -*-

"""Realizar un programa que pida un valor X de porcentaje de alcohol de una marca de cerveza y
que según dicho porcentaje calcule cuantos tercios de esa marca de cerveza (333cc) puedo tomar si
no quiero ingerir más de 50 cc de alcohol. Dar el resultado en valor entero."""

"""Constante con el máximo de alcohol que puedo tomar"""
MAX_ALCOHOL = 50

porcentaje_alcohol = float(input("Introduzca el porcentaje de alcohol de la cerveza:"))

"""Calculo la cantidad de alcohol en un tercio de cerveza"""
cantidad_alcohol = 333 * porcentaje_alcohol / 100

"""Calculo el número de tercios que puedo tomar"""
tercios = MAX_ALCOHOL / cantidad_alcohol

if tercios > 0:
    print("Puedes tomar ", int(tercios), " tercios de cerveza.")
else:
    print("No puedes tomar cerveza.")