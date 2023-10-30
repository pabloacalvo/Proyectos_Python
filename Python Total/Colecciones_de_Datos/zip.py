nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Buenos aires','Barcelona']

combinados =list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")

v = 'hola'
print(v.lower())

