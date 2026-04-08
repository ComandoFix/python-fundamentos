# Herencia en Python

# Clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Clase hija — hereda todo de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, empresa, salario):   # Agregamos atributos empresa y salario
        super().__init__(nombre, edad)                    # Llamamos al constructor del padre para no repetir código
        self.empresa = empresa                            # Agregamos los atributos propios del Empleado
        self.salario = salario                            # Agregamos los atributos propios del Empleado

    def mostrar_trabajo(self):                            # Método propio del Empleado
        print(f"{self.nombre} trabaja en {self.empresa} y gana ${self.salario}.")

# Creamos objetos
persona1 = Persona("Lucas", 15)
empleado1 = Empleado("Emanuel", 31, "ComandoFix", 1500)

# persona1 solo tiene acceso a métodos de Persona
persona1.presentarse()

# empleado1 tiene acceso a métodos de Persona Y de Empleado
empleado1.presentarse()      # heredado de Persona
empleado1.mostrar_trabajo()  # propio de Empleado



# Ejercicio práctico
# Agregá debajo del código que ya tenés en herencia.py una clase hija llamada Estudiante que herede de Persona y tenga:
# Atributos propios: carrera y promedio
# Método propio mostrar_estudio() que imprima la carrera y el promedio
# Creá un objeto y probá tanto presentarse() como mostrar_estudio().

class Estudiante(Persona):
    def __init__(self,nombre,edad,carrera,promedio):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_estudio(self):
        print(f"{self.nombre} estudia {self.carrera} y su promeido es de {self.promedio}")

estudiante1 = Estudiante("María", 22, "Programación", 8.5)
estudiante1.presentarse()
estudiante1.mostrar_estudio()
        