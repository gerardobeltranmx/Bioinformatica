# Clasificación Climaticas

temp = float(input("Dame la temperatura: "))

if temp<0:
    print("Muy Frio")
elif temp>=0 and temp<=10:
    print("Frio")
elif  temp>=11 and temp<=20:
    print("Templado")
elif temp>=21 and temp<=25:
    print("Calido")
else:
    print("Muy Calido")

print("La temperatura es:", temp)
