def numeros_farmacia():
    for n in range(1,100):
        yield f"F-{n}"

def numeros_perfumeria():
    for n in range(1,100):
        yield f"P-{n}"

def numeros_cosmetica():
    for n in range(1,100):
        yield f"F-{n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador_turnos(rubro):
    print("Su turno es".center(25,'*'))
    if rubro == 'P':
        print(next(p).center(25))
    if rubro == 'F':
        print(next(f).center(25))
    if rubro == 'C':
        print(next(c).center(25))
    print("-"*25)
    print("Aguarde y sera atendido".center(25))
    print("-" * 25)
