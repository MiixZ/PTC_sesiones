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
import libreria_comun as lc


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
    with open(fichero, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        fila_1 = reader.__next__()
        datos_utiles = [columna for columna in reader.fieldnames if columna != 'none']

        n_datos = len(datos_utiles)

        # Crear el fichero HTML.
        with open(html_crear, 'w', encoding='utf-8') as html:
            html.write(lc.CABECERA_HTML)

            # Crear la tabla
            tabla_inicio = """
            <table>
            <tr>
            <th>Provincia</th>
            <th>Variación absoluta</th>
            <th>Variación relativa</th>
            </tr>
            """

            html.write(tabla_inicio)

            anios = ["Anio", "2017", "2016", "2015", "2014", "2013", "2012", "2011"]

            # Recorrer el fichero CSV.
            for reg in reader:
                html.write("<tr>\n")
                html.write("<td>%s</td>\n" % reg['Provincia'])

                # Recorrer los datos útiles.
                for dato in datos_utiles:
                    html.write("<td>%s</td>\n" % reg[dato])

                html.write("</tr>\n")

            html.write("</table>\n")
            html.write(lc.PIE_HTML)


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
               cabecera)
lc.leer_fichero('salidas/poblacionProvinciasHM2010-17.csv')

salida_html_R1('salidas/poblacionProvinciasHM2010-17.csv',
               'salidas/salidaR1.html')
