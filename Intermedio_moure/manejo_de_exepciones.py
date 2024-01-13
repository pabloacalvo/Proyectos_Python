import math

def calculaRaiz(num):
    if num < 0:
        raise ValueError ("El numero no puede ser negativo")
    return math.sqrt(num)

def divide ():
    while True:
        try:
            op1 =  (float(input("Primer numero")))
            op2 = (float(input("Segundo numero")))
            print ("La division es " + str(op1/op2))
            break
        except ValueError:
            print("El valor introcido es erroneo")
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        finally: # se ejecuta siempre
            print("Calculo finalizado")

def evalueEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad < 20:
        return "Muy joven"
    if edad > 40:
        return "Sos joven"
    if edad > 65:
        return "Eres Maduro"
    if edad > 100:
        return "Cuidate"

op = float(input("Ingresa un numero: "))
try:
    print(calculaRaiz(op))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
print("Programa terminado")