import csv

archivo = open("municipios.csv","r")

entrada = csv.reader(archivo)

for nombre, poblacion, superfice in entrada:
    print(nombre, poblacion, superfice)

archivo.close()    