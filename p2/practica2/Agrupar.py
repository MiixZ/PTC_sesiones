import math
import matplotlib.pyplot as plt
import json
import os
import glob
import sys
import parametros as p


# VARIABLES
listaPos = sorted(glob.glob("positivo*"))
listaNeg = sorted(glob.glob("negativo*"))
numPos = len(listaPos)
numNeg = len(listaNeg)

# FUNCIONES
def distancia(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)


def agrupar_puntos(puntos):
    clusters = []
    cluster_actual = [puntos[0]]

    for punto in puntos[1:]:
        if distancia(punto, cluster_actual[-1]) < p.UmbralDistancia and len(cluster_actual) < p.MaxPuntos:
            cluster_actual.append(punto)
        else:
            if len(cluster_actual) >= p.MinPuntos:
                clusters.append(cluster_actual)
            cluster_actual = [punto]

    if len(cluster_actual) >= p.MinPuntos:
        clusters.append(cluster_actual)

    return clusters

