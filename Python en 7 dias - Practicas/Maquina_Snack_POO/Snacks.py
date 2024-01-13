from Snack import Snack
class Snacks:

    lista_snacks =[
            Snack('Papas',70),
            Snack('Bananas',80),
            Snack('Refresco',30)
        ]

    def add_snack(self,snack):
        Snacks.lista_snacks.append(snack)
        print(f'El snack {snack.nombre} se agrego con exito')

    def __str__(self):
        snacks_str = ''
        for snack in Snacks.lista_snacks:
            snacks_str += '\n' + snack.__str__()

        return f""" *** Snacks en el inventario ***
        {snacks_str}"""

