import logging
import aiogram
import RequestDB
import Button
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5412361981:AAF7i8e5LIQP0CrF6aYdLCMU6dLN8Sh2paI'



# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])    #write 'start' to start bot
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=Button.inline_kb1)

@dp.message_handler(commands=['help'])    #write 'help' to get list commands
async def help(message: types.Message):
    await message.reply("/start - начать\n"
                        "/help - команды")

@dp.callback_query_handler(lambda c: c.data == 'MakeOrder')     #Make order
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Создание заказа!', reply_markup=Button.inline_service)

@dp.callback_query_handler(lambda c: c.data == 'SelectService')     #Select Service
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выбери услугу', reply_markup=Button.greet_kb)


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Некорректные данные')


if __name__ == '__main__':
    executor.start_polling(dp)