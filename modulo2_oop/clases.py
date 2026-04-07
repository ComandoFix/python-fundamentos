class Auto:

    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.encendido = False      # valor por defecto

    # Método: acción que puede hacer el objeto
    def encender(self):
        if self.combustible > 0:
            self.encendido = True
            print(f"{self.marca} encendido.")
        else:
            print(f"{self.marca} sin combustible.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} — Estado: {estado} — Combustible: {self.combustible}%")


# Creamos los objetos
auto1 = Auto("Toyota", "Corolla", 80)
auto2 = Auto("Ford", "Focus", 0)

# Llamamos los métodos con punto, igual que los atributos
auto1.mostrar_estado()
auto1.encender()
auto1.mostrar_estado()

print("---")

auto2.mostrar_estado()
auto2.encender()


# Ejercicio práctico
# Escribí una clase llamada Persona con:
# Atributos: nombre, edad, email
# Método presentarse() que imprima algo como: "Hola, soy Emanuel, tengo 31 años."
# Método es_mayor_de_edad() que imprima si la persona es mayor o menor de edad
#- Crear una lista vacía llamada "contactos"

class Persona:                                            

    def __init__(self, nombre, edad, email):              
        self.nombre = nombre                              
        self.edad = edad
        self.email = email

    def presentarse(self):                                
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años")                         
    
    def es_mayor_de_edad(self):                               
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")     
        else:
            print(f"{self.nombre} es menor de edad")     


persona1 = Persona("Emanuel",31,"emanuel@gmail.com")  
persona1.presentarse()
persona1.es_mayor_de_edad()
