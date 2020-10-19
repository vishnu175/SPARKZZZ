# (C) SPARKZZZ 2020 @vishnu175
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
import time
from userbot import CMD_HELP



DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"

@command(outgoing=True, pattern="^.ready$")
async def amireallyalive(ready):
    """ For .ready command, check if the bot is running.  """
    await ready.edit("▁ ▂ ▄ ▅ ▆ ▇ █S≋P≋A≋R≋K≋Z≋Z≋Z█ ▇ ▆ ▅ ▄ ▂ ▁\n\n"
                     "🙋  `-̷-̷ Currently Alive! 🦾 -̷-̷` \n\n"
                     "💻__Telethon version: 1.17  🐍Python: 3.8.6\n\n__"
                     "**◆ ---------------------- ✪ --------------------◆**\n"
                     "𝕭𝖔𝖙 𝕺𝖜𝖓𝖊𝖗: [V⃫  I⃫  S⃫  H⃫  N⃫  U⃫   C⃫  S⃫  ✪](t.me/CSV1990)\n"
                     f"🎀  𝑀𝓎 𝓂𝒶𝓈𝓉𝑒𝓇  🎀 :{DEFAULTUSER}\n"
                     "**◆ ---------------------- ✪ -------------------------◆**\n\n"
                     "                  ★¸.•☆•.¸★ [GitHub](https://github.com/vishnu175/SPARKZZZ) ★¸.•☆•.¸★"
                     "                                                ")
CMD_HELP.update({
    "ready": "\
**Requested Module --> ready**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.ready```\
\nUsage: Checks If Userbot Is Alive.\
"
})
