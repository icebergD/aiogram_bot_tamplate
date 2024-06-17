from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from callback_handler import callbackHandler
from message_handler import messageHandler
from utils.config import config
from command_handler import startCommand
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot(config.TOKEN, parse_mode=config.PARSE_MODE, disable_web_page_preview=config.DISABLE_WEB_PAGE_PREVIWE)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
   await startCommand(message)



@dp.message_handler()
async def message(message: types.Message):
    await messageHandler(message)



@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    await callbackHandler(call) 
    


if __name__ == '__main__':
    executor.start_polling(dp)
