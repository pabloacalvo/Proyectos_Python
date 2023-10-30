import datetime
from datetime import datetime
from datetime import date

#mi_hora = datetime.time(17,35)
#mi_dia = datetime.date(2025,10,17)
mi_fecha = datetime(2025,5,15,22,10,15,2500)

#print(mi_dia.today())
print(mi_fecha)

nacimiento = date(1991,12,31)
actual = date.today()

vida = actual - nacimiento
print(vida)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)

vigilia = duerme - despierta
print(vigilia.min)


import datetime

hora_actual = datetime.datetime.now()

print(hora_actual)
print(hora_actual.day)
print(hora_actual.month)
print(hora_actual.year)
print(hora_actual.minute)