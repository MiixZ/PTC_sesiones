"""Programa con una función que compruebe
 que los datos introducidos (en euros) cumplen con
 las condiciones: Sólo caracteres numéricos pero usando el "." :para
 separar los decimales. Un máximo de dos decimales."""

def comprobarEuros(euros):
    """Comprueba que los euros introducidos son correctos.
    euros: float
    return: bool"""
    euros = str(euros)
    datosEurosDecimales = euros.split(".")

    if len(datosEurosDecimales) == 2:
        if datosEurosDecimales[0].isdigit() and datosEurosDecimales[1].isdigit() and len(datosEurosDecimales[1]) <= 2:
            return True
        else:
            return False
    elif len(datosEurosDecimales) == 1:
        if datosEurosDecimales[0].isdigit():
            return True
        else:
            return False
    else:
        return False

"El programa principal será un bucle que vaya leyendo los euros introducidos periodicamente y diga si son correctos o no"
dentro = True
while dentro:
    datos = input("Introduzca los euros: ")
    if comprobarEuros(datos):
        print("Los euros son correctos.")
    else:
        print("Los euros son incorrectos.")

    if datos == "fin":
        dentro = False