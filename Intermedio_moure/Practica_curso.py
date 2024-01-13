def conversor_celsius(dato):
    grados = ((dato - 32 ) * 5 )/ 9
    return print(f"Son {grados.__round__()} °C")

def conversor_fahrenheit(dato):
    fahrenheit = (((dato * 9)) / 5) + 32
    return print(f"Son {fahrenheit.__round__()} °F")


dato = float(input("Decime un valor a convertir"))
conversor_fahrenheit(dato)
conversor_celsius(dato)