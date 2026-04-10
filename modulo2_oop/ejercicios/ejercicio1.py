# Ejercicio 1 — Clase básica
# Consigna:
# Creá una clase llamada Libro con:
# Atributos: titulo, autor, paginas
# Método mostrar_info() que imprima los tres datos
# Método es_largo() que imprima si el libro tiene más de 300 páginas o no


class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print(f"El libro {self.titulo} pertenece a {self.autor} y tiene {self.paginas} paginas")
    
    def es_largo(self):
        if self.paginas >= 300:
            print(f"El libro {self.titulo} tiene mas de 300 paginas")
        else:
            print(f"El libro {self.titulo} tiene menos de 300 paginas")            

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 310)
libro2 = Libro("Rayuela","Julio Cortázar", 200)

libro1.mostrar_info()
libro1.es_largo()
libro2.mostrar_info()
libro2.es_largo()

