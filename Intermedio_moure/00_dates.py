### Dates ####

from datetime import datetime

now = datetime.now()
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(now)

print(now.timestamp())
year_2023 = datetime(2023,1,1,3)

print_date(year_2023)

from datetime import time

current_time = time(21,6,28)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)



from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
