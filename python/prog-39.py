import sys
# Operaciones con archivos Fasta

archivo = open(sys.argv[1], "r")

buscar = sys.argv[2]
contar = 0

for linea in archivo:
    contar = contar + linea.count(buscar)
    #print(linea, end="")


print("la subcadena se encontro %d veces " % (contar))
archivo.close()


