import os
import json
import pickle
from matplotlib import pyplot as plt
import sim as vrep  # Al final cambiarlo por import vrep
import time
import numpy as np
import agrupar
import caracteristicas as car
import pandas as pd

# VARIABLES
clientID = 0  # Identificador de la conexión con el simulador


# FUNCIONES
def distancia_entre_clusters(cluster1, cluster2):
    min_dist = 100000
    for i in range(cluster1["numero_puntos"]):
        for j in range(cluster2["numero_puntos"]):
            p1 = [cluster1["puntosX"][i], cluster1["puntosY"][i]]
            p2 = [cluster2["puntosX"][j], cluster2["puntosY"][j]]
            dist = car.distancia_euclidea(p1, p2)
            if dist < min_dist:
                min_dist = dist

    return min_dist


def punto_medio_clusteres(cluster1, cluster2):
    x1 = np.mean(cluster1["puntosX"])
    y1 = np.mean(cluster1["puntosY"])
    x2 = np.mean(cluster2["puntosX"])
    y2 = np.mean(cluster2["puntosY"])

    punto_medio_x = (x1 + x2) / 2
    punto_medio_y = (y1 + y2) / 2

    return [punto_medio_x, punto_medio_y]


def main():
    n_cluster = 0
    # Si no existe el directorio /prediccion, lo creamos
    if not os.path.exists("prediccion"):
        os.mkdir("prediccion")

    # Nos colocamos en el directorio /prediccion
    os.chdir("prediccion")

    # ROBOTS
    # Obtener el handler del robot
    _, robot = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)

    # MOTORES
    # Obtener el handler de los motores del robot
    _, motor_izquierdo = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
    _, motor_derecho = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)

    # CAMARA
    # Obtener el handler de la cámara
    _, camara = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)

    # LASER
    # Obtener el handler del laser
    _, laser = vrep.simxGetStringSignal(clientID, 'LaserData', vrep.simx_opmode_streaming)

    # Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(clientID, camara, 0, vrep.simx_opmode_streaming)
    time.sleep(1)

    returnCode, signalValue = vrep.simxGetStringSignal(clientID, 'LaserData', vrep.simx_opmode_buffer)

    laserData = vrep.simxUnpackFloats(signalValue)

    puntos_x = []
    puntos_y = []

    for indice in range(0, len(laserData), 3):
        puntos_x.append(laserData[indice + 1])
        puntos_y.append(laserData[indice + 2])

    points_cluster = []

    for i in range(len(puntos_x)):
        points_cluster.append([puntos_x[i], puntos_y[i]])

    clusters = agrupar.agrupar_puntos(points_cluster)

    for cluster_idx in range(len(clusters)):
        clusters[cluster_idx] = {
            "numero_cluster": n_cluster,
            "numero_puntos": len(clusters[cluster_idx]),
            "puntosX": [punto[0] for punto in clusters[cluster_idx]],
            "puntosY": [punto[1] for punto in clusters[cluster_idx]]
        }
        n_cluster += 1

    # Creamos un np array donde guardamos el número de cluster y sus características
    caracteristicas = np.zeros((len(clusters), 3))

    i = 0
    for cluster in clusters:
        perimetro = car.calcular_perimetro(cluster)
        profundidad = car.calcular_profundidad(cluster)
        anchura = car.calcular_anchura(cluster)

        caracteristicas[i] = [perimetro, profundidad, anchura]
        i += 1

    # Usamos el predictor que tenemos en ../clasificador.pkl para cada cluster a partir de sus características.
    # Dibujamos en rojo los clusters que son piernas y en azul los que no.
    with open('../clasificador.pkl', 'rb') as f:
        clasificador = pickle.load(f)

    # Cogemos las características de los clusters
    y_pred = clasificador.predict(caracteristicas)

    # Pasamos el np a un dataframe de pandas
    df = pd.DataFrame(caracteristicas, columns=['perimetro', 'profundidad', 'anchura'])
    df['clase'] = y_pred

    # Mostramos los resultados de la predicción
    print("Predicción: ")
    print(y_pred)

    # Dibujamos los clusters. En rojo los que son piernas y en azul los que no.
    plt.clf()
    plt.axis('tight')
    plt.axis([1, 3.3, -2.15, 2.15])

    for i in range(len(df)):
        puntos_cluster = [clusters[i]["puntosX"], clusters[i]["puntosY"]]
        if y_pred[i] == 1:
            color = 'r.'        # Si es una pierna, en rojo
        else:
            color = 'b.'        # Si no es una pierna, en azul

        for j in range(len(puntos_cluster[0])):
            plt.plot(puntos_cluster[0][j], puntos_cluster[1][j], color)

        # Comprobamos la distancia con los otros clústeres
        for k in range(i + 1, len(df)):
            cluster2 = clusters[k]
            puntos_cluster2 = [cluster2["puntosX"], cluster2["puntosY"]]
            dist = distancia_entre_clusters(clusters[i], cluster2)
            if dist < 0.2:
                # Calculamos el punto medio y lo pintamos en verde
                punto_medio = punto_medio_clusteres(clusters[i], cluster2)
                plt.plot(punto_medio[0], punto_medio[1], 'g.')

    # Guardamos la imagen como predecir.jpg
    plt.savefig("predecir.jpg")

    # Volvemos al directorio padre.
    os.chdir("..")
