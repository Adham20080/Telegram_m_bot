from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Uzbek', callback_data='uzbek'),
     InlineKeyboardButton(text='Turk', callback_data='turk'),
     InlineKeyboardButton(text='Arabic', callback_data='arab'),
     InlineKeyboardButton(text='Xorazm', callback_data='xor'),
     InlineKeyboardButton(text='Russian', callback_data='rus')]
])
