municipios = open("municipios.txt","r")
sumaPoblacion = 0
sumaSuperficie = 0
for municipio in municipios :
    datos = municipio.split(",")
    poblacion = int(datos[1])
    superficie = int(datos[2])
    sumaPoblacion = sumaPoblacion + poblacion
    sumaSuperficie = sumaSuperficie + superficie
   
print("La población de Sinaloa es: ", sumaPoblacion)
print("La superficie de Sinaloa es: ", sumaSuperficie)




municipios.close()


