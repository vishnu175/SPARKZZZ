
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_IMG = Config.ALIVE_PIC
if ALIVE_IMG is None:
  ALIVE_IMG = "http://i.pinimg.com/originals/42/a5/2c/42a52caffb1b65daa92ee798706b5a93.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
  ALIVE_MESSAGE = "**🔱༒★彡☣️ 🇦​🇵​ 🇽​🇩​ ☣️彡★༒ USERBOT IS Awake 🔱\n\n\n**"
  ALIVE_MESSAGE += "`My Bot Status\n\n\n`"
  ALIVE_MESSAGE += f"`Telethon: 6.9.0\n\n`"
  ALIVE_MESSAGE += f"`Python: PYTHON-3.6.4 \n\n`"
  ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!\n\n`"
  ALIVE_MESSAGE += f"`Bot Created And Maintained By`: {DEFAULTUSER}\n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_IMG,caption=ALIVE_MESSAGE)
