# -*- coding: utf-8 -*-

"""Pedir tres valores reales x1,x2,x3, obtener su máximo y su mínimo y mostrarlos por pantalla. (No
usar la funcion max y min de python)."""

numero1 = float(input("Introduzca el primer número:"))

numero2 = float(input("Introduzca el segundo número:"))

numero3 = float(input("Introduzca el tercer número:"))

"""Calculo el máximo y el mínimo de los tres números"""
if numero1 > numero2:
    if numero1 > numero3:
        maximo = numero1
    else:
        maximo = numero3
else:
    if numero2 > numero3:
        maximo = numero2
    else:
        maximo = numero3

if numero1 < numero2:
    if numero1 < numero3:
        minimo = numero1
    else:
        minimo = numero3
else:
    if numero2 < numero3:
        minimo = numero2
    else:
        minimo = numero3

print("El máximo es: ", maximo)
print("El mínimo es: ", minimo)