import notas.nota as modelo

class Acciones:
    def crear(self,usuario):
        print(f"Ok,{usuario[1]} vas a crear una nueva nota...")
        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = input("Introduce la nota: ")
        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"{nota.titulo} fue guardada con exito".center(50,'-'))
        else:
            print(f'\n No se ha guardado la nota, {usuario[1]}')


    def mostrar(self, usuario):
        print(f"Ok, {usuario[1]} estas son tus notas:\n")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        if len(notas)==0:
            print('No hay notas para mostrar')
        else:
            for nota in notas:
                print(''.center(50,'*'))
                print(f'- Titulo: {nota[2]}\n')
                print(f'{nota[3]}\n')
                print(''.center(50,'*'))
            print('Fin de tus notas'.center(50,'-'))

    def borrar(self,usuario):
        print(f"Ok, {usuario[1]} vas a borrar notas ".center(50,'-'))
        titulo = input("Ingresa el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0],titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >=1:
            print(f"Tu nota {nota.titulo} se ha borrado")
        else:
            print(f"No se ha borrado la nota: {nota.titulo}")
        