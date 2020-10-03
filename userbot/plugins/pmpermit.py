import asyncio
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, LESS_SPAMMY
from userbot.utils import admin_cmd

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
TELEPIC = PMPERMIT_PIC if PMPERMIT_PIC else "https://telegra.ph/file/d8084e46678ed299cdd4f.jpg"
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
MESAG = str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "`SPARKZZZ inbox security 🔐! Please wait for me to approve you. 😊"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ User"
USER_BOT_WARN_ZERO = "`Hey you,..I have already warned you not to spam inbox ✉️. Now you have been blocked and reported until further notice.`\n\n**GoodBye🙋!** "
USER_BOT_NO_WARN = ("**Welcome to ⚡SPARKZZZ inbox security 🔐.**\n\nNice to see you here.unfortunately  "
                    f"[{DEFAULTUSER}](tg://user?id={myid}) is not available right now.This is an automated message from SPARKZZZ-BOT inbox security.kindly wait till my master approves  you..or tag him in group\n\n"
                    f"{MESSAGE}"
                    "\n\n\n** Send** `/start` ** so that we can decide why you're here.**")


