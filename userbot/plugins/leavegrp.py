# (C) SPARKZZZ 2020 

"""

.leave

"""

from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd
import time

@sparkzzz.on(admin_cmd(pattern="leave", outgoing=True))

async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("`Peoples here not having helping mentality..so i m leaving 🙋.`")

        time.sleep(3)

        if '-' in str(e.chat_id):

            await borg(LeaveChannelRequest(e.chat_id))

        else:

            await e.edit('`Please use this in groups :/`')
