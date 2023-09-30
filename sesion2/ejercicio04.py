# -*- coding: utf-8 -*-

"""PROGRAMA CAJA DE SUPERMERCADO"""


def calcularMonedasMinimas(cambio, valor_monedas):
    monedas = divmod(cambio, valor_monedas)[0]
    cambio_restante = divmod(cambio, valor_monedas)[1]
    return monedas, cambio_restante


print("Precio compra:")
precio_compra = float(input())

print("Dinero entregado por el cliente:")
dinero_entregado = float(input())

cambio = dinero_entregado - precio_compra

monedas1euro = calcularMonedasMinimas(cambio, 1)
cambio = monedas1euro[1]

monedas50cent = calcularMonedasMinimas(cambio, 0.5)
cambio = monedas50cent[1]

monedas10cent = calcularMonedasMinimas(cambio, 0.1)
cambio = monedas10cent[1]

monedas1cent = calcularMonedasMinimas(cambio, 0.01)

print("Monedas de 1 euro: ", int(monedas1euro[0]))
print("Monedas de 50 cent: ", int(monedas50cent[0]))
print("Monedas de 10 cent: ", int(monedas10cent[0]))
print("Monedas de 1 cent: ", int(monedas1cent[0])+1)