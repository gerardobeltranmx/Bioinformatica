cadena = input("Indicar la cadena")
# Convertir a minusculas toda la cadena
cadena = cadena.lower()

cuentaA = cadena.count("a")
cuentaE = cadena.count("e")
cuentaI = cadena.count("i")
cuentaO = cadena.count("o")
cuentaU = cadena.count("u")

total = cuentaA + cuentaE + cuentaI + cuentaO + cuentaU

print("numero de vocales es", total)



