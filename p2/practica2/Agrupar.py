import math
import matplotlib.pyplot as plt
import json
import os
import glob
import sys
import parametros as p


# FUNCIONES
def distancia(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)


def agrupar_puntos(points):
    cluster = []
    cluster_actual = [points[0]]

    for punto in points[1:]:
        if distancia(punto, cluster_actual[-1]) < p.UmbralDistancia and len(cluster_actual) < p.MaxPuntos:
            cluster_actual.append(punto)
        else:
            if len(cluster_actual) >= p.MinPuntos:
                cluster.append(cluster_actual)
            cluster_actual = [punto]

    if len(cluster_actual) >= p.MinPuntos:
        cluster.append(cluster_actual)

    return cluster


# Lógica principal
def main():
    print("Directorio de trabajo es: ", os.getcwd())

    # Si los ficheros clustersPiernas.json y clustersNoPiernas.json existen, los borramos
    if os.path.exists("clustersPiernas.json"):
        os.remove("clustersPiernas.json")

    if os.path.exists("clustersNoPiernas.json"):
        os.remove("clustersNoPiernas.json")

    # VARIABLES
    listaPos = sorted(glob.glob("positivo*"))
    listaNeg = sorted(glob.glob("negativo*"))
    numPos = len(listaPos)
    numNeg = len(listaNeg)
    nombresjson = [
        "enPieCerca.json",
        "enPieMedia.json",
        "enPieLejos.json",
        "sentadoCerca.json",
        "sentadoMedia.json",
        "sentadoLejos.json",
        "cilindroMenorCerca.json",
        "cilindroMenorMedia.json",
        "cilindroMenorLejos.json",
        "cilindroMayorCerca.json",
        "cilindroMayorMedia.json",
        "cilindroMayorLejos.json"
    ]

    if numPos > 0:
        print("Numero de directorios con lecturas positivas: ", numPos)
    else:
        sys.exit("Error, no hay directorios con lecturas positivas")

    if numNeg > 0:
        print("Numero de directorios con lecturas negativas: ", numNeg)
    else:
        sys.exit("Error, no hay directorios con lecturas negativas")

    for index, positivo in enumerate(listaPos):
        objetos = []
        fichero_actual = positivo + "/" + nombresjson[index]

        # Para los ejemplos positivos, creamos clustersPiernas.json con el formato:
        # {
        #     "numero_cluster": i,
        #     "numero_puntos": j),
        #     "puntosX": [lista de puntos X],
        #     "puntosY": [lista de puntos Y]
        # }

        with open(fichero_actual, 'r') as f:
            for line in f:
                objetos.append(json.loads(line))

        cabecera = objetos[0]
        segundos = cabecera['TiempoSleep']
        maxIter = cabecera['MaxIteraciones']

        iterTotalesDict = objetos[len(objetos) - 1]
        iterTotales = iterTotalesDict['Iteraciones totales']

        plt.axis('equal')
        plt.axis([0, 4, -2, 2])

        # Para cada iteración, agrupamos los puntos y los guardamos en un fichero JSON
        for i in range(iterTotales):
            iteracion = objetos[i + 1]['Iteracion']
            puntosX = objetos[i + 1]['PuntosX']
            puntosY = objetos[i + 1]['PuntosY']

            print("Iteración: ", iteracion)
            plt.clf()
            plt.plot(puntosX, puntosY, 'r.')

            puntos = []
            for idx in range(len(puntosX)):
                puntos.append([puntosX[idx], puntosY[idx]])

            clusters = agrupar_puntos(puntos)

            for cluster_idx in range(len(clusters)):
                clusters[cluster_idx] = {
                    "numero_cluster": cluster_idx,
                    "numero_puntos": len(clusters[cluster_idx]),
                    "puntosX": [punto[0] for punto in clusters[cluster_idx]],
                    "puntosY": [punto[1] for punto in clusters[cluster_idx]]
                }

            with open("clustersPiernas.json", "a") as f:
                f.write(json.dumps(clusters) + '\n')

            # plt.show()

    # Hacemos lo propio con los ejemplos negativos
    for index, negativo in enumerate(listaNeg):
        objetos = []
        fichero_actual = negativo + "/" + nombresjson[index + 6]

        # Para los ejemplos negativos, creamos clustersNoPiernas.json con el formato:
        # {
        #     "numero_cluster": i,
        #     "numero_puntos": j),
        #     "puntosX": [lista de puntos X],
        #     "puntosY": [lista de puntos Y]
        # }

        with open(fichero_actual, 'r') as f:
            for line in f:
                objetos.append(json.loads(line))

        cabecera = objetos[0]
        segundos = cabecera['TiempoSleep']
        maxIter = cabecera['MaxIteraciones']

        iterTotalesDict = objetos[len(objetos) - 1]
        iterTotales = iterTotalesDict['Iteraciones totales']

        plt.axis('equal')
        plt.axis([0, 4, -2, 2])

        # Para cada iteración, agrupamos los puntos y los guardamos en un fichero JSON
        for i in range(iterTotales):
            iteracion = objetos[i + 1]['Iteracion']
            puntosX = objetos[i + 1]['PuntosX']
            puntosY = objetos[i + 1]['PuntosY']

            print("Iteración: ", iteracion)
            plt.clf()
            plt.plot(puntosX, puntosY, 'r.')

            puntos = []
            for idx in range(len(puntosX)):
                puntos.append([puntosX[idx], puntosY[idx]])

            clusters = agrupar_puntos(puntos)

            for cluster_idx in range(len(clusters)):
                clusters[cluster_idx] = {
                    "numero_cluster": cluster_idx,
                    "numero_puntos": len(clusters[cluster_idx]),
                    "puntosX": [punto[0] for punto in clusters[cluster_idx]],
                    "puntosY": [punto[1] for punto in clusters[cluster_idx]]
                }

            with open("clustersNoPiernas.json", "a") as f:
                f.write(json.dumps(clusters) + '\n')

            # plt.show()