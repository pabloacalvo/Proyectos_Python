letras = []
lista_texto = []
texto = input('Ingresa un mensaje: ')
letras.append(input('Ingresa la primera letra: '))
letras.append(input('Ingresa la segunda letra: '))
letras.append(input('Ingresa la tercer letra: '))

texto = texto.lower()
for letra in letras:
    print(f'La letra {letra} aparece {texto.count(letra)} de veces en el texto que ingresaste')

lista_texto = texto.split()
print(f'El texto que ingresaste tiene {len(lista_texto)} palabras')

print(f'Primer letra del texto: {texto[0]}')
print(f'Ultima letra del texto: {texto[-1]}')
lista_texto.reverse()
texto_invertido = ' '.join(lista_texto)
print(f'Si invirtieramos el orden las palabras en el texto quedaria: \n {texto_invertido}')
if 'python' in texto:
    print('Verdadero, Python se encuentra en el texto ingresado')
else:
    print('Falso, Python no se encuentra en el texto ingresado')





