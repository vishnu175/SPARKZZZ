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

@command(outgoing=True, pattern="^.start$")
async def amireallyalive(start):
    """ For .start command, check if the bot is running.  """
    await start.edit("▁ ▂ ▄ ▅ ▆ ▇ █ ⚡ˢ𝓹ᗩＲЌ𝔷𝕫ᶻ⚡ █ ▇ ▆ ▅ ▄ ▂ ▁\n\n"
                     "👍🏻  `-̷-̷ Currently Alive! 🍻 -̷-̷` \n\n"
                     "__Telethon version: 1.16.4 // Python: 3.8.6\n\n__"
                     "**◆ ---------------- ✪ ----------------◆**\n"
                     "𝓑𝓸𝓽 𝓜𝓪𝓭𝓮 𝓑𝔂: [V⃫  I⃫  S⃫  H⃫  N⃫  U⃫   C⃫  S⃫  ✪](t.me/CSV1990)\n"
                     f"🎀  𝑀𝓎 𝓂𝒶𝓈𝓉𝑒𝓇  🎀 :{DEFAULTUSER}\n"
                     "**◆ ---------------- ✪ ----------------◆**\n\n"
                     "                  ★彡 [GitHub](https://github.com/vishnu175/SPARKZZZ) 彡★"
                     "                                                ")
CMD_HELP.update({
    "alive": "\
**Requested Module --> start**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.start```\
\nUsage: Checks If Userbot Is Alive.\
"
})
