from pathlib import Path
import os
from os import system

# Mostrar menu de inicio
menu = 0
mi_ruta = Path(Path.home(),'Recetas')
finalizar_programa = False
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1
    return contador

def inicio():
    system('cls')
    print("  Bienvenido  ".center(100,'*'))
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Tenes disponible {contar_recetas(mi_ruta)} recetas")
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elegi una opcion: ")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir
        """)
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("Categorias".center(20,'*'))
    ruta_categoria = Path(ruta)
    lista_categorias = []
    contador = 0
    #Iteramos dentro de las carpetas del directorio
    for carpeta in ruta_categoria.iterdir():
        contador += 1
        carpeta_str = str(carpeta.name)
        lista_categorias.append(carpeta)
        print(f"[{contador}] - {carpeta_str}")
    return lista_categorias

def elegir_categoria(lista):
    elegir_correcta = 'x'
    while not elegir_correcta.isnumeric() or int(elegir_correcta) not in range(1,len(lista)+1):
        elegir_correcta = input("\nElige una categoria: ")
    return lista[int(elegir_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas".center(20, '*'))
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 0
    for receta in ruta_recetas.glob("*.txt"):
        contador += 1
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
    return lista_recetas


def elegir_receta(lista):
    elegir_correcta = 'x'
    while not elegir_correcta.isnumeric() or int(elegir_correcta) not in range(1, len(lista) + 1):
        elegir_correcta = input("\nElige una receta: ")
    return lista[int(elegir_correcta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribi el nombre de tu receta: ")
        nombre_receta = input()+'.txt'
        contenido_receta=input("Escribi la receta: ")
        ruta_nueva = Path(ruta,nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} fue guardada")
            existe = True
        else:
            print("Esa receta ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        nombre_categoria = input("Escribi de la nueva categoria: ")
        ruta_nueva = Path(ruta,nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPrecione V para volver al menu: ")


while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if  len(mis_recetas) <1 :
            print("No hay recetes en esa categoria")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True


