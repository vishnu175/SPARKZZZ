from telethon import events
import asyncio
import os
import subprocess
import sys
from userbot.utils import admin_cmd
from userbot.utils import humanbytes, progress, time_formatter

@sparkzzz.on(admin_cmd(pattern=r"getc"))
async def get_media(event):
    if event.fwd_from:
        return
    dir= "./temp/"
    try:
        os.makedirs("./temp/")
    except:
    	pass
    channel_username= event.text
    command = ['ls','temp','|','wc','-l' ]
    limit = channel_username[6:9]
    print(limit)
    channel_username = channel_username[11: ]
    print(channel_username)
    await event.edit("Downloading Media From this Channel.")
    msgs = await event.client.get_messages(channel_username, limit=int(limit))
    with open('log.txt','w') as f:
    	f.write(str(msgs))
    for msg in msgs:
       if msg.media is not None:
	        await event.client.download_media(
                msg,dir)
    ps = subprocess.Popen(('ls', 'temp'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('wc', '-l'), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'","")
    output = output.replace("\n'","")
    await event.edit("Downloaded "+output+" files.")
             
                         
@sparkzzz.on(admin_cmd(pattern=r"geta"))
async def get_media(event):
    if event.fwd_from:
        return
    dir= "./temp/"
    try:
        os.makedirs("./temp/")
    except:
    	pass
    channel_username= event.text
    command = ['ls','temp','|','wc','-l' ]
    channel_username = channel_username[7:]
 
   
    print(channel_username)
    await event.edit("Downloading All Media From this Channel.")
    msgs = await event.client.get_messages(channel_username,limit=3000)
    with open('log.txt','w') as f:
    	f.write(str(msgs))
    for msg in msgs:
       if msg.media is not None:
	        await event.client.download_media(
                msg,dir)          
    ps = subprocess.Popen(('ls', 'temp'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('wc', '-l'), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'","")
    output = output.replace("\n'","")
    await event.edit("Downloaded "+output+" files.")
             
