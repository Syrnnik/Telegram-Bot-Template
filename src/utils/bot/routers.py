from aiogram import Dispatcher

from callbacks import all_callback_routers
from handlers import all_handlers_routers


def set_bot_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(*all_handlers_routers)
    dispatcher.include_routers(*all_callback_routers)
