numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    #print(f'{nombre} se encuentra en el indice {indice}')
    if nombre.startswith('M'):
        print(nombre)

lista = list(enumerate('Python'))
print(lista)

