"""
Proyecto Python MySql
-Abrir asistente
-Login o registro
-Si elegimos registro, creara un usuario en la bbdd
-Si elegimos login, identifica al usuario y nos preguntara
    Crear nota,mostrar nota, borrar nota
"""
from usuarios import acciones
print('Acciones disponibles'.center(50,'-'))
print("""
        -Registro
        -Login
""")
hazEL = acciones.Acciones()
accion = input("Elegir opcion: ")
if accion.lower() == "registro":
    hazEL.registro()
elif accion.lower() == "login":
    hazEL.login()
