# Sistema de login con múltiples usuarios
# Diseña un sistema de login que:
# 1. • Tenga al menos 3 pares usuario-contraseña definidos (ej: admin/1234, user/abcd, invitado/0000)
# 2. • Cada usuario tiene un rol diferente: 'administrador', 'usuario', 'invitado'
# 3. • Al entrar, muestre el menú correspondiente a su rol (no hace falta que el menú funcione, solo mostrarlo)
# 4. • Use try/except en todas las entradas de datos
# Pista: pueden usar variables separadas para cada usuario o investigar los diccionarios de Python


print("="*30)
print("SISTEMA DE LOGIN")
print("="*30)

usuario1 = "admin"
password1 = "1234"
rol1 = "administrador"

usuario2 = "user"
password2 = "abcd"
rol2 = "usuario"

usuario3 = "invitado"
password3 = "0000"
rol3 = "invitado"

while True:
    try:

        usuario = input("Ingrese usuario: ")
        contraseña = input("Ingrese contraseña: ")

        rol = None

        if usuario == usuario1 and contraseña == password1:
            rol = rol1
        elif usuario == usuario2 and contraseña == password2:
            rol = rol2
        elif usuario == usuario3 and contraseña == password3:
            rol = rol3

        if rol != None:
            print(f"\nBienvenido {usuario} ({rol})")

            while True:
                if rol == "administrador":
                    print("\nMenú Administrador:")
                    print("1. Gestionar usuarios")
                    print("2. Ver reportes")
                    print("3. Configuración")
                    print("4. Salir")

                elif rol == "usuario":
                    print("\nMenú Usuario:")
                    print("1. Ver perfil")
                    print("2. Realizar compras")
                    print("3. Salir")

                elif rol == "invitado":
                    print("\nMenú Invitado:")
                    print("1. Ver catálogo")
                    print("2. Salir")

                opcion = input("Seleccione una opción: ")

                if (rol == "administrador" and opcion == "4") or \
                   (rol == "usuario" and opcion == "3") or \
                   (rol == "invitado" and opcion == "2"):
                    print("Saliendo del sistema...")
                    break

                else:
                    print("Opción seleccionada (no funcional).")
            break
        else:
            print("Usuario o contraseña incorrectos. Intente de nuevo.\n")

    except Exception as e:
        print("Error en la entrada de datos:", e)


