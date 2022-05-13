# zad_10_Bot - название бота
def newsget():
    from bs4 import BeautifulSoup
    import requests
    data = requests.get('https://kaktus.media/')
    soup = BeautifulSoup(data.text, 'html.parser')
    allNews = soup.find('div', class_='Dashboard-Board Dashboard-Board----FORE_MEDIA')
    news = allNews.findAll('a', class_='Dashboard-Content-Card--name')
    text = ''
    for i in news:
        text += str(i.text)
    return text
import logging
from aiogram import Bot, Dispatcher, executor, types
# Объект бота
bot = Bot(token="5392920690:AAEUyDHZor5gO6fr9cylQZoaP4UGeZh16Kc")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply(newsget())
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
