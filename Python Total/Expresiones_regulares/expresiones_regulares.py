import re

texto =  'llama al 564-525-6588 ya mismo'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'


resultado = re.search(patron,texto)
print(resultado)
#Obtengo el valor
print(resultado.group())

resultado2 = re.search(patron2,texto)
print(resultado2)


# Busqueda por grupos para obtener por indice
patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado3 = re.search(patron3,texto)
print(resultado3.group(1))
print(resultado3.group(2))
print(resultado3.group(3))

# Uso practico para validar creacion de contraseñas

clave = input('Clave: ')
patron_clave = r'\D{1}\w{7}'
chequear = re.search(patron_clave,clave)
print(chequear)


texto_t = "No atendemos los lunes por la tarde"
buscar1 = re.search(r'lunes|martes',texto_t)
#Comodin:  cada punto es caracter adicional que obtenemos
buscar2 = re.search(r'.....demos',texto_t)
print(buscar2)
#verificar si esta al comienzo del string
buscar3 = re.search(r'\D^',texto_t)
#verificar si no hay un digito al final del string
buscar4 = re.search(r'\D$',texto_t)
#Excluir algo del patron
buscar5 = re.findall(r'[^\s]+',texto_t)
print(''.join(buscar5))

print




