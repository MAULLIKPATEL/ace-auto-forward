#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("5302267659:AAEM6afCuKDOalK9qryWrSoDYr7BiOxdAm0")
    # The Telegram API things
    API_ID = int(os.environ.get("15823382"))
    API_HASH = os.environ.get("016d5e115a06ddfb6121823d72ae4d8c")
    AUTH_USERS = os.environ.get("5104293442")

