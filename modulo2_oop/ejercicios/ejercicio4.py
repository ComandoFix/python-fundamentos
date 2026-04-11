# Ejercicio 4 — Polimorfismo (consigna corregida)
# Creá tres clases: Circulo, Rectangulo y Triangulo.
# Cada clase recibe sus medidas como atributos:

# Circulo → recibe radio
# Rectangulo → recibe base y altura
# Triangulo → recibe base y altura

# Cada clase debe tener:
# Método area() que calcule y devuelva el área
# Método mostrar() que imprima el nombre de la figura y su área

# Fórmulas:
# Círculo: 3.14159 * radio ** 2
# Rectángulo: base * altura
# Triángulo: (base * altura) / 2

# Luego creá estos tres objetos:
# Circulo(5)
# Rectangulo(4, 6)
# Triangulo(3, 8)

#Agregalos a una lista y recorrela con un for llamando a mostrar() en cada figura.



## -- EJERCICIO SIN HERENCIA
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        area_circulo = 3.14159 * self.radio ** 2
        return area_circulo
    
    def mostrar(self):
        print(f"El area de la forma Circulo es: {self.area()}")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area_rectangulo = self.base * self.altura
        return area_rectangulo
    
    def mostrar(self):
        print(f"El area de la forma Rectangulo es: {self.area()}")

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area_triangulo = (self.base * self.altura) / 2
        return area_triangulo
    
    def mostrar(self):
        print(f"El area de la forma Triangulo es: {self.area()}")

#Objetos
figura_circulo = Circulo(5)
figura_rectangulo = Rectangulo(4, 6)
figura_triangulo = Triangulo(3, 8)

#Lista para recorrer
areas = [figura_circulo, figura_rectangulo, figura_triangulo]

for figura in areas:
    figura.mostrar()



## -- EJERCICIO CON HERENCIA
class Figura:
    def area(self):
        pass 
    
    def mostrar(self):
        print(f"(herencia) El área de {type(self).__name__} es: {self.area()}")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        area_circulo = 3.14159 * self.radio ** 2
        return area_circulo

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area_rectangulo = self.base * self.altura
        return area_rectangulo

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area_triangulo = (self.base * self.altura) / 2
        return area_triangulo

#Objetos
figura_circulo = Circulo(5)
figura_rectangulo = Rectangulo(4, 6)
figura_triangulo = Triangulo(3, 8)

#Lista para recorrer
areas = [figura_circulo, figura_rectangulo, figura_triangulo]

for figura in areas:
    figura.mostrar()