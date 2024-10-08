from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("button"))
async def button_clicked(callback: CallbackQuery):
    # Show alert with clicked button number
    await callback.answer(f"You click: {callback.data}", show_alert=True)
    # Answer to user message with clicked button number
    await callback.message.answer(f"You click: {callback.data}")
