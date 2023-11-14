"""
Calcular la variación de la población por provincias desde el año 2011 a 2017 en términos absolutos y relativos
generando la página web 1 (variacionprovincias.html) que contenga una tabla como la del pdf.
Las fórmulas a aplicar:
Variación absoluta = Población 2017 – Población 2016
Variación relativa = (Población 2017 – Población 2016) * 100
                        ----------------------------------------
"""

import locale
import funciones as lc

locale.setlocale(locale.LC_ALL, '')

CABECERA = "Provincia;2017;2016;2015;2014;2013;2012;2011;2010"      # Cabecera con los datos que vamos a coger.

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
    dict_r = lc.dict_fichero_csv(fichero)       # Limpiamos el fichero csv.

    # Diccionarios y estructuras que vamos a usar.
    p_poblacion = ""            # String que vamos a escribir en el html.
    fila_1 = dict_r.__next__()  # Saltamos la primera fila (datos que usamos para coger las cabeceras).
    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años que vamos a usar.
    n_datos = len(datos_utiles)                 # Longitud de los datos.
    n_years = n_datos - 2  # 2017 a 2011        # Número de años que vamos a usar menos la columna "Provincias".

    # Crear el fichero HTML.
    with open(html_crear, 'w', encoding='utf-8') as html:
        p_poblacion += lc.CABECERA_HTML

        # Crear la tabla con la estructura que queremos.
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

        # Inicio de la estructura de la tabla.
        p_poblacion += "<tr>\n"
        p_poblacion += "<th>%s</th>\n" % datos_utiles[0]    # Titulo de la primera columna.

        # Doble for para colocar los años tanto en la variación absoluta como en la relativa.
        for i in range(1, n_years):
            p_poblacion += "<th>%s</th>\n" % datos_utiles[i]

        for i in range(1, n_years):
            p_poblacion += "<th>%s</th>\n" % datos_utiles[i]

        p_poblacion += "</tr>\n"

        dict_r.__next__()  # Saltamos la primera fila (Datos innecesarios).
        for a_dict in dict_r:
            # Añadimos las provincias.
            p_poblacion += "<tr>\n"
            p_poblacion += "<td>%s</td>\n" % a_dict['Provincia']        # Nombre de la provincia en la primera columna.

            # Inicio celdas de datos.
            for i in range(1, n_years):
                variacion_absoluta = lc.variacion_absoluta(a_dict[datos_utiles[i]],
                                                           a_dict[datos_utiles[i + 1]])
                # Añadimos la variación absoluta.
                p_poblacion += "<td>%s</td>\n" % variacion_absoluta
            for i in range(1, n_years):
                variacion_relativa = lc.variacion_relativa(float(a_dict[datos_utiles[i]]),
                                                     float(a_dict[datos_utiles[i + 1]]))
                # Añadimos la variación relativa.
                p_poblacion += "<td>%s</td>\n" % variacion_relativa

            # Fin celdas de datos.
            p_poblacion += "</tr>\n"

        p_poblacion += "</table>\n"
        p_poblacion += lc.PIE_HTML

        html.write(p_poblacion)


def ejecutar_R1():
    lc.limpiar_csv('entradas/poblacionProvinciasHM2010-17.csv',
                   "resultados/poblacionProvinciasHM2010-17-limpio.csv",
                   CABECERA, "Total", "Notas")

    # lc.leer_fichero('resultados/poblacionProvinciasHM2010-17.csv')

    salida_html_R1('resultados/poblacionProvinciasHM2010-17-limpio.csv',
                   'resultados/variacionProvincias.html')


# Programa principal.
if __name__ == "__main__":
    ejecutar_R1()
