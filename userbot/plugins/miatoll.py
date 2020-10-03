#(c) SPARKZZZ 2020
# @vishnu175
import os
import asyncio
from telethon import custom
from telethon import events, errors, functions, types
from userbot.utils import admin_cmd

@sparkzzz.on(admin_cmd(pattern="miatoll ?(.*)"))
async def handler(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    input_args = event.pattern_match.group(1)
    # Tweak input for lower chance of failure
    args = input_args.split()[0]
    args = f"#{args}"
    chat = "@MiatollOfficial"
    async for message in client.iter_messages(chat):
        msg = message.text
        if msg is None:
            msg = ""
        if args.lower() in msg.lower():
            result = message
            break
        else:
            result = f"Nothing found for query:\n {input_args}"
    await event.delete()
    await client.send_message(
        event.chat_id,
        result,
        reply_to=reply,
        parse_mode="HTML",
        force_document=False,
        silent=True
    )

ENV.HELPER.update({"miatoll": "\
```.miatoll <rom_name>```\
\nUsage: Returns the latest build for a custom rom.\
\n```.miatoll <kernel_name>```\
\nUsage: Returns the latest build for a custom kernel.\
\n```.miatoll recovery```\
\nUsage: Returns the latest lrtwrp build.\
\n\nUsing .miatoll rom / .miatoll kernel will return latest rom or kernel.\
"})
