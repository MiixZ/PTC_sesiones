# -*- coding: utf-8 -*-

"""Realizar un programa que tomando como entrada la radiación solar media por día en Kwh/m2
calcule el número mínimo de paneles solares que se necesitan para producir, al menos, 1000 Kwh
en un mes (30 días) teniendo en cuenta que los paneles solares tienen un 17% de rendimiento y que
son de un tamaño de 1.6 m2."""

print("Introduzca la radiación solar media por día en Kwh/m2:")
radiacion_solar = float(input())

radiacion_solar_mes = radiacion_solar * 30
radiacion_solar_mes_rendimiento = radiacion_solar_mes * 0.17 / 1.6
paneles_solares = 1000 / radiacion_solar_mes_rendimiento

print("El número mínimo de paneles solares es: ", int(paneles_solares))