def devuelve_ciudades( *ciudades ):
    for element in ciudades:
        yield element


ciudades_devueltas = devuelve_ciudades('Madrid','Buenos Aires', 'Lanus', 'Barcelona')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))