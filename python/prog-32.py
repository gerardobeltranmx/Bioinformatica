cadena = "##ATGCAAATTGTGTGTGCATAATTTATATAGG$CTAGAATAGAATC$G$CTA##"
seg = "GC"

cadena = cadena.strip("#")

cadena = cadena.replace("$", "")

num = cadena.count("GC")
tam = len(cadena) / 2
porcentaje = num / tam *100
print("El porcentaje es %.2f" % porcentaje)





