# Crear un sistema de evaluación de notas de 1 a 5 a los estudiantes usando el if, elif y else.

# El programa debe de solicitar solamente la nota del estudiante, si la nota es mayor o igual que a 3, el estudiante pasa la materia, si es mayor o igual que a 2 pasa a recuperación de la materia, y si es menor que 2 pierde la materia.

# Agregar comentario sobre la nota del estudiante, si es mayor o igual a 4.5 es excelente, si es mayor o igual a 4 es muy bueno, si es mayor o igual a 3.5 es bueno, si es mayor o igual a 3 es suficiente, si es mayor o igual a 2.5 es insuficiente, y si es menor que 2.5 es deficiente.

# Si el estudiante pone una nota invalida, ya sea menor que 0 o mayor que 5 el programa debe de mostrar un mensaje de error y no mostrar el resultado de la evaluación.


nota = float(input("Ingrese la nota del estudiante (0.0 - 5.0): "))

if nota < 0 or nota > 5:
 print("\nError: Nota inválida. Por favor ingrese una nota entre 0.0 y 5.0.")

if nota >= 3 and nota <= 5:
 print("\nAprobado.")

elif nota >= 2 and nota < 3:
 print("\nRecuperación.")

elif nota > 5 or nota < 0:
    print("\nNo se puede evaluar la nota debido a que es inválida.")
    
    
else:
 print("\nReprobado.")

if nota > 5 or nota < 0:
 print("\nIntente nuevamente con una nota válida.")

if nota >= 4.5 and nota <= 5:
 print("\nComentario: Excelente.")

elif nota >= 4 and nota < 4.5:
 print("\nComentario: Bien hecho")

elif nota >= 3.5 and nota < 4:
 print("\nComentario: Suficiente.")

elif nota >= 2.5 and nota < 3.5:
 print("\nComentario: Insuficiente.")

elif nota < 2.5 and nota >= 0:
 print("\nComentario: Deficiente.")