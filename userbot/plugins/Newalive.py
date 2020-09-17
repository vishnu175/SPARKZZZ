import asyncio
import os
from telethon import events
from PIL import Image
from userbot import ALIVE_NAME, telever
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from userbot.uniborgConfig import Config
from telethon.tl.types import ChannelParticipantsAdmins
ALV_PIC = os.environ.get("ALIVE_PIC" , None)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"
ALV_PIC = "https://telegra.ph/file/e4d5011aa1fd76b742649.png"
tele = f"**⚡SPARKZZZ INSIDE⚡**\n\n
tele += "`🌐 SYSTEM IS ONLINE 🌐`\n\n"
tele += "` 👉 Telethon version:` **1.16.4**\n` 💻 Python:` **3.8.3**\n"
tele += f"` 👉 SPARKZZZ Version:` **{telever}**\n"
tele += "` 👉 Info:` **@sparkzzzbotsupport**\n"
tele += f"` 👉 Sudo :` **{sudo}**\n"
tele += f"` 👉 Uptime:` **{uptime}**\n"
tele += "` 👉 Database Status:` **FUNCTIONAL 🔌!**\n"
tele += f"` 👉 My Master` : **[{DEFAULTUSER}](tg://user?id={myid})**\n\n"
tele += "    [⚙️  FORK REPO ⚙️](https://github.com/vishnu175/SPARKZZZ)"
@telebot.on(admin_cmd(outgoing=True, pattern="alive"))
@telebot.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
chat = await alive.get_chat()
""" For .alive command, check if the bot is running.  """
await borg.send_file(alive.chat_id, ALV_PIC,caption=tele, link_preview = False)
await alive.delete()
