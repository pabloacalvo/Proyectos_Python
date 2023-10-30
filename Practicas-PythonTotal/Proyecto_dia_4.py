from random import randint
nombre = input("Decime tu nombre: ")
numero = randint(1,100)
oportunidades = 8
intentos = 0
dato = 0
print(f"Bueno {nombre} he pensado un numero del 1 al 100, y tienes 8 intentos para adviniar cual es el numero ")
while dato != numero and oportunidades != 0:
    dato = int(input(f"Ingresa el numero tenes {str(oportunidades)} oportunidades: "))
    if dato not in range(1,100):
        print(f"El {dato} no esta dentro del rango del 1 al 100")
    elif dato > numero :
        print(f"Mi numero es mas chico que el {dato}")
    elif dato < numero:
        print(f"Mi numero es mas grande que el {dato}")
    elif dato == numero:
        break
    oportunidades -= 1
    intentos += 1
if dato != numero:
    print(f"GAME OVER!!!! el numero era el {numero}")
else:
    print(f"GANASTE!!!! {nombre} ADIVINASTE EN -{intentos}- INTENTOS EL NUMERO ERA EL {numero}!!!!")   


