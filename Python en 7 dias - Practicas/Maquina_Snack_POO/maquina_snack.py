from Snacks import Snacks
from Snack import Snack

lista_compras = []
total = 0.0
snacks = Snacks()


def menu():
    while True:
        print('*** Maquina de Snacks ***')
        print('Snacks disponibles:')
        print(f'\t1. Comprar snack')
        print(f'\t2. Mostrar ticket')
        print(f'\t3. Crear snack')
        print(f'\t4. Salir')
        opcion = int(input('Elegi una opcion: '))
        if opcion == 1:
            comprar_snack()
        elif opcion == 2:
            mostrar_ticket()
        elif opcion ==3:
            crear_snack()
        elif opcion == 4:
            print('Saliste hasta luego!')
            return

def comprar_snack():
    print(snacks)
    id_snack = int(input('Ingresa el ID del snack a comprar: '))
    snack_encontrado = False
    for snack in snacks.lista_snacks:
        if snack.id == id_snack:
             lista_compras.append(snack)
             snack_encontrado = True
             print(f'Se agrego {snack.nombre} a la lista de compras')
             break

    if not snack_encontrado:
        print('No existe el ID seleccionado')


def crear_snack():
    nombre = input('Ingresa el nombre del snack: ')
    precio = float(input('Ingresa el precio del snack: '))
    nuevo_snack = Snack(nombre, precio)
    snacks.add_snack(nuevo_snack)
    print(snacks)
def mostrar_ticket():
    global total
    print('----------------- Factura -----------------')
    for snack in lista_compras:
        total = total + snack.precio
        print(f'\t{snack.nombre} ...... ${snack.precio}')
    print(f'\t\t TOTAL A PAGAR $: {total}')
    print('-----------------------------')

menu()