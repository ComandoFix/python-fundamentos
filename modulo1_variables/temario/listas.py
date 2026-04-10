# Listas en Python

# Creamos una lista de nombres
usuarios = ["Emanuel", "Juan", "María", "Ana"]

# Accedemos a elementos por índice
print(usuarios[0])   # Emanuel
print(usuarios[1])   # Juan
print(usuarios[-1])  # Ana (índice negativo: cuenta desde el final)

# Longitud de la lista
print(len(usuarios))  # 4

# Agregamos un elemento al final
usuarios.append("Carlos")
print(usuarios)

# Eliminamos un elemento por valor
usuarios.remove("Juan")
print(usuarios)

# Recorremos toda la lista con un for
for usuario in usuarios:
    print(f"Usuario: {usuario}")



#Ejercicio práctico
#Escribí un programa que haga esto:
#Creá una lista con 5 precios de productos. Recorrela con un for y mostrá cada precio. Al final mostrá el precio más alto y el más bajo.
#Pista: Python tiene dos funciones incorporadas llamadas max() y min() que reciben una lista y devuelven el valor máximo y mínimo.

# Lista de precios
precios = [19.99, 5.49, 3.50, 12.00, 7.25]

for precio in precios:
    print(f"Precio: ${precio}")

print(f"El precio mas alto es ${max(precios)}")
print(f"El precio mas bajo es ${min(precios)}")
