from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print(f'Yesterday: {yesterday}')
print(f'Today: {today}')
print(f'Tomorrow: {tomorrow}')
