from aiogram import Bot
from loguru import logger

from configs.loader import scheduler

EXAMPLE_INTERVAL_IN_SECONDS = 10


async def example_task(bot: Bot):
    bot_data = await bot.me()
    logger.info(f"{bot_data.first_name} is still here..")


async def start_example_task(bot: Bot):
    scheduler.add_job(
        example_task,
        trigger="interval",
        seconds=EXAMPLE_INTERVAL_IN_SECONDS,
        kwargs={
            "bot": bot,
        }
    )
    scheduler.start()
