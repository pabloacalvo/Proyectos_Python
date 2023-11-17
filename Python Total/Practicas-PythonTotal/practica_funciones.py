from random import shuffle
palitos = ['-','--','---','----']

def mezclar_palitos(lista):
    shuffle(palitos)
    return lista

def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Te salvaste")
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)