try:
    nombre = input('Cual es tu nombre: ')
    if len(nombre)>1:
        nombre_usuario = 'El nombre es '+nombre
    print(nombre_usuario)
except:
    print('ocurrio un error')

else:
    print('todo funciono')
finally:
    print('fin de la iteracion')

# Multiples excepciones

try:
    numero = int(input('numero para elevarlo al cuadrado: '))
    print(f'el cuadrado es: {str(pow(numero,2))}')
except TypeError:
    print('Debes convertir los numeros a entero')

except ValueError:
    print('Introduce un numero correcto')
except Exception as e:
    print(type(e))
    print(f'Ocurrio un error: {e}')

# Personalizar un error
try:
    nombre = input('Introduce el nombre: ')
    edad =int(input('Introduce tu edad: '))

    if(5< edad>120):
        raise ValueError('La edad introducida no es real')
    elif(len(nombre)<= 1):
        raise ValueError('El nombre no esta completo')
    else:
        print(f'Bienvenido {nombre} de edad {edad}')
except ValueError:
    print('introduce los datos correctamente')