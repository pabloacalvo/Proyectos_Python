from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta

print('Creacion Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(-5,'Rojo')

print(f'Area del cuadrado: {cuadrado1.calcular_area()}')

print('Creacion Objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(3,1,'Azul')
rectangulo1.ancho = -10
print(rectangulo1)
print(f'Area del rectangulo: {rectangulo1.calcular_area()}')


