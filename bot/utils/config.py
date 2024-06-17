import os
from .singleton import Singleton

class config(Singleton):
    MAIN_TOKEN = ''
    TEST_TOKEN = ''
    TOKEN = TEST_TOKEN

    DISABLE_WEB_PAGE_PREVIWE = True

    PARSE_MODE = "Html"
    # PARSE_MODE = "MarkdownV2"


 