import bs4
import requests

# Creamos URL sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1,51):
    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    # Iterar en cada libro de cada pagina
    for libro in libros:
        # Chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # Guardamos ese titulo en una variable
            titulo_libro = libro.select('a')[1]['title']
            # Agregamos el libro a la lista
            titulos_rating_alto.append(titulo_libro)



# Ver los libros en consola
for titulo  in titulos_rating_alto:
    print(titulo)


