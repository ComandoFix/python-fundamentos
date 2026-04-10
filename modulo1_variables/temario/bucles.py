# Bucles: while y for

# --- WHILE ---
# Contador simple: cuenta del 1 al 5
# Creamos una variable que empieza en 1
contador = 1  # tambien se puede poner "contador += 1" para evitar el "contador = contador + 1"


# El bucle se repite mientras contador sea menor o igual a 5
while contador <= 5:
    print(f"Número: {contador}")
    # Sumamos 1 al contador en cada repetición
    # Si no hacemos esto, el bucle nunca termina (bucle infinito)
    contador = contador + 1

print("---")

# --- FOR ---
# range(1, 6) genera una secuencia de números del 1 al 5
# El 6 no se incluye, range() excluye el último número
for numero in range(1, 6):
    print(f"Número: {numero}")




##Ejercicio práctico
#Quiero que escribas vos solo, debajo del código que ya tenés en `bucles.py`, un programa que haga esto:
#> Pedile al usuario un número con `input()`. Usá un bucle `for` para imprimir la tabla de multiplicar de ese número, del 1 al 10.

numero_dado = int(input("Ingrese un numero: "))

for lista in range(1,11):
    print(f"{numero_dado} x {lista} = {numero_dado * lista}")

