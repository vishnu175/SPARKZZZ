import pyshorteners
from userbot.utils import admin_cmd

@sparkzzz.on(admin_cmd(pattern="urlshort (.*)"))
async def vom(event):
    try:
        link = event.pattern_match.group(1)
        pys = pyshorteners.Shortener()
        tny = pys.tinyurl.short(link)
        shortinglink = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ <code>{link}</code> \n"
            f"<b><u>Shortened Link</u></b> ➠ <code>{tny}</code>"
        )
        await event.edit(shortinglink, parse_mode="HTML")
    except Exception as e:
        await event.edit("SomeThing Went Wrong. \nError : " + e)
