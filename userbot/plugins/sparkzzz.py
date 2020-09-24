# @ copyright SPARKZZZZ

"""
.sparkzzz
"""

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot.utils import admin_cmd

import time

@sparkzzz.on(admin_cmd(pattern="gdn", outgoing=True))

async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("`WELCOME TO SPARKZZZ`"\n\n
    "**⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜\n⬜️⬜️⬜️⬜️⬜️🟨🟨⬜⬜⬜🟨\n⬜️⬜️⬜️⬜🟨⬜🟨⬜⬜🟨⬜\n⬜⬜⬜🟨⬜⬜🟨⬜🟨⬜⬜\n⬜⬜🟨⬜⬜⬜🟨🟨⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n\n welcome to SPARKZZZ\n\n⚡⚡⚡⚡!!!!!**"
    ")

        time.sleep(3)

        if '-' in str(e.chat_id):

            await sparkzzz(LeaveChannelRequest(e.chat_id))
