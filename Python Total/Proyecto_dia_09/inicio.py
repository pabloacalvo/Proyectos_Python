import datetime
import os
import re
from pathlib import Path
import time
import math

inicio = time.time()

patron = r'N\D{3}-\d{5}'
date_now = datetime.date.today()
nro_encontrados = []
archivo_con_datos = []
ruta = './Mi_Gran_Directorio'

def buscar_patron(archivo, patron):
    file = open(archivo, 'r')
    texto = file.read()
    busqueda = re.search(patron,texto)
    if busqueda is not None:
        return re.search(patron,texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            resultado = buscar_patron(Path(carpeta,arch),patron)
            if resultado != '':
                nro_encontrados.append((resultado.group()))
                archivo_con_datos.append(arch.title())

def mostrar_resultado():
    indice = 0
    print('-'*50)
    print(f'FECHA DE BUSQUEDA: {date_now.day}/{date_now.month}/{date_now.year}')
    print('\n')
    print('ARCHIVO \t\t\tNRO SERIE')
    print('--------\t\t\t--------')
    for a in archivo_con_datos:
        print(f'{a}\t{nro_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(nro_encontrados)}')
    fin = time.time()
    duracion = fin -inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} seegundos')
    print('-'*50)

crear_listas()
mostrar_resultado()






