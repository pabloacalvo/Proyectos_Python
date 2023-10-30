class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido



class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=0.0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nN° de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self,monto):
        self.balance += monto
        print(f"Deposito aceptado, se registro un deposito de {monto}")

    def retirar(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= monto
            print(f"Se registro un retiro de {monto}")


def inicio():
    eleccion_menu = 0
    cliente = crear_cliente()
    print("  Bienvenido  ".center(100,'*'))
    print(cliente)
    while eleccion_menu != 's':
        print("Elegi una opcion: ")
        print("""
        [R] - Retirar
        [D] - Depositar
        [S] - Salir
        """)
        eleccion_menu = input().lower()
        if eleccion_menu == 'd':
            monto = float(input("Ingresa el monto de depositar: "))
            cliente.depositar(monto)
            print(cliente)
        elif  eleccion_menu == 'r':
            monto = float(input("Ingresa el monto a retirar: "))
            cliente.retirar(monto)
            print(cliente)
        elif eleccion_menu == 's':
            print("Has salido, hasta luego!")

def crear_cliente():
    nombre = input("Ingresa un nombre: ")
    apellido = input("Ingresa el apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre,apellido,numero_cuenta)
    return cliente


inicio()

