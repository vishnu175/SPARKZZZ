"""Find Movies Fast"""
# Made by- @DeletedUser420 idea- @AnInnocentboy and then kanged by me
# Ported by @buddhhu

from typing import Tuple, Optional
from telethon.tl.types import InputMessagesFilterVideo
from userbot.utils import admin_cmd

def get_file_id_and_ref(message) -> Tuple[Optional[str], Optional[str]]:
    """ get file_id and file_ref """
    file_ = message.audio or message.photo \
        or message.sticker or message.voice or message.video_note \
        or message.video or message.document
    if file_:
        return file_.id, file_.file_reference
    return None, None

@borg.on(admin_cmd(pattern="movie (.*)"))
async def movie_search(event):
    """get movie from channel"""
    movie = event.pattern_match.group(1)
    if not movie:
        await event.reply("Provide a movie name")
        return
    search = await event.reply("♥ __Searching For__ **{}**".format(movie))
    chat_id = event.chat_id
    f_id = ""
    f_ref = ""
    async for msg in event.client.iter_messages(-1001176164495, search=movie,  limit=2, filter=InputMessagesFilterVideo):
    	f_id, f_ref = get_file_id_and_ref(msg)
    	if not (f_id or f_ref):
    		await search.edit("♡ Movie Not Found !")
    		return
    caption = movie
    await event.client.send_file(chat_id, msg, caption=caption, supports_streaming=True)
    await search.delete()
