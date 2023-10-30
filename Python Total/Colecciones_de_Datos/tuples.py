# Tupla dentro de otra, son inmutables, mas eficientes
# ocupan menos espacio
mi_tuple = (1,2,(10,20),3,4)
t = (1,5.5,'ff')
t = list(t)
print(type(t))
t = tuple(t)
print(type(t))
print(mi_tuple[2][1])
# asinacion de variables con datos de tuplas, deben haber la misma
# cantidad de elementos
x,y,z = t

tupla2 = (1,2,3,1)
print(len(tupla2))
# contar cantidad de apariciones de un elemento
print(tupla2.count(1))
#consultar indice del elemento
print(tupla2.index(2))