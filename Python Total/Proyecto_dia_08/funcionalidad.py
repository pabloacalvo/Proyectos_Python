from numeros import *

def inicio():
    eleccion = None
    while True:
        try:
            print("Bienvenido elegi una opcion")
            eleccion = input((f"[F] Turno para Farmacia\n[P] Turno para Perfumeria\n[C]Turno para Cosmetica\n[S] Turno para Salir")).upper()
            ['F','P','C','S'].index(eleccion)
        except ValueError:
            print('Opcion Incorrecta')
        else:
            break
    if eleccion == 'S':
        print("Has salido del sistema de turnos")
    else:
        decorador_turnos(eleccion)
        preguntar()


def preguntar():
    while True:
        try:
            otro_turno = input("¿Deseas sacar otro turno? [S] [N]" ).upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('Opcion incorrecta')
        else:
            if otro_turno =='S':
                inicio()
            else:
                print('Gracias por tu visita')
            break


inicio()