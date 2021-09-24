numDolares = int(input("Numero de Dolares:"))
tipoCambio = float(input("Tipo de cambio:"))

i = 1

while i <=numDolares :
    pesos = i * tipoCambio
    print ("%d <-------------->  %.2f" % (i, pesos))
    i = i + 1
