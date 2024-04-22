from aiogram.types import BotCommand

start_command = BotCommand(
    command="start",
    description="Start chat with bot"
)

all_commands = [
    start_command,
]
