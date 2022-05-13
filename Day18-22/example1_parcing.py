import json
import pprint
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types

r = requests.get(f'https://openweathermap.org/')
print(r.text)
city = r.json()['name']
data = datetime.datetime.fromtimestamp(r.json()['dt'])
temp = r.json()['main']['temp']
humi = r.json()['main']['humidity']
sunrise = datetime.datetime.fromtimestamp(r.json()['sys']['sunrise'])
sunset = datetime.datetime.fromtimestamp(r.json()['sys']['sunset'])

print(r.status_code)
print(r.text)