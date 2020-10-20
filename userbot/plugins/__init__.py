import html
import time
from datetime import datetime

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from heroku_config import Var
from userbot import ALIVE_NAME, sparkzzzver
from userbot.__init__ import StartTime
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd, sudo_cmd

# stats
if Config.PRIVATE_GROUP_BOT_API_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.INBOXSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "@TeleBotSupport"

tele = f"TeleBot Version: {sparkzzzver}\n"
tele += f"Log Group: {log}\n"
tele += f"Assistant Bot: {bots}\n"
tele += f"Lydia: {lyd}\n"
tele += f"Sudo: {sudo}\n"
tele += f"PMSecurity: {pm}\n"
tele += f"\nVisit @TeleBotSupport for assistance.\n"
telestats = f"{tele}"
