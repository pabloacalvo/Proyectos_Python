import os

#ruta actual
ruta = os.getcwd()

# asignar ruta
#ruta = os.chdir('C:\\Users\\pc250282\\OneDrive - NCR Corporation\\Desktop')
#ruta = 'C:\\Users\\pc250282\\OneDrive - NCR Corporation\\Desktop\\dc.txt'

#Obtengo la ruta del archivo
elemento = os.path.dirname(ruta)
elemento = os.path.basename(ruta)

#Devulve una tupla con la ruta y el nombre de base
elemento = os.path.split(ruta)

#Eliminar directorio
#os.rmdir('C:\\Users\\pc250282\\OneDrive - NCR Corporation\\Desktop\\nueva')

# Crea la carpeta
#ruta = os.makedirs('C:\\Users\\pc250282\\OneDrive - NCR Corporation\\Desktop\\nueva')
#archivo = open('dc.txt')
#print(archivo.read())

# Para todos los sistemas operativos
from pathlib import Path

# Forma de abrir, concatenando la carpeta con el archivo
#carpeta = Path('/Users/pc250282/OneDrive - NCR Corporation/Desktop')
#archivo = carpeta / 'dc.txt'

#Misma forma pero enviando toda la ruta completa, se le pude quitar el C: para windows y funciona
carpeta = Path('/Users/pc250282/OneDrive - NCR Corporation/Desktop/dc.txt')
mi_archivo = open(carpeta)
print(mi_archivo.read())
