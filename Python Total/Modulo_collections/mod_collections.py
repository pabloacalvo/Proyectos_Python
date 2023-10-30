from collections import Counter, defaultdict, namedtuple

# Counter cuenta elementos

serie = Counter([1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,4,4,4,4,4,4])
# Muestra los mas frecuentes si dentro del paretensis pongo 1 o 2 me muestra el que mas aparece o sel segundo q mas aparece
print(serie.most_common())

#Crea una lista de elementos unicos
print(list(serie))

# Se coontruye en nuevo valor en base una busqueda que deberia a ver dado error
mi_dic = defaultdict(lambda:'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['cuatro'])
print(mi_dic)

# Tupla nominada
Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.75,79)
print(ariel.nombre)