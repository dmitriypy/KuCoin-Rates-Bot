from aiogram import Dispatcher

from handlers.text.start import bot_start
from handlers.text.price import price
from handlers.text.rates import rates


def register_user_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])

    dp.register_message_handler(price, commands=['price'])
    dp.register_message_handler(rates, commands=['rates'])