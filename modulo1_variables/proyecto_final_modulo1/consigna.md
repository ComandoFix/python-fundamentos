📋 Consigna — Proyecto Final Módulo 2
Nombre del proyecto: Gestor de Contactos v2
Objetivo: Refactorizar el Gestor de Contactos del Módulo 1 aplicando todo lo aprendido en el Módulo 2.

Requisitos:
1. Usar OOP
Cada contacto debe ser un objeto de la clase Contacto, no un diccionario. La clase debe tener:

Atributos: nombre, telefono, email
Método mostrar() que imprima los datos del contacto
Método to_dict() que convierta el objeto a diccionario
Método from_dict() que cree un objeto desde un diccionario

2. Persistencia con JSON
Los contactos deben guardarse en un archivo contactos.json automáticamente cada vez que se agrega o elimina uno. Al abrir el programa, los contactos deben cargarse desde ese archivo. Si cerrás y abrís el programa, los contactos tienen que seguir ahí.
3. Manejo de errores
El programa no debe romperse ante entradas inválidas o archivos inexistentes.
4. Separación de archivos

contacto.py → solo la clase Contacto
main.py → importa la clase y maneja el menú y la lógica

5. Menú igual al Módulo 1

Agregar contacto
Ver contactos
Buscar contacto
Eliminar contacto
Salir