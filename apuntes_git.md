# Apuntes — Git y GitHub

## ¿Qué es Git?
Git es un sistema que registra los cambios de tu código a lo largo del tiempo.
Cada vez que guardás un punto en el historial, eso se llama **commit**.
Podés volver a cualquier commit anterior si algo sale mal.

## ¿Qué es GitHub?
GitHub es un sitio web donde subís tu código para guardarlo en la nube
y que otros puedan verlo. Es donde va tu portfolio.

---

## Flujo de trabajo completo (primera vez)

Estos comandos se usan UNA SOLA VEZ para configurar un proyecto nuevo.

### 1. Configurar tu identidad (solo la primera vez en la PC)
```````````````git config --global user.name "Tu Nombre"```
``````````````git config --global user.email "tu@email.com"```

### 2. Inicializar Git en la carpeta del proyecto
`````````````git init```

### 3. Agregar todos los archivos
````````````git add .```

### 4. Crear el primer commit
```````````git commit -m "feat: descripción de lo que hiciste"```

### 5. Renombrar la rama principal
``````````git branch -M main```

### 6. Conectar con GitHub (reemplazá TU_USUARIO)
`````````git remote add origin https://github.com/TU_USUARIO/nombre-repo.git```

### 7. Subir el código
````````git push -u origin main```

---

## Flujo de trabajo diario (cada vez que hacés cambios)

Estos tres comandos los vas a usar TODO EL TIEMPO.

### 1. Agregar los cambios
```````git add .```

### 2. Crear el commit con descripción
``````git commit -m "descripción de lo que cambiaste"```

### 3. Subir a GitHub
`````git push```

---

## Prefijos para mensajes de commit

Convención real usada en equipos profesionales:

| Prefijo | Cuándo usarlo |
|---|---|
| `feat:` | Agregás algo nuevo |
| `fix:` | Corregís un error |
| `docs:` | Cambiás documentación o comentarios |
| `refactor:` | Mejorás el código sin cambiar lo que hace |

### Ejemplos:
- `feat: primer ejercicio - variables y tipos de datos`
- `fix: corregir error en el cálculo de edad`
- `docs: actualizar README con instrucciones`

---

## Comandos útiles extra

Ver el estado actual de los archivos modificados:
````git status```

Ver el historial de commits:
```git log --oneline```

---

## Analogía para recordar el flujo diario

- `git add .` → metés los archivos en una caja
- `git commit` → sellás la caja con una etiqueta descriptiva
- `git push` → mandás la caja a GitHub
```

