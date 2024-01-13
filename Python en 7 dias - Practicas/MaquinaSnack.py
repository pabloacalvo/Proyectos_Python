snacks = [
    {'id': 0, 'nombre': 'Papas', 'precio': 300},
    {'id': 1, 'nombre': 'Refresco', 'precio': 300},
    {'id': 2, 'nombre': 'Sadwich', 'precio': 120}
]



lista_compra = []
total = 0.0

def menu():
    while True:
        print('*** Maquina de Snacks ***')
        print('Snacks disponibles:')
        print(f'\t1. Comprar snack')
        print(f'\t2. Mostrar ticket')
        print(f'\t3. Salir')
        opcion = int(input('Elegi una opcion: '))
        if opcion == 1:
            snack_seleccionado = comprar_snack()
            lista_compra.append(snack_seleccionado)
        elif opcion == 2:
            mostrar_ticket(lista_compra)
        elif opcion == 3:
            print('Saliste hasta luego!')
            return


def mostrar_snacks(snacks):
    for snack in snacks:
        print('-----------------------------')
        print(f'ID: {snack["id"]}')
        print(f'NOMBRE: {snack["nombre"]}')
        print(f'PRECIO: {snack["precio"]}')


def comprar_snack():
    mostrar_snacks(snacks)
    snack = int(input('Ingresa el ID del snack a comprar: '))
    snack_seleccionado = snacks[snack]
    print(f'\tCompraste ---> {snack_seleccionado["nombre"]}')
    return snack_seleccionado

def mostrar_ticket(lista_compra):
    global total
    print('----------------- Factura -----------------')
    for snack in lista_compra:
        total = total + snack['precio']
        print(f'\t{snack["nombre"]} ...... ${snack["precio"]}')
    print(f'\t\t TOTAL A PAGAR $: {total}')
    print('-----------------------------')


menu()