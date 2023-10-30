import bs4
import requests
import lxml

#resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/acoplamiento-pilares-de-la-programacion.html')
resultado = requests.get('https://escueladirecta-blog.blogspot.com/blog/26007/encapsulamiento')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# Obtenemos una lista con la etiqueta que buscamos
"""print(sopa.select('title'))
print(sopa.select('title')[0].getText())
parrafo_especial = sopa.select('p')[3].getText()"""

columna_lateral = sopa.select('.first-items')

# Extraer imagenes

'''resultado = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes = sopa.select('.course-box-image')[0]['src']
imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg','wb') # escribir binario
f.write(imagen_curso_1.content)
f.close()'''

