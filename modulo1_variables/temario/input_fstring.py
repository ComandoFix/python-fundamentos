# input() y f-strings
# El usuario escribe su nombre y edad, el programa responde

# input() muestra un mensaje y espera que el usuario escriba algo
# Lo que escribe queda guardado en la variable "nombre"
nombre = input("¿Cuál es tu nombre? ")

# Todo lo que devuelve input() es str, aunque el usuario escriba un número
edad = input("¿Cuántos años tenés? ")

# Convertimos edad a int porque queremos operar con ella como número
# int() convierte un str a entero
edad = int(edad)

# f-string: la f antes de las comillas permite meter variables con {}
print(f"Hola {nombre}, tenés {edad} años.")

# También podemos hacer operaciones dentro del {}
print(f"El año que viene vas a tener {edad + 1} años.")
