#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5915526534:AAGUtVAU89AXPnJF-zrkCTShzxzevpBCJLs")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "14517587"))
    API_HASH = os.environ.get("API_HASH", "c51ecd079bd1229b9cc6e26cbbb60d93")
    AUTH_USERS = os.environ.get("OWNER", "5989158216,5472986881,5715553928,5104293442")

