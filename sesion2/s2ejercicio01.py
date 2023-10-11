# -*- coding: utf-8 -*-

"""PRECIO VEHÍCULO"""

"""Calcular precio de un vehículo suponiendo que tenemos que pedir como datos de entrada los
siguientes: precio bruto del vehículo, porcentaje de ganancia del vendedor, IVA a aplicar. El precio
base se calcula incrementando el precio bruto con el porcentaje de ganancia. El precio final será el
precio base incrementado con el porcentaje de IVA."""

def pedirDato(mensaje):
    print(mensaje)
    dato = float(input())
    return dato


precio_bruto = pedirDato("Introduzca el precio bruto del vehículo (sin IVA):")

porcentaje_ganancia = pedirDato("Introduzca el porcentaje de ganancia del vendedor:")

porcentaje_iva = pedirDato("Introduzca el porcentaje de IVA:")

precio_base = precio_bruto + precio_bruto * porcentaje_ganancia / 100

precio_final = precio_base + precio_base * porcentaje_iva / 100

print("El precio final del vehículo es: ", precio_final)