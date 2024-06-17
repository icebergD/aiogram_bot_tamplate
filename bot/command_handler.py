from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.temp_data import UserState
from utils.config import config
from message_generator.starter import Starter

bot = Bot(config.TOKEN, parse_mode=config.PARSE_MODE, disable_web_page_preview=config.DISABLE_WEB_PAGE_PREVIWE)


async def startCommand(message: types.Message):
    # UserState.updateUserState(message.chat.id, '')
    await message.answer('Hello, lets start!')
    await Starter.mainMenuMessage(message)