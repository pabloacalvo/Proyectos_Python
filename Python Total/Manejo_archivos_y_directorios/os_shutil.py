import os
import shutil
import send2trash

#Conocer directorio actual

print(os.getcwd())

archivo = open('curso.txt','w')
archivo.write('Texto de prueba')
archivo.close()
#Listar archivos y quedan en una lista
print(os.listdir())

#Mover archivos
#shutil.move('curso.txt','C:\\Users\\pc250282')

#Borrar archivos de forma segura porque los mueve a la papelera
#send2trash.send2trash('C:\\Users\\pc250282\\curso.txt')

print(os.walk('C:\\Users\\pc250282\\Europa'))

# genera carpeta, subcarpetas y archivos
ruta = 'C:\\Users\\pc250282\\Europa'

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f"en la carpeta {carpeta}")
    print(f"Las subcarpetas son :")
    for sub in subcarpeta:
        print(f'\t {sub}')
    print(f"Los archivos son: ")
    for arch in archivo:
        #Ver si el nombre comienza con(2015)
        if arch.startswith('2015'):
            print('Encontrado')
        print(f'\t {arch}')
    print('\n')