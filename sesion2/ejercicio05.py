# -*- coding: utf-8 -*-

"""Hacer un programa para calcular la diferencia en horas:minutos:segundos entre dos instantes de
tiempo dados en horas:minutos:segundos."""

print("Introduzca la primera hora con el siguiente formato (hh:mm:ss):")
hora1 = input()
hora_minuto_segundo1 = hora1.split(":")

print("Introduzca la segunda hora con el siguiente formato (hh:mm:ss):")
hora2 = input()
hora_minuto_segundo2 = hora2.split(":")

dif_horas = int(hora_minuto_segundo2[0]) - int(hora_minuto_segundo1[0])
dif_minutos = int(hora_minuto_segundo2[1]) - int(hora_minuto_segundo1[1])
dif_segundos = int(hora_minuto_segundo2[2]) - int(hora_minuto_segundo1[2])

print("La diferencia entre las dos horas es: ", abs(dif_horas), ":", abs(dif_minutos), ":", abs(dif_segundos))