class Persona:
    def __init__(self, nombre,apellido):
        self._nombre = nombre # Atributo protegido
        self.__apellido = apellido # Atributo privado

    def mostrar_persona(self):
        print(f'Persona: nombre {self._nombre}, apellido: {self.__apellido}')

    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self.__apellido

    def setNombre(self, nombre):
        self._nombre=nombre

    def setApellido(self, apellido):
        self.__apellido=apellido




# Codigo principal

persona1 = Persona('Pablo', 'Calvo')

# Lectura de atributos
print(persona1.getNombre())
print(persona1.getApellido())

# Modificar atributos
persona1.setNombre('Pablo Ariel')
persona1.mostrar_persona()