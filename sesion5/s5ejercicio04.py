"""
Escribir un programa para crear una agenda telefónica usando un diccionario.
La agenda debe usar como clave el nombre+apellidos de la persona y como dato su telefono.
Pedir los datos por teclado, si el nombre y apellidos ya existe debe avisar y
dar opción a modificarlo o eliminarlo. Si el nombre + apellidos no está en la agenda
debe incluirlo pidiendo el teléfono. Para terminar especificar una secuencia de salida tipo “Salir=$$”.
"""

# -*- coding: utf-8 -*-

agenda = {}

while True:
    nombre_apellidos = input("Introduce el nombre y apellidos: ")
    if nombre_apellidos == "Salir=$$":
        break
    if nombre_apellidos in agenda:
        print("El nombre y apellidos ya existen en la agenda.")
        opcion = input("¿Quieres modificarlo (M) o eliminarlo (E)? ")
        if opcion.upper() == "M":
            nuevo_nombre = input("Introduce el nuevo nombre y apellidos: ")
            agenda[nuevo_nombre] = agenda.pop(nombre_apellidos)
        elif opcion.upper() == "E":
            agenda.pop(nombre_apellidos)
    else:
        telefono = input("Introduce el número de teléfono: ")
        agenda[nombre_apellidos] = telefono

print("Agenda: ", agenda)