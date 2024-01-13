

opcion = True
saldo = 0.0
while opcion:
    print("""------------ Bienvenido al cajero automatico de Ciudad Gotica ------------
        ***Opciones disponibles: ***
        1. Consultar saldo
        2.Retirar
        3.Depositar
        4.Salir
    """)
    opcion = int(input('Selecciona una operacion a realizar: '))
    if opcion == 1:
        print(f"Tu saldo es ${saldo} ")
    elif opcion == 2:
        retiro =float(input("Ingrese valor a retirar: "))
        if retiro > saldo :
            print(f"Saldo insuficiente, consula tu saldo y reintenta")
        else:
            saldo -= retiro
    elif opcion == 3:
        deposito =float(input("Ingrese valor a depositar"))
        saldo += deposito
    elif opcion == 4:
        opcion = False
    else:
        print(f'La opcion -{opcion}- no es valida')
print("Saliste del sistema, hasta luego!")