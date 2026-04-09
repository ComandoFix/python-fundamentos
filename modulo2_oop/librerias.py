# Librerías estándar: json, os, datetime
import json
import os
from datetime import datetime   # Importa solo la clase datetime de la librería datetime. Es una forma más específica de importar, así no tenés que escribir datetime.datetime cada vez.

# --- JSON ---

# Diccionario Python
usuario = {
    "nombre": "Emanuel",
    "edad": 31,
    "email": "emanuel@gmail.com"
}

# Convertir diccionario a texto JSON
usuario_json = json.dumps(usuario, indent=4) #indent=4 le dice que use 4 espacios de sangría para que sea legible. Sin indent, saldría todo en una sola línea.
print("Diccionario como JSON:")
print(usuario_json)
print(type(usuario_json))  # es un str

# Convertir texto JSON a diccionario
usuario_dict = json.loads(usuario_json)      # loads significa "load string". Hace el camino inverso: convierte texto JSON a diccionario Python. Esto es lo que hacés cuando tu API recibe datos de afuera.
print(f"\nNombre desde JSON: {usuario_dict['nombre']}")
print(type(usuario_dict))  # es un dict

# Guardar JSON en un archivo
with open("usuario.json", "w") as archivo:
    json.dump(usuario, archivo, indent=4)      # dump sin la s escribe directamente en un archivo. La diferencia con dumps es que uno trabaja con strings y el otro con archivos.
print("\nArchivo usuario.json creado.")

# Leer JSON desde un archivo
with open("usuario.json", "r") as archivo:
    datos = json.load(archivo)                 # load sin la s lee desde un archivo y devuelve un diccionario Python directamente.
print(f"Datos leídos del archivo: {datos}")

print("---")

# --- OS ---

# Obtener la carpeta actual
carpeta_actual = os.getcwd()                  # getcwd significa "get current working directory". Devuelve la ruta de la carpeta donde está parada la terminal
print(f"Carpeta actual: {carpeta_actual}")

# Verificar si un archivo existe
existe = os.path.exists("usuario.json")       # Verifica si un archivo o carpeta existe en el sistema. Devuelve True o False. Muy útil antes de intentar abrir un archivo para evitar errores.
print(f"¿Existe usuario.json? {existe}")

# Listar archivos de la carpeta actual
archivos = os.listdir(".")                    # Lista todos los archivos y carpetas en la ruta que le pasás. El . significa "la carpeta actual".
print(f"Archivos en la carpeta: {archivos}")

print("---")

# --- DATETIME ---

# Fecha y hora actual
ahora = datetime.now()                       # Devuelve la fecha y hora exacta en este momento
print(f"Fecha y hora actual: {ahora}")

# Formatear la fecha
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M") # strftime convierte la fecha a un texto con el formato que vos definís.
print(f"Fecha formateada: {fecha_formateada}")
# Los códigos son:
# %d → día
# %m → mes
# %Y → año con 4 dígitos
# %H → hora
# %M → minutos

# Calcular diferencia entre fechas
fecha_nacimiento = datetime(1994, 1, 15)
edad = datetime.now() - fecha_nacimiento
print(f"Días vividos: {edad.days}")
# Creás una fecha específica y la restás a la fecha actual.
# El resultado es un objeto timedelta que representa una diferencia de tiempo.
# .days te da esa diferencia en días