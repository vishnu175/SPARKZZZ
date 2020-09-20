# ported for SPARKZZZ
"""Emoji
Available Commands:
.np
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="np"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "np":
    await event.edit("np")
    animation_chars = [
            "No",
            "Problem",
            "bro 😇",
            "No Problem bro 😇",
            "No Problem bro 😇. Take your",
            "No Problem bro 😇. Take your own",
            "No Problem bro 😇. Take your own Time"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
