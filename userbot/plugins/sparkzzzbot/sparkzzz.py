from telethon import events, custom, Button
from telethon import events
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
import os
import requests
import asyncio
import emoji
from datetime import datetimemport math
from userbot import bot
from userbot import ALIVE_NAME
from userbot.uniborgConfig import Config
from heroku_config import Var



DEFUSR = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ-user'

@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    await tgbot.send_message(
           event.chat_id,
           message=startinfo,
           buttons = [
           [Button.url("SPARKZZZ-REPO", "https://github.com/vishnu175/SPARKZZZ/")]
           [Button.url("SPARKZZZ", "t.me/sparkzzzbothelp")]
            ]
      )
    
    
tgbot.on(events.NewMessage(pattern="^/help"))
async def thisfn(event):
    await tgbot.send_message(
           event.chat_id,
           message=helpinfo,
           link_preview = False,
           buttons = [
           [Button.url("SPARKZZZ", "https://t.me/sparkzzzbothelp")]
            ]
      )  
    
    
    
