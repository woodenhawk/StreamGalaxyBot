from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#######     inline buttons     #######

inline_btn_1 = InlineKeyboardButton('Сделать заказ', callback_data='MakeOrder') #Make order
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

service_btn = InlineKeyboardButton('Выбрать услугу', callback_data='SelectService') #select service
inline_service = InlineKeyboardMarkup().add(service_btn)

rent_btn = InlineKeyboardButton('Аренда', callback_data='rent')
rec_btn = InlineKeyboardButton('Запись', callback_data='rec')
trans_btn = InlineKeyboardButton('Трансляция', callback_data='trans')

inline_type = InlineKeyboardMarkup().add(rent_btn, rec_btn, trans_btn)

#######     keyboard buttons     #######

button_date = KeyboardButton('/Дата')
greet_date = ReplyKeyboardMarkup()
greet_date.add(button_date)
greet_date = ReplyKeyboardMarkup(resize_keyboard=True).add(button_date)