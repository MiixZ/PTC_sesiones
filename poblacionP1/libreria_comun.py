# Funciones globales para R1, R2, R3, R4 y R5.

import csv

def round2(numero):
    """
    Redondea un número a dos decimales.
    :param numero:
    :return:
    """
    return round(numero, 2)


def limpiar_csv(fichero, fichero_nuevo, cabecera):
    """
    Limpia un fichero CSV de datos no útiles.
    :param fichero: Fichero CSV a limpiar.
    :return: None
    """
    fichero_inicial = open(fichero, 'r', encoding='utf-8')
    cadena_pob = fichero_inicial.read()
    fichero_inicial.close()

    primero = cadena_pob.find("Total")
    ultimo = cadena_pob.find("Notas")

    cadena_final = cadena_pob[primero:ultimo]

    # Creamos el fichero final.
    fichero_final = open(fichero_nuevo, "w", encoding="utf-8")
    fichero_final.write(cabecera + '\n' + cadena_final)
    fichero_final.close()


def leer_fichero(fichero):
    """
    Lee un fichero CSV.
    :param fichero: Fichero CSV a leer.
    :return: Lista con los valores del fichero.
    """
    with open(fichero, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for reg in reader:
            print(reg)


cabecera = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010"
cadena_deseada = limpiar_csv('entradas/poblacionProvinciasHM2010-17.csv',
                            "salidas/poblacionProvinciasHM2010-17.csv",
                            cabecera)
leer_fichero('salidas/poblacionProvinciasHM2010-17.csv')