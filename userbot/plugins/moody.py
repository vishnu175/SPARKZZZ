"""Emoji
Available Commands:
.moody"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("moody"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)
    
    #await event.edit(input_str)
    await event.edit("I am getting moody now")
    animation_chars = [
           "😆😆😆",
           "😋🤨🧐",
           "😛😒😣",
           "😝😖🤩",
           "😜😑😰",
           "🤪😳🥵",
           "😭🥺😩",
           "😫😠🤬",
           "😬😐😶",
           "😵😵😵"  
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])           
