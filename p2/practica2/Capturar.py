import math
import os
import json
import random
import cv2
from matplotlib import pyplot as plt
import sim as vrep  # Al final cambiarlo por import vrep
import parametros as p
import time
import numpy as np

# VARIABLES
tiempo_espera = 0.5  # Tiempo de espera entre iteraciones en segundos
clientID = 0  # Identificador de la conexión con el simulador


def main(file_path):
    # ROBOTS
    # Obtener el handler del robot
    _, robot = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)

    directorio = file_path.split("/")[0]
    fichero = file_path.split("/")[1]

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

    velocidad = 0

    # Obtener el handler de la persona
    if "enPie" in fichero:
        nombre = 'Bill#0'
        y = 0
        z = 0
    elif "sentado" in fichero:
        nombre = 'Bill'
        y = 0
        z = 0
    elif "cilindroMenor" in fichero:
        nombre = 'Cylinder'
        y = 0
        z = 0.25
    else:
        nombre = 'Cylinder2'
        y = 0
        z = 0.25

    _, objeto = vrep.simxGetObjectHandle(clientID, nombre, vrep.simx_opmode_oneshot_wait)

    # Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(clientID, camara, 0, vrep.simx_opmode_streaming)
    time.sleep(1)

    plt.axis('equal')
    plt.axis([0, 4, -2, 2])

    os.chdir(directorio)

    cabecera = {
        "TiempoSleep": tiempo_espera,
        "MaxIteraciones": p.iteracciones
    }

    f_json = open(fichero, "w")
    f_json.write(json.dumps(cabecera) + '\n')

    seguir = True
    i = 1

    if "Cerca" in fichero:
        minimo = p.cerca
        maximo = p.media
    elif "Media" in fichero:
        minimo = p.media
        maximo = p.lejos
    else:
        minimo = p.lejos
        maximo = p.lejos + 1

    orientacion_inicial = random.uniform(-math.pi, math.pi)

    while i <= p.iteracciones and seguir:
        # Genera dos números aleatorios entre p.cerca y p.media para las coordenadas x e y
        x = random.uniform(minimo, maximo)

        # Calcula la nueva posición de la persona
        nueva_posicion = [x, y, z]

        # Mueve a la persona a la nueva posición
        returnCode = vrep.simxSetObjectPosition(clientID, objeto, -1, nueva_posicion, vrep.simx_opmode_oneshot)

        # Genera un número aleatorio entre -π y π
        cambio_orientacion = random.uniform(-math.pi, math.pi)

        # Cambiamos la orientación, ojo está en radianes
        returnCode = vrep.simxSetObjectOrientation(clientID, objeto, -1, [0.0, 0.0, cambio_orientacion],
                                                   vrep.simx_opmode_oneshot)

        time.sleep(tiempo_espera)

        # Guardamos los datos del laser
        puntos_x = []
        puntos_y = []
        puntos_z = []

        returnCode, signalValue = vrep.simxGetStringSignal(clientID, 'LaserData', vrep.simx_opmode_buffer)

        datosLaser = vrep.simxUnpackFloats(signalValue)

        for indice in range(0, len(datosLaser), 3):
            puntos_x.append(datosLaser[indice + 1])
            puntos_y.append(datosLaser[indice + 2])
            puntos_z.append(datosLaser[indice])

        # Guardamos los datos de la camara
        plt.clf()
        plt.plot(puntos_x, puntos_y, 'ro')

        if i == 1 or i == p.iteracciones:
            plt.savefig('Plot' + str(i - 1) + '.jpg')

        print("Iteración: ", i)

        lectura = {
            "Iteracion": i,
            "PuntosX": puntos_x,
            "PuntosY": puntos_y
        }

        f_json.write(json.dumps(lectura) + '\n')

        _, resolution, image = vrep.simxGetVisionSensorImage(clientID, camara, 0, vrep.simx_opmode_buffer)
        img = np.array(image, dtype=np.uint8)
        img.resize([resolution[0], resolution[1], 3])
        img = np.rot90(img, 2)
        img = np.fliplr(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if i == 1 or i == p.iteracciones:
            nombre_imagen = fichero.split(".")[0]
            cv2.imwrite(nombre_imagen + str(i - 1) + '.jpg', img)

        cv2.imshow('Imagen', img)

        tecla = cv2.waitKey(5) & 0xFF
        if tecla == 27:
            seguir = False

        i += 1

    finFichero = {
        "Iteraciones totales": i - 1
    }

    f_json.write(json.dumps(finFichero) + '\n')
    f_json.close()
