import datetime
from datetime import datetime
from datetime import date

#mi_hora = datetime.time(17,35)
#mi_dia = datetime.date(2025,10,17)
mi_fecha = datetime(2025,5,15,22,10,15,2500)

#print(mi_dia.today())
#print(mi_fecha)

nacimiento = date(1991,12,31)
actual = date.today()

vida = actual - nacimiento
#print(vida)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)


vigilia = duerme - despierta
#print(vigilia.min)

prueba = date(2023,12,27)
prueba = prueba.strftime("%d-%m-%Y")
value = '27-12-2023'
prueba_2 = datetime.strptime(value,"%d-%m-%Y")

# Crear un objeto date dandole como parametro un string y un formato
prueba_3 = datetime.strptime('27-12-2023','%d-%m-%Y')

print(prueba_2)
# Transformar a string
prueba_2 = prueba_2.strftime("%Y%m%d")
print(prueba_2)


"""valor = prueba_2 - prueba_3
if valor.days >= 1:
    print('holas')
else:
    print('chau')"""




"""hora_actual = datetime.datetime.now()

print(hora_actual)
print(hora_actual.day)
print(hora_actual.month)
print(hora_actual.year)
print(hora_actual.minute)"""