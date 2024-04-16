from aiogram import Dispatcher

from callbacks.example import start_callback_router
from handlers.button import button_router
from handlers.start import start_router


def set_bot_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(
        start_router,
        start_callback_router,
        button_router,
    )
