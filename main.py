from aiogram.utils import executor
from coin import dp
import logging
from handler import client, callback, eztra, fsmAdminMentor,wikipedia
from DSA.BZD import sql_create

async def on_startup(_):
    sql_create()

fsmAdminMentor.register_handler_fsmAdminMentor(dp)
client.register_handler_client(dp)
callback.register_handler_callback(dp)
wikipedia.register_handler_wikipedia(dp)
eztra.register_handler_ezta(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
