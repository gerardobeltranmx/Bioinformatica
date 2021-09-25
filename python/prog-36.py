import sys
nombre = sys.argv[1]
archivo = open(nombre, "r")

linea = archivo.readline()

while linea:
    print(linea, end="")
    linea = archivo.readline()
    
archivo.close()

