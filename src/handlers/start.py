from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from constants.bot_commands import start_command
from states.example import ExampleState

start_router = Router(name=__name__)


@start_router.message(Command(start_command))
async def start(message: Message, state: FSMContext):
    # Set user state
    await state.set_state(ExampleState.example)
    # Answer to user message
    await message.answer("Hello!")
