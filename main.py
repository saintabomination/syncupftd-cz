import requests
from datetime import date
from datetime import datetime
from datetime import timedelta

EXCHANGE_RATE_API='https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest'
TARGET_CURRENCY='czk'
DATE_FORMAT = '%d.%m.%Y'
TIME_FORMAT = '%H:%M:%S'
NAME_DAY_API = 'https://svatkyapi.cz/api'

def get_exchange_rate(input_currency, output_currency):
    try:
        request = requests.get(f'{EXCHANGE_RATE_API}/currencies/{input_currency}/{output_currency}.json')
        data = request.json()
        return data[TARGET_CURRENCY]
    except:
        return 'N/A'

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

print('\nMěny\n')
print(f'USD: {get_exchange_rate("usd", TARGET_CURRENCY)} {TARGET_CURRENCY.upper()}')
print(f'EUR: {get_exchange_rate("eur", TARGET_CURRENCY)} {TARGET_CURRENCY.upper()}')
print(f'GPB: {get_exchange_rate("gbp", TARGET_CURRENCY)} {TARGET_CURRENCY.upper()}')

print('\nSvátky\n')
print(f'Yesterday: {get_name_day(yesterday)}')
print(f'Today: {get_name_day(today)}')
print(f'Tomorrow: {get_name_day(tomorrow)}')
