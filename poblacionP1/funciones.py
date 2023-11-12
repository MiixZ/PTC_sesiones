# Funciones globales para R1, R2, R3, R4 y R5.

import csv
import locale

from bs4 import BeautifulSoup
import numpy as np

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
        comunidades[celdas[i].get_text().strip()] = celdas[i + 1].get_text().strip()

    return comunidades


def dict_fichero_csv(fichero):
    """
    Lee un fichero CSV.
    :param fichero: Fichero CSV a leer.
    :return: Diccionario con los datos del fichero CSV.
    """
    f = open(fichero, 'r', encoding='utf-8')
    dict_r = csv.DictReader(f, delimiter=';')
    return dict_r


def calcular_total_por_comunidad(dict_provincias, dict_datos, n_years, datos_utiles):
    """
    Dado el diccionario de comunidades, provincias y los datos, calcular el total de cada comunidad autónoma.
    :param n_years: Número de años (total + hombres + mujeres)
    :param datos_utiles: Mismos datos que en el fichero CSV.
    :param dict_provincias: Diccioanrio de provincias.
    :param dict_datos:  Diccionario con los datos de las provincias en cada año.
    :return: Un numpy array con los datos de todos los años extraidos.
    """
    dict_result = {}
    z = 0
    for a_dict in dict_datos:
        cod_comunidad_autonoma_actual = dict_provincias[a_dict['Provincia'][:2]]['CODAUTO']
        temp = np.zeros(n_years - 1)
        for i in range(1, len(a_dict)):
            if a_dict[datos_utiles[i]] != '':
                temp[i - 1] = round(float(a_dict[datos_utiles[i]]), 2)

        if cod_comunidad_autonoma_actual in dict_result:
            dict_result[cod_comunidad_autonoma_actual] += temp
        else:
            dict_result[cod_comunidad_autonoma_actual] = temp

    return dict_result


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
            'PRO': (CPRO + " " + nombre_provincia)
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


def calcular_media_comunidades(dict_datos_comunidades, numero_anios):
    """
    Calcula la media de población de una comunidad autónoma.
    :param numero_anios: Número de años total.
    :param dict_datos_comunidades: Datos de la comunidad autónoma, con su código y
    un numpy array con los datos de todos los años extraidos.
    :return: Diccionario con el código de la comunidad autónoma y la media de población del total.
    """
    dict_media_comunidades = {}
    for cod_comunidad, datos_comunidad in dict_datos_comunidades.items():
        dict_media_comunidades[cod_comunidad] = round(np.mean(datos_comunidad[:numero_anios]), 2)

    return dict_media_comunidades


def comunidades_con_mas_media(dict_media_comunidades, numero_comunidades):
    """
    Devuelve las comunidades con más media de población.
    :param numero_comunidades: Número de comunidades a devolver.
    :param dict_media_comunidades: Diccionario con el código de la comunidad autónoma y la media de población del total.
    :return: Lista con las comunidades con más media de población.
    """
    copia_dict_media_comunidades = dict_media_comunidades.copy()
    comunidades_mas_media = []
    for i in range(0, numero_comunidades):
        maximo = max(copia_dict_media_comunidades, key=copia_dict_media_comunidades.get)
        comunidades_mas_media.append(maximo)
        copia_dict_media_comunidades.pop(maximo)

    return comunidades_mas_media


def devolver_nombres_comunidades(dict_comunidades_mas_poblacion, dict_comunidades):
    """
    Devuelve los nombres de las comunidades con más población.
    :param dict_comunidades: Diccionario con el código de la comunidad autónoma y el nombre de la comunidad autónoma.
    :param dict_comunidades_mas_poblacion: Diccionario con el código de la comunidad autónoma y la media de población del total.
    :return: Lista con los nombres de las comunidades con más población.
    """
    lista_nombres_comunidades = []
    for cod_comunidad in dict_comunidades_mas_poblacion:
        lista_nombres_comunidades.append(dict_comunidades[cod_comunidad])

    return lista_nombres_comunidades


def devolver_poblacion_hombres(dict_datos_comunidades, numero_anios, numero_anios_total):
    """
    Calcula la población de hombres de una comunidad autónoma en cada año.
    :param numero_anios_total: Número de años total.
    :param numero_anios: Número de años total.
    :param dict_datos_comunidades: Datos de la comunidad autónoma, con su código y
    un numpy array con los datos de todos los años extraidos.
    :return: Diccionario con el código de la comunidad autónoma y un numpy con la población de los hombres en cada año.
    """
    dict_poblacion_hombres = {}
    for cod_comunidad, datos_comunidad in dict_datos_comunidades.items():
        temp = np.zeros(numero_anios)
        for i in range(0, numero_anios):
            temp[i] = datos_comunidad[i + numero_anios]

        dict_poblacion_hombres[cod_comunidad] = temp

    return dict_poblacion_hombres


def devolver_poblacion_mujeres(dict_datos_comunidades, numero_anios, numero_anios_total):
    """
    Calcula la población de mujeres de una comunidad autónoma en cada año.
    :param numero_anios_total: Número de años total.
    :param numero_anios: Número de años total.
    :param dict_datos_comunidades: Datos de la comunidad autónoma, con su código y
    un numpy array con los datos de todos los años extraidos.
    :return: Diccionario con el código de la comunidad autónoma y un numpy con la población de las mujeres en cada año.
    """
    dict_poblacion_mujeres = {}
    for cod_comunidad, datos_comunidad in dict_datos_comunidades.items():
        temp = np.zeros(numero_anios)
        for i in range(0, numero_anios):
            temp[i] = datos_comunidad[i + numero_anios * 2]

        dict_poblacion_mujeres[cod_comunidad] = temp

    return dict_poblacion_mujeres


def devolver_datos_comunidades(dict_comunidades_mas_poblacion, dict_datos_genero):
    """
    Devuelve los datos de las comunidades con más población en forma de lista.
    :param dict_datos_genero: Diccionario con el código de la comunidad autónoma y un numpy con la población de los hombres o mujeres en cada año.
    :param dict_comunidades_mas_poblacion: Diccionario con el código de la comunidad autónoma y la media de población del total.
    :return: Diccionario con el código de la comunidad autónoma y un numpy con la población de los hombres o mujeres en cada año.
    """
    lista_datos_comunidades = []
    for cod_comunidad in dict_comunidades_mas_poblacion:
        lista_datos_comunidades.append(dict_datos_genero[cod_comunidad])

    return lista_datos_comunidades


def crear_tabla_comunidades(dict_comunidades, dict_resultados, n_years):
    """
    Crea una tabla con las comunidades autónomas.
    :param n_years: Número de años.
    :param dict_resultados: Diccionario con los datos a usar.
    :param dict_comunidades: Diccionario con las comunidades autónomas.
    :return: Cadena con la tabla HTML.
    """
    p_poblacion = ""

    for cod_comunidad, comunidad in dict_comunidades.items():
        # Añadimos las columna de las provincias.
        p_poblacion += "<tr>\n"
        p_poblacion += "<td><strong>%s<strong></td>\n" % (cod_comunidad + ' ' + comunidad)
        for i in range(0, n_years - 1):
            variacion_absoluta = dict_resultados[cod_comunidad.strip()][i]
            p_poblacion += "<td>%s</td>\n" % locale.format_string('%.0f', variacion_absoluta, grouping=True)
        p_poblacion += "</tr>\n"

    return p_poblacion