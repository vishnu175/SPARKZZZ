# Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("whoami"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,36)
    await event.edit("Hello ")
    animation_chars = [
            "I",
            "am",
            "Abir Hasan",
            "I am [Abir Hasan](http://t.me/AbirHasan2005). \n**Skills:** \n**[1] Bash/Shell** \n**[2] Python** \n**[3] HTML** \n**[4] PHP** \n**[5] Git** \n \n`I use Ubuntu, Kali, Android and Windows OS.`\n\n**Telegram Group: **[Linux Repositories](http://t.me/linux_repo) \n **Learn Coding, Programming & Hacking. Feedback for my GitHub Repositories. Report Bugs and More there. Also get Updates in group.**\n\n**Follow on: **\n[GitHub Profile](https://github.com/AbirHasan2005) \n[Twitter Profile](https://twitter.com/AbirHasan2005) \n[Facebook Profile](https://facebook.com/AbirHasan2005) \n[Instagram Profile](https://instagram.com/AbirHasan2005)\n"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])