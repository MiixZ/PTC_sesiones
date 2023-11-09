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
def salida_html_R1(fichero):
    """
    Genera la página web 1 (variacionprovincias.html)
    leyendo los datos del fichero que le pasamos como parámetro.
    Para cada provincia (fila) leerá el total nacional de cada año (columna) y
    generará una tabla con dos grandes columnas (Variación absoluta y Variación relativa)
    de cada provincia en el csv.
    :param fichero: CSV a leer.
    :return: None
    """


def variacion_relativa(anio_mayor, anio_menor):
    """
    Calcula la variación relativa entre dos años.
    :param anio_mayor: Año mayor.
    :param anio_menor: Año menor.
    :return: Variación relativa entre ambos años.
    """
    return ((anio_mayor - anio_menor) / anio_menor) * 100
