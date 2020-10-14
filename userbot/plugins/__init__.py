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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TEST SWITCHES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


if botname: 
 bots = "Enabled"
else:
 bots = "Disabled"


if pvtgrpid:
 log = "Enabled"
else:
 log = "Disabled"


if sudousers:
 sudo = "Disabled"
else:
 sudo = "Enabled"


if lydiaactive:
 lyd = "Enabled"
else:
 lyd = "Disabled"


if inboxsecurity.lower() == "off":
 pm = "Disabled" 
else:
 pm = "Enabled"
 
	
#credits to TELEBOT	
SPARKZZZUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"
#>>>>>>>>>>>SPARKZZZ-BOT INLINESTATS>>>>>>>>>>>>>>>>>>>>>>>>>
tele =f"SPARKZZZ Version: {sparkzzzver}\n"
tele +=f"Log Group: {log}\n"
tele +=f"INLINE Bot: {bots}\n"
tele +=f"Lydia: {lyd}\n"
tele +=f"Sudo: {sudo}\n"
tele +=f"INBOXSecurity: {pm}\n"
tele +=f"\nVisit[SPARKZZZ](t.me/sparkzzzbothelp) for assistance.\n"
telestats = (f"{tele}")



# 1)  /start
startinfo =(f"Hi{ALIVE_NAME}, **WELCOME TO SPARKZZZ-BOT** Nice To Meet You.\n Type /help to know what are the things you can do with SPARKZZZ-BOT \n\n[SPARKZZZ-BOT](t.me/sparkzzzbothelp)")

# 2) /help
helpinfo = (" Facilities provided by SPARKZZZ-BOT are here")

# 3) Deploy Button
deployinfo =("You Can easily Deploy SPARKZZZ-BOT In Heroku ,\n\n[SPARKZZZ-BOT](t.me/sparkzzzbothelp)"

# 4) Translate /tr (type /tr as reply to translate languages)

# 5) /info 
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    replied_user_profile_photos = await borg(GetUserPhotosRequest(
        user_id=replied_user.user.id,
        offset=42,
        max_id=0,
        limit=80
    ))
    replied_user_profile_photos_count = "NaN"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError as e:
        pass
    user_id = replied_user.user.id
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their names
        first_name = first_name.replace("\u2060", "")
    # inspired by https://telegram.dog/afsaI181
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "Need a Profile Picture to check **this**"
        location = str(e)
    forinfo = """Extracted Userdata From SPARKZZZ DATABASE
ID: <code>{}</code>
Target's Name: <a href='tg://user?id={}'>{}</a>
Bio: {}
DC ID: {}
Number of PPs: {}
Restricted? : {}
Verified : {}
Bot : {}
No. of Common Groups : {}
""".format(
        user_id,
        user_id,
        first_name,
        user_bio,
        dc_id,
        replied_user_profile_photos_count,
        replied_user.user.restricted,
        replied_user.user.verified,
        replied_user.user.bot,
        common_chats
    )
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = event.message.id
        
async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e

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
uptime = get_readable_time((time.time() - StartTime))
end = datetime.now()
ms = (end - start).microseconds / 1000
uptime = get_readable_time((time.time() - StartTime))
pingspeed = f"🏓Ping speed: {ms}"\n🤖SPARKZZZ Uptime: {uptime}")


def check(tele):
    if "/start" in tele:
        return True
    wew = re.search(re.escape(f"\\b{tele}\\b"), "a|b|c|d")
    if wew:
        return True
    return False

# inspired by https://github.com/sandy1709/catuserbot/blob/master/userbot/plugins/__init__.py
# @sn12384

async def telealive():
    start = datetime.now()
    if Config.SUDO_USERS:
        sudo = "Active"
    else:
        sudo = "Disabled"
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    try:
        useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/80.0.3987.149 Mobile Safari/537.36'
                     )
        user_id = Heroku.account().id
        headers = {
            'User-Agent': useragent,
            'Authorization': f'Bearer {Var.HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
        }
        path = "/accounts/" + user_id + "/actions/get-quota"
        r = requests.get(heroku_api + path, headers=headers)
        result = r.json()
        quota = result['account_quota']
        quota_used = result['quota_used']

        # Used
        remaining_quota = quota - quota_used
        math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
		
        # Current
        App = result['apps']
        try:
            App[0]['quota_used']
        except IndexError:
            AppQuotaUsed = 0
        else:
            AppQuotaUsed = App[0]['quota_used'] / 60
            math.floor(App[0]['quota_used'] * 100 / quota)
			
        hrs = math.floor(AppQuotaUsed / 60)
        mins = math.floor(AppQuotaUsed % 60)
        dyno = f"{hrs}h {mins}m/{hours}h {minutes}m"
    except Exception as e:
        dyno = e
    info = f"SPARKZZZ Stats\
                  \n\nVersion : {sparkzzzver}\
                  \nSudo : {sudo}\
		  \nPing : {ms}\
                  \nDyno : {dyno}\
                  "
    return info	     
	     
