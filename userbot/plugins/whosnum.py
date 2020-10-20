# (C) SPARKZZZ 2020
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
import asyncio

@sparkzzz.on(admin_cmd(pattern=("num ?(.*)")))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any 10 digit mobile number.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to a mobile number```")
       return
    chat = "@knowhobot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to a valid mobile number.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1115604796))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```you blocked @knowhobot```")
              return
          if response.text.startswith("Hello,"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.edit(f"{response.message.message}")
