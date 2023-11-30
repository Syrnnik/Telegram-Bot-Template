from aiogram import Dispatcher

from handlers.start import start_router


def set_bot_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(
        start_router,
    )
