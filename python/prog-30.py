cadena = input("Indicar la cadena: ")
# Convertir a minusculas toda la cadena
cadena = cadena.lower()
cadena = cadena.replace(" ","")
cuentaA = cadena.count("a")
cuentaE = cadena.count("e")
cuentaI = cadena.count("i")
cuentaO = cadena.count("o")
cuentaU = cadena.count("u")

totalVocales = cuentaA + cuentaE + cuentaI + cuentaO + cuentaU

total = len(cadena)

totalConsonantes = total - totalVocales

print("La cadena tiene %d vocales y %d consonantes" % (totalVocales, totalConsonantes) )



