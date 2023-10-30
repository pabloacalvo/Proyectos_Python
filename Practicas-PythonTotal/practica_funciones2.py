from random import randint
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2



def evaluar_jugada(dados):
    suma_dados = 0
    for num in resultado:
        suma_dados += num
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}.Lamentable"
    elif  6 < suma_dados < 10:
        return f"La suma de tus dados {suma_dados}. Tiene buenas chances"
    elif suma_dados > 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora" 

def evaluar_jugada_2(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}.Lamentable"
    elif  6 < suma_dados < 10:
        return f"La suma de tus dados {suma_dados}. Tiene buenas chances"
    elif suma_dados > 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"   

dados = lanzar_dados()
print(dados)
print(evaluar_jugada_2(dados[0],dados[1]))