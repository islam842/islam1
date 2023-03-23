import random
from config import ADMINS, bot
from aiogram import Dispatcher, types
from database.bot_db import sql_command_all,sql_command_delete
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


async def emoji(message: types.Message):
    if message.from_user.id in ADMINS and message.text.startswith('game'):
        emojis = ['🏀', '⚽️', '🎯', '🎳', '🎰', '🎲']
        random_emoji = random.choice(emojis)
        await message.answer_dice(random_emoji)
    elif not message.from_user.id in ADMINS and message.text.startswith('game'):
        await message.answer("Вы не являетесь админом")


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await message.answer(
            f"{user[2]} {user[3]} {user[4]} "
            f"{user[5]}\n@{user[1]}",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(f"DELETE {user[2]}",
                                     callback_data=f"DELETE {user[0]}")
            )
        )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("DELETE ", ""))
    await call.answer(text="Удалено!", show_alert=True)
    await call.message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(emoji)
    dp.register_message_handler(delete_data,commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startwith("DELETE"))
