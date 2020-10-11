# (C) SPARKZZZ 2020
# @vishnu175
"""Cmd: `.repo`"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@sparkzzz.on(admin_cmd("repo"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Link To The SPARKZZZ Repo:** https://github.com/vishnu175/SPARKZZZ"
    chat = await event.get_input_chat()
    async for x in sparkzzz.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
