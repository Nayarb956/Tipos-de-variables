# Un parque de diversiones cobra la entrada segun la edad, menor de 3 años entran gratis, de 3 a 12 años, pagan 8 mil, de 13 a 60 años pagan 15 mil y mayores de 60 pagan 10 mil
# Si la edad es un valor imposible o incredible, el programa debe de mostrar un mensaje de error y no mostrar el resultado del cobro. (Ejemplo: edad negativa, edad mayor a 122 años)

edad = int(input("Ingrese la edad del visitante: "))

dia = input("¿Qué día de la semana es hoy?: ").lower() 

if edad < 0 or edad > 122:
 print("Error: Por favor ingrese una edad válida.")
		
elif edad < 3:
 print("La entrada es gratuita.")
elif edad <= 12:
 print("La entrada cuesta $8,000")
		
elif edad <= 60:
 print("La entrada cuesta $15,000")
		
else:
 print("La entrada cuesta $10,000")


# Si es "Miercoles", todos los precios tienen un 20% de descuento, sin importar la edad (excepto los que entran gratis). El programa debe de solicitar el día de la semana y mostrar el precio con el descuento aplicado si es necesario. Si el día ingresado no es un día válido, el programa debe de mostrar un mensaje de error y no mostrar el resultado del cobro. 


if dia.lower() == "miercoles":

	if edad <= 12:
		print("Con el descuento del 20% para el dia miercoles, la entrada cuesta $6,400")
		
	elif edad <= 60:
		print("Con el descuento del 20% para el dia miercoles, la entrada cuesta $12,000")
		
	else:
		print("Con el descuento del 20% para el dia miercoles, la entrada cuesta $8,000")