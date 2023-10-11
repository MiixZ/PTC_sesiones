import financiacion

euros = financiacion.leerFloat2decimales()
interes = financiacion.leerFloat2decimales()
anios = financiacion.leerInt()

capital = float(euros)
for i in range(anios):
    capital = financiacion.calcularCapitalAnual(capital, float(interes))
    print("Capital tras ", i + 1, " años: ", capital)
