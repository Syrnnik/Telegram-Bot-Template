from aiogram import Bot

from constants.bot_commands import all_commands


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(all_commands)
