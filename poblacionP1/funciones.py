# Funciones globales para R1, R2, R3, R4 y R5.

import csv
from bs4 import BeautifulSoup

CABECERA_HTML = """
<!DOCTYPE html><html><head><title>Ejemplo tabla</title>
<link rel="stylesheet" href="estilo.css"> <meta charset="utf8"></head>
<body>
"""

PIE_HTML = """
</body>
</html>
"""


def limpiar_csv(fichero, fichero_nuevo, cabecera, primera_palabra, ultima_palabra):
    """
    Limpia un fichero CSV de datos no útiles.
    :param ultima_palabra:
    :param primera_palabra:
    :param cabecera: Cabecera del fichero CSV.
    :param fichero_nuevo: Fichero CSV nuevo.
    :param fichero: Fichero CSV a limpiar.
    :return: None
    """
    fichero_inicial = open(fichero, 'r', encoding='utf-8')
    cadena_pob = fichero_inicial.read()
    fichero_inicial.close()

    primero = cadena_pob.find(primera_palabra)
    ultimo = cadena_pob.find(ultima_palabra)

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


def leer_comunidades(fichero):
    """
    Lee un fichero HTML.
    :param fichero: Fichero HTML a leer.
    :return: Diccionario con código de comunidad autónoma y nombre de la comunidad autónoma.
    """
    comunidades = {}
    f = open(fichero, 'r', encoding='utf-8')
    soup = BeautifulSoup(f, 'html.parser')

    celdas = soup.find_all('td')

    for i in range(0, len(celdas), 2):
        comunidades[celdas[i].get_text()] = celdas[i + 1].get_text()

    return comunidades


def devolver_parte_provincia(provincias):
    provincias2 = {}

    for i in range(0, len(provincias), 4):
        CODAUTO = provincias[i].get_text()
        CCAA = provincias[i + 1].get_text()
        CPRO = provincias[i + 2].get_text()
        nombre_provincia = provincias[i + 3].get_text()

        # Creamos un diccionario anidado para cada provincia
        provincias2[CPRO] = {
            'CCAA': CCAA,
            'CODAUTO': CODAUTO,
            'PRO': nombre_provincia
        }

    return provincias2


def leer_provincias(fichero):
    """
    Lee un fichero HTML.
    :param fichero: Fichero HTML a leer.
    :return: Diccionario con código de provincia y nombre de la provincia.
    """

    f = open(fichero, 'r', encoding='utf-8')
    soup = BeautifulSoup(f, 'html.parser')
    cabecera = soup.find_all('th')
    celdas = soup.find_all('td')

    """
    Esta vez hay 4 celdas por provincia, con CODAUTO, CCAA, cod_provincia y provincia.
    Guardamos todos los datos en un diccionario.
    Como "Ciudades autónomas" es una celda, vamos a dividir en dos partes.
    """
    parte1_provincias = celdas[:-11]
    provincias = devolver_parte_provincia(parte1_provincias)

    parte2_provincias = celdas[-8:]
    provincias.update(devolver_parte_provincia(parte2_provincias))

    return provincias
