import requests
from datetime import date
from datetime import timedelta

NAME_DAY_API = 'https://svatkyapi.cz/api'

def get_name_day(date):
    request = requests.get(f'{NAME_DAY_API}/day/{date}')
    
    if request.status_code != 200:
        return 'N/A'

    data = request.json()
    return data['name']

today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print(f'Yesterday: {get_name_day(yesterday)}')
print(f'Today: {get_name_day(today)}')
print(f'Tomorrow: {get_name_day(tomorrow)}')
