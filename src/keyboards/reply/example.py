from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

"""How it will be shown:
| Button1 |  | Button 2 |
|       Button 3        |
"""
_example_reply_keyboard_buttons = [
    [
        KeyboardButton(text="Button 4"),
        KeyboardButton(text="Button 5"),
    ],
    [
        KeyboardButton(text="Button 6"),
    ]
]

example_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=_example_reply_keyboard_buttons,
    resize_keyboard=True,
    input_field_placeholder="Select button"
)
