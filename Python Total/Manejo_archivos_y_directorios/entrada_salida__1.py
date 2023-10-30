mi_archivo = open('pruebas.txt')

print(mi_archivo.read())
una_linea = mi_archivo.readline()
todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)