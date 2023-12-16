import os

import numpy as np
import json
import csv


def distancia_euclidea(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def calcular_perimetro(cluster):
    perimetro = 0
    for i in range(cluster["numero_puntos"] - 1):
        p1 = [cluster["puntosX"][i], cluster["puntosY"][i]]
        p2 = [cluster["puntosX"][i + 1], cluster["puntosY"][i + 1]]
        perimetro += distancia_euclidea(p1, p2)

    return perimetro


def calcular_anchura(cluster):
    p1 = [cluster["puntosX"][0], cluster["puntosY"][0]]
    p2 = [cluster["puntosX"][-1], cluster["puntosY"][-1]]

    return distancia_euclidea(p1, p2)


def calcular_profundidad(cluster):
    p1 = [cluster["puntosX"][0], cluster["puntosY"][0]]
    p2 = [cluster["puntosX"][-1], cluster["puntosY"][-1]]
    profundidades = []
    for i in range(cluster["numero_puntos"]):
        punto = [cluster["puntosX"][i], cluster["puntosY"][i]]
        numerador = abs((p2[1] - p1[1]) * punto[0] - (p2[0] - p1[0]) * punto[1] + p2[0] * p1[1] - p2[1] * p1[0])
        denominador = np.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)
        if denominador == 0:
            profundidades.append(0)
        else:
            profundidades.append(numerador / denominador)
    return max(profundidades)


# MAIN
def main():
    # Si existen los ficheros .dat, los borramos
    if os.path.exists("caracteristicasPiernas.dat"):
        os.remove("caracteristicasPiernas.dat")

    if os.path.exists("caracteristicasNoPiernas.dat"):
        os.remove("caracteristicasNoPiernas.dat")

    # Si existe el .csv, lo borramos
    if os.path.exists("piernasDataset.csv"):
        os.remove("piernasDataset.csv")

    # Leer los ficheros de clústeres
    with open('clustersPiernas.json', 'r') as f:
        clusters_piernas = [json.loads(line) for line in f]

    with open('clustersNoPiernas.json', 'r') as f:
        clusters_no_piernas = [json.loads(line) for line in f]

    # Calcular las características y guardarlas en nuevos ficheros
    with open('caracteristicasPiernas.dat', 'w') as f:
        for cluster in clusters_piernas:
            caracteristicas = {
                "numero_cluster": cluster["numero_cluster"],
                "perimetro": calcular_perimetro(cluster),
                "profundidad": calcular_profundidad(cluster),
                "anchura": calcular_anchura(cluster),
                "esPierna": 1  # Verdadero para los clústeres de piernas
            }
            f.write(json.dumps(caracteristicas) + '\n')

    with open('caracteristicasNoPiernas.dat', 'w') as f:
        for cluster in clusters_no_piernas:
            caracteristicas = {
                "numero_cluster": cluster["numero_cluster"],
                "perimetro": calcular_perimetro(cluster),
                "profundidad": calcular_profundidad(cluster),
                "anchura": calcular_anchura(cluster),
                "esPierna": 0  # Falso para los clústeres de no piernas
            }
            f.write(json.dumps(caracteristicas) + '\n')

    # Leer los ficheros de características
    with open('caracteristicasPiernas.dat', 'r') as f:
        caracteristicas_piernas = [json.loads(line) for line in f]

    with open('caracteristicasNoPiernas.dat', 'r') as f:
        caracteristicas_no_piernas = [json.loads(line) for line in f]

    # Crear el fichero piernasDataset.csv
    with open('piernasDataset.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Escribir las características de los clústeres no piernas
        for caracteristicas in caracteristicas_no_piernas:
            writer.writerow([format(caracteristicas['perimetro'], '.2f'),
                             format(caracteristicas['profundidad'], '.2f'),
                             format(caracteristicas['anchura'], '.2f'),
                             0])

        # Escribir las características de los clústeres piernas
        for caracteristicas in caracteristicas_piernas:
            writer.writerow([format(caracteristicas['perimetro'], '.2f'),
                             format(caracteristicas['profundidad'], '.2f'),
                             format(caracteristicas['anchura'], '.2f'),
                             1])
