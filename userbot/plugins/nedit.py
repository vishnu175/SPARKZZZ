from telethon import events
import io
from userbot.utils import admin_cmd
import asyncio

@borg.on(admin_cmd(pattern="nedit (.*)"))
async def dead(nedit):
	"Name Editor type-1"
	name = nedit.pattern_match.group(1)
	A = (f"✦҈͜͡➳🇮🇳{name}🇮🇳✦҈͜͡➳")
	await nedit.edit(A)


@borg.on(admin_cmd(pattern="nedit1 (.*|<> emoji)"))
async def cus(nedit1):
	w=""
	name = nedit1.pattern_match.group(1)
	for i in range(0,len(name)-1):
		ch=name[i]
		if(ch != ' '):
			w=w+ch
		else:
			break
	e=name[len(w)+1:]
	B = (f"**✦҈͜͡➳{e}{w}{e}✦҈͜͡➳**")
	await nedit1.edit(B)
