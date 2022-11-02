import random
from aiogram import types , Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from coin import bot, dp
from parser.news import get_data

# @dp.message_handler(commands=['quiz'])
async def s1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Независимость Америки(год)?"
    answers = [
        "1756 лет",
        "1804 лет",
        "1776 лет",
        "1805 лет",
        "1769 лет",
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="неправильно!",
        reply_markup=markup
    )


# @dp.message_handler(commands=['!pin'])
async def eo(message: types.Message):
    await bot.pin_chat_message(message.from_user.id, message.message_id)


# @dp.message_handler(commands=['Mem'])
async def ecco(message: types.Message):
    ff = random.randint(1, 2)
    if ff == 1:
        photo = open('meddia/m.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo)
    elif ff == 2:
        photo = open('meddia/mmm.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo)

# @dp.message_handler(commands=['game'])
async def eco(message: types.Message):
    ds = [1, 2, 3, 4, 5, 6]
    sf = random.choice(ds)
    if sf == 1:
        await bot.send_dice(message.from_user.id, emoji= "⚽️")
    elif sf == 2:
        await bot.send_dice(message.from_user.id, emoji= "🏀")
    elif sf == 3:
        await bot.send_dice(message.from_user.id, emoji= "🎲")
    elif sf == 4:
        await bot.send_dice(message.from_user.id, emoji= "🎯")
    elif sf == 5:
        await bot.send_dice(message.from_user.id, emoji= "🎳")
    elif sf == 6:
        await bot.send_dice(message.from_user.id, emoji="🎰")

# @dp.message_handler(commands=['dice'])
async def dic(message: types.Message):
    await message.answer('ТЫ:')
    dice1 = await bot.send_dice(message.from_user.id,emoji= "🎲")
    dfg1 = (dice1.dice.value)
    await message.answer('БОТ:')
    dice2 = await bot.send_dice(message.from_user.id,emoji= "🎲")
    dfg2 = (dice2.dice.value)
    if dfg1 < dfg2:
        await message.answer('ты проиграл.')
    elif dfg1 == dfg2:
        await message.answer('ничья.')
    else:
        await message.answer("Вы выиграли.")



async def newss(message: types.Message):
    items = parser()
    for item in items:
        await message.answer(
            f"{item['name']}\n\n"
            f"{item['link']}\n"
            f"{item['img']}\n"
        )


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(s1, commands=['quiz'])
    dp.register_message_handler(eo, commands=['!pin'])
    dp.register_message_handler(ecco, commands=['Mem'])
    dp.register_message_handler(eco, commands=['game'])
    dp.register_message_handler(dic, commands=['dice'])
    dp.register_message_handler(newss, commands=['news'])
