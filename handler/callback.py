from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from coin import bot, dp

# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def s2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)
    question = "В чем смысл жизни?"
    answers = [
        "нету смысла",
        "для продолжения рода",
        "развития себя ",
        "сам определяеш смысл",
        "просто жить без смысла",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="неправильно!",
        reply_markup=markup
    )

# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def s3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_3)
    question = " Кто создал первую реально работающую программируемую вычислительную машину (компьютер) ?"
    answers = [
        "Чарлз Бэббидж в 1919",
        "Конрад Цузе в 1941 году",
        "Уильям Моггридж в 1928 ",
        "Говарда Эйкен в 1925 ",
        "Альберт Эйнштейн в 1921",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="неправильно!",
        reply_markup=markup
    )

def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(s2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(s3, lambda call: call.data == "button_call_2")


