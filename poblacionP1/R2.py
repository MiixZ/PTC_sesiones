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
# Leemos el diccionario de comunidades autónomas.
comunidades = lc.leer_comunidades('./entradasUTF8/comunidadesAutonomas.htm')

"""
    PARA LEER EL DICCIONARIO DE COMUNIDADES
for cod_comunidad, comunidad in comunidades.items():
    print(cod_comunidad, comunidad)
"""

# Leemos la lista de provincias.
provincias = lc.leer_provincias('./entradasUTF8/comunidadAutonoma-Provincia.htm')

"""
    PARA LEER EL DICCIONARIO DE PROVINCIAS
for cod_provincia, datos_provincia in provincias.items():
    print(cod_provincia, datos_provincia['PRO'], datos_provincia['CODAUTO'], datos_provincia['CCAA'])
"""

lc.limpiar_csv('./entradas/poblacionProvinciasHM2010-17.csv',
               './salidas/r2.csv',
               CABECERA, '02 Albacete', 'Notas')

# lc.leer_fichero('./salidas/r2.csv')
