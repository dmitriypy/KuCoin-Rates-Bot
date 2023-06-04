from aiogram import Dispatcher

from handlers.text import register_user_handler


def register_handlers(dp: Dispatcher):
    register_user_handler(dp)
