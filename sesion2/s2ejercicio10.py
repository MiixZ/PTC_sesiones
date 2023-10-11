# -*- coding: utf-8 -*-

"""Partiendo de una disolución de ácido sulfúrico en agua al 80 % de concentración, quiero obtener
una cantidad x de centímetros cúbicos a una concentración y% (y<80%). Siendo x, e y valores de
entrada al programa, calcular cuantos centímetros cúbicos de la disolución al 80% y de agua son
necesarios para obtener los x centímetros cúbicos deseados al y% de concentración."""

print("Introduzca la cantidad de centímetros cúbicos de disolución:")
centimetros_cubicos = float(input())

print("Introduzca la concentración de la disolución:")
concentracion = float(input())

centimetros_cubicos_agua = centimetros_cubicos * (80 - concentracion) / concentracion
centimetros_cubicos_disolucion = centimetros_cubicos - centimetros_cubicos_agua

print("Se necesitan ", int(centimetros_cubicos_disolucion), " centímetros cúbicos de disolución y ", int(centimetros_cubicos_agua), " centímetros cúbicos de agua.")