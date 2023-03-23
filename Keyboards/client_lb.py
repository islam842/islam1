from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("IOS"),
    KeyboardButton("UX/UI"),
    KeyboardButton("BACKEND"),
    KeyboardButton("PM"),
    KeyboardButton("FRONTEND"),
    KeyboardButton("ANDROID"),
    KeyboardButton("ОТМЕНА")
)

group_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True

).add(
    KeyboardButton("27-3B"),
    KeyboardButton("27-2B"),
    KeyboardButton("27-1B"),
    KeyboardButton("26-2B"),
    KeyboardButton("25-3B"),
    KeyboardButton("24-2B"),
    KeyboardButton("28-1B"),
    KeyboardButton("27-4B"),
    KeyboardButton("ОТМЕНА")
)



submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True



).add(
    KeyboardButton("ЗАНОВО"),
    KeyboardButton("ЗАВЕРШИТЬ"),
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("ОТМЕНА"),
)
