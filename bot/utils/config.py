import os
from .singleton import Singleton

class config(Singleton):
    MAIN_TOKEN = ''
    TEST_TOKEN = '7309028858:AAG4cAYbMMtnXcOaRZuv45nY3eICWBkXs1s'
    TOKEN = TEST_TOKEN

    DISABLE_WEB_PAGE_PREVIWE = True

    PARSE_MODE = "Html"
    # PARSE_MODE = "MarkdownV2"


 