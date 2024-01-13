class Snack:
    contador_snack = 0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        Snack.contador_snack+=1
        self.id=Snack.contador_snack

    def __str__(self):
        return f'ID: {self.id} - NOMBRE: {self.nombre} PRECIO: ${self.precio}'