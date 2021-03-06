import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types

ow_api = '32df5beb2d7d555fd8c950fcf2b48e99'
tg_bot_token = '5335063016:AAGc67oOlL9b72Y97GFmEiZZJqbAQDxBGiA'


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.reply('Hello')

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={ow_api}&units=metric&lang=ru')
        city = r.json()['name']
        data = datetime.datetime.fromtimestamp(r.json()['dt'])
        temp = r.json()['main']['temp']
        humi = r.json()['main']['humidity']
        sunrise = datetime.datetime.fromtimestamp(r.json()['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(r.json()['sys']['sunset'])

        await message.reply(f'Ваш город - {city} \n Время - {data} \n Температура - {temp} \n Влажность - {humi} \n Восход - {sunrise} \n Закад - {sunset}')
    except:
        await message.reply('Что-то пошло не так')

if __name__ == '__main__':
    executor.start_polling(dp)