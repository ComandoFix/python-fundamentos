# Operadores y condicionales
# Programa que evalúa si una persona puede acceder a un sistema

# Pedimos los datos al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tenés? "))

# Evaluamos la edad con if/elif/else
if edad >= 18:
    print(f"Bienvenido {nombre}, tenés acceso al sistema.")
elif edad >= 13:
    print(f"Hola {nombre}, tenés acceso limitado.")
    
else:
    print(f"Lo sentimos {nombre}, no tenés acceso.")

# Ejemplo con operador lógico "and"
if edad >= 13 : 
    tiene_cuenta = input("¿Tenés cuenta registrada? (si/no) ")

    if edad >= 18 and tiene_cuenta == "si":
        print("Acceso completo habilitado.")
    else:
        print("Acceso denegado.")
