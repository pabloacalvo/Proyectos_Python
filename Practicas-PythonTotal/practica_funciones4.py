from random import choice
def lanzar_moneda():
    lista_moneda = ['Cara','Cruz']
    return choice(lista_moneda)

def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print("La lista se autodestruira")
        lista = []
        return lista
    if resultado == 'Cruz':
        print("La lista fue salvada")
        return lista

lista_numeros = [1,2,3,4]
result = lanzar_moneda()
print(probar_suerte(result,lista_numeros))