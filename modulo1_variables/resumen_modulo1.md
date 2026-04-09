# Resumen Módulo 1 — Python Fundamentos

## 1. Variables y tipos de datos
Una variable es un espacio en memoria con un nombre asignado que almacena un valor.
```python
nombre = "Emanuel"   # str - texto
edad = 31            # int - número entero
altura = 1.75        # float - número decimal
activo = True        # bool - verdadero o falso
```

### Tipos de datos básicos
| Tipo | Descripción | Ejemplo |
|---|---|---|
| `str` | Texto | `"Hola"` |
| `int` | Número entero | `25` |
| `float` | Número decimal | `9.99` |
| `bool` | Verdadero o falso | `True` / `False` |

### Funciones útiles
```python
type(variable)   # devuelve el tipo de dato
int("25")        # convierte str a int
float("9.99")    # convierte str a float
```

---

## 2. print() e input()
```python
print("Hola mundo")          # muestra texto en consola
nombre = input("Tu nombre: ") # espera que el usuario escriba algo
```

⚠️ Todo lo que devuelve input() es siempre str.
Si necesitás un número, convertilo:
```python
edad = int(input("Tu edad: "))
```

---

## 3. F-strings
Permiten insertar variables dentro de texto de forma limpia.
```python
nombre = "Emanuel"
edad = 31
print(f"Hola {nombre}, tenés {edad} años.")
print(f"El año que viene tenés {edad + 1} años.")
```

---

## 4. Operadores

### Operadores de comparación
| Operador | Significado |
|---|---|
| `==` | igual a |
| `!=` | distinto de |
| `>`  | mayor que |
| `<`  | menor que |
| `>=` | mayor o igual |
| `<=` | menor o igual |

### Operadores lógicos
| Operador | Descripción |
|---|---|
| `and` | ambas condiciones deben ser True |
| `or`  | al menos una debe ser True |
| `not` | invierte el resultado |

---

## 5. Condicionales
```python
if condicion:
    # se ejecuta si la condición es True
elif otra_condicion:
    # se ejecuta si la segunda condición es True
else:
    # se ejecuta si ninguna condición fue True
```

⚠️ Python usa indentación (4 espacios) en lugar de llaves {}.
⚠️ Los dos puntos : son obligatorios al final de cada condición.

---

## 6. Bucles

### While — repetir mientras una condición sea True
```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # equivale a contador = contador + 1
```
⚠️ Si olvidás incrementar el contador, se genera un bucle infinito.
Para detenerlo: Ctrl + C en la terminal.

### For — repetir una cantidad definida de veces
```python
for numero in range(1, 6):  # del 1 al 5, el 6 no se incluye
    print(numero)
```

### ¿Cuándo usar cada uno?
| Bucle | Usalo cuando... |
|---|---|
| `while` | No sabés cuántas veces vas a repetir |
| `for` | Sabés exactamente cuántas veces o tenés una lista |

---

## 7. Funciones

Bloque de código con nombre que podés ejecutar cuando quieras.
```python
# Definir una función
def saludar(nombre):
    return f"Hola {nombre}"

# Llamar una función
mensaje = saludar("Emanuel")
print(mensaje)
```

### Conceptos clave
- `def` → define la función
- Parámetros → datos que recibe la función para trabajar
- `return` → devuelve el resultado. Sin return, la función devuelve `None`
- Definir ≠ ejecutar. La función solo corre cuando la llamás con paréntesis.

---

## 8. Listas

Colección ordenada de elementos. Se accede por índice numérico que empieza en 0.
```python
usuarios = ["Emanuel", "Juan", "María"]

usuarios[0]    # Emanuel (primer elemento)
usuarios[-1]   # María (último elemento)
len(usuarios)  # 3 (longitud de la lista)

usuarios.append("Carlos")    # agrega al final
usuarios.remove("Juan")      # elimina por valor

for usuario in usuarios:
    print(usuario)
```

---

## 9. Diccionarios

Colección de pares clave-valor. Se accede por nombre de clave, no por índice.
```python
usuario = {
    "nombre": "Emanuel",
    "edad": 31,
    "email": "emanuel@email.com"
}

usuario["nombre"]            # Emanuel
usuario["edad"] = 32         # modifica un valor
usuario["ciudad"] = "BsAs"   # agrega una clave nueva
del usuario["email"]         # elimina una clave

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
```

### Lista vs Diccionario
| | Lista | Diccionario |
|---|---|---|
| Acceso | Por índice numérico | Por nombre de clave |
| Uso | Colección ordenada de elementos | Datos estructurados con etiquetas |
| Ejemplo | Lista de precios | Ficha de un usuario |

---

## 10. Git y GitHub

### Configuración inicial (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

### Flujo primera vez
git init
git add .
git commit -m "feat: descripción"
git branch -M main
git remote add origin https://github.com/USUARIO/REPO.git
git push -u origin main

### Flujo diario
git add .
git commit -m "prefijo: descripción"
git push

### Prefijos de commits
| Prefijo | Cuándo usarlo |
|---|---|
| `feat:` | Agregás algo nuevo |
| `fix:` | Corregís un error |
| `docs:` | Cambiás documentación |
| `refactor:` | Mejorás el código sin cambiar lo que hace |

### Comandos útiles
git status          # ver archivos modificados
git log --oneline   # ver historial de commits