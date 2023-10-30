import itertools


def generador():
    num = 1
    while True:
        yield num
        num +=1


def mi_generador():
    for x in itertools.count(1):
        yield x

def generador_de_multiplos_de_7():
    numero = 7
    while True:
        yield numero
        numero += 7

# Crear una instancia del generador
generador = generador_de_multiplos_de_7()

# Ejemplo de uso
for _ in range(5):  # Obtener los primeros 5 múltiplos de 7
    print(next(generador))

def generador_restar_vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te quedan 1 vida"
    yield "Game Over"

perder_vida = generador_restar_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))