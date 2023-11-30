import asyncio

from aiogram import Bot

from configs.loader import dp, bot
from utils.bot.commands import set_bot_commands
from utils.bot.routers import set_bot_routers


async def on_startup(bot: Bot):
    await set_bot_commands(bot)

    bot_data = await bot.me()
    print(f"{bot_data.first_name} is ready!")


async def main():
    set_bot_routers(dp)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
