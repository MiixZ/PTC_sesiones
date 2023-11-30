"""
Realizar un programa que muestre un menú de opciones al usuario con las siguientes operaciones
sobre una lista que inicialmente está vacía: 1) Insertar un entero positivo (debe insertarlo en orden
ascendente), 2) Eliminar un valor de la lista dado el entero positivo, 3) Eliminar un valor dada su
posición, 4) Salir. Después de cada operación se debe siempre mostrar al usuario el estado de la
lista y se deben controlar las posibles situaciones de error informando al usuario de dicho error y
volviendo a solicitar la entrada correspondiente.
"""

# -*- coding: utf-8 -*-


def esta_ordenada_ascendente(lista):
    """Comprueba si una lista está ordenada de forma ascendente.
    lista: list
    return: bool"""
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


lista = []
seguir = True

while seguir:
    print("\n1) Insertar un entero positivo\n" + 
          "2) Eliminar un valor de la lista dado el entero positivo\n" + 
          "3) Eliminar un valor dada su posición\n" + 
          "4) Finalizar\n")
    
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        intentando = True
        while intentando:
            try:
                num = int(input("Introduce un entero positivo: "))
                if num < 0: raise ValueError("El número debe ser positivo")
                lista.append(num)

                if esta_ordenada_ascendente(lista):
                    print("Número insertado correctamente")
                    intentando = False
                else:
                    lista.remove(num)
                    raise ValueError("La lista no estaría ordenada de forma ascendente", lista)        
            except ValueError as e:
                print("Error: ", e)

    elif opcion == 2:
        intentando = True
        while intentando:
            try:
                num = int(input("Introduce el entero a eliminar: "))
                if num < 0: raise ValueError("El número debe ser positivo")

                if num not in lista:
                    raise ValueError("El número no está en la lista")
                else:
                    intentando = False
                    lista.remove(num)
                    print("Número eliminado correctamente")
            except ValueError as e:
                print("Error: ", e)

    elif opcion == 3:
        intentando = True
        while intentando:
            try:
                pos = int(input("Introduce la posición a eliminar: "))
                if pos < 0: raise ValueError("El número debe ser positivo")
                if pos > len(lista): raise ValueError("La posición está fuera de rango")

                lista.remove(lista[pos])
                print("Posición eliminada correctamente")
                intentando = False
            except ValueError as e:
                print("Error: ", e)
    elif opcion == 4:
        print("Finalizando...")
        seguir = False
    else:
        print("Opción no válida")

    print("Estado de la lista: ", lista)