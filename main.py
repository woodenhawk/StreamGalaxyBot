import logging
import aiogram
import logging
import os
from datetime import datetime
from aiogram_datepicker import Datepicker, DatepickerSettings
import RequestDB
import Button

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery

API_TOKEN = '5412361981:AAF7i8e5LIQP0CrF6aYdLCMU6dLN8Sh2paI'



# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



class DatePick(StatesGroup):
    waiting_for_date = State()
    wait_name = State()
    wait_email = State()
    wait_phone = State()


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
    print(callback_query.from_user.id)
    RequestDB.InsertUser(callback_query.from_user.id)
    await callback_query.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'SelectService')     #Select Service
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выбери услугу', reply_markup=Button.inline_type)
    await callback_query.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'rent')     #Selected Rent
async def process_callback_rent(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Осталось выбрать дату",reply_markup=Button.greet_date)
    RequestDB.ServiceUser(callback_query.from_user.id, 1, "Без даты")
    await callback_query.message.delete()

@dp.callback_query_handler(lambda c: c.data == 'rec')     #Selected Rent
async def process_callback_rec(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Осталось выбрать дату", reply_markup=Button.greet_date)
    RequestDB.ServiceUser(callback_query.from_user.id, 2, "Без даты")
    await callback_query.message.delete()

@dp.callback_query_handler(lambda c: c.data == 'trans')     #Selected Rent
async def process_callback_rent(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Осталось выбрать дату", reply_markup=Button.greet_date)
    RequestDB.ServiceUser(callback_query.from_user.id, 3, "Без даты")
    await callback_query.message.delete()

# @dp.message_handler(commands=['Добавить'])
# async def Date(message: types.Message):
#     await bot.send_message(message.from_user.id, "Введите дату в формате чч:мм дд.мм.гггг")
#     await DatePick.waiting_for_date.set()

# @dp.message_handler(state=DatePick.waiting_for_date)
# async def date_chosen(message: types.Message, state: FSMContext):
#     print("asdasd")
#     await state.update_data(date_picked=message.text.lower())
#     RequestDB.UpdateServiceUser(message.text, message.from_user.id)
#     await state.finish()
#     await bot.send_message(message.from_user.id, "Добавил")
#____________________________________________________________________________________#

# def register_handlers_food(dp: Dispatcher):
#     dp.register_message_handler(Date, commands="Добавить", state="*")
#     dp.register_message_handler(date_chosen(), state=DatePick.waiting_for_date)


# @dp.message_handler()
# async def echo_message(message: types.Message):
#
#     await bot.send_message(message.from_user.id, 'Отлично')
#     RequestDB.UpdateServiceUser(message.text, message.from_user.id)

#_______________________________________________________________#


DatepickerSettings(
    initial_view='day',  #available views -> day, month, year
    initial_date=datetime.now().date(),  #default date
    views={
        'day': {
            'show_weekdays': True,
            'weekdays_labels': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
            'header': ['prev-year', 'days-title', 'next-year'],
            'footer': ['prev-month', 'select', 'next-month'], #if you don't need select action, you can remove it and the date will return automatically without waiting for the button select
            #available actions -> prev-year, days-title, next-year, prev-month, select, next-month, ignore
        },
        'month': {
            'months_labels': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
            'header': [
                        'prev-year',
                        ['year', 'select'], #you can separate buttons into groups
                        'next-year'
                       ],
            'footer': ['select'],
            #available actions -> prev-year, year, next-year, select, ignore
        },
        'year': {
            'header': [],
            'footer': ['prev-years', 'next-years'],
            #available actions -> prev-years, ignore, next-years
        }
    },
    labels={
        'prev-year': '<<',
        'next-year': '>>',
        'prev-years': '<<',
        'next-years': '>>',
        'days-title': '{month} {year}',
        'selected-day': '{day} *',
        'selected-month': '{month} *',
        'present-day': '• {day} •',
        'prev-month': '<',
        'select': 'Выбрать',
        'next-month': '>',
        'ignore': ''
    },
    custom_actions=[] #some custom actions

)


def _get_datepicker_settings():
 return DatepickerSettings() #some settings


@dp.message_handler(commands=['Дата'])
async def Pick(message: Message):
 markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
 datepicker = Datepicker(_get_datepicker_settings())

 markup = datepicker.start_calendar()
 await message.answer ('Выберите дату: ', reply_markup=markup)


@dp.callback_query_handler(Datepicker.datepicker_callback.filter())
async def _process_datepicker(callback_query: CallbackQuery, callback_data: dict):
 datepicker = Datepicker(_get_datepicker_settings())

 date = await datepicker.process(callback_query, callback_data)

 if date:
    RequestDB.UpdateServiceUser(date, callback_query.from_user.id)
    await callback_query.message.answer(date.strftime('Добавлена дата: %d/%m/%Y\nНапишите Ваше имя'))
    await DatePick.wait_name.set()


 await callback_query.answer()


# if __name__ == '__main__':
#  executor.start_polling(dp, skip_updates=True)



@dp.message_handler(state=DatePick.wait_name)
async def Name(message: types.Message, state: FSMContext):
    RequestDB.UpdateNameUser(message.text, message.from_user.id)
    await bot.send_message(message.from_user.id, "Отлично\nТеперь напишите e-mail")
    await DatePick.wait_email.set()

@dp.message_handler(state=DatePick.wait_email)
async def Emale(message: types.Message, state: FSMContext):
    RequestDB.UpdateEmailUser(message.text, message.from_user.id)
    await bot.send_message(message.from_user.id, "Прекрасно!\nНапишите телефон")
    await DatePick.wait_phone.set()

@dp.message_handler(state=DatePick.wait_phone)
async def Phone(message: types.Message, state: FSMContext):
    RequestDB.UpdatePhoneUser(message.text, message.from_user.id)
    await state.finish()
    await bot.send_message(message.from_user.id, "Ожидайте ответа администратора")




if __name__ == '__main__':
    executor.start_polling(dp)