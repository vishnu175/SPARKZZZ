# (C) SPARKZZZ 2020

"""
cmds:.info
"""
import asyncio
from userbot.utils import admin_cmd 

@sparkzzz.on(admin_cmd(pattern="info"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "Visit this page to know more about SPARKZZZ.":
    await event.edit("WELCOME TO")
    animation_chars = [
            "**⚡SPARKZZZ⚡**",
            "[More Info](https://github.com/vishnu175/SPARKZZZ)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])




# (C) SPARKZZZ 2020
