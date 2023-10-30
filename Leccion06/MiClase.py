class MiClase:
    variable_clase = "Valor variable de clase"

    def __init__(self, variable_instancia):
        self.variable_intancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

MiClase.metodo_clase()
miObjeto1 = MiClase('varible_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()