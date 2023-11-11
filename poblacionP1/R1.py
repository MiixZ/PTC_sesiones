"""
Calcular la variación de la población por provincias desde el año 2011 a 2017 en términos absolutos y relativos
generando la página web 1 (variacionprovincias.html) que contenga una tabla como la del pdf.
Las fórmulas a aplicar:
Variación absoluta = Población 2017 – Población 2016
Variación relativa = (Población 2017 – Población 2016) * 100
                        ----------------------------------------
"""

import csv
import bs4
import numpy as np
import matplotlib as mpl
import locale
import funciones as lc

locale.setlocale(locale.LC_ALL, '')


# Hay que usar diccionarios y numpy arrays. Prohibido
# usar pandas y dataframe.


# Funciones
def salida_html_R1(fichero, html_crear):
    """
    Genera la página web 1 (variacionprovincias.html)
    leyendo los datos del fichero que le pasamos como parámetro.
    Para cada provincia (fila) leerá el total nacional de cada año (columna) y
    generará una tabla con dos grandes columnas (Variación absoluta y Variación relativa)
    de cada provincia en el csv.
    :param fichero: CSV a leer.
    :param html_crear: HTML a crear.
    :return: None
    """
    # Leer el fichero CSV.
    f = open(fichero, encoding='utf-8')
    dict_r = csv.DictReader(f, delimiter=';')
    p_poblacion = ""
    fila_1 = dict_r.__next__()
    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']
    n_datos = len(datos_utiles)
    n_years = n_datos - 2  # 2017 a 2010

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
        """ % (n_years - 1, n_years)  # -1 para quitar la columna "provincias"

        # html.write(tabla_inicio)
        p_poblacion += tabla_inicio

        # Añadimos los años para la variación absoluta y relativa.
        p_poblacion += "<tr>\n"
        p_poblacion += "<th>%s</th>\n" % datos_utiles[0]
        for i in range(1, n_years):
            p_poblacion += "<th>%s</th>\n" % datos_utiles[i]
        for i in range(1, n_years):
            p_poblacion += "<th>%s</th>\n" % datos_utiles[i]
        p_poblacion += "</tr>\n"

        dict_r.__next__()  # Saltamos la primera fila (años).
        for a_dict in dict_r:
            # Añadimos las provincias.
            p_poblacion += "<tr>\n"
            p_poblacion += "<td>%s</td>\n" % a_dict['Provincia']
            for i in range(1, n_years):
                variacion_absoluta = (float(a_dict[datos_utiles[i]]) - float(a_dict[datos_utiles[i + 1]]))
                # Añadimos la variación absoluta.
                p_poblacion += "<td>%s</td>\n" % locale.format_string('%.2f', variacion_absoluta, grouping=True)
            for i in range(1, n_years):
                variacion_relat = variacion_relativa(float(a_dict[datos_utiles[i]]),
                                                     float(a_dict[datos_utiles[i + 1]]))
                # Añadimos la variación relativa.
                p_poblacion += "<td>%s</td>\n" % locale.format_string('%.2f', variacion_relat, grouping=True)
            p_poblacion += "</tr>\n"

        # html.write("</table>\n")
        p_poblacion += "</table>\n"
        # html.write(lc.PIE_HTML)
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


def variacion_relativa(anio_mayor, anio_menor):
    """
    Calcula la variación relativa entre dos años.
    :param anio_mayor: Año mayor.
    :param anio_menor: Año menor.
    :return: Variación relativa entre ambos años.
    """
    return ((anio_mayor - anio_menor) / anio_menor) * 100


cabecera = "Provincia;2017;2016;2015;2014;2013;2012;2011;2010"
lc.limpiar_csv('entradas/poblacionProvinciasHM2010-17.csv',
               "salidas/poblacionProvinciasHM2010-17.csv",
               cabecera, "Total", "Notas")
lc.leer_fichero('salidas/poblacionProvinciasHM2010-17.csv')

salida_html_R1('salidas/poblacionProvinciasHM2010-17.csv',
               'salidas/salidaR1.html')
