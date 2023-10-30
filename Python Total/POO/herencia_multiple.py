class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Ave,Reptil, Pez, Mamifero):
    tiene_pico = True
    vertebrado = True
    venenoso = True

    def poner_huevos(self):
        pass

    def nadar(self):
        pass

    def caminar(self):
        pass

    def amamantar(self):
        pass


print(Ornitorrinco.mro())


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def __init__(self,color_ojos,tipo_pelo,altura,voz,deporte_preferido):
        super().__init__(color_ojos,tipo_pelo,altura,voz,deporte_preferido)

    def reir(self):
        pass
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
    def caminar(self):
        pass
