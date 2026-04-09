# Resumen Módulo 2 — Programación Orientada a Objetos

## 1. Los 4 pilares de OOP

### Abstracción — Clases y Objetos
Una clase es el molde. Un objeto es una instancia creada a partir de ese molde.

```python
class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca      # atributo
        self.modelo = modelo    # atributo

    def encender(self):         # método
        print(f"{self.marca} encendido.")

auto1 = Auto("Toyota", "Corolla")  # objeto / instancia
auto1.encender()
```

### Terminología clave
| Término | Definición |
|---|---|
| Clase | El molde que define la estructura |
| Objeto | Una instancia creada a partir de la clase |
| Instanciar | El acto de crear un objeto desde una clase |
| Constructor | El método `__init__` que inicializa el objeto |
| Atributo | Un dato que pertenece al objeto |
| Método | Una función que pertenece a la clase |
| `self` | Referencia al objeto dentro de la clase |

### ¿Qué es `__init__`?
Se ejecuta automáticamente al crear un objeto. Define los atributos iniciales.

### ¿Qué es `self`?
Dentro de la clase se llama `self`. Fuera de la clase se llama `auto1`, `auto2`, etc.
Son el mismo objeto, distinto nombre según desde dónde lo mirás.

---

### Herencia
Una clase hija hereda atributos y métodos de una clase padre.
`super()` llama al constructor del padre para no repetir código.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")

class Empleado(Persona):
    def __init__(self, nombre, edad, empresa):
        super().__init__(nombre, edad)  # hereda de Persona
        self.empresa = empresa

    def mostrar_trabajo(self):
        print(f"{self.nombre} trabaja en {self.empresa}.")

empleado1 = Empleado("Emanuel", 31, "ComandoFix")
empleado1.presentarse()     # heredado de Persona
empleado1.mostrar_trabajo() # propio de Empleado
```

---

### Encapsulamiento
Controla el acceso a los atributos para proteger la integridad de los datos.

| Sintaxis | Significado |
|---|---|
| `self.nombre` | Público — accesible desde cualquier lado |
| `self._nombre` | Protegido — no debería modificarse desde afuera |
| `self.__nombre` | Privado — Python lo oculta activamente |

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo        # privado

    def get_saldo(self):            # getter
        return self.__saldo

    def depositar(self, monto):     # setter con validación
        if monto > 0:
            self.__saldo += monto
```

---

### Polimorfismo
Diferentes clases pueden tener métodos con el mismo nombre que se comportan distinto.

```python
class Perro:
    def hablar(self):
        print("Guau!")

class Gato:
    def hablar(self):
        print("Miau!")

animales = [Perro(), Gato()]
for animal in animales:
    animal.hablar()  # mismo método, distinto comportamiento
```

---

## 2. Manejo de archivos

```python
# Escribir
with open("archivo.txt", "w") as archivo:
    archivo.write("contenido\n")

# Leer completo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

# Leer línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina el \n

# Agregar sin borrar
with open("archivo.txt", "a") as archivo:
    archivo.write("nueva línea\n")
```

### Modos de apertura
| Modo | Significado |
|---|---|
| `"r"` | Leer |
| `"w"` | Escribir (borra el contenido anterior) |
| `"a"` | Agregar al final |
| `"r+"` | Leer y escribir |

---

## 3. Manejo de errores

```python
try:
    numero = int(input("Ingresá un número: "))
except ValueError:
    print("Eso no es un número.")
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Todo salió bien.")
finally:
    print("Esto se ejecuta siempre.")
```

### Excepciones más comunes
| Excepción | Cuándo ocurre |
|---|---|
| `ValueError` | Valor incorrecto para el tipo. Ej: `int("hola")` |
| `IndexError` | Índice fuera del rango de una lista |
| `KeyError` | Clave inexistente en un diccionario |
| `FileNotFoundError` | Archivo que no existe |
| `TypeError` | Operación entre tipos incompatibles |
| `ZeroDivisionError` | División por cero |

---

## 4. Librerías estándar

### json
```python
import json

# Diccionario → texto JSON
texto = json.dumps(diccionario, indent=4)

# Texto JSON → diccionario
diccionario = json.loads(texto)

# Guardar en archivo
with open("datos.json", "w") as f:
    json.dump(diccionario, f, indent=4)

# Leer desde archivo
with open("datos.json", "r") as f:
    datos = json.load(f)
```

### os
```python
import os

os.getcwd()              # carpeta actual
os.path.exists("ruta")  # verificar si existe
os.listdir(".")          # listar archivos de la carpeta
os.makedirs("carpeta")  # crear carpeta
```

### datetime
```python
from datetime import datetime

ahora = datetime.now()                    # fecha y hora actual
formateada = ahora.strftime("%d/%m/%Y")  # formatear fecha
diferencia = datetime.now() - fecha      # diferencia entre fechas
dias = diferencia.days                   # diferencia en días
```

---

## 5. Entornos virtuales y pip

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Instalar librería
pip install nombre_libreria

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements.txt (en otra máquina)
pip install -r requirements.txt

# Desactivar entorno virtual
deactivate
```

### Regla de oro
La carpeta `venv` nunca se sube a GitHub. Siempre en `.gitignore`.