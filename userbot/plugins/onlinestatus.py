"""
Commands - .offline .online
Offline = Add an offline tag in your name and change profile pic to black.
Online = Remove Offline Tag from your name and change profile pic to vars PROFILE_IMAGE.
"""


import os
import urllib
from telethon.tl import functions
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ User"

OFFLINE_TAG = "『OFFLINE』"
ONLINE_TAG =  "『ONLINE』"
PROFILE_IMAGE = os.environ.get(
    "PROFILE_IMAGE", "https://telegra.ph/file/d51cc6f49768f962df667.png"
)


@sparkzzz.on(admin_cmd(pattern="offline"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Already in Offline Mode.**")
        return
    await event.edit("**Changing Profile to Offline...**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(
        "https://telegra.ph/file/710085b85d99599d33b0d.png", "donottouch.jpg"
    )
    photo = "status.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await sparkzzz(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit("**Changed status to Offline.**")
    try:
        os.system("rm -fr status.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    last_name = DEFAULTUSER
    first_name = OFFLINE_TAG
    try:
        await sparkzzz(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Offline now.**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@sparkzzz.on(admin_cmd(pattern="on"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Changing status to Online...**")
    else:
        await event.edit("**Already Online.**")
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(PROFILE_IMAGE, "donottouch.jpg")
    photo = "status.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await sparkzzz(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit("**Changed status to Online.**")
    try:
        os.system("rm -fr status.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    first_name = ONLINE_TAG
    last_name = DEFAULTUSER
    try:
        await sparkzzz(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Online !**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
