 
#© SPARKZZZ
# Kangers plz keep credits





import asyncio 
from telethon import events
from userbot.utils import admin_cmd
from platform import uname
from userbot import ALIVE_NAME


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"




 @borg.on(admin_cmd(pattern="tspb  (.*)"))
 async def survivor(spb):
    name = spb.pattern_match.group(1)
    V = (f"**Tribute to SPB  from ➥ {name} .\n\n**"
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠉⠉⠹⠿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡟⠹⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⡿⢧⣤⡤⢋⡴⠶⢶⣦⡄⠀⠀⠀⠀⣀⣀⣾⣿⣿⣿⣿\n"
            "⣿⣿⠉⢹⡷⢸⠏⠁⠀⠀⠀⠈⠁⠀⠃⠀⠓⠋⢽⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⡀⠀⠀⠈⠀⠀⠀⠀⡠⠈⠠⠤⣀⣀⣀⢄⠀⠀⢠⣿⣿⣿⣿\n"
            "⣿⣿⣇⣤⠀⠀⠀⠀⠀⠺⢶⠿⠓⠉⠉⢿⣿⣤⡆⠀⣼⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠈⠀⠀⠀⠰⡟⠙⠃⠀⣿⣿⣿⣿⣿\n"
            "⡿⠿⠿⢿⣿⣿⣿⣆⠀⢄⠀⠀⠀⠀⠀⠀⢁⡀⣠⣾⣿⣿⣿⣿⣿\n"
⠀⠀       "     ⠀⠀⠉⠻⣿⣿⣷⣄⠑⢶⣦⣦⣤⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿\n"
⠀⠀⠀    "              ⠀⠈⠻⢿⣿⣿⣶⣿⣿⣿⣿⣿⣿⡿⠛⠛⠻⠿⣿⣿\n"
⠀⠀⠀ ⠀"⠀⠀            ⠀⠀⠈⠻⢷⣾⠿⠿⢿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠉\n"


     await  spb.edit(V)
