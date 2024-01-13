### Error Types ###

# SyntaxError = Codigo mal escrito
# Name error = Variables sin definidir

# Index error = Lista fuera de rango
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
##print(my_list[5])

# Module Not Found = Modulo que no existe
##import maths
import math

# AttributeError = Accedo a un atributo que no existe
##print(math.PI)
print(math.pi)

# Key error = Error de clave que se intenta consultar
my_dict = {"Nombre":"Pablo", "Apellido":"Calvo", "Edad":31, 1:"Python"}
print(my_dict["Edad"])
##print(my_dict["Apellid"])
print(my_dict["Apellido"])

# TypeError = Error en el tipo de variable o atributo
##print(my_list["0"])
print(my_list[0])

# ImportError = error en el import del modulo
##from math import PI
from math import pi as PI_VALUE
print(PI_VALUE)

# ValueError
my_int = int("10")
##my_int = int("10 años")
print(type(my_int))

