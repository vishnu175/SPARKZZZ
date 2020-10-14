# (C) SPARKZZZ 2020
# @vishnu175
from telethon.utils import get_input_location
from datetime import datetime
import asyncio
import time
import html
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from userbot.__init__ import StartTime
from userbot import ALIVE_NAME


# SPARKZZZ- BOT IS AN INLINE ASSISTANT BOT HAVING SOME COOL FEAUTURES

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SPARKZZZ-BOT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#=============================HELP COMMANDS===================================


# 1)  /start
startinfo =(f"Hi{ALIVE_NAME}, **WELCOME TO SPARKZZZ-BOT** Nice To Meet You.\n Type /help to know what are the things you can do with SPARKZZZ-BOT \n\n[SPARKZZZ-BOT](t.me/sparkzzzbothelp)")

# 2) /help
helpinfo = (" Facilities provided by SPARKZZZ-BOT are here")

# 3) Deploy Button
deployinfo =("You Can easily Deploy SPARKZZZ-BOT In Heroku ,\n\n[SPARKZZZ-BOT](t.me/sparkzzzbothelp)"

# 4) Translate /tr (type /tr as reply to translate languages)

# 5) /info 
info = ("type /info @username to grt information about the given user")

# 6) /ping will give the ping stats
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

start = datetime.now()
end = datetime.now()
ms = (end - start).microseconds / 1000
uptime = get_readable_time((time.time() - StartTime))
pingspeed = f"🏓Ping speed: {ms}"\n🤖SPARKZZZ Uptime: {uptime}")


# (C) SPARKZZZ 2020




