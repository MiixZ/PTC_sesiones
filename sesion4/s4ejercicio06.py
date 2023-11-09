"""
Solicitar un número entero N por teclado e implentar una función que devuelva una lista con la
descomposición en factores primos de N. Mostrar el resultado por pantalla.
"""


def es_primo(numero_a_comprobar):
    """Comprueba si un número es primo.
    numero_a_comprobar: int
    return: bool"""
    for i in range(2, numero_a_comprobar):
        if numero_a_comprobar % i == 0:
            return False
    return True


def lista_primos(numero_a_descomponer):
    """Devuelve una lista con los factores primos de un número.
    numero_a_descomponer: int
    return: list"""
    lista = []
    for i in range(2, numero_a_descomponer + 1):
        if es_primo(i):
            while numero_a_descomponer % i == 0:
                lista.append(i)
                numero_a_descomponer //= i
    return lista


N = int(input("Introduzca un número: "))
print("La descomposición en factores primos de", N, "es", lista_primos(N))
