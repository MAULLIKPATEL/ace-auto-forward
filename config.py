#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5302267659:AAEM6afCuKDOalK9qryWrSoDYr7BiOxdAm0")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "15823382"))
    API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    AUTH_USERS = os.environ.get("OWNER", "1291288382,1296213694,5104293442,5201973365")

