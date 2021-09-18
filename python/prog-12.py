# Determina el tipo de triangulo

lado1 = int(input("Indicar el lado 1: "))
lado2 = int(input("Indicar el lado 2: "))
lado3 = int(input("Indicar el lado 3: "))


if (lado1==lado2) and (lado2==lado3) :
    print("El triangulo es equilatero!!!")
elif (lado1==lado2) or (lado2==lado3) or (lado3==lado1):
    print("El triangulo es isosceles!!!")
else:
    print("El triangulo es escaleno!!!")
