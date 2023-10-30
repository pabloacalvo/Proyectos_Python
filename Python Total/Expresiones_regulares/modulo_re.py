import re

"""
/d -> digito numerico
/w -> digito alfanumerico
/s -> espacio en blanco
/D -> no numerico
/W -> no alfanumerico
/S -> no es un espacio en blanco

Cuantificadores

+ -> aparece 1 o mas veces
{n} -> se repite n veces
{n,m} -> se repite entre n m veces
{n,} -> de n veces hacia arriba
* -> cero o mas veces
? -> 1 o cero veces
"""

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio online"

patron = 'ayuda'
# Obtengo un objeto
busqueda = re.search(patron,texto)
print(busqueda)
# Obtengo una lista con la busqueda
busqueda2  = re.findall(patron,texto)
print(busqueda.span)
for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())