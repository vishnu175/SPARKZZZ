

import requests
import asyncio
import random
import re
import time
import sys
import os
from os import remove, execl
from datetime import datetime
from collections import deque
from contextlib import suppress
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon import events
import git
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from userbot import bot, ALIVE_NAME
from userbot.utils import admin_cmd
from heroku_config import Var as Config

# -- Constants -- #
OFFICIAL_UPSTREAM_REPO = "https://github.com/vishnu175/SPARKZZZ"
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
DELETE_TIMEOUT = 4
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"
# -- Constants End -- #


@sparkzzz.on(admin_cmd("update ?(.*)", outgoing=True))
async def updater(upd):
    "For .update command, check if the bot is up to date, update if specified"
    await upd.edit('**Ricerca update in corso....**')

    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote('updater', OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != 'master':
        await upd.edit(
            f'**[UPDATER]: Sembra che stai utilizzando un ramo custom** {active_branch_name}.'
            '**in tal caso, Updater è in grado di identificare**'
            '**quale ramo deve essere unito.**'
            '**Per favore checkout a qualsiasi branch ufficiale**')
        repo.__del__()
        return

    try:
        repo.create_remote('updater', OFFICIAL_UPSTREAM_REPO)
    except BaseException as e:
        print(e)
        pass

    upd_rem = repo.remote('updater')
    upd_rem.fetch(active_branch_name)

    changelog = await gen_chlog(repo, f'HEAD..updater/{active_branch_name}')

    if not changelog:
        await upd.edit(
            f'\n{DEFAULTUSER} è **AGGIORNATO**\n')
        repo.__del__()
        await asyncio.sleep(DELETE_TIMEOUT)
        await upd.delete()
        return

    changelog_str = f'**New UPDATE trovato per** {DEFAULTUSER}\n\n**CHANGELOG:**\n {changelog}'
    if len(changelog_str) > 4095:
        await upd.edit('**Il changelog delle modifiche è troppo grande,leggi il file.**')
        file = open("change.txt", "w+")
        file.write(changelog_str)
        file.close()
        await bot.client.send_file(
            upd.chat_id,
            "change.txt",
            reply_to=upd.id,
        )
        os.remove("change.txt")
    else:
        await upd.edit(changelog_str)

    upd_rem.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if Var.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Var.HEROKU_APP_NAME is not None:
                heroku_app = None
                for app in heroku_applications:
                    if app.name == Var.HEROKU_APP_NAME:
                        heroku_app = app
                if heroku_app is None:
                    await upd.edit('**Invalid APP Name. Inserisci il nome del bot nella Var `HEROKU_APP_NAME.**')
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://",
                    "https://api:" + Var.HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(deploy_start(bot, upd, HEROKU_GIT_REF_SPEC, remote))

            else:
                await upd.edit('**Crea la Var `HEROKU_APP_NAME` e inserisci il nome del bot in heroku come value.**')
                return
        else:
            await upd.edit('**Nessuna app heroku,trovata**')
    else:
        await upd.edit('**Nessuna API KEY trovata nella Var `HEROKU_API_KEY**')
        

async def gen_chlog(repo, diff_marker):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff_marker):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log

async def deploy_start(bot, upd, refspec, remote):
    await upd.edit('**Update in corso...\nAttendi 5 minuti e premi `.alive`**')
    await remote.push(refspec=refspec)
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)

