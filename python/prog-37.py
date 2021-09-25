import sys

archivo = open(sys.argv[1],"r")

for linea in archivo:
    print(linea, end="")

archivo.close()

