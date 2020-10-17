from telethon.utils import get_input_location
from datetime import datetime
import asyncio
import time
import os
import re
import time
import math
import heroku3
import requests
import html
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from userbot.__init__ import StartTime
from userbot import ALIVE_NAME
from heroku_config import Var
from userbot.utils import admin_cmd
from userbot.utils import  sudo_cmd
from userbot import sparkzzzver
from telethon import events
from userbot.uniborgConfig import Config

SPARKZZZUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Var.HEROKU_APP_NAME
HEROKU_API_KEY = Var.HEROKU_API_KEY

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SPARKZZZ-BOT STATS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

botname = Config.TG_BOT_USER_NAME_BF_HER
pvtgrpid = Config.PRIVATE_GROUP_BOT_API_ID	
sudousers = Config.SUDO_USERS
lydiaactive =  Var.LYDIA_API_KEY
inboxsecurity = Var.INBOXSECURITY
herokuappstats = Var.HEROKU_APP_NAME
youtubesearch = Config.YOUTUBE_API_KEY
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TEST SWITCHES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


if botname: 
 inlinebot = "Enabled"
else:
 inlinebot = "Disabled"


if pvtgrpid:
 logs = "Enabled"
else:
 logs = "Disabled"


if sudousers:
 sudo = "Disabled"
else:
 sudo = "Enabled"


if lydiaactive:
 lydia = "Enabled"
else:
 lydia = "Disabled"


if herokuappstats:
 herokuapp = "Active"
else:
 herokuapp = "Inactive"

if youtubesearch:
 yts = "Enabled"
else:
 yts = "Disabled"  
 
		
#>>>>>>>>>>>SPARKZZZ-BOT INLINESTATS>>>>>>>>>>>>>>>>>>>>>>>>>

inli  =f"SPARKZZZ Version: {sparkzzzver}\n"
inli  +=f"INLINE BOT: {inlinebot}\n"
inli  +=f"HEROKU STATS: {herokuapp}\n"
inli  +=f"SPARKZZZ LOGS:{logs}\n"
inli  +=f"LYDIA: {lydia}\n"
inli  +=f"SUDO: {sudo}\n"
inli  +=f"YT SEARCH: {yts}\n"
inli  +=f"\n[SPARKZZZ](t.me/sparkzzzbothelp).\n"
sparkzzzstatus = (f"{inli}")

#>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
