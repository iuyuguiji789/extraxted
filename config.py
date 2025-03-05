#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7749377548:AAFpYFg0tAUvIGdlLTFUYUxX9LSKzAxrGr8")
    API_ID = int(os.environ.get("API_ID", "12380656"))
    API_HASH = os.environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
    AUTH_USERS = "6434053909"

