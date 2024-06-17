from aiogram import Bot, types
from message_generator.starter import Starter
from utils.config import config
from utils.temp_data import UserState


bot = Bot(config.TOKEN, parse_mode=config.PARSE_MODE, disable_web_page_preview=config.DISABLE_WEB_PAGE_PREVIWE)


async def callbackHandler(call: types.CallbackQuery):
    
    data = call.data

    match data:
        case data if data.startswith('callback_'): await Starter.callbackMessage(call)

        