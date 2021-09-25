import csv
archivoCSV=open("clientes.csv")
entrada = csv.DictReader(archivoCSV)
for reg in entrada:
    print(reg['Nombre'], reg['Edad'], reg['Estatura'])