# Sistema de categorización de productos
# Diseñar un sistema que reciba el nombre y precio de un producto y lo clasifique


print("=" * 50)
print("BIENVENIDO AL SISTEMA DE CATEGORIZACIÓN DE PRODUCTOS")
print("=" * 50)

# Solicitar el nombre del producto y validar que no esté vacío

# El programa seguirá solicitando el nombre del producto hasta que el usuario ingrese un valor válido (no vacío).
while True:
    nombre = input("\nIngrese el nombre del producto: ").strip()
    if nombre:
        # Si el nombre no está vacío, se sale del bucle y se continúa con el programa.
        break
    else:
        print("Error: El nombre del producto no puede estar vacío.")

# Solicitar el precio del producto y validar que sea un número positivo

while True:
    precio_input = input("Ingrese el precio del producto: ")
    # El programa intentará convertir la entrada del usuario a un número flotante. Si la conversión falla (por ejemplo, si el usuario ingresa texto en lugar de un número), se mostrará un mensaje de error y se solicitará nuevamente el precio.
    try:
        precio = float(precio_input)
        if precio > 0:
            break
        else:
            print("Error: El precio debe ser un número positivo mayor que cero.")
# Si el usuario ingresa un valor que no se puede convertir a un número (como texto), se capturará la excepción ValueError y se mostrará un mensaje de error indicando que el precio debe ser un número válido.                        
    except ValueError:
        print("Error: El precio debe ser un número válido.")

# Clasificar el producto según su precio y calcular el descuento correspondiente

if precio <= 10000:
    categoria = "Producto económico"
    descuento = 0
elif precio <= 50000:
    categoria = "Producto estándar"
    descuento = 5
elif precio <= 200000:
    categoria = "Producto premium"
    descuento = 10
else:
    categoria = "Producto de lujo"
    descuento = 15

precio_final = precio - (precio * descuento / 100)

print(f"\nProducto: {nombre}")
print(f"Categoría: {categoria}")
print(f"Descuento aplicado: {descuento}%")
print(f"Precio final: ${precio_final}")

# Fin del programa