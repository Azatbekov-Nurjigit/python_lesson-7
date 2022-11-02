from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
g_1 = KeyboardButton('FRONTEND')
g_2 = KeyboardButton('BACKEND')
g_3 = KeyboardButton('FULLSTACK')
g_4 = KeyboardButton('IOS')
g_5 = KeyboardButton('ANDROID')
g_6 = KeyboardButton('UX\OI')

direction_markup.add(g_1, g_2, g_3).add(g_4, g_5, g_6).add(KeyboardButton('CANCEL'))

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")
share_location = KeyboardButton("Share location", request_location=True)
share_info = KeyboardButton("Share info", request_contact=True)

start_markup.add(start_button, info_button).add(share_location, share_info)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('Нет'))



cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))

