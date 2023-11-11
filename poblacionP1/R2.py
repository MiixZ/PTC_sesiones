"""
Usando el listado de comunidades autónomas que podemos obtener del fichero
comunidadesAutonomas.html, así como de las provincias de cada comunidad autónoma que
podemos obtener de comunidadAutonoma-Provincia.html y los datos de poblacionProvinciasHM2010-17.csv,
hay que generar una página web 2 (fichero poblacionComAutonomas.html) con una tabla con los valores
de población de cada comunidad autónoma en cada año de 2010 a 2017,
indicando también los valores desagregados por sexos (de manera semejante a como aparece
en la siguiente figura). Las celdas deben tener el contenido centrado.
"""

import csv
import locale
import funciones as lc
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, '')

# Hay que usar diccionarios y numpy arrays. Prohibido
# usar pandas y dataframe.

CABECERA = ("Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011"
            ";H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;\n")


# FUNCIONES
def salida_html_R2(fichero, html_crear):
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
    dict_r = lc.dict_fichero_csv(fichero)
    p_poblacion = ""

    fila_1 = dict_r.__next__()  # Saltamos la primera fila (datos innecesarios).
    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años.
    n_datos = len(datos_utiles)
    n_years = n_datos - 1  # 2017 a 2010

    # Crear el fichero HTML.
    with open(html_crear, 'w', encoding='utf-8') as html:
        p_poblacion += lc.CABECERA_HTML

        # Crear la tabla
        tabla_inicio = """
        <table>
        <tr>
        <th rowspan='2'>CCAA</th> \n
        <th colspan=%s>Total</th>
        <th colspan=%s>Hombres</th>
        <th colspan=%s>Mujeres</th>
        </tr>
        """ % ((n_years - 1) // 3, n_years // 3, n_years // 3)  # -1 para quitar la columna "provincias"

        # html.write(tabla_inicio)
        p_poblacion += tabla_inicio

        # ---------------------------------- Cabecera para los años. -----------------------------------------------
        p_poblacion += "<tr>\n"
        for i in range(1, n_years):
            p_poblacion += "<th>%s</th>\n" % datos_utiles[i]
        p_poblacion += "</tr>\n"

        dict_r.__next__()  # Saltamos la primera fila (años en el csv).

        # Cogemos el diccionario de las comunidades autónomas y las provincias.
        comunidades_autonomas = lc.leer_comunidades('./entradasUTF8/comunidadesAutonomas.htm')
        provincias_ = lc.leer_provincias('./entradasUTF8/comunidadAutonoma-Provincia.htm')
        dict_resultados = lc.calcular_total_por_comunidad(provincias_, dict_r, n_years, datos_utiles)

        for cod_comunidad, comunidad in comunidades_autonomas.items():
            # Añadimos las columna de las provincias.

            p_poblacion += "<tr>\n"
            p_poblacion += "<td><strong>%s<strong></td>\n" % (cod_comunidad + comunidad)
            for i in range(0, n_years - 1):
                variacion_absoluta = dict_resultados[cod_comunidad.strip()][i]
                p_poblacion += "<td>%s</td>\n" % locale.format_string('%.2f', variacion_absoluta, grouping=True)
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


# Leemos el diccionario de comunidades autónomas.
comunidades = lc.leer_comunidades('./entradasUTF8/comunidadesAutonomas.htm')

"""
    PARA LEER EL DICCIONARIO DE COMUNIDADES
for cod_comunidad, comunidad in comunidades.items():
    print(cod_comunidad, comunidad['CCAA'], comunidad['cantidad'])
"""

# Leemos la lista de provincias.
provincias = lc.leer_provincias('./entradasUTF8/comunidadAutonoma-Provincia.htm')

"""for cod_provincia, datos_provincia in provincias.items():
    print(cod_provincia, datos_provincia['PRO'], datos_provincia['CODAUTO'], datos_provincia['CCAA'])"""

lc.limpiar_csv('./entradas/poblacionProvinciasHM2010-17.csv',
               './salidas/r2.csv',
               CABECERA, '02 Albacete', 'Notas')

# lc.leer_fichero('./salidas/r2.csv')

salida_html_R2('./salidas/r2.csv', './salidas/salidaR2.html')
