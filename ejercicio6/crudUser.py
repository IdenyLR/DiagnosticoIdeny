
usuarios = []
contador_id = 1  


def agregar_usuario():
    """Permite agregar un usuario con nombre, edad y contraseña."""
    global contador_id
    nombre = input("ingresa el nombre de usuario: ")
    edad = input("ingresa la edad: ")
    contrasena = input("ingresa la contraseña: ")

    usuario = {
        "id": contador_id,
        "nombre": nombre,
        "edad": edad,
        "contrasena": contrasena  
    }

    usuarios.append(usuario)
    contador_id += 1
    print("\n Usuario agregado con éxito.")
    listar_usuarios()


def editar_usuario():
    """Permite editar los datos de un usuario por su ID."""
    listar_usuarios()
    user_id = int(input("\nIngresa el ID del usuario q desea editar: "))

    for usuario in usuarios:
        if usuario["id"] == user_id:
            usuario["nombre"] = input("Nuevo nombre de usuario: ")
            usuario["edad"] = input("Nueva edad: ")
            usuario["contrasena"] = input("Nueva contraseña: ")
            print("\n Usuario actualizado correctamente.")
            listar_usuarios()
            return

    print("\n Usuario no encontrado.")


def eliminar_usuario():
    """Permite eliminar un usuario por su ID."""
    listar_usuarios()
    user_id = int(input("\nIngresa el ID del usuario a eliminar: "))

    for usuario in usuarios:
        if usuario["id"] == user_id:
            usuarios.remove(usuario)
            print("\n Usuario eliminado correctamente.")
            listar_usuarios()
            return

    print("\n Usuario no encontrado.")


def listar_usuarios():
    """Muestra la lista actualizada de usuarios."""
    print("\n⭒⭒⭒ Lista de Usuarios ⭒⭒⭒")
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Contraseña: {usuario['contrasena']}")


def menu():
    """Menú de opciones para la gestión de usuarios."""
    while True:
        print("\n⭒⭒⭒ Menú de Gestión de Usuarios ⭒⭒⭒")
        print("1. Agregar usuario")
        print("2. Editar usuario")
        print("3. Eliminar usuario")
        print("4. Ver lista de usuarios")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            editar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            listar_usuarios()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print(" Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
