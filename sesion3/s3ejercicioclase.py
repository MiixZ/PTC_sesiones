# Una función que compruebe si el valor que se pasa por parámetro es una copia o una referencia

def isReference(prueba):
    prueba+=2
    print(id(prueba))

lista = 1

isReference(lista)

print(id(lista))