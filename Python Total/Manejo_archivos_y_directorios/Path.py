from pathlib import Path

# Ruta absoluta
base = Path.home('')
print(base)
# Ruta relativa
# guia =Path('Barcelona','Sagrada_Familia')

#Convinando ruta obsoluta, con argumentos mas otro objeto path

guia = Path(base,'Europa','España',Path('Barcelona','Sagrada_Familia'))
print(guia)

#guia2 = guia.with_name('La_Pedrera.txt')

#Devuelve la carpeta anterior del elemento
print(guia.parent)
print(guia.parent.parent)