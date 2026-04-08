# Manejo de errores en Python

# --- Error básico ---
try:
    numero = int(input("Ingresá un número: "))
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("Error: eso no es un número válido.")

print("---")

# --- Múltiples tipos de error ---
try:
    lista = [1, 2, 3]
    indice = int(input("Ingresá un índice: "))
    print(f"El valor es: {lista[indice]}")
except ValueError:
    print("Error: ingresaste texto en vez de un número.")
except IndexError:
    print("Error: ese índice no existe en la lista.")

print("---")

# --- Finally ---
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Error: el archivo no existe.")
finally:
    print("Este mensaje se imprime siempre.")