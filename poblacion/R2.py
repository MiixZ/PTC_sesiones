"""
Usando el listado de comunidades autónomas que podemos obtener del fichero
comunidadesAutonomas.html, así como de las provincias de cada comunidad autónoma que
podemos obtener de comunidadAutonoma-Provincia.html y los datos de poblacionProvinciasHM2010-17.csv,
hay que generar una página web 2 (fichero poblacionComAutonomas.html) con una tabla con los valores
de población de cada comunidad autónoma en cada año de 2010 a 2017,
indicando también los valores desagregados por sexos (de manera semejante a como aparece
en la siguiente figura). Las celdas deben tener el contenido centrado.
"""

import locale
import funciones as lc

locale.setlocale(locale.LC_ALL, '')

# Hay que usar diccionarios y numpy arrays. Prohibido
# usar pandas y dataframe.

CABECERA = ("Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011"
            ";H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;\n")


# FUNCIONES
def salida_html_R2(fichero, html_crear):
    """
    Genera la página web 2 (salidaR2.html)
    leyendo los datos del fichero que le pasamos como parámetro.
    Para cada comunidad autónoma, se mostrará la suma de todas sus provincias por año y se insertará en una tabla.
    :param fichero: CSV a leer.
    :param html_crear: HTML a crear.
    :return: None
    """
    print(fichero)

    # Leer y limpiar el fichero CSV.
    dict_r = lc.dict_fichero_csv(fichero)
    p_poblacion = ""  # Variable para guardar el html.
    fila_1 = dict_r.__next__()  # Saltamos la primera fila
    # (datos del total nacional que usamos para coger las cabeceras)

    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años.
    n_datos = len(datos_utiles)
    n_years = n_datos - 1  # 2017 a 2010 menos la columna "Provincias".

    # Crear el fichero HTML.
    with open(html_crear, 'w', encoding='utf-8') as html:
        p_poblacion += lc.CABECERA_HTML

        # Crear la tabla con la estructura que queremos.
        tabla_inicio = """
        <table>
        <tr>
        <th rowspan='2'>CCAA</th> \n
        <th colspan=%s>Total</th>
        <th colspan=%s>Hombres</th>
        <th colspan=%s>Mujeres</th>
        </tr>
        """ % ((n_years - 1) // 3, n_years // 3, n_years // 3)  # -1 para quitar la columna "provincias"

        p_poblacion += tabla_inicio

        # ---------------------------------- Cabecera para los años. -----------------------------------------------
        p_poblacion += "<tr>\n"
        datos_utiles_sin_letra = [dato[1:] if dato != 'Provincia' else dato for dato in datos_utiles]

        for i in range(1, n_years):
            p_poblacion += "<th>%s</th>\n" % datos_utiles_sin_letra[i]

        p_poblacion += "</tr>\n"

        # ---------------------------------- Cuerpo de la tabla. ---------------------------------------------------
        comunidades_autonomas = lc.leer_comunidades(lc.COMUNIDADES_AUTONOMAS_PATH)
        provincias_ = lc.leer_provincias(lc.COMUNIDADES_AUTONOMAS_PROVINCIAS_PATH)
        dict_resultados = lc.calcular_total_por_comunidad(provincias_, dict_r, n_years, datos_utiles)
        p_poblacion += lc.crear_tabla_comunidades(comunidades_autonomas, dict_resultados, n_years)

        # ---------------------------------- Fin de fichero. ------------------------------------------------------

        p_poblacion += lc.PIE_HTML
        html.write(p_poblacion)


def ejecutar_R2():
    """
    Ejecuta la función salida_html_R2(fichero, html_crear).
    :return: None
    """
    lc.limpiar_csv('./entradas/poblacionProvinciasHM2010-17.csv',
                   './resultados/poblacionProvinciasHM2010-17-limpio.csv',
                   CABECERA, 'Total Nacional', 'Notas')
    # lc.leer_fichero('./resultados/r2.csv')
    salida_html_R2('./resultados/poblacionProvinciasHM2010-17-limpio.csv', './resultados/poblacionComAutonomas.html')


# MAIN
if __name__ == "__main__":
    ejecutar_R2()
