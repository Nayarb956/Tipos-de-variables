# Tipos de variables

nombre = "Carlos" # str
edad = 30 # int
altura = 1.75 # float
es_estudiante = True # bool

print(f"Nombre: {nombre} (Tipo: {type(nombre)})")
print(f"Edad: {edad} (Tipo: {type(edad)})")

# Entrada de un bar, si es mayor de edad entra, si no es mayor de edad no entra

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
mayor_de_edad = edad >= 18
estatura = float(input("Ingresa tu estatura en metros: "))

print(f"\nResumen de datos:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"¿Es mayor de edad? {mayor_de_edad}")
print(f"Estatura: {estatura:.2f} metros")