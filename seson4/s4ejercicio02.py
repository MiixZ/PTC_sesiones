"""
Crea una lista con los valores enteros de 1 a N e implementa una función que reciba dicha lista y
nos devuelva una lista con los valores impares y el número de dichos valores. Solicitar N por
teclado y mostrar el resultado por pantalla.
"""


def impares_lista(lista_a_comprobar):
    """Devuelve una lista con los valores impares de una lista y el número de dichos valores.
    lista: list
    return: list"""
    lista_impares = []
    for i in lista_a_comprobar:
        if i % 2 != 0:
            lista_impares.append(i)
    return lista_impares, len(lista_impares)


N = int(input("Introduzca un número: "))
lista = list(range(1, N + 1))

print("La lista de impares de la lista", lista, "es", impares_lista(lista)[0], "y hay",
      impares_lista(lista)[1], "impares.")


# Segunda versión usando filter()
def impares_lista2(lista_a_comprobar):
    """Devuelve una lista con los valores impares de una lista y el número de dichos valores.
    Lambda se utiliza para definir una función anónima (de una línea) que se utiliza en el filter.
    En este caso devuelve true si el número es impar.
    lista: list
    return: list"""
    lista_impares = list(filter(lambda x: x % 2 != 0, lista_a_comprobar))
    return lista_impares, len(lista_impares)


N = int(input("Introduzca un número: "))
lista = list(range(1, N + 1))

print("La lista de impares de la lista", lista, "es", impares_lista2(lista)[0], "y hay",
      impares_lista2(lista)[1], "impares.")
