
"""
Echoes the message via your bot
"""

from userbot.utils import admin_cmd, sudo_cmd

@telebot.on(admin_cmd(pattern=r"echo (.*)"))
@telebot.on(sudo_cmd(pattern=r"echo ( .*)", allow_sudo=True))
async def _(event):
    bxt = Var.TG_BOT_USER_NAME_BF_HER
    try:
     tex = str(event.text[6:])
     await tgbot.send_message(event.chat_id, tex)
     await event.delete()
    except:
     await event.client.send_message(event.chat_id, f"Please add @{bxt} here first!")
     await event.delete()
