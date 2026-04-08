# Polimorfismo en Python

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice: Guau!")

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice: Miau!")

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice: Muuu!")

# Lista con objetos de distintas clases
animales = [
    Perro("Rex"),
    Gato("Mishi"),
    Vaca("Lola")
]

# El mismo método hablar() se comporta distinto según el objeto
for animal in animales:
    animal.hablar()