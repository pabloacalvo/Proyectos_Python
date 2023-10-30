#
palabra = 'python'
lista = [letra for letra in palabra]
lista2 = [numero for numero in range(0,20,2)]
lista3 = [numero/2 for numero in range(0,20,2)]
lista4 = [numero/2 for numero in range(0,20,2) if numero *2 >10]
lista4 = [numero for numero in range(0,20,2) if numero * 2 >10]
lista5 = [numero if numero * 2 > 10 else 'No lo es' for numero in range(0,20,2)]
print(lista)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

pies = [10,20,30,40,50]
metros = [pie * 3.3281 for pie in pies]
print(metros)

temperatura_fahrenheit = [32, 212, 275]
grados_celcius = [(far -32)*(5/9) for far in temperatura_fahrenheit]
print(grados_celcius)
