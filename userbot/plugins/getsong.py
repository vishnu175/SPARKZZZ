import asyncio
import glob
import os
import subprocess
import time
from asyncio.exceptions import TimeoutError

import requests
from bs4 import BeautifulSoup
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pylast import User
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeVideo

from userbot import CMD_HELP, LASTFM_USERNAME, bot, lastfm
from userbot.events import register
from userbot.utils import progress


# For song module
def getmusic(get, DEFAULT_AUDIO_QUALITY):
    search = get

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }

    html = requests.get(
        "https://www.youtube.com/results?search_query=" +
        search,
        headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        if "/watch?v=" in link.get("href"):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get("href")
            break

    video_link = "http://www.youtube.com/" + video_link
    command = (
        "youtube-dl --write-thumbnail --extract-audio --audio-format mp3 --audio-quality " +
        DEFAULT_AUDIO_QUALITY +
        " " +
        video_link)
    os.system(command)


# For getvideosong
def getmusicvideo(cat):
    search = cat
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }
    html = requests.get(
        "https://www.youtube.com/results?search_query=" +
        search,
        headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        if "/watch?v=" in link.get("href"):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get("href")
            break
    video_link = "http://www.youtube.com/" + video_link
    command = 'youtube-dl -f "[filesize<50M]" --merge-output-format mp4 ' + video_link
    os.system(command)


@register(outgoing=True, pattern=r"^\.song (.*)")
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("`Wait..! I am finding your song..`")
    elif reply.message:
        query = reply.message
        await event.edit("`Wait..! I am finding your song..`")
    else:
        await event.edit("`What I am Supposed to find?`")
        return

    getmusic(str(query), "320k")
    l = glob.glob("*.mp3")
    loa = l[0]
    img_extensions = ["webp", "jpg", "jpeg", "webp"]
    img_filenames = [
        fn_img
        for fn_img in os.listdir()
        if any(fn_img.endswith(ext_img) for ext_img in img_extensions)
    ]
    thumb_image = img_filenames[0]
    await event.edit("`Yeah.. Uploading your song..`")
    c_time = time.time()
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=True,
        thumb=thumb_image,
        allow_cache=False,
        caption=query,
        reply_to=reply_to_id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[UPLOAD]", loa)
        ),
    )
    await event.delete()
    os.system("rm -rf *.mp3")
    os.remove(thumb_image)
    subprocess.check_output("rm -rf *.mp3", shell=True)


@register(outgoing=True, pattern=r"^\.vsong(?: |$)(.*)")
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("`Wait..! I am finding your videosong..`")
    elif reply.message:
        query = reply.message
        await event.edit("`Wait..! I am finding your videosong..`")
    else:
        await event.edit("`What I am Supposed to find?`")
        return
    getmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm"))
    if l:
        await event.edit("`Yeah..! i found something..`")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await event.edit("`Uploading video.. Please wait..`")
    os.system("cp *mp4 thumb.mp4")
    os.system("ffmpeg -i thumb.mp4 -vframes 1 -an -s 480x360 -ss 5 thumb.jpg")
    thumb_image = "thumb.jpg"
    c_time = time.time()
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=False,
        thumb=thumb_image,
        allow_cache=False,
        caption=query,
        supports_streaming=True,
        reply_to=reply_to_id,
        attributes=[
            DocumentAttributeVideo(
                duration=duration,
                w=width,
                h=height,
                round_message=False,
                supports_streaming=True,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[UPLOAD]", loa)
        ),
    )
    await event.delete()
    os.remove(thumb_image)
    os.system("rm -rf *.mkv")
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.webm")


@register(outgoing=True, pattern=r"^\.smd (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Error: No scrobbling data found.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@SpotifyMusicDownloaderBot"
    try:
        await event.edit("`Getting Your Music`")
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Downloading...`")
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                msg = await bot.send_message(chat, track)
                respond = await response
                res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                r = await res
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Unblock `@SpotifyMusicDownloaderBot` and retry`")
                return
            await bot.forward_messages(event.chat_id, respond.message)
        await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
        await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@SpotifyMusicDownloaderBot` is not responding or Song not found!.`"
        )


@register(outgoing=True, pattern=r"^\.net (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Error: No current scrobble found.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@WooMaiBot"
    link = f"/netease {track}"
    await event.edit("`Searching...`")
    try:
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Processing... Please wait`")
            try:
                msg = await conv.send_message(link)
                response = await conv.get_response()
                respond = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Please unblock @WooMaiBot and try again`")
                return
            await event.edit("`Sending Your Music...`")
            await asyncio.sleep(3)
            await bot.send_file(event.chat_id, respond)
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, respond.id]
        )
        await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@WooMaiBot` is not responding or Song not found!.`"
        )


@register(outgoing=True, pattern=r"^\.sdd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Enter a valid link to download from`")
    else:
        await event.edit("`Processing...`")
    chat = "@MusicHuntersBot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(d_link)
                details = await conv.get_response()
                song = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@MusicHuntersBot` and retry`")
                return
            await bot.send_file(event.chat_id, song, caption=details.text)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, details.id, song.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@MusicHuntersBot` is not responding or Song not found!.`"
        )


CMD_HELP.update(
    {
        "song": ">`.song` **Artist - Song Title**"
        "\nUsage: Finding and uploading song.\n\n"
        ">`.vsong` **Artist - Song Title**"
        "\nUsage: Finding and uploading videoclip.\n\n"
        ">`.smd` **Artist - Song Title**"
        "\nUsage: Download music from spotify use `@SpotifyMusicDownloaderBot`.\n\n"
        ">`.smd now`"
        "\nUsage: Download current LastFM scrobble use `@SpotifyMusicDownloaderBot`.\n\n"
        ">`.net` **Artist - Song Title**"
        "\nUsage: Download music use `@WooMaiBot`.\n\n"
        ">`.net now`"
        "\nUsage: Download current LastFM scrobble use `@WooMaiBot`.\n\n"
        ">`.sdd <Spotify/Deezer Link>`"
        "\nUsage: Download music from Spotify or Deezer use `@MusicHuntersBot`."})
