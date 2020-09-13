# Ported from other Telegram UserBots for SPARKZZZ//Made for SPARKZZZ
# Kangers, don't remove this line 
# @its_vishnu175

"""Available Commands:
.info
"""

import asyncio

from userbot.utils import admin_cmd
sparkzzz = bot 

@ sparkzzz.on(admin_cmd(pattern="info"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "Visit this page to know more about SPARKZZZ.":
    await event.edit("Thanks")
    animation_chars = [
            "**⚡SPARKZZZ ⚡**",
            "[More Info](https://telegra.ph/file/d8084e46678ed299cdd4f.jpg)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
