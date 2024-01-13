#Con el generador la funcion entra en suspension, utilizando el metodo next gano eficiencia
# util para funciones que devuelvan valores infinitos o programas que vana  consumir muchos recursos

def generaPares(limite):
    num = 1
    miLista=[]
    while num < limite:
        miLista.append(num*2)
        num += 1
    return miLista

def generaParesWithGenerador(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1
devuelvePares = generaParesWithGenerador(10)

print(next(devuelvePares))
print('Aqui podria ir mas codigo')
#print(generaPares(20))

print(next(devuelvePares))
print('Aqui podria ir mas codigo')

print(next(devuelvePares))
print('Aqui podria ir mas codigo')