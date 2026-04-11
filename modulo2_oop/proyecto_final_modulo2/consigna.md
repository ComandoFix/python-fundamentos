ARCHIVO: contacto.py

- Crear una clase "Contacto" con:
    - Atributos: nombre, telefono, email
    - Método mostrar() que imprima los tres datos
    - Método to_dict() que convierta el objeto a diccionario
    - Método from_dict() que cree un objeto Contacto desde un diccionario

ARCHIVO: main.py

- Importar json, os y la clase Contacto desde contacto.py
- Definir una constante ARCHIVO = "contactos.json"

- Crear una función "cargar_contactos" que:
    - Si el archivo no existe, devuelva una lista vacía
    - Si existe, lea el JSON y convierta cada diccionario en objeto Contacto
    - Devuelva la lista de objetos

- Crear una función "guardar_contactos" que reciba la lista de contactos:
    - Convierta cada objeto Contacto a diccionario con to_dict()
    - Guarde la lista en el archivo JSON

- Crear una función "agregar_contacto" que reciba la lista de contactos:
    - Pida nombre, teléfono y email al usuario
    - Cree un objeto Contacto con esos datos
    - Lo agregue a la lista
    - Llame a guardar_contactos()

- Crear una función "ver_contactos" que reciba la lista de contactos:
    - Si la lista está vacía, avise al usuario
    - Si no, llame a mostrar() en cada contacto

- Crear una función "buscar_contacto" que reciba la lista de contactos:
    - Pida un nombre al usuario
    - Recorra la lista buscando ese nombre
    - Si lo encuentra, llame a mostrar()
    - Si no, avise al usuario

- Crear una función "eliminar_contacto" que reciba la lista de contactos:
    - Pida un nombre al usuario
    - Recorra la lista buscando ese nombre
    - Si lo encuentra, pida confirmación
    - Si confirma, elimínelo y llame a guardar_contactos()
    - Si no lo encuentra, avise al usuario

- Crear un bucle while True que:
    - Cargue los contactos desde el archivo al iniciar
    - Muestre un menú con 5 opciones
    - Pida al usuario que elija
    - Ejecute la función correspondiente
    - Si elige 5, rompa el bucle con break