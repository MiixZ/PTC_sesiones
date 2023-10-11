"""Escribe una función inicio_fin_vocal(palabra) que determine si una palabra empieza y acaba con una vocal."""

def inicio_fin_vocal(palabra):
    """Determina si una palabra empieza y acaba con una vocal.
    palabra: str
    return: bool"""
    return palabra[0] in "aeiouAEIOU" and palabra[-1] in "aeiouAEIOU"

"Segunda versión de la función utilizando .startswith y .endswith"
def inicio_fin_vocal2(palabra):
    """Determina si una palabra empieza y acaba con una vocal.
    palabra: str
    return: bool"""
    return (palabra.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")) and
            palabra.endswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")))

palabra1 = input("Introduzca una palabra: ")

if inicio_fin_vocal(palabra1):
    print("La palabra", palabra1, "empieza y acaba con una vocal.")
else:
    print("La palabra", palabra1, "no empieza y acaba con una vocal.")

if inicio_fin_vocal2(palabra1):
    print("La palabra", palabra1, "empieza y acaba con una vocal.")
else:
    print("La palabra", palabra1, "no empieza y acaba con una vocal.")
