# Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/fb4807a43ec085f0996c3.jpg"
pm_caption = "`Repositories of` **@AbirHasan2005**\n"
pm_caption += "**GitHub:** `https://github.com/AbirHasan2005`\n\n"
pm_caption += "**ShellPhish:** `https://github.com/AbirHasan2005/ShellPhish`\n"
pm_caption += "**UserRecon** `https://github.com/AbirHasan2005/UserRecon`\n"
pm_caption += "**CoronaStats:** `https://github.com/AbirHasan2005/CoronaStats`\n"
pm_caption += "**Deskify:** `https://github.com/AbirHasan2005/Deskify`\n"
pm_caption += "**OPRecon:** `https://github.com/AbirHasan2005/OPRecon`\n"
pm_caption += "**fsociety:** `https://github.com/AbirHasan2005/fsociety`\n"
pm_caption += "**RepoHub:** `https://github.com/AbirHasan2005/RepoHub`\n"
pm_caption += "**TelegramScraper:** `https://github.com/AbirHasan2005/TelegramScraper`\n"
pm_caption += "**LittleBrother:** `https://github.com/AbirHasan2005/LittleBrother`\n"
pm_caption += "**Visify:** `https://github.com/AbirHasan2005/Visify`\n"
pm_caption += "**PowerLevel10K:** `https://github.com/AbirHasan2005/PowerLevel10K`\n"
pm_caption += "**PySnakeGame:** `https://github.com/AbirHasan2005/PySnakeGame`\n"
pm_caption += "**YouTube_Views_Bot:** `https://github.com/AbirHasan2005/YouTube_Views_Bot`\n"
@borg.on(admin_cmd(pattern=r"repos"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
