from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_1 = InlineKeyboardButton('Сделать заказ', callback_data='MakeOrder')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

service_btn = InlineKeyboardButton('Выбрать услугу', callback_data='SelectService')
inline_service = InlineKeyboardMarkup().add(service_btn)

button_hi = KeyboardButton('Привет! 👋')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)