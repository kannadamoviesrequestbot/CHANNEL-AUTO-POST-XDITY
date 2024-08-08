#    This file is part of the ChannelAutoForwarder distribution (https://github.com/xditya/ChannelAutoForwarder).
#    Copyright (c) 2021 Adiya
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/xditya/ChannelAutoForwarder/blob/main/License> .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", "7041911")
API_HASH = config("API_HASH", "abab2561c71e3004a55d4ff9763d5383")
SESSION = config("SESSION", "BQBrc3cAg7gPj48U-aw2U0wSD9ShBbvRFL6G-tEeE9izIGaY0xmzF2xkiW2jR7fmtSEBPSbCdgfqzqNX0H0tEw2NzjCC7mgjOCvbZ5O8TBq-z4WAcUD1GGdADCoPnFq45j522X8KUt3Gk_snKWA8xcgms0hAGhDGmkVSKyR6d7hLUB4VKJ562uy-_gtwj6JlqUGypVxstcdLPrNtF5QQs8dS0aQVg6iJXRTlJ0hqpnOcG4zs7PgkdVEl-udB42SCF7FXwKVL1zByrOucyQrSo75eCN1zGpr-C7rZX-LuflemWv6Dl-zVHBib-laZO3MMig-0r6zLINWzdTThvLLno9Aeto5BAAAAAAA7T8-AAA")
FROM_ = config("FROM_CHANNEL", "-1001193622774 -1002009629707")
TO_ = config("TO_CHANNEL", "-1002172471256")
BOT_TOKEN = config("BOT_TOKEN", "7010173297:AAEwtQSHl1CbcOwWG57PFakKrqQ1t_tGjZI")
FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
