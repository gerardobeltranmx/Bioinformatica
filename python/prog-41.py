import csv

archivo = open("municipios.csv","r")

entrada = csv.reader(archivo)

for registro in entrada:
    print(registro[1])

archivo.close()    

