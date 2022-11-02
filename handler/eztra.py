from aiogram import types , Dispatcher
from coin import bot, dp

# @dp.message_handler()
async def echo(message: types.Message):
    jj = message.text
    rr = message.text.isnumeric()
    if rr == True:
        daff = int(jj) **2
        await bot.send_message(message.from_user.id, daff)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_handler_ezta(dp: Dispatcher):
    dp.register_message_handler(echo, content_types='qretwuci456vhthc4er')

