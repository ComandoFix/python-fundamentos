# Funciones en Python

# Definimos una función que saluda a un usuario
# "nombre" es el parámetro: el dato que necesita para trabajar
def saludar(nombre):
    return f"Hola {nombre}, bienvenido."

# Definimos una función que calcula el precio con descuento
# recibe el precio original y el porcentaje de descuento
def calcular_descuento(precio, descuento):
    resultado = precio - (precio * descuento / 100)
    return resultado

# --- LLAMADAS A LAS FUNCIONES ---

# Llamamos a saludar() y guardamos lo que devuelve en una variable
mensaje = saludar("Emanuel")
print(mensaje)

# Llamamos a calcular_descuento() con precio 1000 y 20% de descuento
precio_final = calcular_descuento(1000, 20)
print(f"El precio final es: {precio_final}")


# --- Ejercicio práctico ---
#Escribí una función que:
#Se llame calcular_promedio
#Reciba tres números como parámetros
#Devuelva el promedio de los tres
#La llamés e imprimás el resultado con un f-string

#creando funcion calcular_promedio
def pidiendo_numeros(numero1, numero2, numero3):
    calculando_promedio = ((numero1 + numero2 + numero3) /3 )
    return(calculando_promedio)

#pidiendo al usuario los 3 numeros
numero1 = int(input("inserte un numero: "))
numero2 = int(input("inserte un numero: "))
numero3 = int(input("inserte un numero: "))

resultado = pidiendo_numeros(numero1, numero2, numero3)
print(f"El promedio de los 3 numeros es: {resultado}")

