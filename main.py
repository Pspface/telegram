from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


TOKEN = '6043120582:AAH8VcHc-K7aTE97Sba0BjlcvFqS6dn5nf8'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url="https://itproger/telegram.html")))
    await message.answer('Привет, мой друг!', reply_markup=markup)

executor.start_polling(dp)