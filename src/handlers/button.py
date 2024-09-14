from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text.startswith("Button"))
async def button(message: Message):
    await message.answer(f"You click button: {message.text}")
