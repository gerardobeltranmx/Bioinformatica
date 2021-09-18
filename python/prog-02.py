# este es el valor de PI
PI = 3.141592
# escriba aqui el radio del circulo
radio = float(input("Dame el radio del circulo: "))
# radio = int(radio)
area = PI * radio ** 2
perimetro = 2 * PI * radio
# print("El area del circulo es %.1f" % area)
# print("El perimetro del circulo es %.3f" % perimetro)

print("Para un radio de %.2f el area es %.3f y el perimetro es %.2f"  % (radio, area, perimetro))
print("Para un radio de", radio, "el area es", area, "y el perimetro es", perimetro)




