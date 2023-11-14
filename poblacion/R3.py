"""
Usando Matplotlib, para las 10 comunidades con más población media de 2010 a 2017, generar un gráfico de columnas
que indique la población de hombres y mujeres en el año 2017, salvar el gráfico a fichero e incorporarlo a la página
web 2 del punto R2.
"""

import locale
import funciones as lc
import numpy as np
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, '')

# Hay que usar diccionarios y numpy arrays. Prohibido
# usar pandas y dataframe.

CABECERA = ("Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011"
            ";H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;\n")


def salida_html_R3(fichero, html_):
    """
    Genera la página web 2 (salidaR2_3.html) con el gráfico de barras incorporado.
    leyendo los datos del fichero que le pasamos como parámetro.
    Para cada comunidad autónoma, se mostrará la suma de todas sus provincias por año y se insertará en una tabla.
    :param fichero: CSV a leer.
    :param html: HTML a crear.
    :return: None
    """
    # Leer el fichero CSV.
    dict_r = lc.dict_fichero_csv(fichero)
    p_poblacion = ""
    fila_1 = dict_r.__next__()  # Saltamos la primera fila (datos del total nacional que usamos para coger las cabeceras).

    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años.
    n_datos = len(datos_utiles)
    n_years = n_datos - 1  # 2017 a 2010 menos el título "Provincias".

    # Cogemos todos los diccionarios que vayamos a usar.
    comunidades_autonomas = lc.leer_comunidades(lc.COMUNIDADES_AUTONOMAS_PATH)
    provincias_ = lc.leer_provincias(lc.COMUNIDADES_AUTONOMAS_PROVINCIAS_PATH)
    dict_resultados = lc.calcular_total_por_comunidad(provincias_, dict_r, n_years, datos_utiles)
    dict_medias_total = lc.calcular_media_comunidades(dict_resultados, n_years // 3)
    dict_hombres = lc.devolver_poblacion_hombres(dict_resultados, n_years // 3, n_years)
    dict_mujeres = lc.devolver_poblacion_mujeres(dict_resultados, n_years // 3, n_years)

    # Ponemos el gráfico.
    # Damos nombre a los ejes y título al gráfico.
    plt.figure("barras")
    plt.title("Población de hombres y mujeres en 2017")
    plt.xlabel("Comunidades Autónomas")
    plt.ylabel("Población")

    # Cogemos el código de las 10 comunidades con más población media de 2010 a 2017.
    comunidades_mas_poblacion = lc.comunidades_con_mas_media(dict_medias_total, 10)

    # Cogemos los datos de hombres y mujeres de las 10 comunidades con más población media de 2010 a 2017.
    # Los datos es una lista con 10 listas dentro, cada una con los datos de hombres o mujeres de cada comunidad.
    datos_hombres = lc.devolver_datos_comunidades(comunidades_mas_poblacion, dict_hombres)
    datos_mujeres = lc.devolver_datos_comunidades(comunidades_mas_poblacion, dict_mujeres)

    # Creamos el gráfico.
    num_comunidades = len(comunidades_mas_poblacion)
    X = np.arange(num_comunidades)
    plt.figure("barras")
    plt.axis([0, num_comunidades, 0, 4250000])
    nombre_comunidades = lc.devolver_nombres_comunidades(comunidades_mas_poblacion, comunidades_autonomas)

    # Creamos una lista con los datos de hombres y mujeres de cada comunidad.
    hombres = []
    mujeres = []
    for i in range(num_comunidades):
        hombres.append(datos_hombres[i][0])
        mujeres.append(datos_mujeres[i][0])

    plt.bar(X + 0.25, hombres, color="b", width=0.25)
    plt.bar(X + 0.5, mujeres, color="r", width=0.25)

    plt.xticks(X + 0.38, nombre_comunidades, rotation=80)
    plt.legend(["Hombres", "Mujeres"])
    plt.title("Población por sexo en el año 2017 (CCAA)")
    plt.savefig("./imagenes/R3.png", bbox_inches='tight')

    lc.aniadir_imagen_a_html('./resultados/poblacionComAutonomas.html', '../imagenes/R3.png',
                             "1000px", "800px", "Gráfico de barras")


def ejecutar_R3():
    """
    Ejecuta la función salida_html_R3.
    :return: None
    """
    salida_html_R3('./resultados/poblacionProvinciasHM2010-17-limpio.csv', './resultados/poblacionComAutonomas.html')


# MAIN
if __name__ == "__main__":
    ejecutar_R3()
