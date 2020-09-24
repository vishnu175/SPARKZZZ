from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("sparkzzz"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Hello ")
    animation_chars = [
    "SPARKZZZ",
    "**⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜\n⬜️⬜️⬜️⬜️⬜️🟨🟨⬜⬜⬜🟨\n⬜️⬜️⬜️⬜🟨⬜🟨⬜⬜🟨⬜\n⬜⬜⬜🟨⬜⬜🟨⬜🟨⬜⬜\n⬜⬜🟨⬜⬜⬜🟨🟨⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n\n welcome to SPARKZZZ\n\n⚡⚡⚡⚡!!!!!**"
    ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
