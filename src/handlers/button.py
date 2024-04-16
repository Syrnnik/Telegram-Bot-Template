from aiogram import Router, F
from aiogram.types import Message

button_router = Router(name=__name__)


@button_router.message(F.text.startswith("Button"))
async def button(message: Message):
    await message.answer(f"You click button: {message.text}")
