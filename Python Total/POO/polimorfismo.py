palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


def iterador(*args):
    for arg in args:
        print(len(arg))


iterador(palabra, lista, tupla)


class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

def iterador(*args):
    for arg in args:
        arg.atacar()


mago1=Mago()
arquero1=Arquero()
samurai1=Samurai()

iterador(arquero1,mago1,samurai1)

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")




mago1=Mago()
arquero1=Arquero()
samurai1=Samurai()

lista_personajes = [arquero1,mago1,samurai1]
for personaje in lista_personajes:
    personaje.atacar()


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return print(f"\"{self.titulo}\", de {self.autor}")

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        return print('"Libro eliminado"')

libro1 = Libro('It', 'Stephen King', 10)

libro1.__str__()
print(libro1.__len__())
libro1.__del__()


