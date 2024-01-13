class Persona:
    # Atributo de clase
    contador_personas = 0

    def __init__(self,nombre,apellido):
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona {self.id} Nombre: {self.nombre} Apellido: {self.apellido}')

persona1 = Persona("Juan","Calvo")
persona2 = Persona("Pablo","Lopez")
persona3 = Persona('Cristian','Lema')

personas = persona1,persona2,persona3
print(type(personas))

for persona in personas:
    persona.mostrar_persona()