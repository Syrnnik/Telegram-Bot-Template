from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from constants.bot_commands import start_command
from keyboards.inline.example import example_inline_keyboard
from keyboards.reply.example import example_reply_keyboard
from states.example import ExampleState

start_router = Router(name=__name__)


@start_router.message(Command(start_command))
async def start(message: Message, state: FSMContext):
    # Set user state
    await state.set_state(ExampleState.example)
    # Answer to user message
    # With inline keyboard
    await message.answer("Hello!", reply_markup=example_inline_keyboard)
    # With reply keyboard
    await message.answer("I am bot..", reply_markup=example_reply_keyboard)
