import requests
from datetime import date
from datetime import datetime
from datetime import timedelta

DATE_FORMAT = '%d.%m.%Y'
TIME_FORMAT = '%H:%M:%S'
NAME_DAY_API = 'https://svatkyapi.cz/api'

def get_name_day(date):
    try:
        request = requests.get(f'{NAME_DAY_API}/day/{date}')
        data = request.json()
        return data['name']
    except:
        return 'N/A'
    
current_time = datetime.now()
today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print('SyncUpFTD spuštěn.')
print(current_time.strftime(f'{DATE_FORMAT} {TIME_FORMAT}'))
print('\nSvátky\n')
print(f'Yesterday: {get_name_day(yesterday)}')
print(f'Today: {get_name_day(today)}')
print(f'Tomorrow: {get_name_day(tomorrow)}')
