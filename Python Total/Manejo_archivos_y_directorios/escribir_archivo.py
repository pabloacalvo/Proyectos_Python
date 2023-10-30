registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
linea = '\t'.join(registro_ultima_sesion)+ '\n'
archivo.write(linea)
archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
