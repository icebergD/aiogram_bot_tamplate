from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from utils.singleton import Singleton
from utils.config import config
from utils.temp_data import UserState
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

bot = Bot(config.TOKEN, parse_mode=config.PARSE_MODE, disable_web_page_preview=config.DISABLE_WEB_PAGE_PREVIWE)


class Starter(Singleton):

    @staticmethod
    async def mainMenuMessage(message: types.Message):
        # UserState.updateUserState(message.chat.id, 'main_menu')
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keys = []
        keys.append(KeyboardButton(text="Test btn 1"))
        keys.append(KeyboardButton(text="Test btn 2"))
        keys.append(KeyboardButton(text="Test btn 3"))
        keys.append(KeyboardButton(text="Inline Buttons"))
        markup.add(*keys)
        await message.answer("Main menu", reply_markup=markup)


    @staticmethod
    async def emptyMessage(message: types.Message):
        await message.answer("Empty")


    @staticmethod
    async def callbackButtons(message: types.Message):

        keyboard = InlineKeyboardMarkup(row_width=1)

        keyboard.add(InlineKeyboardButton(f"Url btn", url="https://github.com/"))

        keyboard.add(InlineKeyboardButton(f"Callback btn", callback_data=f"callback_"))

        await message.answer("Inline buttons", reply_markup=keyboard)


    @staticmethod
    async def callbackMessage(message: types.Message):
        await message.answer("Callback works")