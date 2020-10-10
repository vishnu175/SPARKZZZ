# SPARKZZZ 2020 @vishnu175
import os 
import asyncio
from uniborg.util import admin_cmd
from telethon import events
from userbot.utils import admin_cmd


@sparkzzz.on(admin_cmd(pattern=r"upb"))
async def batch_upload(event):
	if event.fwd_from:
		return   
	temp_dir = Config.TMP_DOWNLOAD_DIRECTORY	
	if os.path.exists(temp_dir):    
		files = os.listdir(temp_dir)
		files.sort()
		await event.edit("Uploading Files on Telegram...")
		for file in files:
			required_file_name = temp_dir+"/"+file
			print(required_file_name)
			await borg.send_file(
					event.chat_id,
					required_file_name,
					force_document=True
				)	
	else:
		await event.edit("Directory Not Found.")
		return		
	await event.edit("Successfull.")	
