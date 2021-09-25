import csv
archivoCSV=open("municipios.csv")
entrada = csv.DictReader(archivoCSV)
for reg in entrada:
    print(reg['nombre'], reg['poblacion'], reg['superfice'])