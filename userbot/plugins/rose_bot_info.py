from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

SPZUSER = str(ALIVE_NAME)

bot = "@MissRose_bot"


@sparkzzz.on(admin_cmd("roseinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with sparkzzz.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info")
                audio = await conv.get_response()
                await sparkzzz.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_bot `and retry!")
    elif "@" in sysarg:
        async with sparkzzz.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                await sparkzzz.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
    elif "" in sysarg:
        async with sparkzzz.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                await sparkzzz.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
