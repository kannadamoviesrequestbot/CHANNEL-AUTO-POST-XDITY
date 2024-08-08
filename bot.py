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
SESSION = config("SESSION", "BQCWDQceGf_ClO8QhEp7nkIbkqI3vQNu8GXk67VOL9FE1BmtqwGQh-Xiju6bTrT8xm_n2nBheoDGmaIhVxY-vw2niFRr9tkSK6FSgHiw36zO679wjzAjASgyr4i72iCpvusHUVmAicpWbUnBorg1cxHW-K3CKzPXHMxAEZhhogE0R80CCOE_Q_oJnn77iYEMEV0UrEaNOj7dH27iBbPelYoKZHn2p9W6iual2d3kMt3NEeVq8qFnV7bj99QGRqYmmY6r5NzS4CMwZJ7-_sECSeRTSJVP_IoL85YbDjvDMICJnvXnkheeoFjj306KjoW9swcYomTCofqzqhr61YlzdpNEAAAAAXzndm8A")
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
