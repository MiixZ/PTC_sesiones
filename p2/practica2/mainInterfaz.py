# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import parametros as p
import sim as vrep  # Al final cambiarlo por import vrep
import os


# FUNCIONES
def conectar():
    # Iniciar la conexión con el simulador
    clientID = vrep.simxStart('127.0.0.1', 19999, True,
                              True, 5000, 5)

    # Comprobar si la conexión fue exitosa
    if clientID != -1:
        boton_desconectar.config(state="normal")  # Habilita el botón Desconectar
        boton_capturar.config(state="normal")  # Habilita el botón Capturar
        estado.config(text="Estado: Conectado a CoppeliaSim")
        messagebox.showinfo("Conexión", "Conexión con CoppeliaSim establecida.")
    else:
        messagebox.showerror("Error", "Debe iniciar el simulador.")


def desconectar():
    boton_conectar.config(state="normal")  # Habilita el botón Conectar
    boton_desconectar.config(state="disabled")  # Deshabilita el botón Desconectar
    estado.config(text="Estado: No conectado a CoppeliaSim")


def mostrar_parametros():
    # Crear una nueva ventana
    ventana = tk.Toplevel(root)

    # Crear y empaquetar etiquetas para cada parámetro
    tk.Label(ventana, text="Nuevos valores de los parámetros:").pack()
    tk.Label(ventana, text="Iteraciones: " + str(p.iteracciones)).pack()
    tk.Label(ventana, text="Cerca: " + str(p.cerca)).pack()
    tk.Label(ventana, text="Media: " + str(p.media)).pack()
    tk.Label(ventana, text="Lejos: " + str(p.lejos)).pack()
    tk.Label(ventana, text="MinPuntos: " + str(p.MinPuntos)).pack()
    tk.Label(ventana, text="MaxPuntos: " + str(p.MaxPuntos)).pack()
    tk.Label(ventana, text="UmbralDistancia: " + str(p.UmbralDistancia)).pack()


def cambiar():
    global entries
    p.iteracciones = int(entries[0].get())
    p.cerca = float(entries[1].get())
    p.media = float(entries[2].get())
    p.lejos = float(entries[3].get())
    p.MinPuntos = int(entries[4].get())
    p.MaxPuntos = int(entries[5].get())
    p.UmbralDistancia = float(entries[6].get())

    # Imprimir los nuevos valores de los parámetros
    mostrar_parametros()


def capturar():
    # Comprobar si se ha seleccionado un archivo
    seleccion = ficheros.curselection()
    if not seleccion:  # Si la tupla está vacía
        messagebox.showwarning("Warning", "Debe elegir un fichero de la lista.")
        return

    # Obtener el nombre del archivo seleccionado
    archivo_seleccionado = ficheros.get(seleccion[0])

    # Obtener el directorio del archivo seleccionado
    directorio = os.path.dirname(archivo_seleccionado)

    # Comprobar si el directorio existe y crearlo si no existe
    if not os.path.isdir(directorio):
        os.makedirs(directorio)

    # Comprobar si el archivo ya existe
    if os.path.exists(archivo_seleccionado):
        respuesta = messagebox.askyesno("Pregunta",
                                        "El fichero: " + archivo_seleccionado + " ya existe. Se creará uno nuevo " +
                                        "¿Está seguro?")
        if respuesta:
            os.remove(archivo_seleccionado)

    else:
        respuesta = messagebox.askyesno("Pregunta",
                                        "Se va a crear el fichero: " + archivo_seleccionado + ". ¿Está seguro?")

    # Si el usuario seleccionó "No", retornar sin hacer nada más
    if not respuesta:
        return
    else:
        # Crear el archivo
        with open(archivo_seleccionado, 'w') as f:
            f.close()

    # Ejecutar el script Capturar.py con el archivo seleccionado y los parámetros actuales.
    print("Archivo seleccionado: ", archivo_seleccionado)


# VENTANA PRINCIPAL
root = tk.Tk()  # crea la ventana principal

# VARIABLES
conectado = False
width_box = 5

# COLUMNAS USADAS DE 0 a 3, FILAS DE 0 a 9
root.geometry("700x300")  # anchura x altura
root.title("Práctica PTC Tkinter Robótica")  # título de la ventana

# LABELS
conexion = tk.Label(root, text="Es necesario conectar el simulador CoppeliaSim")
parametros = tk.Label(root, text="Parámetros")
ficheros = tk.Label(root, text="Ficheros para la captura")

estado = tk.Label(root, text="Estado: No conectado a CoppeliaSim")

# GRID PARA LABELS
conexion.grid(row=0, column=0)
parametros.grid(row=1, column=1, sticky='e')
ficheros.grid(row=1, column=3)

estado.grid(row=3, column=0)

# BOTONES PARA COLUMNA 0
boton_conectar = tk.Button(root, text="Conectar con CoppeliaSim", command=conectar)
boton_conectar.grid(row=1, column=0)  # Ajusta la fila y columna según sea necesario

boton_desconectar = tk.Button(root, text="Detener y desconectar CoppeliaSim", command=desconectar, state="disabled")
boton_desconectar.grid(row=2, column=0)  # Ajusta la fila y columna según sea necesario

boton_capturar = tk.Button(root, text="Capturar", command=capturar, state="disabled")
boton_agrupar = tk.Button(root, text="Agrupar", command=desconectar, state="disabled")
boton_extraer = tk.Button(root, text="Extraer características", command=desconectar, state="disabled")
boton_entrenar = tk.Button(root, text="Entrenar clasificador", command=desconectar, state="disabled")
boton_predecir = tk.Button(root, text="Predecir", command=desconectar, state="disabled")
boton_salir = tk.Button(root, text="Salir", command=root.destroy)

boton_capturar.grid(row=4, column=0)
boton_agrupar.grid(row=5, column=0)
boton_extraer.grid(row=6, column=0)
boton_entrenar.grid(row=7, column=0)
boton_predecir.grid(row=8, column=0)
boton_salir.grid(row=9, column=0)

# LABELS y BOTON PARA LA COLUMNA 1
label_texts = ["Iteraciones: ", "Cerca: ", "Media: ", "Lejos: ", "MinPuntos: ", "MaxPuntos: ", "UmbralDistancia: "]

for i, text in enumerate(label_texts):
    label = tk.Label(root, text=text)
    label.grid(row=i + 2, column=1, sticky='e')

boton_cambiar = tk.Button(root, text="Cambiar", command=cambiar)
boton_cambiar.grid(row=9, column=1)

# TEXTBOX PARA LA COLUMNA 2
entry_names = ["iteraciones", "cerca", "media", "lejos", "MinPuntos", "MaxPuntos", "UmbralDistancia"]
default_values = [p.iteracciones, p.cerca, p.media, p.lejos, p.MinPuntos, p.MaxPuntos, p.UmbralDistancia]
entries = []  # Lista de los entrys

for i, name in enumerate(entry_names):
    entry = tk.Entry(root, width=width_box)
    entry.insert(0, str(default_values[i]))
    entry.grid(row=i + 2, column=2)
    entries.append(entry)

# LISTBOX PARA LA COLUMNA 3
file_names = [
    "positivo1/enPieCerca.json", "positivo2/enPieMedia.json", "positivo3/enPieLejos.json",
    "positivo4/sentadoCerca.json", "positivo5/sentadoMedia.json", "positivo6/sentadoLejos.json",
    "negativo1/cilindroMenorCerca.json", "negativo2/cilindroMenorMedia.json", "negativo3/cilindroMenorLejos.json",
    "negativo4/cilindroMayorCerca.json", "negativo5/cilindroMayorMedia.json", "negativo6/cilindroMayorLejos.json"
]

ficheros = tk.Listbox(root, width=35, height=12)
for file_name in file_names:
    ficheros.insert(tk.END, file_name)
ficheros.grid(row=3, column=3, rowspan=6)

root.mainloop()
