from random import *
aleatorio = randint(1,50) # Enteros
aleatorio2 = uniform(1,50) # Decimales
aletorio3 = random() # Decimal entre 0 y 1
colores = ['Rojo','Verde','Amarillo']
aleatorio4 = choice(colores) # Aleatorio de una lista
numeros = list(range(5,50,5))
shuffle(numeros) # Mezcla una lista
print(aleatorio,aleatorio2,aletorio3,aleatorio4,numeros)