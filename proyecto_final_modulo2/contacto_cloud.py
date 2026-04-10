# contacto.py
# Define la clase Contacto con sus atributos y métodos

class Contacto:

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Email: {self.email}")

    def to_dict(self):           # to_dict = Convierte el objeto a diccionario para poder guardarlo en JSON
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

    @classmethod                # Crea un objeto Contacto a partir de un diccionario
    def from_dict(cls, datos):  # Se usa al cargar contactos desde el archivo JSON
        return cls(datos["nombre"], datos["telefono"], datos["email"])