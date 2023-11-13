"""Generar una página web 3 (fichero variacionComAutonomas.html) con una tabla con la variación de población por
comunidades autónomas desde el año 2011 a 2017, indicando variación absoluta, relativa y desagregando dicha
información por sexos, es decir, variación absoluta (hombres, mujeres) y relativa (hombres, mujeres). Para los
cálculos, hay que actuar de manera semejante que en el apartado R1."""

import csv
import bs4
import numpy as np
import matplotlib as mpl
import locale
import funciones as lc

locale.setlocale(locale.LC_ALL, '')

CABECERA = ("Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011"
            ";H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;\n")


def salida_html_R4(fichero, html_crear):
    """
    Genera la página web 3 (variacionComAutonomas.html)
    leyendo los datos del fichero que le pasamos como parámetro.
    Para cada provincia (fila) leerá el total nacional de cada año (columna) y
    generará una tabla con dos grandes columnas (Variación absoluta y Variación relativa)
    de cada provincia en el csv.
    :param fichero: CSV a leer.
    :param html_crear: HTML a crear.
    :return: None
    """
    # Leer el fichero CSV.
    dict_r = lc.dict_fichero_csv(fichero)
    p_poblacion = ""
    fila_1 = dict_r.__next__()  # Saltamos la primera fila (datos del total nacional que usamos para coger las cabeceras).

    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años.
    n_datos = len(datos_utiles)
    n_years = n_datos - 1  # 2017 a 2010 menos la columna "Provincias".

    # Cogemos todos los diccionarios que vamos a usar.
    comunidades_autonomas = lc.leer_comunidades('./entradasUTF8/comunidadesAutonomas.htm')
    provincias_ = lc.leer_provincias('./entradasUTF8/comunidadAutonoma-Provincia.htm')
    dict_resultados = lc.calcular_total_por_comunidad(provincias_, dict_r, n_years, datos_utiles)
    dict_medias_total = lc.calcular_media_comunidades(dict_resultados, n_years // 3)
    dict_hombres = lc.devolver_poblacion_hombres(dict_resultados, n_years // 3, n_years)
    dict_mujeres = lc.devolver_poblacion_mujeres(dict_resultados, n_years // 3, n_years)

    # Crear el fichero HTML.
    with open(html_crear, 'w', encoding='utf-8') as html:
        p_poblacion += lc.CABECERA_HTML

        # Crear la tabla
        tabla_inicio = """
        <table>
        <tr>
        <th> </th>
        <th colspan=%s>Variación absoluta</th>
        <th colspan=%s>Variación relativa</th>
        </tr>
        
        <tr>
        <th> </th>
        <th colspan=%s>Hombres</th>
        <th colspan=%s>Mujeres</th>
        <th colspan=%s>Hombres</th>
        <th colspan=%s>Mujeres</th>
        </tr>
        """ % (2 * n_years // 3 - 2, 2 * n_years // 3 - 2, n_years // 3 - 1, n_years // 3 - 1, n_years // 3 - 1, n_years // 3 - 1)

        # html.write(tabla_inicio)
        p_poblacion += tabla_inicio

        # Añadimos los años para la variación absoluta y relativa.
        p_poblacion += "<tr>\n"
        p_poblacion += "<th> </th>\n"

        for i in range(0, 4):
            for j in range(1, n_years // 3):
                p_poblacion += "<th>%s</th>\n" % datos_utiles[j][1:]

        p_poblacion += "</tr>\n"

        # Creamos la tabla con los datos de las comunidades autónomas.
        for comunidad in comunidades_autonomas:
            p_poblacion += "<tr>\n"
            p_poblacion += "<td><strong>%s</strong></td>\n" % comunidades_autonomas[comunidad]
            for i in range(1, 2):
                for j in range(1, n_years // 3):
                    # Calculamos la variación absoluta de hombres.
                    variacion_absoluta = (float(dict_hombres[comunidad][j - 1]) - float(dict_hombres[comunidad][j]))
                    p_poblacion += "<td>%s</td>\n" % locale.format_string('%.0f', variacion_absoluta, grouping=True)
                for j in range(1, n_years // 3):
                    # Calculamos la variación absoluta de mujeres.
                    variacion_absoluta = (float(dict_mujeres[comunidad][j - 1]) - float(dict_mujeres[comunidad][j]))
                    p_poblacion += "<td>%s</td>\n" % locale.format_string('%.0f', variacion_absoluta, grouping=True)

                for j in range(1, n_years // 3):
                    # Calculamos la variación relativa de hombres sin usar la función de lc.
                    variacion_relativa = (float(dict_hombres[comunidad][j - 1]) - float(dict_hombres[comunidad][j])) / float(dict_hombres[comunidad][j]) * 100
                    p_poblacion += "<td>%s</td>\n" % locale.format_string('%.2f', variacion_relativa, grouping=True)
                for j in range(1, n_years // 3):
                    # Calculamos la variación absoluta de mujeres.
                    variacion_relativa = (float(dict_mujeres[comunidad][j - 1]) - float(dict_mujeres[comunidad][j])) / float(dict_mujeres[comunidad][j]) * 100
                    p_poblacion += "<td>%s</td>\n" % locale.format_string('%.2f', variacion_relativa, grouping=True)

            p_poblacion += "</tr>\n"

        p_poblacion += "</table>\n"
        p_poblacion += lc.PIE_HTML

        html.write(p_poblacion)
        fileEstilo = open("./salidas/estilo.css", "w", encoding="utf8")

        estilo = """  table, th, td {
                        border-collapse: collapse;    
                        border:1px solid black;
                        font-family: Arial, Helvetica, sans-serif;
                        padding: 8px;
                        text-align: center;
                    }  """

        fileEstilo.write(estilo)
        fileEstilo.close()


def ejecutar_R4():
    lc.limpiar_csv('entradas/poblacionProvinciasHM2010-17.csv','./salidas/r2.csv',
                   CABECERA, 'Total Nacional', 'Notas')

    #lc.leer_fichero('./salidas/r2.csv')

    salida_html_R4('./salidas/r2.csv', 'salidas/salidaR4.html')


# Programa principal.
if __name__ == "__main__":
    ejecutar_R4()
