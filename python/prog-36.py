archivo = open("datos.txt", "r")

linea = archivo.readline()

while linea:
    print(linea, end="")
    linea = archivo.readline()
    
archivo.close()

