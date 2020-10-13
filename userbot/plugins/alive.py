# credits to Telebot
# @csv1990
"""Check if your userbot is working."""
import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME, sparkzzzver
from userbot.utils import admin_cmd, sudo_cmd
from userbot.__init__ import StartTime
from datetime import datetime
from userbot.uniborgConfig import Config

ALV_PIC = os.environ.get("ALIVE_PIC" , None)

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
    
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

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"

@sparkzzz.on(admin_cmd(outgoing=True, pattern="alive"))
@sparkzzz.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = f"**⚡𝕊ℙ𝔸ℝ𝕂ℤℤℤ INSIDE⚡**\n\n"
        tele += f"======================================\n"
        tele += "`🌐 𝐒𝐘𝐒𝐓𝐄𝐌 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄 🌐`\n\n"
        tele += "` 👉 Telethon version:` **1.16.4**\n` 🐍 Python:` **3.8.6**\n"
        tele += f"` ⚡ SPARKZZZ Version:` **{sparkzzzver}**\n"
        tele += "` 👉 Info:` **[⚡𝐒𝐏𝐀𝐑𝐊𝐙𝐙𝐙-𝐁𝐎𝐓⚡]**(t.me/sparkzzzbothelp)\n"
        tele += "` 👤 Bot Creator:`**[ℂ𝕊𝕍𝟙𝟡𝟡𝟘]**(t.me/CSV1990)\n"
        tele += f"` 👉 Sudo :` **{sudo}**\n"
        tele += f"` 🕙 Uptime:` **{uptime}**\n"
        tele += "` 🖥️ Database Status:` **FUNCTIONAL 🔌!**\n"
        tele += f"` 🙋 My Master` : **[{DEFAULTUSER}](tg://user?id={myid})**\n\n"
        tele += f"=======================================\n\n"
        tele += "    [⚙️  𝐅𝐎𝐑𝐊 𝐑𝐄𝐏𝐎 ⚙️](https://github.com/vishnu175/SPARKZZZ)"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC,caption=tele, link_preview = False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/f05bb1b963445ff544027.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(alive.chat_id, f"**⚡𝕊ℙ𝔸ℝ𝕂ℤℤℤ INSIDE⚡**\n\n"
                f"======================================\n"
                "`🌐 𝐒𝐘𝐒𝐓𝐄𝐌 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄 🌐`\n\n"
                "` 👉 Telethon version:` **1.16.4**\n` 🐍 Python:` **3.8.6**\n"
                f"` ⚡ SPARKZZZ Version:` **{sparkzzzver}**\n"
                "` 👉 Info:` **[⚡𝐒𝐏𝐀𝐑𝐊𝐙𝐙𝐙-𝐁𝐎𝐓⚡]**(t.me/sparkzzzbothelp)\n"
                "` 👤 Bot Creator:`**[ℂ𝕊𝕍𝟙𝟡𝟡𝟘]**(t.me/CSV1990)\n"             
                f"` 👉 Sudo :` **{sudo}**\n"
                f"` 🕙 SPARKZZZ Uptime:` **{uptime}**\n"
                "` 🖥️ Database Status:` **FUNCTIONAL 🔌!**\n"
                f"` 🙋 My Master` : **[{DEFAULTUSER}](tg://user?id={myid})**\n\n"
                f"=======================================\n\n"       
                "    [⚙️  𝐅𝐎𝐑𝐊 𝐑𝐄𝐏𝐎 ⚙️](https://github.com/vishnu175/SPARKZZZ)", link_preview = False)
        await borg.send_file(alive.chat_id, file=sticker) 
        await alive.delete()     
        

        
        
