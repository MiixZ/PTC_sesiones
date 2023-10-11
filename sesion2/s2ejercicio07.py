# -*- coding: utf-8 -*-

"""Realizar un programa que pida el nombre de una persona, primer apellido, segundo apellido y
que muestre por pantalla como sería el nombre completo en una sola línea. También mostrar el
nombre completo pero al revés. Finalmente volver a descomponer el nombre completo en sus tres
componentes y mostrarlos por pantalla."""

nombre = input("Introduzca el nombre:")

apellido1 = input("Introduzca el primer apellido:")

apellido2 = input("Introduzca el segundo apellido:")

"""Concateno el nombre y los apellidos para el nombre completo"""
nombre_completo = nombre + " " + apellido1 + " " + apellido2
print("El nombre completo es: ", nombre_completo)

"""Concateno el nombre y los apellidos para el nombre completo al revés"""
nombre_completo_reves = apellido2 + " " + apellido1 + " " + nombre
print("El nombre completo al revés es: ", nombre_completo_reves)

nombre_descompuesto = nombre_completo.split(" ")

print("El nombre es: ", nombre_descompuesto[0])
print("El primer apellido es: ", nombre_descompuesto[1])
print("El segundo apellido es: ", nombre_descompuesto[2])