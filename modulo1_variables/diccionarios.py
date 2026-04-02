# Diccionarios en Python

# Creamos un diccionario con datos de un usuario
usuario = {
    "nombre": "Emanuel",
    "edad": 30,
    "email": "emanuel@email.com",
    "activo": True
}

# Accedemos a valores por clave
print(usuario["nombre"])   # Emanuel
print(usuario["edad"])     # 30

# Modificamos un valor existente
usuario["edad"] = 31
print(usuario["edad"])     # 31

# Agregamos una clave nueva
usuario["ciudad"] = "Buenos Aires"
print(usuario)

# Eliminamos una clave
del usuario["activo"]
print(usuario)

# Recorremos el diccionario con un for
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")


#Ejercicio práctico
#Escribí un programa que haga esto:
#Creá un diccionario que represente un producto de una tienda con las claves: nombre, precio, stock y categoria. 
#Luego mostrá cada dato con un f-string y aplicá un 15% de descuento al precio, actualizando el valor en el diccionario.

producto = {
    "nombre": "Camiseta",
    "precio": 29.99,
    "stock": 50,
    "categoria": "Ropa"
}

for key,value in producto.items():
    print(f"{key}: {value}")

producto["precio"] = (producto["precio"] * 0.85)
print(f"El precio con descuento es de {producto['precio']}")