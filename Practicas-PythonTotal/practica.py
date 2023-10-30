a =",,,,____:::Pablo_--%$$##"
print(a.lstrip(","))

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = (marcas_smartphones.isdisjoint(marcas_tv))
print(conjuntos_aislados) 

def invertir_palabra(palabra):
    return palabra[::-1]
palabra ="Pablo"
print(invertir_palabra(palabra))

def todos_positivos(numeros):
    for num in numeros:
        if num < 0:
            return False
    return True

lista_numeros = [1,2,3,-4,5,-10]
print(todos_positivos(lista_numeros))

def cantidad_pares(lista_numeros):
    resultado = 0
    for num in lista_numeros:
        if num % 2 == 0:
            resultado += num
    return resultado


lista_numeros = [1,50,502,755,34]
print(cantidad_pares(lista_numeros))