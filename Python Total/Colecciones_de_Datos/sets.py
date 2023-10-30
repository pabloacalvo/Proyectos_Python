# Los set reciben un solo elemento, por eso los corchetes parenticis o llaves
mi_set = set([1,2,3,4,5])

otro_set = {1,2,3}
print(type(otro_set))

# No pueden tener elementos duplicados, no pueden contener listas ni diccionarios dentro
mi_set2 = set((1,1,1,(1,1,1),5,5,5,3))

print(mi_set2)
print(1 in mi_set2)
# Union de sets
s1 = {1,2,3,10,20,30}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
# Agregar
s1.add(4)
print(s1)
# Eliminar
s1.remove(3)
print(s1)
# Descarta un elemento que puede o no existir, sino existe no generar error
s1.discard(6)
# Elimina un elemento aleatorio
s1.pop()
print(s1)
# Vaciar set
s1.clear()
print(s1)
