cadena = input("Indicar la cadena: ")
# Convertir a minusculas toda la cadena
cadena = cadena.lower()

cuenta = 0
for c in cadena : 
    if c in "aeiou" :
        cuenta = cuenta + 1


print("El numero de vocales es:", cuenta)


