# Ejercicio 2 — Herencia
# Consigna:
# Usando la clase Libro que ya tenés como base, creá una clase hija llamada LibroDigital que herede todo de Libro y agregue:
# Atributo propio: formato (puede ser "PDF", "EPUB", etc.)
# Atributo propio: tamaño_mb (tamaño del archivo en megabytes)
# Método propio mostrar_descarga() que imprima el formato y el tamaño
# Creá un objeto LibroDigital y probá todos los métodos, incluyendo los heredados de Libro.


class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print(f"El libro {self.titulo} pertenece a {self.autor} y tiene {self.paginas} paginas")

class LibroDigital(Libro):
    def __init__(self,titulo,autor,paginas,formato,tamano_mb):
        super().__init__(titulo, autor, paginas)
        self.formato = formato
        self.tamano_mb = tamano_mb

    def mostrar_descarga(self):
        print(f"El libro {self.titulo} es de formato {self.formato} y pesa {self.tamano_mb} megabytes")


librodigital1 = LibroDigital("Rayuela","Julio Cortázar", 200, "EPUB", 512)
librodigital1.mostrar_descarga()
librodigital1.mostrar_info()