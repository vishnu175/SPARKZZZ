from userbot.utils admin_cmd
from userbot import events

@sparkzzz.on(admin_cmd("bot"))
async def handler(event):
await event.reply("you are using SPARKZZZBOT")
