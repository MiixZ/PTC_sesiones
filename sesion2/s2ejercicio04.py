# -*- coding: utf-8 -*-

"""PROGRAMA CAJA DE SUPERMERCADO"""

"""Realizar un programa para una caja de un supermercado que lea un precio desde el teclado y una
cantidad entregada por el cliente (se supone que cantidad >= precio) y obtenga en la pantalla el
numero mnimo de monedas de 1 euro, 50 centimos, 10 centimos y 1 centimo que se deben dar de
cambio. Por ejemplo, si precio es 1.12 euros y cantidad es 5 euros, debe dar como resultado 3
monedas de 1 euro, 1 moneda de 50 centimos, 3 monedas de 10 centimos y 8 monedas de 1
centimo."""

def calcularMonedasMinimas(cambio, valor_monedas):
    monedas = divmod(cambio, valor_monedas)[0]
    cambio_restante = divmod(cambio, valor_monedas)[1]
    return monedas, cambio_restante


"""Pedimos los datos de entrada"""
precio_compra = float(input("Precio compra: "))
dinero_entregado = float(input("Dinero entregado por el cliente: "))

"Calculamos cuánto debemos devolver."
cambio = dinero_entregado*100 - precio_compra*100

"Calculamos las monedas individualmente."
monedas1euro = calcularMonedasMinimas(cambio, 100)
cambio = monedas1euro[1]

monedas50cent = calcularMonedasMinimas(cambio, 50)
cambio = monedas50cent[1]

monedas10cent = calcularMonedasMinimas(cambio, 10)
cambio = monedas10cent[1]

monedas1cent = calcularMonedasMinimas(cambio, 1)

print("Monedas de 1 euro: ", int(monedas1euro[0]))
print("Monedas de 50 cent: ", int(monedas50cent[0]))
print("Monedas de 10 cent: ", int(monedas10cent[0]))
print("Monedas de 1 cent: ", int(monedas1cent[0]))