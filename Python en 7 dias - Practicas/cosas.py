# for i in range(6):
#     if i %2 == 0:
#         print(f'valor: {i}')
# print("Ejercio 1")
# for numero in range(10):
#     if numero % 3 == 0:
#         print(numero)
#
# print("Ejercio 2")
#
# for numero in range (2,7):
#     print(numero)
#
# print("Ejercio 3")
# for numero in range(3, 11, 2):
#     print(numero)

tupla= (13,1,8,3,2,5,8)

#tupla=list(tupla)
# list=[]
# for numero in tupla:
#     if numero <5:
#         list.append(numero)
# print(list)

# diccionario = {
#     'IDE': 'Integrated Development Environment',
#     'OOP': 'Object Oriented Porgramming',
#     'DBMS':'Database Management System'
# }
#
# print(diccionario)
# print(diccionario.get('OOP'))
# print(len(diccionario))
#
# #agregar diccionario
# diccionario['PK'] ='Primary Key'
# print(diccionario)
#
# #remover
# diccionario.pop('DBMS')
# print(diccionario)
#
# #limpiar
# diccionario.clear()
# print(diccionario)

#*nombres se transforma en una tupla
def sumarNum(*args):
    suma=0
    for num in args:
        suma+=int(num)
    return suma

print(sumarNum(2,3,4,5,6,7,8))
print(sumarNum(2,2))

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos(NOMBRE='Pablo',APELLIDO='Calvo')


pago_sin_impuestos=input(f'Proporciones el pago sin impuestos')
pago_monto_impuestos=input(f'Proporciones el monto del impuestos')


def calcularImmpuestos(*args,impuesto):
    total=0
    for datos in args:
        total+=datos
