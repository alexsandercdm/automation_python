
from datetime import date, datetime, timedelta

today = date.today()
print(today)

data = today - today.replace(day=1, year=today.year, month=today.month)
print(f'{data.days}/{today.month}/{today.year}')
