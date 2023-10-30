def  reducir_lista(lista):
    lista_nueva = []
    num_max = 0
    for num in lista:
        if num_max < num:
            num_max = num
        if num not in lista_nueva:
            lista_nueva.append(num)
    lista_nueva.remove(num_max)
    return lista_nueva

def  reducir_lista2(lista):
    num_max = 0
    for num in lista:
        if num_max < num:
            num_max = num
        elif num_max  != num:
            lista.append(num)
    lista.remove(num_max)
    return lista

def promedio(lista):
    resultado = 0
    for num in lista:
        resultado += num
    return resultado / len(lista)


lista_numeros = [1,2,7,8]

print(reducir_lista(lista_numeros))
print(promedio(lista_numeros))