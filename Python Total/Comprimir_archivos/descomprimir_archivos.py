import zipfile
import shutil
"""
# Con ZipFile
zip_abiero = zipfile.ZipFile('Archivo_comprimido.zip','r')

#zip_abiero.extract() uno solo
zip_abiero.extractall()
"""

shutil.unpack_archive('Todo_comprimido.zip', 'Todo_descomprimido','zip')