# (C) SPARKZZZ 2020
from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os

@sparkzzz.on(admin_cmd(outgoing=True, pattern="num(?: |$)(.*)"))
async def num(num):
    if num.fwd_from:
        return
    d_link = num.pattern_match.group(1)
    if ".com" not in d_link:
        await num.edit("`SEND ME A 10 DIGIT MOBILE NUMBER.`**(._.)**")
    else:
        await num.edit("**SEARCHING...!**")
    chat = "@knowhobot"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              response = await conv.get_response()
              r = await conv.get_response()
              msg = await conv.send_message(d_link)
              details = await conv.get_response()
              number = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await num.edit("**Error:** `unblock` @knowhobot `and retry!`")
              return
          await bot.send_file(num.chat_id, number, caption=details.text)
          await num.client.delete_messages(conv.chat_id,
                                             [msg_start.id, response.id, r.id, msg.id, details.id, number.id])
          await num.delete()          
