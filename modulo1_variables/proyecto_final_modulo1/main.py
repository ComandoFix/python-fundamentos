#- Crear una lista vacía llamada "contactos"
contactos = []


# - Crear una función "agregar_contacto" que reciba nombre, teléfono y email
#     - Crear un diccionario con esos datos
#     - Agregarlo a la lista contactos
def agregar_contactos():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    correo = input("Ingrese el correo electrónico del contacto: ")

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    contactos.append(contacto)
    print("Contacto agregado")


# - Crear una función "ver_contactos" que:
#     - Si la lista está vacía, avise al usuario
#     - Si no, recorra la lista y muestre cada contacto
def ver_contactos():
    if not contactos:
        print("No hay contactos para mostrar.")
        return

    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")


# - Crear una función "buscar_contacto" que reciba un nombre:
#     - Recorra la lista buscando ese nombre
#     - Si lo encuentra, lo muestra
#     - Si no, avisa al usuario
def buscar_contacto():
    contacto_buscado = input("Ingrese el nombre del contacto a buscar: ")
    for contacto in contactos:
        if contacto['nombre'] == contacto_buscado:
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
            return
    print("Contacto no encontrado.")


# - Crear una función "eliminar_contacto" que reciba un nombre:
#     - Recorra la lista buscando ese nombre
#     - Si lo encuentra, lo elimina
#     - Si no, avisa al usuario
def eliminar_contacto():
    contacto_a_eliminar = input("Ingrese el nombre del contacto a buscar: ")
    for contacto in contactos:
        if contacto['nombre'] == contacto_a_eliminar:
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
            confirm_remove = input("¿Desea eliminar este contacto? (s/n): ")
            if confirm_remove == "s":
                contactos.remove(contacto)
                print("Contacto eliminado.")
            return
    print("Contacto a eliminar no encontrado.")


# - Crear un bucle while True que:
#     - Muestre un menú con 5 opciones
#     - Pida al usuario que elija
#     - Ejecute la función correspondiente
#     - Si elige 5, rompa el bucle con break
while True:
    print("\n\nMenú de Contactos:")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        agregar_contactos()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

