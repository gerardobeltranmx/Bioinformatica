cmInicio = int(input("Indicar centimetros inicial: "))
cmFin = int(input("Indicar centimetros final: "))
print ("Centimetros      Metros        Yardas        Pulgadas")
i = cmInicio
while i <= cmFin:
    metros = i / 100
    yardas = i / 91.44
    pulgadas = i / 2.54
    print("%11d      %6.2f        %6.2f       %9.2f" % (i, metros, yardas, pulgadas))
    i = i + 1
