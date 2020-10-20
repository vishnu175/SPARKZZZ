# (C) SPARKZZZ 2020
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
import asyncio

@sparkzzz.on(admin_cmd(pattern=("true ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit("```Reply to any 10 digit number.```")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit("```reply to a 10 digits mobile number```")
      return
   chat = "@knowhobot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit("```Reply to actual users message.```")
      return
   await event.edit("```Processing```")
   async with borg.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1115604796))
            await borg.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("```Please unblock @knowhobot and try again```")
            return
         if response.text.startswith("Forward"):
            await event.edit("The user have enabled privacy settings you cant get name history")
         else: 
            await event.edit(f"{response.message.message}")
