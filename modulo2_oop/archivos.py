# Manejo de archivos en Python

# --- ESCRIBIR un archivo ---
with open("contactos.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Emanuel, 31, emanuel@gmail.com\n")
    archivo.write("Lucas, 15, lucas@gmail.com\n")
    archivo.write("María, 22, maria@gmail.com\n")

print("Archivo creado correctamente.")

# --- LEER el archivo completo ---
with open("contactos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# --- LEER línea por línea ---
with open("contactos.txt", "r") as archivo:
    for linea in archivo:
        print(f"Línea: {linea.strip()}")  # strip() elimina el \n del final

# --- AGREGAR una línea sin borrar el contenido ---
with open("contactos.txt", "a") as archivo:
    archivo.write("Carlos, 28, carlos@gmail.com\n")

print("Contacto agregado al archivo.")