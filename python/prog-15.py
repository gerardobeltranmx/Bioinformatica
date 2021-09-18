# Calcular la calificacion de Eduardo

califExamenFinal = float(input("Calificación Examen Final: "))
califParcial1 = float(input("Calificación Parcial 1: "))
califParcial2 = float(input("Calificación Parcial 2: "))
califTareas = float(input("Calificación de Tareas: "))
califProyecto = float(input("Calificación de Proyecto: "))

resultado = 0.25 * califExamenFinal + 0.25 * califParcial1 + 0.25 * califParcial2 
resultado = resultado +  0.10 * califTareas +  0.15 * califProyecto

print("La calficacion final es: ", resultado)

if (resultado>=6):
   print("Aprobado")
else:
   print("No Aprobado")

