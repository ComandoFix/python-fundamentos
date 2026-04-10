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

