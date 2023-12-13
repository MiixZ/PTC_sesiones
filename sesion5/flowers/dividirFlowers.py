"""En este ejercicio vamos a organizar un dataset para clasificación de flores en varias carpetas.
Como datos de entrada se proporciona la carpeta “dataset” que contiene 80 imágenes de
cada uno de 17 tipos de flores, en total 1360 imágenes numeradas de 1 a 1360 y un fichero
“classes.txt” donde viene el nombre de cada clase. Cada 80 imágenes pertenecen a cada una
de las 17 clases listadas en el fichero “classes.txt” según en el orden en el que aparecen en
dicho fichero. Es decir, en “classes.txt” la primera clase se llama “daffodil” (narciso), por
tanto las imágenes image_0001.jpg a image_0080.jpg son narcisos. Del image_0081.jpg a
image_0160.jpg son “snowdrop“(campanillas) y así sucesivamente.
Hay que implementar un programa en Python que sea capaz de crear una carpeta por cada
clase y copiar sus correspondientes imágenes a la vez que se renombran a
"image_9999_clase_n.jpg". Es decir dentro de “daffodil” se deberían llamar
image_0001_daffodil_1.jpg a image_0080_daffodil_80.jpg y así con cada clase.
Para realizar este ejercicio se recomienda usar los módulos glob y os de los cuales tenéis
ejemplos en los script proporcionados de la práctica 2 Tkinter y Robótica. El dataset se
encuentra en Prado. Antes de realizar la entrega se debe corregir el ejercicio con los ficheros
de la carpeta Corregir ejercicio Flowers de Prado. El script a entregar se debe llamar
“dividirFlowers.py”"""

import os

# Path a la carpeta dataset
dataset_dir = 'dataset'
actual_dir = os.getcwd()

# Leer las clases del fichero
with open(dataset_dir + '/classes.txt', 'r') as f:
    classes = [line.strip() for line in f]

# Para cada clase
for i, class_name in enumerate(classes):
    # Crea un directorio por clase si no existe
    class_dir = os.path.join(actual_dir, class_name)
    os.makedirs(class_dir, exist_ok=True)

    # Rango de imágenes
    start = i * 80 + 1
    end = start + 80

    # Para cada imagen
    for j in range(start, end):
        # Cogemos el nombre viejo y le añadimos el nombre de la clase y el número de imagen.
        old_image_name = f'image_{j:04d}.jpg'
        new_image_name = f'image_{j:04d}_{class_name}_{j - start + 1}.jpg'

        # Cogemos la ruta de la imagen vieja y la nueva
        old_image_path = os.path.join(dataset_dir, old_image_name)
        new_image_path = os.path.join(class_dir, new_image_name)

        # Copiamos la imagen vieja en la nueva
        os.system(f'copy {old_image_path} {new_image_path}')        # Windows
        # os.system(f'cp {old_image_path} {new_image_path}')        # Linux
