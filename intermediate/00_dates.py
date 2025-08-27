### Dates ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.timestamp())

print_date(now)

# crear una fecha a partir de unos datos

year_2025 = datetime(2025, 1, 1)

print(year_2025)

from datetime import time

current_time = time(21, 6, 10)

print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2025, 8, 27)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day + 2)
print(current_date)

from datetime import timedelta

