"""
Crear un programa que consulte nombre, apellido, fecha de nacimiento y cree un ID unico con 4 valores nuericos aleotarios

"""
from random import randint
def crear_id():
    print('*** Sitema de ID Unico ***')
    nombre = input("Ingresa tu nombre: ").upper()
    apellido = input("Ingresa tu apellido: ").upper()
    year_nac = input("Ingresa tu año de nacimiento: ")

    num_aleotorio = randint(0,9999)

    id = f'{nombre[0:2]}{apellido[0:2]}{year_nac[2:4]}{num_aleotorio}'

    print(f'Tu ID unico es: {id}')


def crear_mail():
    print('*** Sitema creador de E-mail ***')
    nombre = input("Ingresa tu nombre: ").lower()
    apellido = input("Ingresa tu apellido: ").lower()
    mail = f'{nombre}.{apellido}@ciudadgotica.com'
    print(f"""
    Tu nuevo mail generado por el sistema es:
        {mail}
        *** FELICIDADES ***
    """)

crear_mail()