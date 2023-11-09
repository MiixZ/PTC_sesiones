"""
Crea una lista con los valores enteros de 1 a N e implementa una función que reciba dicha lista y
nos devuelva el máximo y el mínimo de dichos valores, así como sus respectivas posiciones.
Solicitar N por teclado y mostrar el resultado por pantalla.
"""


def max_min_lista(lista_a_comprobar):
    """Devuelve el máximo y el mínimo de una lista, así como sus respectivas posiciones.
    lista: list
    return: int, int, int, int"""
    maximo = lista_a_comprobar[0]
    minimo = lista_a_comprobar[0]
    posicion_maximo = 0
    posicion_minimo = 0
    for i in range(1, len(lista_a_comprobar)):
        if lista_a_comprobar[i] > maximo:
            maximo = lista_a_comprobar[i]
            posicion_maximo = i
        if lista_a_comprobar[i] < minimo:
            minimo = lista_a_comprobar[i]
            posicion_minimo = i
    return maximo, posicion_maximo, minimo, posicion_minimo


N = int(input("Introduzca un número: "))
lista = list(range(1, N + 1))

print("El máximo de la lista", lista, "es", max_min_lista(lista)[0], "y está en la posición",
      max_min_lista(lista)[1])

print("El mínimo de la lista", lista, "es", max_min_lista(lista)[2], "y está en la posición",
      max_min_lista(lista)[3])


# Segunda versión usando max(), min() e index()
def max_min_lista2(lista_a_comprobar):
    """Devuelve el máximo y el mínimo de una lista, así como sus respectivas posiciones.
    lista: list
    return: int, int, int, int"""
    maximo = max(lista_a_comprobar)
    minimo = min(lista_a_comprobar)
    posicion_maximo = lista_a_comprobar.index(maximo)
    posicion_minimo = lista_a_comprobar.index(minimo)
    return maximo, posicion_maximo, minimo, posicion_minimo


N = int(input("Introduzca un número: "))
lista = list(range(1, N + 1))

print("El máximo de la lista", lista, "es", max_min_lista2(lista)[0], "y está en la posición",
      max_min_lista2(lista)[1])

print("El mínimo de la lista", lista, "es", max_min_lista2(lista)[2], "y está en la posición",
      max_min_lista2(lista)[3])
