# Ejercicio 3 — Encapsulamiento
# Consigna:
# Creá una clase llamada Producto que represente un producto de una tienda con:
# Atributo público: nombre
# Atributo privado: __precio
# Atributo privado: __stock
# Método get_precio() que devuelva el precio
# Método get_stock() que devuelva el stock
# Método actualizar_precio(nuevo_precio) que actualice el precio solo si es mayor a cero
# Método vender(cantidad) que reste del stock solo si hay suficiente cantidad disponible
# Método mostrar() que imprima nombre, precio y stock

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"Precio actualizado a: ${self.__precio}")
        else:
            print("El precio debe ser mayor a cero.")

    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Venta exitosa. Stock actual: {self.__stock}")
        else:
            print(f"Stock insuficiente. Stock disponible: {self.__stock}")

    def mostrar(self):
        print(f"Producto: {self.nombre} | Precio: ${self.__precio} | Stock: {self.__stock}")


# --- PROGRAMA PRINCIPAL ---

producto1 = Producto("Reloj", 500, 5)
producto1.mostrar()

# Pedir precio nuevo con validación de tipo y valor
while True:
    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("El precio debe ser mayor a cero. Intente de nuevo.")
        else:
            producto1.actualizar_precio(nuevo_precio)
            break
    except ValueError:
        print("Error: ingreso texto en vez de un número. Intentá de nuevo.")

# Pedir cantidad con validación de tipo y stock disponible
while True:
    try:
        cantidad = int(input("¿Cuántas unidades quiere vender? "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero. Intente de nuevo.")
        elif cantidad > producto1.get_stock():
            print(f"Stock insuficiente. Stock disponible: {producto1.get_stock()}. Intente de nuevo.")
        else:
            producto1.vender(cantidad)
            break
    except ValueError:
        print("Error: ingreso texto en vez de un número. Intente de nuevo.")

producto1.mostrar()