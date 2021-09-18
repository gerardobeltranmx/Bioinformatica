# Calculo del volumen y superfice de un cilindro
# 17-Sep-2021
# Gerardo Beltrán

# Entrada
altura = float(input("Indicar la altura: "))
radio  = float(input("Indicar el radio de la base: "))

# Procesos
PI = 3.141592
volumen = (PI * radio ** 2) * altura
superficie = 2 * PI * radio * altura

# Salida
print("El volumen es: %.2f" % volumen)
print("La superficie  es: %.2f" % superficie)
 



  

