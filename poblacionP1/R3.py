"""
Usando Matplotlib, para las 10 comunidades con más población media de 2010 a 2017, generar un gráfico de columnas
que indique la población de hombres y mujeres en el año 2017, salvar el gráfico a fichero e incorporarlo a la página
web 2 del punto R2.
"""

import matplotlib.pyplot as plt
import numpy as np
import funciones as lc

# Funciones
# Damos nombre a los ejes y título al gráfico.

plt.figure("lineal")
plt.title("Población de hombres y mujeres en 2017")
plt.xlabel("Comunidades Autónomas")
plt.ylabel("Población")

datos = [[1, 2, 3, 4], [3, 5, 3, 5], [8, 6, 4, 2]]
X = np.arange(4)

dict_r = lc.dict_fichero_csv('./salidas/r2.csv')
comunidades_autonomas = lc.leer_comunidades('./entradasUTF8/comunidadesAutonomas.htm')
provincias_ = lc.leer_provincias('./entradasUTF8/comunidadAutonoma-Provincia.htm')
fila_1 = dict_r.__next__()  # Saltamos la primera fila (datos del total nacional que usamos para coger las cabeceras).
datos_utiles = [columna for columna in fila_1.keys() if columna != 'none']  # Cogemos los años.
n_datos = len(datos_utiles)
n_years = n_datos - 1  # 2017 a 2010 menos la columna "Provincias".
dict_resultados = lc.calcular_total_por_comunidad(provincias_, dict_r, n_years, datos_utiles)
dict_medias = lc.calcular_media_comunidades(dict_resultados, n_years // 3)
dict_hombres = lc.devolver_poblacion_hombres(dict_resultados, n_years // 3, n_years)
dict_mujeres = lc.devolver_poblacion_mujeres(dict_resultados, n_years // 3, n_years)
print(dict_mujeres)

print("\nX es:", X)

plt.figure("barras")
plt.axis([0, 5, 0, 10])
plt.bar(X + 0.00, datos[0], color="b", width=0.25)
plt.bar(X + 0.25, datos[1], color="g", width=0.25)
plt.bar(X + 0.50, datos[2], color="r", width=0.25)
plt.xticks(X + 0.38, ["A", "B", "C", "D"])

plt.savefig("Grafico2.jpg")
