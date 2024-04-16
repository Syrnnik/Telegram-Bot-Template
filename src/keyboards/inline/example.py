from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""How it will be shown:
| Button1 |  | Button 2 |
|       Button 3        |
"""
_example_inline_keyboard_buttons = [
    [
        InlineKeyboardButton(text="Button 1", callback_data="button1"),
        InlineKeyboardButton(text="Button 2", callback_data="button2"),
    ],
    [
        InlineKeyboardButton(text="Button 3", url="https://t.me/syrnnik")
    ]
]

example_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=_example_inline_keyboard_buttons)
