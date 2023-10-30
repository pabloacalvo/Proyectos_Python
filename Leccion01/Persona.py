class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.valores = valores
        self.terminos = terminos

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamndo almetodo set nombre')
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def  apellido(self,  apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} {self.valores} {self.terminos}')

    def __del__(self):
        print(f'Persona:{self._nombre} {self._apellido} se esta eliminando')




if __name__ == '__main__':
    persona1 = Persona('Pablo', 'Calvo', 25)
    persona1.mostrar_detalle()

    #persona2 = Persona('Carla', 'Gomez', 56)
    #persona2.mostrar_detalle()
    persona1._nombre = 'Juan Carlos'
    persona1._apellido = 'Coco'
    persona1._edad = 30

    persona1.mostrar_detalle()
