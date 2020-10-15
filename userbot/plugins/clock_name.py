#(C) SPARKZZZ 2020
import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP

DEL_TIME_OUT = 60

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ"

@sparkzzz.on(admin_cmd(pattern="cname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%y")
        HM = time.strftime("%H:%M")
        name = f"{HM}⚡{DEFAULTUSER}⚡{DMY}"
        logger.info(name)
        try:
            await sparkzzz(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name = name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await sparkzzz.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Changed Profile Picture"
            # )
        await asyncio.sleep(DEL_TIME_OUT)
