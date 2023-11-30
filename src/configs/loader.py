from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from configs.env import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
