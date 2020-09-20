
# credits @TeleBot
# SPARKZZZ

import sys
from telethon import events, functions, version, __version__
import random
from userbot.utils import register
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ User"

ONLINESTR = [
	"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**SPARKZZZ is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [VISHNU CS](tg://user?id=719195224) \n\n**More help -** @sparkzzzbothelp \n\n           [🚧 GitHub Repository 🚧](https://github.com/vishnu175/SPARKZZZ)",
	f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to SPARKZZZ**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @sparkzzzbothelp \n\n✔️ Created by: [csv1990](tg://user?id=731591473) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [⚙️ REPO ⚙️](https://github.com/vishnu175/SPARKZZZ)"
]

@telebot.on(admin_cmd(outgoing=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(random.choice(ONLINESTR))
