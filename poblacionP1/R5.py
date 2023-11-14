"""Usando Matplotlib, para las 10 comunidades elegidas en el punto R3 generar un gráfico de líneas que refleje la
evolución de la población total de cada comunidad autónoma desde el año 2010 a 2017, salvar el gráfico a fichero e
incorporarlo a la página web 3 del punto R4."""

import locale
import funciones as lc
import numpy as np
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, '')

# Hay que usar diccionarios y numpy arrays. Prohibido
# usar pandas y dataframe.

CABECERA = ("Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011"
            ";H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;\n")


def salida_html_R5(fichero, html):
    """
    Genera la página web 4 (salidaR4_5.html) con el gráfico de líneas incorporado.
    leyendo los datos del fichero que le pasamos como parámetro.
    Para cada comunidad autónoma, se mostrará la suma de todas sus provincias por año y se insertará en una tabla.
    :param fichero: CSV a leer.
    :param html: HTML a crear.
    :return: None
    """
    # Leer el fichero CSV.
    dict_r = lc.dict_fichero_csv(fichero)
    fila_1 = dict_r.__next__()  # Saltamos la primera fila (datos del total nacional que usamos para coger las cabeceras).

    datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años.
    n_datos = len(datos_utiles)
    n_years = n_datos - 1  # 2017 a 2010 menos el título "Provincias".

    # Cogemos todos los diccionarios que vayamos a usar.
    comunidades_autonomas = lc.leer_comunidades(lc.COMUNIDADES_AUTONOMAS_PATH)
    provincias_ = lc.leer_provincias(lc.COMUNIDADES_AUTONOMAS_PROVINCIAS_PATH)
    dict_resultados = lc.calcular_total_por_comunidad(provincias_, dict_r, n_years, datos_utiles)
    dict_medias_total = lc.calcular_media_comunidades(dict_resultados, n_years // 3)
    comunidades_mas_poblacion = lc.comunidades_con_mas_media(dict_medias_total, 10)

    # Creamos el gráfico de líneas.
    plt.figure("lineal")
    plt.title("Población total en 2010-2017 (CCAA)")
    anios = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
    X = np.arange(len(anios))
    plt.axis([0, len(anios), 1125000, 8750000])

    for comunidad in comunidades_mas_poblacion:
        # Le damos la vuelta porque mostraría de 2017 a 2010.
        plt.plot(dict_resultados[comunidad][len(anios)-1::-1], marker="o", label=comunidades_autonomas[comunidad])

    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

    # Ajustar los límites del eje x y aplicar margen
    margen = 0.5  # 5% de margen
    plt.xlim(-margen, len(anios) - 1 + margen)
    plt.xticks(X, anios)

    # Guardar la figura con un buen espacio alrededor
    plt.savefig("./imagenes/R5.png", bbox_inches="tight")
    lc.aniadir_imagen_a_html(html, "./imagenes/R5.png", "1000px", "80px", "Gráfico de líneas")


def ejecutar_R5():
    salida_html_R5('./resultados/poblacionProvinciasHM2010-17-limpio.csv', './resultados/variacionComAutonomas.html')


if __name__ == "__main__":
    ejecutar_R5()
