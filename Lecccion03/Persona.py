class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.nombre}, Edad: {self.edad}'

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self.sueldo}'

class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color {self.color} Ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Tipo: {self.tipo}'



