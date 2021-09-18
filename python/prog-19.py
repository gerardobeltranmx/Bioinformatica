# numeros divisibles 

inicio = int(input("Valor inicial: "))
fin = int(input("Valor final: "))

cuenta = 0
for  valor in range(inicio, fin+1):
    if (valor % 2 == 0):
         print(valor)
         cuenta = cuenta + 1 

print("son %d numeros divisibles" % cuenta)
