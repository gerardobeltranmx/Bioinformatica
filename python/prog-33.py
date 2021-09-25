cadena = "ATgCAAATTGTGTGTGCaTAaTTTATATAGgCTAGAATAGAATC$g$CTA"
seg = "GC"

cadena = cadena.replace("$", "")

cadena = cadena.upper()

num = cadena.count("GC")
tam = len(cadena) / 2
porcentaje = num / tam *100
print(cadena)
print("El porcentaje es %.2f" % porcentaje)





