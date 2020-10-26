# CREDITS 💳 to FRIDAY
# Ported and edited for ⚡SPARKZZZ⚡ by vishnu175
# module to download youtube music
from youtubesearchpython import SearchVideos
from pytube import YouTube
import os
import wget
from userbot.SparkzzzConfig import Config
import asyncio
from userbot.utils import admin_cmd, edit_or_reply

@sparkzzz.on(admin_cmd(pattern="ymusic ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ytsearch = event.pattern_match.group(1)
    myself_sparkzzz = await edit_or_reply(event, f"`Getting {ytsearch} From Youtube Servers. Please Wait.`")
    search = SearchVideos(f"{ytsearch}", offset = 1, mode = "dict", max_results = 1)
    sr = search.result()
    ser = sr['search_result']
    ylink = ser[0]['link']
    ytitle = ylink[0]['title']
    yid = ylink[0]['id']
    ychannel = ylink[0]['channel']
    ymsc = f"https://img.youtube.com/vi/{ychannel}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir('./music/'):
        os.makedirs('./music/')
    path = Config.TMP_DOWNLOAD_DIRECTORY
    getmsc = wget.download(ymsc, out = path)
    sparkzzz = (f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k ' + ylink)
    os.system(sparkzzz)
    await asyncio.sleep(4)
    ymusi = f"./music/{ytitle}.mp3"
    if os.path.exists(ymusi):
        await myself_sparkzzz.edit("`Song 🎧 found...uploading song...plz wait.`")
    else:
        await myself_sparkzzz.edit("`SomeThing Went Wrong. Try Again After Sometime..`")
    toshow = f"**Song Name 🎼** `{ytitle}` \n**Requested For 🎧** `{ytsearch}` \n**Channel 🎞️** `{ychannel}` \n**Link 🔗** `{ylink}`" 
    await borg.send_file(event.chat_id,
                ymusi,
                force_document=False,
                allow_cache=False,
                caption=toshow,
                thumb=getmsc,
                performer=ychannel,
                supports_streaming=True) 
    await myself_sparkzzz.edit("`Song Uploaded. By ⚡SPARKZZZ⚡`")
    for files in (getmsc, ymusi):
        if files and os.path.exists(files):
            os.remove(files)
