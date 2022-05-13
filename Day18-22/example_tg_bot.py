from aiogram import Bot, Dispatcher, executor, types
import requests
from pprint import pprint
import json
num=int(input('Введите номер страницы'))
char_rick=requests.get("https://rickandmortyapi.com/api/character?page={num}").json()
#char_rick

#pprint(char_rick)
# def usdvaluta(valuta):
#     for page in range(1, 25):
#         data = requests.get(f'https://rickandmortyapi.com/api/character?page={page}')
#     char_rick = data.json()
#     return f'Покупка {char_rick["results"][""][0][1]} \nПродажа {valuta["data"]["sell"][0][1]}'

def info_get(char_rick):
    data1={}
    for i in range(20):
        data1=(f"имя {i, char_rick['results'][i]['name']}\nвид {char_rick['results'][i]['species']}\nстатус {char_rick['results'][i]['status']}\nфото {char_rick['results'][i]['image']}")
    return data1


import logging
from aiogram import Bot, Dispatcher, executor, types
# Объект бота
bot = Bot(token="5335063016:AAGc67oOlL9b72Y97GFmEiZZJqbAQDxBGiA")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply(info_get(char_rick))
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
