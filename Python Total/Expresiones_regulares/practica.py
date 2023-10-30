import re

def verificar_email(email):
    patron = r'\w+\@\w+\.com\w*'   # Cualquier cantidad de caracteres antes y depues del @, luego un .com y luego 0 o mas veces algun caracter(.ar.br.org)
    busqueda = re.search(patron,email)
    if busqueda is not None:
        resultado = 'Ok'
    else:
        resultado = 'La direccion de email es incorrecta'
    return print(resultado)

verificar_email('pablo@live.com')

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    busqueda = re.search(patron,cp)
    if busqueda is not None:
        resultado = 'Ok'
    else:
        resultado = 'El código postal ingresado no es correcto'
    return print(resultado)

verificar_cp('aa9889')