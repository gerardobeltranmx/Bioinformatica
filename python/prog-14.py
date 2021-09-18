# Calculo del indice de masa corporal IMC

# Entrada de datos
peso = float (input("Indicar el peso (kilos): "))
altura = float (input("Indicar la altura (metros): "))

IMC = peso / (altura**2)

print("El IMC es: ", IMC)

if (IMC < 18.5):
    print("Bajo peso")
elif (IMC >=18.5 and IMC<=24.9):
    print("Peso normal")
elif (IMC>=25.0 and IMC<=29.9 ):
    print("Sobrepeso")
else:
    print("Obesidad")


