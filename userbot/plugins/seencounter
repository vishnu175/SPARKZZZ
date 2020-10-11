# ported for SPARKZZZ @csv1990
"""Enable Seen Counter in any message,
to know how many users have seen your message
Syntax: .seen as reply to any message"""
from userbot.utils import admin_cmd
from userbot.uniborgConfig import Config


@sparkzzz.on(admin_cmd(pattern="seen"))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_GROUP_BOT_API_ID is None:
        await event.edit("Please set the required environment variable `PRIVATE_GROUP_BOT_API_ID` for this plugin to work")
        return
    try:
        e = await sparkzzz.get_entity(Config.PRIVATE_GROUP_BOT_API_ID)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await sparkzzz.forward_messages(
            e,
            re_message,
            silent=True
        )
        await sparkzzz.forward_messages(
            event.chat_id,
            fwd_message
        )
        await fwd_message.delete()
        await event.delete()
