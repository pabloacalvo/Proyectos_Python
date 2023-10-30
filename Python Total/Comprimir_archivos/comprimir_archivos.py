import zipfile
import shutil


"""
#Crear y comprimir con zipfile

mi_zip = zipfile.ZipFile('Archivo_comprimido.zip','w')

mi_zip.write('L_JVM010.LOG')
mi_zip.write('Compota de Manzana.txt')

mi_zip.close()

"""

carpeta_origen = 'C:\\Users\\pc250282\\Recetas'

archivo_destino = 'Todo_comprimido'

shutil.make_archive(archivo_destino, 'zip',carpeta_origen)



