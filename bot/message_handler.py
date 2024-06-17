from aiogram import Bot, types
from utils.temp_data import UserState

from utils.config import config
from message_generator.starter import Starter



bot = Bot(config.TOKEN, parse_mode=config.PARSE_MODE, disable_web_page_preview=config.DISABLE_WEB_PAGE_PREVIWE)

async def messageHandler(message: types.Message):
    
    data: str = message.text

    match data:

        case data if data == 'Inline Buttons':
            await Starter.callbackButtons(message)

        case _:
            await Starter.emptyMessage(message)