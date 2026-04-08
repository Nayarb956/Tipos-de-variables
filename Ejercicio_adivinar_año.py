#Algoritmo para adivinar el año en el que nacio por medio de la edad y el año en el que estamos

# Pedir al usuario que ingrese su nombre y edad

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Pedir al usuario que ingrese el año en el que estamos

año_actual = int(input("Ingresa el año en el que estamos: "))

# Calcular el año de nacimiento

año_nacimiento = año_actual - edad
año_nacimiento2 = año_actual - edad - 1

# Mostrar el resultado al usuario

print(f"{nombre}, tu año de nacimiento es: {año_nacimiento} - {año_nacimiento2} (dependiendo de si ya cumpliste años este año o no)")