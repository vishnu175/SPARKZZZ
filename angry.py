"""Emoji
Available Commands:
.angry"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("angry"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 18)
    
    #await event.edit(input_str)
    await event.edit("I am getting angry now")
    animation_chars = [
           "😡😡😡",
           "I am angry with you",
           "Just shut up",
           "And RUN Away NOW",
           "Or else",
           "I would call CEO of Telegram",
           "My friend is also a hacker...",
           "I would call him if you don't shut up",
           "🤬🤬Warning you, Don't repeat it again and shut up now...🤬🤬",
           "🤬🤬🤬🤬🤬 BSDK ab toh chup ho ja."
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])
