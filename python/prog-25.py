numDolares = int(input("Numero de Dolares:"))
tipoCambio = float(input("Tipo de cambio:"))


for i in range(1,numDolares+1):
    pesos = i * tipoCambio
    print("%d  <================>  %.2f" % (i, pesos))
