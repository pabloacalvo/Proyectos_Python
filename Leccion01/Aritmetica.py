
class Aritmetica:
    """
    Clase Artimetica para realizar las operaciones de sumar, restar, etc..
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.resta()}')
print(f'Producto: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir():.2f}')
print(f'Division: {aritmetica1.dividir().__round__(2)}')