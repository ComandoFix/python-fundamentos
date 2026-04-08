# Encapsulamiento en Python

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular       # atributo público
        self.__saldo = saldo         # atributo privado — no accesible directo

    # Getter: método para leer el saldo
    # sirve para poder mostrar el interior del atributo privado. Solo puede leerse, no modificarse
    def get_saldo(self):
        return self.__saldo

    # Setter: método para modificar el saldo con validación
    def depositar(self, monto):
        if monto > 0:               #validador de este ejemplo
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if monto > self.__saldo:
            print("Saldo insuficiente.")
        elif monto <= 0:
            print("El monto debe ser mayor a cero.")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo}")


# Creamos un objeto
cuenta = CuentaBancaria("Emanuel", 1000)

# Accedemos al saldo mediante el getter
print(f"Saldo inicial: ${cuenta.get_saldo()}")

# Intentamos acceder directo al atributo privado
# print(cuenta.__saldo)  # esto daría error

# Usamos los métodos controlados
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(9999)
cuenta.depositar(-100)