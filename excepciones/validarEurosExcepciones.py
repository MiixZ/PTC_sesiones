def leerFloatMax2Decimales(mensaje):
    """
    Vemos si es un digito numérico y formato 99.99. Sirve para euros e interés. Se queda pidiendo
    el dato hasta que esté correcto y devuelve el float positivo con dos decimales.
    :param mensaje: número a chequear.
    :return: valorValidado, numeroIntentosIncorrectos.
    """
    global entrada
    valorValidado = 0.0
    seguirPidiendo = True
    numeroIntentosIncorrectos = 0
    while seguirPidiendo:
        try:
            entrada = input(mensaje)
            valor = float(entrada)
            datosFloat2Decimal = entrada.split(".")

            assert valor > 0, f"El valor debe ser positivo y ha indicado {valor}"

            if len(datosFloat2Decimal) == 2:
                assert len(datosFloat2Decimal[1]) <= 2, f"Debe tener máximo dos dígitos decimales y ha indicado {valor}"

            assert datosFloat2Decimal[0].isdigit() or datosFloat2Decimal[1].isdigit(), f"Los decimales deben ser dígitos {valor}"

            valorValidado = valor
            print("CORRECTO", valor)
            seguirPidiendo = False
        except ValueError:
            print("El valor debe ser numérico, separado con . y con dos decimales como máximo y ha introducido", entrada)
            numeroIntentosIncorrectos += 1
        except AssertionError as error:
            print(error)
            numeroIntentosIncorrectos += 1

    return valorValidado, numeroIntentosIncorrectos


def leerEnteroPositivo(mensaje):
    """
    Vemos si es un digito numérico entero (sin decimales) y positivo.
    Se queda pidiendo el dato hasta que esté correcto y devuelve el entero positivo.
    :param mensaje: número a chequear.
    :return: valorValidado, numeroIntentosIncorrectos.
    """
    global entrada
    valorValidado = 0
    seguirPidiendo = True
    numeroIntentosIncorrectos = 0
    while seguirPidiendo:
        try:
            entrada = input(mensaje)
            valor = int(entrada)
            assert valor > 0, f"El valor debe ser positivo y ha indicado {valor}"

            valorValidado = valor
            print("CORRECTO", valor)
            seguirPidiendo = False
        except ValueError:
            print("El valor debe ser numérico y entero y ha introducido", entrada)
            numeroIntentosIncorrectos += 1
        except AssertionError as error:
            print(error)
            numeroIntentosIncorrectos += 1

    return valorValidado, numeroIntentosIncorrectos


if __name__=="__main__":
    nCorrectas=0
    nIncorrectas=0
    nombreEstudiante="Ismael Díaz Díaz"

    capital, nInc=leerFloatMax2Decimales("Dime capital inicial con 2 decimales máximo: ")
    print("El capital es",capital)
    nCorrectas+=1
    nIncorrectas=nIncorrectas+nInc

    interés, nInc = leerFloatMax2Decimales("Dime interés anual con 2 decimales máximo: ")
    print("El interés es",interés)
    nCorrectas+=1
    nIncorrectas=nIncorrectas+nInc

    anios, nInc = leerEnteroPositivo("Dime el número de años: ")
    print("El número de años es",anios)
    nCorrectas+=1
    nIncorrectas=nIncorrectas+nInc

    print("Fin del programa de validación de euros")
    print("Nombre estudiante: ",nombreEstudiante)
    print("Entradas correctas: ",nCorrectas," incorrectas: ",nIncorrectas)
