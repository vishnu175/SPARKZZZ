"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
# 
import asyncio
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/e4d5011aa1fd76b742649.png"
pm_caption = "`FRIDAY IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEMS STATS**\n"
pm_caption += "`Telethon Version:` **1.15.0**\n`Python:` **3.7.4**\n"
pm_caption += "`Database Status:` **Functional**\n"
pm_caption += "**Current Branch** : `Master`\n"
pm_caption += "**Version** : `3.0`\n"
pm_caption += "**Current Sat** : ``༒★彡☣️ 🇦 🇵  🇽 🇩  ☣️彡★༒2.25`\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [GNU General Public License v3.0](github.com/APXD-git/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [APXD-git@Github](GitHub.com/APXD-git)\n"
pm_caption += "**OS** : `Slim Buster`"
pm_caption += " [Deploy FridayUserbot](https://telegra.ph/file/e4d5011aa1fd76b742649.png)"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()