# Telegram Bot Template

This GitHub template repository provides a starting point for creating Telegram bots using the aiogram 3.
It aims to streamline the development process by providing a basic project structure and essential files.

## Features

✅ Preconfigured development environment with aiogram 3

✅ Basic project structure for easy organization of code

✅ Example bot implementation showcasing usage of aiogram features

✅ Configuration file for storing token and other bot settings

✅ Predefined handlers for common Telegram bot commands

✅ Predefined inline and reply Telegram bot keyboards with own handlers & callbacks

✅ Dockerfile & docker-compose for simple running bot with Docker

✅ Logging setup for monitoring and debugging

✅ Scheduled tasks setup for periodic background operations

## How to Use

Click on the "Use this template" button to create a new repository based on this template.
Clone the newly created repository to your local machine.

### Run Locally

1. Install the necessary dependencies by running `pip3 install -r requirements.txt`
2. Create the `.env` file in the root of project and set `BOT_TOKEN` of your Telegram bot
3. Run the bot using `python3 src/main.py` and start interacting with it on Telegram

### Run with Docker Compose

1. Build docker image by running `docker compose build`
2. Run the bot container using `docker compose up` and start interacting with it on Telegram

The template repository sets up a foundation for building your Telegram bot using aiogram 3, taking care of the
initial project structure and providing an example implementation. You can further enhance and customize your bot by
extending the provided codebase according to your requirements.

_Note: Make sure to review the aiogram [documentation](https://docs.aiogram.dev/en/dev-3.x/) for in-depth explanations
of the library's features and explore its capabilities to create powerful and interactive Telegram bots._

Please feel free to modify and adapt this template to suit your specific bot development needs.

If you have any idea to improve my repo, just let me know in **Issues**

[I have idea!!](https://github.com/Syrnnik/Telegram-Bot-Template/issues/new)

**Happy ~~hacking~~ coding!! 💻🐞**
