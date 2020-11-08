import datetime
from telethon import events
from telegraph import Telegraph
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
from userbot.SparkzzzConfig import Var
import asyncio
telegraph = Telegraph()
mee = telegraph.create_account(short_name="sparkzzz")


@borg.on(admin_cmd(pattern=("sang ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit("```Reply to any user message.```")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit("```reply to text message```")
      return
   chat = "@SangMataInfo_bot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit("```Reply to actual users message.```")
      return
   await event.edit("```Processing```")
   async with borg.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
            await borg.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
         if response.text.startswith("Forward"):
            await event.edit("The user have enabled privacy settings you cant get name history")
         else: 
            await event.edit(f"{response.message.message}")

@sparkzzz.on(admin_cmd(pattern="imusic ?(.*)"))
async def spz(event):
    if event.fwd_from:
        return
    bot = "@vkmusic_bot"
    inli = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(bot, inli)
    await tap[0].click(event.chat_id)
    await event.delete()

@borg.on(admin_cmd(pattern=("fakemail ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   chat = "@fakemailbot"
   command = "/generate"
   await event.edit("```Fakemail Creating, wait```")
   async with borg.conversation(chat) as conv:
      try:
         m = await event.client.send_message("@fakemailbot","/generate")     
         await asyncio.sleep(5)
         k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False) 
         mail = k[0].text
         # print(k[0].text)
      except YouBlockedUserError: 
         await event.reply("```Please unblock @fakemailbot and try again```")
         return
      await event.edit(mail)

@borg.on(admin_cmd(pattern=("mailid ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   chat = "@fakemailbot"
   command = "/id"
   await event.edit("```Fakemail list getting```")
   async with borg.conversation(chat) as conv:
        try:
            m = await event.client.send_message("@fakemailbot","/id")     
            await asyncio.sleep(5)
            k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False) 
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError: 
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@borg.on(admin_cmd(pattern=("ub ?(.*)")))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to text message```")
       return
    chat = "@uploadbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=97342984))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @uploadbot and try again```")
              return
          if response.text.startswith("Hi!,"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.edit(f"{response.message.message}")



@borg.on(admin_cmd(pattern=("gid ?(.*)")))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to text message```")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```you blocked bot```")
              return
          if response.text.startswith("Hello,"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.edit(f"{response.message.message}")




@borg.on(admin_cmd(pattern="purl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.reply("**Reply to any document.**")
       return
    reply_message = await event.get_reply_message() 
    chat = "@FiletolinkTGbot"
    sender = reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1011636686))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await a.edit("```Please unblock me (@FiletolinkTGbot) u Nigga```")
              return
          await event.delete()
          await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)


@borg.on(admin_cmd(pattern="gitdl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.reply("**Reply to a github repo url.**")
       return
    reply_message = await event.get_reply_message() 
    chat = "@gitdownloadbot"
    sender = reply_message.sender
    await event.edit("**Downloading the repository...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1282593576))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await a.edit("```Please unblock me (@gitdownloadbot) u Nigga```")
              return
          await event.delete()
          x = await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)
          await x.edit("Downloaded by [SPARKZZZ](t.me/), via @gitdownloadbot")     

 
@borg.on(admin_cmd(pattern="reader ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("**Reply to a URL.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("**Reply to a url message.**")
       return
    chat = "@chotamreaderbot"
    sender = reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=272572121))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await a.edit("```Please unblock me (@chotamreaderbot) u Nigga```")
              return
          await event.delete()
          await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)
                  
#credits telebot
@sparkzzz.on(admin_cmd(pattern="font ?(.*)"))
async def _(event):
    bot = "@fontsgenbot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await event.edit("Give me a text to stylize")
    else:
        async with borg.conversation(bot) as conv:
            try:
                x = await eor(event, "`Making the text stylish..`")
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(sysarg)
                audio = await conv.get_response()
                title = "Stylish Fonts"
                topaste = audio.text
                topaste = topaste.replace("\n", "<br>")
                response = telegraph.create_page(title, html_content=topaste)
                link = response["path"]
                await x.edit(
                    f"**Normal Text** - {sysarg}\n**Stylised text** - [here](https://telegra.ph/{link})",
                    link_preview=False,
                )
            except YouBlockedUserError:
                await x.edit("**Error:** `unblock` @fontsgenbot `and retry!")
