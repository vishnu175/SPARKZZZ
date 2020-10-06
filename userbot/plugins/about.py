# Ported from other Telegram UserBots for SPARKZZZ//Made for SPARKZZZ
# Kangers, don't remove this line 
# @its_vishnu175

"""Available Commands:
.about
"""

import asyncio

from userbot.utils import admin_cmd
sparkzzz = bot 

@sparkzzz.on(admin_cmd(pattern="about"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "Visit this page to know more about SPARKZZZ.":
    await event.edit("WELCOME TO")
    animation_chars = [
            "**⚡SPARKZZZ USERBOT⚡**",
            "[More Info](https://github.com/vishnu175/SPARKZZZ)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
