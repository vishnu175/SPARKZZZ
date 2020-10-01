# credits to Telebot
# ported for SPARKZZZ
#
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from userbot import telever, ALIVE_NAME
from heroku_config import Var

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
 is = "Disabled" 
else:
 is = "Enabled"
 
TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "@sparkzzzbothelp"

tele =f"SPARKZZZ Version: {telever}\n"
tele +=f"Log Group: {log}\n"
tele +=f"Assistant Bot: {bots}\n"
tele +=f"Lydia: {lyd}\n"
tele +=f"Sudo: {sudo}\n"
tele +=f"InboxSecurity: {is}\n"
tele +=f"\nVisit @sparkzzzbothelp for assistance.\n"
telestats = (f"{tele}")

"""
Usage - .stats - To see the variable stats of SPARKZZZ {inline}
"""
