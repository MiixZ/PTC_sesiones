# Funciones globales para R1, R2, R3, R4 y R5.

import csv


def round2(numero):
    """
    Redondea un número a dos decimales.
    :param numero:
    :return:
    """
    return round(numero, 2)


def leer_anios_csv(fichero):
    """
    Lee los años de un fichero CSV.
    :param fichero: Fichero CSV a leer.
    :return: Número de años.
    """
    with open(fichero, newline='') as f:
        reader = csv.reader(f)
        return len(next(reader)) - 1
