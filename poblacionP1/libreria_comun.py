# Funciones globales para R1, R2, R3, R4 y R5.

import csv

CABECERA_HTML = """
<!DOCTYPE html><html><head><title>Ejemplo tabla</title>
<link rel="stylesheet" href="estilo.css"> <meta charset="utf8"></head>
<body>
"""

PIE_HTML = """
</body>
</html>
"""


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
    :param cabecera: Cabecera del fichero CSV.
    :param fichero_nuevo: Fichero CSV nuevo.
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
