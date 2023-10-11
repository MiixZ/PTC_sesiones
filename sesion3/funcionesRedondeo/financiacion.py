import decimal
from decimal import Decimal

def leerFloat2decimales():
    """Comprueba que los euros introducidos son correctos.
    euros: float
    return: bool"""
    dentro = True
    while dentro:
        float2decimal = input("Introduzca un número con dos decimales: ")
        datosfloat2decimal = float2decimal.split(".")

        if len(datosfloat2decimal) == 2:
            if datosfloat2decimal[0].isdigit() and datosfloat2decimal[1].isdigit() and len(
                    datosfloat2decimal[1]) <= 2:
                dentro = False
                return float2decimal
        elif len(datosfloat2decimal) == 1:
            if datosfloat2decimal[0].isdigit():
                dentro = False
                return float2decimal

"Vemos si el parámetro es un número entero sin decimales y positivo."
def leerInt():
    dentro = True
    while(dentro):
        numero = input("Introduzca un número entero: ")
        num = int(numero)
        if num > 0 and num == float(numero):
            dentro = False
            return num

def redondear(numero, decimales):
    """Redondea un número a un número de decimales.
    numero: float
    decimales: int
    return: float"""
    return round(numero, decimales)

def calcularCapitalAnual(capitalInicial, interes):
    """Calcula el capital anual de un capital inicial y un interés.
    capitalInicial: float en euros con dos decimales
    interes: float en tanto por cierto con dos decimales
    return: float"""
    return redondear(capitalInicial + capitalInicial * interes / 100, 2)

def redondearConDecimal(numero, decimales):
    return Decimal(numero).quantize(decimal.Decimal('0.' + '0' * decimales))

def calcularCapitalAnual2(capitalInicial, interes):
    """Calcula el capital anual de un capital inicial y un interés.
    capitalInicial: float en euros con dos decimales
    interes: float en tanto por cierto con dos decimales
    return: float"""
    return redondearConDecimal(Decimal(capitalInicial) + Decimal(capitalInicial) * Decimal(interes) / 100, 2)